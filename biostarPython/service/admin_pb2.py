# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\x12\x05\x61\x64min\"\x10\n\x0eGetInfoRequest\"5\n\x0fGetInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tbuildDate\x18\x02 \x01(\t2A\n\x05\x41\x64min\x12\x38\n\x07GetInfo\x12\x15.admin.GetInfoRequest\x1a\x16.admin.GetInfoResponseB3\n\x18\x63om.supremainc.sdk.adminP\x01Z\x15\x62iostar/service/adminb\x06proto3')



_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'admin_pb2'
  # @@protoc_insertion_point(class_scope:admin.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'admin_pb2'
  # @@protoc_insertion_point(class_scope:admin.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)

_ADMIN = DESCRIPTOR.services_by_name['Admin']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.supremainc.sdk.adminP\001Z\025biostar/service/admin'
  _GETINFOREQUEST._serialized_start=22
  _GETINFOREQUEST._serialized_end=38
  _GETINFORESPONSE._serialized_start=40
  _GETINFORESPONSE._serialized_end=93
  _ADMIN._serialized_start=95
  _ADMIN._serialized_end=160
# @@protoc_insertion_point(module_scope)
