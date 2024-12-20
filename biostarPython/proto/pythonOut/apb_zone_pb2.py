# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: apb_zone.proto
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
    'apb_zone.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import zone_pb2 as zone__pb2
from biostarPython.service import action_pb2 as action__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61pb_zone.proto\x12\rgsdk.apb_zone\x1a\nzone.proto\x1a\x0c\x61\x63tion.proto\"I\n\x06Member\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12-\n\nreaderType\x18\x02 \x01(\x0e\x32\x19.gsdk.apb_zone.ReaderType\"\xeb\x01\n\x08ZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12!\n\x04type\x18\x03 \x01(\x0e\x32\x13.gsdk.apb_zone.Type\x12\x10\n\x08\x64isabled\x18\x04 \x01(\x08\x12\x0f\n\x07\x61larmed\x18\x05 \x01(\x08\x12\x15\n\rresetDuration\x18\x06 \x01(\r\x12&\n\x07members\x18\x07 \x03(\x0b\x32\x15.gsdk.apb_zone.Member\x12$\n\x07\x61\x63tions\x18\x08 \x03(\x0b\x32\x13.gsdk.action.Action\x12\x16\n\x0e\x62ypassGroupIDs\x18\t \x03(\r\"\x1e\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"5\n\x0bGetResponse\x12&\n\x05zones\x18\x01 \x03(\x0b\x32\x17.gsdk.apb_zone.ZoneInfo\"5\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\":\n\x11GetStatusResponse\x12%\n\x06status\x18\x01 \x03(\x0b\x32\x15.gsdk.zone.ZoneStatus\"F\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\x05zones\x18\x02 \x03(\x0b\x32\x17.gsdk.apb_zone.ZoneInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"A\n\x0c\x43learRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06zoneID\x18\x02 \x01(\r\x12\x0f\n\x07userIDs\x18\x03 \x03(\t\"\x0f\n\rClearResponse\"3\n\x0f\x43learAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06zoneID\x18\x02 \x01(\r\"\x12\n\x10\x43learAllResponse\"E\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\x12\x0f\n\x07\x61larmed\x18\x03 \x01(\x08\"\x12\n\x10SetAlarmResponse*\x80\x01\n\x04\x45num\x12\x0c\n\x08NO_RESET\x10\x00\x12\x1c\n\x16\x44\x45\x46\x41ULT_RESET_DURATION\x10\x80\xa3\x05\x12\x0e\n\nMAX_ALARMS\x10\x05\x12\x15\n\x11MAX_BYPASS_GROUPS\x10\x10\x12\x0f\n\x0bMAX_MEMBERS\x10@\x12\x14\n\x0fMAX_NAME_LENGTH\x10\x90\x01*\x1a\n\x04Type\x12\x08\n\x04HARD\x10\x00\x12\x08\n\x04SOFT\x10\x01*!\n\nReaderType\x12\t\n\x05\x45NTRY\x10\x00\x12\x08\n\x04\x45XIT\x10\x01\x32\xca\x04\n\x07\x41PBZone\x12<\n\x03Get\x12\x19.gsdk.apb_zone.GetRequest\x1a\x1a.gsdk.apb_zone.GetResponse\x12N\n\tGetStatus\x12\x1f.gsdk.apb_zone.GetStatusRequest\x1a .gsdk.apb_zone.GetStatusResponse\x12<\n\x03\x41\x64\x64\x12\x19.gsdk.apb_zone.AddRequest\x1a\x1a.gsdk.apb_zone.AddResponse\x12\x42\n\x05\x43lear\x12\x1b.gsdk.apb_zone.ClearRequest\x1a\x1c.gsdk.apb_zone.ClearResponse\x12K\n\x08\x43learAll\x12\x1e.gsdk.apb_zone.ClearAllRequest\x1a\x1f.gsdk.apb_zone.ClearAllResponse\x12\x45\n\x06\x44\x65lete\x12\x1c.gsdk.apb_zone.DeleteRequest\x1a\x1d.gsdk.apb_zone.DeleteResponse\x12N\n\tDeleteAll\x12\x1f.gsdk.apb_zone.DeleteAllRequest\x1a .gsdk.apb_zone.DeleteAllResponse\x12K\n\x08SetAlarm\x12\x1e.gsdk.apb_zone.SetAlarmRequest\x1a\x1f.gsdk.apb_zone.SetAlarmResponseB8\n\x1b\x63om.supremainc.sdk.apb_zoneP\x01Z\x17\x62iostar/service/apbZoneb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apb_zone_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.supremainc.sdk.apb_zoneP\001Z\027biostar/service/apbZone'
  _globals['_ENUM']._serialized_start=1039
  _globals['_ENUM']._serialized_end=1167
  _globals['_TYPE']._serialized_start=1169
  _globals['_TYPE']._serialized_end=1195
  _globals['_READERTYPE']._serialized_start=1197
  _globals['_READERTYPE']._serialized_end=1230
  _globals['_MEMBER']._serialized_start=59
  _globals['_MEMBER']._serialized_end=132
  _globals['_ZONEINFO']._serialized_start=135
  _globals['_ZONEINFO']._serialized_end=370
  _globals['_GETREQUEST']._serialized_start=372
  _globals['_GETREQUEST']._serialized_end=402
  _globals['_GETRESPONSE']._serialized_start=404
  _globals['_GETRESPONSE']._serialized_end=457
  _globals['_GETSTATUSREQUEST']._serialized_start=459
  _globals['_GETSTATUSREQUEST']._serialized_end=512
  _globals['_GETSTATUSRESPONSE']._serialized_start=514
  _globals['_GETSTATUSRESPONSE']._serialized_end=572
  _globals['_ADDREQUEST']._serialized_start=574
  _globals['_ADDREQUEST']._serialized_end=644
  _globals['_ADDRESPONSE']._serialized_start=646
  _globals['_ADDRESPONSE']._serialized_end=659
  _globals['_DELETEREQUEST']._serialized_start=661
  _globals['_DELETEREQUEST']._serialized_end=711
  _globals['_DELETERESPONSE']._serialized_start=713
  _globals['_DELETERESPONSE']._serialized_end=729
  _globals['_DELETEALLREQUEST']._serialized_start=731
  _globals['_DELETEALLREQUEST']._serialized_end=767
  _globals['_DELETEALLRESPONSE']._serialized_start=769
  _globals['_DELETEALLRESPONSE']._serialized_end=788
  _globals['_CLEARREQUEST']._serialized_start=790
  _globals['_CLEARREQUEST']._serialized_end=855
  _globals['_CLEARRESPONSE']._serialized_start=857
  _globals['_CLEARRESPONSE']._serialized_end=872
  _globals['_CLEARALLREQUEST']._serialized_start=874
  _globals['_CLEARALLREQUEST']._serialized_end=925
  _globals['_CLEARALLRESPONSE']._serialized_start=927
  _globals['_CLEARALLRESPONSE']._serialized_end=945
  _globals['_SETALARMREQUEST']._serialized_start=947
  _globals['_SETALARMREQUEST']._serialized_end=1016
  _globals['_SETALARMRESPONSE']._serialized_start=1018
  _globals['_SETALARMRESPONSE']._serialized_end=1036
  _globals['_APBZONE']._serialized_start=1233
  _globals['_APBZONE']._serialized_end=1819
# @@protoc_insertion_point(module_scope)
