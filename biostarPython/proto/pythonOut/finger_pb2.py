# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: finger.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x66inger.proto\x12\x0bgsdk.finger\x1a\terr.proto\"<\n\nFingerData\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\x12\x11\n\ttemplates\x18\x03 \x03(\x0c\"n\n\x0bScanRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x33\n\x0etemplateFormat\x18\x02 \x01(\x0e\x32\x1b.gsdk.finger.TemplateFormat\x12\x18\n\x10qualityThreshold\x18\x03 \x01(\r\":\n\x0cScanResponse\x12\x14\n\x0ctemplateData\x18\x01 \x01(\x0c\x12\x14\n\x0cqualityScore\x18\x02 \x01(\r\"#\n\x0fGetImageRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"$\n\x10GetImageResponse\x12\x10\n\x08\x42MPImage\x18\x01 \x01(\x0c\"N\n\rVerifyRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12+\n\nfingerData\x18\x02 \x01(\x0b\x32\x17.gsdk.finger.FingerData\"\x10\n\x0eVerifyResponse\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\">\n\x11GetConfigResponse\x12)\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x19.gsdk.finger.FingerConfig\"O\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.gsdk.finger.FingerConfig\"\x13\n\x11SetConfigResponse\"U\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12)\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.gsdk.finger.FingerConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\x80\x03\n\x0c\x46ingerConfig\x12\x31\n\rsecurityLevel\x18\x01 \x01(\x0e\x32\x1a.gsdk.finger.SecurityLevel\x12\'\n\x08\x66\x61stMode\x18\x02 \x01(\x0e\x32\x15.gsdk.finger.FastMode\x12-\n\x0bsensitivity\x18\x03 \x01(\x0e\x32\x18.gsdk.finger.Sensitivity\x12+\n\nsensorMode\x18\x04 \x01(\x0e\x32\x17.gsdk.finger.SensorMode\x12\x33\n\x0etemplateFormat\x18\x05 \x01(\x0e\x32\x1b.gsdk.finger.TemplateFormat\x12\x13\n\x0bscanTimeout\x18\x06 \x01(\x05\x12\x1a\n\x12\x61\x64vancedEnrollment\x18\x07 \x01(\x08\x12\x11\n\tshowImage\x18\x08 \x01(\x08\x12\'\n\x08LFDLevel\x18\t \x01(\x0e\x32\x15.gsdk.finger.LFDLevel\x12\x16\n\x0e\x63heckDuplicate\x18\n \x01(\x08*o\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x18\n\x14\x44\x45\x46\x41ULT_SCAN_TIMEOUT\x10\n\x12\x14\n\x10MIN_SCAN_TIMEOUT\x10\x01\x12\x14\n\x10MAX_SCAN_TIMEOUT\x10\x14*`\n\x0eTemplateFormat\x12\x1b\n\x17TEMPLATE_FORMAT_SUPREMA\x10\x00\x12\x17\n\x13TEMPLATE_FORMAT_ISO\x10\x01\x12\x18\n\x14TEMPLATE_FORMAT_ANSI\x10\x02*B\n\nFingerFlag\x12\x18\n\x14\x42S2_FINGER_FLAG_NONE\x10\x00\x12\x1a\n\x16\x42S2_FINGER_FLAG_DURESS\x10\x01*W\n\rSecurityLevel\x12\n\n\x06SECURE\x10\x00\x12\x0f\n\x0bMORE_SECURE\x10\x01\x12\x0f\n\x0bMOST_SECURE\x10\x02\x12\x14\n\x10\x44\x45\x46\x41ULT_SECURITY\x10\x00\x1a\x02\x10\x01*R\n\x08\x46\x61stMode\x12\r\n\tAUTOMATIC\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06\x46\x41STER\x10\x02\x12\x0b\n\x07\x46\x41STEST\x10\x03\x12\x10\n\x0c\x44\x45\x46\x41ULT_FAST\x10\x00\x1a\x02\x10\x01*\x85\x02\n\x0bSensitivity\x12\x14\n\x10LOWEST_SENSITIVE\x10\x00\x12\x14\n\x10LEVEL0_SENSITIVE\x10\x00\x12\x14\n\x10LEVEL1_SENSITIVE\x10\x01\x12\x14\n\x10LEVEL2_SENSITIVE\x10\x02\x12\x14\n\x10LEVEL3_SENSITIVE\x10\x03\x12\x14\n\x10LEVEL4_SENSITIVE\x10\x04\x12\x14\n\x10LEVEL5_SENSITIVE\x10\x05\x12\x14\n\x10LEVEL6_SENSITIVE\x10\x06\x12\x14\n\x10LEVEL7_SENSITIVE\x10\x07\x12\x15\n\x11HIGHEST_SENSITIVE\x10\x07\x12\x15\n\x11\x44\x45\x46\x41ULT_SENSITITY\x10\x07\x1a\x02\x10\x01*T\n\nSensorMode\x12\r\n\tALWAYS_ON\x10\x00\x12\x1a\n\x16\x41\x43TIVATED_BY_PROXIMITY\x10\x01\x12\x17\n\x13\x44\x45\x46\x41ULT_SENSOR_MODE\x10\x00\x1a\x02\x10\x01*[\n\x08LFDLevel\x12\x0c\n\x08NOT_USED\x10\x00\x12\n\n\x06STRICT\x10\x01\x12\x0f\n\x0bMORE_STRICT\x10\x02\x12\x0f\n\x0bMOST_STRICT\x10\x03\x12\x0f\n\x0b\x44\x45\x46\x41ULT_LFD\x10\x00\x1a\x02\x10\x01\x32\xc4\x03\n\x06\x46inger\x12;\n\x04Scan\x12\x18.gsdk.finger.ScanRequest\x1a\x19.gsdk.finger.ScanResponse\x12G\n\x08GetImage\x12\x1c.gsdk.finger.GetImageRequest\x1a\x1d.gsdk.finger.GetImageResponse\x12\x41\n\x06Verify\x12\x1a.gsdk.finger.VerifyRequest\x1a\x1b.gsdk.finger.VerifyResponse\x12J\n\tGetConfig\x12\x1d.gsdk.finger.GetConfigRequest\x1a\x1e.gsdk.finger.GetConfigResponse\x12J\n\tSetConfig\x12\x1d.gsdk.finger.SetConfigRequest\x1a\x1e.gsdk.finger.SetConfigResponse\x12Y\n\x0eSetConfigMulti\x12\".gsdk.finger.SetConfigMultiRequest\x1a#.gsdk.finger.SetConfigMultiResponseB5\n\x19\x63om.supremainc.sdk.fingerP\x01Z\x16\x62iostar/service/fingerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'finger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.supremainc.sdk.fingerP\001Z\026biostar/service/finger'
  _globals['_SECURITYLEVEL']._loaded_options = None
  _globals['_SECURITYLEVEL']._serialized_options = b'\020\001'
  _globals['_FASTMODE']._loaded_options = None
  _globals['_FASTMODE']._serialized_options = b'\020\001'
  _globals['_SENSITIVITY']._loaded_options = None
  _globals['_SENSITIVITY']._serialized_options = b'\020\001'
  _globals['_SENSORMODE']._loaded_options = None
  _globals['_SENSORMODE']._serialized_options = b'\020\001'
  _globals['_LFDLEVEL']._loaded_options = None
  _globals['_LFDLEVEL']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=1198
  _globals['_ENUM']._serialized_end=1309
  _globals['_TEMPLATEFORMAT']._serialized_start=1311
  _globals['_TEMPLATEFORMAT']._serialized_end=1407
  _globals['_FINGERFLAG']._serialized_start=1409
  _globals['_FINGERFLAG']._serialized_end=1475
  _globals['_SECURITYLEVEL']._serialized_start=1477
  _globals['_SECURITYLEVEL']._serialized_end=1564
  _globals['_FASTMODE']._serialized_start=1566
  _globals['_FASTMODE']._serialized_end=1648
  _globals['_SENSITIVITY']._serialized_start=1651
  _globals['_SENSITIVITY']._serialized_end=1912
  _globals['_SENSORMODE']._serialized_start=1914
  _globals['_SENSORMODE']._serialized_end=1998
  _globals['_LFDLEVEL']._serialized_start=2000
  _globals['_LFDLEVEL']._serialized_end=2091
  _globals['_FINGERDATA']._serialized_start=40
  _globals['_FINGERDATA']._serialized_end=100
  _globals['_SCANREQUEST']._serialized_start=102
  _globals['_SCANREQUEST']._serialized_end=212
  _globals['_SCANRESPONSE']._serialized_start=214
  _globals['_SCANRESPONSE']._serialized_end=272
  _globals['_GETIMAGEREQUEST']._serialized_start=274
  _globals['_GETIMAGEREQUEST']._serialized_end=309
  _globals['_GETIMAGERESPONSE']._serialized_start=311
  _globals['_GETIMAGERESPONSE']._serialized_end=347
  _globals['_VERIFYREQUEST']._serialized_start=349
  _globals['_VERIFYREQUEST']._serialized_end=427
  _globals['_VERIFYRESPONSE']._serialized_start=429
  _globals['_VERIFYRESPONSE']._serialized_end=445
  _globals['_GETCONFIGREQUEST']._serialized_start=447
  _globals['_GETCONFIGREQUEST']._serialized_end=483
  _globals['_GETCONFIGRESPONSE']._serialized_start=485
  _globals['_GETCONFIGRESPONSE']._serialized_end=547
  _globals['_SETCONFIGREQUEST']._serialized_start=549
  _globals['_SETCONFIGREQUEST']._serialized_end=628
  _globals['_SETCONFIGRESPONSE']._serialized_start=630
  _globals['_SETCONFIGRESPONSE']._serialized_end=649
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=651
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=736
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=738
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=809
  _globals['_FINGERCONFIG']._serialized_start=812
  _globals['_FINGERCONFIG']._serialized_end=1196
  _globals['_FINGER']._serialized_start=2094
  _globals['_FINGER']._serialized_end=2546
# @@protoc_insertion_point(module_scope)
