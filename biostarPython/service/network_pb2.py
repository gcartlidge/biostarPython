# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2
from biostarPython.service import connect_pb2 as connect__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnetwork.proto\x12\x07network\x1a\terr.proto\x1a\rconnect.proto\"&\n\x12GetIPConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"8\n\x13GetIPConfigResponse\x12!\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x11.network.IPConfig\"I\n\x12SetIPConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12!\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x11.network.IPConfig\"\x15\n\x13SetIPConfigResponse\"O\n\x17SetIPConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12!\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x11.network.IPConfig\"D\n\x18SetIPConfigMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"\xc2\x02\n\x08IPConfig\x12\x0f\n\x07useDHCP\x18\x01 \x01(\x08\x12\x0e\n\x06IPAddr\x18\x02 \x01(\t\x12\x0f\n\x07gateway\x18\x03 \x01(\t\x12\x12\n\nsubnetMask\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x12/\n\x0e\x63onnectionMode\x18\x06 \x01(\x0e\x32\x17.connect.ConnectionMode\x12\x12\n\nserverAddr\x18\x07 \x01(\t\x12\x12\n\nserverPort\x18\x08 \x01(\x05\x12\x15\n\rSSLServerPort\x18\t \x01(\x05\x12\x0e\n\x06useDNS\x18\n \x01(\x08\x12\x11\n\tDNSServer\x18\x0b \x01(\t\x12\x11\n\tserverURL\x18\x0c \x01(\t\x12\x0f\n\x07MTUSize\x18\r \x01(\x05\x12+\n\x08\x62\x61seband\x18\x0e \x01(\x0e\x32\x19.network.EthernetBaseband\"(\n\x14GetWLANConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"<\n\x15GetWLANConfigResponse\x12#\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x13.network.WLANConfig\"M\n\x14SetWLANConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.network.WLANConfig\"\x17\n\x15SetWLANConfigResponse\"S\n\x19SetWLANConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.network.WLANConfig\"F\n\x1aSetWLANConfigMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"\xc0\x01\n\nWLANConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12*\n\x06opMode\x18\x02 \x01(\x0e\x32\x1a.network.WLANOperationMode\x12\'\n\x08\x61uthType\x18\x03 \x01(\x0e\x32\x15.network.WLANAuthType\x12,\n\x07\x65ncType\x18\x04 \x01(\x0e\x32\x1b.network.WLANEncryptionType\x12\r\n\x05\x45SSID\x18\x05 \x01(\t\x12\x0f\n\x07\x61uthKey\x18\x06 \x01(\t*A\n\x10\x45thernetBaseband\x12\x15\n\x11\x42\x41SEBAND_10BASE_T\x10\x00\x12\x16\n\x12\x42\x41SEBAND_100BASE_T\x10\x01*C\n\x11WLANOperationMode\x12\x17\n\x13WLAN_OPMODE_MANAGED\x10\x00\x12\x15\n\x11WLAN_OPMODE_ADHOC\x10\x01*g\n\x0cWLANAuthType\x12\x12\n\x0eWLAN_AUTH_OPEN\x10\x00\x12\x14\n\x10WLAN_AUTH_SHARED\x10\x01\x12\x15\n\x11WLAN_AUTH_WPA_PSK\x10\x02\x12\x16\n\x12WLAN_AUTH_WPA2_PSK\x10\x03*\x85\x01\n\x12WLANEncryptionType\x12\x11\n\rWLAN_ENC_NONE\x10\x00\x12\x14\n\x10\x42S2_WLAN_ENC_WEP\x10\x01\x12\x19\n\x15\x42S2_WLAN_ENC_TKIP_AES\x10\x02\x12\x14\n\x10\x42S2_WLAN_ENC_AES\x10\x03\x12\x15\n\x11\x42S2_WLAN_ENC_TKIP\x10\x04\x32\xf5\x03\n\x07Network\x12H\n\x0bGetIPConfig\x12\x1b.network.GetIPConfigRequest\x1a\x1c.network.GetIPConfigResponse\x12H\n\x0bSetIPConfig\x12\x1b.network.SetIPConfigRequest\x1a\x1c.network.SetIPConfigResponse\x12W\n\x10SetIPConfigMulti\x12 .network.SetIPConfigMultiRequest\x1a!.network.SetIPConfigMultiResponse\x12N\n\rGetWLANConfig\x12\x1d.network.GetWLANConfigRequest\x1a\x1e.network.GetWLANConfigResponse\x12N\n\rSetWLANConfig\x12\x1d.network.SetWLANConfigRequest\x1a\x1e.network.SetWLANConfigResponse\x12]\n\x12SetWLANConfigMulti\x12\".network.SetWLANConfigMultiRequest\x1a#.network.SetWLANConfigMultiResponseB7\n\x1a\x63om.supremainc.sdk.networkP\x01Z\x17\x62iostar/service/networkb\x06proto3')

_ETHERNETBASEBAND = DESCRIPTOR.enum_types_by_name['EthernetBaseband']
EthernetBaseband = enum_type_wrapper.EnumTypeWrapper(_ETHERNETBASEBAND)
_WLANOPERATIONMODE = DESCRIPTOR.enum_types_by_name['WLANOperationMode']
WLANOperationMode = enum_type_wrapper.EnumTypeWrapper(_WLANOPERATIONMODE)
_WLANAUTHTYPE = DESCRIPTOR.enum_types_by_name['WLANAuthType']
WLANAuthType = enum_type_wrapper.EnumTypeWrapper(_WLANAUTHTYPE)
_WLANENCRYPTIONTYPE = DESCRIPTOR.enum_types_by_name['WLANEncryptionType']
WLANEncryptionType = enum_type_wrapper.EnumTypeWrapper(_WLANENCRYPTIONTYPE)
BASEBAND_10BASE_T = 0
BASEBAND_100BASE_T = 1
WLAN_OPMODE_MANAGED = 0
WLAN_OPMODE_ADHOC = 1
WLAN_AUTH_OPEN = 0
WLAN_AUTH_SHARED = 1
WLAN_AUTH_WPA_PSK = 2
WLAN_AUTH_WPA2_PSK = 3
WLAN_ENC_NONE = 0
BS2_WLAN_ENC_WEP = 1
BS2_WLAN_ENC_TKIP_AES = 2
BS2_WLAN_ENC_AES = 3
BS2_WLAN_ENC_TKIP = 4


_GETIPCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetIPConfigRequest']
_GETIPCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['GetIPConfigResponse']
_SETIPCONFIGREQUEST = DESCRIPTOR.message_types_by_name['SetIPConfigRequest']
_SETIPCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['SetIPConfigResponse']
_SETIPCONFIGMULTIREQUEST = DESCRIPTOR.message_types_by_name['SetIPConfigMultiRequest']
_SETIPCONFIGMULTIRESPONSE = DESCRIPTOR.message_types_by_name['SetIPConfigMultiResponse']
_IPCONFIG = DESCRIPTOR.message_types_by_name['IPConfig']
_GETWLANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['GetWLANConfigRequest']
_GETWLANCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['GetWLANConfigResponse']
_SETWLANCONFIGREQUEST = DESCRIPTOR.message_types_by_name['SetWLANConfigRequest']
_SETWLANCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['SetWLANConfigResponse']
_SETWLANCONFIGMULTIREQUEST = DESCRIPTOR.message_types_by_name['SetWLANConfigMultiRequest']
_SETWLANCONFIGMULTIRESPONSE = DESCRIPTOR.message_types_by_name['SetWLANConfigMultiResponse']
_WLANCONFIG = DESCRIPTOR.message_types_by_name['WLANConfig']
GetIPConfigRequest = _reflection.GeneratedProtocolMessageType('GetIPConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIPCONFIGREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.GetIPConfigRequest)
  })
_sym_db.RegisterMessage(GetIPConfigRequest)

GetIPConfigResponse = _reflection.GeneratedProtocolMessageType('GetIPConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETIPCONFIGRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.GetIPConfigResponse)
  })
_sym_db.RegisterMessage(GetIPConfigResponse)

SetIPConfigRequest = _reflection.GeneratedProtocolMessageType('SetIPConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETIPCONFIGREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetIPConfigRequest)
  })
_sym_db.RegisterMessage(SetIPConfigRequest)

SetIPConfigResponse = _reflection.GeneratedProtocolMessageType('SetIPConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETIPCONFIGRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetIPConfigResponse)
  })
_sym_db.RegisterMessage(SetIPConfigResponse)

SetIPConfigMultiRequest = _reflection.GeneratedProtocolMessageType('SetIPConfigMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETIPCONFIGMULTIREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetIPConfigMultiRequest)
  })
_sym_db.RegisterMessage(SetIPConfigMultiRequest)

SetIPConfigMultiResponse = _reflection.GeneratedProtocolMessageType('SetIPConfigMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETIPCONFIGMULTIRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetIPConfigMultiResponse)
  })
_sym_db.RegisterMessage(SetIPConfigMultiResponse)

IPConfig = _reflection.GeneratedProtocolMessageType('IPConfig', (_message.Message,), {
  'DESCRIPTOR' : _IPCONFIG,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.IPConfig)
  })
_sym_db.RegisterMessage(IPConfig)

GetWLANConfigRequest = _reflection.GeneratedProtocolMessageType('GetWLANConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWLANCONFIGREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.GetWLANConfigRequest)
  })
_sym_db.RegisterMessage(GetWLANConfigRequest)

GetWLANConfigResponse = _reflection.GeneratedProtocolMessageType('GetWLANConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETWLANCONFIGRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.GetWLANConfigResponse)
  })
_sym_db.RegisterMessage(GetWLANConfigResponse)

SetWLANConfigRequest = _reflection.GeneratedProtocolMessageType('SetWLANConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetWLANConfigRequest)
  })
_sym_db.RegisterMessage(SetWLANConfigRequest)

SetWLANConfigResponse = _reflection.GeneratedProtocolMessageType('SetWLANConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetWLANConfigResponse)
  })
_sym_db.RegisterMessage(SetWLANConfigResponse)

SetWLANConfigMultiRequest = _reflection.GeneratedProtocolMessageType('SetWLANConfigMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGMULTIREQUEST,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetWLANConfigMultiRequest)
  })
