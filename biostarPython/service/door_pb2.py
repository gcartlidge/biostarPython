# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: door.proto
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
    'door.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import device_pb2 as device__pb2
from biostarPython.service import action_pb2 as action__pb2
from biostarPython.service import apb_zone_pb2 as apb__zone__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndoor.proto\x12\tgsdk.door\x1a\x0c\x64\x65vice.proto\x1a\x0c\x61\x63tion.proto\x1a\x0e\x61pb_zone.proto\"\'\n\x05Relay\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\"i\n\x06Sensor\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.gsdk.device.SwitchType\x12\x18\n\x10\x61pbUseDoorSensor\x18\x04 \x01(\x08\"S\n\nExitButton\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.gsdk.device.SwitchType\"\xa0\x01\n\x06Status\x12\x0e\n\x06\x64oorID\x18\x01 \x01(\r\x12\x0e\n\x06isOpen\x18\x02 \x01(\x08\x12\x12\n\nisUnlocked\x18\x03 \x01(\x08\x12\x10\n\x08heldOpen\x18\x04 \x01(\x08\x12\x13\n\x0bunlockFlags\x18\x05 \x01(\r\x12\x11\n\tlockFlags\x18\x06 \x01(\r\x12\x12\n\nalarmFlags\x18\x07 \x01(\r\x12\x14\n\x0clastOpenTime\x18\x08 \x01(\r\"\x83\x05\n\x08\x44oorInfo\x12\x0e\n\x06\x64oorID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rentryDeviceID\x18\x03 \x01(\r\x12\x14\n\x0c\x65xitDeviceID\x18\x04 \x01(\r\x12\x1f\n\x05relay\x18\x05 \x01(\x0b\x32\x10.gsdk.door.Relay\x12!\n\x06sensor\x18\x06 \x01(\x0b\x32\x11.gsdk.door.Sensor\x12%\n\x06\x62utton\x18\x07 \x01(\x0b\x32\x15.gsdk.door.ExitButton\x12\x17\n\x0f\x61utoLockTimeout\x18\x08 \x01(\r\x12\x17\n\x0fheldOpenTimeout\x18\t \x01(\r\x12\x13\n\x0binstantLock\x18\n \x01(\x08\x12\x13\n\x0bunlockFlags\x18\x0b \x01(\r\x12\x11\n\tlockFlags\x18\x0c \x01(\r\x12\x19\n\x11unconditionalLock\x18\r \x01(\x08\x12.\n\x11\x66orcedOpenActions\x18\x0e \x03(\x0b\x32\x13.gsdk.action.Action\x12,\n\x0fheldOpenActions\x18\x0f \x03(\x0b\x32\x13.gsdk.action.Action\x12\x1a\n\x12\x64ualAuthScheduleID\x18\x10 \x01(\r\x12\x31\n\x0e\x64ualAuthDevice\x18\x11 \x01(\x0e\x32\x19.gsdk.door.DualAuthDevice\x12-\n\x0c\x64ualAuthType\x18\x12 \x01(\x0e\x32\x17.gsdk.door.DualAuthType\x12\x17\n\x0f\x64ualAuthTimeout\x18\x13 \x01(\r\x12\x18\n\x10\x64ualAuthGroupIDs\x18\x14 \x03(\r\x12(\n\x07\x61pbZone\x18\x15 \x01(\x0b\x32\x17.gsdk.apb_zone.ZoneInfo\"\"\n\x0eGetListRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"5\n\x0fGetListResponse\x12\"\n\x05\x64oors\x18\x01 \x03(\x0b\x32\x13.gsdk.door.DoorInfo\"$\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"6\n\x11GetStatusResponse\x12!\n\x06status\x18\x01 \x03(\x0b\x32\x11.gsdk.door.Status\"B\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x05\x64oors\x18\x02 \x03(\x0b\x32\x13.gsdk.door.DoorInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"B\n\x0bLockRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\x12\x10\n\x08\x64oorFlag\x18\x03 \x01(\r\"\x0e\n\x0cLockResponse\"D\n\rUnlockRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\x12\x10\n\x08\x64oorFlag\x18\x03 \x01(\r\"\x10\n\x0eUnlockResponse\"E\n\x0eReleaseRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\x12\x10\n\x08\x64oorFlag\x18\x03 \x01(\r\"\x11\n\x0fReleaseResponse\"G\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\x12\x11\n\talarmFlag\x18\x03 \x01(\r\"\x12\n\x10SetAlarmResponse*@\n\x08\x44oorFlag\x12\x08\n\x04NONE\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\r\n\tEMERGENCY\x10\x02\x12\x0c\n\x08OPERATOR\x10\x04*L\n\tAlarmFlag\x12\x0c\n\x08NO_ALARM\x10\x00\x12\x0f\n\x0b\x46ORCED_OPEN\x10\x01\x12\r\n\tHELD_OPEN\x10\x02\x12\x11\n\rAPB_VIOLATION\x10\x04*\x85\x01\n\x0e\x44ualAuthDevice\x12\x17\n\x13\x44UAL_AUTH_NO_DEVICE\x10\x00\x12\x1f\n\x1b\x44UAL_AUTH_ENTRY_DEVICE_ONLY\x10\x01\x12\x1e\n\x1a\x44UAL_AUTH_EXIT_DEVICE_ONLY\x10\x02\x12\x19\n\x15\x44UAL_AUTH_BOTH_DEVICE\x10\x03*6\n\x0c\x44ualAuthType\x12\x12\n\x0e\x44UAL_AUTH_NONE\x10\x00\x12\x12\n\x0e\x44UAL_AUTH_LAST\x10\x01*\xf9\x01\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x1d\n\x19\x44\x45\x46\x41ULT_AUTO_LOCK_TIMEOUT\x10\x03\x12\x1d\n\x19\x44\x45\x46\x41ULT_HELD_OPEN_TIMEOUT\x10\n\x12\x1d\n\x19\x44\x45\x46\x41ULT_DUAL_AUTH_TIMEOUT\x10\x0f\x12\x1a\n\x16MAX_FORCED_OPEN_ALARMS\x10\x05\x12\x18\n\x14MAX_HELD_OPEN_ALARMS\x10\x05\x12!\n\x1dMAX_DUAL_AUTH_APPROVAL_GROUPS\x10\x10\x12\x14\n\x0fMAX_NAME_LENGTH\x10\x90\x01\x1a\x02\x10\x01\x32\xcc\x04\n\x04\x44oor\x12@\n\x07GetList\x12\x19.gsdk.door.GetListRequest\x1a\x1a.gsdk.door.GetListResponse\x12\x46\n\tGetStatus\x12\x1b.gsdk.door.GetStatusRequest\x1a\x1c.gsdk.door.GetStatusResponse\x12\x34\n\x03\x41\x64\x64\x12\x15.gsdk.door.AddRequest\x1a\x16.gsdk.door.AddResponse\x12=\n\x06\x44\x65lete\x12\x18.gsdk.door.DeleteRequest\x1a\x19.gsdk.door.DeleteResponse\x12\x46\n\tDeleteAll\x12\x1b.gsdk.door.DeleteAllRequest\x1a\x1c.gsdk.door.DeleteAllResponse\x12\x37\n\x04Lock\x12\x16.gsdk.door.LockRequest\x1a\x17.gsdk.door.LockResponse\x12=\n\x06Unlock\x12\x18.gsdk.door.UnlockRequest\x1a\x19.gsdk.door.UnlockResponse\x12@\n\x07Release\x12\x19.gsdk.door.ReleaseRequest\x1a\x1a.gsdk.door.ReleaseResponse\x12\x43\n\x08SetAlarm\x12\x1a.gsdk.door.SetAlarmRequest\x1a\x1b.gsdk.door.SetAlarmResponseB1\n\x17\x63om.supremainc.sdk.doorP\x01Z\x14\x62iostar/service/doorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'door_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.supremainc.sdk.doorP\001Z\024biostar/service/door'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_DOORFLAG']._serialized_start=1863
  _globals['_DOORFLAG']._serialized_end=1927
  _globals['_ALARMFLAG']._serialized_start=1929
  _globals['_ALARMFLAG']._serialized_end=2005
  _globals['_DUALAUTHDEVICE']._serialized_start=2008
  _globals['_DUALAUTHDEVICE']._serialized_end=2141
  _globals['_DUALAUTHTYPE']._serialized_start=2143
  _globals['_DUALAUTHTYPE']._serialized_end=2197
  _globals['_ENUM']._serialized_start=2200
  _globals['_ENUM']._serialized_end=2449
  _globals['_RELAY']._serialized_start=69
  _globals['_RELAY']._serialized_end=108
  _globals['_SENSOR']._serialized_start=110
  _globals['_SENSOR']._serialized_end=215
  _globals['_EXITBUTTON']._serialized_start=217
  _globals['_EXITBUTTON']._serialized_end=300
  _globals['_STATUS']._serialized_start=303
  _globals['_STATUS']._serialized_end=463
  _globals['_DOORINFO']._serialized_start=466
  _globals['_DOORINFO']._serialized_end=1109
  _globals['_GETLISTREQUEST']._serialized_start=1111
  _globals['_GETLISTREQUEST']._serialized_end=1145
  _globals['_GETLISTRESPONSE']._serialized_start=1147
  _globals['_GETLISTRESPONSE']._serialized_end=1200
  _globals['_GETSTATUSREQUEST']._serialized_start=1202
  _globals['_GETSTATUSREQUEST']._serialized_end=1238
  _globals['_GETSTATUSRESPONSE']._serialized_start=1240
  _globals['_GETSTATUSRESPONSE']._serialized_end=1294
  _globals['_ADDREQUEST']._serialized_start=1296
  _globals['_ADDREQUEST']._serialized_end=1362
  _globals['_ADDRESPONSE']._serialized_start=1364
  _globals['_ADDRESPONSE']._serialized_end=1377
  _globals['_DELETEREQUEST']._serialized_start=1379
  _globals['_DELETEREQUEST']._serialized_end=1429
  _globals['_DELETERESPONSE']._serialized_start=1431
  _globals['_DELETERESPONSE']._serialized_end=1447
  _globals['_DELETEALLREQUEST']._serialized_start=1449
  _globals['_DELETEALLREQUEST']._serialized_end=1485
  _globals['_DELETEALLRESPONSE']._serialized_start=1487
  _globals['_DELETEALLRESPONSE']._serialized_end=1506
  _globals['_LOCKREQUEST']._serialized_start=1508
  _globals['_LOCKREQUEST']._serialized_end=1574
  _globals['_LOCKRESPONSE']._serialized_start=1576
  _globals['_LOCKRESPONSE']._serialized_end=1590
  _globals['_UNLOCKREQUEST']._serialized_start=1592
  _globals['_UNLOCKREQUEST']._serialized_end=1660
  _globals['_UNLOCKRESPONSE']._serialized_start=1662
  _globals['_UNLOCKRESPONSE']._serialized_end=1678
  _globals['_RELEASEREQUEST']._serialized_start=1680
  _globals['_RELEASEREQUEST']._serialized_end=1749
  _globals['_RELEASERESPONSE']._serialized_start=1751
  _globals['_RELEASERESPONSE']._serialized_end=1768
  _globals['_SETALARMREQUEST']._serialized_start=1770
  _globals['_SETALARMREQUEST']._serialized_end=1841
  _globals['_SETALARMRESPONSE']._serialized_start=1843
  _globals['_SETALARMRESPONSE']._serialized_end=1861
  _globals['_DOOR']._serialized_start=2452
  _globals['_DOOR']._serialized_end=3040
# @@protoc_insertion_point(module_scope)
