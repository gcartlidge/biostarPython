# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import card_pb2 as card__pb2
from biostarPython.service import finger_pb2 as finger__pb2
from biostarPython.service import user_pb2 as user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x06server\x1a\ncard.proto\x1a\x0c\x66inger.proto\x1a\nuser.proto\"\x90\x02\n\rServerRequest\x12$\n\x07reqType\x18\x01 \x01(\x0e\x32\x13.server.RequestType\x12\x10\n\x08\x64\x65viceID\x18\x02 \x01(\r\x12\r\n\x05seqNO\x18\x03 \x01(\r\x12(\n\tverifyReq\x18\x04 \x01(\x0b\x32\x15.server.VerifyRequest\x12,\n\x0bidentifyReq\x18\x05 \x01(\x0b\x32\x17.server.IdentifyRequest\x12.\n\x0cglobalAPBReq\x18\x06 \x01(\x0b\x32\x18.server.GlobalAPBRequest\x12\x30\n\ruserPhraseReq\x18\x07 \x01(\x0b\x32\x19.server.UserPhraseRequest\"_\n\rVerifyRequest\x12\x0e\n\x06isCard\x18\x01 \x01(\x08\x12\x1c\n\x08\x63\x61rdType\x18\x02 \x01(\x0e\x32\n.card.Type\x12\x10\n\x08\x63\x61rdData\x18\x03 \x01(\x0c\x12\x0e\n\x06userID\x18\x04 \x01(\t\"W\n\x0fIdentifyRequest\x12.\n\x0etemplateFormat\x18\x01 \x01(\x0e\x32\x16.finger.TemplateFormat\x12\x14\n\x0ctemplateData\x18\x02 \x01(\x0c\"#\n\x10GlobalAPBRequest\x12\x0f\n\x07userIDs\x18\x01 \x03(\t\"#\n\x11UserPhraseRequest\x12\x0e\n\x06userID\x18\x01 \x01(\t\"%\n\x10SubscribeRequest\x12\x11\n\tqueueSize\x18\x01 \x01(\x05\"\x14\n\x12UnsubscribeRequest\"\x15\n\x13UnsubscribeResponse\"~\n\x13HandleVerifyRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\r\n\x05seqNO\x18\x02 \x01(\r\x12(\n\x07\x65rrCode\x18\x03 \x01(\x0e\x32\x17.server.ServerErrorCode\x12\x1c\n\x04user\x18\x04 \x01(\x0b\x32\x0e.user.UserInfo\"\x16\n\x14HandleVerifyResponse\"\x80\x01\n\x15HandleIdentifyRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\r\n\x05seqNO\x18\x02 \x01(\r\x12(\n\x07\x65rrCode\x18\x03 \x01(\x0e\x32\x17.server.ServerErrorCode\x12\x1c\n\x04user\x18\x04 \x01(\x0b\x32\x0e.user.UserInfo\"\x18\n\x16HandleIdentifyResponse\"s\n\x16HandleGlobalAPBRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\r\n\x05seqNO\x18\x02 \x01(\r\x12(\n\x07\x65rrCode\x18\x03 \x01(\x0e\x32\x17.server.ServerErrorCode\x12\x0e\n\x06zoneID\x18\x04 \x01(\r\"\x19\n\x17HandleGlobalAPBResponse\"x\n\x17HandleUserPhraseRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\r\n\x05seqNO\x18\x02 \x01(\r\x12(\n\x07\x65rrCode\x18\x03 \x01(\x0e\x32\x17.server.ServerErrorCode\x12\x12\n\nuserPhrase\x18\x04 \x01(\t\"\x1a\n\x18HandleUserPhraseResponse*x\n\x0bRequestType\x12\x0e\n\nNO_REQUEST\x10\x00\x12\x12\n\x0eVERIFY_REQUEST\x10\x01\x12\x14\n\x10IDENTIFY_REQUEST\x10\x02\x12\x16\n\x12GLOBAL_APB_REQUEST\x10\x03\x12\x17\n\x13USER_PHRASE_REQUEST\x10\x04*\xb5\x01\n\x0fServerErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x18\n\x0bVERIFY_FAIL\x10\xd3\xfd\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1a\n\rIDENTIFY_FAIL\x10\xd2\xfd\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12HARD_APB_VIOLATION\x10\xce\xf6\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12SOFT_APB_VIOLATION\x10\xcd\xf6\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1d\n\x10\x43\x41NNOT_FIND_USER\x10\xb6\xfa\xff\xff\xff\xff\xff\xff\xff\x01\x32\xd7\x03\n\x06Server\x12>\n\tSubscribe\x12\x18.server.SubscribeRequest\x1a\x15.server.ServerRequest0\x01\x12\x46\n\x0bUnsubscribe\x12\x1a.server.UnsubscribeRequest\x1a\x1b.server.UnsubscribeResponse\x12I\n\x0cHandleVerify\x12\x1b.server.HandleVerifyRequest\x1a\x1c.server.HandleVerifyResponse\x12O\n\x0eHandleIdentify\x12\x1d.server.HandleIdentifyRequest\x1a\x1e.server.HandleIdentifyResponse\x12R\n\x0fHandleGlobalAPB\x12\x1e.server.HandleGlobalAPBRequest\x1a\x1f.server.HandleGlobalAPBResponse\x12U\n\x10HandleUserPhrase\x12\x1f.server.HandleUserPhraseRequest\x1a .server.HandleUserPhraseResponseB5\n\x19\x63om.supremainc.sdk.serverP\x01Z\x16\x62iostar/service/serverb\x06proto3')

