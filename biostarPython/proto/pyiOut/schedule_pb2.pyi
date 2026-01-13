import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PredefinedSchedule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEVER: _ClassVar[PredefinedSchedule]
    ALWAYS: _ClassVar[PredefinedSchedule]

class WeekDay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUNDAY: _ClassVar[WeekDay]
    MONDAY: _ClassVar[WeekDay]
    TUESDAY: _ClassVar[WeekDay]
    WEDNESDAY: _ClassVar[WeekDay]
    THURSDAY: _ClassVar[WeekDay]
    FRIDAY: _ClassVar[WeekDay]
    SATURDAY: _ClassVar[WeekDay]
    WEEKDAYS: _ClassVar[WeekDay]

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    MAX_HOLIDAY_GROUPS: _ClassVar[Enum]
    MAX_TIME_PERIODS: _ClassVar[Enum]
    MAX_DAILY_SCHEDULES: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]

class HolidayRecurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DO_NOT_RECUR: _ClassVar[HolidayRecurrence]
    RECUR_YEARLY: _ClassVar[HolidayRecurrence]
    RECUR_MONTHLY: _ClassVar[HolidayRecurrence]
    RECUR_WEEKLY: _ClassVar[HolidayRecurrence]
NEVER: PredefinedSchedule
ALWAYS: PredefinedSchedule
SUNDAY: WeekDay
MONDAY: WeekDay
TUESDAY: WeekDay
WEDNESDAY: WeekDay
THURSDAY: WeekDay
FRIDAY: WeekDay
SATURDAY: WeekDay
WEEKDAYS: WeekDay
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_HOLIDAY_GROUPS: Enum
MAX_TIME_PERIODS: Enum
MAX_DAILY_SCHEDULES: Enum
MAX_NAME_LENGTH: Enum
DO_NOT_RECUR: HolidayRecurrence
RECUR_YEARLY: HolidayRecurrence
RECUR_MONTHLY: HolidayRecurrence
RECUR_WEEKLY: HolidayRecurrence

class ScheduleInfo(_message.Message):
    __slots__ = ("ID", "name", "daily", "weekly", "holidays")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DAILY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_FIELD_NUMBER: _ClassVar[int]
    HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    daily: DailySchedule
    weekly: WeeklySchedule
    holidays: _containers.RepeatedCompositeFieldContainer[HolidaySchedule]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., daily: _Optional[_Union[DailySchedule, _Mapping]] = ..., weekly: _Optional[_Union[WeeklySchedule, _Mapping]] = ..., holidays: _Optional[_Iterable[_Union[HolidaySchedule, _Mapping]]] = ...) -> None: ...

class DaySchedule(_message.Message):
    __slots__ = ("periods",)
    PERIODS_FIELD_NUMBER: _ClassVar[int]
    periods: _containers.RepeatedCompositeFieldContainer[TimePeriod]
    def __init__(self, periods: _Optional[_Iterable[_Union[TimePeriod, _Mapping]]] = ...) -> None: ...

class TimePeriod(_message.Message):
    __slots__ = ("startTime", "endTime")
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    startTime: int
    endTime: int
    def __init__(self, startTime: _Optional[int] = ..., endTime: _Optional[int] = ...) -> None: ...

class WeeklySchedule(_message.Message):
    __slots__ = ("daySchedules",)
    DAYSCHEDULES_FIELD_NUMBER: _ClassVar[int]
    daySchedules: _containers.RepeatedCompositeFieldContainer[DaySchedule]
    def __init__(self, daySchedules: _Optional[_Iterable[_Union[DaySchedule, _Mapping]]] = ...) -> None: ...

class DailySchedule(_message.Message):
    __slots__ = ("startDate", "daySchedules")
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    DAYSCHEDULES_FIELD_NUMBER: _ClassVar[int]
    startDate: int
    daySchedules: _containers.RepeatedCompositeFieldContainer[DaySchedule]
    def __init__(self, startDate: _Optional[int] = ..., daySchedules: _Optional[_Iterable[_Union[DaySchedule, _Mapping]]] = ...) -> None: ...

class HolidaySchedule(_message.Message):
    __slots__ = ("groupID", "daySchedule")
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    DAYSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    groupID: int
    daySchedule: DaySchedule
    def __init__(self, groupID: _Optional[int] = ..., daySchedule: _Optional[_Union[DaySchedule, _Mapping]] = ...) -> None: ...

class HolidayGroup(_message.Message):
    __slots__ = ("ID", "name", "holidays")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    holidays: _containers.RepeatedCompositeFieldContainer[Holiday]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., holidays: _Optional[_Iterable[_Union[Holiday, _Mapping]]] = ...) -> None: ...

class Holiday(_message.Message):
    __slots__ = ("date", "recurrence")
    DATE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    date: int
    recurrence: HolidayRecurrence
    def __init__(self, date: _Optional[int] = ..., recurrence: _Optional[_Union[HolidayRecurrence, str]] = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("schedules",)
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[ScheduleInfo]
    def __init__(self, schedules: _Optional[_Iterable[_Union[ScheduleInfo, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("deviceID", "schedules")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    schedules: _containers.RepeatedCompositeFieldContainer[ScheduleInfo]
    def __init__(self, deviceID: _Optional[int] = ..., schedules: _Optional[_Iterable[_Union[ScheduleInfo, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "schedules")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    schedules: _containers.RepeatedCompositeFieldContainer[ScheduleInfo]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., schedules: _Optional[_Iterable[_Union[ScheduleInfo, _Mapping]]] = ...) -> None: ...

class AddMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "scheduleIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    scheduleIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., scheduleIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "scheduleIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    scheduleIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., scheduleIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class GetHolidayListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetHolidayListResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[HolidayGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[HolidayGroup, _Mapping]]] = ...) -> None: ...

class AddHolidayRequest(_message.Message):
    __slots__ = ("deviceID", "groups")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    groups: _containers.RepeatedCompositeFieldContainer[HolidayGroup]
    def __init__(self, deviceID: _Optional[int] = ..., groups: _Optional[_Iterable[_Union[HolidayGroup, _Mapping]]] = ...) -> None: ...

class AddHolidayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddHolidayMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "groups")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    groups: _containers.RepeatedCompositeFieldContainer[HolidayGroup]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., groups: _Optional[_Iterable[_Union[HolidayGroup, _Mapping]]] = ...) -> None: ...

class AddHolidayMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteHolidayRequest(_message.Message):
    __slots__ = ("deviceID", "groupIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteHolidayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteHolidayMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "groupIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteHolidayMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllHolidayRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllHolidayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllHolidayMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllHolidayMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
