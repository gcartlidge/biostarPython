import device_pb2 as _device_pb2
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
    DEFAULT_ACTIVATE_TIMEOUT: _ClassVar[Enum]
    DEFAULT_DUAL_AUTH_TIMEOUT: _ClassVar[Enum]
    MAX_ALARMS: _ClassVar[Enum]
    MAX_DEVICES: _ClassVar[Enum]
    MAX_DUAL_AUTH_APPROVAL_GROUPS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]
    MAX_FLOORS: _ClassVar[Enum]

class FloorFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[FloorFlag]
    SCHEDULE: _ClassVar[FloorFlag]
    OPERATOR: _ClassVar[FloorFlag]
    ACTION: _ClassVar[FloorFlag]
    EMERGENCY: _ClassVar[FloorFlag]

class AlarmFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_ALARM: _ClassVar[AlarmFlag]
    FIRST: _ClassVar[AlarmFlag]
    SECOND: _ClassVar[AlarmFlag]
    TAMPER: _ClassVar[AlarmFlag]

class DualAuthApprovalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_ON_LIFT: _ClassVar[DualAuthApprovalType]
    LAST_ON_LIFT: _ClassVar[DualAuthApprovalType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_ACTIVATE_TIMEOUT: Enum
DEFAULT_DUAL_AUTH_TIMEOUT: Enum
MAX_ALARMS: Enum
MAX_DEVICES: Enum
MAX_DUAL_AUTH_APPROVAL_GROUPS: Enum
MAX_NAME_LENGTH: Enum
MAX_FLOORS: Enum
NONE: FloorFlag
SCHEDULE: FloorFlag
OPERATOR: FloorFlag
ACTION: FloorFlag
EMERGENCY: FloorFlag
NO_ALARM: AlarmFlag
FIRST: AlarmFlag
SECOND: AlarmFlag
TAMPER: AlarmFlag
NONE_ON_LIFT: DualAuthApprovalType
LAST_ON_LIFT: DualAuthApprovalType

class FloorStatus(_message.Message):
    __slots__ = ("activated", "activateFlags", "deactivateFlags")
    ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    ACTIVATEFLAGS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATEFLAGS_FIELD_NUMBER: _ClassVar[int]
    activated: bool
    activateFlags: int
    deactivateFlags: int
    def __init__(self, activated: bool = ..., activateFlags: _Optional[int] = ..., deactivateFlags: _Optional[int] = ...) -> None: ...

class Floor(_message.Message):
    __slots__ = ("deviceID", "port", "status")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    status: FloorStatus
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., status: _Optional[_Union[FloorStatus, _Mapping]] = ...) -> None: ...

