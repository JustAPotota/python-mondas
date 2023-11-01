import v4
import v5
import json
import os
import re
import requests
import shutil
from argparse import ArgumentParser
from configparser import ConfigParser
from dataclasses import dataclass
from datetime import date, datetime, time, timezone
from enum import Enum
from io import BytesIO, BufferedReader
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict, List, Optional, Self, Tuple
from zipfile import ZipFile

@dataclass
class ExtensionVersion:
    date: datetime
    url: str

    @classmethod
    def from_strings(cls, date: str, url: str) -> Optional[Self]:
        try:
            return cls(datetime.fromisoformat(date), url)
        except ValueError:
            return

@dataclass
class Extension:
    symbol: bytes
    repo: str
    versions: list[ExtensionVersion]

    @classmethod
    def from_strings(cls, symbol: str, repo: str, versions: list[dict[str, str]]) -> Self:
        versions = [ExtensionVersion.from_strings(**version) for version in versions]
        versions = [version for version in versions if version is not None]
        return cls(symbol.encode(), repo, versions)
    
    def is_used(self, executable: bytes) -> bool:
        return executable.find(self.symbol) != -1
    
    def get_latest_version(self, before: datetime) -> Optional[ExtensionVersion]:
        for version in self.versions:
            if version.date <= before:
                return version

class DefoldChannel(Enum):
    Alpha = "alpha"
    Beta = "beta"
    Stable = "stable"

@dataclass
class DefoldVersion:
    number: Tuple[int, int, int]
    channel: DefoldChannel
    sha: str
    date: datetime

    @classmethod
    def from_strings(cls, name: str, sha: str, date: str) -> Optional[Self]:
        match = re.search("(\\d+)\\.(\\d+)\\.(\\d+)-?(alpha|beta)?", name)
        if match is None:
            return
        
        groups = match.groups(default="stable")
        
        try:
            x = int(groups[0])
            y = int(groups[1])
            z = int(groups[2])
            channel = DefoldChannel(groups[3])
            return cls((x,y,z), channel, sha, datetime.fromisoformat(date))
        except ValueError:
            return
        
    def __repr__(self) -> str:
        return f"{self.number[0]}.{self.number[1]}.{self.number[2]}-{self.channel.value} ({self.sha})"

def upgrade_index(index: v4.ArchiveIndex) -> v5.ArchiveIndex:
    index.version = 5
    return index

def upgrade_manifest(path: Path, output: Path, index: v5.ArchiveIndex):
    # Load old manifest
    old_manifest_file = v4.ManifestFile()
    old_manifest_file.ParseFromString(path.read_bytes())
    old_manifest_data = v4.ManifestData()
    old_manifest_data.ParseFromString(old_manifest_file.data)

    # Create new manifest file
    new_manifest_file = v5.ManifestFile()
    new_manifest_file.version = 5
    new_manifest_file.signature = old_manifest_file.signature
    new_manifest_file.archive_identifier = old_manifest_file.archive_identifier

    # Create new manfiest data
    new_manifest_data = v5.ManifestData()

    # Set header
    new_manifest_data.header.resource_hash_algorithm = old_manifest_data.header.resource_hash_algorithm
    new_manifest_data.header.signature_hash_algorithm = old_manifest_data.header.signature_hash_algorithm
    new_manifest_data.header.signature_sign_algorithm = old_manifest_data.header.signature_sign_algorithm
    new_manifest_data.header.project_identifier.data = old_manifest_data.header.project_identifier.data

    # Set engine versions
    for old_engine_version in old_manifest_data.engine_versions:
        new_engine_version = v5.HashDigest()
        new_engine_version.data = old_engine_version.data
        new_manifest_data.engine_versions.append(new_engine_version)

    # Set resources
    for old_resource in old_manifest_data.resources:
        new_resource = v5.ResourceEntry()
        new_resource.hash.data = old_resource.hash.data
        new_resource.url = old_resource.url
        new_resource.url_hash = old_resource.url_hash
        for old_dependant in old_resource.dependants:
            new_resource.dependants.append(old_dependant)

        # v5 manifest resources now include some data from the index
        index_entry = index.find_entry(new_resource.hash.data)
        if index_entry is None:
            raise Exception(f"Entry for {new_resource.url} not found")
        
        new_resource.size = index_entry.size
        new_resource.compressed_size = index_entry.compressed_size
        new_resource.flags = old_resource.flags
        new_resource.flags |= (index_entry.flags & 0b01) << 2
        new_resource.flags |= (index_entry.flags & 0b10) << 3

        new_manifest_data.resources.append(new_resource)

    new_manifest_file.data = new_manifest_data.SerializeToString()
    output.write_bytes(new_manifest_file.SerializeToString())

def load_extensions(json_path: Path) -> list[Extension]:
    with open(json_path, "r") as file:
        return [Extension.from_strings(**extension) for extension in json.load(file)]

def load_defold_versions(json_path: Path) -> list[DefoldVersion]:
    with open(json_path, "r") as file:
        versions = [DefoldVersion.from_strings(**version) for version in json.load(file)]
        return [version for version in versions if version is not None]

def get_engine_version(executable_path: Path, versions: list[DefoldVersion]) -> Optional[DefoldVersion]:
    with open(executable_path, "rb") as file:
        contents = file.read()
        for version in versions:
            if contents.find(version.sha.encode()) != -1:
                return version

