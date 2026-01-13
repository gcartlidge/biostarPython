import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    DEFAULT_ENROLL_TIMEOUT: _ClassVar[Enum]
    DEFAULT_ENROLL_TIMEOUT_EX: _ClassVar[Enum]
    DEFAULT_MAX_ROTATION: _ClassVar[Enum]
    DEFAULT_MIN_DETECTION_DISTANCE: _ClassVar[Enum]
    DEFAULT_MAX_DETECTION_DISTANCE: _ClassVar[Enum]
    MIN_ENROLL_TIMEOUT: _ClassVar[Enum]
    MAX_ENROLL_TIMEOUT: _ClassVar[Enum]
    MIN_ENROLL_TIMEOUT_EX: _ClassVar[Enum]
    MAX_ENROLL_TIMEOUT_EX: _ClassVar[Enum]
    MIN_MAX_ROTATION: _ClassVar[Enum]
    MAX_MAX_ROTATION: _ClassVar[Enum]
    MIN_MIN_DETECTION_DISTANCE: _ClassVar[Enum]
    MAX_MIN_DETECTION_DISTANCE: _ClassVar[Enum]
    MIN_MAX_DETECTION_DISTANCE: _ClassVar[Enum]
    MAX_MAX_DETECTION_DISTANCE: _ClassVar[Enum]

class FaceFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_FLAG_NONE: _ClassVar[FaceFlag]
    BS2_FACE_FLAG_WARPED: _ClassVar[FaceFlag]
    BS2_FACE_FLAG_TEMPLATE_ONLY: _ClassVar[FaceFlag]
    BS2_FACE_FLAG_EX: _ClassVar[FaceFlag]

class FaceSecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_SECURITY_NORMAL: _ClassVar[FaceSecurityLevel]
    BS2_FACE_SECURITY_SECURE: _ClassVar[FaceSecurityLevel]
    BS2_FACE_SECURITY_MORE_SECURE: _ClassVar[FaceSecurityLevel]
    BS2_FACE_SECURITY_DEFAULT: _ClassVar[FaceSecurityLevel]

class FaceEnrollThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_ENROLL_THRESHOLD_0: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_1: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_2: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_3: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_4: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_5: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_6: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_7: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_8: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_9: _ClassVar[FaceEnrollThreshold]
    BS2_FACE_ENROLL_THRESHOLD_DEFAULT: _ClassVar[FaceEnrollThreshold]

class FaceLightCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_LIGHT_CONDITION_INDOOR: _ClassVar[FaceLightCondition]
    BS2_FACE_LIGHT_CONDITION_OUTDOOR: _ClassVar[FaceLightCondition]
    BS2_FACE_LIGHT_CONDITION_AUTO: _ClassVar[FaceLightCondition]
    BS2_FACE_LIGHT_CONDITION_DARK: _ClassVar[FaceLightCondition]
    BS2_FACE_LIGHT_CONDITION_DEFAULT: _ClassVar[FaceLightCondition]

class FaceDetectSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_DETECT_SENSITIVITY_OFF: _ClassVar[FaceDetectSensitivity]
    BS2_FACE_DETECT_SENSITIVITY_LOW: _ClassVar[FaceDetectSensitivity]
    BS2_FACE_DETECT_SENSITIVITY_MIDDLE: _ClassVar[FaceDetectSensitivity]
    BS2_FACE_DETECT_SENSITIVITY_HIGH: _ClassVar[FaceDetectSensitivity]
    BS2_FACE_DETECT_SENSITIVITY_DEFAULT: _ClassVar[FaceDetectSensitivity]

class FaceLFDLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_LFD_LEVEL_OFF: _ClassVar[FaceLFDLevel]
    BS2_FACE_LFD_LEVEL_LOW: _ClassVar[FaceLFDLevel]
    BS2_FACE_LFD_LEVEL_MIDDLE: _ClassVar[FaceLFDLevel]
    BS2_FACE_LFD_LEVEL_HIGH: _ClassVar[FaceLFDLevel]
    BS2_FACE_LFD_LEVEL_DEFAULT: _ClassVar[FaceLFDLevel]

class FacePreviewOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_PREVIEW_NONE: _ClassVar[FacePreviewOption]
    BS2_FACE_PREVIEW_HALF: _ClassVar[FacePreviewOption]
    BS2_FACE_PREVIEW_FULL: _ClassVar[FacePreviewOption]
    BS2_FACE_PREVIEW_DEFAULT: _ClassVar[FacePreviewOption]

class FaceOperationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_FACE_OPERATION_MODE_FUSION: _ClassVar[FaceOperationMode]
    BS2_FACE_OPERATION_MODE_VISUAL_ONLY: _ClassVar[FaceOperationMode]
    BS2_FACE_OPERATION_MODE_VISUAL_AND_IR_FD_ONLY: _ClassVar[FaceOperationMode]
    BS2_FACE_OPERATION_MODE_DEFAULT: _ClassVar[FaceOperationMode]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_ENROLL_TIMEOUT: Enum
DEFAULT_ENROLL_TIMEOUT_EX: Enum
DEFAULT_MAX_ROTATION: Enum
DEFAULT_MIN_DETECTION_DISTANCE: Enum
DEFAULT_MAX_DETECTION_DISTANCE: Enum
MIN_ENROLL_TIMEOUT: Enum
MAX_ENROLL_TIMEOUT: Enum
MIN_ENROLL_TIMEOUT_EX: Enum
MAX_ENROLL_TIMEOUT_EX: Enum
MIN_MAX_ROTATION: Enum
MAX_MAX_ROTATION: Enum
MIN_MIN_DETECTION_DISTANCE: Enum
MAX_MIN_DETECTION_DISTANCE: Enum
MIN_MAX_DETECTION_DISTANCE: Enum
MAX_MAX_DETECTION_DISTANCE: Enum
BS2_FACE_FLAG_NONE: FaceFlag
BS2_FACE_FLAG_WARPED: FaceFlag
BS2_FACE_FLAG_TEMPLATE_ONLY: FaceFlag
BS2_FACE_FLAG_EX: FaceFlag
BS2_FACE_SECURITY_NORMAL: FaceSecurityLevel
BS2_FACE_SECURITY_SECURE: FaceSecurityLevel
BS2_FACE_SECURITY_MORE_SECURE: FaceSecurityLevel
BS2_FACE_SECURITY_DEFAULT: FaceSecurityLevel
BS2_FACE_ENROLL_THRESHOLD_0: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_1: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_2: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_3: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_4: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_5: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_6: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_7: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_8: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_9: FaceEnrollThreshold
BS2_FACE_ENROLL_THRESHOLD_DEFAULT: FaceEnrollThreshold
BS2_FACE_LIGHT_CONDITION_INDOOR: FaceLightCondition
BS2_FACE_LIGHT_CONDITION_OUTDOOR: FaceLightCondition
BS2_FACE_LIGHT_CONDITION_AUTO: FaceLightCondition
BS2_FACE_LIGHT_CONDITION_DARK: FaceLightCondition
BS2_FACE_LIGHT_CONDITION_DEFAULT: FaceLightCondition
BS2_FACE_DETECT_SENSITIVITY_OFF: FaceDetectSensitivity
BS2_FACE_DETECT_SENSITIVITY_LOW: FaceDetectSensitivity
BS2_FACE_DETECT_SENSITIVITY_MIDDLE: FaceDetectSensitivity
BS2_FACE_DETECT_SENSITIVITY_HIGH: FaceDetectSensitivity
BS2_FACE_DETECT_SENSITIVITY_DEFAULT: FaceDetectSensitivity
BS2_FACE_LFD_LEVEL_OFF: FaceLFDLevel
BS2_FACE_LFD_LEVEL_LOW: FaceLFDLevel
BS2_FACE_LFD_LEVEL_MIDDLE: FaceLFDLevel
BS2_FACE_LFD_LEVEL_HIGH: FaceLFDLevel
BS2_FACE_LFD_LEVEL_DEFAULT: FaceLFDLevel
BS2_FACE_PREVIEW_NONE: FacePreviewOption
BS2_FACE_PREVIEW_HALF: FacePreviewOption
BS2_FACE_PREVIEW_FULL: FacePreviewOption
BS2_FACE_PREVIEW_DEFAULT: FacePreviewOption
BS2_FACE_OPERATION_MODE_FUSION: FaceOperationMode
BS2_FACE_OPERATION_MODE_VISUAL_ONLY: FaceOperationMode
BS2_FACE_OPERATION_MODE_VISUAL_AND_IR_FD_ONLY: FaceOperationMode
BS2_FACE_OPERATION_MODE_DEFAULT: FaceOperationMode

