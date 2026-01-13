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
    DEFAULT_VOIP_SERVER_PORT: _ClassVar[Enum]
    MAX_VOIP_ID_LENGTH: _ClassVar[Enum]
    MAX_VOIP_PASSWORD_LENGTH: _ClassVar[Enum]
    MAX_PHONEBOOK_ITEMS: _ClassVar[Enum]
    MAX_PHONE_NUMBER_LENGTH: _ClassVar[Enum]
    MAX_PHONE_DESCRIPTION_LENGTH: _ClassVar[Enum]
    MAX_VOIP_URL_LENGTH: _ClassVar[Enum]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_VOIP_SERVER_PORT: Enum
MAX_VOIP_ID_LENGTH: Enum
MAX_VOIP_PASSWORD_LENGTH: Enum
MAX_PHONEBOOK_ITEMS: Enum
MAX_PHONE_NUMBER_LENGTH: Enum
MAX_PHONE_DESCRIPTION_LENGTH: Enum
MAX_VOIP_URL_LENGTH: Enum

class UserPhone(_message.Message):
    __slots__ = ("phoneNumber", "description")
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    phoneNumber: str
    description: str
    def __init__(self, phoneNumber: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class VOIPConfig(_message.Message):
    __slots__ = ("serverURL", "serverPort", "userID", "userPW", "enabled", "exitButton", "DTMFMode", "registrationDuration", "speakerVolume", "micVolume", "authorizationCode", "showExtensionNumber", "useOutboundProxy", "proxyURL", "proxyPort", "phones")
    SERVERURL_FIELD_NUMBER: _ClassVar[int]
    SERVERPORT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERPW_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXITBUTTON_FIELD_NUMBER: _ClassVar[int]
    DTMFMODE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATIONDURATION_FIELD_NUMBER: _ClassVar[int]
    SPEAKERVOLUME_FIELD_NUMBER: _ClassVar[int]
    MICVOLUME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATIONCODE_FIELD_NUMBER: _ClassVar[int]
    SHOWEXTENSIONNUMBER_FIELD_NUMBER: _ClassVar[int]
    USEOUTBOUNDPROXY_FIELD_NUMBER: _ClassVar[int]
    PROXYURL_FIELD_NUMBER: _ClassVar[int]
    PROXYPORT_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    serverURL: str
    serverPort: int
    userID: str
    userPW: str
    enabled: bool
    exitButton: int
    DTMFMode: int
    registrationDuration: int
    speakerVolume: int
    micVolume: int
    authorizationCode: str
    showExtensionNumber: bool
    useOutboundProxy: bool
    proxyURL: str
    proxyPort: int
    phones: _containers.RepeatedCompositeFieldContainer[UserPhone]
    def __init__(self, serverURL: _Optional[str] = ..., serverPort: _Optional[int] = ..., userID: _Optional[str] = ..., userPW: _Optional[str] = ..., enabled: bool = ..., exitButton: _Optional[int] = ..., DTMFMode: _Optional[int] = ..., registrationDuration: _Optional[int] = ..., speakerVolume: _Optional[int] = ..., micVolume: _Optional[int] = ..., authorizationCode: _Optional[str] = ..., showExtensionNumber: bool = ..., useOutboundProxy: bool = ..., proxyURL: _Optional[str] = ..., proxyPort: _Optional[int] = ..., phones: _Optional[_Iterable[_Union[UserPhone, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: VOIPConfig
    def __init__(self, config: _Optional[_Union[VOIPConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: VOIPConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[VOIPConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: VOIPConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[VOIPConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
