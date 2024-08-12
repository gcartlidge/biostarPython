import action_pb2 as _action_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_STATUS_NORMAL: _ClassVar[DeviceStatus]
    DEVICE_STATUS_LOCKED: _ClassVar[DeviceStatus]
    DEVICE_STATUS_RTC_ERROR: _ClassVar[DeviceStatus]
    DEVICE_STATUS_WAITING_INPUT: _ClassVar[DeviceStatus]
    DEVICE_STATUS_WAITING_DHCP: _ClassVar[DeviceStatus]
    DEVICE_STATUS_SCAN_FINGER: _ClassVar[DeviceStatus]
    DEVICE_STATUS_SCAN_CARD: _ClassVar[DeviceStatus]
    DEVICE_STATUS_SUCCESS: _ClassVar[DeviceStatus]
    DEVICE_STATUS_FAIL: _ClassVar[DeviceStatus]
    DEVICE_STATUS_DURESS: _ClassVar[DeviceStatus]
    DEVICE_STATUS_PROCESS_CONFIG_CARD: _ClassVar[DeviceStatus]
    DEVICE_STATUS_SUCCESS_CONFIG_CARD: _ClassVar[DeviceStatus]
    DEVICE_STATUS_SCAN_FACE: _ClassVar[DeviceStatus]
    DEVICE_STATUS_RESERVED3: _ClassVar[DeviceStatus]
    DEVICE_STATUS_RESERVED4: _ClassVar[DeviceStatus]
    MAX_DEVICE_STATUSES: _ClassVar[DeviceStatus]
DEVICE_STATUS_NORMAL: DeviceStatus
DEVICE_STATUS_LOCKED: DeviceStatus
DEVICE_STATUS_RTC_ERROR: DeviceStatus
DEVICE_STATUS_WAITING_INPUT: DeviceStatus
DEVICE_STATUS_WAITING_DHCP: DeviceStatus
DEVICE_STATUS_SCAN_FINGER: DeviceStatus
DEVICE_STATUS_SCAN_CARD: DeviceStatus
DEVICE_STATUS_SUCCESS: DeviceStatus
DEVICE_STATUS_FAIL: DeviceStatus
DEVICE_STATUS_DURESS: DeviceStatus
DEVICE_STATUS_PROCESS_CONFIG_CARD: DeviceStatus
DEVICE_STATUS_SUCCESS_CONFIG_CARD: DeviceStatus
DEVICE_STATUS_SCAN_FACE: DeviceStatus
DEVICE_STATUS_RESERVED3: DeviceStatus
DEVICE_STATUS_RESERVED4: DeviceStatus
MAX_DEVICE_STATUSES: DeviceStatus

class LEDStatus(_message.Message):
    __slots__ = ("deviceStatus", "count", "signals")
    DEVICESTATUS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    deviceStatus: DeviceStatus
    count: int
    signals: _containers.RepeatedCompositeFieldContainer[_action_pb2.LEDSignal]
    def __init__(self, deviceStatus: _Optional[_Union[DeviceStatus, str]] = ..., count: _Optional[int] = ..., signals: _Optional[_Iterable[_Union[_action_pb2.LEDSignal, _Mapping]]] = ...) -> None: ...

class BuzzerStatus(_message.Message):
    __slots__ = ("deviceStatus", "count", "signals")
    DEVICESTATUS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    deviceStatus: DeviceStatus
    count: int
    signals: _containers.RepeatedCompositeFieldContainer[_action_pb2.BuzzerSignal]
    def __init__(self, deviceStatus: _Optional[_Union[DeviceStatus, str]] = ..., count: _Optional[int] = ..., signals: _Optional[_Iterable[_Union[_action_pb2.BuzzerSignal, _Mapping]]] = ...) -> None: ...

class StatusConfig(_message.Message):
    __slots__ = ("LEDState", "BuzzerState")
    LEDSTATE_FIELD_NUMBER: _ClassVar[int]
    BUZZERSTATE_FIELD_NUMBER: _ClassVar[int]
    LEDState: _containers.RepeatedCompositeFieldContainer[LEDStatus]
    BuzzerState: _containers.RepeatedCompositeFieldContainer[BuzzerStatus]
    def __init__(self, LEDState: _Optional[_Iterable[_Union[LEDStatus, _Mapping]]] = ..., BuzzerState: _Optional[_Iterable[_Union[BuzzerStatus, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: StatusConfig
    def __init__(self, config: _Optional[_Union[StatusConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: StatusConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[StatusConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: StatusConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[StatusConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
