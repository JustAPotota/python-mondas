meta:
  id: arci
  file-extension: arci
  endian: be
seq:
  - id: header
    type: header
instances:
  entries:
    pos: header.entries_offset
    type: entry
    repeat: expr
    repeat-expr: header.entry_count
  hashes:
    pos: header.hashes_offset
    size: header.hash_length
    repeat: expr
    repeat-expr: header.entry_count
types:
  header:
    seq:
      - id: version
        type: u4
      - id: padding
        size: 12
      - id: entry_count
        type: u4
      - id: entries_offset
        type: u4
      - id: hashes_offset
        type: u4
      - id: hash_length
        type: u4
      - id: md5
        size: 16
  entry:
    seq:
      - id: offset
        type: u4
      - id: size
        type: u4
      - id: compressed_size
        type: u4
      - id: unused_flags
        type: b29
      - id: liveupdate
        type: b1
      - id: compressed
        type: b1
      - id: encrypted
        type: b1