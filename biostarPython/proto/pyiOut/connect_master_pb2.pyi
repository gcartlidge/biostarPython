import connect_pb2 as _connect_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectRequest(_message.Message):
    __slots__ = ("gatewayID", "connectInfo")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    CONNECTINFO_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    connectInfo: _connect_pb2.ConnectInfo
    def __init__(self, gatewayID: _Optional[str] = ..., connectInfo: _Optional[_Union[_connect_pb2.ConnectInfo, _Mapping]] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class AddAsyncConnectionRequest(_message.Message):
    __slots__ = ("gatewayID", "connectInfos")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    CONNECTINFOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    connectInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.AsyncConnectInfo]
    def __init__(self, gatewayID: _Optional[str] = ..., connectInfos: _Optional[_Iterable[_Union[_connect_pb2.AsyncConnectInfo, _Mapping]]] = ...) -> None: ...

class AddAsyncConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAsyncConnectionRequest(_message.Message):
    __slots__ = ("gatewayID", "deviceIDs")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gatewayID: _Optional[str] = ..., deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAsyncConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddAsyncConnectionDBRequest(_message.Message):
    __slots__ = ("gatewayID", "connectInfos")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    CONNECTINFOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    connectInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.AsyncConnectInfo]
    def __init__(self, gatewayID: _Optional[str] = ..., connectInfos: _Optional[_Iterable[_Union[_connect_pb2.AsyncConnectInfo, _Mapping]]] = ...) -> None: ...

class AddAsyncConnectionDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAsyncConnectionDBRequest(_message.Message):
    __slots__ = ("gatewayID", "deviceIDs")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gatewayID: _Optional[str] = ..., deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAsyncConnectionDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAsyncConnectionDBRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetAsyncConnectionDBResponse(_message.Message):
    __slots__ = ("connectInfos",)
    CONNECTINFOS_FIELD_NUMBER: _ClassVar[int]
    connectInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.AsyncConnectInfo]
    def __init__(self, connectInfos: _Optional[_Iterable[_Union[_connect_pb2.AsyncConnectInfo, _Mapping]]] = ...) -> None: ...

class SetAcceptFilterRequest(_message.Message):
    __slots__ = ("gatewayID", "filter")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    filter: _connect_pb2.AcceptFilter
    def __init__(self, gatewayID: _Optional[str] = ..., filter: _Optional[_Union[_connect_pb2.AcceptFilter, _Mapping]] = ...) -> None: ...

class SetAcceptFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAcceptFilterRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetAcceptFilterResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _connect_pb2.AcceptFilter
    def __init__(self, filter: _Optional[_Union[_connect_pb2.AcceptFilter, _Mapping]] = ...) -> None: ...

class SetAcceptFilterDBRequest(_message.Message):
    __slots__ = ("gatewayID", "filter")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    filter: _connect_pb2.AcceptFilter
    def __init__(self, gatewayID: _Optional[str] = ..., filter: _Optional[_Union[_connect_pb2.AcceptFilter, _Mapping]] = ...) -> None: ...

class SetAcceptFilterDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAcceptFilterDBRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetAcceptFilterDBResponse(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _connect_pb2.AcceptFilter
    def __init__(self, filter: _Optional[_Union[_connect_pb2.AcceptFilter, _Mapping]] = ...) -> None: ...

class GetPendingListRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetPendingListResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.PendingDeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[_connect_pb2.PendingDeviceInfo, _Mapping]]] = ...) -> None: ...

class GetDeviceListRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetDeviceListResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.DeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[_connect_pb2.DeviceInfo, _Mapping]]] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DisconnectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisconnectAllRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class DisconnectAllResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchDeviceRequest(_message.Message):
    __slots__ = ("gatewayID", "timeout")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    timeout: int
    def __init__(self, gatewayID: _Optional[str] = ..., timeout: _Optional[int] = ...) -> None: ...

class SearchDeviceResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.SearchDeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[_connect_pb2.SearchDeviceInfo, _Mapping]]] = ...) -> None: ...

class GetSlaveDeviceRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetSlaveDeviceResponse(_message.Message):
    __slots__ = ("slaveDeviceInfos",)
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.SlaveDeviceInfo]
    def __init__(self, slaveDeviceInfos: _Optional[_Iterable[_Union[_connect_pb2.SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetSlaveDeviceRequest(_message.Message):
    __slots__ = ("gatewayID", "slaveDeviceInfos")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.SlaveDeviceInfo]
    def __init__(self, gatewayID: _Optional[str] = ..., slaveDeviceInfos: _Optional[_Iterable[_Union[_connect_pb2.SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetSlaveDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddSlaveDeviceDBRequest(_message.Message):
    __slots__ = ("gatewayID", "slaveDeviceInfos")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.SlaveDeviceInfo]
    def __init__(self, gatewayID: _Optional[str] = ..., slaveDeviceInfos: _Optional[_Iterable[_Union[_connect_pb2.SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class AddSlaveDeviceDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSlaveDeviceDBRequest(_message.Message):
    __slots__ = ("gatewayID", "deviceIDs")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gatewayID: _Optional[str] = ..., deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteSlaveDeviceDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSlaveDeviceDBRequest(_message.Message):
    __slots__ = ("gatewayID",)
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    def __init__(self, gatewayID: _Optional[str] = ...) -> None: ...

class GetSlaveDeviceDBResponse(_message.Message):
    __slots__ = ("slaveDeviceInfos",)
    SLAVEDEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveDeviceInfos: _containers.RepeatedCompositeFieldContainer[_connect_pb2.SlaveDeviceInfo]
    def __init__(self, slaveDeviceInfos: _Optional[_Iterable[_Union[_connect_pb2.SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SubscribeStatusRequest(_message.Message):
    __slots__ = ("queueSize",)
    QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
    queueSize: int
    def __init__(self, queueSize: _Optional[int] = ...) -> None: ...

class SetConnectionModeRequest(_message.Message):
    __slots__ = ("deviceID", "connectionMode")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    connectionMode: _connect_pb2.ConnectionMode
    def __init__(self, deviceID: _Optional[int] = ..., connectionMode: _Optional[_Union[_connect_pb2.ConnectionMode, str]] = ...) -> None: ...

class SetConnectionModeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConnectionModeMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "connectionMode")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONMODE_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    connectionMode: _connect_pb2.ConnectionMode
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., connectionMode: _Optional[_Union[_connect_pb2.ConnectionMode, str]] = ...) -> None: ...

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
