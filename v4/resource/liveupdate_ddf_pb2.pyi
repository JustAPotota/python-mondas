"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _HashAlgorithm:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HashAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HashAlgorithm.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HASH_UNKNOWN: _HashAlgorithm.ValueType  # 0
    HASH_MD5: _HashAlgorithm.ValueType  # 1
    HASH_SHA1: _HashAlgorithm.ValueType  # 2
    HASH_SHA256: _HashAlgorithm.ValueType  # 3
    HASH_SHA512: _HashAlgorithm.ValueType  # 4

class HashAlgorithm(_HashAlgorithm, metaclass=_HashAlgorithmEnumTypeWrapper):
    """
    This enum specifies the supported hashing algorithms both for resource
    verification and signature generation.

    The HASH_UNKNOWN value is used as a default that cannot be used to create
    a manifest. This forces every call to explicitly specify the hashing
    algorithm in order to avoid accidentally downgrading the strength of a hash
    or unnecessarily using a too expensive hash.
    """

HASH_UNKNOWN: HashAlgorithm.ValueType  # 0
HASH_MD5: HashAlgorithm.ValueType  # 1
HASH_SHA1: HashAlgorithm.ValueType  # 2
HASH_SHA256: HashAlgorithm.ValueType  # 3
HASH_SHA512: HashAlgorithm.ValueType  # 4
global___HashAlgorithm = HashAlgorithm

class _SignAlgorithm:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SignAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SignAlgorithm.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SIGN_UNKNOWN: _SignAlgorithm.ValueType  # 0
    SIGN_RSA: _SignAlgorithm.ValueType  # 1

class SignAlgorithm(_SignAlgorithm, metaclass=_SignAlgorithmEnumTypeWrapper):
    """
    This enum specifies the supported encryption algorithms used for signature
    generation.

    The SIGN_UNKNOWN value is used as a default that cannot be used to create
    a manifest. This forces every call to explicitly specify the encryption
    algorithm.
    """

SIGN_UNKNOWN: SignAlgorithm.ValueType  # 0
SIGN_RSA: SignAlgorithm.ValueType  # 1
global___SignAlgorithm = SignAlgorithm

class _ResourceEntryFlag:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ResourceEntryFlagEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResourceEntryFlag.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    BUNDLED: _ResourceEntryFlag.ValueType  # 1
    EXCLUDED: _ResourceEntryFlag.ValueType  # 2

class ResourceEntryFlag(_ResourceEntryFlag, metaclass=_ResourceEntryFlagEnumTypeWrapper):
    """
    Enum flag on manifest resource entry
    """

BUNDLED: ResourceEntryFlag.ValueType  # 1
EXCLUDED: ResourceEntryFlag.ValueType  # 2
global___ResourceEntryFlag = ResourceEntryFlag

