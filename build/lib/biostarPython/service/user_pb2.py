# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
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
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import card_pb2 as card__pb2
from biostarPython.service import finger_pb2 as finger__pb2
from biostarPython.service import face_pb2 as face__pb2
from biostarPython.service import tna_pb2 as tna__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\tgsdk.user\x1a\ncard.proto\x1a\x0c\x66inger.proto\x1a\nface.proto\x1a\ttna.proto\x1a\terr.proto\"\x8b\x01\n\x07UserHdr\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x10\n\x08userFlag\x18\x02 \x01(\r\x12\x11\n\tnumOfCard\x18\x03 \x01(\x05\x12\x13\n\x0bnumOfFinger\x18\x04 \x01(\x05\x12\x11\n\tnumOfFace\x18\x05 \x01(\x05\x12\x13\n\x0b\x61uthGroupID\x18\x06 \x01(\r\x12\x12\n\nupdateMask\x18\x07 \x01(\r\"\"\n\x0eGetListRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"3\n\x0fGetListResponse\x12 \n\x04hdrs\x18\x01 \x03(\x0b\x32\x12.gsdk.user.UserHdr\"\x8b\x02\n\x0bUserSetting\x12\x11\n\tstartTime\x18\x01 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\r\x12\x19\n\x11\x62iometricAuthMode\x18\x03 \x01(\r\x12\x14\n\x0c\x63\x61rdAuthMode\x18\x04 \x01(\r\x12\x12\n\nIDAuthMode\x18\x05 \x01(\r\x12/\n\rsecurityLevel\x18\x06 \x01(\x0e\x32\x18.gsdk.user.SecurityLevel\x12\x17\n\x0f\x66\x61\x63\x65\x41uthExtMode\x18\x07 \x01(\r\x12\x19\n\x11\x66ingerAuthExtMode\x18\x08 \x01(\r\x12\x17\n\x0f\x63\x61rdAuthExtMode\x18\t \x01(\r\x12\x15\n\rIDAuthExtMode\x18\n \x01(\r\"\xb0\x02\n\x08UserInfo\x12\x1f\n\x03hdr\x18\x01 \x01(\x0b\x32\x12.gsdk.user.UserHdr\x12\'\n\x07setting\x18\x02 \x01(\x0b\x32\x16.gsdk.user.UserSetting\x12\x0c\n\x04name\x18\x03 \x01(\t\x12%\n\x05\x63\x61rds\x18\x04 \x03(\x0b\x32\x16.gsdk.card.CSNCardData\x12(\n\x07\x66ingers\x18\x05 \x03(\x0b\x32\x17.gsdk.finger.FingerData\x12\"\n\x05\x66\x61\x63\x65s\x18\x06 \x03(\x0b\x32\x13.gsdk.face.FaceData\x12\x16\n\x0e\x61\x63\x63\x65ssGroupIDs\x18\x07 \x03(\r\x12#\n\x08jobCodes\x18\x08 \x03(\x0b\x32\x11.gsdk.tna.JobCode\x12\x0b\n\x03PIN\x18\t \x01(\x0c\x12\r\n\x05photo\x18\n \x01(\x0c\"/\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"1\n\x0bGetResponse\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"H\n\x11GetPartialRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\x12\x10\n\x08infoMask\x18\x03 \x01(\r\"8\n\x12GetPartialResponse\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"X\n\rEnrollRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"\x10\n\x0e\x45nrollResponse\"^\n\x12\x45nrollMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"D\n\x13\x45nrollMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"E\n\rUpdateRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"\x10\n\x0eUpdateResponse\"K\n\x12UpdateMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"D\n\x13UpdateMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"\x10\n\x0e\x44\x65leteResponse\"8\n\x12\x44\x65leteMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"D\n\x13\x44\x65leteMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"*\n\x15\x44\x65leteAllMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"G\n\x16\x44\x65leteAllMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"A\n\x08UserCard\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12%\n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x16.gsdk.card.CSNCardData\"3\n\x0eGetCardRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"9\n\x0fGetCardResponse\x12&\n\tuserCards\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserCard\"J\n\x0eSetCardRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\tuserCards\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserCard\"\x11\n\x0fSetCardResponse\"P\n\x13SetCardMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\tuserCards\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserCard\"E\n\x14SetCardMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"F\n\nUserFinger\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12(\n\x07\x66ingers\x18\x02 \x03(\x0b\x32\x17.gsdk.finger.FingerData\"5\n\x10GetFingerRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"?\n\x11GetFingerResponse\x12*\n\x0buserFingers\x18\x01 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"P\n\x10SetFingerRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12*\n\x0buserFingers\x18\x02 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"\x13\n\x11SetFingerResponse\"V\n\x15SetFingerMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12*\n\x0buserFingers\x18\x02 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"G\n\x16SetFingerMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\">\n\x08UserFace\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\"\n\x05\x66\x61\x63\x65s\x18\x02 \x03(\x0b\x32\x13.gsdk.face.FaceData\"3\n\x0eGetFaceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"9\n\x0fGetFaceResponse\x12&\n\tuserFaces\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserFace\"J\n\x0eSetFaceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\tuserFaces\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserFace\"\x11\n\x0fSetFaceResponse\"P\n\x13SetFaceMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\tuserFaces\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserFace\"E\n\x14SetFaceMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"9\n\x0fUserAccessGroup\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63\x65ssGroupIDs\x18\x02 \x03(\r\":\n\x15GetAccessGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"N\n\x16GetAccessGroupResponse\x12\x34\n\x10userAccessGroups\x18\x01 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"_\n\x15SetAccessGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x34\n\x10userAccessGroups\x18\x02 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"\x18\n\x16SetAccessGroupResponse\"e\n\x1aSetAccessGroupMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x34\n\x10userAccessGroups\x18\x02 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"L\n\x1bSetAccessGroupMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"B\n\x0bUserJobCode\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12#\n\x08jobCodes\x18\x02 \x03(\x0b\x32\x11.gsdk.tna.JobCode\"6\n\x11GetJobCodeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"B\n\x12GetJobCodeResponse\x12,\n\x0cuserJobCodes\x18\x01 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"S\n\x11SetJobCodeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12,\n\x0cuserJobCodes\x18\x02 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"\x14\n\x12SetJobCodeResponse\"Y\n\x16SetJobCodeMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12,\n\x0cuserJobCodes\x18\x02 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"H\n\x17SetJobCodeMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\" \n\x11GetPINHashRequest\x12\x0b\n\x03PIN\x18\x01 \x01(\t\"%\n\x12GetPINHashResponse\x12\x0f\n\x07hashVal\x18\x01 \x01(\x0c\"8\n\x18GetPINHashWithKeyRequest\x12\x0b\n\x03PIN\x18\x01 \x01(\t\x12\x0f\n\x07hashKey\x18\x02 \x01(\x0c\"\'\n\x13GetStatisticRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\xa5\x01\n\rUserStatistic\x12\x12\n\nnumOfUsers\x18\x01 \x01(\r\x12\x12\n\nnumOfCards\x18\x02 \x01(\r\x12\x19\n\x11numOfFingerprints\x18\x03 \x01(\r\x12\x12\n\nnumOfFaces\x18\x04 \x01(\r\x12\x12\n\nnumOfNames\x18\x05 \x01(\r\x12\x13\n\x0bnumOfImages\x18\x06 \x01(\r\x12\x14\n\x0cnumOfPhrases\x18\x07 \x01(\r\"G\n\x14GetStatisticResponse\x12/\n\ruserStatistic\x18\x01 \x01(\x0b\x32\x18.gsdk.user.UserStatistic*\x9b\x01\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x15\n\x11MAX_ACCESS_GROUPS\x10\x10\x12\x11\n\rMAX_JOB_CODES\x10\x10\x12\x12\n\x0eMAX_PIN_LENGTH\x10 \x12\x18\n\x14MAX_JOB_LABEL_LENGTH\x10\x30\x12\x14\n\x0fMAX_NAME_LENGTH\x10\xc0\x01\x1a\x02\x10\x01*\x90\x01\n\x08UserFlag\x12\x12\n\x0eUSER_FLAG_NONE\x10\x00\x12\x15\n\x11USER_FLAG_CREATED\x10\x01\x12\x15\n\x11USER_FLAG_UPDATED\x10\x02\x12\x15\n\x11USER_FLAG_DELETED\x10\x04\x12\x17\n\x12USER_FLAG_DISABLED\x10\x80\x01\x12\x12\n\rUSER_FLAG_ALL\x10\xff\x01*\xd3\x01\n\nUpdateMask\x12\r\n\tKEEP_NONE\x10\x00\x12\x14\n\x10KEEP_USER_PHRASE\x10\x01\x12\x16\n\x12KEEP_USER_JOB_CODE\x10\x02\x12\x12\n\x0eKEEP_USER_NAME\x10\x04\x12\x13\n\x0fKEEP_USER_PHOTO\x10\x08\x12\x11\n\rKEEP_USER_PIN\x10\x10\x12\x12\n\x0eKEEP_USER_CARD\x10 \x12\x14\n\x10KEEP_USER_FINGER\x10@\x12\x13\n\x0eKEEP_USER_FACE\x10\x80\x01\x12\r\n\x08KEEP_ALL\x10\xff\x01*\xab\x01\n\rSecurityLevel\x12\x19\n\x15SECURITY_LEVEL_LOWEST\x10\x00\x12\x18\n\x14SECURITY_LEVEL_LOWER\x10\x01\x12\x16\n\x12SECURITY_LEVEL_LOW\x10\x02\x12\x19\n\x15SECURITY_LEVEL_NORMAL\x10\x03\x12\x17\n\x13SECURITY_LEVEL_HIGH\x10\x04\x12\x19\n\x15SECURITY_LEVEL_HIGHER\x10\x05*\xd6\x02\n\x08InfoMask\x12\x15\n\x11USER_MASK_ID_ONLY\x10\x00\x12\x11\n\rUSER_MASK_HDR\x10\x01\x12\x15\n\x11USER_MASK_SETTING\x10\x02\x12\x12\n\x0eUSER_MASK_NAME\x10\x04\x12\x13\n\x0fUSER_MASK_PHOTO\x10\x08\x12\x11\n\rUSER_MASK_PIN\x10\x10\x12\x12\n\x0eUSER_MASK_CARD\x10 \x12\x14\n\x10USER_MASK_FINGER\x10@\x12\x13\n\x0eUSER_MASK_FACE\x10\x80\x01\x12\x1b\n\x16USER_MASK_ACCESS_GROUP\x10\x80\x02\x12\x12\n\rUSER_MASK_JOB\x10\x80\x04\x12\x15\n\x10USER_MASK_PHRASE\x10\x80\x08\x12\x16\n\x11USER_MASK_FACE_EX\x10\x80\x10\x12\x19\n\x14USER_MASK_SETTING_EX\x10\x80 \x12\x13\n\rUSER_MASK_ALL\x10\xff\xff\x03\x32\x99\x11\n\x04User\x12@\n\x07GetList\x12\x19.gsdk.user.GetListRequest\x1a\x1a.gsdk.user.GetListResponse\x12\x34\n\x03Get\x12\x15.gsdk.user.GetRequest\x1a\x16.gsdk.user.GetResponse\x12I\n\nGetPartial\x12\x1c.gsdk.user.GetPartialRequest\x1a\x1d.gsdk.user.GetPartialResponse\x12=\n\x06\x45nroll\x12\x18.gsdk.user.EnrollRequest\x1a\x19.gsdk.user.EnrollResponse\x12L\n\x0b\x45nrollMulti\x12\x1d.gsdk.user.EnrollMultiRequest\x1a\x1e.gsdk.user.EnrollMultiResponse\x12=\n\x06Update\x12\x18.gsdk.user.UpdateRequest\x1a\x19.gsdk.user.UpdateResponse\x12L\n\x0bUpdateMulti\x12\x1d.gsdk.user.UpdateMultiRequest\x1a\x1e.gsdk.user.UpdateMultiResponse\x12=\n\x06\x44\x65lete\x12\x18.gsdk.user.DeleteRequest\x1a\x19.gsdk.user.DeleteResponse\x12L\n\x0b\x44\x65leteMulti\x12\x1d.gsdk.user.DeleteMultiRequest\x1a\x1e.gsdk.user.DeleteMultiResponse\x12\x46\n\tDeleteAll\x12\x1b.gsdk.user.DeleteAllRequest\x1a\x1c.gsdk.user.DeleteAllResponse\x12U\n\x0e\x44\x65leteAllMulti\x12 .gsdk.user.DeleteAllMultiRequest\x1a!.gsdk.user.DeleteAllMultiResponse\x12@\n\x07GetCard\x12\x19.gsdk.user.GetCardRequest\x1a\x1a.gsdk.user.GetCardResponse\x12@\n\x07SetCard\x12\x19.gsdk.user.SetCardRequest\x1a\x1a.gsdk.user.SetCardResponse\x12O\n\x0cSetCardMulti\x12\x1e.gsdk.user.SetCardMultiRequest\x1a\x1f.gsdk.user.SetCardMultiResponse\x12\x46\n\tGetFinger\x12\x1b.gsdk.user.GetFingerRequest\x1a\x1c.gsdk.user.GetFingerResponse\x12\x46\n\tSetFinger\x12\x1b.gsdk.user.SetFingerRequest\x1a\x1c.gsdk.user.SetFingerResponse\x12U\n\x0eSetFingerMulti\x12 .gsdk.user.SetFingerMultiRequest\x1a!.gsdk.user.SetFingerMultiResponse\x12@\n\x07GetFace\x12\x19.gsdk.user.GetFaceRequest\x1a\x1a.gsdk.user.GetFaceResponse\x12@\n\x07SetFace\x12\x19.gsdk.user.SetFaceRequest\x1a\x1a.gsdk.user.SetFaceResponse\x12O\n\x0cSetFaceMulti\x12\x1e.gsdk.user.SetFaceMultiRequest\x1a\x1f.gsdk.user.SetFaceMultiResponse\x12U\n\x0eGetAccessGroup\x12 .gsdk.user.GetAccessGroupRequest\x1a!.gsdk.user.GetAccessGroupResponse\x12U\n\x0eSetAccessGroup\x12 .gsdk.user.SetAccessGroupRequest\x1a!.gsdk.user.SetAccessGroupResponse\x12\x64\n\x13SetAccessGroupMulti\x12%.gsdk.user.SetAccessGroupMultiRequest\x1a&.gsdk.user.SetAccessGroupMultiResponse\x12I\n\nGetJobCode\x12\x1c.gsdk.user.GetJobCodeRequest\x1a\x1d.gsdk.user.GetJobCodeResponse\x12I\n\nSetJobCode\x12\x1c.gsdk.user.SetJobCodeRequest\x1a\x1d.gsdk.user.SetJobCodeResponse\x12X\n\x0fSetJobCodeMulti\x12!.gsdk.user.SetJobCodeMultiRequest\x1a\".gsdk.user.SetJobCodeMultiResponse\x12I\n\nGetPINHash\x12\x1c.gsdk.user.GetPINHashRequest\x1a\x1d.gsdk.user.GetPINHashResponse\x12W\n\x11GetPINHashWithKey\x12#.gsdk.user.GetPINHashWithKeyRequest\x1a\x1d.gsdk.user.GetPINHashResponse\x12O\n\x0cGetStatistic\x12\x1e.gsdk.user.GetStatisticRequest\x1a\x1f.gsdk.user.GetStatisticResponseB1\n\x17\x63om.supremainc.sdk.userP\x01Z\x14\x62iostar/service/userb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.supremainc.sdk.userP\001Z\024biostar/service/user'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=4697
  _globals['_ENUM']._serialized_end=4852
  _globals['_USERFLAG']._serialized_start=4855
  _globals['_USERFLAG']._serialized_end=4999
  _globals['_UPDATEMASK']._serialized_start=5002
  _globals['_UPDATEMASK']._serialized_end=5213
  _globals['_SECURITYLEVEL']._serialized_start=5216
  _globals['_SECURITYLEVEL']._serialized_end=5387
  _globals['_INFOMASK']._serialized_start=5390
  _globals['_INFOMASK']._serialized_end=5732
  _globals['_USERHDR']._serialized_start=86
  _globals['_USERHDR']._serialized_end=225
  _globals['_GETLISTREQUEST']._serialized_start=227
  _globals['_GETLISTREQUEST']._serialized_end=261
  _globals['_GETLISTRESPONSE']._serialized_start=263
  _globals['_GETLISTRESPONSE']._serialized_end=314
  _globals['_USERSETTING']._serialized_start=317
  _globals['_USERSETTING']._serialized_end=584
  _globals['_USERINFO']._serialized_start=587
  _globals['_USERINFO']._serialized_end=891
  _globals['_GETREQUEST']._serialized_start=893
  _globals['_GETREQUEST']._serialized_end=940
  _globals['_GETRESPONSE']._serialized_start=942
  _globals['_GETRESPONSE']._serialized_end=991
  _globals['_GETPARTIALREQUEST']._serialized_start=993
  _globals['_GETPARTIALREQUEST']._serialized_end=1065
  _globals['_GETPARTIALRESPONSE']._serialized_start=1067
  _globals['_GETPARTIALRESPONSE']._serialized_end=1123
  _globals['_ENROLLREQUEST']._serialized_start=1125
  _globals['_ENROLLREQUEST']._serialized_end=1213
  _globals['_ENROLLRESPONSE']._serialized_start=1215
  _globals['_ENROLLRESPONSE']._serialized_end=1231
  _globals['_ENROLLMULTIREQUEST']._serialized_start=1233
  _globals['_ENROLLMULTIREQUEST']._serialized_end=1327
  _globals['_ENROLLMULTIRESPONSE']._serialized_start=1329
  _globals['_ENROLLMULTIRESPONSE']._serialized_end=1397
  _globals['_UPDATEREQUEST']._serialized_start=1399
  _globals['_UPDATEREQUEST']._serialized_end=1468
  _globals['_UPDATERESPONSE']._serialized_start=1470
  _globals['_UPDATERESPONSE']._serialized_end=1486
  _globals['_UPDATEMULTIREQUEST']._serialized_start=1488
  _globals['_UPDATEMULTIREQUEST']._serialized_end=1563
  _globals['_UPDATEMULTIRESPONSE']._serialized_start=1565
  _globals['_UPDATEMULTIRESPONSE']._serialized_end=1633
  _globals['_DELETEREQUEST']._serialized_start=1635
  _globals['_DELETEREQUEST']._serialized_end=1685
  _globals['_DELETERESPONSE']._serialized_start=1687
  _globals['_DELETERESPONSE']._serialized_end=1703
  _globals['_DELETEMULTIREQUEST']._serialized_start=1705
  _globals['_DELETEMULTIREQUEST']._serialized_end=1761
  _globals['_DELETEMULTIRESPONSE']._serialized_start=1763
  _globals['_DELETEMULTIRESPONSE']._serialized_end=1831
  _globals['_DELETEALLREQUEST']._serialized_start=1833
  _globals['_DELETEALLREQUEST']._serialized_end=1869
  _globals['_DELETEALLRESPONSE']._serialized_start=1871
  _globals['_DELETEALLRESPONSE']._serialized_end=1890
  _globals['_DELETEALLMULTIREQUEST']._serialized_start=1892
  _globals['_DELETEALLMULTIREQUEST']._serialized_end=1934
  _globals['_DELETEALLMULTIRESPONSE']._serialized_start=1936
  _globals['_DELETEALLMULTIRESPONSE']._serialized_end=2007
  _globals['_USERCARD']._serialized_start=2009
  _globals['_USERCARD']._serialized_end=2074
  _globals['_GETCARDREQUEST']._serialized_start=2076
  _globals['_GETCARDREQUEST']._serialized_end=2127
  _globals['_GETCARDRESPONSE']._serialized_start=2129
  _globals['_GETCARDRESPONSE']._serialized_end=2186
  _globals['_SETCARDREQUEST']._serialized_start=2188
  _globals['_SETCARDREQUEST']._serialized_end=2262
  _globals['_SETCARDRESPONSE']._serialized_start=2264
  _globals['_SETCARDRESPONSE']._serialized_end=2281
  _globals['_SETCARDMULTIREQUEST']._serialized_start=2283
  _globals['_SETCARDMULTIREQUEST']._serialized_end=2363
  _globals['_SETCARDMULTIRESPONSE']._serialized_start=2365
  _globals['_SETCARDMULTIRESPONSE']._serialized_end=2434
  _globals['_USERFINGER']._serialized_start=2436
  _globals['_USERFINGER']._serialized_end=2506
  _globals['_GETFINGERREQUEST']._serialized_start=2508
  _globals['_GETFINGERREQUEST']._serialized_end=2561
  _globals['_GETFINGERRESPONSE']._serialized_start=2563
  _globals['_GETFINGERRESPONSE']._serialized_end=2626
  _globals['_SETFINGERREQUEST']._serialized_start=2628
  _globals['_SETFINGERREQUEST']._serialized_end=2708
  _globals['_SETFINGERRESPONSE']._serialized_start=2710
  _globals['_SETFINGERRESPONSE']._serialized_end=2729
  _globals['_SETFINGERMULTIREQUEST']._serialized_start=2731
  _globals['_SETFINGERMULTIREQUEST']._serialized_end=2817
  _globals['_SETFINGERMULTIRESPONSE']._serialized_start=2819
  _globals['_SETFINGERMULTIRESPONSE']._serialized_end=2890
  _globals['_USERFACE']._serialized_start=2892
  _globals['_USERFACE']._serialized_end=2954
  _globals['_GETFACEREQUEST']._serialized_start=2956
  _globals['_GETFACEREQUEST']._serialized_end=3007
  _globals['_GETFACERESPONSE']._serialized_start=3009
  _globals['_GETFACERESPONSE']._serialized_end=3066
  _globals['_SETFACEREQUEST']._serialized_start=3068
  _globals['_SETFACEREQUEST']._serialized_end=3142
  _globals['_SETFACERESPONSE']._serialized_start=3144
  _globals['_SETFACERESPONSE']._serialized_end=3161
  _globals['_SETFACEMULTIREQUEST']._serialized_start=3163
  _globals['_SETFACEMULTIREQUEST']._serialized_end=3243
  _globals['_SETFACEMULTIRESPONSE']._serialized_start=3245
  _globals['_SETFACEMULTIRESPONSE']._serialized_end=3314
  _globals['_USERACCESSGROUP']._serialized_start=3316
  _globals['_USERACCESSGROUP']._serialized_end=3373
  _globals['_GETACCESSGROUPREQUEST']._serialized_start=3375
  _globals['_GETACCESSGROUPREQUEST']._serialized_end=3433
  _globals['_GETACCESSGROUPRESPONSE']._serialized_start=3435
  _globals['_GETACCESSGROUPRESPONSE']._serialized_end=3513
  _globals['_SETACCESSGROUPREQUEST']._serialized_start=3515
  _globals['_SETACCESSGROUPREQUEST']._serialized_end=3610
  _globals['_SETACCESSGROUPRESPONSE']._serialized_start=3612
  _globals['_SETACCESSGROUPRESPONSE']._serialized_end=3636
  _globals['_SETACCESSGROUPMULTIREQUEST']._serialized_start=3638
  _globals['_SETACCESSGROUPMULTIREQUEST']._serialized_end=3739
  _globals['_SETACCESSGROUPMULTIRESPONSE']._serialized_start=3741
  _globals['_SETACCESSGROUPMULTIRESPONSE']._serialized_end=3817
  _globals['_USERJOBCODE']._serialized_start=3819
  _globals['_USERJOBCODE']._serialized_end=3885
  _globals['_GETJOBCODEREQUEST']._serialized_start=3887
  _globals['_GETJOBCODEREQUEST']._serialized_end=3941
  _globals['_GETJOBCODERESPONSE']._serialized_start=3943
  _globals['_GETJOBCODERESPONSE']._serialized_end=4009
  _globals['_SETJOBCODEREQUEST']._serialized_start=4011
  _globals['_SETJOBCODEREQUEST']._serialized_end=4094
  _globals['_SETJOBCODERESPONSE']._serialized_start=4096
  _globals['_SETJOBCODERESPONSE']._serialized_end=4116
  _globals['_SETJOBCODEMULTIREQUEST']._serialized_start=4118
  _globals['_SETJOBCODEMULTIREQUEST']._serialized_end=4207
  _globals['_SETJOBCODEMULTIRESPONSE']._serialized_start=4209
  _globals['_SETJOBCODEMULTIRESPONSE']._serialized_end=4281
  _globals['_GETPINHASHREQUEST']._serialized_start=4283
  _globals['_GETPINHASHREQUEST']._serialized_end=4315
  _globals['_GETPINHASHRESPONSE']._serialized_start=4317
  _globals['_GETPINHASHRESPONSE']._serialized_end=4354
  _globals['_GETPINHASHWITHKEYREQUEST']._serialized_start=4356
  _globals['_GETPINHASHWITHKEYREQUEST']._serialized_end=4412
  _globals['_GETSTATISTICREQUEST']._serialized_start=4414
  _globals['_GETSTATISTICREQUEST']._serialized_end=4453
  _globals['_USERSTATISTIC']._serialized_start=4456
  _globals['_USERSTATISTIC']._serialized_end=4621
  _globals['_GETSTATISTICRESPONSE']._serialized_start=4623
  _globals['_GETSTATISTICRESPONSE']._serialized_end=4694
  _globals['_USER']._serialized_start=5735
  _globals['_USER']._serialized_end=7936
# @@protoc_insertion_point(module_scope)
