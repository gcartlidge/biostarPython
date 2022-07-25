# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import cert_pb2 as cert__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgateway.proto\x12\x07gateway\x1a\ncert.proto\"H\n\x0bGatewayInfo\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tdeviceIDs\x18\x02 \x03(\r\x12\x13\n\x0bisConnected\x18\x03 \x01(\x08\"\x10\n\x0eGetListRequest\"%\n\x0fGetListResponse\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\" \n\nGetRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"9\n\x0bGetResponse\x12*\n\x0cgatewayInfos\x18\x01 \x03(\x0b\x32\x14.gateway.GatewayInfo\" \n\nAddRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\r\n\x0b\x41\x64\x64Response\"#\n\rDeleteRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\x10\n\x0e\x44\x65leteResponse\"g\n\x18\x43reateCertificateRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1e\n\x07subject\x18\x02 \x01(\x0b\x32\r.cert.PKIName\x12\x18\n\x10\x65xpireAfterYears\x18\x03 \x01(\x05\"D\n\x19\x43reateCertificateResponse\x12\x13\n\x0bgatewayCert\x18\x01 \x01(\t\x12\x12\n\ngatewayKey\x18\x02 \x01(\t\"/\n\x19GetIssuanceHistoryRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\x92\x01\n\x0f\x43\x65rtificateInfo\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1e\n\x07subject\x18\x02 \x01(\x0b\x32\r.cert.PKIName\x12\x10\n\x08serialNO\x18\x03 \x01(\x03\x12\x11\n\tissueDate\x18\x04 \x01(\x03\x12\x12\n\nexpiryDate\x18\x05 \x01(\x03\x12\x13\n\x0b\x62lacklisted\x18\x06 \x01(\x08\"I\n\x1aGetIssuanceHistoryResponse\x12+\n\tcertInfos\x18\x01 \x03(\x0b\x32\x18.gateway.CertificateInfo\"4\n\x1eGetCertificateBlacklistRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"N\n\x1fGetCertificateBlacklistResponse\x12+\n\tcertInfos\x18\x01 \x03(\x0b\x32\x18.gateway.CertificateInfo\"F\n\x1e\x41\x64\x64\x43\x65rtificateBlacklistRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"!\n\x1f\x41\x64\x64\x43\x65rtificateBlacklistResponse\"I\n!DeleteCertificateBlacklistRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"$\n\"DeleteCertificateBlacklistResponse\"+\n\x16SubscribeStatusRequest\x12\x11\n\tqueueSize\x18\x01 \x01(\x05\"U\n\x0cStatusChange\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1f\n\x06status\x18\x02 \x01(\x0e\x32\x0f.gateway.Status\x12\x11\n\ttimestamp\x18\x03 \x01(\r*)\n\x06Status\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x32\xc1\x06\n\x07Gateway\x12<\n\x07GetList\x12\x17.gateway.GetListRequest\x1a\x18.gateway.GetListResponse\x12\x30\n\x03Get\x12\x13.gateway.GetRequest\x1a\x14.gateway.GetResponse\x12\x30\n\x03\x41\x64\x64\x12\x13.gateway.AddRequest\x1a\x14.gateway.AddResponse\x12\x39\n\x06\x44\x65lete\x12\x16.gateway.DeleteRequest\x1a\x17.gateway.DeleteResponse\x12Z\n\x11\x43reateCertificate\x12!.gateway.CreateCertificateRequest\x1a\".gateway.CreateCertificateResponse\x12]\n\x12GetIssuanceHistory\x12\".gateway.GetIssuanceHistoryRequest\x1a#.gateway.GetIssuanceHistoryResponse\x12l\n\x17GetCertificateBlacklist\x12\'.gateway.GetCertificateBlacklistRequest\x1a(.gateway.GetCertificateBlacklistResponse\x12l\n\x17\x41\x64\x64\x43\x65rtificateBlacklist\x12\'.gateway.AddCertificateBlacklistRequest\x1a(.gateway.AddCertificateBlacklistResponse\x12u\n\x1a\x44\x65leteCertificateBlacklist\x12*.gateway.DeleteCertificateBlacklistRequest\x1a+.gateway.DeleteCertificateBlacklistResponse\x12K\n\x0fSubscribeStatus\x12\x1f.gateway.SubscribeStatusRequest\x1a\x15.gateway.StatusChange0\x01\x42\x37\n\x1a\x63om.supremainc.sdk.gatewayP\x01Z\x17\x62iostar/service/gatewayb\x06proto3')

