# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tenant.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import cert_pb2 as cert__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ctenant.proto\x12\x0bgsdk.tenant\x1a\ncert.proto\"2\n\nTenantInfo\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12\x12\n\ngatewayIDs\x18\x02 \x03(\t\"\x10\n\x0eGetListRequest\"$\n\x0fGetListResponse\x12\x11\n\ttenantIDs\x18\x01 \x03(\t\"\x1f\n\nGetRequest\x12\x11\n\ttenantIDs\x18\x01 \x03(\t\";\n\x0bGetResponse\x12,\n\x0btenantInfos\x18\x01 \x03(\x0b\x32\x17.gsdk.tenant.TenantInfo\":\n\nAddRequest\x12,\n\x0btenantInfos\x18\x01 \x03(\x0b\x32\x17.gsdk.tenant.TenantInfo\"\r\n\x0b\x41\x64\x64Response\"\"\n\rDeleteRequest\x12\x11\n\ttenantIDs\x18\x01 \x03(\t\"\x10\n\x0e\x44\x65leteResponse\"9\n\x11\x41\x64\x64GatewayRequest\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12\x12\n\ngatewayIDs\x18\x02 \x03(\t\"\x14\n\x12\x41\x64\x64GatewayResponse\"<\n\x14\x44\x65leteGatewayRequest\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12\x12\n\ngatewayIDs\x18\x02 \x03(\t\"\x17\n\x15\x44\x65leteGatewayResponse\"k\n\x18\x43reateCertificateRequest\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12#\n\x07subject\x18\x02 \x01(\x0b\x32\x12.gsdk.cert.PKIName\x12\x18\n\x10\x65xpireAfterYears\x18\x03 \x01(\x05\"B\n\x19\x43reateCertificateResponse\x12\x12\n\ntenantCert\x18\x01 \x01(\t\x12\x11\n\ttenantKey\x18\x02 \x01(\t\".\n\x19GetIssuanceHistoryRequest\x12\x11\n\ttenantIDs\x18\x01 \x03(\t\"\x96\x01\n\x0f\x43\x65rtificateInfo\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12#\n\x07subject\x18\x02 \x01(\x0b\x32\x12.gsdk.cert.PKIName\x12\x10\n\x08serialNO\x18\x03 \x01(\x03\x12\x11\n\tissueDate\x18\x04 \x01(\x03\x12\x12\n\nexpiryDate\x18\x05 \x01(\x03\x12\x13\n\x0b\x62lacklisted\x18\x06 \x01(\x08\"M\n\x1aGetIssuanceHistoryResponse\x12/\n\tcertInfos\x18\x01 \x03(\x0b\x32\x1c.gsdk.tenant.CertificateInfo\"3\n\x1eGetCertificateBlacklistRequest\x12\x11\n\ttenantIDs\x18\x01 \x03(\t\"R\n\x1fGetCertificateBlacklistResponse\x12/\n\tcertInfos\x18\x01 \x03(\x0b\x32\x1c.gsdk.tenant.CertificateInfo\"E\n\x1e\x41\x64\x64\x43\x65rtificateBlacklistRequest\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"!\n\x1f\x41\x64\x64\x43\x65rtificateBlacklistResponse\"H\n!DeleteCertificateBlacklistRequest\x12\x10\n\x08tenantID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"$\n\"DeleteCertificateBlacklistResponse2\xe2\x07\n\x06Tenant\x12\x44\n\x07GetList\x12\x1b.gsdk.tenant.GetListRequest\x1a\x1c.gsdk.tenant.GetListResponse\x12\x38\n\x03Get\x12\x17.gsdk.tenant.GetRequest\x1a\x18.gsdk.tenant.GetResponse\x12\x38\n\x03\x41\x64\x64\x12\x17.gsdk.tenant.AddRequest\x1a\x18.gsdk.tenant.AddResponse\x12\x41\n\x06\x44\x65lete\x12\x1a.gsdk.tenant.DeleteRequest\x1a\x1b.gsdk.tenant.DeleteResponse\x12M\n\nAddGateway\x12\x1e.gsdk.tenant.AddGatewayRequest\x1a\x1f.gsdk.tenant.AddGatewayResponse\x12V\n\rDeleteGateway\x12!.gsdk.tenant.DeleteGatewayRequest\x1a\".gsdk.tenant.DeleteGatewayResponse\x12\x62\n\x11\x43reateCertificate\x12%.gsdk.tenant.CreateCertificateRequest\x1a&.gsdk.tenant.CreateCertificateResponse\x12\x65\n\x12GetIssuanceHistory\x12&.gsdk.tenant.GetIssuanceHistoryRequest\x1a\'.gsdk.tenant.GetIssuanceHistoryResponse\x12t\n\x17GetCertificateBlacklist\x12+.gsdk.tenant.GetCertificateBlacklistRequest\x1a,.gsdk.tenant.GetCertificateBlacklistResponse\x12t\n\x17\x41\x64\x64\x43\x65rtificateBlacklist\x12+.gsdk.tenant.AddCertificateBlacklistRequest\x1a,.gsdk.tenant.AddCertificateBlacklistResponse\x12}\n\x1a\x44\x65leteCertificateBlacklist\x12..gsdk.tenant.DeleteCertificateBlacklistRequest\x1a/.gsdk.tenant.DeleteCertificateBlacklistResponseB5\n\x19\x63om.supremainc.sdk.tenantP\x01Z\x16\x62iostar/service/tenantb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tenant_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.supremainc.sdk.tenantP\001Z\026biostar/service/tenant'
  _TENANTINFO._serialized_start=41
  _TENANTINFO._serialized_end=91
  _GETLISTREQUEST._serialized_start=93
  _GETLISTREQUEST._serialized_end=109
  _GETLISTRESPONSE._serialized_start=111
  _GETLISTRESPONSE._serialized_end=147
  _GETREQUEST._serialized_start=149
  _GETREQUEST._serialized_end=180
  _GETRESPONSE._serialized_start=182
  _GETRESPONSE._serialized_end=241
  _ADDREQUEST._serialized_start=243
  _ADDREQUEST._serialized_end=301
  _ADDRESPONSE._serialized_start=303
  _ADDRESPONSE._serialized_end=316
  _DELETEREQUEST._serialized_start=318
  _DELETEREQUEST._serialized_end=352
  _DELETERESPONSE._serialized_start=354
  _DELETERESPONSE._serialized_end=370
  _ADDGATEWAYREQUEST._serialized_start=372
  _ADDGATEWAYREQUEST._serialized_end=429
  _ADDGATEWAYRESPONSE._serialized_start=431
  _ADDGATEWAYRESPONSE._serialized_end=451
  _DELETEGATEWAYREQUEST._serialized_start=453
  _DELETEGATEWAYREQUEST._serialized_end=513
  _DELETEGATEWAYRESPONSE._serialized_start=515
  _DELETEGATEWAYRESPONSE._serialized_end=538
  _CREATECERTIFICATEREQUEST._serialized_start=540
  _CREATECERTIFICATEREQUEST._serialized_end=647
  _CREATECERTIFICATERESPONSE._serialized_start=649
  _CREATECERTIFICATERESPONSE._serialized_end=715
  _GETISSUANCEHISTORYREQUEST._serialized_start=717
  _GETISSUANCEHISTORYREQUEST._serialized_end=763
  _CERTIFICATEINFO._serialized_start=766
  _CERTIFICATEINFO._serialized_end=916
  _GETISSUANCEHISTORYRESPONSE._serialized_start=918
  _GETISSUANCEHISTORYRESPONSE._serialized_end=995
  _GETCERTIFICATEBLACKLISTREQUEST._serialized_start=997
  _GETCERTIFICATEBLACKLISTREQUEST._serialized_end=1048
  _GETCERTIFICATEBLACKLISTRESPONSE._serialized_start=1050
  _GETCERTIFICATEBLACKLISTRESPONSE._serialized_end=1132
  _ADDCERTIFICATEBLACKLISTREQUEST._serialized_start=1134
  _ADDCERTIFICATEBLACKLISTREQUEST._serialized_end=1203
  _ADDCERTIFICATEBLACKLISTRESPONSE._serialized_start=1205
  _ADDCERTIFICATEBLACKLISTRESPONSE._serialized_end=1238
  _DELETECERTIFICATEBLACKLISTREQUEST._serialized_start=1240
  _DELETECERTIFICATEBLACKLISTREQUEST._serialized_end=1312
  _DELETECERTIFICATEBLACKLISTRESPONSE._serialized_start=1314
  _DELETECERTIFICATEBLACKLISTRESPONSE._serialized_end=1350
  _TENANT._serialized_start=1353
  _TENANT._serialized_end=2347
# @@protoc_insertion_point(module_scope)
