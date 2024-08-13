# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lift_zone.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0flift_zone.proto\x12\x0egsdk.lift_zone\x1a\nzone.proto\x1a\x0c\x61\x63tion.proto\",\n\x04Lift\x12\x0e\n\x06liftID\x18\x01 \x01(\r\x12\x14\n\x0c\x66loorIndexes\x18\x03 \x03(\r\"\x80\x02\n\x08ZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x63tivateScheduleID\x18\x03 \x01(\r\x12\x1c\n\x14\x64\x65\x61\x63tivateScheduleID\x18\x04 \x01(\r\x12\x10\n\x08\x64isabled\x18\x05 \x01(\x08\x12\x0f\n\x07\x61larmed\x18\x06 \x01(\x08\x12#\n\x05lifts\x18\x07 \x03(\x0b\x32\x14.gsdk.lift_zone.Lift\x12$\n\x07\x61\x63tions\x18\x08 \x03(\x0b\x32\x13.gsdk.action.Action\x12\x16\n\x0e\x62ypassGroupIDs\x18\t \x03(\r\x12\x16\n\x0eunlockGroupIDs\x18\n \x03(\r\"\x1e\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"6\n\x0bGetResponse\x12\'\n\x05zones\x18\x01 \x03(\x0b\x32\x18.gsdk.lift_zone.ZoneInfo\"5\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\":\n\x11GetStatusResponse\x12%\n\x06status\x18\x01 \x03(\x0b\x32\x15.gsdk.zone.ZoneStatus\"G\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\'\n\x05zones\x18\x02 \x03(\x0b\x32\x18.gsdk.lift_zone.ZoneInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"E\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\x12\x0f\n\x07\x61larmed\x18\x03 \x01(\x08\"\x12\n\x10SetAlarmResponse*\x90\x01\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x0e\n\nMAX_ALARMS\x10\x05\x12\x15\n\x11MAX_BYPASS_GROUPS\x10\x10\x12\x15\n\x11MAX_UNLOCK_GROUPS\x10\x10\x12\r\n\tMAX_LIFTS\x10 \x12\x14\n\x0fMAX_NAME_LENGTH\x10\x90\x01\x1a\x02\x10\x01\x32\xc6\x03\n\x08LiftZone\x12>\n\x03Get\x12\x1a.gsdk.lift_zone.GetRequest\x1a\x1b.gsdk.lift_zone.GetResponse\x12P\n\tGetStatus\x12 .gsdk.lift_zone.GetStatusRequest\x1a!.gsdk.lift_zone.GetStatusResponse\x12>\n\x03\x41\x64\x64\x12\x1a.gsdk.lift_zone.AddRequest\x1a\x1b.gsdk.lift_zone.AddResponse\x12G\n\x06\x44\x65lete\x12\x1d.gsdk.lift_zone.DeleteRequest\x1a\x1e.gsdk.lift_zone.DeleteResponse\x12P\n\tDeleteAll\x12 .gsdk.lift_zone.DeleteAllRequest\x1a!.gsdk.lift_zone.DeleteAllResponse\x12M\n\x08SetAlarm\x12\x1f.gsdk.lift_zone.SetAlarmRequest\x1a .gsdk.lift_zone.SetAlarmResponseB:\n\x1c\x63om.supremainc.sdk.lift_zoneP\x01Z\x18\x62iostar/service/liftZoneb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lift_zone_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.supremainc.sdk.lift_zoneP\001Z\030biostar/service/liftZone'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=878
  _globals['_ENUM']._serialized_end=1022
  _globals['_LIFT']._serialized_start=61
  _globals['_LIFT']._serialized_end=105
  _globals['_ZONEINFO']._serialized_start=108
  _globals['_ZONEINFO']._serialized_end=364
  _globals['_GETREQUEST']._serialized_start=366
  _globals['_GETREQUEST']._serialized_end=396
  _globals['_GETRESPONSE']._serialized_start=398
  _globals['_GETRESPONSE']._serialized_end=452
  _globals['_GETSTATUSREQUEST']._serialized_start=454
  _globals['_GETSTATUSREQUEST']._serialized_end=507
  _globals['_GETSTATUSRESPONSE']._serialized_start=509
  _globals['_GETSTATUSRESPONSE']._serialized_end=567
  _globals['_ADDREQUEST']._serialized_start=569
  _globals['_ADDREQUEST']._serialized_end=640
  _globals['_ADDRESPONSE']._serialized_start=642
  _globals['_ADDRESPONSE']._serialized_end=655
  _globals['_DELETEREQUEST']._serialized_start=657
  _globals['_DELETEREQUEST']._serialized_end=707
  _globals['_DELETERESPONSE']._serialized_start=709
  _globals['_DELETERESPONSE']._serialized_end=725
  _globals['_DELETEALLREQUEST']._serialized_start=727
  _globals['_DELETEALLREQUEST']._serialized_end=763
  _globals['_DELETEALLRESPONSE']._serialized_start=765
  _globals['_DELETEALLRESPONSE']._serialized_end=784
  _globals['_SETALARMREQUEST']._serialized_start=786
  _globals['_SETALARMREQUEST']._serialized_end=855
  _globals['_SETALARMRESPONSE']._serialized_start=857
  _globals['_SETALARMRESPONSE']._serialized_end=875
  _globals['_LIFTZONE']._serialized_start=1025
  _globals['_LIFTZONE']._serialized_end=1479
# @@protoc_insertion_point(module_scope)