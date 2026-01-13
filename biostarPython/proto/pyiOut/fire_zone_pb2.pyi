import zone_pb2 as _zone_pb2
import action_pb2 as _action_pb2
import device_pb2 as _device_pb2
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
    MAX_ALARMS: _ClassVar[Enum]
    MAX_SENSORS: _ClassVar[Enum]
    MAX_DOOR_OR_LIFTS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_ALARMS: Enum
MAX_SENSORS: Enum
MAX_DOOR_OR_LIFTS: Enum
MAX_NAME_LENGTH: Enum

class FireSensor(_message.Message):
    __slots__ = ("deviceID", "port", "type", "duration")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    type: _device_pb2.SwitchType
    duration: int
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., duration: _Optional[int] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("zoneID", "name", "disabled", "alarmed", "doorIDs", "sensors", "actions")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALARMED_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    SENSORS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    name: str
    disabled: bool
    alarmed: bool
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    sensors: _containers.RepeatedCompositeFieldContainer[FireSensor]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    def __init__(self, zoneID: _Optional[int] = ..., name: _Optional[str] = ..., disabled: bool = ..., alarmed: bool = ..., doorIDs: _Optional[_Iterable[int]] = ..., sensors: _Optional[_Iterable[_Union[FireSensor, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ...) -> None: ...

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