class FaceData(_message.Message):
    __slots__ = ("index", "flag", "templates", "imageData", "irTemplates", "irImageData")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    IMAGEDATA_FIELD_NUMBER: _ClassVar[int]
    IRTEMPLATES_FIELD_NUMBER: _ClassVar[int]
    IRIMAGEDATA_FIELD_NUMBER: _ClassVar[int]
    index: int
    flag: int
    templates: _containers.RepeatedScalarFieldContainer[bytes]
    imageData: bytes
    irTemplates: _containers.RepeatedScalarFieldContainer[bytes]
    irImageData: bytes
    def __init__(self, index: _Optional[int] = ..., flag: _Optional[int] = ..., templates: _Optional[_Iterable[bytes]] = ..., imageData: _Optional[bytes] = ..., irTemplates: _Optional[_Iterable[bytes]] = ..., irImageData: _Optional[bytes] = ...) -> None: ...

class ScanRequest(_message.Message):
    __slots__ = ("deviceID", "enrollThreshold")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ENROLLTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    enrollThreshold: FaceEnrollThreshold
    def __init__(self, deviceID: _Optional[int] = ..., enrollThreshold: _Optional[_Union[FaceEnrollThreshold, str]] = ...) -> None: ...

class ScanResponse(_message.Message):
    __slots__ = ("faceData",)
    FACEDATA_FIELD_NUMBER: _ClassVar[int]
    faceData: FaceData
    def __init__(self, faceData: _Optional[_Union[FaceData, _Mapping]] = ...) -> None: ...

class ExtractRequest(_message.Message):
    __slots__ = ("deviceID", "imageData", "isWarped")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    IMAGEDATA_FIELD_NUMBER: _ClassVar[int]
    ISWARPED_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    imageData: bytes
    isWarped: bool
    def __init__(self, deviceID: _Optional[int] = ..., imageData: _Optional[bytes] = ..., isWarped: bool = ...) -> None: ...

class ExtractResponse(_message.Message):
    __slots__ = ("templateData",)
    TEMPLATEDATA_FIELD_NUMBER: _ClassVar[int]
    templateData: bytes
    def __init__(self, templateData: _Optional[bytes] = ...) -> None: ...

class NormalizeRequest(_message.Message):
    __slots__ = ("deviceID", "unwrappedImageData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    UNWRAPPEDIMAGEDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    unwrappedImageData: bytes
    def __init__(self, deviceID: _Optional[int] = ..., unwrappedImageData: _Optional[bytes] = ...) -> None: ...

class NormalizeResponse(_message.Message):
    __slots__ = ("wrappedImageData",)
    WRAPPEDIMAGEDATA_FIELD_NUMBER: _ClassVar[int]
    wrappedImageData: bytes
    def __init__(self, wrappedImageData: _Optional[bytes] = ...) -> None: ...

class AuthGroup(_message.Message):
    __slots__ = ("ID", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetAuthGroupRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetAuthGroupResponse(_message.Message):
    __slots__ = ("authGroups",)
    AUTHGROUPS_FIELD_NUMBER: _ClassVar[int]
    authGroups: _containers.RepeatedCompositeFieldContainer[AuthGroup]
    def __init__(self, authGroups: _Optional[_Iterable[_Union[AuthGroup, _Mapping]]] = ...) -> None: ...

class AddAuthGroupRequest(_message.Message):
    __slots__ = ("deviceID", "authGroups")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    AUTHGROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    authGroups: _containers.RepeatedCompositeFieldContainer[AuthGroup]
    def __init__(self, deviceID: _Optional[int] = ..., authGroups: _Optional[_Iterable[_Union[AuthGroup, _Mapping]]] = ...) -> None: ...

class AddAuthGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddAuthGroupMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "authGroups")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    AUTHGROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    authGroups: _containers.RepeatedCompositeFieldContainer[AuthGroup]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., authGroups: _Optional[_Iterable[_Union[AuthGroup, _Mapping]]] = ...) -> None: ...

class AddAuthGroupMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAuthGroupRequest(_message.Message):
    __slots__ = ("deviceID", "groupIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAuthGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAuthGroupMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "groupIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAuthGroupMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllAuthGroupRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllAuthGroupResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllAuthGroupMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllAuthGroupMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class FaceConfig(_message.Message):
    __slots__ = ("securityLevel", "lightCondition", "enrollThreshold", "detectSensitivity", "enrollTimeout", "LFDLevel", "quickEnrollment", "previewOption", "checkDuplicate", "operationMode", "maxRotation", "faceWidthMin", "faceWidthMax", "searchRangeX", "searchRangeWidth", "detectDistanceMin", "detectDistanceMax", "wideSearch", "unableToSaveImageOfVisualFace")
    SECURITYLEVEL_FIELD_NUMBER: _ClassVar[int]
    LIGHTCONDITION_FIELD_NUMBER: _ClassVar[int]
    ENROLLTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DETECTSENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ENROLLTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LFDLEVEL_FIELD_NUMBER: _ClassVar[int]
    QUICKENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    PREVIEWOPTION_FIELD_NUMBER: _ClassVar[int]
    CHECKDUPLICATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONMODE_FIELD_NUMBER: _ClassVar[int]
    MAXROTATION_FIELD_NUMBER: _ClassVar[int]
    FACEWIDTHMIN_FIELD_NUMBER: _ClassVar[int]
    FACEWIDTHMAX_FIELD_NUMBER: _ClassVar[int]
    SEARCHRANGEX_FIELD_NUMBER: _ClassVar[int]
    SEARCHRANGEWIDTH_FIELD_NUMBER: _ClassVar[int]
    DETECTDISTANCEMIN_FIELD_NUMBER: _ClassVar[int]
    DETECTDISTANCEMAX_FIELD_NUMBER: _ClassVar[int]
    WIDESEARCH_FIELD_NUMBER: _ClassVar[int]
    UNABLETOSAVEIMAGEOFVISUALFACE_FIELD_NUMBER: _ClassVar[int]
    securityLevel: FaceSecurityLevel
    lightCondition: FaceLightCondition
    enrollThreshold: FaceEnrollThreshold
    detectSensitivity: FaceDetectSensitivity
    enrollTimeout: int
    LFDLevel: FaceLFDLevel
    quickEnrollment: bool
    previewOption: FacePreviewOption
    checkDuplicate: bool
    operationMode: FaceOperationMode
    maxRotation: int
    faceWidthMin: int
    faceWidthMax: int
    searchRangeX: int
    searchRangeWidth: int
    detectDistanceMin: int
    detectDistanceMax: int
    wideSearch: bool
    unableToSaveImageOfVisualFace: bool
    def __init__(self, securityLevel: _Optional[_Union[FaceSecurityLevel, str]] = ..., lightCondition: _Optional[_Union[FaceLightCondition, str]] = ..., enrollThreshold: _Optional[_Union[FaceEnrollThreshold, str]] = ..., detectSensitivity: _Optional[_Union[FaceDetectSensitivity, str]] = ..., enrollTimeout: _Optional[int] = ..., LFDLevel: _Optional[_Union[FaceLFDLevel, str]] = ..., quickEnrollment: bool = ..., previewOption: _Optional[_Union[FacePreviewOption, str]] = ..., checkDuplicate: bool = ..., operationMode: _Optional[_Union[FaceOperationMode, str]] = ..., maxRotation: _Optional[int] = ..., faceWidthMin: _Optional[int] = ..., faceWidthMax: _Optional[int] = ..., searchRangeX: _Optional[int] = ..., searchRangeWidth: _Optional[int] = ..., detectDistanceMin: _Optional[int] = ..., detectDistanceMax: _Optional[int] = ..., wideSearch: bool = ..., unableToSaveImageOfVisualFace: bool = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: FaceConfig
    def __init__(self, config: _Optional[_Union[FaceConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: FaceConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[FaceConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: FaceConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[FaceConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
