# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tna.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttna.proto\x12\x08gsdk.tna\x1a\terr.proto\"|\n\tTNAConfig\x12\x1c\n\x04mode\x18\x01 \x01(\x0e\x32\x0e.gsdk.tna.Mode\x12\x1a\n\x03key\x18\x02 \x01(\x0e\x32\r.gsdk.tna.Key\x12\x12\n\nisRequired\x18\x03 \x01(\x08\x12\x11\n\tschedules\x18\x04 \x03(\r\x12\x0e\n\x06labels\x18\x05 \x03(\t\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"8\n\x11GetConfigResponse\x12#\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x13.gsdk.tna.TNAConfig\"I\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.gsdk.tna.TNAConfig\"\x13\n\x11SetConfigResponse\"O\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.gsdk.tna.TNAConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"&\n\x07JobCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\r\n\x05label\x18\x02 \x01(\t\"\x8c\x01\n\x06TNALog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x11\n\teventCode\x18\x05 \x01(\r\x12\x0f\n\x07subCode\x18\x06 \x01(\r\x12\x1d\n\x06TNAKey\x18\x07 \x01(\x0e\x32\r.gsdk.tna.Key\"e\n\x0eTNAEventFilter\x12\x11\n\tstartTime\x18\x01 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\r\x12\x0f\n\x07userIDs\x18\x03 \x03(\t\x12\x1e\n\x07TNAKeys\x18\x04 \x03(\x0e\x32\r.gsdk.tna.Key\"\x82\x01\n\nJobCodeLog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x11\n\teventCode\x18\x05 \x01(\r\x12\x0f\n\x07subCode\x18\x06 \x01(\r\x12\x0f\n\x07jobCode\x18\x07 \x01(\r\"[\n\x12JobCodeEventFilter\x12\x11\n\tstartTime\x18\x01 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\r\x12\x0f\n\x07userIDs\x18\x03 \x03(\t\x12\x10\n\x08jobCodes\x18\x04 \x03(\r\"y\n\x10GetTNALogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\x12(\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x18.gsdk.tna.TNAEventFilter\"8\n\x11GetTNALogResponse\x12#\n\tTNAEvents\x18\x01 \x03(\x0b\x32\x10.gsdk.tna.TNALog\"S\n\x14GetJobCodeLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\"D\n\x15GetJobCodeLogResponse\x12+\n\rjobCodeEvents\x18\x01 \x03(\x0b\x32\x14.gsdk.tna.JobCodeLog*L\n\x04Mode\x12\n\n\x06UNUSED\x10\x00\x12\x0b\n\x07\x42Y_USER\x10\x01\x12\x0f\n\x0b\x42Y_SCHEDULE\x10\x02\x12\x0f\n\x0bLAST_CHOICE\x10\x03\x12\t\n\x05\x46IXED\x10\x04*\xcd\x01\n\x03Key\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05KEY_1\x10\x01\x12\t\n\x05KEY_2\x10\x02\x12\t\n\x05KEY_3\x10\x03\x12\t\n\x05KEY_4\x10\x04\x12\t\n\x05KEY_5\x10\x05\x12\t\n\x05KEY_6\x10\x06\x12\t\n\x05KEY_7\x10\x07\x12\t\n\x05KEY_8\x10\x08\x12\t\n\x05KEY_9\x10\t\x12\n\n\x06KEY_10\x10\n\x12\n\n\x06KEY_11\x10\x0b\x12\n\n\x06KEY_12\x10\x0c\x12\n\n\x06KEY_13\x10\r\x12\n\n\x06KEY_14\x10\x0e\x12\n\n\x06KEY_15\x10\x0f\x12\n\n\x06KEY_16\x10\x10\x32\xfe\x02\n\x03TNA\x12\x44\n\tGetConfig\x12\x1a.gsdk.tna.GetConfigRequest\x1a\x1b.gsdk.tna.GetConfigResponse\x12\x44\n\tSetConfig\x12\x1a.gsdk.tna.SetConfigRequest\x1a\x1b.gsdk.tna.SetConfigResponse\x12S\n\x0eSetConfigMulti\x12\x1f.gsdk.tna.SetConfigMultiRequest\x1a .gsdk.tna.SetConfigMultiResponse\x12\x44\n\tGetTNALog\x12\x1a.gsdk.tna.GetTNALogRequest\x1a\x1b.gsdk.tna.GetTNALogResponse\x12P\n\rGetJobCodeLog\x12\x1e.gsdk.tna.GetJobCodeLogRequest\x1a\x1f.gsdk.tna.GetJobCodeLogResponseB/\n\x16\x63om.supremainc.sdk.tnaP\x01Z\x13\x62iostar/service/tnab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tna_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.supremainc.sdk.tnaP\001Z\023biostar/service/tna'
  _MODE._serialized_start=1354
  _MODE._serialized_end=1430
  _KEY._serialized_start=1433
  _KEY._serialized_end=1638
  _TNACONFIG._serialized_start=34
  _TNACONFIG._serialized_end=158
  _GETCONFIGREQUEST._serialized_start=160
  _GETCONFIGREQUEST._serialized_end=196
  _GETCONFIGRESPONSE._serialized_start=198
  _GETCONFIGRESPONSE._serialized_end=254
  _SETCONFIGREQUEST._serialized_start=256
  _SETCONFIGREQUEST._serialized_end=329
  _SETCONFIGRESPONSE._serialized_start=331
  _SETCONFIGRESPONSE._serialized_end=350
  _SETCONFIGMULTIREQUEST._serialized_start=352
  _SETCONFIGMULTIREQUEST._serialized_end=431
  _SETCONFIGMULTIRESPONSE._serialized_start=433
  _SETCONFIGMULTIRESPONSE._serialized_end=504
  _JOBCODE._serialized_start=506
  _JOBCODE._serialized_end=544
  _TNALOG._serialized_start=547
  _TNALOG._serialized_end=687
  _TNAEVENTFILTER._serialized_start=689
  _TNAEVENTFILTER._serialized_end=790
  _JOBCODELOG._serialized_start=793
  _JOBCODELOG._serialized_end=923
  _JOBCODEEVENTFILTER._serialized_start=925
  _JOBCODEEVENTFILTER._serialized_end=1016
  _GETTNALOGREQUEST._serialized_start=1018
  _GETTNALOGREQUEST._serialized_end=1139
  _GETTNALOGRESPONSE._serialized_start=1141
  _GETTNALOGRESPONSE._serialized_end=1197
  _GETJOBCODELOGREQUEST._serialized_start=1199
  _GETJOBCODELOGREQUEST._serialized_end=1282
  _GETJOBCODELOGRESPONSE._serialized_start=1284
  _GETJOBCODELOGRESPONSE._serialized_end=1352
  _TNA._serialized_start=1641
  _TNA._serialized_end=2023
# @@protoc_insertion_point(module_scope)
