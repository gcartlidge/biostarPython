# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import network_pb2 as network__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tudp.proto\x12\x08gsdk.udp\x1a\rnetwork.proto\".\n\nDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06IPAddr\x18\x02 \x01(\t\">\n\x12GetIPConfigRequest\x12(\n\ndeviceInfo\x18\x01 \x01(\x0b\x32\x14.gsdk.udp.DeviceInfo\"=\n\x13GetIPConfigResponse\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.gsdk.network.IPConfig\"f\n\x12SetIPConfigRequest\x12(\n\ndeviceInfo\x18\x01 \x01(\x0b\x32\x14.gsdk.udp.DeviceInfo\x12&\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x16.gsdk.network.IPConfig\"\x15\n\x13SetIPConfigResponse2\x9d\x01\n\x03UDP\x12J\n\x0bGetIPConfig\x12\x1c.gsdk.udp.GetIPConfigRequest\x1a\x1d.gsdk.udp.GetIPConfigResponse\x12J\n\x0bSetIPConfig\x12\x1c.gsdk.udp.SetIPConfigRequest\x1a\x1d.gsdk.udp.SetIPConfigResponseB/\n\x16\x63om.supremainc.sdk.udpP\x01Z\x13\x62iostar/service/udpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'udp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.supremainc.sdk.udpP\001Z\023biostar/service/udp'
  _globals['_DEVICEINFO']._serialized_start=38
  _globals['_DEVICEINFO']._serialized_end=84
  _globals['_GETIPCONFIGREQUEST']._serialized_start=86
  _globals['_GETIPCONFIGREQUEST']._serialized_end=148
  _globals['_GETIPCONFIGRESPONSE']._serialized_start=150
  _globals['_GETIPCONFIGRESPONSE']._serialized_end=211
  _globals['_SETIPCONFIGREQUEST']._serialized_start=213
  _globals['_SETIPCONFIGREQUEST']._serialized_end=315
  _globals['_SETIPCONFIGRESPONSE']._serialized_start=317
  _globals['_SETIPCONFIGRESPONSE']._serialized_end=338
  _globals['_UDP']._serialized_start=341
  _globals['_UDP']._serialized_end=498
# @@protoc_insertion_point(module_scope)
