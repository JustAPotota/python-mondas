import v4
import v5
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict, List, Optional, Self, Tuple

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
    
@dataclass
class Extension:
    symbol: bytes
    repo: str

EXTENSIONS = [
    Extension(b"STEAMWORKS", "britzl/steamworks-defold"),
    Extension(b"DAABBCC", "selimanac/DAABBCC"),
    Extension(b"DEFOS", "subsoap/defos")
]

def upgrade_index(index: v4.ArchiveIndex) -> v5.ArchiveIndex:
    index.version = 5
    return index

def upgrade_manifest(path: Path, index: v5.ArchiveIndex):
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
    path.write_bytes(new_manifest_file.SerializeToString())

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
            
def native_extensions_used(executable_path: Path, available_extensions: List[Extension]) -> List[Extension]:
    pass

def upgrade_executable(path: Path, current_version: DefoldVersion):
    pass

def needs_updating(version: DefoldVersion) -> bool:
    return version.number[1] < 5

def main(executable_path: Path):
    versions = load_defold_versions(Path("defold_versions.json"))
    current_version = get_engine_version(executable_path, versions)
    if current_version is None:
        return print("Unable to determine the engine version used")
    print(f"Detected engine version {current_version}")
    if not needs_updating(current_version):
        return print("This game already supports the new liveupdate system")
    
    game_path = executable_path.resolve().parent
    index_path = game_path / "game.arci"
    manifest_path = game_path / "game.dmanifest"

    index = v4.ArchiveIndex.from_file(index_path)
    index = upgrade_index(index)
    index.write_to_file(index_path)
    upgrade_manifest(manifest_path, index)
    upgrade_executable(executable_path, current_version)

if __name__ == "__main__":
    main(Path(sys.argv[1]))