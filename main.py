import v4
import v5
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

def build_hash_table(index: v5.ArchiveIndex) -> dict[bytes, v5.ArchiveIndex.Entry]:
    out = {}
    for i in range(len(index.entries)):
        entry = index.entries[i]
        hash = index.hashes[i]
        out[hash] = entry
    return out

def upgrade_index(index: v4.ArchiveIndex) -> v5.ArchiveIndex:
    return index

def upgrade_manifest(path: Path, hash_table: dict[bytes, v5.ArchiveIndex.Entry]):
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
    new_manifest_data.header.project_identifier = old_manifest_data.header.project_identifier

    # Set engine versions
    new_manifest_data.engine_versions = old_manifest_data.engine_versions

    # Set resources
    for old_resource in old_manifest_data.resources:
        new_resource = v5.ResourceEntry()
        new_resource.hash.data = old_resource.hash.data
        new_resource.url = old_resource.url
        new_resource.url_hash = old_resource.url_hash

        index_entry = hash_table[new_resource.hash.data]
        new_resource.size = index_entry.size
        new_resource.compressed_size = index_entry.compressed_size
        new_resource.flags = old_resource.flags
        new_resource.flags |= (index_entry.encrypted << 2)
        new_resource.flags |= (index_entry.compressed << 3)
        new_resource.dependants = old_resource.dependants

        new_manifest_data.resources.append(new_resource)

    new_manifest_file.data = new_manifest_data.SerializeToString()
    path.write_bytes(new_manifest_file.SerializeToString())



def main(game_path: Path):
    index_path = game_path / "game.arci"
    manifest_path = game_path / "game.dmanifest"

    index = v4.ArchiveIndex.from_file(index_path)
    index = upgrade_index(index)
    hash_table = build_hash_table(index)
    upgrade_manifest(manifest_path, hash_table)

if __name__ == "__main__":
    main(Path(sys.argv[1]))