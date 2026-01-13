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
    DEFAULT_SCAN_TIMEOUT: _ClassVar[Enum]
    MIN_SCAN_TIMEOUT: _ClassVar[Enum]
    MAX_SCAN_TIMEOUT: _ClassVar[Enum]

class TemplateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPLATE_FORMAT_SUPREMA: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_ISO: _ClassVar[TemplateFormat]
    TEMPLATE_FORMAT_ANSI: _ClassVar[TemplateFormat]

class FingerFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FINGER_FLAG_NONE: _ClassVar[FingerFlag]
    BS2_FINGER_FLAG_DURESS: _ClassVar[FingerFlag]

class SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURE: _ClassVar[SecurityLevel]
    MORE_SECURE: _ClassVar[SecurityLevel]
    MOST_SECURE: _ClassVar[SecurityLevel]
    DEFAULT_SECURITY: _ClassVar[SecurityLevel]

class FastMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTOMATIC: _ClassVar[FastMode]
    FAST: _ClassVar[FastMode]
    FASTER: _ClassVar[FastMode]
    FASTEST: _ClassVar[FastMode]
    DEFAULT_FAST: _ClassVar[FastMode]

class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOWEST_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL0_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL1_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL2_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL3_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL4_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL5_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL6_SENSITIVE: _ClassVar[Sensitivity]
    LEVEL7_SENSITIVE: _ClassVar[Sensitivity]
    HIGHEST_SENSITIVE: _ClassVar[Sensitivity]
    DEFAULT_SENSITITY: _ClassVar[Sensitivity]

class SensorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALWAYS_ON: _ClassVar[SensorMode]
    ACTIVATED_BY_PROXIMITY: _ClassVar[SensorMode]
    DEFAULT_SENSOR_MODE: _ClassVar[SensorMode]

class LFDLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_USED: _ClassVar[LFDLevel]
    STRICT: _ClassVar[LFDLevel]
    MORE_STRICT: _ClassVar[LFDLevel]
    MOST_STRICT: _ClassVar[LFDLevel]
    DEFAULT_LFD: _ClassVar[LFDLevel]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_SCAN_TIMEOUT: Enum
MIN_SCAN_TIMEOUT: Enum
MAX_SCAN_TIMEOUT: Enum
TEMPLATE_FORMAT_SUPREMA: TemplateFormat
TEMPLATE_FORMAT_ISO: TemplateFormat
TEMPLATE_FORMAT_ANSI: TemplateFormat
BS2_FINGER_FLAG_NONE: FingerFlag
BS2_FINGER_FLAG_DURESS: FingerFlag
SECURE: SecurityLevel
MORE_SECURE: SecurityLevel
MOST_SECURE: SecurityLevel
DEFAULT_SECURITY: SecurityLevel
AUTOMATIC: FastMode
FAST: FastMode
FASTER: FastMode
FASTEST: FastMode
DEFAULT_FAST: FastMode
LOWEST_SENSITIVE: Sensitivity
LEVEL0_SENSITIVE: Sensitivity
LEVEL1_SENSITIVE: Sensitivity
LEVEL2_SENSITIVE: Sensitivity
LEVEL3_SENSITIVE: Sensitivity
LEVEL4_SENSITIVE: Sensitivity
LEVEL5_SENSITIVE: Sensitivity
LEVEL6_SENSITIVE: Sensitivity
LEVEL7_SENSITIVE: Sensitivity
HIGHEST_SENSITIVE: Sensitivity
DEFAULT_SENSITITY: Sensitivity
ALWAYS_ON: SensorMode
ACTIVATED_BY_PROXIMITY: SensorMode
DEFAULT_SENSOR_MODE: SensorMode
NOT_USED: LFDLevel
STRICT: LFDLevel
MORE_STRICT: LFDLevel
MOST_STRICT: LFDLevel
DEFAULT_LFD: LFDLevel

class FingerData(_message.Message):
    __slots__ = ("index", "flag", "templates")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    index: int
    flag: int
    templates: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, index: _Optional[int] = ..., flag: _Optional[int] = ..., templates: _Optional[_Iterable[bytes]] = ...) -> None: ...

class ScanRequest(_message.Message):
    __slots__ = ("deviceID", "templateFormat", "qualityThreshold")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEFORMAT_FIELD_NUMBER: _ClassVar[int]
    QUALITYTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    templateFormat: TemplateFormat
    qualityThreshold: int
    def __init__(self, deviceID: _Optional[int] = ..., templateFormat: _Optional[_Union[TemplateFormat, str]] = ..., qualityThreshold: _Optional[int] = ...) -> None: ...

class ScanResponse(_message.Message):
    __slots__ = ("templateData", "qualityScore")
    TEMPLATEDATA_FIELD_NUMBER: _ClassVar[int]
    QUALITYSCORE_FIELD_NUMBER: _ClassVar[int]
    templateData: bytes
    qualityScore: int
    def __init__(self, templateData: _Optional[bytes] = ..., qualityScore: _Optional[int] = ...) -> None: ...

class GetImageRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetImageResponse(_message.Message):
    __slots__ = ("BMPImage",)
    BMPIMAGE_FIELD_NUMBER: _ClassVar[int]
    BMPImage: bytes
    def __init__(self, BMPImage: _Optional[bytes] = ...) -> None: ...

class VerifyRequest(_message.Message):
    __slots__ = ("deviceID", "fingerData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    FINGERDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    fingerData: FingerData
    def __init__(self, deviceID: _Optional[int] = ..., fingerData: _Optional[_Union[FingerData, _Mapping]] = ...) -> None: ...

class VerifyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: FingerConfig
    def __init__(self, config: _Optional[_Union[FingerConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: FingerConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[FingerConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: FingerConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[FingerConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class FingerConfig(_message.Message):
    __slots__ = ("securityLevel", "fastMode", "sensitivity", "sensorMode", "templateFormat", "scanTimeout", "advancedEnrollment", "showImage", "LFDLevel", "checkDuplicate")
    SECURITYLEVEL_FIELD_NUMBER: _ClassVar[int]
    FASTMODE_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    SENSORMODE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATEFORMAT_FIELD_NUMBER: _ClassVar[int]
    SCANTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ADVANCEDENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    SHOWIMAGE_FIELD_NUMBER: _ClassVar[int]
    LFDLEVEL_FIELD_NUMBER: _ClassVar[int]
    CHECKDUPLICATE_FIELD_NUMBER: _ClassVar[int]
    securityLevel: SecurityLevel
    fastMode: FastMode
    sensitivity: Sensitivity
    sensorMode: SensorMode
    templateFormat: TemplateFormat
    scanTimeout: int
    advancedEnrollment: bool
    showImage: bool
    LFDLevel: LFDLevel
    checkDuplicate: bool
    def __init__(self, securityLevel: _Optional[_Union[SecurityLevel, str]] = ..., fastMode: _Optional[_Union[FastMode, str]] = ..., sensitivity: _Optional[_Union[Sensitivity, str]] = ..., sensorMode: _Optional[_Union[SensorMode, str]] = ..., templateFormat: _Optional[_Union[TemplateFormat, str]] = ..., scanTimeout: _Optional[int] = ..., advancedEnrollment: bool = ..., showImage: bool = ..., LFDLevel: _Optional[_Union[LFDLevel, str]] = ..., checkDuplicate: bool = ...) -> None: ...
