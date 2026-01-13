import network_pb2 as _network_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ("deviceID", "IPAddr")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    IPAddr: str
    def __init__(self, deviceID: _Optional[int] = ..., IPAddr: _Optional[str] = ...) -> None: ...

class GetIPConfigRequest(_message.Message):
    __slots__ = ("deviceInfo",)
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    deviceInfo: DeviceInfo
    def __init__(self, deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GetIPConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _network_pb2.IPConfig
    def __init__(self, config: _Optional[_Union[_network_pb2.IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigRequest(_message.Message):
    __slots__ = ("deviceInfo", "config")
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceInfo: DeviceInfo
    config: _network_pb2.IPConfig
    def __init__(self, deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ..., config: _Optional[_Union[_network_pb2.IPConfig, _Mapping]] = ...) -> None: ...

class SetIPConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