_REQUESTTYPE = DESCRIPTOR.enum_types_by_name['RequestType']
RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
_SERVERERRORCODE = DESCRIPTOR.enum_types_by_name['ServerErrorCode']
ServerErrorCode = enum_type_wrapper.EnumTypeWrapper(_SERVERERRORCODE)
NO_REQUEST = 0
VERIFY_REQUEST = 1
IDENTIFY_REQUEST = 2
GLOBAL_APB_REQUEST = 3
USER_PHRASE_REQUEST = 4
SUCCESS = 0
VERIFY_FAIL = -301
IDENTIFY_FAIL = -302
HARD_APB_VIOLATION = -1202
SOFT_APB_VIOLATION = -1203
CANNOT_FIND_USER = -714


_SERVERREQUEST = DESCRIPTOR.message_types_by_name['ServerRequest']
_VERIFYREQUEST = DESCRIPTOR.message_types_by_name['VerifyRequest']
_IDENTIFYREQUEST = DESCRIPTOR.message_types_by_name['IdentifyRequest']
_GLOBALAPBREQUEST = DESCRIPTOR.message_types_by_name['GlobalAPBRequest']
_USERPHRASEREQUEST = DESCRIPTOR.message_types_by_name['UserPhraseRequest']
_SUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['SubscribeRequest']
_UNSUBSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['UnsubscribeRequest']
_UNSUBSCRIBERESPONSE = DESCRIPTOR.message_types_by_name['UnsubscribeResponse']
_HANDLEVERIFYREQUEST = DESCRIPTOR.message_types_by_name['HandleVerifyRequest']
_HANDLEVERIFYRESPONSE = DESCRIPTOR.message_types_by_name['HandleVerifyResponse']
_HANDLEIDENTIFYREQUEST = DESCRIPTOR.message_types_by_name['HandleIdentifyRequest']
_HANDLEIDENTIFYRESPONSE = DESCRIPTOR.message_types_by_name['HandleIdentifyResponse']
_HANDLEGLOBALAPBREQUEST = DESCRIPTOR.message_types_by_name['HandleGlobalAPBRequest']
_HANDLEGLOBALAPBRESPONSE = DESCRIPTOR.message_types_by_name['HandleGlobalAPBResponse']
_HANDLEUSERPHRASEREQUEST = DESCRIPTOR.message_types_by_name['HandleUserPhraseRequest']
_HANDLEUSERPHRASERESPONSE = DESCRIPTOR.message_types_by_name['HandleUserPhraseResponse']
ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.ServerRequest)
  })
_sym_db.RegisterMessage(ServerRequest)

VerifyRequest = _reflection.GeneratedProtocolMessageType('VerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.VerifyRequest)
  })
_sym_db.RegisterMessage(VerifyRequest)

IdentifyRequest = _reflection.GeneratedProtocolMessageType('IdentifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFYREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.IdentifyRequest)
  })
_sym_db.RegisterMessage(IdentifyRequest)

GlobalAPBRequest = _reflection.GeneratedProtocolMessageType('GlobalAPBRequest', (_message.Message,), {
  'DESCRIPTOR' : _GLOBALAPBREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.GlobalAPBRequest)
  })
_sym_db.RegisterMessage(GlobalAPBRequest)

UserPhraseRequest = _reflection.GeneratedProtocolMessageType('UserPhraseRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERPHRASEREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.UserPhraseRequest)
  })
_sym_db.RegisterMessage(UserPhraseRequest)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

UnsubscribeRequest = _reflection.GeneratedProtocolMessageType('UnsubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNSUBSCRIBEREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.UnsubscribeRequest)
  })
_sym_db.RegisterMessage(UnsubscribeRequest)

UnsubscribeResponse = _reflection.GeneratedProtocolMessageType('UnsubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNSUBSCRIBERESPONSE,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.UnsubscribeResponse)
  })
