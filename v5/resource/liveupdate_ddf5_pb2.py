# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource/liveupdate_ddf5.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v5.ddf import ddf_extensions_pb2 as ddf_dot_ddf__extensions__pb2
from v5.ddf import ddf_math_pb2 as ddf_dot_ddf__math__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eresource/liveupdate_ddf5.proto\x12\x10\x64mLiveUpdateDDF5\x1a\x18\x64\x64\x66/ddf_extensions.proto\x1a\x12\x64\x64\x66/ddf_math.proto\"\x1a\n\nHashDigest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"\xb6\x02\n\x0eManifestHeader\x12M\n\x17resource_hash_algorithm\x18\x01 \x02(\x0e\x32\x1f.dmLiveUpdateDDF5.HashAlgorithm:\x0bHASH_SHA256\x12N\n\x18signature_hash_algorithm\x18\x02 \x02(\x0e\x32\x1f.dmLiveUpdateDDF5.HashAlgorithm:\x0bHASH_SHA256\x12K\n\x18signature_sign_algorithm\x18\x03 \x02(\x0e\x32\x1f.dmLiveUpdateDDF5.SignAlgorithm:\x08SIGN_RSA\x12\x38\n\x12project_identifier\x18\x04 \x02(\x0b\x32\x1c.dmLiveUpdateDDF5.HashDigest\"\xa7\x01\n\rResourceEntry\x12*\n\x04hash\x18\x01 \x02(\x0b\x32\x1c.dmLiveUpdateDDF5.HashDigest\x12\x0b\n\x03url\x18\x02 \x02(\t\x12\x10\n\x08url_hash\x18\x03 \x02(\x04\x12\x0c\n\x04size\x18\x04 \x02(\r\x12\x17\n\x0f\x63ompressed_size\x18\x05 \x02(\r\x12\x10\n\x05\x66lags\x18\x06 \x02(\r:\x01\x30\x12\x12\n\ndependants\x18\x07 \x03(\x04\"\xab\x01\n\x0cManifestData\x12\x30\n\x06header\x18\x01 \x02(\x0b\x32 .dmLiveUpdateDDF5.ManifestHeader\x12\x35\n\x0f\x65ngine_versions\x18\x02 \x03(\x0b\x32\x1c.dmLiveUpdateDDF5.HashDigest\x12\x32\n\tresources\x18\x03 \x03(\x0b\x32\x1f.dmLiveUpdateDDF5.ResourceEntry\"_\n\x0cManifestFile\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x12\x11\n\tsignature\x18\x02 \x02(\x0c\x12\x1a\n\x12\x61rchive_identifier\x18\x03 \x01(\x0c\x12\x12\n\x07version\x18\x04 \x01(\r:\x01\x30*`\n\rHashAlgorithm\x12\x10\n\x0cHASH_UNKNOWN\x10\x00\x12\x0c\n\x08HASH_MD5\x10\x01\x12\r\n\tHASH_SHA1\x10\x02\x12\x0f\n\x0bHASH_SHA256\x10\x03\x12\x0f\n\x0bHASH_SHA512\x10\x04*/\n\rSignAlgorithm\x12\x10\n\x0cSIGN_UNKNOWN\x10\x00\x12\x0c\n\x08SIGN_RSA\x10\x01*M\n\x11ResourceEntryFlag\x12\x0b\n\x07\x42UNDLED\x10\x01\x12\x0c\n\x08\x45XCLUDED\x10\x02\x12\r\n\tENCRYPTED\x10\x04\x12\x0e\n\nCOMPRESSED\x10\x08\x42\'\n\x1b\x63om.dynamo.liveupdate.protoB\x08Manifest')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'resource.liveupdate_ddf5_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.dynamo.liveupdate.protoB\010Manifest'
  _globals['_HASHALGORITHM']._serialized_start=880
  _globals['_HASHALGORITHM']._serialized_end=976
  _globals['_SIGNALGORITHM']._serialized_start=978
  _globals['_SIGNALGORITHM']._serialized_end=1025
  _globals['_RESOURCEENTRYFLAG']._serialized_start=1027
  _globals['_RESOURCEENTRYFLAG']._serialized_end=1104
  _globals['_HASHDIGEST']._serialized_start=98
  _globals['_HASHDIGEST']._serialized_end=124
  _globals['_MANIFESTHEADER']._serialized_start=127
  _globals['_MANIFESTHEADER']._serialized_end=437
  _globals['_RESOURCEENTRY']._serialized_start=440
  _globals['_RESOURCEENTRY']._serialized_end=607
  _globals['_MANIFESTDATA']._serialized_start=610
  _globals['_MANIFESTDATA']._serialized_end=781
  _globals['_MANIFESTFILE']._serialized_start=783
  _globals['_MANIFESTFILE']._serialized_end=878
# @@protoc_insertion_point(module_scope)
