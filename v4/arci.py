# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Arci(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Arci.Header(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_u4be()
            self.padding = self._io.read_bytes(12)
            self.entry_count = self._io.read_u4be()
            self.entries_offset = self._io.read_u4be()
            self.hashes_offset = self._io.read_u4be()
            self.hash_length = self._io.read_u4be()
            self.md5 = self._io.read_bytes(16)


    class Entry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.offset = self._io.read_u4be()
            self.size = self._io.read_u4be()
            self.compressed_size = self._io.read_u4be()
            self.unused_flags = self._io.read_bits_int_be(29)
            self.liveupdate = self._io.read_bits_int_be(1) != 0
            self.compressed = self._io.read_bits_int_be(1) != 0
            self.encrypted = self._io.read_bits_int_be(1) != 0


    @property
    def entries(self):
        if hasattr(self, '_m_entries'):
            return self._m_entries

        _pos = self._io.pos()
        self._io.seek(self.header.entries_offset)
        self._m_entries = []
        for i in range(self.header.entry_count):
            self._m_entries.append(Arci.Entry(self._io, self, self._root))

        self._io.seek(_pos)
        return getattr(self, '_m_entries', None)

    @property
    def hashes(self):
        if hasattr(self, '_m_hashes'):
            return self._m_hashes

        _pos = self._io.pos()
        self._io.seek(self.header.hashes_offset)
        self._m_hashes = []
        for i in range(self.header.entry_count):
            self._m_hashes.append(self._io.read_bytes(self.header.hash_length))

        self._io.seek(_pos)
        return getattr(self, '_m_hashes', None)


