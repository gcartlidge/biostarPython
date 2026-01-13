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
    DEFAULT_MATCH_TIMEOUT: _ClassVar[Enum]
    DEFAULT_AUTH_TIMEOUT: _ClassVar[Enum]
    DEFAULT_AUTH_TIMEOUT_FOR_FACE: _ClassVar[Enum]
    MIN_MATCH_TIMEOUT: _ClassVar[Enum]
    MAX_MATCH_TIMEOUT: _ClassVar[Enum]
    MIN_AUTH_TIMEOUT: _ClassVar[Enum]
    MAX_AUTH_TIMEOUT: _ClassVar[Enum]

class AuthMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_MODE_BIOMETRIC_ONLY: _ClassVar[AuthMode]
    AUTH_MODE_BIOMETRIC_PIN: _ClassVar[AuthMode]
    AUTH_MODE_CARD_ONLY: _ClassVar[AuthMode]
    AUTH_MODE_CARD_BIOMETRIC: _ClassVar[AuthMode]
    AUTH_MODE_CARD_PIN: _ClassVar[AuthMode]
    AUTH_MODE_CARD_BIOMETRIC_OR_PIN: _ClassVar[AuthMode]
    AUTH_MODE_CARD_BIOMETRIC_PIN: _ClassVar[AuthMode]
    AUTH_MODE_ID_BIOMETRIC: _ClassVar[AuthMode]
    AUTH_MODE_ID_PIN: _ClassVar[AuthMode]
    AUTH_MODE_ID_BIOMETRIC_OR_PIN: _ClassVar[AuthMode]
    AUTH_MODE_ID_BIOMETRIC_PIN: _ClassVar[AuthMode]
    AUTH_MODE_NONE: _ClassVar[AuthMode]
    AUTH_MODE_PROHIBITED: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FACE_ONLY: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FACE_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FACE_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FACE_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FINGERPRINT_ONLY: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FINGERPRINT_FACE: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_FINGERPRINT_FACE_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_ONLY: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FINGERPRINT_FACE: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_FINGERPRINT: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FINGERPRINT_FACE: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN: _ClassVar[AuthMode]
    AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN: _ClassVar[AuthMode]

class OperatorLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATOR_LEVEL_NONE: _ClassVar[OperatorLevel]
    OPERATOR_LEVEL_ADMIN: _ClassVar[OperatorLevel]
    OPERATOR_LEVEL_CONFIG: _ClassVar[OperatorLevel]
    OPERATOR_LEVEL_USER: _ClassVar[OperatorLevel]

class FaceDetectionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FACE_DETECTION_NONE: _ClassVar[FaceDetectionLevel]
    FACE_DETECTION_NORMAL: _ClassVar[FaceDetectionLevel]
    FACE_DETECTION_STRICT: _ClassVar[FaceDetectionLevel]

class GlobalAPBFailActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GLOBAL_APB_FAIL_ACTION_NONE: _ClassVar[GlobalAPBFailActionType]
    GLOBAL_APB_FAIL_ACTION_SOFT: _ClassVar[GlobalAPBFailActionType]
    GLOBAL_APB_FAIL_ACTION_HARD: _ClassVar[GlobalAPBFailActionType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_MATCH_TIMEOUT: Enum
DEFAULT_AUTH_TIMEOUT: Enum
DEFAULT_AUTH_TIMEOUT_FOR_FACE: Enum
MIN_MATCH_TIMEOUT: Enum
MAX_MATCH_TIMEOUT: Enum
MIN_AUTH_TIMEOUT: Enum
MAX_AUTH_TIMEOUT: Enum
AUTH_MODE_BIOMETRIC_ONLY: AuthMode
AUTH_MODE_BIOMETRIC_PIN: AuthMode
AUTH_MODE_CARD_ONLY: AuthMode
AUTH_MODE_CARD_BIOMETRIC: AuthMode
AUTH_MODE_CARD_PIN: AuthMode
AUTH_MODE_CARD_BIOMETRIC_OR_PIN: AuthMode
AUTH_MODE_CARD_BIOMETRIC_PIN: AuthMode
AUTH_MODE_ID_BIOMETRIC: AuthMode
AUTH_MODE_ID_PIN: AuthMode
AUTH_MODE_ID_BIOMETRIC_OR_PIN: AuthMode
AUTH_MODE_ID_BIOMETRIC_PIN: AuthMode
AUTH_MODE_NONE: AuthMode
AUTH_MODE_PROHIBITED: AuthMode
AUTH_EXT_MODE_FACE_ONLY: AuthMode
AUTH_EXT_MODE_FACE_FINGERPRINT: AuthMode
AUTH_EXT_MODE_FACE_PIN: AuthMode
AUTH_EXT_MODE_FACE_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_FACE_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_FINGERPRINT_ONLY: AuthMode
AUTH_EXT_MODE_FINGERPRINT_FACE: AuthMode
AUTH_EXT_MODE_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_FINGERPRINT_FACE_OR_PIN: AuthMode
AUTH_EXT_MODE_FINGERPRINT_FACE_PIN: AuthMode
AUTH_EXT_MODE_CARD_ONLY: AuthMode
AUTH_EXT_MODE_CARD_FACE: AuthMode
AUTH_EXT_MODE_CARD_FINGERPRINT: AuthMode
AUTH_EXT_MODE_CARD_PIN: AuthMode
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT: AuthMode
AUTH_EXT_MODE_CARD_FACE_OR_PIN: AuthMode
AUTH_EXT_MODE_CARD_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_CARD_FACE_FINGERPRINT: AuthMode
AUTH_EXT_MODE_CARD_FACE_PIN: AuthMode
AUTH_EXT_MODE_CARD_FINGERPRINT_FACE: AuthMode
AUTH_EXT_MODE_CARD_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_CARD_FACE_OR_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_CARD_FACE_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_CARD_FINGERPRINT_FACE_OR_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE: AuthMode
AUTH_EXT_MODE_ID_FINGERPRINT: AuthMode
AUTH_EXT_MODE_ID_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT: AuthMode
AUTH_EXT_MODE_ID_FACE_OR_PIN: AuthMode
AUTH_EXT_MODE_ID_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE_FINGERPRINT: AuthMode
AUTH_EXT_MODE_ID_FACE_PIN: AuthMode
AUTH_EXT_MODE_ID_FINGERPRINT_FACE: AuthMode
AUTH_EXT_MODE_ID_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE_OR_FINGERPRINT_PIN: AuthMode
AUTH_EXT_MODE_ID_FACE_FINGERPRINT_OR_PIN: AuthMode
AUTH_EXT_MODE_ID_FINGERPRINT_FACE_OR_PIN: AuthMode
OPERATOR_LEVEL_NONE: OperatorLevel
OPERATOR_LEVEL_ADMIN: OperatorLevel
OPERATOR_LEVEL_CONFIG: OperatorLevel
OPERATOR_LEVEL_USER: OperatorLevel
FACE_DETECTION_NONE: FaceDetectionLevel
FACE_DETECTION_NORMAL: FaceDetectionLevel
FACE_DETECTION_STRICT: FaceDetectionLevel
GLOBAL_APB_FAIL_ACTION_NONE: GlobalAPBFailActionType
GLOBAL_APB_FAIL_ACTION_SOFT: GlobalAPBFailActionType
GLOBAL_APB_FAIL_ACTION_HARD: GlobalAPBFailActionType

class Operator(_message.Message):
    __slots__ = ("userID", "level")
    USERID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    userID: str
    level: OperatorLevel
    def __init__(self, userID: _Optional[str] = ..., level: _Optional[_Union[OperatorLevel, str]] = ...) -> None: ...

class AuthSchedule(_message.Message):
    __slots__ = ("mode", "scheduleID")
    MODE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    mode: AuthMode
    scheduleID: int
    def __init__(self, mode: _Optional[_Union[AuthMode, str]] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class AuthConfig(_message.Message):
    __slots__ = ("authSchedules", "useGlobalAPB", "globalAPBFailAction", "useGroupMatching", "usePrivateAuth", "faceDetectionLevel", "useServerMatching", "useFullAccess", "matchTimeout", "authTimeout", "operators")
    AUTHSCHEDULES_FIELD_NUMBER: _ClassVar[int]
    USEGLOBALAPB_FIELD_NUMBER: _ClassVar[int]
    GLOBALAPBFAILACTION_FIELD_NUMBER: _ClassVar[int]
    USEGROUPMATCHING_FIELD_NUMBER: _ClassVar[int]
    USEPRIVATEAUTH_FIELD_NUMBER: _ClassVar[int]
    FACEDETECTIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    USESERVERMATCHING_FIELD_NUMBER: _ClassVar[int]
    USEFULLACCESS_FIELD_NUMBER: _ClassVar[int]
    MATCHTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AUTHTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    authSchedules: _containers.RepeatedCompositeFieldContainer[AuthSchedule]
    useGlobalAPB: bool
    globalAPBFailAction: GlobalAPBFailActionType
    useGroupMatching: bool
    usePrivateAuth: bool
    faceDetectionLevel: FaceDetectionLevel
    useServerMatching: bool
    useFullAccess: bool
    matchTimeout: int
    authTimeout: int
    operators: _containers.RepeatedCompositeFieldContainer[Operator]
    def __init__(self, authSchedules: _Optional[_Iterable[_Union[AuthSchedule, _Mapping]]] = ..., useGlobalAPB: bool = ..., globalAPBFailAction: _Optional[_Union[GlobalAPBFailActionType, str]] = ..., useGroupMatching: bool = ..., usePrivateAuth: bool = ..., faceDetectionLevel: _Optional[_Union[FaceDetectionLevel, str]] = ..., useServerMatching: bool = ..., useFullAccess: bool = ..., matchTimeout: _Optional[int] = ..., authTimeout: _Optional[int] = ..., operators: _Optional[_Iterable[_Union[Operator, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: AuthConfig
    def __init__(self, config: _Optional[_Union[AuthConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: AuthConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[AuthConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: AuthConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[AuthConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
