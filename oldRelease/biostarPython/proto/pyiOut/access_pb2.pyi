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
    MAX_LEVELS_IN_GROUP: _ClassVar[Enum]
    MAX_SCHEDULES_IN_LEVEL: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_LEVELS_IN_GROUP: Enum
MAX_SCHEDULES_IN_LEVEL: Enum
MAX_NAME_LENGTH: Enum

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class AccessGroup(_message.Message):
    __slots__ = ("ID", "name", "levelIDs")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVELIDS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    levelIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., levelIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("groups",)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[AccessGroup]
    def __init__(self, groups: _Optional[_Iterable[_Union[AccessGroup, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("deviceID", "groups")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    groups: _containers.RepeatedCompositeFieldContainer[AccessGroup]
    def __init__(self, deviceID: _Optional[int] = ..., groups: _Optional[_Iterable[_Union[AccessGroup, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "groups")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    groups: _containers.RepeatedCompositeFieldContainer[AccessGroup]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., groups: _Optional[_Iterable[_Union[AccessGroup, _Mapping]]] = ...) -> None: ...

class AddMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "groupIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "groupIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    groupIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., groupIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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

class GetLevelListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DoorSchedule(_message.Message):
    __slots__ = ("doorID", "scheduleID")
    DOORID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    doorID: int
    scheduleID: int
    def __init__(self, doorID: _Optional[int] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class AccessLevel(_message.Message):
    __slots__ = ("ID", "name", "doorSchedules")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOORSCHEDULES_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    doorSchedules: _containers.RepeatedCompositeFieldContainer[DoorSchedule]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., doorSchedules: _Optional[_Iterable[_Union[DoorSchedule, _Mapping]]] = ...) -> None: ...

class GetLevelListResponse(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[AccessLevel]
    def __init__(self, levels: _Optional[_Iterable[_Union[AccessLevel, _Mapping]]] = ...) -> None: ...

class AddLevelRequest(_message.Message):
    __slots__ = ("deviceID", "levels")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    levels: _containers.RepeatedCompositeFieldContainer[AccessLevel]
    def __init__(self, deviceID: _Optional[int] = ..., levels: _Optional[_Iterable[_Union[AccessLevel, _Mapping]]] = ...) -> None: ...

class AddLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "levels")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    levels: _containers.RepeatedCompositeFieldContainer[AccessLevel]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., levels: _Optional[_Iterable[_Union[AccessLevel, _Mapping]]] = ...) -> None: ...

class AddLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteLevelRequest(_message.Message):
    __slots__ = ("deviceID", "levelIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LEVELIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    levelIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., levelIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "levelIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    LEVELIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    levelIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., levelIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllLevelRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class FloorSchedule(_message.Message):
    __slots__ = ("liftID", "floorIndex", "scheduleID")
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEX_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    liftID: int
    floorIndex: int
    scheduleID: int
    def __init__(self, liftID: _Optional[int] = ..., floorIndex: _Optional[int] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class FloorLevel(_message.Message):
    __slots__ = ("ID", "name", "floorSchedules")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLOORSCHEDULES_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    floorSchedules: _containers.RepeatedCompositeFieldContainer[FloorSchedule]
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., floorSchedules: _Optional[_Iterable[_Union[FloorSchedule, _Mapping]]] = ...) -> None: ...

class GetFloorLevelListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetFloorLevelListResponse(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[FloorLevel]
    def __init__(self, levels: _Optional[_Iterable[_Union[FloorLevel, _Mapping]]] = ...) -> None: ...

class AddFloorLevelRequest(_message.Message):
    __slots__ = ("deviceID", "levels")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    levels: _containers.RepeatedCompositeFieldContainer[FloorLevel]
    def __init__(self, deviceID: _Optional[int] = ..., levels: _Optional[_Iterable[_Union[FloorLevel, _Mapping]]] = ...) -> None: ...

class AddFloorLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddFloorLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "levels")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    levels: _containers.RepeatedCompositeFieldContainer[FloorLevel]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., levels: _Optional[_Iterable[_Union[FloorLevel, _Mapping]]] = ...) -> None: ...

class AddFloorLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteFloorLevelRequest(_message.Message):
    __slots__ = ("deviceID", "levelIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LEVELIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    levelIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., levelIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteFloorLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFloorLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "levelIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    LEVELIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    levelIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., levelIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteFloorLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllFloorLevelRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllFloorLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllFloorLevelMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllFloorLevelMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
