# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ddf/ddf_extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x64\x64\x66/ddf_extensions.proto\x1a google/protobuf/descriptor.proto:0\n\x05\x61lias\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\t:7\n\x0cstruct_align\x12\x1f.google.protobuf.MessageOptions\x18\xd3\x86\x03 \x01(\x08:1\n\x08resource\x12\x1d.google.protobuf.FieldOptions\x18\xb4\x87\x03 \x01(\x08:4\n\x0b\x66ield_align\x12\x1d.google.protobuf.FieldOptions\x18\xd4\x86\x03 \x01(\x08:8\n\x0b\x64isplayName\x12!.google.protobuf.EnumValueOptions\x18\x98\x88\x03 \x01(\t:5\n\rddf_namespace\x12\x1c.google.protobuf.FileOptions\x18\xd1\x86\x03 \x01(\t:4\n\x0c\x64\x64\x66_includes\x12\x1c.google.protobuf.FileOptions\x18\xd2\x86\x03 \x01(\tB!\n\x10\x63om.dynamo.protoB\rDdfExtensions')


ALIAS_FIELD_NUMBER = 50000
alias = DESCRIPTOR.extensions_by_name['alias']
STRUCT_ALIGN_FIELD_NUMBER = 50003
struct_align = DESCRIPTOR.extensions_by_name['struct_align']
RESOURCE_FIELD_NUMBER = 50100
resource = DESCRIPTOR.extensions_by_name['resource']
FIELD_ALIGN_FIELD_NUMBER = 50004
field_align = DESCRIPTOR.extensions_by_name['field_align']
DISPLAYNAME_FIELD_NUMBER = 50200
displayName = DESCRIPTOR.extensions_by_name['displayName']
DDF_NAMESPACE_FIELD_NUMBER = 50001
ddf_namespace = DESCRIPTOR.extensions_by_name['ddf_namespace']
DDF_INCLUDES_FIELD_NUMBER = 50002
ddf_includes = DESCRIPTOR.extensions_by_name['ddf_includes']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(alias)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(struct_align)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(resource)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_align)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(displayName)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(ddf_namespace)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(ddf_includes)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.dynamo.protoB\rDdfExtensions'
# @@protoc_insertion_point(module_scope)
