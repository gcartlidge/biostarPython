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
    DEFAULT_RTSP_SERVER_PORT: _ClassVar[Enum]
    MAX_RTSP_ID_LENGTH: _ClassVar[Enum]
    MAX_RTSP_PASSWORD_LENGTH: _ClassVar[Enum]

class RTSP_RESOLUTION_TYPE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RTSP_RESOLUTION_DEFAULT: _ClassVar[RTSP_RESOLUTION_TYPE]
    RTSP_RESOLUTION_TYPE_1: _ClassVar[RTSP_RESOLUTION_TYPE]
    RTSP_RESOLUTION_TYPE_2: _ClassVar[RTSP_RESOLUTION_TYPE]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_RTSP_SERVER_PORT: Enum
MAX_RTSP_ID_LENGTH: Enum
MAX_RTSP_PASSWORD_LENGTH: Enum
RTSP_RESOLUTION_DEFAULT: RTSP_RESOLUTION_TYPE
RTSP_RESOLUTION_TYPE_1: RTSP_RESOLUTION_TYPE
RTSP_RESOLUTION_TYPE_2: RTSP_RESOLUTION_TYPE

class RTSPConfig(_message.Message):
    __slots__ = ("serverURL", "serverPort", "userID", "userPW", "enabled", "resolution")
    SERVERURL_FIELD_NUMBER: _ClassVar[int]
    SERVERPORT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERPW_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    serverURL: str
    serverPort: int
    userID: str
    userPW: str
    enabled: bool
    resolution: RTSP_RESOLUTION_TYPE
    def __init__(self, serverURL: _Optional[str] = ..., serverPort: _Optional[int] = ..., userID: _Optional[str] = ..., userPW: _Optional[str] = ..., enabled: bool = ..., resolution: _Optional[_Union[RTSP_RESOLUTION_TYPE, str]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: RTSPConfig
    def __init__(self, config: _Optional[_Union[RTSPConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: RTSPConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[RTSPConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: RTSPConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[RTSPConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
