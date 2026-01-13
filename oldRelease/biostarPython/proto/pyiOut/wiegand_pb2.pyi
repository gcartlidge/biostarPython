import device_pb2 as _device_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    DEFAULT_OUT_PULSE_WIDTH: _ClassVar[Enum]
    DEFAULT_OUT_PULSE_INTERVAL: _ClassVar[Enum]
    MIN_OUT_PULSE_WIDTH: _ClassVar[Enum]
    MAX_OUT_PULSE_WIDTH: _ClassVar[Enum]
    MIN_OUT_PULSE_INTERVAL: _ClassVar[Enum]
    MAX_OUT_PULSE_INTERVAL: _ClassVar[Enum]
    MAX_ID_FIELDS: _ClassVar[Enum]
    MAX_PARITY_FIELDS: _ClassVar[Enum]
    MAX_WIEGAND_FIELD_BITS: _ClassVar[Enum]
    MAX_WIEGAND_FIELD_BYTES: _ClassVar[Enum]
    MAX_WIEGAND_FORMATS: _ClassVar[Enum]

class WiegandMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIEGAND_IN_ONLY: _ClassVar[WiegandMode]
    WIEGAND_OUT_ONLY: _ClassVar[WiegandMode]
    WIEGAND_IN_OUT: _ClassVar[WiegandMode]

class WiegandParity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIEGAND_PARITY_NONE: _ClassVar[WiegandParity]
    WIEGAND_PARITY_ODD: _ClassVar[WiegandParity]
    WIEGAND_PARITY_EVEN: _ClassVar[WiegandParity]

