# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nzone.proto\x12\x04zone\"L\n\nZoneStatus\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x1c\n\x06status\x18\x02 \x01(\x0e\x32\x0c.zone.Status\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08*p\n\x04Type\x12\x07\n\x03\x41PB\x10\x00\x12\r\n\tTIMED_APB\x10\x01\x12\x0e\n\nFIRE_ALARM\x10\x02\x12\x12\n\x0eSCHEDULED_LOCK\x10\x03\x12\x13\n\x0fINTRUSION_ALARM\x10\x04\x12\r\n\tINTERLOCK\x10\x05\x12\x08\n\x04LIFT\x10\x06*|\n\x06Status\x12\n\n\x06NORMAL\x10\x00\x12\x0b\n\x07\x41LARMED\x10\x01\x12\n\n\x06LOCKED\x10\x02\x12\x0c\n\x08UNLOCKED\x10\x04\x12\x0f\n\x0bLIFT_LOCKED\x10\x02\x12\x11\n\rLIFT_UNLOCKED\x10\x04\x12\t\n\x05\x41RMED\x10\x08\x12\x0c\n\x08\x44ISARMED\x10\x00\x1a\x02\x10\x01\x42\x31\n\x17\x63om.supremainc.sdk.zoneP\x01Z\x14\x62iostar/service/zoneb\x06proto3')

_TYPE = DESCRIPTOR.enum_types_by_name['Type']
Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
APB = 0
TIMED_APB = 1
FIRE_ALARM = 2
SCHEDULED_LOCK = 3
INTRUSION_ALARM = 4
INTERLOCK = 5
LIFT = 6
NORMAL = 0
ALARMED = 1
LOCKED = 2
UNLOCKED = 4
LIFT_LOCKED = 2
LIFT_UNLOCKED = 4
ARMED = 8
DISARMED = 0


_ZONESTATUS = DESCRIPTOR.message_types_by_name['ZoneStatus']
ZoneStatus = _reflection.GeneratedProtocolMessageType('ZoneStatus', (_message.Message,), {
  'DESCRIPTOR' : _ZONESTATUS,
  '__module__' : 'zone_pb2'
  # @@protoc_insertion_point(class_scope:zone.ZoneStatus)
  })
_sym_db.RegisterMessage(ZoneStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.supremainc.sdk.zoneP\001Z\024biostar/service/zone'
  _STATUS._options = None
  _STATUS._serialized_options = b'\020\001'
  _TYPE._serialized_start=98
  _TYPE._serialized_end=210
  _STATUS._serialized_start=212
  _STATUS._serialized_end=336
  _ZONESTATUS._serialized_start=20
  _ZONESTATUS._serialized_end=96
# @@protoc_insertion_point(module_scope)
