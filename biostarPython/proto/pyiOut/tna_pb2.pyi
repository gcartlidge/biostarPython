import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNUSED: _ClassVar[Mode]
    BY_USER: _ClassVar[Mode]
    BY_SCHEDULE: _ClassVar[Mode]
    LAST_CHOICE: _ClassVar[Mode]
    FIXED: _ClassVar[Mode]

class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[Key]
    KEY_1: _ClassVar[Key]
    KEY_2: _ClassVar[Key]
    KEY_3: _ClassVar[Key]
    KEY_4: _ClassVar[Key]
    KEY_5: _ClassVar[Key]
    KEY_6: _ClassVar[Key]
    KEY_7: _ClassVar[Key]
    KEY_8: _ClassVar[Key]
    KEY_9: _ClassVar[Key]
    KEY_10: _ClassVar[Key]
    KEY_11: _ClassVar[Key]
    KEY_12: _ClassVar[Key]
    KEY_13: _ClassVar[Key]
    KEY_14: _ClassVar[Key]
    KEY_15: _ClassVar[Key]
    KEY_16: _ClassVar[Key]
    MAX_TNA_KEYS: _ClassVar[Key]
    MAX_TNA_LABEL_LENGTH: _ClassVar[Key]
UNUSED: Mode
BY_USER: Mode
BY_SCHEDULE: Mode
LAST_CHOICE: Mode
FIXED: Mode
UNSPECIFIED: Key
KEY_1: Key
KEY_2: Key
KEY_3: Key
KEY_4: Key
KEY_5: Key
KEY_6: Key
KEY_7: Key
KEY_8: Key
KEY_9: Key
KEY_10: Key
KEY_11: Key
KEY_12: Key
KEY_13: Key
KEY_14: Key
KEY_15: Key
KEY_16: Key
MAX_TNA_KEYS: Key
MAX_TNA_LABEL_LENGTH: Key

class TNAConfig(_message.Message):
    __slots__ = ("mode", "key", "isRequired", "schedules", "labels")
    MODE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ISREQUIRED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    mode: Mode
    key: Key
    isRequired: bool
    schedules: _containers.RepeatedScalarFieldContainer[int]
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[_Union[Mode, str]] = ..., key: _Optional[_Union[Key, str]] = ..., isRequired: bool = ..., schedules: _Optional[_Iterable[int]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TNAConfig
    def __init__(self, config: _Optional[_Union[TNAConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: TNAConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[TNAConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: TNAConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[TNAConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class JobCode(_message.Message):
    __slots__ = ("code", "label")
    CODE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    code: int
    label: str
    def __init__(self, code: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class TNALog(_message.Message):
    __slots__ = ("ID", "timestamp", "deviceID", "userID", "eventCode", "subCode", "TNAKey")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SUBCODE_FIELD_NUMBER: _ClassVar[int]
    TNAKEY_FIELD_NUMBER: _ClassVar[int]
    ID: int
    timestamp: int
    deviceID: int
    userID: str
    eventCode: int
    subCode: int
    TNAKey: Key
    def __init__(self, ID: _Optional[int] = ..., timestamp: _Optional[int] = ..., deviceID: _Optional[int] = ..., userID: _Optional[str] = ..., eventCode: _Optional[int] = ..., subCode: _Optional[int] = ..., TNAKey: _Optional[_Union[Key, str]] = ...) -> None: ...

class TNAEventFilter(_message.Message):
    __slots__ = ("startTime", "endTime", "userIDs", "TNAKeys")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    TNAKEYS_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    TNAKeys: _containers.RepeatedScalarFieldContainer[Key]
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ..., TNAKeys: _Optional[_Iterable[_Union[Key, str]]] = ...) -> None: ...

class JobCodeLog(_message.Message):
    __slots__ = ("ID", "timestamp", "deviceID", "userID", "eventCode", "subCode", "jobCode")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SUBCODE_FIELD_NUMBER: _ClassVar[int]
    JOBCODE_FIELD_NUMBER: _ClassVar[int]
    ID: int
    timestamp: int
    deviceID: int
    userID: str
    eventCode: int
    subCode: int
    jobCode: int
    def __init__(self, ID: _Optional[int] = ..., timestamp: _Optional[int] = ..., deviceID: _Optional[int] = ..., userID: _Optional[str] = ..., eventCode: _Optional[int] = ..., subCode: _Optional[int] = ..., jobCode: _Optional[int] = ...) -> None: ...

class JobCodeEventFilter(_message.Message):
    __slots__ = ("startTime", "endTime", "userIDs", "jobCodes")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    JOBCODES_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    jobCodes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ..., jobCodes: _Optional[_Iterable[int]] = ...) -> None: ...

class GetTNALogRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog", "filter")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    filter: TNAEventFilter
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ..., filter: _Optional[_Union[TNAEventFilter, _Mapping]] = ...) -> None: ...

class GetTNALogResponse(_message.Message):
    __slots__ = ("TNAEvents",)
    TNAEVENTS_FIELD_NUMBER: _ClassVar[int]
    TNAEvents: _containers.RepeatedCompositeFieldContainer[TNALog]
    def __init__(self, TNAEvents: _Optional[_Iterable[_Union[TNALog, _Mapping]]] = ...) -> None: ...

class GetJobCodeLogRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ...) -> None: ...

class GetJobCodeLogResponse(_message.Message):
    __slots__ = ("jobCodeEvents",)
    JOBCODEEVENTS_FIELD_NUMBER: _ClassVar[int]
    jobCodeEvents: _containers.RepeatedCompositeFieldContainer[JobCodeLog]
    def __init__(self, jobCodeEvents: _Optional[_Iterable[_Union[JobCodeLog, _Mapping]]] = ...) -> None: ...
