import device_pb2 as _device_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_USE: _ClassVar[Mode]
    MASTER: _ClassVar[Mode]
    SLAVE: _ClassVar[Mode]
    STANDALONE: _ClassVar[Mode]

class IPDOutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARDID: _ClassVar[IPDOutputFormat]
    USERID: _ClassVar[IPDOutputFormat]
NOT_USE: Mode
MASTER: Mode
SLAVE: Mode
STANDALONE: Mode
CARDID: IPDOutputFormat
USERID: IPDOutputFormat

class SlaveDeviceInfo(_message.Message):
    __slots__ = ("deviceID", "type", "enabled", "connected", "channelID")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: _device_pb2.Type
    enabled: bool
    connected: bool
    channelID: int
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.Type, str]] = ..., enabled: bool = ..., connected: bool = ..., channelID: _Optional[int] = ...) -> None: ...

class SearchDeviceRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class SearchDeviceResponse(_message.Message):
    __slots__ = ("slaveInfos",)
    SLAVEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveInfos: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, slaveInfos: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetDeviceRequest(_message.Message):
    __slots__ = ("deviceID", "slaveInfos")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SLAVEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    slaveInfos: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, deviceID: _Optional[int] = ..., slaveInfos: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("slaveInfos",)
    SLAVEINFOS_FIELD_NUMBER: _ClassVar[int]
    slaveInfos: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, slaveInfos: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class IntelligentPDInfo(_message.Message):
    __slots__ = ("useExceptionCode", "exceptionCode", "outputFormat", "OSDPID")
    USEEXCEPTIONCODE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONCODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTFORMAT_FIELD_NUMBER: _ClassVar[int]
    OSDPID_FIELD_NUMBER: _ClassVar[int]
    useExceptionCode: bool
    exceptionCode: bytes
    outputFormat: IPDOutputFormat
    OSDPID: int
    def __init__(self, useExceptionCode: bool = ..., exceptionCode: _Optional[bytes] = ..., outputFormat: _Optional[_Union[IPDOutputFormat, str]] = ..., OSDPID: _Optional[int] = ...) -> None: ...

class RS485Channel(_message.Message):
    __slots__ = ("channelID", "mode", "baudRate", "slaveDevices")
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    BAUDRATE_FIELD_NUMBER: _ClassVar[int]
    SLAVEDEVICES_FIELD_NUMBER: _ClassVar[int]
    channelID: int
    mode: Mode
    baudRate: int
    slaveDevices: _containers.RepeatedCompositeFieldContainer[SlaveDeviceInfo]
    def __init__(self, channelID: _Optional[int] = ..., mode: _Optional[_Union[Mode, str]] = ..., baudRate: _Optional[int] = ..., slaveDevices: _Optional[_Iterable[_Union[SlaveDeviceInfo, _Mapping]]] = ...) -> None: ...

class RS485Config(_message.Message):
    __slots__ = ("channels", "intelligentInfo")
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENTINFO_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[RS485Channel]
    intelligentInfo: IntelligentPDInfo
    def __init__(self, channels: _Optional[_Iterable[_Union[RS485Channel, _Mapping]]] = ..., intelligentInfo: _Optional[_Union[IntelligentPDInfo, _Mapping]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: RS485Config
    def __init__(self, config: _Optional[_Union[RS485Config, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: RS485Config
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[RS485Config, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: RS485Config
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[RS485Config, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
