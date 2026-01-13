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
    DEFAULT_HIGH_TEMPERATURE_THRESHOLD: _ClassVar[Enum]
    DEFAULT_LOW_TEMPERATURE_THRESHOLD: _ClassVar[Enum]
    DEFAULT_DISTANCE: _ClassVar[Enum]
    DEFAULT_EMISSIVITY: _ClassVar[Enum]
    DEFAULT_ROI_X: _ClassVar[Enum]
    DEFAULT_ROI_Y: _ClassVar[Enum]
    DEFAULT_ROI_WIDTH: _ClassVar[Enum]
    DEFAULT_ROI_HEIGHT: _ClassVar[Enum]
    MIN_TEMPERATURE_THRESHOLD: _ClassVar[Enum]
    MAX_EMPERATURE_THRESHOLD: _ClassVar[Enum]
    MIN_DISTANCE: _ClassVar[Enum]
    MAX_DISTANCE: _ClassVar[Enum]
    MIN_EMISSIVITY: _ClassVar[Enum]
    MAX_EMISSIVITY: _ClassVar[Enum]
    MIN_ROI_X: _ClassVar[Enum]
    MAX_ROI_X: _ClassVar[Enum]
    MIN_ROI_Y: _ClassVar[Enum]
    MAX_ROI_Y: _ClassVar[Enum]
    MIN_ROI_WIDTH: _ClassVar[Enum]
    MAX_ROI_WIDTH: _ClassVar[Enum]
    MIN_ROI_HEIGHT: _ClassVar[Enum]
    MAX_ROI_HEIGHT: _ClassVar[Enum]
    MIN_COMPENSATION_TEMPERATURE: _ClassVar[Enum]
    MAX_COMPENSATION_TEMPERATURE: _ClassVar[Enum]

class CheckMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFF: _ClassVar[CheckMode]
    HARD: _ClassVar[CheckMode]
    SOFT: _ClassVar[CheckMode]

class CheckOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AFTER_AUTH: _ClassVar[CheckOrder]
    BEFORE_AUTH: _ClassVar[CheckOrder]
    WITHOUT_AUTH: _ClassVar[CheckOrder]

class TemperatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAHRENHEIT: _ClassVar[TemperatureFormat]
    CELSIUS: _ClassVar[TemperatureFormat]

class MaskDetectionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_USE: _ClassVar[MaskDetectionLevel]
    NORMAL: _ClassVar[MaskDetectionLevel]
    HIGH: _ClassVar[MaskDetectionLevel]
    VERY_HIGH: _ClassVar[MaskDetectionLevel]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_HIGH_TEMPERATURE_THRESHOLD: Enum
DEFAULT_LOW_TEMPERATURE_THRESHOLD: Enum
DEFAULT_DISTANCE: Enum
DEFAULT_EMISSIVITY: Enum
DEFAULT_ROI_X: Enum
DEFAULT_ROI_Y: Enum
DEFAULT_ROI_WIDTH: Enum
DEFAULT_ROI_HEIGHT: Enum
MIN_TEMPERATURE_THRESHOLD: Enum
MAX_EMPERATURE_THRESHOLD: Enum
MIN_DISTANCE: Enum
MAX_DISTANCE: Enum
MIN_EMISSIVITY: Enum
MAX_EMISSIVITY: Enum
MIN_ROI_X: Enum
MAX_ROI_X: Enum
MIN_ROI_Y: Enum
MAX_ROI_Y: Enum
MIN_ROI_WIDTH: Enum
MAX_ROI_WIDTH: Enum
MIN_ROI_HEIGHT: Enum
MAX_ROI_HEIGHT: Enum
MIN_COMPENSATION_TEMPERATURE: Enum
MAX_COMPENSATION_TEMPERATURE: Enum
OFF: CheckMode
HARD: CheckMode
SOFT: CheckMode
AFTER_AUTH: CheckOrder
BEFORE_AUTH: CheckOrder
WITHOUT_AUTH: CheckOrder
FAHRENHEIT: TemperatureFormat
CELSIUS: TemperatureFormat
NOT_USE: MaskDetectionLevel
NORMAL: MaskDetectionLevel
HIGH: MaskDetectionLevel
VERY_HIGH: MaskDetectionLevel

