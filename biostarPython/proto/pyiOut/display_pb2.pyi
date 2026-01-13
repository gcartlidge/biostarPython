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
    DEFAULT_MENU_TIMEOUT: _ClassVar[Enum]
    DEFAULT_MESSAGE_TIMEOUT: _ClassVar[Enum]
    DEFAULT_BACKLIGHT_TIMEOUT: _ClassVar[Enum]
    DEFAULT_VOLUME: _ClassVar[Enum]
    MIN_VOLUME: _ClassVar[Enum]
    MAX_VOLUME: _ClassVar[Enum]
    MIN_MESSAGE_TIMEOUT: _ClassVar[Enum]
    MAX_MESSAGE_TIMEOUT: _ClassVar[Enum]
    OSDP_LED_SHOW_TIMEOUT: _ClassVar[Enum]

class LanguageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_LANGUAGE_KOREAN: _ClassVar[LanguageType]
    BS2_LANGUAGE_ENGLISH: _ClassVar[LanguageType]
    BS2_LANGUAGE_CUSTOM: _ClassVar[LanguageType]

class BackgroundType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_BG_LOGO: _ClassVar[BackgroundType]
    BS2_BG_NOTICE: _ClassVar[BackgroundType]
    BS2_BG_SLIDE: _ClassVar[BackgroundType]
    BS2_BG_PDF: _ClassVar[BackgroundType]

class BackgroundTheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_BG_THEME_01: _ClassVar[BackgroundTheme]
    BS2_BG_THEME_02: _ClassVar[BackgroundTheme]
    BS2_BG_THEME_03: _ClassVar[BackgroundTheme]
    BS2_BG_THEME_04: _ClassVar[BackgroundTheme]

class DateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_DATE_FORMAT_YYYYMMDD: _ClassVar[DateFormat]
    BS2_DATE_FORMAT_MMDDYYYY: _ClassVar[DateFormat]
    BS2_DATE_FORMAT_DDMMYYYY: _ClassVar[DateFormat]

class TimeFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_TIME_FORMAT_12_HOUR: _ClassVar[TimeFormat]
    BS2_TIME_FORMAT_24_HOUR: _ClassVar[TimeFormat]

class ShowOSDPResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_SHOW_OSDP_RESULT_ON: _ClassVar[ShowOSDPResult]
    BS2_SHOW_OSDP_RESULT_OFF: _ClassVar[ShowOSDPResult]

class ShowOptionUserInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_SHOW_USER_INFO_ALL: _ClassVar[ShowOptionUserInfo]
    BS2_SHOW_USER_INFO_PARTIAL: _ClassVar[ShowOptionUserInfo]
    BS2_SHOW_USER_INFO_NOTHING: _ClassVar[ShowOptionUserInfo]

class KeypadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BS2_KEYPAD_TYPE_SCRAMBLE: _ClassVar[KeypadType]
    BS2_KEYPAD_TYPE_NORMAL: _ClassVar[KeypadType]

class SoundIndex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOUND_INDEX_WELCOME: _ClassVar[SoundIndex]
    SOUND_INDEX_AUTH_SUCCESS: _ClassVar[SoundIndex]
    SOUND_INDEX_AUTH_FAIL: _ClassVar[SoundIndex]
    SOUND_INDEX_ALARM_1: _ClassVar[SoundIndex]
    SOUND_INDEX_ALARM_2: _ClassVar[SoundIndex]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_MENU_TIMEOUT: Enum
DEFAULT_MESSAGE_TIMEOUT: Enum
DEFAULT_BACKLIGHT_TIMEOUT: Enum
DEFAULT_VOLUME: Enum
MIN_VOLUME: Enum
MAX_VOLUME: Enum
MIN_MESSAGE_TIMEOUT: Enum
MAX_MESSAGE_TIMEOUT: Enum
OSDP_LED_SHOW_TIMEOUT: Enum
BS2_LANGUAGE_KOREAN: LanguageType
BS2_LANGUAGE_ENGLISH: LanguageType
BS2_LANGUAGE_CUSTOM: LanguageType
BS2_BG_LOGO: BackgroundType
BS2_BG_NOTICE: BackgroundType
BS2_BG_SLIDE: BackgroundType
BS2_BG_PDF: BackgroundType
BS2_BG_THEME_01: BackgroundTheme
BS2_BG_THEME_02: BackgroundTheme
BS2_BG_THEME_03: BackgroundTheme
BS2_BG_THEME_04: BackgroundTheme
BS2_DATE_FORMAT_YYYYMMDD: DateFormat
BS2_DATE_FORMAT_MMDDYYYY: DateFormat
BS2_DATE_FORMAT_DDMMYYYY: DateFormat
BS2_TIME_FORMAT_12_HOUR: TimeFormat
BS2_TIME_FORMAT_24_HOUR: TimeFormat
BS2_SHOW_OSDP_RESULT_ON: ShowOSDPResult
BS2_SHOW_OSDP_RESULT_OFF: ShowOSDPResult
BS2_SHOW_USER_INFO_ALL: ShowOptionUserInfo
BS2_SHOW_USER_INFO_PARTIAL: ShowOptionUserInfo
BS2_SHOW_USER_INFO_NOTHING: ShowOptionUserInfo
BS2_KEYPAD_TYPE_SCRAMBLE: KeypadType
BS2_KEYPAD_TYPE_NORMAL: KeypadType
SOUND_INDEX_WELCOME: SoundIndex
SOUND_INDEX_AUTH_SUCCESS: SoundIndex
SOUND_INDEX_AUTH_FAIL: SoundIndex
SOUND_INDEX_ALARM_1: SoundIndex
SOUND_INDEX_ALARM_2: SoundIndex

