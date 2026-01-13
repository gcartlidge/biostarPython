import zone_pb2 as _zone_pb2
import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    MAX_ALARMS: _ClassVar[Enum]
    MAX_BYPASS_GROUPS: _ClassVar[Enum]
    MAX_UNLOCK_GROUPS: _ClassVar[Enum]
    MAX_LIFTS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_ALARMS: Enum
MAX_BYPASS_GROUPS: Enum
MAX_UNLOCK_GROUPS: Enum
MAX_LIFTS: Enum
MAX_NAME_LENGTH: Enum

class Lift(_message.Message):
    __slots__ = ("liftID", "floorIndexes")
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEXES_FIELD_NUMBER: _ClassVar[int]
    liftID: int
    floorIndexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, liftID: _Optional[int] = ..., floorIndexes: _Optional[_Iterable[int]] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("zoneID", "name", "activateScheduleID", "deactivateScheduleID", "disabled", "alarmed", "lifts", "actions", "bypassGroupIDs", "unlockGroupIDs")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATESCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATESCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALARMED_FIELD_NUMBER: _ClassVar[int]
    LIFTS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    BYPASSGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    UNLOCKGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    name: str
    activateScheduleID: int
    deactivateScheduleID: int
    disabled: bool
    alarmed: bool
    lifts: _containers.RepeatedCompositeFieldContainer[Lift]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    bypassGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    unlockGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, zoneID: _Optional[int] = ..., name: _Optional[str] = ..., activateScheduleID: _Optional[int] = ..., deactivateScheduleID: _Optional[int] = ..., disabled: bool = ..., alarmed: bool = ..., lifts: _Optional[_Iterable[_Union[Lift, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., bypassGroupIDs: _Optional[_Iterable[int]] = ..., unlockGroupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("zones",)
    ZONES_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[ZoneInfo]
    def __init__(self, zones: _Optional[_Iterable[_Union[ZoneInfo, _Mapping]]] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ("deviceID", "zoneIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zoneIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., zoneIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetStatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[_zone_pb2.ZoneStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[_zone_pb2.ZoneStatus, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("deviceID", "zones")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zones: _containers.RepeatedCompositeFieldContainer[ZoneInfo]
    def __init__(self, deviceID: _Optional[int] = ..., zones: _Optional[_Iterable[_Union[ZoneInfo, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "zoneIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zoneIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., zoneIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAlarmRequest(_message.Message):
    __slots__ = ("deviceID", "zoneIDs", "alarmed")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONEIDS_FIELD_NUMBER: _ClassVar[int]
    ALARMED_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zoneIDs: _containers.RepeatedScalarFieldContainer[int]
    alarmed: bool
    def __init__(self, deviceID: _Optional[int] = ..., zoneIDs: _Optional[_Iterable[int]] = ..., alarmed: bool = ...) -> None: ...

class SetAlarmResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