class ThermalCameraROI(_message.Message):
    __slots__ = ("x", "y", "width", "height")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    width: int
    height: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class ThermalCamera(_message.Message):
    __slots__ = ("distance", "emissionRate", "ROI", "useBodyCompensation", "compensationTemperature")
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    EMISSIONRATE_FIELD_NUMBER: _ClassVar[int]
    ROI_FIELD_NUMBER: _ClassVar[int]
    USEBODYCOMPENSATION_FIELD_NUMBER: _ClassVar[int]
    COMPENSATIONTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    distance: int
    emissionRate: int
    ROI: ThermalCameraROI
    useBodyCompensation: bool
    compensationTemperature: int
    def __init__(self, distance: _Optional[int] = ..., emissionRate: _Optional[int] = ..., ROI: _Optional[_Union[ThermalCameraROI, _Mapping]] = ..., useBodyCompensation: bool = ..., compensationTemperature: _Optional[int] = ...) -> None: ...

class ThermalConfig(_message.Message):
    __slots__ = ("checkMode", "checkOrder", "temperatureFormat", "temperatureThresholdHigh", "auditTemperature", "useRejectSound", "useOverlapThermal", "camera", "maskCheckMode", "maskDetectionLevel", "useDynamicROI", "temperatureThresholdLow")
    CHECKMODE_FIELD_NUMBER: _ClassVar[int]
    CHECKORDER_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREFORMAT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURETHRESHOLDHIGH_FIELD_NUMBER: _ClassVar[int]
    AUDITTEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    USEREJECTSOUND_FIELD_NUMBER: _ClassVar[int]
    USEOVERLAPTHERMAL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    MASKCHECKMODE_FIELD_NUMBER: _ClassVar[int]
    MASKDETECTIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    USEDYNAMICROI_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURETHRESHOLDLOW_FIELD_NUMBER: _ClassVar[int]
    checkMode: CheckMode
    checkOrder: CheckOrder
    temperatureFormat: TemperatureFormat
    temperatureThresholdHigh: int
    auditTemperature: bool
    useRejectSound: bool
    useOverlapThermal: bool
    camera: ThermalCamera
    maskCheckMode: CheckMode
    maskDetectionLevel: MaskDetectionLevel
    useDynamicROI: bool
    temperatureThresholdLow: int
    def __init__(self, checkMode: _Optional[_Union[CheckMode, str]] = ..., checkOrder: _Optional[_Union[CheckOrder, str]] = ..., temperatureFormat: _Optional[_Union[TemperatureFormat, str]] = ..., temperatureThresholdHigh: _Optional[int] = ..., auditTemperature: bool = ..., useRejectSound: bool = ..., useOverlapThermal: bool = ..., camera: _Optional[_Union[ThermalCamera, _Mapping]] = ..., maskCheckMode: _Optional[_Union[CheckMode, str]] = ..., maskDetectionLevel: _Optional[_Union[MaskDetectionLevel, str]] = ..., useDynamicROI: bool = ..., temperatureThresholdLow: _Optional[int] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: ThermalConfig
    def __init__(self, config: _Optional[_Union[ThermalConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: ThermalConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[ThermalConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: ThermalConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[ThermalConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class TemperatureLog(_message.Message):
    __slots__ = ("ID", "timestamp", "deviceID", "userID", "eventCode", "subCode", "temperature")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SUBCODE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    ID: int
    timestamp: int
    deviceID: int
    userID: str
    eventCode: int
    subCode: int
    temperature: int
    def __init__(self, ID: _Optional[int] = ..., timestamp: _Optional[int] = ..., deviceID: _Optional[int] = ..., userID: _Optional[str] = ..., eventCode: _Optional[int] = ..., subCode: _Optional[int] = ..., temperature: _Optional[int] = ...) -> None: ...

class GetTemperatureLogRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ...) -> None: ...

class GetTemperatureLogResponse(_message.Message):
    __slots__ = ("temperatureEvents",)
    TEMPERATUREEVENTS_FIELD_NUMBER: _ClassVar[int]
    temperatureEvents: _containers.RepeatedCompositeFieldContainer[TemperatureLog]
    def __init__(self, temperatureEvents: _Optional[_Iterable[_Union[TemperatureLog, _Mapping]]] = ...) -> None: ...
