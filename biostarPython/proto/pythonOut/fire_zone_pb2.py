# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: fire_zone.proto
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
    'fire_zone.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import zone_pb2 as zone__pb2
from biostarPython.service import action_pb2 as action__pb2
from biostarPython.service import device_pb2 as device__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66ire_zone.proto\x12\x0egsdk.fire_zone\x1a\nzone.proto\x1a\x0c\x61\x63tion.proto\x1a\x0c\x64\x65vice.proto\"e\n\nFireSensor\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.gsdk.device.SwitchType\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\"\xaf\x01\n\x08ZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0f\n\x07\x61larmed\x18\x04 \x01(\x08\x12\x0f\n\x07\x64oorIDs\x18\x05 \x03(\r\x12+\n\x07sensors\x18\x06 \x03(\x0b\x32\x1a.gsdk.fire_zone.FireSensor\x12$\n\x07\x61\x63tions\x18\x07 \x03(\x0b\x32\x13.gsdk.action.Action\"\x1e\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"6\n\x0bGetResponse\x12\'\n\x05zones\x18\x01 \x03(\x0b\x32\x18.gsdk.fire_zone.ZoneInfo\"5\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\":\n\x11GetStatusResponse\x12%\n\x06status\x18\x01 \x03(\x0b\x32\x15.gsdk.zone.ZoneStatus\"G\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\'\n\x05zones\x18\x02 \x03(\x0b\x32\x18.gsdk.fire_zone.ZoneInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"E\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\x12\x0f\n\x07\x61larmed\x18\x03 \x01(\x08\"\x12\n\x10SetAlarmResponse*w\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x0e\n\nMAX_ALARMS\x10\x05\x12\x0f\n\x0bMAX_SENSORS\x10\x08\x12\x15\n\x11MAX_DOOR_OR_LIFTS\x10 \x12\x14\n\x0fMAX_NAME_LENGTH\x10\x90\x01\x32\xcb\x03\n\rFireAlarmZone\x12>\n\x03Get\x12\x1a.gsdk.fire_zone.GetRequest\x1a\x1b.gsdk.fire_zone.GetResponse\x12P\n\tGetStatus\x12 .gsdk.fire_zone.GetStatusRequest\x1a!.gsdk.fire_zone.GetStatusResponse\x12>\n\x03\x41\x64\x64\x12\x1a.gsdk.fire_zone.AddRequest\x1a\x1b.gsdk.fire_zone.AddResponse\x12G\n\x06\x44\x65lete\x12\x1d.gsdk.fire_zone.DeleteRequest\x1a\x1e.gsdk.fire_zone.DeleteResponse\x12P\n\tDeleteAll\x12 .gsdk.fire_zone.DeleteAllRequest\x1a!.gsdk.fire_zone.DeleteAllResponse\x12M\n\x08SetAlarm\x12\x1f.gsdk.fire_zone.SetAlarmRequest\x1a .gsdk.fire_zone.SetAlarmResponseB:\n\x1c\x63om.supremainc.sdk.fire_zoneP\x01Z\x18\x62iostar/service/fireZoneb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fire_zone_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.supremainc.sdk.fire_zoneP\001Z\030biostar/service/fireZone'
  _globals['_ENUM']._serialized_start=867
  _globals['_ENUM']._serialized_end=986
  _globals['_FIRESENSOR']._serialized_start=75
  _globals['_FIRESENSOR']._serialized_end=176
  _globals['_ZONEINFO']._serialized_start=179
  _globals['_ZONEINFO']._serialized_end=354
  _globals['_GETREQUEST']._serialized_start=356
  _globals['_GETREQUEST']._serialized_end=386
  _globals['_GETRESPONSE']._serialized_start=388
  _globals['_GETRESPONSE']._serialized_end=442
  _globals['_GETSTATUSREQUEST']._serialized_start=444
  _globals['_GETSTATUSREQUEST']._serialized_end=497
  _globals['_GETSTATUSRESPONSE']._serialized_start=499
  _globals['_GETSTATUSRESPONSE']._serialized_end=557
  _globals['_ADDREQUEST']._serialized_start=559
  _globals['_ADDREQUEST']._serialized_end=630
  _globals['_ADDRESPONSE']._serialized_start=632
  _globals['_ADDRESPONSE']._serialized_end=645
  _globals['_DELETEREQUEST']._serialized_start=647
  _globals['_DELETEREQUEST']._serialized_end=697
  _globals['_DELETERESPONSE']._serialized_start=699
  _globals['_DELETERESPONSE']._serialized_end=715
  _globals['_DELETEALLREQUEST']._serialized_start=717
  _globals['_DELETEALLREQUEST']._serialized_end=753
  _globals['_DELETEALLRESPONSE']._serialized_start=755
  _globals['_DELETEALLRESPONSE']._serialized_end=774
  _globals['_SETALARMREQUEST']._serialized_start=776
  _globals['_SETALARMREQUEST']._serialized_end=845
  _globals['_SETALARMRESPONSE']._serialized_start=847
  _globals['_SETALARMRESPONSE']._serialized_end=865
  _globals['_FIREALARMZONE']._serialized_start=989
  _globals['_FIREALARMZONE']._serialized_end=1448
# @@protoc_insertion_point(module_scope)
