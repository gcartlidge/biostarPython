# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2
from biostarPython.service import tna_pb2 as tna__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x65vent.proto\x12\ngsdk.event\x1a\terr.proto\x1a\ttna.proto\"Y\n\x0f\x44\x65tectInputInfo\x12\x12\n\nioDeviceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12$\n\x05value\x18\x03 \x01(\x0e\x32\x15.gsdk.event.PortValue\"Q\n\rAlarmZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0e\n\x06\x64oorID\x18\x02 \x01(\r\x12\x12\n\nioDeviceID\x18\x03 \x01(\r\x12\x0c\n\x04port\x18\x04 \x01(\r\"4\n\x11InterlockZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0f\n\x07\x64oorIDs\x18\x02 \x03(\r\"\x8e\x03\n\x08\x45ventLog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x10\n\x08\x65ntityID\x18\x05 \x01(\r\x12\x11\n\teventCode\x18\x06 \x01(\r\x12\x0f\n\x07subCode\x18\x07 \x01(\r\x12\x1d\n\x06TNAKey\x18\x08 \x01(\x0e\x32\r.gsdk.tna.Key\x12\x10\n\x08hasImage\x18\t \x01(\x08\x12\x17\n\x0f\x63hangedOnDevice\x18\n \x01(\x08\x12\x13\n\x0btemperature\x18\x0b \x01(\r\x12\x10\n\x08\x63\x61rdData\x18\x0c \x01(\x0c\x12.\n\tinputInfo\x18\r \x01(\x0b\x32\x1b.gsdk.event.DetectInputInfo\x12\x30\n\ralarmZoneInfo\x18\x0e \x01(\x0b\x32\x19.gsdk.event.AlarmZoneInfo\x12\x38\n\x11interlockZoneInfo\x18\x0f \x01(\x0b\x32\x1d.gsdk.event.InterlockZoneInfo\"s\n\x0b\x45ventFilter\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\r\x12\x11\n\teventCode\x18\x04 \x01(\r\x12\x1d\n\x06TNAKey\x18\x05 \x01(\x0e\x32\r.gsdk.tna.Key\"+\n\x17\x45nableMonitoringRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x1a\n\x18\x45nableMonitoringResponse\"1\n\x1c\x45nableMonitoringMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"N\n\x1d\x45nableMonitoringMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\",\n\x18\x44isableMonitoringRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x1b\n\x19\x44isableMonitoringResponse\"2\n\x1d\x44isableMonitoringMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"O\n\x1e\x44isableMonitoringMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"W\n\x1bSubscribeRealtimeLogRequest\x12\x11\n\tqueueSize\x18\x01 \x01(\x05\x12\x11\n\tdeviceIDs\x18\x02 \x03(\r\x12\x12\n\neventCodes\x18\x03 \x03(\r\"1\n\x1cSubscribeRealtimeLogResponse\x12\x11\n\tlogChanID\x18\x01 \x01(\t\"L\n\rGetLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\"6\n\x0eGetLogResponse\x12$\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x14.gsdk.event.EventLog\"\x80\x01\n\x17GetLogWithFilterRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\x12(\n\x07\x66ilters\x18\x04 \x03(\x0b\x32\x17.gsdk.event.EventFilter\"@\n\x18GetLogWithFilterResponse\x12$\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x14.gsdk.event.EventLog\"\x81\x01\n\x08ImageLog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x11\n\teventCode\x18\x05 \x01(\r\x12\x0f\n\x07subCode\x18\x06 \x01(\r\x12\x10\n\x08JPGImage\x18\x07 \x01(\x0c\"Q\n\x12GetImageLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\"@\n\x13GetImageLogResponse\x12)\n\x0bimageEvents\x18\x01 \x03(\x0b\x32\x14.gsdk.event.ImageLog\"4\n\x0bImageFilter\x12\x11\n\teventCode\x18\x01 \x01(\r\x12\x12\n\nscheduleID\x18\x02 \x01(\r\")\n\x15GetImageFilterRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"B\n\x16GetImageFilterResponse\x12(\n\x07\x66ilters\x18\x01 \x03(\x0b\x32\x17.gsdk.event.ImageFilter\"S\n\x15SetImageFilterRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12(\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x17.gsdk.event.ImageFilter\"\x18\n\x16SetImageFilterResponse\"Y\n\x1aSetImageFilterMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12(\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x17.gsdk.event.ImageFilter\"L\n\x1bSetImageFilterMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"#\n\x0f\x43learLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x12\n\x10\x43learLogResponse\")\n\x14\x43learLogMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"F\n\x15\x43learLogMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*@\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x15\n\x11MAX_EVENT_FILTERS\x10 *L\n\tPortValue\x12\x08\n\x04OPEN\x10\x00\x12\n\n\x06\x43LOSED\x10\x01\x12\x14\n\x10SUPERVISED_SHORT\x10\x02\x12\x13\n\x0fSUPERVISED_OPEN\x10\x03\x32\xa7\t\n\x05\x45vent\x12]\n\x10\x45nableMonitoring\x12#.gsdk.event.EnableMonitoringRequest\x1a$.gsdk.event.EnableMonitoringResponse\x12l\n\x15\x45nableMonitoringMulti\x12(.gsdk.event.EnableMonitoringMultiRequest\x1a).gsdk.event.EnableMonitoringMultiResponse\x12`\n\x11\x44isableMonitoring\x12$.gsdk.event.DisableMonitoringRequest\x1a%.gsdk.event.DisableMonitoringResponse\x12o\n\x16\x44isableMonitoringMulti\x12).gsdk.event.DisableMonitoringMultiRequest\x1a*.gsdk.event.DisableMonitoringMultiResponse\x12W\n\x14SubscribeRealtimeLog\x12\'.gsdk.event.SubscribeRealtimeLogRequest\x1a\x14.gsdk.event.EventLog0\x01\x12?\n\x06GetLog\x12\x19.gsdk.event.GetLogRequest\x1a\x1a.gsdk.event.GetLogResponse\x12]\n\x10GetLogWithFilter\x12#.gsdk.event.GetLogWithFilterRequest\x1a$.gsdk.event.GetLogWithFilterResponse\x12N\n\x0bGetImageLog\x12\x1e.gsdk.event.GetImageLogRequest\x1a\x1f.gsdk.event.GetImageLogResponse\x12W\n\x0eGetImageFilter\x12!.gsdk.event.GetImageFilterRequest\x1a\".gsdk.event.GetImageFilterResponse\x12W\n\x0eSetImageFilter\x12!.gsdk.event.SetImageFilterRequest\x1a\".gsdk.event.SetImageFilterResponse\x12\x66\n\x13SetImageFilterMulti\x12&.gsdk.event.SetImageFilterMultiRequest\x1a\'.gsdk.event.SetImageFilterMultiResponse\x12\x45\n\x08\x43learLog\x12\x1b.gsdk.event.ClearLogRequest\x1a\x1c.gsdk.event.ClearLogResponse\x12T\n\rClearLogMulti\x12 .gsdk.event.ClearLogMultiRequest\x1a!.gsdk.event.ClearLogMultiResponseB3\n\x18\x63om.supremainc.sdk.eventP\x01Z\x15\x62iostar/service/eventb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.supremainc.sdk.eventP\001Z\025biostar/service/event'
  _globals['_ENUM']._serialized_start=2576
  _globals['_ENUM']._serialized_end=2640
  _globals['_PORTVALUE']._serialized_start=2642
  _globals['_PORTVALUE']._serialized_end=2718
  _globals['_DETECTINPUTINFO']._serialized_start=49
  _globals['_DETECTINPUTINFO']._serialized_end=138
  _globals['_ALARMZONEINFO']._serialized_start=140
  _globals['_ALARMZONEINFO']._serialized_end=221
  _globals['_INTERLOCKZONEINFO']._serialized_start=223
  _globals['_INTERLOCKZONEINFO']._serialized_end=275
  _globals['_EVENTLOG']._serialized_start=278
  _globals['_EVENTLOG']._serialized_end=676
  _globals['_EVENTFILTER']._serialized_start=678
  _globals['_EVENTFILTER']._serialized_end=793
  _globals['_ENABLEMONITORINGREQUEST']._serialized_start=795
  _globals['_ENABLEMONITORINGREQUEST']._serialized_end=838
  _globals['_ENABLEMONITORINGRESPONSE']._serialized_start=840
  _globals['_ENABLEMONITORINGRESPONSE']._serialized_end=866
  _globals['_ENABLEMONITORINGMULTIREQUEST']._serialized_start=868
  _globals['_ENABLEMONITORINGMULTIREQUEST']._serialized_end=917
  _globals['_ENABLEMONITORINGMULTIRESPONSE']._serialized_start=919
  _globals['_ENABLEMONITORINGMULTIRESPONSE']._serialized_end=997
  _globals['_DISABLEMONITORINGREQUEST']._serialized_start=999
  _globals['_DISABLEMONITORINGREQUEST']._serialized_end=1043
  _globals['_DISABLEMONITORINGRESPONSE']._serialized_start=1045
  _globals['_DISABLEMONITORINGRESPONSE']._serialized_end=1072
  _globals['_DISABLEMONITORINGMULTIREQUEST']._serialized_start=1074
  _globals['_DISABLEMONITORINGMULTIREQUEST']._serialized_end=1124
  _globals['_DISABLEMONITORINGMULTIRESPONSE']._serialized_start=1126
  _globals['_DISABLEMONITORINGMULTIRESPONSE']._serialized_end=1205
  _globals['_SUBSCRIBEREALTIMELOGREQUEST']._serialized_start=1207
  _globals['_SUBSCRIBEREALTIMELOGREQUEST']._serialized_end=1294
  _globals['_SUBSCRIBEREALTIMELOGRESPONSE']._serialized_start=1296
  _globals['_SUBSCRIBEREALTIMELOGRESPONSE']._serialized_end=1345
  _globals['_GETLOGREQUEST']._serialized_start=1347
  _globals['_GETLOGREQUEST']._serialized_end=1423
  _globals['_GETLOGRESPONSE']._serialized_start=1425
  _globals['_GETLOGRESPONSE']._serialized_end=1479
  _globals['_GETLOGWITHFILTERREQUEST']._serialized_start=1482
  _globals['_GETLOGWITHFILTERREQUEST']._serialized_end=1610
  _globals['_GETLOGWITHFILTERRESPONSE']._serialized_start=1612
  _globals['_GETLOGWITHFILTERRESPONSE']._serialized_end=1676
  _globals['_IMAGELOG']._serialized_start=1679
  _globals['_IMAGELOG']._serialized_end=1808
  _globals['_GETIMAGELOGREQUEST']._serialized_start=1810
  _globals['_GETIMAGELOGREQUEST']._serialized_end=1891
  _globals['_GETIMAGELOGRESPONSE']._serialized_start=1893
  _globals['_GETIMAGELOGRESPONSE']._serialized_end=1957
  _globals['_IMAGEFILTER']._serialized_start=1959
  _globals['_IMAGEFILTER']._serialized_end=2011
  _globals['_GETIMAGEFILTERREQUEST']._serialized_start=2013
  _globals['_GETIMAGEFILTERREQUEST']._serialized_end=2054
  _globals['_GETIMAGEFILTERRESPONSE']._serialized_start=2056
  _globals['_GETIMAGEFILTERRESPONSE']._serialized_end=2122
  _globals['_SETIMAGEFILTERREQUEST']._serialized_start=2124
  _globals['_SETIMAGEFILTERREQUEST']._serialized_end=2207
  _globals['_SETIMAGEFILTERRESPONSE']._serialized_start=2209
  _globals['_SETIMAGEFILTERRESPONSE']._serialized_end=2233
  _globals['_SETIMAGEFILTERMULTIREQUEST']._serialized_start=2235
  _globals['_SETIMAGEFILTERMULTIREQUEST']._serialized_end=2324
  _globals['_SETIMAGEFILTERMULTIRESPONSE']._serialized_start=2326
  _globals['_SETIMAGEFILTERMULTIRESPONSE']._serialized_end=2402
  _globals['_CLEARLOGREQUEST']._serialized_start=2404
  _globals['_CLEARLOGREQUEST']._serialized_end=2439
  _globals['_CLEARLOGRESPONSE']._serialized_start=2441
  _globals['_CLEARLOGRESPONSE']._serialized_end=2459
  _globals['_CLEARLOGMULTIREQUEST']._serialized_start=2461
  _globals['_CLEARLOGMULTIREQUEST']._serialized_end=2502
  _globals['_CLEARLOGMULTIRESPONSE']._serialized_start=2504
  _globals['_CLEARLOGMULTIRESPONSE']._serialized_end=2574
  _globals['_EVENT']._serialized_start=2721
  _globals['_EVENT']._serialized_end=3912
# @@protoc_insertion_point(module_scope)