class WiegandOutType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIEGAND_OUT_UNSPECIFIED: _ClassVar[WiegandOutType]
    WIEGAND_OUT_CARD_ID: _ClassVar[WiegandOutType]
    WIEGAND_OUT_USER_ID: _ClassVar[WiegandOutType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_OUT_PULSE_WIDTH: Enum
DEFAULT_OUT_PULSE_INTERVAL: Enum
MIN_OUT_PULSE_WIDTH: Enum
MAX_OUT_PULSE_WIDTH: Enum
MIN_OUT_PULSE_INTERVAL: Enum
MAX_OUT_PULSE_INTERVAL: Enum
MAX_ID_FIELDS: Enum
MAX_PARITY_FIELDS: Enum
MAX_WIEGAND_FIELD_BITS: Enum
MAX_WIEGAND_FIELD_BYTES: Enum
MAX_WIEGAND_FORMATS: Enum
WIEGAND_IN_ONLY: WiegandMode
WIEGAND_OUT_ONLY: WiegandMode
WIEGAND_IN_OUT: WiegandMode
WIEGAND_PARITY_NONE: WiegandParity
WIEGAND_PARITY_ODD: WiegandParity
WIEGAND_PARITY_EVEN: WiegandParity
WIEGAND_OUT_UNSPECIFIED: WiegandOutType
WIEGAND_OUT_CARD_ID: WiegandOutType
WIEGAND_OUT_USER_ID: WiegandOutType

class ParityField(_message.Message):
    __slots__ = ("parityPos", "parityType", "data")
    PARITYPOS_FIELD_NUMBER: _ClassVar[int]
    PARITYTYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    parityPos: int
    parityType: WiegandParity
    data: bytes
    def __init__(self, parityPos: _Optional[int] = ..., parityType: _Optional[_Union[WiegandParity, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class WiegandFormat(_message.Message):
    __slots__ = ("formatID", "length", "IDFields", "parityFields")
    FORMATID_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    IDFIELDS_FIELD_NUMBER: _ClassVar[int]
    PARITYFIELDS_FIELD_NUMBER: _ClassVar[int]
    formatID: int
    length: int
    IDFields: _containers.RepeatedScalarFieldContainer[bytes]
    parityFields: _containers.RepeatedCompositeFieldContainer[ParityField]
    def __init__(self, formatID: _Optional[int] = ..., length: _Optional[int] = ..., IDFields: _Optional[_Iterable[bytes]] = ..., parityFields: _Optional[_Iterable[_Union[ParityField, _Mapping]]] = ...) -> None: ...

class WiegandConfig(_message.Message):
    __slots__ = ("mode", "useWiegandBypass", "useFailCode", "failCode", "outPulseWidth", "outPulseInterval", "formats", "slaveFormats", "CSNFormat", "useWiegandUserID")
    MODE_FIELD_NUMBER: _ClassVar[int]
    USEWIEGANDBYPASS_FIELD_NUMBER: _ClassVar[int]
    USEFAILCODE_FIELD_NUMBER: _ClassVar[int]
    FAILCODE_FIELD_NUMBER: _ClassVar[int]
    OUTPULSEWIDTH_FIELD_NUMBER: _ClassVar[int]
    OUTPULSEINTERVAL_FIELD_NUMBER: _ClassVar[int]
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    SLAVEFORMATS_FIELD_NUMBER: _ClassVar[int]
    CSNFORMAT_FIELD_NUMBER: _ClassVar[int]
    USEWIEGANDUSERID_FIELD_NUMBER: _ClassVar[int]
    mode: WiegandMode
    useWiegandBypass: bool
    useFailCode: bool
    failCode: int
    outPulseWidth: int
    outPulseInterval: int
    formats: _containers.RepeatedCompositeFieldContainer[WiegandFormat]
    slaveFormats: _containers.RepeatedCompositeFieldContainer[WiegandFormat]
    CSNFormat: WiegandFormat
    useWiegandUserID: WiegandOutType
    def __init__(self, mode: _Optional[_Union[WiegandMode, str]] = ..., useWiegandBypass: bool = ..., useFailCode: bool = ..., failCode: _Optional[int] = ..., outPulseWidth: _Optional[int] = ..., outPulseInterval: _Optional[int] = ..., formats: _Optional[_Iterable[_Union[WiegandFormat, _Mapping]]] = ..., slaveFormats: _Optional[_Iterable[_Union[WiegandFormat, _Mapping]]] = ..., CSNFormat: _Optional[_Union[WiegandFormat, _Mapping]] = ..., useWiegandUserID: _Optional[_Union[WiegandOutType, str]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: WiegandConfig
    def __init__(self, config: _Optional[_Union[WiegandConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: WiegandConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[WiegandConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: WiegandConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[WiegandConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class WiegandTamperInput(_message.Message):
    __slots__ = ("deviceID", "port", "switchType")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SWITCHTYPE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    switchType: _device_pb2.SwitchType
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., switchType: _Optional[_Union[_device_pb2.SwitchType, str]] = ...) -> None: ...

class WiegandOutput(_message.Message):
    __slots__ = ("deviceID", "port")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ...) -> None: ...

class WiegandDeviceInfo(_message.Message):
    __slots__ = ("deviceID", "tamperInput", "redLEDOutput", "greenLEDOutput", "buzzerOutput")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TAMPERINPUT_FIELD_NUMBER: _ClassVar[int]
    REDLEDOUTPUT_FIELD_NUMBER: _ClassVar[int]
    GREENLEDOUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUZZEROUTPUT_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    tamperInput: WiegandTamperInput
    redLEDOutput: WiegandOutput
    greenLEDOutput: WiegandOutput
    buzzerOutput: WiegandOutput
    def __init__(self, deviceID: _Optional[int] = ..., tamperInput: _Optional[_Union[WiegandTamperInput, _Mapping]] = ..., redLEDOutput: _Optional[_Union[WiegandOutput, _Mapping]] = ..., greenLEDOutput: _Optional[_Union[WiegandOutput, _Mapping]] = ..., buzzerOutput: _Optional[_Union[WiegandOutput, _Mapping]] = ...) -> None: ...

class SearchDeviceRequest(_message.Message):
    __slots__ = ("parentDeviceID",)
    PARENTDEVICEID_FIELD_NUMBER: _ClassVar[int]
    parentDeviceID: int
    def __init__(self, parentDeviceID: _Optional[int] = ...) -> None: ...

class SearchDeviceResponse(_message.Message):
    __slots__ = ("wiegandDeviceIDs",)
    WIEGANDDEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    wiegandDeviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, wiegandDeviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class SetDeviceRequest(_message.Message):
    __slots__ = ("parentDeviceID", "deviceInfos")
    PARENTDEVICEID_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    parentDeviceID: int
    deviceInfos: _containers.RepeatedCompositeFieldContainer[WiegandDeviceInfo]
    def __init__(self, parentDeviceID: _Optional[int] = ..., deviceInfos: _Optional[_Iterable[_Union[WiegandDeviceInfo, _Mapping]]] = ...) -> None: ...

class SetDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("parentDeviceID",)
    PARENTDEVICEID_FIELD_NUMBER: _ClassVar[int]
    parentDeviceID: int
    def __init__(self, parentDeviceID: _Optional[int] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("deviceInfos",)
    DEVICEINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceInfos: _containers.RepeatedCompositeFieldContainer[WiegandDeviceInfo]
    def __init__(self, deviceInfos: _Optional[_Iterable[_Union[WiegandDeviceInfo, _Mapping]]] = ...) -> None: ...
