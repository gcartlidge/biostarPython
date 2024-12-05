# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: network.proto
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
    'network.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2
from biostarPython.service import connect_pb2 as connect__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnetwork.proto\x12\x0cgsdk.network\x1a\terr.proto\x1a\rconnect.proto\"&\n\x12GetIPConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"=\n\x13GetIPConfigResponse\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.gsdk.network.IPConfig\"N\n\x12SetIPConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x16.gsdk.network.IPConfig\"\x15\n\x13SetIPConfigResponse\"T\n\x17SetIPConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x16.gsdk.network.IPConfig\"I\n\x18SetIPConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\xcc\x02\n\x08IPConfig\x12\x0f\n\x07useDHCP\x18\x01 \x01(\x08\x12\x0e\n\x06IPAddr\x18\x02 \x01(\t\x12\x0f\n\x07gateway\x18\x03 \x01(\t\x12\x12\n\nsubnetMask\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x12\x34\n\x0e\x63onnectionMode\x18\x06 \x01(\x0e\x32\x1c.gsdk.connect.ConnectionMode\x12\x12\n\nserverAddr\x18\x07 \x01(\t\x12\x12\n\nserverPort\x18\x08 \x01(\x05\x12\x15\n\rSSLServerPort\x18\t \x01(\x05\x12\x0e\n\x06useDNS\x18\n \x01(\x08\x12\x11\n\tDNSServer\x18\x0b \x01(\t\x12\x11\n\tserverURL\x18\x0c \x01(\t\x12\x0f\n\x07MTUSize\x18\r \x01(\x05\x12\x30\n\x08\x62\x61seband\x18\x0e \x01(\x0e\x32\x1e.gsdk.network.EthernetBaseband\"(\n\x14GetWLANConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"A\n\x15GetWLANConfigResponse\x12(\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x18.gsdk.network.WLANConfig\"R\n\x14SetWLANConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12(\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x18.gsdk.network.WLANConfig\"\x17\n\x15SetWLANConfigResponse\"X\n\x19SetWLANConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12(\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x18.gsdk.network.WLANConfig\"K\n\x1aSetWLANConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\xcf\x01\n\nWLANConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12/\n\x06opMode\x18\x02 \x01(\x0e\x32\x1f.gsdk.network.WLANOperationMode\x12,\n\x08\x61uthType\x18\x03 \x01(\x0e\x32\x1a.gsdk.network.WLANAuthType\x12\x31\n\x07\x65ncType\x18\x04 \x01(\x0e\x32 .gsdk.network.WLANEncryptionType\x12\r\n\x05\x45SSID\x18\x05 \x01(\t\x12\x0f\n\x07\x61uthKey\x18\x06 \x01(\t*\x80\x02\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x1d\n\x17\x44\x45\x46\x41ULT_TCP_DEVICE_PORT\x10\x8b\x90\x03\x12\x1d\n\x17\x44\x45\x46\x41ULT_TCP_SERVER_PORT\x10\x8c\x90\x03\x12!\n\x1b\x44\x45\x46\x41ULT_TCP_SSL_SERVER_PORT\x10\x8d\x90\x03\x12\x15\n\x10MIN_TCP_MTU_SIZE\x10\xb6\x08\x12\x15\n\x10MAX_TCP_MTU_SIZE\x10\xea\x0b\x12\x14\n\x10MAX_ESSID_LENGTH\x10 \x12\x17\n\x13MAX_WLAN_KEY_LENGTH\x10@\x12\x17\n\x12MAX_DNS_URL_LENGTH\x10\x80\x02*A\n\x10\x45thernetBaseband\x12\x15\n\x11\x42\x41SEBAND_10BASE_T\x10\x00\x12\x16\n\x12\x42\x41SEBAND_100BASE_T\x10\x01*C\n\x11WLANOperationMode\x12\x17\n\x13WLAN_OPMODE_MANAGED\x10\x00\x12\x15\n\x11WLAN_OPMODE_ADHOC\x10\x01*g\n\x0cWLANAuthType\x12\x12\n\x0eWLAN_AUTH_OPEN\x10\x00\x12\x14\n\x10WLAN_AUTH_SHARED\x10\x01\x12\x15\n\x11WLAN_AUTH_WPA_PSK\x10\x02\x12\x16\n\x12WLAN_AUTH_WPA2_PSK\x10\x03*\x85\x01\n\x12WLANEncryptionType\x12\x11\n\rWLAN_ENC_NONE\x10\x00\x12\x14\n\x10\x42S2_WLAN_ENC_WEP\x10\x01\x12\x19\n\x15\x42S2_WLAN_ENC_TKIP_AES\x10\x02\x12\x14\n\x10\x42S2_WLAN_ENC_AES\x10\x03\x12\x15\n\x11\x42S2_WLAN_ENC_TKIP\x10\x04\x32\xb1\x04\n\x07Network\x12R\n\x0bGetIPConfig\x12 .gsdk.network.GetIPConfigRequest\x1a!.gsdk.network.GetIPConfigResponse\x12R\n\x0bSetIPConfig\x12 .gsdk.network.SetIPConfigRequest\x1a!.gsdk.network.SetIPConfigResponse\x12\x61\n\x10SetIPConfigMulti\x12%.gsdk.network.SetIPConfigMultiRequest\x1a&.gsdk.network.SetIPConfigMultiResponse\x12X\n\rGetWLANConfig\x12\".gsdk.network.GetWLANConfigRequest\x1a#.gsdk.network.GetWLANConfigResponse\x12X\n\rSetWLANConfig\x12\".gsdk.network.SetWLANConfigRequest\x1a#.gsdk.network.SetWLANConfigResponse\x12g\n\x12SetWLANConfigMulti\x12\'.gsdk.network.SetWLANConfigMultiRequest\x1a(.gsdk.network.SetWLANConfigMultiResponseB7\n\x1a\x63om.supremainc.sdk.networkP\x01Z\x17\x62iostar/service/networkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'network_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.supremainc.sdk.networkP\001Z\027biostar/service/network'
  _globals['_ENUM']._serialized_start=1355
  _globals['_ENUM']._serialized_end=1611
  _globals['_ETHERNETBASEBAND']._serialized_start=1613
  _globals['_ETHERNETBASEBAND']._serialized_end=1678
  _globals['_WLANOPERATIONMODE']._serialized_start=1680
  _globals['_WLANOPERATIONMODE']._serialized_end=1747
  _globals['_WLANAUTHTYPE']._serialized_start=1749
  _globals['_WLANAUTHTYPE']._serialized_end=1852
  _globals['_WLANENCRYPTIONTYPE']._serialized_start=1855
  _globals['_WLANENCRYPTIONTYPE']._serialized_end=1988
  _globals['_GETIPCONFIGREQUEST']._serialized_start=57
  _globals['_GETIPCONFIGREQUEST']._serialized_end=95
  _globals['_GETIPCONFIGRESPONSE']._serialized_start=97
  _globals['_GETIPCONFIGRESPONSE']._serialized_end=158
  _globals['_SETIPCONFIGREQUEST']._serialized_start=160
  _globals['_SETIPCONFIGREQUEST']._serialized_end=238
  _globals['_SETIPCONFIGRESPONSE']._serialized_start=240
  _globals['_SETIPCONFIGRESPONSE']._serialized_end=261
  _globals['_SETIPCONFIGMULTIREQUEST']._serialized_start=263
  _globals['_SETIPCONFIGMULTIREQUEST']._serialized_end=347
  _globals['_SETIPCONFIGMULTIRESPONSE']._serialized_start=349
  _globals['_SETIPCONFIGMULTIRESPONSE']._serialized_end=422
  _globals['_IPCONFIG']._serialized_start=425
  _globals['_IPCONFIG']._serialized_end=757
  _globals['_GETWLANCONFIGREQUEST']._serialized_start=759
  _globals['_GETWLANCONFIGREQUEST']._serialized_end=799
  _globals['_GETWLANCONFIGRESPONSE']._serialized_start=801
  _globals['_GETWLANCONFIGRESPONSE']._serialized_end=866
  _globals['_SETWLANCONFIGREQUEST']._serialized_start=868
  _globals['_SETWLANCONFIGREQUEST']._serialized_end=950
  _globals['_SETWLANCONFIGRESPONSE']._serialized_start=952
  _globals['_SETWLANCONFIGRESPONSE']._serialized_end=975
  _globals['_SETWLANCONFIGMULTIREQUEST']._serialized_start=977
  _globals['_SETWLANCONFIGMULTIREQUEST']._serialized_end=1065
  _globals['_SETWLANCONFIGMULTIRESPONSE']._serialized_start=1067
  _globals['_SETWLANCONFIGMULTIRESPONSE']._serialized_end=1142
  _globals['_WLANCONFIG']._serialized_start=1145
  _globals['_WLANCONFIG']._serialized_end=1352
  _globals['_NETWORK']._serialized_start=1991
  _globals['_NETWORK']._serialized_end=2552
# @@protoc_insertion_point(module_scope)