_sym_db.RegisterMessage(SetWLANConfigMultiRequest)

SetWLANConfigMultiResponse = _reflection.GeneratedProtocolMessageType('SetWLANConfigMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETWLANCONFIGMULTIRESPONSE,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.SetWLANConfigMultiResponse)
  })
_sym_db.RegisterMessage(SetWLANConfigMultiResponse)

WLANConfig = _reflection.GeneratedProtocolMessageType('WLANConfig', (_message.Message,), {
  'DESCRIPTOR' : _WLANCONFIG,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:network.WLANConfig)
  })
_sym_db.RegisterMessage(WLANConfig)

_NETWORK = DESCRIPTOR.services_by_name['Network']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.supremainc.sdk.networkP\001Z\027biostar/service/network'
  _ETHERNETBASEBAND._serialized_start=1284
  _ETHERNETBASEBAND._serialized_end=1349
  _WLANOPERATIONMODE._serialized_start=1351
  _WLANOPERATIONMODE._serialized_end=1418
  _WLANAUTHTYPE._serialized_start=1420
  _WLANAUTHTYPE._serialized_end=1523
  _WLANENCRYPTIONTYPE._serialized_start=1526
  _WLANENCRYPTIONTYPE._serialized_end=1659
  _GETIPCONFIGREQUEST._serialized_start=52
  _GETIPCONFIGREQUEST._serialized_end=90
  _GETIPCONFIGRESPONSE._serialized_start=92
  _GETIPCONFIGRESPONSE._serialized_end=148
  _SETIPCONFIGREQUEST._serialized_start=150
  _SETIPCONFIGREQUEST._serialized_end=223
  _SETIPCONFIGRESPONSE._serialized_start=225
  _SETIPCONFIGRESPONSE._serialized_end=246
  _SETIPCONFIGMULTIREQUEST._serialized_start=248
  _SETIPCONFIGMULTIREQUEST._serialized_end=327
  _SETIPCONFIGMULTIRESPONSE._serialized_start=329
  _SETIPCONFIGMULTIRESPONSE._serialized_end=397
  _IPCONFIG._serialized_start=400
  _IPCONFIG._serialized_end=722
  _GETWLANCONFIGREQUEST._serialized_start=724
  _GETWLANCONFIGREQUEST._serialized_end=764
  _GETWLANCONFIGRESPONSE._serialized_start=766
  _GETWLANCONFIGRESPONSE._serialized_end=826
  _SETWLANCONFIGREQUEST._serialized_start=828
  _SETWLANCONFIGREQUEST._serialized_end=905
  _SETWLANCONFIGRESPONSE._serialized_start=907
  _SETWLANCONFIGRESPONSE._serialized_end=930
  _SETWLANCONFIGMULTIREQUEST._serialized_start=932
  _SETWLANCONFIGMULTIREQUEST._serialized_end=1015
  _SETWLANCONFIGMULTIRESPONSE._serialized_start=1017
  _SETWLANCONFIGMULTIRESPONSE._serialized_end=1087
  _WLANCONFIG._serialized_start=1090
  _WLANCONFIG._serialized_end=1282
  _NETWORK._serialized_start=1662
  _NETWORK._serialized_end=2163
# @@protoc_insertion_point(module_scope)
