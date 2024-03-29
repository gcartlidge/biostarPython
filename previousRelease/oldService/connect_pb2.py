# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: connect.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import device_pb2 as device__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rconnect.proto\x12\x0cgsdk.connect\x1a\x0c\x64\x65vice.proto\x1a\terr.proto\";\n\x0b\x43onnectInfo\x12\x0e\n\x06IPAddr\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0e\n\x06useSSL\x18\x03 \x01(\x08\"@\n\x0e\x43onnectRequest\x12.\n\x0b\x63onnectInfo\x18\x01 \x01(\x0b\x32\x19.gsdk.connect.ConnectInfo\"#\n\x0f\x43onnectResponse\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"R\n\x10\x41syncConnectInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06IPAddr\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0e\n\x06useSSL\x18\x04 \x01(\x08\"Q\n\x19\x41\x64\x64\x41syncConnectionRequest\x12\x34\n\x0c\x63onnectInfos\x18\x01 \x03(\x0b\x32\x1e.gsdk.connect.AsyncConnectInfo\"\x1c\n\x1a\x41\x64\x64\x41syncConnectionResponse\"1\n\x1c\x44\x65leteAsyncConnectionRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"\x1f\n\x1d\x44\x65leteAsyncConnectionResponse\"Y\n\x0c\x41\x63\x63\x65ptFilter\x12\x10\n\x08\x61llowAll\x18\x01 \x01(\x08\x12\x11\n\tdeviceIDs\x18\x02 \x03(\r\x12\x0f\n\x07IPAddrs\x18\x03 \x03(\t\x12\x13\n\x0bsubnetMasks\x18\x04 \x03(\t\"D\n\x16SetAcceptFilterRequest\x12*\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1a.gsdk.connect.AcceptFilter\"\x19\n\x17SetAcceptFilterResponse\"\x18\n\x16GetAcceptFilterRequest\"E\n\x17GetAcceptFilterResponse\x12*\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x1a.gsdk.connect.AcceptFilter\"F\n\x11PendingDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06IPAddr\x18\x02 \x01(\t\x12\x0f\n\x07lastTry\x18\x03 \x01(\r\"\x17\n\x15GetPendingListRequest\"N\n\x16GetPendingListResponse\x12\x34\n\x0b\x64\x65viceInfos\x18\x01 \x03(\x0b\x32\x1f.gsdk.connect.PendingDeviceInfo\"\xbf\x01\n\nDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x34\n\x0e\x63onnectionMode\x18\x02 \x01(\x0e\x32\x1c.gsdk.connect.ConnectionMode\x12\x0e\n\x06IPAddr\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12$\n\x06status\x18\x05 \x01(\x0e\x32\x14.gsdk.connect.Status\x12\x15\n\rautoReconnect\x18\x06 \x01(\x08\x12\x0e\n\x06useSSL\x18\x07 \x01(\x08\"\x16\n\x14GetDeviceListRequest\"F\n\x15GetDeviceListResponse\x12-\n\x0b\x64\x65viceInfos\x18\x01 \x03(\x0b\x32\x18.gsdk.connect.DeviceInfo\"&\n\x11\x44isconnectRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"\x14\n\x12\x44isconnectResponse\"\x16\n\x14\x44isconnectAllRequest\"\x17\n\x15\x44isconnectAllResponse\"&\n\x13SearchDeviceRequest\x12\x0f\n\x07timeout\x18\x01 \x01(\r\"\xba\x01\n\x10SearchDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.gsdk.device.Type\x12\x0f\n\x07useDHCP\x18\x03 \x01(\x08\x12\x34\n\x0e\x63onnectionMode\x18\x04 \x01(\x0e\x32\x1c.gsdk.connect.ConnectionMode\x12\x0e\n\x06IPAddr\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\x12\x0e\n\x06useSSL\x18\x07 \x01(\x08\"K\n\x14SearchDeviceResponse\x12\x33\n\x0b\x64\x65viceInfos\x18\x01 \x03(\x0b\x32\x1e.gsdk.connect.SearchDeviceInfo\"_\n\x0fSlaveDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x1b\n\x13rs485SlaveDeviceIDs\x18\x02 \x03(\r\x12\x1d\n\x15wiegandSlaveDeviceIDs\x18\x03 \x03(\r\"\x17\n\x15GetSlaveDeviceRequest\"Q\n\x16GetSlaveDeviceResponse\x12\x37\n\x10slaveDeviceInfos\x18\x01 \x03(\x0b\x32\x1d.gsdk.connect.SlaveDeviceInfo\"P\n\x15SetSlaveDeviceRequest\x12\x37\n\x10slaveDeviceInfos\x18\x01 \x03(\x0b\x32\x1d.gsdk.connect.SlaveDeviceInfo\"\x18\n\x16SetSlaveDeviceResponse\"+\n\x16SubscribeStatusRequest\x12\x11\n\tqueueSize\x18\x01 \x01(\x05\"/\n\x17SubscribeStatusResponse\x12\x14\n\x0cstatusChanID\x18\x01 \x01(\t\"Y\n\x0cStatusChange\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.gsdk.connect.Status\x12\x11\n\ttimestamp\x18\x03 \x01(\r\"b\n\x18SetConnectionModeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x34\n\x0e\x63onnectionMode\x18\x02 \x01(\x0e\x32\x1c.gsdk.connect.ConnectionMode\"\x1b\n\x19SetConnectionModeResponse\"h\n\x1dSetConnectionModeMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x34\n\x0e\x63onnectionMode\x18\x02 \x01(\x0e\x32\x1c.gsdk.connect.ConnectionMode\"O\n\x1eSetConnectionModeMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"$\n\x10\x45nableSSLRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x45nableSSLResponse\"*\n\x15\x45nableSSLMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"G\n\x16\x45nableSSLMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"%\n\x11\x44isableSSLRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x14\n\x12\x44isableSSLResponse\"+\n\x16\x44isableSSLMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"H\n\x17\x44isableSSLMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*M\n\x0e\x43onnectionMode\x12\x14\n\x10SERVER_TO_DEVICE\x10\x00\x12\x14\n\x10\x44\x45VICE_TO_SERVER\x10\x01\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x1a\x02\x10\x01*\x9e\x01\n\x06Status\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\x11\n\rTCP_CONNECTED\x10\x01\x12\x11\n\rTLS_CONNECTED\x10\x02\x12\x17\n\x12TCP_CANNOT_CONNECT\x10\x80\x02\x12\x14\n\x0fTCP_NOT_ALLOWED\x10\x81\x02\x12\x17\n\x12TLS_CANNOT_CONNECT\x10\x80\x04\x12\x14\n\x0fTLS_NOT_ALLOWED\x10\x81\x04\x32\xed\r\n\x07\x43onnect\x12\x46\n\x07\x43onnect\x12\x1c.gsdk.connect.ConnectRequest\x1a\x1d.gsdk.connect.ConnectResponse\x12g\n\x12\x41\x64\x64\x41syncConnection\x12\'.gsdk.connect.AddAsyncConnectionRequest\x1a(.gsdk.connect.AddAsyncConnectionResponse\x12p\n\x15\x44\x65leteAsyncConnection\x12*.gsdk.connect.DeleteAsyncConnectionRequest\x1a+.gsdk.connect.DeleteAsyncConnectionResponse\x12^\n\x0fSetAcceptFilter\x12$.gsdk.connect.SetAcceptFilterRequest\x1a%.gsdk.connect.SetAcceptFilterResponse\x12^\n\x0fGetAcceptFilter\x12$.gsdk.connect.GetAcceptFilterRequest\x1a%.gsdk.connect.GetAcceptFilterResponse\x12[\n\x0eGetPendingList\x12#.gsdk.connect.GetPendingListRequest\x1a$.gsdk.connect.GetPendingListResponse\x12X\n\rGetDeviceList\x12\".gsdk.connect.GetDeviceListRequest\x1a#.gsdk.connect.GetDeviceListResponse\x12O\n\nDisconnect\x12\x1f.gsdk.connect.DisconnectRequest\x1a .gsdk.connect.DisconnectResponse\x12X\n\rDisconnectAll\x12\".gsdk.connect.DisconnectAllRequest\x1a#.gsdk.connect.DisconnectAllResponse\x12U\n\x0cSearchDevice\x12!.gsdk.connect.SearchDeviceRequest\x1a\".gsdk.connect.SearchDeviceResponse\x12[\n\x0eGetSlaveDevice\x12#.gsdk.connect.GetSlaveDeviceRequest\x1a$.gsdk.connect.GetSlaveDeviceResponse\x12[\n\x0eSetSlaveDevice\x12#.gsdk.connect.SetSlaveDeviceRequest\x1a$.gsdk.connect.SetSlaveDeviceResponse\x12\x64\n\x11SetConnectionMode\x12&.gsdk.connect.SetConnectionModeRequest\x1a\'.gsdk.connect.SetConnectionModeResponse\x12s\n\x16SetConnectionModeMulti\x12+.gsdk.connect.SetConnectionModeMultiRequest\x1a,.gsdk.connect.SetConnectionModeMultiResponse\x12L\n\tEnableSSL\x12\x1e.gsdk.connect.EnableSSLRequest\x1a\x1f.gsdk.connect.EnableSSLResponse\x12[\n\x0e\x45nableSSLMulti\x12#.gsdk.connect.EnableSSLMultiRequest\x1a$.gsdk.connect.EnableSSLMultiResponse\x12O\n\nDisableSSL\x12\x1f.gsdk.connect.DisableSSLRequest\x1a .gsdk.connect.DisableSSLResponse\x12^\n\x0f\x44isableSSLMulti\x12$.gsdk.connect.DisableSSLMultiRequest\x1a%.gsdk.connect.DisableSSLMultiResponse\x12U\n\x0fSubscribeStatus\x12$.gsdk.connect.SubscribeStatusRequest\x1a\x1a.gsdk.connect.StatusChange0\x01\x42\x37\n\x1a\x63om.supremainc.sdk.connectP\x01Z\x17\x62iostar/service/connectb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'connect_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.supremainc.sdk.connectP\001Z\027biostar/service/connect'
  _CONNECTIONMODE._options = None
  _CONNECTIONMODE._serialized_options = b'\020\001'
  _CONNECTIONMODE._serialized_start=2840
  _CONNECTIONMODE._serialized_end=2917
  _STATUS._serialized_start=2920
  _STATUS._serialized_end=3078
  _CONNECTINFO._serialized_start=56
  _CONNECTINFO._serialized_end=115
  _CONNECTREQUEST._serialized_start=117
  _CONNECTREQUEST._serialized_end=181
  _CONNECTRESPONSE._serialized_start=183
  _CONNECTRESPONSE._serialized_end=218
  _ASYNCCONNECTINFO._serialized_start=220
  _ASYNCCONNECTINFO._serialized_end=302
  _ADDASYNCCONNECTIONREQUEST._serialized_start=304
  _ADDASYNCCONNECTIONREQUEST._serialized_end=385
  _ADDASYNCCONNECTIONRESPONSE._serialized_start=387
  _ADDASYNCCONNECTIONRESPONSE._serialized_end=415
  _DELETEASYNCCONNECTIONREQUEST._serialized_start=417
  _DELETEASYNCCONNECTIONREQUEST._serialized_end=466
  _DELETEASYNCCONNECTIONRESPONSE._serialized_start=468
  _DELETEASYNCCONNECTIONRESPONSE._serialized_end=499
  _ACCEPTFILTER._serialized_start=501
  _ACCEPTFILTER._serialized_end=590
  _SETACCEPTFILTERREQUEST._serialized_start=592
  _SETACCEPTFILTERREQUEST._serialized_end=660
  _SETACCEPTFILTERRESPONSE._serialized_start=662
  _SETACCEPTFILTERRESPONSE._serialized_end=687
  _GETACCEPTFILTERREQUEST._serialized_start=689
  _GETACCEPTFILTERREQUEST._serialized_end=713
  _GETACCEPTFILTERRESPONSE._serialized_start=715
  _GETACCEPTFILTERRESPONSE._serialized_end=784
  _PENDINGDEVICEINFO._serialized_start=786
  _PENDINGDEVICEINFO._serialized_end=856
  _GETPENDINGLISTREQUEST._serialized_start=858
  _GETPENDINGLISTREQUEST._serialized_end=881
  _GETPENDINGLISTRESPONSE._serialized_start=883
  _GETPENDINGLISTRESPONSE._serialized_end=961
  _DEVICEINFO._serialized_start=964
  _DEVICEINFO._serialized_end=1155
  _GETDEVICELISTREQUEST._serialized_start=1157
  _GETDEVICELISTREQUEST._serialized_end=1179
  _GETDEVICELISTRESPONSE._serialized_start=1181
  _GETDEVICELISTRESPONSE._serialized_end=1251
  _DISCONNECTREQUEST._serialized_start=1253
  _DISCONNECTREQUEST._serialized_end=1291
  _DISCONNECTRESPONSE._serialized_start=1293
  _DISCONNECTRESPONSE._serialized_end=1313
  _DISCONNECTALLREQUEST._serialized_start=1315
  _DISCONNECTALLREQUEST._serialized_end=1337
  _DISCONNECTALLRESPONSE._serialized_start=1339
  _DISCONNECTALLRESPONSE._serialized_end=1362
  _SEARCHDEVICEREQUEST._serialized_start=1364
  _SEARCHDEVICEREQUEST._serialized_end=1402
  _SEARCHDEVICEINFO._serialized_start=1405
  _SEARCHDEVICEINFO._serialized_end=1591
  _SEARCHDEVICERESPONSE._serialized_start=1593
  _SEARCHDEVICERESPONSE._serialized_end=1668
  _SLAVEDEVICEINFO._serialized_start=1670
  _SLAVEDEVICEINFO._serialized_end=1765
  _GETSLAVEDEVICEREQUEST._serialized_start=1767
  _GETSLAVEDEVICEREQUEST._serialized_end=1790
  _GETSLAVEDEVICERESPONSE._serialized_start=1792
  _GETSLAVEDEVICERESPONSE._serialized_end=1873
  _SETSLAVEDEVICEREQUEST._serialized_start=1875
  _SETSLAVEDEVICEREQUEST._serialized_end=1955
  _SETSLAVEDEVICERESPONSE._serialized_start=1957
  _SETSLAVEDEVICERESPONSE._serialized_end=1981
  _SUBSCRIBESTATUSREQUEST._serialized_start=1983
  _SUBSCRIBESTATUSREQUEST._serialized_end=2026
  _SUBSCRIBESTATUSRESPONSE._serialized_start=2028
  _SUBSCRIBESTATUSRESPONSE._serialized_end=2075
  _STATUSCHANGE._serialized_start=2077
  _STATUSCHANGE._serialized_end=2166
  _SETCONNECTIONMODEREQUEST._serialized_start=2168
  _SETCONNECTIONMODEREQUEST._serialized_end=2266
  _SETCONNECTIONMODERESPONSE._serialized_start=2268
  _SETCONNECTIONMODERESPONSE._serialized_end=2295
  _SETCONNECTIONMODEMULTIREQUEST._serialized_start=2297
  _SETCONNECTIONMODEMULTIREQUEST._serialized_end=2401
  _SETCONNECTIONMODEMULTIRESPONSE._serialized_start=2403
  _SETCONNECTIONMODEMULTIRESPONSE._serialized_end=2482
  _ENABLESSLREQUEST._serialized_start=2484
  _ENABLESSLREQUEST._serialized_end=2520
  _ENABLESSLRESPONSE._serialized_start=2522
  _ENABLESSLRESPONSE._serialized_end=2541
  _ENABLESSLMULTIREQUEST._serialized_start=2543
  _ENABLESSLMULTIREQUEST._serialized_end=2585
  _ENABLESSLMULTIRESPONSE._serialized_start=2587
  _ENABLESSLMULTIRESPONSE._serialized_end=2658
  _DISABLESSLREQUEST._serialized_start=2660
  _DISABLESSLREQUEST._serialized_end=2697
  _DISABLESSLRESPONSE._serialized_start=2699
  _DISABLESSLRESPONSE._serialized_end=2719
  _DISABLESSLMULTIREQUEST._serialized_start=2721
  _DISABLESSLMULTIREQUEST._serialized_end=2764
  _DISABLESSLMULTIRESPONSE._serialized_start=2766
  _DISABLESSLMULTIRESPONSE._serialized_end=2838
  _CONNECT._serialized_start=3081
  _CONNECT._serialized_end=4854
# @@protoc_insertion_point(module_scope)
