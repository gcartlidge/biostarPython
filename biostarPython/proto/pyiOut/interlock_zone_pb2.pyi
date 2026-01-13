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
    MAX_DOORS: _ClassVar[Enum]
    MAX_INPUTS: _ClassVar[Enum]
    MAX_OUTPUTS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_NONE: _ClassVar[OperationType]
    OPERATION_ENRTY: _ClassVar[OperationType]
    OPERATION_EXIT: _ClassVar[OperationType]
    OPERATION_ALL: _ClassVar[OperationType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_DOORS: Enum
MAX_INPUTS: Enum
MAX_OUTPUTS: Enum
MAX_NAME_LENGTH: Enum
OPERATION_NONE: OperationType
OPERATION_ENRTY: OperationType
OPERATION_EXIT: OperationType
OPERATION_ALL: OperationType

class Input(_message.Message):
    __slots__ = ("deviceID", "port", "switchType", "duration", "operation")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SWITCHTYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    switchType: _device_pb2.SwitchType
    duration: int
    operation: int
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., switchType: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., duration: _Optional[int] = ..., operation: _Optional[int] = ...) -> None: ...

class Output(_message.Message):
    __slots__ = ("event", "action")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    event: int
    action: _action_pb2.Action
    def __init__(self, event: _Optional[int] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("zoneID", "name", "disabled", "inputs", "outputs", "doorIDs")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    name: str
    disabled: bool
    inputs: _containers.RepeatedCompositeFieldContainer[Input]
    outputs: _containers.RepeatedCompositeFieldContainer[Output]
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, zoneID: _Optional[int] = ..., name: _Optional[str] = ..., disabled: bool = ..., inputs: _Optional[_Iterable[_Union[Input, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[Output, _Mapping]]] = ..., doorIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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
