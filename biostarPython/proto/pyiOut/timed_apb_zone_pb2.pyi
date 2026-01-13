import zone_pb2 as _zone_pb2
import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_RESET: _ClassVar[Enum]
    DEFAULT_RESET_DURATION: _ClassVar[Enum]
    MAX_ALARMS: _ClassVar[Enum]
    MAX_BYPASS_GROUPS: _ClassVar[Enum]
    MAX_MEMBERS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARD: _ClassVar[Type]
    SOFT: _ClassVar[Type]
NO_RESET: Enum
DEFAULT_RESET_DURATION: Enum
MAX_ALARMS: Enum
MAX_BYPASS_GROUPS: Enum
MAX_MEMBERS: Enum
MAX_NAME_LENGTH: Enum
HARD: Type
SOFT: Type

class Member(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("zoneID", "name", "type", "disabled", "alarmed", "resetDuration", "members", "actions", "bypassGroupIDs")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALARMED_FIELD_NUMBER: _ClassVar[int]
    RESETDURATION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    BYPASSGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    name: str
    type: Type
    disabled: bool
    alarmed: bool
    resetDuration: int
    members: _containers.RepeatedCompositeFieldContainer[Member]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    bypassGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, zoneID: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[Type, str]] = ..., disabled: bool = ..., alarmed: bool = ..., resetDuration: _Optional[int] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., bypassGroupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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

class ClearRequest(_message.Message):
    __slots__ = ("deviceID", "zoneID", "userIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    USERIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zoneID: int
    userIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., zoneID: _Optional[int] = ..., userIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class ClearResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearAllRequest(_message.Message):
    __slots__ = ("deviceID", "zoneID")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    zoneID: int
    def __init__(self, deviceID: _Optional[int] = ..., zoneID: _Optional[int] = ...) -> None: ...

class ClearAllResponse(_message.Message):
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