_sym_db.RegisterMessage(UnsubscribeResponse)

HandleVerifyRequest = _reflection.GeneratedProtocolMessageType('HandleVerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEVERIFYREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleVerifyRequest)
  })
_sym_db.RegisterMessage(HandleVerifyRequest)

HandleVerifyResponse = _reflection.GeneratedProtocolMessageType('HandleVerifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEVERIFYRESPONSE,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleVerifyResponse)
  })
_sym_db.RegisterMessage(HandleVerifyResponse)

HandleIdentifyRequest = _reflection.GeneratedProtocolMessageType('HandleIdentifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEIDENTIFYREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleIdentifyRequest)
  })
_sym_db.RegisterMessage(HandleIdentifyRequest)

HandleIdentifyResponse = _reflection.GeneratedProtocolMessageType('HandleIdentifyResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEIDENTIFYRESPONSE,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleIdentifyResponse)
  })
_sym_db.RegisterMessage(HandleIdentifyResponse)

HandleGlobalAPBRequest = _reflection.GeneratedProtocolMessageType('HandleGlobalAPBRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEGLOBALAPBREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleGlobalAPBRequest)
  })
_sym_db.RegisterMessage(HandleGlobalAPBRequest)

HandleGlobalAPBResponse = _reflection.GeneratedProtocolMessageType('HandleGlobalAPBResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEGLOBALAPBRESPONSE,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleGlobalAPBResponse)
  })
_sym_db.RegisterMessage(HandleGlobalAPBResponse)

HandleUserPhraseRequest = _reflection.GeneratedProtocolMessageType('HandleUserPhraseRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEUSERPHRASEREQUEST,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleUserPhraseRequest)
  })
_sym_db.RegisterMessage(HandleUserPhraseRequest)

HandleUserPhraseResponse = _reflection.GeneratedProtocolMessageType('HandleUserPhraseResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDLEUSERPHRASERESPONSE,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.HandleUserPhraseResponse)
  })
_sym_db.RegisterMessage(HandleUserPhraseResponse)

_SERVER = DESCRIPTOR.services_by_name['Server']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.supremainc.sdk.serverP\001Z\026biostar/service/server'
  _REQUESTTYPE._serialized_start=1284
  _REQUESTTYPE._serialized_end=1404
  _SERVERERRORCODE._serialized_start=1407
  _SERVERERRORCODE._serialized_end=1588
  _SERVERREQUEST._serialized_start=63
  _SERVERREQUEST._serialized_end=335
  _VERIFYREQUEST._serialized_start=337
  _VERIFYREQUEST._serialized_end=432
  _IDENTIFYREQUEST._serialized_start=434
  _IDENTIFYREQUEST._serialized_end=521
  _GLOBALAPBREQUEST._serialized_start=523
  _GLOBALAPBREQUEST._serialized_end=558
  _USERPHRASEREQUEST._serialized_start=560
  _USERPHRASEREQUEST._serialized_end=595
  _SUBSCRIBEREQUEST._serialized_start=597
  _SUBSCRIBEREQUEST._serialized_end=634
  _UNSUBSCRIBEREQUEST._serialized_start=636
  _UNSUBSCRIBEREQUEST._serialized_end=656
  _UNSUBSCRIBERESPONSE._serialized_start=658
  _UNSUBSCRIBERESPONSE._serialized_end=679
  _HANDLEVERIFYREQUEST._serialized_start=681
  _HANDLEVERIFYREQUEST._serialized_end=807
  _HANDLEVERIFYRESPONSE._serialized_start=809
  _HANDLEVERIFYRESPONSE._serialized_end=831
  _HANDLEIDENTIFYREQUEST._serialized_start=834
  _HANDLEIDENTIFYREQUEST._serialized_end=962
  _HANDLEIDENTIFYRESPONSE._serialized_start=964
  _HANDLEIDENTIFYRESPONSE._serialized_end=988
  _HANDLEGLOBALAPBREQUEST._serialized_start=990
  _HANDLEGLOBALAPBREQUEST._serialized_end=1105
  _HANDLEGLOBALAPBRESPONSE._serialized_start=1107
  _HANDLEGLOBALAPBRESPONSE._serialized_end=1132
  _HANDLEUSERPHRASEREQUEST._serialized_start=1134
  _HANDLEUSERPHRASEREQUEST._serialized_end=1254
  _HANDLEUSERPHRASERESPONSE._serialized_start=1256
  _HANDLEUSERPHRASERESPONSE._serialized_end=1282
  _SERVER._serialized_start=1591
  _SERVER._serialized_end=2062
# @@protoc_insertion_point(module_scope)