class DisplayConfig(_message.Message):
    __slots__ = ("language", "background", "theme", "volume", "useVoice", "dateFormat", "timeFormat", "showDateTime", "menuTimeout", "msgTimeout", "backlightTimeout", "useUserPhrase", "queryUserPhrase", "useScreenSaver", "showOSDPResult", "showOptionUserName", "showOptionUserId", "keypadType")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    USEVOICE_FIELD_NUMBER: _ClassVar[int]
    DATEFORMAT_FIELD_NUMBER: _ClassVar[int]
    TIMEFORMAT_FIELD_NUMBER: _ClassVar[int]
    SHOWDATETIME_FIELD_NUMBER: _ClassVar[int]
    MENUTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MSGTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BACKLIGHTTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    USEUSERPHRASE_FIELD_NUMBER: _ClassVar[int]
    QUERYUSERPHRASE_FIELD_NUMBER: _ClassVar[int]
    USESCREENSAVER_FIELD_NUMBER: _ClassVar[int]
    SHOWOSDPRESULT_FIELD_NUMBER: _ClassVar[int]
    SHOWOPTIONUSERNAME_FIELD_NUMBER: _ClassVar[int]
    SHOWOPTIONUSERID_FIELD_NUMBER: _ClassVar[int]
    KEYPADTYPE_FIELD_NUMBER: _ClassVar[int]
    language: LanguageType
    background: BackgroundType
    theme: BackgroundTheme
    volume: int
    useVoice: bool
    dateFormat: DateFormat
    timeFormat: TimeFormat
    showDateTime: bool
    menuTimeout: int
    msgTimeout: int
    backlightTimeout: int
    useUserPhrase: bool
    queryUserPhrase: bool
    useScreenSaver: bool
    showOSDPResult: ShowOSDPResult
    showOptionUserName: ShowOptionUserInfo
    showOptionUserId: ShowOptionUserInfo
    keypadType: KeypadType
    def __init__(self, language: _Optional[_Union[LanguageType, str]] = ..., background: _Optional[_Union[BackgroundType, str]] = ..., theme: _Optional[_Union[BackgroundTheme, str]] = ..., volume: _Optional[int] = ..., useVoice: bool = ..., dateFormat: _Optional[_Union[DateFormat, str]] = ..., timeFormat: _Optional[_Union[TimeFormat, str]] = ..., showDateTime: bool = ..., menuTimeout: _Optional[int] = ..., msgTimeout: _Optional[int] = ..., backlightTimeout: _Optional[int] = ..., useUserPhrase: bool = ..., queryUserPhrase: bool = ..., useScreenSaver: bool = ..., showOSDPResult: _Optional[_Union[ShowOSDPResult, str]] = ..., showOptionUserName: _Optional[_Union[ShowOptionUserInfo, str]] = ..., showOptionUserId: _Optional[_Union[ShowOptionUserInfo, str]] = ..., keypadType: _Optional[_Union[KeypadType, str]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DisplayConfig
    def __init__(self, config: _Optional[_Union[DisplayConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: DisplayConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[DisplayConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: DisplayConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[DisplayConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateLanguagePackRequest(_message.Message):
    __slots__ = ("deviceID", "data")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    data: bytes
    def __init__(self, deviceID: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UpdateLanguagePackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateLanguagePackMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "data")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    data: bytes
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., data: _Optional[bytes] = ...) -> None: ...

class UpdateLanguagePackMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateNoticeRequest(_message.Message):
    __slots__ = ("deviceID", "notice")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    notice: str
    def __init__(self, deviceID: _Optional[int] = ..., notice: _Optional[str] = ...) -> None: ...

class UpdateNoticeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateNoticeMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "notice")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    notice: str
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., notice: _Optional[str] = ...) -> None: ...

class UpdateNoticeMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateBackgroundImageRequest(_message.Message):
    __slots__ = ("deviceID", "PNGImage")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PNGIMAGE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    PNGImage: bytes
    def __init__(self, deviceID: _Optional[int] = ..., PNGImage: _Optional[bytes] = ...) -> None: ...

class UpdateBackgroundImageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBackgroundImageMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "PNGImage")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    PNGIMAGE_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    PNGImage: bytes
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., PNGImage: _Optional[bytes] = ...) -> None: ...

class UpdateBackgroundImageMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateSlideImagesRequest(_message.Message):
    __slots__ = ("deviceID", "PNGImages")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PNGIMAGES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    PNGImages: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, deviceID: _Optional[int] = ..., PNGImages: _Optional[_Iterable[bytes]] = ...) -> None: ...

class UpdateSlideImagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSlideImagesMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "PNGImages")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    PNGIMAGES_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    PNGImages: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., PNGImages: _Optional[_Iterable[bytes]] = ...) -> None: ...

class UpdateSlideImagesMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpdateSoundRequest(_message.Message):
    __slots__ = ("deviceID", "index", "waveData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    WAVEDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    index: SoundIndex
    waveData: bytes
    def __init__(self, deviceID: _Optional[int] = ..., index: _Optional[_Union[SoundIndex, str]] = ..., waveData: _Optional[bytes] = ...) -> None: ...

class UpdateSoundResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateSoundMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "index", "waveData")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    WAVEDATA_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    index: SoundIndex
    waveData: bytes
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., index: _Optional[_Union[SoundIndex, str]] = ..., waveData: _Optional[bytes] = ...) -> None: ...

class UpdateSoundMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