class Sensor(_message.Message):
    __slots__ = ("deviceID", "port", "type", "duration", "scheduleID")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    type: _device_pb2.SwitchType
    duration: int
    scheduleID: int
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., duration: _Optional[int] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class Alarm(_message.Message):
    __slots__ = ("sensor", "action")
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    sensor: Sensor
    action: _action_pb2.Action
    def __init__(self, sensor: _Optional[_Union[Sensor, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("liftID", "alarmFlags", "tamperOn", "floors")
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAGS_FIELD_NUMBER: _ClassVar[int]
    TAMPERON_FIELD_NUMBER: _ClassVar[int]
    FLOORS_FIELD_NUMBER: _ClassVar[int]
    liftID: int
    alarmFlags: int
    tamperOn: bool
    floors: _containers.RepeatedCompositeFieldContainer[FloorStatus]
    def __init__(self, liftID: _Optional[int] = ..., alarmFlags: _Optional[int] = ..., tamperOn: bool = ..., floors: _Optional[_Iterable[_Union[FloorStatus, _Mapping]]] = ...) -> None: ...

class LiftInfo(_message.Message):
    __slots__ = ("liftID", "name", "deviceIDs", "activateTimeout", "dualAuthTimeout", "dualAuthApproval", "dualAuthRequiredDeviceIDs", "dualAuthScheduleID", "floors", "dualAuthApprovalGroupIDs", "alarms", "alarmFlags", "tamper", "tamperOn")
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATETIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHAPPROVAL_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHREQUIREDDEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHSCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    FLOORS_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHAPPROVALGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAGS_FIELD_NUMBER: _ClassVar[int]
    TAMPER_FIELD_NUMBER: _ClassVar[int]
    TAMPERON_FIELD_NUMBER: _ClassVar[int]
    liftID: int
    name: str
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    activateTimeout: int
    dualAuthTimeout: int
    dualAuthApproval: DualAuthApprovalType
    dualAuthRequiredDeviceIDs: _containers.RepeatedScalarFieldContainer[int]
    dualAuthScheduleID: int
    floors: _containers.RepeatedCompositeFieldContainer[Floor]
    dualAuthApprovalGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    alarms: _containers.RepeatedCompositeFieldContainer[Alarm]
    alarmFlags: int
    tamper: Alarm
    tamperOn: bool
    def __init__(self, liftID: _Optional[int] = ..., name: _Optional[str] = ..., deviceIDs: _Optional[_Iterable[int]] = ..., activateTimeout: _Optional[int] = ..., dualAuthTimeout: _Optional[int] = ..., dualAuthApproval: _Optional[_Union[DualAuthApprovalType, str]] = ..., dualAuthRequiredDeviceIDs: _Optional[_Iterable[int]] = ..., dualAuthScheduleID: _Optional[int] = ..., floors: _Optional[_Iterable[_Union[Floor, _Mapping]]] = ..., dualAuthApprovalGroupIDs: _Optional[_Iterable[int]] = ..., alarms: _Optional[_Iterable[_Union[Alarm, _Mapping]]] = ..., alarmFlags: _Optional[int] = ..., tamper: _Optional[_Union[Alarm, _Mapping]] = ..., tamperOn: bool = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("lifts",)
    LIFTS_FIELD_NUMBER: _ClassVar[int]
    lifts: _containers.RepeatedCompositeFieldContainer[LiftInfo]
    def __init__(self, lifts: _Optional[_Iterable[_Union[LiftInfo, _Mapping]]] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetStatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[Status]
    def __init__(self, status: _Optional[_Iterable[_Union[Status, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("deviceID", "lifts")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    lifts: _containers.RepeatedCompositeFieldContainer[LiftInfo]
    def __init__(self, deviceID: _Optional[int] = ..., lifts: _Optional[_Iterable[_Union[LiftInfo, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "liftIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    liftIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., liftIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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

class ActivateRequest(_message.Message):
    __slots__ = ("deviceID", "liftID", "floorIndexes", "activateFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEXES_FIELD_NUMBER: _ClassVar[int]
    ACTIVATEFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    liftID: int
    floorIndexes: _containers.RepeatedScalarFieldContainer[int]
    activateFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., liftID: _Optional[int] = ..., floorIndexes: _Optional[_Iterable[int]] = ..., activateFlag: _Optional[int] = ...) -> None: ...

class ActivateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeactivateRequest(_message.Message):
    __slots__ = ("deviceID", "liftID", "floorIndexes", "deactivateFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEXES_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATEFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    liftID: int
    floorIndexes: _containers.RepeatedScalarFieldContainer[int]
    deactivateFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., liftID: _Optional[int] = ..., floorIndexes: _Optional[_Iterable[int]] = ..., deactivateFlag: _Optional[int] = ...) -> None: ...

class DeactivateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseRequest(_message.Message):
    __slots__ = ("deviceID", "liftID", "floorIndexes", "floorFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEXES_FIELD_NUMBER: _ClassVar[int]
    FLOORFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    liftID: int
    floorIndexes: _containers.RepeatedScalarFieldContainer[int]
    floorFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., liftID: _Optional[int] = ..., floorIndexes: _Optional[_Iterable[int]] = ..., floorFlag: _Optional[int] = ...) -> None: ...

class ReleaseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAlarmRequest(_message.Message):
    __slots__ = ("deviceID", "liftIDs", "alarmFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    LIFTIDS_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    liftIDs: _containers.RepeatedScalarFieldContainer[int]
    alarmFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., liftIDs: _Optional[_Iterable[int]] = ..., alarmFlag: _Optional[int] = ...) -> None: ...

class SetAlarmResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
