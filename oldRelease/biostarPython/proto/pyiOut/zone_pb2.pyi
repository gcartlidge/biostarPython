from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APB: _ClassVar[Type]
    TIMED_APB: _ClassVar[Type]
    FIRE_ALARM: _ClassVar[Type]
    SCHEDULED_LOCK: _ClassVar[Type]
    INTRUSION_ALARM: _ClassVar[Type]
    INTERLOCK: _ClassVar[Type]
    LIFT: _ClassVar[Type]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL: _ClassVar[Status]
    ALARMED: _ClassVar[Status]
    LOCKED: _ClassVar[Status]
    UNLOCKED: _ClassVar[Status]
    LIFT_LOCKED: _ClassVar[Status]
    LIFT_UNLOCKED: _ClassVar[Status]
    ARMED: _ClassVar[Status]
    DISARMED: _ClassVar[Status]
APB: Type
TIMED_APB: Type
FIRE_ALARM: Type
SCHEDULED_LOCK: Type
INTRUSION_ALARM: Type
INTERLOCK: Type
LIFT: Type
NORMAL: Status
ALARMED: Status
LOCKED: Status
UNLOCKED: Status
LIFT_LOCKED: Status
LIFT_UNLOCKED: Status
ARMED: Status
DISARMED: Status

class ZoneStatus(_message.Message):
    __slots__ = ("zoneID", "status", "disabled")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    status: Status
    disabled: bool
    def __init__(self, zoneID: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ..., disabled: bool = ...) -> None: ...
