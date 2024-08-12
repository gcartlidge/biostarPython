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
    MIN_DST_OFFSET: _ClassVar[Enum]
    MAX_DST_OFFSET: _ClassVar[Enum]
    MAX_DST_SCHEDULES: _ClassVar[Enum]

class Month(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MONTH_JANUARY: _ClassVar[Month]
    MONTH_FEBRUARY: _ClassVar[Month]
    MONTH_MARCH: _ClassVar[Month]
    MONTH_APRIL: _ClassVar[Month]
    MONTH_MAY: _ClassVar[Month]
    MONTH_JUNE: _ClassVar[Month]
    MONTH_JULY: _ClassVar[Month]
    MONTH_AUGUST: _ClassVar[Month]
    MONTH_SEPTEMBER: _ClassVar[Month]
    MONTH_OCTOBER: _ClassVar[Month]
    MONTH_NOVEMBER: _ClassVar[Month]
    MONTH_DECEMBER: _ClassVar[Month]

class Weekday(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEEKDAY_SUNDAY: _ClassVar[Weekday]
    WEEKDAY_MONDAY: _ClassVar[Weekday]
    WEEKDAY_TUESDAY: _ClassVar[Weekday]
    WEEKDAY_WEDNESDAY: _ClassVar[Weekday]
    WEEKDAY_THURSDAY: _ClassVar[Weekday]
    WEEKDAY_FRIDAY: _ClassVar[Weekday]
    WEEKDAY_SATURDAY: _ClassVar[Weekday]

class Ordinal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDINAL_FIRST: _ClassVar[Ordinal]
    ORDINAL_SECOND: _ClassVar[Ordinal]
    ORDINAL_THIRD: _ClassVar[Ordinal]
    ORDINAL_FOURTH: _ClassVar[Ordinal]
    ORDINAL_FIFTH: _ClassVar[Ordinal]
    ORDINAL_SIXTH: _ClassVar[Ordinal]
    ORDINAL_SEVENTH: _ClassVar[Ordinal]
    ORDINAL_EIGHTH: _ClassVar[Ordinal]
    ORDINAL_NINTH: _ClassVar[Ordinal]
    ORDINAL_TENTH: _ClassVar[Ordinal]
    ORDINAL_LAST: _ClassVar[Ordinal]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MIN_DST_OFFSET: Enum
MAX_DST_OFFSET: Enum
MAX_DST_SCHEDULES: Enum
MONTH_JANUARY: Month
MONTH_FEBRUARY: Month
MONTH_MARCH: Month
MONTH_APRIL: Month
MONTH_MAY: Month
MONTH_JUNE: Month
MONTH_JULY: Month
MONTH_AUGUST: Month
MONTH_SEPTEMBER: Month
MONTH_OCTOBER: Month
MONTH_NOVEMBER: Month
MONTH_DECEMBER: Month
WEEKDAY_SUNDAY: Weekday
WEEKDAY_MONDAY: Weekday
WEEKDAY_TUESDAY: Weekday
WEEKDAY_WEDNESDAY: Weekday
WEEKDAY_THURSDAY: Weekday
WEEKDAY_FRIDAY: Weekday
WEEKDAY_SATURDAY: Weekday
ORDINAL_FIRST: Ordinal
ORDINAL_SECOND: Ordinal
ORDINAL_THIRD: Ordinal
ORDINAL_FOURTH: Ordinal
ORDINAL_FIFTH: Ordinal
ORDINAL_SIXTH: Ordinal
ORDINAL_SEVENTH: Ordinal
ORDINAL_EIGHTH: Ordinal
ORDINAL_NINTH: Ordinal
ORDINAL_TENTH: Ordinal
ORDINAL_LAST: Ordinal

class GetRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("GMTTime",)
    GMTTIME_FIELD_NUMBER: _ClassVar[int]
    GMTTime: int
    def __init__(self, GMTTime: _Optional[int] = ...) -> None: ...

class SetRequest(_message.Message):
    __slots__ = ("deviceID", "GMTTime")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GMTTIME_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    GMTTime: int
    def __init__(self, deviceID: _Optional[int] = ..., GMTTime: _Optional[int] = ...) -> None: ...

class SetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "GMTTime")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GMTTIME_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    GMTTime: int
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., GMTTime: _Optional[int] = ...) -> None: ...

class SetMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class TimeConfig(_message.Message):
    __slots__ = ("timeZone", "syncWithServer")
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    SYNCWITHSERVER_FIELD_NUMBER: _ClassVar[int]
    timeZone: int
    syncWithServer: bool
    def __init__(self, timeZone: _Optional[int] = ..., syncWithServer: bool = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TimeConfig
    def __init__(self, config: _Optional[_Union[TimeConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: TimeConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[TimeConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: TimeConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[TimeConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class WeekTime(_message.Message):
    __slots__ = ("year", "month", "ordinal", "weekday", "hour", "minute", "second")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    WEEKDAY_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: Month
    ordinal: Ordinal
    weekday: Weekday
    hour: int
    minute: int
    second: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[_Union[Month, str]] = ..., ordinal: _Optional[_Union[Ordinal, str]] = ..., weekday: _Optional[_Union[Weekday, str]] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., second: _Optional[int] = ...) -> None: ...

class DSTSchedule(_message.Message):
    __slots__ = ("startTime", "endTime", "timeOffset")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    TIMEOFFSET_FIELD_NUMBER: _ClassVar[int]
    startTime: WeekTime
    endTime: WeekTime
    timeOffset: int
    def __init__(self, startTime: _Optional[_Union[WeekTime, _Mapping]] = ..., endTime: _Optional[_Union[WeekTime, _Mapping]] = ..., timeOffset: _Optional[int] = ...) -> None: ...

class DSTConfig(_message.Message):
    __slots__ = ("schedules",)
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[DSTSchedule]
    def __init__(self, schedules: _Optional[_Iterable[_Union[DSTSchedule, _Mapping]]] = ...) -> None: ...

class GetDSTConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetDSTConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DSTConfig
    def __init__(self, config: _Optional[_Union[DSTConfig, _Mapping]] = ...) -> None: ...

class SetDSTConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: DSTConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[DSTConfig, _Mapping]] = ...) -> None: ...

class SetDSTConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetDSTConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: DSTConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[DSTConfig, _Mapping]] = ...) -> None: ...

class SetDSTConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
