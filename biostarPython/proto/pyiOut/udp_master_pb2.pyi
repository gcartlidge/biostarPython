import network_pb2 as _network_pb2
import udp_pb2 as _udp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetIPConfigRequest(_message.Message):
    __slots__ = ("gatewayID", "deviceInfo")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceInfo: _udp_pb2.DeviceInfo
    def __init__(self, gatewayID: _Optional[str] = ..., deviceInfo: _Optional[_Union[_udp_pb2.DeviceInfo, _Mapping]] = ...) -> None: ...

class GetIPConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _network_pb2.IPConfig
    def __init__(self, config: _Optional[_Union[_network_pb2.IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigRequest(_message.Message):
    __slots__ = ("gatewayID", "deviceInfo", "config")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceInfo: _udp_pb2.DeviceInfo
    config: _network_pb2.IPConfig
    def __init__(self, gatewayID: _Optional[str] = ..., deviceInfo: _Optional[_Union[_udp_pb2.DeviceInfo, _Mapping]] = ..., config: _Optional[_Union[_network_pb2.IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
