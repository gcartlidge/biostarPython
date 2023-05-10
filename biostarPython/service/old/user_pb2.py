# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import card_pb2 as card__pb2
from biostarPython.service import finger_pb2 as finger__pb2
from biostarPython.service import face_pb2 as face__pb2
from biostarPython.service import tna_pb2 as tna__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\tgsdk.user\x1a\ncard.proto\x1a\x0c\x66inger.proto\x1a\nface.proto\x1a\ttna.proto\x1a\terr.proto\"e\n\x07UserHdr\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x11\n\tnumOfCard\x18\x02 \x01(\x05\x12\x13\n\x0bnumOfFinger\x18\x03 \x01(\x05\x12\x11\n\tnumOfFace\x18\x04 \x01(\x05\x12\x13\n\x0b\x61uthGroupID\x18\x05 \x01(\r\"\"\n\x0eGetListRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"3\n\x0fGetListResponse\x12 \n\x04hdrs\x18\x01 \x03(\x0b\x32\x12.gsdk.user.UserHdr\"\xf1\x01\n\x0bUserSetting\x12\x11\n\tstartTime\x18\x01 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\r\x12\x19\n\x11\x62iometricAuthMode\x18\x03 \x01(\r\x12\x14\n\x0c\x63\x61rdAuthMode\x18\x04 \x01(\r\x12\x12\n\nIDAuthMode\x18\x05 \x01(\r\x12\x15\n\rsecurityLevel\x18\x06 \x01(\r\x12\x17\n\x0f\x66\x61\x63\x65\x41uthExtMode\x18\x07 \x01(\r\x12\x19\n\x11\x66ingerAuthExtMode\x18\x08 \x01(\r\x12\x17\n\x0f\x63\x61rdAuthExtMode\x18\t \x01(\r\x12\x15\n\rIDAuthExtMode\x18\n \x01(\r\"\xb0\x02\n\x08UserInfo\x12\x1f\n\x03hdr\x18\x01 \x01(\x0b\x32\x12.gsdk.user.UserHdr\x12\'\n\x07setting\x18\x02 \x01(\x0b\x32\x16.gsdk.user.UserSetting\x12\x0c\n\x04name\x18\x03 \x01(\t\x12%\n\x05\x63\x61rds\x18\x04 \x03(\x0b\x32\x16.gsdk.card.CSNCardData\x12(\n\x07\x66ingers\x18\x05 \x03(\x0b\x32\x17.gsdk.finger.FingerData\x12\"\n\x05\x66\x61\x63\x65s\x18\x06 \x03(\x0b\x32\x13.gsdk.face.FaceData\x12\x16\n\x0e\x61\x63\x63\x65ssGroupIDs\x18\x07 \x03(\r\x12#\n\x08jobCodes\x18\x08 \x03(\x0b\x32\x11.gsdk.tna.JobCode\x12\x0b\n\x03PIN\x18\t \x01(\x0c\x12\r\n\x05photo\x18\n \x01(\x0c\"/\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"1\n\x0bGetResponse\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"H\n\x11GetPartialRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\x12\x10\n\x08infoMask\x18\x03 \x01(\r\"8\n\x12GetPartialResponse\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserInfo\"X\n\rEnrollRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"\x10\n\x0e\x45nrollResponse\"^\n\x12\x45nrollMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\"\n\x05users\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserInfo\x12\x11\n\toverwrite\x18\x03 \x01(\x08\"D\n\x13\x45nrollMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"\x10\n\x0e\x44\x65leteResponse\"8\n\x12\x44\x65leteMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"D\n\x13\x44\x65leteMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"*\n\x15\x44\x65leteAllMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"G\n\x16\x44\x65leteAllMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"A\n\x08UserCard\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12%\n\x05\x63\x61rds\x18\x02 \x03(\x0b\x32\x16.gsdk.card.CSNCardData\"3\n\x0eGetCardRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"9\n\x0fGetCardResponse\x12&\n\tuserCards\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserCard\"J\n\x0eSetCardRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\tuserCards\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserCard\"\x11\n\x0fSetCardResponse\"P\n\x13SetCardMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\tuserCards\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserCard\"E\n\x14SetCardMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"F\n\nUserFinger\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12(\n\x07\x66ingers\x18\x02 \x03(\x0b\x32\x17.gsdk.finger.FingerData\"5\n\x10GetFingerRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"?\n\x11GetFingerResponse\x12*\n\x0buserFingers\x18\x01 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"P\n\x10SetFingerRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12*\n\x0buserFingers\x18\x02 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"\x13\n\x11SetFingerResponse\"V\n\x15SetFingerMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12*\n\x0buserFingers\x18\x02 \x03(\x0b\x32\x15.gsdk.user.UserFinger\"G\n\x16SetFingerMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\">\n\x08UserFace\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\"\n\x05\x66\x61\x63\x65s\x18\x02 \x03(\x0b\x32\x13.gsdk.face.FaceData\"3\n\x0eGetFaceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"9\n\x0fGetFaceResponse\x12&\n\tuserFaces\x18\x01 \x03(\x0b\x32\x13.gsdk.user.UserFace\"J\n\x0eSetFaceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\tuserFaces\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserFace\"\x11\n\x0fSetFaceResponse\"P\n\x13SetFaceMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\tuserFaces\x18\x02 \x03(\x0b\x32\x13.gsdk.user.UserFace\"E\n\x14SetFaceMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"9\n\x0fUserAccessGroup\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63\x65ssGroupIDs\x18\x02 \x03(\r\":\n\x15GetAccessGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"N\n\x16GetAccessGroupResponse\x12\x34\n\x10userAccessGroups\x18\x01 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"_\n\x15SetAccessGroupRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x34\n\x10userAccessGroups\x18\x02 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"\x18\n\x16SetAccessGroupResponse\"e\n\x1aSetAccessGroupMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x34\n\x10userAccessGroups\x18\x02 \x03(\x0b\x32\x1a.gsdk.user.UserAccessGroup\"L\n\x1bSetAccessGroupMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"B\n\x0bUserJobCode\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12#\n\x08jobCodes\x18\x02 \x03(\x0b\x32\x11.gsdk.tna.JobCode\"6\n\x11GetJobCodeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07userIDs\x18\x02 \x03(\t\"B\n\x12GetJobCodeResponse\x12,\n\x0cuserJobCodes\x18\x01 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"S\n\x11SetJobCodeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12,\n\x0cuserJobCodes\x18\x02 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"\x14\n\x12SetJobCodeResponse\"Y\n\x16SetJobCodeMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12,\n\x0cuserJobCodes\x18\x02 \x03(\x0b\x32\x16.gsdk.user.UserJobCode\"H\n\x17SetJobCodeMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\" \n\x11GetPINHashRequest\x12\x0b\n\x03PIN\x18\x01 \x01(\t\"%\n\x12GetPINHashResponse\x12\x0f\n\x07hashVal\x18\x01 \x01(\x0c\"8\n\x18GetPINHashWithKeyRequest\x12\x0b\n\x03PIN\x18\x01 \x01(\t\x12\x0f\n\x07hashKey\x18\x02 \x01(\x0c*\xd6\x02\n\x08InfoMask\x12\x15\n\x11USER_MASK_ID_ONLY\x10\x00\x12\x11\n\rUSER_MASK_HDR\x10\x01\x12\x15\n\x11USER_MASK_SETTING\x10\x02\x12\x12\n\x0eUSER_MASK_NAME\x10\x04\x12\x13\n\x0fUSER_MASK_PHOTO\x10\x08\x12\x11\n\rUSER_MASK_PIN\x10\x10\x12\x12\n\x0eUSER_MASK_CARD\x10 \x12\x14\n\x10USER_MASK_FINGER\x10@\x12\x13\n\x0eUSER_MASK_FACE\x10\x80\x01\x12\x1b\n\x16USER_MASK_ACCESS_GROUP\x10\x80\x02\x12\x12\n\rUSER_MASK_JOB\x10\x80\x04\x12\x15\n\x10USER_MASK_PHRASE\x10\x80\x08\x12\x16\n\x11USER_MASK_FACE_EX\x10\x80\x10\x12\x19\n\x14USER_MASK_SETTING_EX\x10\x80 \x12\x13\n\rUSER_MASK_ALL\x10\xff\xff\x03\x32\xbb\x0f\n\x04User\x12@\n\x07GetList\x12\x19.gsdk.user.GetListRequest\x1a\x1a.gsdk.user.GetListResponse\x12\x34\n\x03Get\x12\x15.gsdk.user.GetRequest\x1a\x16.gsdk.user.GetResponse\x12I\n\nGetPartial\x12\x1c.gsdk.user.GetPartialRequest\x1a\x1d.gsdk.user.GetPartialResponse\x12=\n\x06\x45nroll\x12\x18.gsdk.user.EnrollRequest\x1a\x19.gsdk.user.EnrollResponse\x12L\n\x0b\x45nrollMulti\x12\x1d.gsdk.user.EnrollMultiRequest\x1a\x1e.gsdk.user.EnrollMultiResponse\x12=\n\x06\x44\x65lete\x12\x18.gsdk.user.DeleteRequest\x1a\x19.gsdk.user.DeleteResponse\x12L\n\x0b\x44\x65leteMulti\x12\x1d.gsdk.user.DeleteMultiRequest\x1a\x1e.gsdk.user.DeleteMultiResponse\x12\x46\n\tDeleteAll\x12\x1b.gsdk.user.DeleteAllRequest\x1a\x1c.gsdk.user.DeleteAllResponse\x12U\n\x0e\x44\x65leteAllMulti\x12 .gsdk.user.DeleteAllMultiRequest\x1a!.gsdk.user.DeleteAllMultiResponse\x12@\n\x07GetCard\x12\x19.gsdk.user.GetCardRequest\x1a\x1a.gsdk.user.GetCardResponse\x12@\n\x07SetCard\x12\x19.gsdk.user.SetCardRequest\x1a\x1a.gsdk.user.SetCardResponse\x12O\n\x0cSetCardMulti\x12\x1e.gsdk.user.SetCardMultiRequest\x1a\x1f.gsdk.user.SetCardMultiResponse\x12\x46\n\tGetFinger\x12\x1b.gsdk.user.GetFingerRequest\x1a\x1c.gsdk.user.GetFingerResponse\x12\x46\n\tSetFinger\x12\x1b.gsdk.user.SetFingerRequest\x1a\x1c.gsdk.user.SetFingerResponse\x12U\n\x0eSetFingerMulti\x12 .gsdk.user.SetFingerMultiRequest\x1a!.gsdk.user.SetFingerMultiResponse\x12@\n\x07GetFace\x12\x19.gsdk.user.GetFaceRequest\x1a\x1a.gsdk.user.GetFaceResponse\x12@\n\x07SetFace\x12\x19.gsdk.user.SetFaceRequest\x1a\x1a.gsdk.user.SetFaceResponse\x12O\n\x0cSetFaceMulti\x12\x1e.gsdk.user.SetFaceMultiRequest\x1a\x1f.gsdk.user.SetFaceMultiResponse\x12U\n\x0eGetAccessGroup\x12 .gsdk.user.GetAccessGroupRequest\x1a!.gsdk.user.GetAccessGroupResponse\x12U\n\x0eSetAccessGroup\x12 .gsdk.user.SetAccessGroupRequest\x1a!.gsdk.user.SetAccessGroupResponse\x12\x64\n\x13SetAccessGroupMulti\x12%.gsdk.user.SetAccessGroupMultiRequest\x1a&.gsdk.user.SetAccessGroupMultiResponse\x12I\n\nGetJobCode\x12\x1c.gsdk.user.GetJobCodeRequest\x1a\x1d.gsdk.user.GetJobCodeResponse\x12I\n\nSetJobCode\x12\x1c.gsdk.user.SetJobCodeRequest\x1a\x1d.gsdk.user.SetJobCodeResponse\x12X\n\x0fSetJobCodeMulti\x12!.gsdk.user.SetJobCodeMultiRequest\x1a\".gsdk.user.SetJobCodeMultiResponse\x12I\n\nGetPINHash\x12\x1c.gsdk.user.GetPINHashRequest\x1a\x1d.gsdk.user.GetPINHashResponse\x12W\n\x11GetPINHashWithKey\x12#.gsdk.user.GetPINHashWithKeyRequest\x1a\x1d.gsdk.user.GetPINHashResponseB1\n\x17\x63om.supremainc.sdk.userP\x01Z\x14\x62iostar/service/userb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.supremainc.sdk.userP\001Z\024biostar/service/user'
  _INFOMASK._serialized_start=4114
  _INFOMASK._serialized_end=4456
  _USERHDR._serialized_start=85
  _USERHDR._serialized_end=186
  _GETLISTREQUEST._serialized_start=188
  _GETLISTREQUEST._serialized_end=222
  _GETLISTRESPONSE._serialized_start=224
  _GETLISTRESPONSE._serialized_end=275
  _USERSETTING._serialized_start=278
  _USERSETTING._serialized_end=519
  _USERINFO._serialized_start=522
  _USERINFO._serialized_end=826
  _GETREQUEST._serialized_start=828
  _GETREQUEST._serialized_end=875
  _GETRESPONSE._serialized_start=877
  _GETRESPONSE._serialized_end=926
  _GETPARTIALREQUEST._serialized_start=928
  _GETPARTIALREQUEST._serialized_end=1000
  _GETPARTIALRESPONSE._serialized_start=1002
  _GETPARTIALRESPONSE._serialized_end=1058
  _ENROLLREQUEST._serialized_start=1060
  _ENROLLREQUEST._serialized_end=1148
  _ENROLLRESPONSE._serialized_start=1150
  _ENROLLRESPONSE._serialized_end=1166
  _ENROLLMULTIREQUEST._serialized_start=1168
  _ENROLLMULTIREQUEST._serialized_end=1262
  _ENROLLMULTIRESPONSE._serialized_start=1264
  _ENROLLMULTIRESPONSE._serialized_end=1332
  _DELETEREQUEST._serialized_start=1334
  _DELETEREQUEST._serialized_end=1384
  _DELETERESPONSE._serialized_start=1386
  _DELETERESPONSE._serialized_end=1402
  _DELETEMULTIREQUEST._serialized_start=1404
  _DELETEMULTIREQUEST._serialized_end=1460
  _DELETEMULTIRESPONSE._serialized_start=1462
  _DELETEMULTIRESPONSE._serialized_end=1530
  _DELETEALLREQUEST._serialized_start=1532
  _DELETEALLREQUEST._serialized_end=1568
  _DELETEALLRESPONSE._serialized_start=1570
  _DELETEALLRESPONSE._serialized_end=1589
  _DELETEALLMULTIREQUEST._serialized_start=1591
  _DELETEALLMULTIREQUEST._serialized_end=1633
  _DELETEALLMULTIRESPONSE._serialized_start=1635
  _DELETEALLMULTIRESPONSE._serialized_end=1706
  _USERCARD._serialized_start=1708
  _USERCARD._serialized_end=1773
  _GETCARDREQUEST._serialized_start=1775
  _GETCARDREQUEST._serialized_end=1826
  _GETCARDRESPONSE._serialized_start=1828
  _GETCARDRESPONSE._serialized_end=1885
  _SETCARDREQUEST._serialized_start=1887
  _SETCARDREQUEST._serialized_end=1961
  _SETCARDRESPONSE._serialized_start=1963
  _SETCARDRESPONSE._serialized_end=1980
  _SETCARDMULTIREQUEST._serialized_start=1982
  _SETCARDMULTIREQUEST._serialized_end=2062
  _SETCARDMULTIRESPONSE._serialized_start=2064
  _SETCARDMULTIRESPONSE._serialized_end=2133
  _USERFINGER._serialized_start=2135
  _USERFINGER._serialized_end=2205
  _GETFINGERREQUEST._serialized_start=2207
  _GETFINGERREQUEST._serialized_end=2260
  _GETFINGERRESPONSE._serialized_start=2262
  _GETFINGERRESPONSE._serialized_end=2325
  _SETFINGERREQUEST._serialized_start=2327
  _SETFINGERREQUEST._serialized_end=2407
  _SETFINGERRESPONSE._serialized_start=2409
  _SETFINGERRESPONSE._serialized_end=2428
  _SETFINGERMULTIREQUEST._serialized_start=2430
  _SETFINGERMULTIREQUEST._serialized_end=2516
  _SETFINGERMULTIRESPONSE._serialized_start=2518
  _SETFINGERMULTIRESPONSE._serialized_end=2589
  _USERFACE._serialized_start=2591
  _USERFACE._serialized_end=2653
  _GETFACEREQUEST._serialized_start=2655
  _GETFACEREQUEST._serialized_end=2706
  _GETFACERESPONSE._serialized_start=2708
  _GETFACERESPONSE._serialized_end=2765
  _SETFACEREQUEST._serialized_start=2767
  _SETFACEREQUEST._serialized_end=2841
  _SETFACERESPONSE._serialized_start=2843
  _SETFACERESPONSE._serialized_end=2860
  _SETFACEMULTIREQUEST._serialized_start=2862
  _SETFACEMULTIREQUEST._serialized_end=2942
  _SETFACEMULTIRESPONSE._serialized_start=2944
  _SETFACEMULTIRESPONSE._serialized_end=3013
  _USERACCESSGROUP._serialized_start=3015
  _USERACCESSGROUP._serialized_end=3072
  _GETACCESSGROUPREQUEST._serialized_start=3074
  _GETACCESSGROUPREQUEST._serialized_end=3132
  _GETACCESSGROUPRESPONSE._serialized_start=3134
  _GETACCESSGROUPRESPONSE._serialized_end=3212
  _SETACCESSGROUPREQUEST._serialized_start=3214
  _SETACCESSGROUPREQUEST._serialized_end=3309
  _SETACCESSGROUPRESPONSE._serialized_start=3311
  _SETACCESSGROUPRESPONSE._serialized_end=3335
  _SETACCESSGROUPMULTIREQUEST._serialized_start=3337
  _SETACCESSGROUPMULTIREQUEST._serialized_end=3438
  _SETACCESSGROUPMULTIRESPONSE._serialized_start=3440
  _SETACCESSGROUPMULTIRESPONSE._serialized_end=3516
  _USERJOBCODE._serialized_start=3518
  _USERJOBCODE._serialized_end=3584
  _GETJOBCODEREQUEST._serialized_start=3586
  _GETJOBCODEREQUEST._serialized_end=3640
  _GETJOBCODERESPONSE._serialized_start=3642
  _GETJOBCODERESPONSE._serialized_end=3708
  _SETJOBCODEREQUEST._serialized_start=3710
  _SETJOBCODEREQUEST._serialized_end=3793
  _SETJOBCODERESPONSE._serialized_start=3795
  _SETJOBCODERESPONSE._serialized_end=3815
  _SETJOBCODEMULTIREQUEST._serialized_start=3817
  _SETJOBCODEMULTIREQUEST._serialized_end=3906
  _SETJOBCODEMULTIRESPONSE._serialized_start=3908
  _SETJOBCODEMULTIRESPONSE._serialized_end=3980
  _GETPINHASHREQUEST._serialized_start=3982
  _GETPINHASHREQUEST._serialized_end=4014
  _GETPINHASHRESPONSE._serialized_start=4016
  _GETPINHASHRESPONSE._serialized_end=4053
  _GETPINHASHWITHKEYREQUEST._serialized_start=4055
  _GETPINHASHWITHKEYREQUEST._serialized_end=4111
  _USER._serialized_start=4459
  _USER._serialized_end=6438
# @@protoc_insertion_point(module_scope)