def get_missing_elements(l: list) -> Optional[list[int]]:
    missing = [i for i in range(len(l)) if l[i] is None]
    return missing if len(missing) > 0 else None

def get_config_file_name(zip: ZipFile) -> str:
    filtered = [
        file_name for file_name in zip.namelist() if file_name.endswith("game.project")]
    return filtered[0]

def get_root_name(zip: ZipFile) -> str:
    match = re.match(".+?/", zip.namelist()[0])
    if match is None:
        return ""
    return match.group()

def get_include_dir(zip: ZipFile) -> str:
    file_name = get_config_file_name(zip)
    with zip.open(file_name) as contents:
        config = ConfigParser()
        config.read_string(contents.read().decode())
        return config["library"]["include_dirs"]

def extract_library_dir(zip: ZipFile, path: Path):
    root_name = get_root_name(zip)
    include_dir = get_include_dir(zip)
    full_include_dir_name = root_name + include_dir + "/"
    library_files = [info for info in zip.infolist(
    ) if not info.is_dir() and info.filename.startswith(full_include_dir_name)]

    for library_file in library_files:
        library_file.filename = library_file.filename.removeprefix(
            root_name)
        zip.extract(library_file, path)

def download_extract_zips(path: Path, urls: list[str]):
    for url in urls:
        print(f"Downloading {url}...")
        response = requests.get(url)
        if not response.ok:
            raise Exception(response.text)
        with ZipFile(BytesIO(response.content)) as zip:
            extract_library_dir(zip, path)

def open_all(base_path: str, paths: list[Path]) -> dict[str, BufferedReader]:
    files_dict = {}
    for path in paths:
        name = os.path.splitroot(str(path)[len(base_path):])[2]
        files_dict[name] = open(path, "rb")
    return files_dict

def get_all_file_names(path: Path) -> list[Path]:
    all = path.rglob("*")
    files = [path for path in all if path.is_file()]
    return files

def save_executable(zip: ZipFile, path: Path, platform: str):
    filename = "dmengine" if platform == "x86_64-linux" else "dmengine.exe"
    with zip.open(filename, "r") as source:
        with open(path, "wb") as dest:
            dest.write(source.read())

def upgrade_executable(path: Path, to_version: DefoldVersion, platform: str, release_date: datetime, available_extensions: List[Extension]):
    contents = path.read_bytes()
    used_extensions = list(filter(lambda extension: extension.is_used(contents), available_extensions))
    print("Extensions used:")
    for extension in used_extensions:
        print(f"- {extension.repo}")
    extension_versions = [extension.get_latest_version(release_date) for extension in used_extensions]
    missing = get_missing_elements(extension_versions)
    if missing is not None:
        print("Unable to find valid versions for:")
        for i in missing:
            print(f"- {used_extensions[i].repo}")
        return
    
    extension_urls = [version.url for version in extension_versions]
    with TemporaryDirectory() as tmp:
        download_extract_zips(Path(tmp), extension_urls)
        files = open_all(tmp, get_all_file_names(Path(tmp)))
        print("Building...")
        response = requests.post(f"https://build.defold.com/build/{platform}/{to_version.sha}", files=files)
        if not response.ok:
            raise Exception(response.text)
        with ZipFile(BytesIO(response.content)) as zip:
            save_executable(zip, path, platform)
            path.chmod(755)

def needs_updating(version: DefoldVersion) -> bool:
    return version.number[1] < 5

def main(executable_path: Path, release_date: Optional[date], platform: str):
    versions = load_defold_versions(Path("defold_versions.json"))
    to_version = next(version for version in versions if version.number == (1, 5, 0))
    extensions = load_extensions(Path("extension_versions.json"))
    current_version = get_engine_version(executable_path, versions)
    if current_version is None:
        return print("Unable to determine the engine version used")
    print(f"Detected engine version {current_version}")
    if not needs_updating(current_version):
        return print("This game already supports the new liveupdate system")
    
    game_path = executable_path.resolve().parent
    index_path = game_path / "game.arci"
    manifest_path = game_path / "game.dmanifest"

    with TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        index = v4.ArchiveIndex.from_file(index_path)
        index = upgrade_index(index)
        index.write_to_file(tmp / "game.arci")
        print("Upgraded index file")
        upgrade_manifest(manifest_path, tmp / "game.dmanifest", index)
        print("Upgraded manifest file")

        if release_date is None:
            upgrade_executable(executable_path, to_version, platform, current_version.date, extensions)
        else:
            upgrade_executable(executable_path, to_version, platform, datetime.combine(release_date, time()).astimezone(), extensions)
        print("Upgraded executable")

        shutil.move(tmp / "game.arci", index_path)
        shutil.move(tmp / "game.dmanifest", manifest_path)
        print("Upgrade complete!")

def parse_datetime(s: str) -> datetime:
    return datetime.strptime(s, "%d/%m/%Y")

if __name__ == "__main__":
    parser = ArgumentParser(description="Upgrade a Defold game to engine version 1.5.0")
    parser.add_argument("exe", type=Path, help="Path to the game executable")
    parser.add_argument("-d", "--release-date", type=parse_datetime, help="Release date of the game in DD/MM/YYYY format. Setting this will usually provide much better results")
    parser.add_argument("-p", "--platform", help="Platform the game is built for", choices=["x86_64-linux", "x86_64-windows"], required=True)
    args = parser.parse_args()
    main(args.exe, args.release_date, args.platform)