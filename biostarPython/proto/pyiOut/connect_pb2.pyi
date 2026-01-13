import device_pb2 as _device_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVER_TO_DEVICE: _ClassVar[ConnectionMode]
    DEVICE_TO_SERVER: _ClassVar[ConnectionMode]
    DEFAULT: _ClassVar[ConnectionMode]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISCONNECTED: _ClassVar[Status]
    TCP_CONNECTED: _ClassVar[Status]
    TLS_CONNECTED: _ClassVar[Status]
    TCP_CANNOT_CONNECT: _ClassVar[Status]
    TCP_NOT_ALLOWED: _ClassVar[Status]
    TLS_CANNOT_CONNECT: _ClassVar[Status]
    TLS_NOT_ALLOWED: _ClassVar[Status]
SERVER_TO_DEVICE: ConnectionMode
DEVICE_TO_SERVER: ConnectionMode
DEFAULT: ConnectionMode
DISCONNECTED: Status
TCP_CONNECTED: Status
TLS_CONNECTED: Status
TCP_CANNOT_CONNECT: Status
TCP_NOT_ALLOWED: Status
TLS_CANNOT_CONNECT: Status
TLS_NOT_ALLOWED: Status

class ConnectInfo(_message.Message):
    __slots__ = ("IPAddr", "port", "useSSL")
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USESSL_FIELD_NUMBER: _ClassVar[int]
    IPAddr: str
    port: int
    useSSL: bool
    def __init__(self, IPAddr: _Optional[str] = ..., port: _Optional[int] = ..., useSSL: bool = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ("connectInfo",)
    CONNECTINFO_FIELD_NUMBER: _ClassVar[int]
    connectInfo: ConnectInfo
    def __init__(self, connectInfo: _Optional[_Union[ConnectInfo, _Mapping]] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class AsyncConnectInfo(_message.Message):
    __slots__ = ("deviceID", "IPAddr", "port", "useSSL")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USESSL_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    IPAddr: str
    port: int
    useSSL: bool
    def __init__(self, deviceID: _Optional[int] = ..., IPAddr: _Optional[str] = ..., port: _Optional[int] = ..., useSSL: bool = ...) -> None: ...

class AddAsyncConnectionRequest(_message.Message):
    __slots__ = ("connectInfos",)
    CONNECTINFOS_FIELD_NUMBER: _ClassVar[int]
    connectInfos: _containers.RepeatedCompositeFieldContainer[AsyncConnectInfo]
    def __init__(self, connectInfos: _Optional[_Iterable[_Union[AsyncConnectInfo, _Mapping]]] = ...) -> None: ...

class AddAsyncConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAsyncConnectionRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAsyncConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptFilter(_message.Message):
    __slots__ = ("allowAll", "deviceIDs", "IPAddrs", "subnetMasks")
    ALLOWALL_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    IPADDRS_FIELD_NUMBER: _ClassVar[int]
    SUBNETMASKS_FIELD_NUMBER: _ClassVar[int]
    allowAll: bool
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    IPAddrs: _containers.RepeatedScalarFieldContainer[str]
    subnetMasks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowAll: bool = ..., deviceIDs: _Optional[_Iterable[int]] = ..., IPAddrs: _Optional[_Iterable[str]] = ..., subnetMasks: _Optional[_Iterable[str]] = ...) -> None: ...

class SetAcceptFilterRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: AcceptFilter
    def __init__(self, filter: _Optional[_Union[AcceptFilter, _Mapping]] = ...) -> None: ...

class SetAcceptFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAcceptFilterRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAcceptFilterResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: AcceptFilter
    def __init__(self, filter: _Optional[_Union[AcceptFilter, _Mapping]] = ...) -> None: ...

class PendingDeviceInfo(_message.Message):
    __slots__ = ("deviceID", "type", "IPAddr", "lastTry")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    LASTTRY_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: _device_pb2.Type
    IPAddr: str
    lastTry: int
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.Type, str]] = ..., IPAddr: _Optional[str] = ..., lastTry: _Optional[int] = ...) -> None: ...

class GetPendingListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPendingListResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[PendingDeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[PendingDeviceInfo, _Mapping]]] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("deviceID", "type", "connectionMode", "IPAddr", "port", "status", "autoReconnect", "useSSL")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTORECONNECT_FIELD_NUMBER: _ClassVar[int]
    USESSL_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: _device_pb2.Type
    connectionMode: ConnectionMode
    IPAddr: str
    port: int
    status: Status
    autoReconnect: bool
    useSSL: bool
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.Type, str]] = ..., connectionMode: _Optional[_Union[ConnectionMode, str]] = ..., IPAddr: _Optional[str] = ..., port: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ..., autoReconnect: bool = ..., useSSL: bool = ...) -> None: ...

class GetDeviceListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceListResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[DeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[DeviceInfo, _Mapping]]] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DisconnectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisconnectAllRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisconnectAllResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchDeviceRequest(_message.Message):
    __slots__ = ("timeout",)
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timeout: int
    def __init__(self, timeout: _Optional[int] = ...) -> None: ...

class SearchDeviceInfo(_message.Message):
    __slots__ = ("deviceID", "type", "useDHCP", "connectionMode", "IPAddr", "port", "useSSL", "serverAddr")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USEDHCP_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    IPADDR_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USESSL_FIELD_NUMBER: _ClassVar[int]
    SERVERADDR_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: _device_pb2.Type
    useDHCP: bool
    connectionMode: ConnectionMode
    IPAddr: str
    port: int
    useSSL: bool
    serverAddr: str
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.Type, str]] = ..., useDHCP: bool = ..., connectionMode: _Optional[_Union[ConnectionMode, str]] = ..., IPAddr: _Optional[str] = ..., port: _Optional[int] = ..., useSSL: bool = ..., serverAddr: _Optional[str] = ...) -> None: ...

class SearchDeviceResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[SearchDeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[SearchDeviceInfo, _Mapping]]] = ...) -> None: ...

class SlaveDeviceInfo(_message.Message):
    __slots__ = ("deviceID", "rs485SlaveDeviceIDs", "wiegandSlaveDeviceIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    RS485SLAVEDEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    WIEGANDSLAVEDEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    rs485SlaveDeviceIDs: _containers.RepeatedScalarFieldContainer[int]
    wiegandSlaveDeviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., rs485SlaveDeviceIDs: _Optional[_Iterable[int]] = ..., wiegandSlaveDeviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetSlaveDeviceRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSlaveDeviceResponse(_message.Message):
    __slots__ = ("slaveDeviceInfos",)
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, slaveDeviceInfos: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetSlaveDeviceRequest(_message.Message):
    __slots__ = ("slaveDeviceInfos",)
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, slaveDeviceInfos: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetSlaveDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeStatusRequest(_message.Message):
    __slots__ = ("queueSize",)
    QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
    queueSize: int
    def __init__(self, queueSize: _Optional[int] = ...) -> None: ...

class SubscribeStatusResponse(_message.Message):
    __slots__ = ("statusChanID",)
    STATUSCHANID_FIELD_NUMBER: _ClassVar[int]
    statusChanID: str
    def __init__(self, statusChanID: _Optional[str] = ...) -> None: ...

class StatusChange(_message.Message):
    __slots__ = ("deviceID", "status", "timestamp")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    status: Status
    timestamp: int
    def __init__(self, deviceID: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SetConnectionModeRequest(_message.Message):
    __slots__ = ("deviceID", "connectionMode")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    connectionMode: ConnectionMode
    def __init__(self, deviceID: _Optional[int] = ..., connectionMode: _Optional[_Union[ConnectionMode, str]] = ...) -> None: ...

class SetConnectionModeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConnectionModeMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "connectionMode")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    connectionMode: ConnectionMode
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., connectionMode: _Optional[_Union[ConnectionMode, str]] = ...) -> None: ...

class SetConnectionModeMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class EnableSSLRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class EnableSSLResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableSSLMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class EnableSSLMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DisableSSLRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DisableSSLResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableSSLMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DisableSSLMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
