# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: err.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'err.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\terr.proto\x12\x08gsdk.err\"<\n\rErrorResponse\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03msg\x18\x03 \x01(\t\"C\n\x12MultiErrorResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"D\n\x14GatewayErrorResponse\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03msg\x18\x03 \x01(\t2\x07\n\x05\x45rrorB/\n\x16\x63om.supremainc.sdk.errP\x01Z\x13\x62iostar/service/errb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'err_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.supremainc.sdk.errP\001Z\023biostar/service/err'
  _globals['_ERRORRESPONSE']._serialized_start=23
  _globals['_ERRORRESPONSE']._serialized_end=83
  _globals['_MULTIERRORRESPONSE']._serialized_start=85
  _globals['_MULTIERRORRESPONSE']._serialized_end=152
  _globals['_GATEWAYERRORRESPONSE']._serialized_start=154
  _globals['_GATEWAYERRORRESPONSE']._serialized_end=222
  _globals['_ERROR']._serialized_start=224
  _globals['_ERROR']._serialized_end=231
# @@protoc_insertion_point(module_scope)
