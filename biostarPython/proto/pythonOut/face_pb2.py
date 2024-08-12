# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: face.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nface.proto\x12\tgsdk.face\x1a\terr.proto\"w\n\x08\x46\x61\x63\x65\x44\x61ta\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\x12\x11\n\ttemplates\x18\x03 \x03(\x0c\x12\x11\n\timageData\x18\x05 \x01(\x0c\x12\x13\n\x0birTemplates\x18\x07 \x03(\x0c\x12\x13\n\x0birImageData\x18\t \x01(\x0c\"X\n\x0bScanRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x37\n\x0f\x65nrollThreshold\x18\x02 \x01(\x0e\x32\x1e.gsdk.face.FaceEnrollThreshold\"5\n\x0cScanResponse\x12%\n\x08\x66\x61\x63\x65\x44\x61ta\x18\x02 \x01(\x0b\x32\x13.gsdk.face.FaceData\"G\n\x0e\x45xtractRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x11\n\timageData\x18\x02 \x01(\x0c\x12\x10\n\x08isWarped\x18\x03 \x01(\x08\"\'\n\x0f\x45xtractResponse\x12\x14\n\x0ctemplateData\x18\x02 \x01(\x0c\"@\n\x10NormalizeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x1a\n\x12unwrappedImageData\x18\x02 \x01(\x0c\"-\n\x11NormalizeResponse\x12\x18\n\x10wrappedImageData\x18\x01 \x01(\x0c\"%\n\tAuthGroup\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\'\n\x13GetAuthGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"@\n\x14GetAuthGroupResponse\x12(\n\nauthGroups\x18\x01 \x03(\x0b\x32\x14.gsdk.face.AuthGroup\"Q\n\x13\x41\x64\x64\x41uthGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12(\n\nauthGroups\x18\x02 \x03(\x0b\x32\x14.gsdk.face.AuthGroup\"\x16\n\x14\x41\x64\x64\x41uthGroupResponse\"W\n\x18\x41\x64\x64\x41uthGroupMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12(\n\nauthGroups\x18\x02 \x03(\x0b\x32\x14.gsdk.face.AuthGroup\"J\n\x19\x41\x64\x64\x41uthGroupMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"<\n\x16\x44\x65leteAuthGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x10\n\x08groupIDs\x18\x02 \x03(\r\"\x19\n\x17\x44\x65leteAuthGroupResponse\"B\n\x1b\x44\x65leteAuthGroupMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x10\n\x08groupIDs\x18\x02 \x03(\r\"M\n\x1c\x44\x65leteAuthGroupMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"-\n\x19\x44\x65leteAllAuthGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x1c\n\x1a\x44\x65leteAllAuthGroupResponse\"3\n\x1e\x44\x65leteAllAuthGroupMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"P\n\x1f\x44\x65leteAllAuthGroupMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\x86\x05\n\nFaceConfig\x12\x33\n\rsecurityLevel\x18\x01 \x01(\x0e\x32\x1c.gsdk.face.FaceSecurityLevel\x12\x35\n\x0elightCondition\x18\x02 \x01(\x0e\x32\x1d.gsdk.face.FaceLightCondition\x12\x37\n\x0f\x65nrollThreshold\x18\x03 \x01(\x0e\x32\x1e.gsdk.face.FaceEnrollThreshold\x12;\n\x11\x64\x65tectSensitivity\x18\x04 \x01(\x0e\x32 .gsdk.face.FaceDetectSensitivity\x12\x15\n\renrollTimeout\x18\x05 \x01(\r\x12)\n\x08LFDLevel\x18\x06 \x01(\x0e\x32\x17.gsdk.face.FaceLFDLevel\x12\x17\n\x0fquickEnrollment\x18\x07 \x01(\x08\x12\x33\n\rpreviewOption\x18\x08 \x01(\x0e\x32\x1c.gsdk.face.FacePreviewOption\x12\x16\n\x0e\x63heckDuplicate\x18\t \x01(\x08\x12\x33\n\roperationMode\x18\n \x01(\x0e\x32\x1c.gsdk.face.FaceOperationMode\x12\x13\n\x0bmaxRotation\x18\x0b \x01(\r\x12\x14\n\x0c\x66\x61\x63\x65WidthMin\x18\x0c \x01(\r\x12\x14\n\x0c\x66\x61\x63\x65WidthMax\x18\r \x01(\r\x12\x14\n\x0csearchRangeX\x18\x0e \x01(\r\x12\x18\n\x10searchRangeWidth\x18\x0f \x01(\r\x12\x19\n\x11\x64\x65tectDistanceMin\x18\x10 \x01(\r\x12\x19\n\x11\x64\x65tectDistanceMax\x18\x11 \x01(\r\x12\x12\n\nwideSearch\x18\x12 \x01(\x08\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\":\n\x11GetConfigResponse\x12%\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x15.gsdk.face.FaceConfig\"K\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.face.FaceConfig\"\x13\n\x11SetConfigResponse\"Q\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.face.FaceConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\xdd\x03\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x1a\n\x16\x44\x45\x46\x41ULT_ENROLL_TIMEOUT\x10<\x12\x1d\n\x19\x44\x45\x46\x41ULT_ENROLL_TIMEOUT_EX\x10\x14\x12\x18\n\x14\x44\x45\x46\x41ULT_MAX_ROTATION\x10\x0f\x12\"\n\x1e\x44\x45\x46\x41ULT_MIN_DETECTION_DISTANCE\x10\x1e\x12\"\n\x1e\x44\x45\x46\x41ULT_MAX_DETECTION_DISTANCE\x10\x64\x12\x16\n\x12MIN_ENROLL_TIMEOUT\x10\x1e\x12\x16\n\x12MAX_ENROLL_TIMEOUT\x10<\x12\x19\n\x15MIN_ENROLL_TIMEOUT_EX\x10\n\x12\x19\n\x15MAX_ENROLL_TIMEOUT_EX\x10\x14\x12\x14\n\x10MIN_MAX_ROTATION\x10\x00\x12\x14\n\x10MAX_MAX_ROTATION\x10\x1e\x12\x1e\n\x1aMIN_MIN_DETECTION_DISTANCE\x10\x1e\x12\x1e\n\x1aMAX_MIN_DETECTION_DISTANCE\x10\x64\x12\x1e\n\x1aMIN_MAX_DETECTION_DISTANCE\x10(\x12\x1f\n\x1aMAX_MAX_DETECTION_DISTANCE\x10\xff\x01\x1a\x02\x10\x01*S\n\x08\x46\x61\x63\x65\x46lag\x12\x16\n\x12\x42S2_FACE_FLAG_NONE\x10\x00\x12\x18\n\x14\x42S2_FACE_FLAG_WARPED\x10\x01\x12\x15\n\x10\x42S2_FACE_FLAG_EX\x10\x80\x02*\x95\x01\n\x11\x46\x61\x63\x65SecurityLevel\x12\x1c\n\x18\x42S2_FACE_SECURITY_NORMAL\x10\x00\x12\x1c\n\x18\x42S2_FACE_SECURITY_SECURE\x10\x01\x12!\n\x1d\x42S2_FACE_SECURITY_MORE_SECURE\x10\x02\x12\x1d\n\x19\x42S2_FACE_SECURITY_DEFAULT\x10\x00\x1a\x02\x10\x01*\x8a\x03\n\x13\x46\x61\x63\x65\x45nrollThreshold\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_0\x10\x00\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_1\x10\x01\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_2\x10\x02\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_3\x10\x03\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_4\x10\x04\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_5\x10\x05\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_6\x10\x06\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_7\x10\x07\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_8\x10\x08\x12\x1f\n\x1b\x42S2_FACE_ENROLL_THRESHOLD_9\x10\t\x12%\n!BS2_FACE_ENROLL_THRESHOLD_DEFAULT\x10\x04\x1a\x02\x10\x01*\xcf\x01\n\x12\x46\x61\x63\x65LightCondition\x12#\n\x1f\x42S2_FACE_LIGHT_CONDITION_INDOOR\x10\x00\x12$\n BS2_FACE_LIGHT_CONDITION_OUTDOOR\x10\x01\x12!\n\x1d\x42S2_FACE_LIGHT_CONDITION_AUTO\x10\x02\x12!\n\x1d\x42S2_FACE_LIGHT_CONDITION_DARK\x10\x03\x12$\n BS2_FACE_LIGHT_CONDITION_DEFAULT\x10\x00\x1a\x02\x10\x01*\xdc\x01\n\x15\x46\x61\x63\x65\x44\x65tectSensitivity\x12#\n\x1f\x42S2_FACE_DETECT_SENSITIVITY_OFF\x10\x00\x12#\n\x1f\x42S2_FACE_DETECT_SENSITIVITY_LOW\x10\x01\x12&\n\"BS2_FACE_DETECT_SENSITIVITY_MIDDLE\x10\x02\x12$\n BS2_FACE_DETECT_SENSITIVITY_HIGH\x10\x03\x12\'\n#BS2_FACE_DETECT_SENSITIVITY_DEFAULT\x10\x02\x1a\x02\x10\x01*\xa6\x01\n\x0c\x46\x61\x63\x65LFDLevel\x12\x1a\n\x16\x42S2_FACE_LFD_LEVEL_OFF\x10\x00\x12\x1a\n\x16\x42S2_FACE_LFD_LEVEL_LOW\x10\x01\x12\x1d\n\x19\x42S2_FACE_LFD_LEVEL_MIDDLE\x10\x02\x12\x1b\n\x17\x42S2_FACE_LFD_LEVEL_HIGH\x10\x03\x12\x1e\n\x1a\x42S2_FACE_LFD_LEVEL_DEFAULT\x10\x00\x1a\x02\x10\x01*\x86\x01\n\x11\x46\x61\x63\x65PreviewOption\x12\x19\n\x15\x42S2_FACE_PREVIEW_NONE\x10\x00\x12\x19\n\x15\x42S2_FACE_PREVIEW_HALF\x10\x01\x12\x19\n\x15\x42S2_FACE_PREVIEW_FULL\x10\x02\x12\x1c\n\x18\x42S2_FACE_PREVIEW_DEFAULT\x10\x01\x1a\x02\x10\x01*\xbc\x01\n\x11\x46\x61\x63\x65OperationMode\x12\"\n\x1e\x42S2_FACE_OPERATION_MODE_FUSION\x10\x00\x12\'\n#BS2_FACE_OPERATION_MODE_VISUAL_ONLY\x10\x01\x12\x31\n-BS2_FACE_OPERATION_MODE_VISUAL_AND_IR_FD_ONLY\x10\x02\x12#\n\x1f\x42S2_FACE_OPERATION_MODE_DEFAULT\x10\x00\x1a\x02\x10\x01\x32\xca\x08\n\x04\x46\x61\x63\x65\x12\x37\n\x04Scan\x12\x16.gsdk.face.ScanRequest\x1a\x17.gsdk.face.ScanResponse\x12@\n\x07\x45xtract\x12\x19.gsdk.face.ExtractRequest\x1a\x1a.gsdk.face.ExtractResponse\x12\x46\n\tNormalize\x12\x1b.gsdk.face.NormalizeRequest\x1a\x1c.gsdk.face.NormalizeResponse\x12\x46\n\tGetConfig\x12\x1b.gsdk.face.GetConfigRequest\x1a\x1c.gsdk.face.GetConfigResponse\x12\x46\n\tSetConfig\x12\x1b.gsdk.face.SetConfigRequest\x1a\x1c.gsdk.face.SetConfigResponse\x12U\n\x0eSetConfigMulti\x12 .gsdk.face.SetConfigMultiRequest\x1a!.gsdk.face.SetConfigMultiResponse\x12O\n\x0cGetAuthGroup\x12\x1e.gsdk.face.GetAuthGroupRequest\x1a\x1f.gsdk.face.GetAuthGroupResponse\x12O\n\x0c\x41\x64\x64\x41uthGroup\x12\x1e.gsdk.face.AddAuthGroupRequest\x1a\x1f.gsdk.face.AddAuthGroupResponse\x12^\n\x11\x41\x64\x64\x41uthGroupMulti\x12#.gsdk.face.AddAuthGroupMultiRequest\x1a$.gsdk.face.AddAuthGroupMultiResponse\x12X\n\x0f\x44\x65leteAuthGroup\x12!.gsdk.face.DeleteAuthGroupRequest\x1a\".gsdk.face.DeleteAuthGroupResponse\x12g\n\x14\x44\x65leteAuthGroupMulti\x12&.gsdk.face.DeleteAuthGroupMultiRequest\x1a\'.gsdk.face.DeleteAuthGroupMultiResponse\x12\x61\n\x12\x44\x65leteAllAuthGroup\x12$.gsdk.face.DeleteAllAuthGroupRequest\x1a%.gsdk.face.DeleteAllAuthGroupResponse\x12p\n\x17\x44\x65leteAllAuthGroupMulti\x12).gsdk.face.DeleteAllAuthGroupMultiRequest\x1a*.gsdk.face.DeleteAllAuthGroupMultiResponseB1\n\x17\x63om.supremainc.sdk.faceP\x01Z\x14\x62iostar/service/faceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'face_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.supremainc.sdk.faceP\001Z\024biostar/service/face'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_FACESECURITYLEVEL']._loaded_options = None
  _globals['_FACESECURITYLEVEL']._serialized_options = b'\020\001'
  _globals['_FACEENROLLTHRESHOLD']._loaded_options = None
  _globals['_FACEENROLLTHRESHOLD']._serialized_options = b'\020\001'
  _globals['_FACELIGHTCONDITION']._loaded_options = None
  _globals['_FACELIGHTCONDITION']._serialized_options = b'\020\001'
  _globals['_FACEDETECTSENSITIVITY']._loaded_options = None
  _globals['_FACEDETECTSENSITIVITY']._serialized_options = b'\020\001'
  _globals['_FACELFDLEVEL']._loaded_options = None
  _globals['_FACELFDLEVEL']._serialized_options = b'\020\001'
  _globals['_FACEPREVIEWOPTION']._loaded_options = None
  _globals['_FACEPREVIEWOPTION']._serialized_options = b'\020\001'
  _globals['_FACEOPERATIONMODE']._loaded_options = None
  _globals['_FACEOPERATIONMODE']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=2397
  _globals['_ENUM']._serialized_end=2874
  _globals['_FACEFLAG']._serialized_start=2876
  _globals['_FACEFLAG']._serialized_end=2959
  _globals['_FACESECURITYLEVEL']._serialized_start=2962
  _globals['_FACESECURITYLEVEL']._serialized_end=3111
  _globals['_FACEENROLLTHRESHOLD']._serialized_start=3114
  _globals['_FACEENROLLTHRESHOLD']._serialized_end=3508
  _globals['_FACELIGHTCONDITION']._serialized_start=3511
  _globals['_FACELIGHTCONDITION']._serialized_end=3718
  _globals['_FACEDETECTSENSITIVITY']._serialized_start=3721
  _globals['_FACEDETECTSENSITIVITY']._serialized_end=3941
  _globals['_FACELFDLEVEL']._serialized_start=3944
  _globals['_FACELFDLEVEL']._serialized_end=4110
  _globals['_FACEPREVIEWOPTION']._serialized_start=4113
  _globals['_FACEPREVIEWOPTION']._serialized_end=4247
  _globals['_FACEOPERATIONMODE']._serialized_start=4250
  _globals['_FACEOPERATIONMODE']._serialized_end=4438
  _globals['_FACEDATA']._serialized_start=36
  _globals['_FACEDATA']._serialized_end=155
  _globals['_SCANREQUEST']._serialized_start=157
  _globals['_SCANREQUEST']._serialized_end=245
  _globals['_SCANRESPONSE']._serialized_start=247
  _globals['_SCANRESPONSE']._serialized_end=300
  _globals['_EXTRACTREQUEST']._serialized_start=302
  _globals['_EXTRACTREQUEST']._serialized_end=373
  _globals['_EXTRACTRESPONSE']._serialized_start=375
  _globals['_EXTRACTRESPONSE']._serialized_end=414
  _globals['_NORMALIZEREQUEST']._serialized_start=416
  _globals['_NORMALIZEREQUEST']._serialized_end=480
  _globals['_NORMALIZERESPONSE']._serialized_start=482
  _globals['_NORMALIZERESPONSE']._serialized_end=527
  _globals['_AUTHGROUP']._serialized_start=529
  _globals['_AUTHGROUP']._serialized_end=566
  _globals['_GETAUTHGROUPREQUEST']._serialized_start=568
  _globals['_GETAUTHGROUPREQUEST']._serialized_end=607
  _globals['_GETAUTHGROUPRESPONSE']._serialized_start=609
  _globals['_GETAUTHGROUPRESPONSE']._serialized_end=673
  _globals['_ADDAUTHGROUPREQUEST']._serialized_start=675
  _globals['_ADDAUTHGROUPREQUEST']._serialized_end=756
  _globals['_ADDAUTHGROUPRESPONSE']._serialized_start=758
  _globals['_ADDAUTHGROUPRESPONSE']._serialized_end=780
  _globals['_ADDAUTHGROUPMULTIREQUEST']._serialized_start=782
  _globals['_ADDAUTHGROUPMULTIREQUEST']._serialized_end=869
  _globals['_ADDAUTHGROUPMULTIRESPONSE']._serialized_start=871
  _globals['_ADDAUTHGROUPMULTIRESPONSE']._serialized_end=945
  _globals['_DELETEAUTHGROUPREQUEST']._serialized_start=947
  _globals['_DELETEAUTHGROUPREQUEST']._serialized_end=1007
  _globals['_DELETEAUTHGROUPRESPONSE']._serialized_start=1009
  _globals['_DELETEAUTHGROUPRESPONSE']._serialized_end=1034
  _globals['_DELETEAUTHGROUPMULTIREQUEST']._serialized_start=1036
  _globals['_DELETEAUTHGROUPMULTIREQUEST']._serialized_end=1102
  _globals['_DELETEAUTHGROUPMULTIRESPONSE']._serialized_start=1104
  _globals['_DELETEAUTHGROUPMULTIRESPONSE']._serialized_end=1181
  _globals['_DELETEALLAUTHGROUPREQUEST']._serialized_start=1183
  _globals['_DELETEALLAUTHGROUPREQUEST']._serialized_end=1228
  _globals['_DELETEALLAUTHGROUPRESPONSE']._serialized_start=1230
  _globals['_DELETEALLAUTHGROUPRESPONSE']._serialized_end=1258
  _globals['_DELETEALLAUTHGROUPMULTIREQUEST']._serialized_start=1260
  _globals['_DELETEALLAUTHGROUPMULTIREQUEST']._serialized_end=1311
  _globals['_DELETEALLAUTHGROUPMULTIRESPONSE']._serialized_start=1313
  _globals['_DELETEALLAUTHGROUPMULTIRESPONSE']._serialized_end=1393
  _globals['_FACECONFIG']._serialized_start=1396
  _globals['_FACECONFIG']._serialized_end=2042
  _globals['_GETCONFIGREQUEST']._serialized_start=2044
  _globals['_GETCONFIGREQUEST']._serialized_end=2080
  _globals['_GETCONFIGRESPONSE']._serialized_start=2082
  _globals['_GETCONFIGRESPONSE']._serialized_end=2140
  _globals['_SETCONFIGREQUEST']._serialized_start=2142
  _globals['_SETCONFIGREQUEST']._serialized_end=2217
  _globals['_SETCONFIGRESPONSE']._serialized_start=2219
  _globals['_SETCONFIGRESPONSE']._serialized_end=2238
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=2240
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=2321
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=2323
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=2394
  _globals['_FACE']._serialized_start=4441
  _globals['_FACE']._serialized_end=5539
# @@protoc_insertion_point(module_scope)
