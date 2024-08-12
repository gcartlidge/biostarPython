# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thermal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rthermal.proto\x12\x0cgsdk.thermal\x1a\terr.proto\"G\n\x10ThermalCameraROI\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\"\xa2\x01\n\rThermalCamera\x12\x10\n\x08\x64istance\x18\x01 \x01(\r\x12\x14\n\x0c\x65missionRate\x18\x02 \x01(\r\x12+\n\x03ROI\x18\x03 \x01(\x0b\x32\x1e.gsdk.thermal.ThermalCameraROI\x12\x1b\n\x13useBodyCompensation\x18\x04 \x01(\x08\x12\x1f\n\x17\x63ompensationTemperature\x18\x05 \x01(\x05\"\xe7\x03\n\rThermalConfig\x12*\n\tcheckMode\x18\x01 \x01(\x0e\x32\x17.gsdk.thermal.CheckMode\x12,\n\ncheckOrder\x18\x02 \x01(\x0e\x32\x18.gsdk.thermal.CheckOrder\x12:\n\x11temperatureFormat\x18\x03 \x01(\x0e\x32\x1f.gsdk.thermal.TemperatureFormat\x12 \n\x18temperatureThresholdHigh\x18\x04 \x01(\r\x12\x18\n\x10\x61uditTemperature\x18\x05 \x01(\x08\x12\x16\n\x0euseRejectSound\x18\x06 \x01(\x08\x12\x19\n\x11useOverlapThermal\x18\x07 \x01(\x08\x12+\n\x06\x63\x61mera\x18\x08 \x01(\x0b\x32\x1b.gsdk.thermal.ThermalCamera\x12.\n\rmaskCheckMode\x18\t \x01(\x0e\x32\x17.gsdk.thermal.CheckMode\x12<\n\x12maskDetectionLevel\x18\n \x01(\x0e\x32 .gsdk.thermal.MaskDetectionLevel\x12\x15\n\ruseDynamicROI\x18\x0b \x01(\x08\x12\x1f\n\x17temperatureThresholdLow\x18\x0c \x01(\r\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"@\n\x11GetConfigResponse\x12+\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1b.gsdk.thermal.ThermalConfig\"Q\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12+\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1b.gsdk.thermal.ThermalConfig\"\x13\n\x11SetConfigResponse\"W\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12+\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1b.gsdk.thermal.ThermalConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\x8a\x01\n\x0eTemperatureLog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x11\n\teventCode\x18\x05 \x01(\r\x12\x0f\n\x07subCode\x18\x06 \x01(\r\x12\x13\n\x0btemperature\x18\x07 \x01(\r\"W\n\x18GetTemperatureLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\"T\n\x19GetTemperatureLogResponse\x12\x37\n\x11temperatureEvents\x18\x01 \x03(\x0b\x32\x1c.gsdk.thermal.TemperatureLog*\xe3\x04\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\'\n\"DEFAULT_HIGH_TEMPERATURE_THRESHOLD\x10\xd8\x1d\x12&\n!DEFAULT_LOW_TEMPERATURE_THRESHOLD\x10\x80\x19\x12\x14\n\x10\x44\x45\x46\x41ULT_DISTANCE\x10\x64\x12\x16\n\x12\x44\x45\x46\x41ULT_EMISSIVITY\x10\x62\x12\x11\n\rDEFAULT_ROI_X\x10\x1e\x12\x11\n\rDEFAULT_ROI_Y\x10\x19\x12\x15\n\x11\x44\x45\x46\x41ULT_ROI_WIDTH\x10\x32\x12\x16\n\x12\x44\x45\x46\x41ULT_ROI_HEIGHT\x10\x37\x12\x1d\n\x19MIN_TEMPERATURE_THRESHOLD\x10\x64\x12\x1d\n\x18MAX_EMPERATURE_THRESHOLD\x10\x94#\x12\x10\n\x0cMIN_DISTANCE\x10\x00\x12\x11\n\x0cMAX_DISTANCE\x10\xf4\x01\x12\x12\n\x0eMIN_EMISSIVITY\x10_\x12\x12\n\x0eMAX_EMISSIVITY\x10\x62\x12\r\n\tMIN_ROI_X\x10\x00\x12\r\n\tMAX_ROI_X\x10\x63\x12\r\n\tMIN_ROI_Y\x10\x00\x12\r\n\tMAX_ROI_Y\x10\x63\x12\x11\n\rMIN_ROI_WIDTH\x10\x00\x12\x11\n\rMAX_ROI_WIDTH\x10\x63\x12\x12\n\x0eMIN_ROI_HEIGHT\x10\x00\x12\x12\n\x0eMAX_ROI_HEIGHT\x10\x63\x12)\n\x1cMIN_COMPENSATION_TEMPERATURE\x10\xce\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12 \n\x1cMAX_COMPENSATION_TEMPERATURE\x10\x32\x1a\x02\x10\x01*(\n\tCheckMode\x12\x07\n\x03OFF\x10\x00\x12\x08\n\x04HARD\x10\x01\x12\x08\n\x04SOFT\x10\x02*?\n\nCheckOrder\x12\x0e\n\nAFTER_AUTH\x10\x00\x12\x0f\n\x0b\x42\x45\x46ORE_AUTH\x10\x01\x12\x10\n\x0cWITHOUT_AUTH\x10\x02*0\n\x11TemperatureFormat\x12\x0e\n\nFAHRENHEIT\x10\x00\x12\x0b\n\x07\x43\x45LSIUS\x10\x01*F\n\x12MaskDetectionLevel\x12\x0b\n\x07NOT_USE\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\r\n\tVERY_HIGH\x10\x03\x32\xe8\x02\n\x07Thermal\x12L\n\tGetConfig\x12\x1e.gsdk.thermal.GetConfigRequest\x1a\x1f.gsdk.thermal.GetConfigResponse\x12L\n\tSetConfig\x12\x1e.gsdk.thermal.SetConfigRequest\x1a\x1f.gsdk.thermal.SetConfigResponse\x12[\n\x0eSetConfigMulti\x12#.gsdk.thermal.SetConfigMultiRequest\x1a$.gsdk.thermal.SetConfigMultiResponse\x12\x64\n\x11GetTemperatureLog\x12&.gsdk.thermal.GetTemperatureLogRequest\x1a\'.gsdk.thermal.GetTemperatureLogResponseB7\n\x1a\x63om.supremainc.sdk.thermalP\x01Z\x17\x62iostar/service/thermalb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thermal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.supremainc.sdk.thermalP\001Z\027biostar/service/thermal'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=1457
  _globals['_ENUM']._serialized_end=2068
  _globals['_CHECKMODE']._serialized_start=2070
  _globals['_CHECKMODE']._serialized_end=2110
  _globals['_CHECKORDER']._serialized_start=2112
  _globals['_CHECKORDER']._serialized_end=2175
  _globals['_TEMPERATUREFORMAT']._serialized_start=2177
  _globals['_TEMPERATUREFORMAT']._serialized_end=2225
  _globals['_MASKDETECTIONLEVEL']._serialized_start=2227
  _globals['_MASKDETECTIONLEVEL']._serialized_end=2297
  _globals['_THERMALCAMERAROI']._serialized_start=42
  _globals['_THERMALCAMERAROI']._serialized_end=113
  _globals['_THERMALCAMERA']._serialized_start=116
  _globals['_THERMALCAMERA']._serialized_end=278
  _globals['_THERMALCONFIG']._serialized_start=281
  _globals['_THERMALCONFIG']._serialized_end=768
  _globals['_GETCONFIGREQUEST']._serialized_start=770
  _globals['_GETCONFIGREQUEST']._serialized_end=806
  _globals['_GETCONFIGRESPONSE']._serialized_start=808
  _globals['_GETCONFIGRESPONSE']._serialized_end=872
  _globals['_SETCONFIGREQUEST']._serialized_start=874
  _globals['_SETCONFIGREQUEST']._serialized_end=955
  _globals['_SETCONFIGRESPONSE']._serialized_start=957
  _globals['_SETCONFIGRESPONSE']._serialized_end=976
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=978
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=1065
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=1067
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=1138
  _globals['_TEMPERATURELOG']._serialized_start=1141
  _globals['_TEMPERATURELOG']._serialized_end=1279
  _globals['_GETTEMPERATURELOGREQUEST']._serialized_start=1281
  _globals['_GETTEMPERATURELOGREQUEST']._serialized_end=1368
  _globals['_GETTEMPERATURELOGRESPONSE']._serialized_start=1370
  _globals['_GETTEMPERATURELOGRESPONSE']._serialized_end=1454
  _globals['_THERMAL']._serialized_start=2300
  _globals['_THERMAL']._serialized_end=2660
# @@protoc_insertion_point(module_scope)
