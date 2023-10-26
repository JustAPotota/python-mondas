import hashlib
import os
import struct
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Optional, Self

class _Reader:
    _stream: BytesIO

    def __init__(self, data: bytes) -> None:
        self._stream = BytesIO(data)
    
    def long(self) -> int:
        return struct.unpack(">q", self._stream.read(8))[0]
    
    def skip(self, amount: int) -> None:
        self._stream.seek(amount, os.SEEK_CUR)

    def seek(self, offset: int) -> None:
        self._stream.seek(offset)

    def bytes(self, amount: int) -> bytes:
        return self._stream.read(amount)

    def int(self) -> int:
        return struct.unpack(">I", self._stream.read(4))[0]
    
class _Writer:
    _stream: BytesIO

    def __init__(self) -> None:
        self._stream = BytesIO()

    def long(self, long: int) -> None:
        self._stream.write(struct.pack(">q", long))
    
    def skip(self, amount: int) -> None:
        self._stream.seek(amount, os.SEEK_CUR)

    def seek(self, offset: int) -> None:
        self._stream.seek(offset, os.SEEK_SET)

    def rewind(self) -> None:
        self._stream.seek(0)

    def current_offset(self) -> int:
        return self._stream.tell()

    def read(self) -> bytes:
        return self._stream.read()

    def bytes(self, bytes: bytes) -> None:
        self._stream.write(bytes)

    def int(self, int: int) -> None:
        self._stream.write(struct.pack(">I", int))

@dataclass
class IndexEntry:
    offset: int
    size: int
    compressed_size: int
    hash: bytes
    flags: int

@dataclass
class ArchiveIndex:
    version: int
    hash_length: int
    entries: list[IndexEntry]
    _userdata: int
    md5: bytes

    @classmethod
    def from_file(cls, path: Path) -> Self:
        return cls.from_bytes(path.read_bytes())
    
    def write_to_file(self, path: Path) -> None:
        path.write_bytes(self.into_bytes())
    
    @classmethod
    def from_bytes(cls, bytes: bytes) -> Self:
        reader = _Reader(bytes)

        version = reader.int()
        reader.skip(4)
        userdata = reader.long()
        entry_count = reader.int()
        entries_offset = reader.int()
        hashes_offest = reader.int()
        hash_length = reader.int()
        md5 = reader.bytes(16)

        hashes = []
        for i in range(entry_count):
            reader.seek(hashes_offest + i * 64)
            hashes.append(reader.bytes(hash_length))
        
        entries = []
        reader.seek(entries_offset)
        for i in range(entry_count):
            offset = reader.int()
            size = reader.int()
            compressed_size = reader.int()
            flags = reader.int()

            entries.append(IndexEntry(offset, size, compressed_size, hashes[i], flags))

        return cls(version, hash_length, entries, userdata, md5)
    
    def into_bytes(self) -> bytes:
        writer = _Writer()

        header_length = 4 + 4 + 8 + 16 + 16
        writer.skip(header_length)
        for entry in self.entries:
            writer.bytes(entry.hash)
            writer.skip(64 - self.hash_length)

        entries_offset = writer.current_offset()
        for entry in self.entries:
            writer.int(entry.offset)
            writer.int(entry.size)
            writer.int(entry.compressed_size)
            writer.int(entry.flags)

        writer.seek(header_length)
        md5 = hashlib.md5(writer.read()).digest()

        writer.rewind()
        writer.int(self.version)
        writer.int(0)
        writer.long(self._userdata)
        writer.int(len(self.entries))
        writer.int(entries_offset)
        writer.int(header_length)
        writer.int(self.hash_length)
        writer.bytes(md5)

        self.md5 = md5

        writer.rewind()
        return writer.read()
    
    def find_entry(self, hash: bytes) -> Optional[IndexEntry]:
        for entry in self.entries:
            if entry.hash == hash:
                return entry