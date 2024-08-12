# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\tgsdk.auth\x1a\terr.proto\"C\n\x08Operator\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\'\n\x05level\x18\x02 \x01(\x0e\x32\x18.gsdk.auth.OperatorLevel\"E\n\x0c\x41uthSchedule\x12!\n\x04mode\x18\x01 \x01(\x0e\x32\x13.gsdk.auth.AuthMode\x12\x12\n\nscheduleID\x18\x02 \x01(\r\"\x85\x03\n\nAuthConfig\x12.\n\rauthSchedules\x18\x01 \x03(\x0b\x32\x17.gsdk.auth.AuthSchedule\x12\x14\n\x0cuseGlobalAPB\x18\x02 \x01(\x08\x12?\n\x13globalAPBFailAction\x18\x03 \x01(\x0e\x32\".gsdk.auth.GlobalAPBFailActionType\x12\x18\n\x10useGroupMatching\x18\x04 \x01(\x08\x12\x16\n\x0eusePrivateAuth\x18\x05 \x01(\x08\x12\x39\n\x12\x66\x61\x63\x65\x44\x65tectionLevel\x18\x06 \x01(\x0e\x32\x1d.gsdk.auth.FaceDetectionLevel\x12\x19\n\x11useServerMatching\x18\x07 \x01(\x08\x12\x15\n\ruseFullAccess\x18\x08 \x01(\x08\x12\x14\n\x0cmatchTimeout\x18\t \x01(\r\x12\x13\n\x0b\x61uthTimeout\x18\n \x01(\r\x12&\n\toperators\x18\x0b \x03(\x0b\x32\x13.gsdk.auth.Operator\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\":\n\x11GetConfigResponse\x12%\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x15.gsdk.auth.AuthConfig\"K\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.auth.AuthConfig\"\x13\n\x11SetConfigResponse\"Q\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.auth.AuthConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\xdf\x01\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x19\n\x15\x44\x45\x46\x41ULT_MATCH_TIMEOUT\x10\x05\x12\x18\n\x14\x44\x45\x46\x41ULT_AUTH_TIMEOUT\x10\n\x12!\n\x1d\x44\x45\x46\x41ULT_AUTH_TIMEOUT_FOR_FACE\x10\x05\x12\x15\n\x11MIN_MATCH_TIMEOUT\x10\x01\x12\x15\n\x11MAX_MATCH_TIMEOUT\x10\x14\x12\x14\n\x10MIN_AUTH_TIMEOUT\x10\x03\x12\x14\n\x10MAX_AUTH_TIMEOUT\x10\x14\x1a\x02\x10\x01*\xdb\x0e\n\x08\x41uthMode\x12\x1c\n\x18\x41UTH_MODE_BIOMETRIC_ONLY\x10\x00\x12\x1b\n\x17\x41UTH_MODE_BIOMETRIC_PIN\x10\x01\x12\x17\n\x13\x41UTH_MODE_CARD_ONLY\x10\x02\x12\x1c\n\x18\x41UTH_MODE_CARD_BIOMETRIC\x10\x03\x12\x16\n\x12\x41UTH_MODE_CARD_PIN\x10\x04\x12#\n\x1f\x41UTH_MODE_CARD_BIOMETRIC_OR_PIN\x10\x05\x12 \n\x1c\x41UTH_MODE_CARD_BIOMETRIC_PIN\x10\x06\x12\x1a\n\x16\x41UTH_MODE_ID_BIOMETRIC\x10\x07\x12\x14\n\x10\x41UTH_MODE_ID_PIN\x10\x08\x12!\n\x1d\x41UTH_MODE_ID_BIOMETRIC_OR_PIN\x10\t\x12\x1e\n\x1a\x41UTH_MODE_ID_BIOMETRIC_PIN\x10\n\x12\x13\n\x0e\x41UTH_MODE_NONE\x10\xff\x01\x12\x19\n\x14\x41UTH_MODE_PROHIBITED\x10\xfe\x01\x12\x1b\n\x17\x41UTH_EXT_MODE_FACE_ONLY\x10\x0b\x12\"\n\x1e\x41UTH_EXT_MODE_FACE_FINGERPRINT\x10\x0c\x12\x1a\n\x16\x41UTH_EXT_MODE_FACE_PIN\x10\r\x12)\n%AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN\x10\x0e\x12&\n\"AUTH_EXT_MODE_FACE_FINGERPRINT_PIN\x10\x0f\x12\"\n\x1e\x41UTH_EXT_MODE_FINGERPRINT_ONLY\x10\x10\x12\"\n\x1e\x41UTH_EXT_MODE_FINGERPRINT_FACE\x10\x11\x12!\n\x1d\x41UTH_EXT_MODE_FINGERPRINT_PIN\x10\x12\x12)\n%AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN\x10\x13\x12&\n\"AUTH_EXT_MODE_FINGERPRINT_FACE_PIN\x10\x14\x12\x1b\n\x17\x41UTH_EXT_MODE_CARD_ONLY\x10\x15\x12\x1b\n\x17\x41UTH_EXT_MODE_CARD_FACE\x10\x16\x12\"\n\x1e\x41UTH_EXT_MODE_CARD_FINGERPRINT\x10\x17\x12\x1a\n\x16\x41UTH_EXT_MODE_CARD_PIN\x10\x18\x12*\n&AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT\x10\x19\x12\"\n\x1e\x41UTH_EXT_MODE_CARD_FACE_OR_PIN\x10\x1a\x12)\n%AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN\x10\x1b\x12\x31\n-AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN\x10\x1c\x12\'\n#AUTH_EXT_MODE_CARD_FACE_FINGERPRINT\x10\x1d\x12\x1f\n\x1b\x41UTH_EXT_MODE_CARD_FACE_PIN\x10\x1e\x12\'\n#AUTH_EXT_MODE_CARD_FINGERPRINT_FACE\x10\x1f\x12&\n\"AUTH_EXT_MODE_CARD_FINGERPRINT_PIN\x10 \x12.\n*AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN\x10!\x12.\n*AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN\x10\"\x12.\n*AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN\x10#\x12\x19\n\x15\x41UTH_EXT_MODE_ID_FACE\x10$\x12 \n\x1c\x41UTH_EXT_MODE_ID_FINGERPRINT\x10%\x12\x18\n\x14\x41UTH_EXT_MODE_ID_PIN\x10&\x12(\n$AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT\x10\'\x12 \n\x1c\x41UTH_EXT_MODE_ID_FACE_OR_PIN\x10(\x12\'\n#AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN\x10)\x12/\n+AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN\x10*\x12%\n!AUTH_EXT_MODE_ID_FACE_FINGERPRINT\x10+\x12\x1d\n\x19\x41UTH_EXT_MODE_ID_FACE_PIN\x10,\x12%\n!AUTH_EXT_MODE_ID_FINGERPRINT_FACE\x10-\x12$\n AUTH_EXT_MODE_ID_FINGERPRINT_PIN\x10.\x12,\n(AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN\x10/\x12,\n(AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN\x10\x30\x12,\n(AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN\x10\x31*v\n\rOperatorLevel\x12\x17\n\x13OPERATOR_LEVEL_NONE\x10\x00\x12\x18\n\x14OPERATOR_LEVEL_ADMIN\x10\x01\x12\x19\n\x15OPERATOR_LEVEL_CONFIG\x10\x02\x12\x17\n\x13OPERATOR_LEVEL_USER\x10\x03*c\n\x12\x46\x61\x63\x65\x44\x65tectionLevel\x12\x17\n\x13\x46\x41\x43\x45_DETECTION_NONE\x10\x00\x12\x19\n\x15\x46\x41\x43\x45_DETECTION_NORMAL\x10\x01\x12\x19\n\x15\x46\x41\x43\x45_DETECTION_STRICT\x10\x02*|\n\x17GlobalAPBFailActionType\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_NONE\x10\x00\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_SOFT\x10\x01\x12\x1f\n\x1bGLOBAL_APB_FAIL_ACTION_HARD\x10\x02\x32\xed\x01\n\x04\x41uth\x12\x46\n\tGetConfig\x12\x1b.gsdk.auth.GetConfigRequest\x1a\x1c.gsdk.auth.GetConfigResponse\x12\x46\n\tSetConfig\x12\x1b.gsdk.auth.SetConfigRequest\x1a\x1c.gsdk.auth.SetConfigResponse\x12U\n\x0eSetConfigMulti\x12 .gsdk.auth.SetConfigMultiRequest\x1a!.gsdk.auth.SetConfigMultiResponseB1\n\x17\x63om.supremainc.sdk.authP\x01Z\x14\x62iostar/service/authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.supremainc.sdk.authP\001Z\024biostar/service/auth'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=921
  _globals['_ENUM']._serialized_end=1144
  _globals['_AUTHMODE']._serialized_start=1147
  _globals['_AUTHMODE']._serialized_end=3030
  _globals['_OPERATORLEVEL']._serialized_start=3032
  _globals['_OPERATORLEVEL']._serialized_end=3150
  _globals['_FACEDETECTIONLEVEL']._serialized_start=3152
  _globals['_FACEDETECTIONLEVEL']._serialized_end=3251
  _globals['_GLOBALAPBFAILACTIONTYPE']._serialized_start=3253
  _globals['_GLOBALAPBFAILACTIONTYPE']._serialized_end=3377
  _globals['_OPERATOR']._serialized_start=36
  _globals['_OPERATOR']._serialized_end=103
  _globals['_AUTHSCHEDULE']._serialized_start=105
  _globals['_AUTHSCHEDULE']._serialized_end=174
  _globals['_AUTHCONFIG']._serialized_start=177
  _globals['_AUTHCONFIG']._serialized_end=566
  _globals['_GETCONFIGREQUEST']._serialized_start=568
  _globals['_GETCONFIGREQUEST']._serialized_end=604
  _globals['_GETCONFIGRESPONSE']._serialized_start=606
  _globals['_GETCONFIGRESPONSE']._serialized_end=664
  _globals['_SETCONFIGREQUEST']._serialized_start=666
  _globals['_SETCONFIGREQUEST']._serialized_end=741
  _globals['_SETCONFIGRESPONSE']._serialized_start=743
  _globals['_SETCONFIGRESPONSE']._serialized_end=762
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=764
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=845
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=847
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=918
  _globals['_AUTH']._serialized_start=3380
  _globals['_AUTH']._serialized_end=3617
# @@protoc_insertion_point(module_scope)