@typing_extensions.final
class HashDigest(google.protobuf.message.Message):
    """
    Stores a hashdigest
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    def __init__(
        self,
        *,
        data: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___HashDigest = HashDigest

@typing_extensions.final
class ManifestHeader(google.protobuf.message.Message):
    """
    The manifest header specifies general information about the manifest.

    - magic_number             : An identifier used to uniquely a manifest
    - version                  : The version of the manifest format
    - resource_hash_algorithm  : The algorithm that should be used when hashing
                                 resources
    - signature_hash_algorithm : The algorithm that should be used when hashing
                                 content for signature verification
    - signature_sign_algorithm : The algorithm that should be used for
                                 encryption and decryption for signature
                                 verification
    - project_identifier       : An identifier meant to uniquely identify a
                                 project to avoid loading a manifest for a
                                 different project. This is implemented as the
                                 SHA-1 hash of the project title
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAGIC_NUMBER_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    RESOURCE_HASH_ALGORITHM_FIELD_NUMBER: builtins.int
    SIGNATURE_HASH_ALGORITHM_FIELD_NUMBER: builtins.int
    SIGNATURE_SIGN_ALGORITHM_FIELD_NUMBER: builtins.int
    PROJECT_IDENTIFIER_FIELD_NUMBER: builtins.int
    magic_number: builtins.int
    version: builtins.int
    resource_hash_algorithm: global___HashAlgorithm.ValueType
    signature_hash_algorithm: global___HashAlgorithm.ValueType
    signature_sign_algorithm: global___SignAlgorithm.ValueType
    @property
    def project_identifier(self) -> global___HashDigest: ...
    def __init__(
        self,
        *,
        magic_number: builtins.int | None = ...,
        version: builtins.int | None = ...,
        resource_hash_algorithm: global___HashAlgorithm.ValueType | None = ...,
        signature_hash_algorithm: global___HashAlgorithm.ValueType | None = ...,
        signature_sign_algorithm: global___SignAlgorithm.ValueType | None = ...,
        project_identifier: global___HashDigest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["magic_number", b"magic_number", "project_identifier", b"project_identifier", "resource_hash_algorithm", b"resource_hash_algorithm", "signature_hash_algorithm", b"signature_hash_algorithm", "signature_sign_algorithm", b"signature_sign_algorithm", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["magic_number", b"magic_number", "project_identifier", b"project_identifier", "resource_hash_algorithm", b"resource_hash_algorithm", "signature_hash_algorithm", b"signature_hash_algorithm", "signature_sign_algorithm", b"signature_sign_algorithm", "version", b"version"]) -> None: ...

global___ManifestHeader = ManifestHeader

@typing_extensions.final
class ResourceEntry(google.protobuf.message.Message):
    """
    An entry that is produced for each resource that is part of the manifest.

    - url                      : The URL that is used by the engine to identify
                                 a resource
    - hash                     : The hash of the resource data. This is used to
                                 index each resource in the archive with their
                                 actual hash.
    - dependants               : A list of resources (hashes) that are required
                                 to load the current resource. A Collection that
                                 is childed to a CollectionProxy is not
                                 considered a dependant since it is not required
                                 to load the parent Collection of the
                                 CollectionProxy.
    - flags                    : How this resources is stored. Is used for manifest
                                 verification to determine if a resource is expected
                                 to be in the bundle or not.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    URL_HASH_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    DEPENDANTS_FIELD_NUMBER: builtins.int
    FLAGS_FIELD_NUMBER: builtins.int
    url: builtins.str
    url_hash: builtins.int
    @property
    def hash(self) -> global___HashDigest: ...
    @property
    def dependants(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    flags: builtins.int
    """ResourceEntryFlag"""
    def __init__(
        self,
        *,
        url: builtins.str | None = ...,
        url_hash: builtins.int | None = ...,
        hash: global___HashDigest | None = ...,
        dependants: collections.abc.Iterable[builtins.int] | None = ...,
        flags: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["flags", b"flags", "hash", b"hash", "url", b"url", "url_hash", b"url_hash"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dependants", b"dependants", "flags", b"flags", "hash", b"hash", "url", b"url", "url_hash", b"url_hash"]) -> None: ...

global___ResourceEntry = ResourceEntry

@typing_extensions.final
class ManifestData(google.protobuf.message.Message):
    """
    The manifest data that contains all information about the project.

    - header                   : The manifest header
    - engine_versions          : A list of engine versions (specified by their
                                 hash and same as sys.engine_info) that are able
                                 to support the manifest. An engine should only
                                 attempt to initialize with a manifest that has
                                 that version of the engine listed as a
                                 supported engine.
    - resources                : The resources that are part of the manifest.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEADER_FIELD_NUMBER: builtins.int
    ENGINE_VERSIONS_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___ManifestHeader: ...
    @property
    def engine_versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HashDigest]: ...
    @property
    def resources(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceEntry]: ...
    def __init__(
        self,
        *,
        header: global___ManifestHeader | None = ...,
        engine_versions: collections.abc.Iterable[global___HashDigest] | None = ...,
        resources: collections.abc.Iterable[global___ResourceEntry] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header", b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["engine_versions", b"engine_versions", "header", b"header", "resources", b"resources"]) -> None: ...

global___ManifestData = ManifestData

@typing_extensions.final
class ManifestFile(google.protobuf.message.Message):
    """
    The Manifest. This is separate from ManifestData to easily create a
    signature of the manifest content. Nothing other than a single ManifestData
    entry and a single signature should be part of this entity.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    SIGNATURE_FIELD_NUMBER: builtins.int
    ARCHIVE_IDENTIFIER_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    signature: builtins.bytes
    archive_identifier: builtins.bytes
    def __init__(
        self,
        *,
        data: builtins.bytes | None = ...,
        signature: builtins.bytes | None = ...,
        archive_identifier: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["archive_identifier", b"archive_identifier", "data", b"data", "signature", b"signature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["archive_identifier", b"archive_identifier", "data", b"data", "signature", b"signature"]) -> None: ...

global___ManifestFile = ManifestFile
