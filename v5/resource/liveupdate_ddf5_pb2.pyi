from ddf import ddf_extensions_pb2 as _ddf_extensions_pb2
from ddf import ddf_math_pb2 as _ddf_math_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    HASH_UNKNOWN: _ClassVar[HashAlgorithm]
    HASH_MD5: _ClassVar[HashAlgorithm]
    HASH_SHA1: _ClassVar[HashAlgorithm]
    HASH_SHA256: _ClassVar[HashAlgorithm]
    HASH_SHA512: _ClassVar[HashAlgorithm]

class SignAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SIGN_UNKNOWN: _ClassVar[SignAlgorithm]
    SIGN_RSA: _ClassVar[SignAlgorithm]

class ResourceEntryFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BUNDLED: _ClassVar[ResourceEntryFlag]
    EXCLUDED: _ClassVar[ResourceEntryFlag]
    ENCRYPTED: _ClassVar[ResourceEntryFlag]
    COMPRESSED: _ClassVar[ResourceEntryFlag]
HASH_UNKNOWN: HashAlgorithm
HASH_MD5: HashAlgorithm
HASH_SHA1: HashAlgorithm
HASH_SHA256: HashAlgorithm
HASH_SHA512: HashAlgorithm
SIGN_UNKNOWN: SignAlgorithm
SIGN_RSA: SignAlgorithm
BUNDLED: ResourceEntryFlag
EXCLUDED: ResourceEntryFlag
ENCRYPTED: ResourceEntryFlag
COMPRESSED: ResourceEntryFlag

class HashDigest(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ManifestHeader(_message.Message):
    __slots__ = ["resource_hash_algorithm", "signature_hash_algorithm", "signature_sign_algorithm", "project_identifier"]
    RESOURCE_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_SIGN_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    resource_hash_algorithm: HashAlgorithm
    signature_hash_algorithm: HashAlgorithm
    signature_sign_algorithm: SignAlgorithm
    project_identifier: HashDigest
    def __init__(self, resource_hash_algorithm: _Optional[_Union[HashAlgorithm, str]] = ..., signature_hash_algorithm: _Optional[_Union[HashAlgorithm, str]] = ..., signature_sign_algorithm: _Optional[_Union[SignAlgorithm, str]] = ..., project_identifier: _Optional[_Union[HashDigest, _Mapping]] = ...) -> None: ...

class ResourceEntry(_message.Message):
    __slots__ = ["hash", "url", "url_hash", "size", "compressed_size", "flags", "dependants"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    URL_HASH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    DEPENDANTS_FIELD_NUMBER: _ClassVar[int]
    hash: HashDigest
    url: str
    url_hash: int
    size: int
    compressed_size: int
    flags: int
    dependants: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hash: _Optional[_Union[HashDigest, _Mapping]] = ..., url: _Optional[str] = ..., url_hash: _Optional[int] = ..., size: _Optional[int] = ..., compressed_size: _Optional[int] = ..., flags: _Optional[int] = ..., dependants: _Optional[_Iterable[int]] = ...) -> None: ...

class ManifestData(_message.Message):
    __slots__ = ["header", "engine_versions", "resources"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENGINE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    header: ManifestHeader
    engine_versions: _containers.RepeatedCompositeFieldContainer[HashDigest]
    resources: _containers.RepeatedCompositeFieldContainer[ResourceEntry]
    def __init__(self, header: _Optional[_Union[ManifestHeader, _Mapping]] = ..., engine_versions: _Optional[_Iterable[_Union[HashDigest, _Mapping]]] = ..., resources: _Optional[_Iterable[_Union[ResourceEntry, _Mapping]]] = ...) -> None: ...

class ManifestFile(_message.Message):
    __slots__ = ["data", "signature", "archive_identifier", "version"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    signature: bytes
    archive_identifier: bytes
    version: int
    def __init__(self, data: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., archive_identifier: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...