_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
DISCONNECTED = 0
CONNECTED = 1


_GATEWAYINFO = DESCRIPTOR.message_types_by_name['GatewayInfo']
_GETLISTREQUEST = DESCRIPTOR.message_types_by_name['GetListRequest']
_GETLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetListResponse']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_ADDRESPONSE = DESCRIPTOR.message_types_by_name['AddResponse']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETERESPONSE = DESCRIPTOR.message_types_by_name['DeleteResponse']
_CREATECERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['CreateCertificateRequest']
_CREATECERTIFICATERESPONSE = DESCRIPTOR.message_types_by_name['CreateCertificateResponse']
_GETISSUANCEHISTORYREQUEST = DESCRIPTOR.message_types_by_name['GetIssuanceHistoryRequest']
_CERTIFICATEINFO = DESCRIPTOR.message_types_by_name['CertificateInfo']
_GETISSUANCEHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['GetIssuanceHistoryResponse']
_GETCERTIFICATEBLACKLISTREQUEST = DESCRIPTOR.message_types_by_name['GetCertificateBlacklistRequest']
_GETCERTIFICATEBLACKLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetCertificateBlacklistResponse']
_ADDCERTIFICATEBLACKLISTREQUEST = DESCRIPTOR.message_types_by_name['AddCertificateBlacklistRequest']
_ADDCERTIFICATEBLACKLISTRESPONSE = DESCRIPTOR.message_types_by_name['AddCertificateBlacklistResponse']
_DELETECERTIFICATEBLACKLISTREQUEST = DESCRIPTOR.message_types_by_name['DeleteCertificateBlacklistRequest']
_DELETECERTIFICATEBLACKLISTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteCertificateBlacklistResponse']
_SUBSCRIBESTATUSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeStatusRequest']
_STATUSCHANGE = DESCRIPTOR.message_types_by_name['StatusChange']
GatewayInfo = _reflection.GeneratedProtocolMessageType('GatewayInfo', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYINFO,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GatewayInfo)
  })
_sym_db.RegisterMessage(GatewayInfo)

GetListRequest = _reflection.GeneratedProtocolMessageType('GetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetListRequest)
  })
_sym_db.RegisterMessage(GetListRequest)

GetListResponse = _reflection.GeneratedProtocolMessageType('GetListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetListResponse)
  })
_sym_db.RegisterMessage(GetListResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

CreateCertificateRequest = _reflection.GeneratedProtocolMessageType('CreateCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECERTIFICATEREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CreateCertificateRequest)
  })
_sym_db.RegisterMessage(CreateCertificateRequest)

CreateCertificateResponse = _reflection.GeneratedProtocolMessageType('CreateCertificateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECERTIFICATERESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CreateCertificateResponse)
  })
_sym_db.RegisterMessage(CreateCertificateResponse)

GetIssuanceHistoryRequest = _reflection.GeneratedProtocolMessageType('GetIssuanceHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETISSUANCEHISTORYREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetIssuanceHistoryRequest)
  })
_sym_db.RegisterMessage(GetIssuanceHistoryRequest)

CertificateInfo = _reflection.GeneratedProtocolMessageType('CertificateInfo', (_message.Message,), {
  'DESCRIPTOR' : _CERTIFICATEINFO,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CertificateInfo)
  })
_sym_db.RegisterMessage(CertificateInfo)

GetIssuanceHistoryResponse = _reflection.GeneratedProtocolMessageType('GetIssuanceHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETISSUANCEHISTORYRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetIssuanceHistoryResponse)
  })
_sym_db.RegisterMessage(GetIssuanceHistoryResponse)

GetCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('GetCertificateBlacklistRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEBLACKLISTREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetCertificateBlacklistRequest)
  })
_sym_db.RegisterMessage(GetCertificateBlacklistRequest)

GetCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('GetCertificateBlacklistResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCERTIFICATEBLACKLISTRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetCertificateBlacklistResponse)
  })
_sym_db.RegisterMessage(GetCertificateBlacklistResponse)

AddCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('AddCertificateBlacklistRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDCERTIFICATEBLACKLISTREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddCertificateBlacklistRequest)
  })
_sym_db.RegisterMessage(AddCertificateBlacklistRequest)

AddCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('AddCertificateBlacklistResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDCERTIFICATEBLACKLISTRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddCertificateBlacklistResponse)
  })
_sym_db.RegisterMessage(AddCertificateBlacklistResponse)

DeleteCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('DeleteCertificateBlacklistRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECERTIFICATEBLACKLISTREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteCertificateBlacklistRequest)
  })
_sym_db.RegisterMessage(DeleteCertificateBlacklistRequest)

DeleteCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('DeleteCertificateBlacklistResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECERTIFICATEBLACKLISTRESPONSE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteCertificateBlacklistResponse)
  })
_sym_db.RegisterMessage(DeleteCertificateBlacklistResponse)

SubscribeStatusRequest = _reflection.GeneratedProtocolMessageType('SubscribeStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBESTATUSREQUEST,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.SubscribeStatusRequest)
  })
_sym_db.RegisterMessage(SubscribeStatusRequest)

StatusChange = _reflection.GeneratedProtocolMessageType('StatusChange', (_message.Message,), {
  'DESCRIPTOR' : _STATUSCHANGE,
  '__module__' : 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.StatusChange)
  })
_sym_db.RegisterMessage(StatusChange)

_GATEWAY = DESCRIPTOR.services_by_name['Gateway']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.supremainc.sdk.gatewayP\001Z\027biostar/service/gateway'
  _STATUS._serialized_start=1300
  _STATUS._serialized_end=1341
  _GATEWAYINFO._serialized_start=38
  _GATEWAYINFO._serialized_end=110
  _GETLISTREQUEST._serialized_start=112
  _GETLISTREQUEST._serialized_end=128
  _GETLISTRESPONSE._serialized_start=130
  _GETLISTRESPONSE._serialized_end=167
  _GETREQUEST._serialized_start=169
  _GETREQUEST._serialized_end=201
  _GETRESPONSE._serialized_start=203
  _GETRESPONSE._serialized_end=260
  _ADDREQUEST._serialized_start=262
  _ADDREQUEST._serialized_end=294
  _ADDRESPONSE._serialized_start=296
  _ADDRESPONSE._serialized_end=309
  _DELETEREQUEST._serialized_start=311
  _DELETEREQUEST._serialized_end=346
  _DELETERESPONSE._serialized_start=348
  _DELETERESPONSE._serialized_end=364
  _CREATECERTIFICATEREQUEST._serialized_start=366
  _CREATECERTIFICATEREQUEST._serialized_end=469
  _CREATECERTIFICATERESPONSE._serialized_start=471
  _CREATECERTIFICATERESPONSE._serialized_end=539
  _GETISSUANCEHISTORYREQUEST._serialized_start=541
  _GETISSUANCEHISTORYREQUEST._serialized_end=588
  _CERTIFICATEINFO._serialized_start=591
  _CERTIFICATEINFO._serialized_end=737
  _GETISSUANCEHISTORYRESPONSE._serialized_start=739
  _GETISSUANCEHISTORYRESPONSE._serialized_end=812
  _GETCERTIFICATEBLACKLISTREQUEST._serialized_start=814
  _GETCERTIFICATEBLACKLISTREQUEST._serialized_end=866
  _GETCERTIFICATEBLACKLISTRESPONSE._serialized_start=868
  _GETCERTIFICATEBLACKLISTRESPONSE._serialized_end=946
  _ADDCERTIFICATEBLACKLISTREQUEST._serialized_start=948
  _ADDCERTIFICATEBLACKLISTREQUEST._serialized_end=1018
  _ADDCERTIFICATEBLACKLISTRESPONSE._serialized_start=1020
  _ADDCERTIFICATEBLACKLISTRESPONSE._serialized_end=1053
  _DELETECERTIFICATEBLACKLISTREQUEST._serialized_start=1055
  _DELETECERTIFICATEBLACKLISTREQUEST._serialized_end=1128
  _DELETECERTIFICATEBLACKLISTRESPONSE._serialized_start=1130
  _DELETECERTIFICATEBLACKLISTRESPONSE._serialized_end=1166
  _SUBSCRIBESTATUSREQUEST._serialized_start=1168
  _SUBSCRIBESTATUSREQUEST._serialized_end=1211
  _STATUSCHANGE._serialized_start=1213
  _STATUSCHANGE._serialized_end=1298
  _GATEWAY._serialized_start=1344
  _GATEWAY._serialized_end=2177
# @@protoc_insertion_point(module_scope)
