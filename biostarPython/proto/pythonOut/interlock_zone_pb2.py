# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interlock_zone.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import zone_pb2 as zone__pb2
import action_pb2 as action__pb2
import device_pb2 as device__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14interlock_zone.proto\x12\x13gsdk.interlock_zone\x1a\nzone.proto\x1a\x0c\x61\x63tion.proto\x1a\x0c\x64\x65vice.proto\"y\n\x05Input\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12+\n\nswitchType\x18\x03 \x01(\x0e\x32\x17.gsdk.device.SwitchType\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\x12\x11\n\toperation\x18\x05 \x01(\r\"<\n\x06Output\x12\r\n\x05\x65vent\x18\x01 \x01(\r\x12#\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x13.gsdk.action.Action\"\xa5\x01\n\x08ZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12*\n\x06inputs\x18\x04 \x03(\x0b\x32\x1a.gsdk.interlock_zone.Input\x12,\n\x07outputs\x18\x05 \x03(\x0b\x32\x1b.gsdk.interlock_zone.Output\x12\x0f\n\x07\x64oorIDs\x18\x06 \x03(\r\"\x1e\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\";\n\x0bGetResponse\x12,\n\x05zones\x18\x01 \x03(\x0b\x32\x1d.gsdk.interlock_zone.ZoneInfo\"5\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\":\n\x11GetStatusResponse\x12%\n\x06status\x18\x01 \x03(\x0b\x32\x15.gsdk.zone.ZoneStatus\"L\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12,\n\x05zones\x18\x02 \x03(\x0b\x32\x1d.gsdk.interlock_zone.ZoneInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"E\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\x12\x0f\n\x07\x61larmed\x18\x03 \x01(\x08\"\x12\n\x10SetAlarmResponse*s\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\r\n\tMAX_DOORS\x10\x04\x12\x0e\n\nMAX_INPUTS\x10\x04\x12\x0f\n\x0bMAX_OUTPUTS\x10\x08\x12\x14\n\x0fMAX_NAME_LENGTH\x10\x90\x01\x1a\x02\x10\x01*`\n\rOperationType\x12\x12\n\x0eOPERATION_NONE\x10\x00\x12\x13\n\x0fOPERATION_ENRTY\x10\x01\x12\x12\n\x0eOPERATION_EXIT\x10\x02\x12\x12\n\rOPERATION_ALL\x10\xff\x01\x32\x87\x04\n\rInterlockZone\x12H\n\x03Get\x12\x1f.gsdk.interlock_zone.GetRequest\x1a .gsdk.interlock_zone.GetResponse\x12Z\n\tGetStatus\x12%.gsdk.interlock_zone.GetStatusRequest\x1a&.gsdk.interlock_zone.GetStatusResponse\x12H\n\x03\x41\x64\x64\x12\x1f.gsdk.interlock_zone.AddRequest\x1a .gsdk.interlock_zone.AddResponse\x12Q\n\x06\x44\x65lete\x12\".gsdk.interlock_zone.DeleteRequest\x1a#.gsdk.interlock_zone.DeleteResponse\x12Z\n\tDeleteAll\x12%.gsdk.interlock_zone.DeleteAllRequest\x1a&.gsdk.interlock_zone.DeleteAllResponse\x12W\n\x08SetAlarm\x12$.gsdk.interlock_zone.SetAlarmRequest\x1a%.gsdk.interlock_zone.SetAlarmResponseBD\n!com.supremainc.sdk.interlock_zoneP\x01Z\x1d\x62iostar/service/interlockZoneb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'interlock_zone_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.supremainc.sdk.interlock_zoneP\001Z\035biostar/service/interlockZone'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=959
  _globals['_ENUM']._serialized_end=1074
  _globals['_OPERATIONTYPE']._serialized_start=1076
  _globals['_OPERATIONTYPE']._serialized_end=1172
  _globals['_INPUT']._serialized_start=85
  _globals['_INPUT']._serialized_end=206
  _globals['_OUTPUT']._serialized_start=208
  _globals['_OUTPUT']._serialized_end=268
  _globals['_ZONEINFO']._serialized_start=271
  _globals['_ZONEINFO']._serialized_end=436
  _globals['_GETREQUEST']._serialized_start=438
  _globals['_GETREQUEST']._serialized_end=468
  _globals['_GETRESPONSE']._serialized_start=470
  _globals['_GETRESPONSE']._serialized_end=529
  _globals['_GETSTATUSREQUEST']._serialized_start=531
  _globals['_GETSTATUSREQUEST']._serialized_end=584
  _globals['_GETSTATUSRESPONSE']._serialized_start=586
  _globals['_GETSTATUSRESPONSE']._serialized_end=644
  _globals['_ADDREQUEST']._serialized_start=646
  _globals['_ADDREQUEST']._serialized_end=722
  _globals['_ADDRESPONSE']._serialized_start=724
  _globals['_ADDRESPONSE']._serialized_end=737
  _globals['_DELETEREQUEST']._serialized_start=739
  _globals['_DELETEREQUEST']._serialized_end=789
  _globals['_DELETERESPONSE']._serialized_start=791
  _globals['_DELETERESPONSE']._serialized_end=807
  _globals['_DELETEALLREQUEST']._serialized_start=809
  _globals['_DELETEALLREQUEST']._serialized_end=845
  _globals['_DELETEALLRESPONSE']._serialized_start=847
  _globals['_DELETEALLRESPONSE']._serialized_end=866
  _globals['_SETALARMREQUEST']._serialized_start=868
  _globals['_SETALARMREQUEST']._serialized_end=937
  _globals['_SETALARMRESPONSE']._serialized_start=939
  _globals['_SETALARMRESPONSE']._serialized_end=957
  _globals['_INTERLOCKZONE']._serialized_start=1175
  _globals['_INTERLOCKZONE']._serialized_end=1694
# @@protoc_insertion_point(module_scope)
