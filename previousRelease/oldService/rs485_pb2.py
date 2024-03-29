# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rs485.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import device_pb2 as device__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0brs485.proto\x12\ngsdk.rs485\x1a\x0c\x64\x65vice.proto\x1a\terr.proto\"{\n\x0fSlaveDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.gsdk.device.Type\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x11\n\tconnected\x18\x04 \x01(\x08\x12\x11\n\tchannelID\x18\x05 \x01(\r\"\'\n\x13SearchDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"G\n\x14SearchDeviceResponse\x12/\n\nslaveInfos\x18\x01 \x03(\x0b\x32\x1b.gsdk.rs485.SlaveDeviceInfo\"U\n\x10SetDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12/\n\nslaveInfos\x18\x02 \x03(\x0b\x32\x1b.gsdk.rs485.SlaveDeviceInfo\"\x13\n\x11SetDeviceResponse\"$\n\x10GetDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"D\n\x11GetDeviceResponse\x12/\n\nslaveInfos\x18\x02 \x03(\x0b\x32\x1b.gsdk.rs485.SlaveDeviceInfo\"\x87\x01\n\x11IntelligentPDInfo\x12\x18\n\x10useExceptionCode\x18\x01 \x01(\x08\x12\x15\n\rexceptionCode\x18\x02 \x01(\x0c\x12\x31\n\x0coutputFormat\x18\x03 \x01(\x0e\x32\x1b.gsdk.rs485.IPDOutputFormat\x12\x0e\n\x06OSDPID\x18\x04 \x01(\r\"S\n\x0cRS485Channel\x12\x11\n\tchannelID\x18\x01 \x01(\r\x12\x1e\n\x04mode\x18\x02 \x01(\x0e\x32\x10.gsdk.rs485.Mode\x12\x10\n\x08\x62\x61udRate\x18\x03 \x01(\r\"q\n\x0bRS485Config\x12*\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x18.gsdk.rs485.RS485Channel\x12\x36\n\x0fintelligentInfo\x18\x02 \x01(\x0b\x32\x1d.gsdk.rs485.IntelligentPDInfo\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"<\n\x11GetConfigResponse\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.gsdk.rs485.RS485Config\"M\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.gsdk.rs485.RS485Config\"\x13\n\x11SetConfigResponse\"S\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.gsdk.rs485.RS485Config\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*:\n\x04Mode\x12\x0b\n\x07NOT_USE\x10\x00\x12\n\n\x06MASTER\x10\x01\x12\t\n\x05SLAVE\x10\x02\x12\x0e\n\nSTANDALONE\x10\x03*)\n\x0fIPDOutputFormat\x12\n\n\x06\x43\x41RDID\x10\x00\x12\n\n\x06USERID\x10\x01\x32\xdb\x03\n\x05RS485\x12Q\n\x0cSearchDevice\x12\x1f.gsdk.rs485.SearchDeviceRequest\x1a .gsdk.rs485.SearchDeviceResponse\x12H\n\tGetDevice\x12\x1c.gsdk.rs485.GetDeviceRequest\x1a\x1d.gsdk.rs485.GetDeviceResponse\x12H\n\tSetDevice\x12\x1c.gsdk.rs485.SetDeviceRequest\x1a\x1d.gsdk.rs485.SetDeviceResponse\x12H\n\tGetConfig\x12\x1c.gsdk.rs485.GetConfigRequest\x1a\x1d.gsdk.rs485.GetConfigResponse\x12H\n\tSetConfig\x12\x1c.gsdk.rs485.SetConfigRequest\x1a\x1d.gsdk.rs485.SetConfigResponse\x12W\n\x0eSetConfigMulti\x12!.gsdk.rs485.SetConfigMultiRequest\x1a\".gsdk.rs485.SetConfigMultiResponseB3\n\x18\x63om.supremainc.sdk.rs485P\x01Z\x15\x62iostar/service/rs485b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rs485_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.supremainc.sdk.rs485P\001Z\025biostar/service/rs485'
  _MODE._serialized_start=1203
  _MODE._serialized_end=1261
  _IPDOUTPUTFORMAT._serialized_start=1263
  _IPDOUTPUTFORMAT._serialized_end=1304
  _SLAVEDEVICEINFO._serialized_start=52
  _SLAVEDEVICEINFO._serialized_end=175
  _SEARCHDEVICEREQUEST._serialized_start=177
  _SEARCHDEVICEREQUEST._serialized_end=216
  _SEARCHDEVICERESPONSE._serialized_start=218
  _SEARCHDEVICERESPONSE._serialized_end=289
  _SETDEVICEREQUEST._serialized_start=291
  _SETDEVICEREQUEST._serialized_end=376
  _SETDEVICERESPONSE._serialized_start=378
  _SETDEVICERESPONSE._serialized_end=397
  _GETDEVICEREQUEST._serialized_start=399
  _GETDEVICEREQUEST._serialized_end=435
  _GETDEVICERESPONSE._serialized_start=437
  _GETDEVICERESPONSE._serialized_end=505
  _INTELLIGENTPDINFO._serialized_start=508
  _INTELLIGENTPDINFO._serialized_end=643
  _RS485CHANNEL._serialized_start=645
  _RS485CHANNEL._serialized_end=728
  _RS485CONFIG._serialized_start=730
  _RS485CONFIG._serialized_end=843
  _GETCONFIGREQUEST._serialized_start=845
  _GETCONFIGREQUEST._serialized_end=881
  _GETCONFIGRESPONSE._serialized_start=883
  _GETCONFIGRESPONSE._serialized_end=943
  _SETCONFIGREQUEST._serialized_start=945
  _SETCONFIGREQUEST._serialized_end=1022
  _SETCONFIGRESPONSE._serialized_start=1024
  _SETCONFIGRESPONSE._serialized_end=1043
  _SETCONFIGMULTIREQUEST._serialized_start=1045
  _SETCONFIGMULTIREQUEST._serialized_end=1128
  _SETCONFIGMULTIRESPONSE._serialized_start=1130
  _SETCONFIGMULTIRESPONSE._serialized_end=1201
  _RS485._serialized_start=1307
  _RS485._serialized_end=1782
# @@protoc_insertion_point(module_scope)
