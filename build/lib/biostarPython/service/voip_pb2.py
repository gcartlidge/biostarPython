# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voip.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nvoip.proto\x12\tgsdk.voip\x1a\terr.proto\"5\n\tUserPhone\x12\x13\n\x0bphoneNumber\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\xef\x02\n\nVOIPConfig\x12\x11\n\tserverURL\x18\x01 \x01(\t\x12\x12\n\nserverPort\x18\x02 \x01(\r\x12\x0e\n\x06userID\x18\x03 \x01(\t\x12\x0e\n\x06userPW\x18\x04 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x05 \x01(\x08\x12\x12\n\nexitButton\x18\x06 \x01(\r\x12\x10\n\x08\x44TMFMode\x18\x07 \x01(\r\x12\x1c\n\x14registrationDuration\x18\t \x01(\r\x12\x15\n\rspeakerVolume\x18\n \x01(\r\x12\x11\n\tmicVolume\x18\x0b \x01(\r\x12\x19\n\x11\x61uthorizationCode\x18\x0c \x01(\t\x12\x1b\n\x13showExtensionNumber\x18\r \x01(\x08\x12\x18\n\x10useOutboundProxy\x18\x0e \x01(\x08\x12\x10\n\x08proxyURL\x18\x0f \x01(\t\x12\x11\n\tproxyPort\x18\x10 \x01(\r\x12$\n\x06phones\x18\x08 \x03(\x0b\x32\x14.gsdk.voip.UserPhone\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\":\n\x11GetConfigResponse\x12%\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x15.gsdk.voip.VOIPConfig\"K\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.voip.VOIPConfig\"\x13\n\x11SetConfigResponse\"Q\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.voip.VOIPConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse2\xed\x01\n\x04VOIP\x12\x46\n\tGetConfig\x12\x1b.gsdk.voip.GetConfigRequest\x1a\x1c.gsdk.voip.GetConfigResponse\x12\x46\n\tSetConfig\x12\x1b.gsdk.voip.SetConfigRequest\x1a\x1c.gsdk.voip.SetConfigResponse\x12U\n\x0eSetConfigMulti\x12 .gsdk.voip.SetConfigMultiRequest\x1a!.gsdk.voip.SetConfigMultiResponseB1\n\x17\x63om.supremainc.sdk.voipP\x01Z\x14\x62iostar/service/voipb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'voip_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.supremainc.sdk.voipP\001Z\024biostar/service/voip'
  _USERPHONE._serialized_start=36
  _USERPHONE._serialized_end=89
  _VOIPCONFIG._serialized_start=92
  _VOIPCONFIG._serialized_end=459
  _GETCONFIGREQUEST._serialized_start=461
  _GETCONFIGREQUEST._serialized_end=497
  _GETCONFIGRESPONSE._serialized_start=499
  _GETCONFIGRESPONSE._serialized_end=557
  _SETCONFIGREQUEST._serialized_start=559
  _SETCONFIGREQUEST._serialized_end=634
  _SETCONFIGRESPONSE._serialized_start=636
  _SETCONFIGRESPONSE._serialized_end=655
  _SETCONFIGMULTIREQUEST._serialized_start=657
  _SETCONFIGMULTIREQUEST._serialized_end=738
  _SETCONFIGMULTIRESPONSE._serialized_start=740
  _SETCONFIGMULTIRESPONSE._serialized_end=811
  _VOIP._serialized_start=814
  _VOIP._serialized_end=1051
# @@protoc_insertion_point(module_scope)
