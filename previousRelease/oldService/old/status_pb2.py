# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import action_pb2 as action__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstatus.proto\x12\x0bgsdk.status\x1a\x0c\x61\x63tion.proto\x1a\terr.proto\"t\n\tLEDStatus\x12/\n\x0c\x64\x65viceStatus\x18\x01 \x01(\x0e\x32\x19.gsdk.status.DeviceStatus\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\'\n\x07signals\x18\x03 \x03(\x0b\x32\x16.gsdk.action.LEDSignal\"z\n\x0c\x42uzzerStatus\x12/\n\x0c\x64\x65viceStatus\x18\x01 \x01(\x0e\x32\x19.gsdk.status.DeviceStatus\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12*\n\x07signals\x18\x03 \x03(\x0b\x32\x19.gsdk.action.BuzzerSignal\"h\n\x0cStatusConfig\x12(\n\x08LEDState\x18\x01 \x03(\x0b\x32\x16.gsdk.status.LEDStatus\x12.\n\x0b\x42uzzerState\x18\x02 \x03(\x0b\x32\x19.gsdk.status.BuzzerStatus\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\">\n\x11GetConfigResponse\x12)\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x19.gsdk.status.StatusConfig\"O\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.gsdk.status.StatusConfig\"\x13\n\x11SetConfigResponse\"U\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.gsdk.status.StatusConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\xce\x03\n\x0c\x44\x65viceStatus\x12\x18\n\x14\x44\x45VICE_STATUS_NORMAL\x10\x00\x12\x18\n\x14\x44\x45VICE_STATUS_LOCKED\x10\x01\x12\x1b\n\x17\x44\x45VICE_STATUS_RTC_ERROR\x10\x02\x12\x1f\n\x1b\x44\x45VICE_STATUS_WAITING_INPUT\x10\x03\x12\x1e\n\x1a\x44\x45VICE_STATUS_WAITING_DHCP\x10\x04\x12\x1d\n\x19\x44\x45VICE_STATUS_SCAN_FINGER\x10\x05\x12\x1b\n\x17\x44\x45VICE_STATUS_SCAN_CARD\x10\x06\x12\x19\n\x15\x44\x45VICE_STATUS_SUCCESS\x10\x07\x12\x16\n\x12\x44\x45VICE_STATUS_FAIL\x10\x08\x12\x18\n\x14\x44\x45VICE_STATUS_DURESS\x10\t\x12%\n!DEVICE_STATUS_PROCESS_CONFIG_CARD\x10\n\x12%\n!DEVICE_STATUS_SUCCESS_CONFIG_CARD\x10\x0b\x12\x1b\n\x17\x44\x45VICE_STATUS_SCAN_FACE\x10\x0c\x12\x1b\n\x17\x44\x45VICE_STATUS_RESERVED3\x10\r\x12\x1b\n\x17\x44\x45VICE_STATUS_RESERVED4\x10\x0e\x32\xfb\x01\n\x06Status\x12J\n\tGetConfig\x12\x1d.gsdk.status.GetConfigRequest\x1a\x1e.gsdk.status.GetConfigResponse\x12J\n\tSetConfig\x12\x1d.gsdk.status.SetConfigRequest\x1a\x1e.gsdk.status.SetConfigResponse\x12Y\n\x0eSetConfigMulti\x12\".gsdk.status.SetConfigMultiRequest\x1a#.gsdk.status.SetConfigMultiResponseB5\n\x19\x63om.supremainc.sdk.statusP\x01Z\x16\x62iostar/service/statusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'status_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.supremainc.sdk.statusP\001Z\026biostar/service/status'
  _DEVICESTATUS._serialized_start=767
  _DEVICESTATUS._serialized_end=1229
  _LEDSTATUS._serialized_start=54
  _LEDSTATUS._serialized_end=170
  _BUZZERSTATUS._serialized_start=172
  _BUZZERSTATUS._serialized_end=294
  _STATUSCONFIG._serialized_start=296
  _STATUSCONFIG._serialized_end=400
  _GETCONFIGREQUEST._serialized_start=402
  _GETCONFIGREQUEST._serialized_end=438
  _GETCONFIGRESPONSE._serialized_start=440
  _GETCONFIGRESPONSE._serialized_end=502
  _SETCONFIGREQUEST._serialized_start=504
  _SETCONFIGREQUEST._serialized_end=583
  _SETCONFIGRESPONSE._serialized_start=585
  _SETCONFIGRESPONSE._serialized_end=604
  _SETCONFIGMULTIREQUEST._serialized_start=606
  _SETCONFIGMULTIREQUEST._serialized_end=691
  _SETCONFIGMULTIRESPONSE._serialized_start=693
  _SETCONFIGMULTIRESPONSE._serialized_end=764
  _STATUS._serialized_start=1232
  _STATUS._serialized_end=1483
# @@protoc_insertion_point(module_scope)
