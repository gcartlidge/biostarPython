import device_pb2 as _device_pb2
import action_pb2 as _action_pb2
import apb_zone_pb2 as _apb_zone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoorFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[DoorFlag]
    SCHEDULED: _ClassVar[DoorFlag]
    EMERGENCY: _ClassVar[DoorFlag]
    OPERATOR: _ClassVar[DoorFlag]

class AlarmFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_ALARM: _ClassVar[AlarmFlag]
    FORCED_OPEN: _ClassVar[AlarmFlag]
    HELD_OPEN: _ClassVar[AlarmFlag]
    APB_VIOLATION: _ClassVar[AlarmFlag]

class DualAuthDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUAL_AUTH_NO_DEVICE: _ClassVar[DualAuthDevice]
    DUAL_AUTH_ENTRY_DEVICE_ONLY: _ClassVar[DualAuthDevice]
    DUAL_AUTH_EXIT_DEVICE_ONLY: _ClassVar[DualAuthDevice]
    DUAL_AUTH_BOTH_DEVICE: _ClassVar[DualAuthDevice]

class DualAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUAL_AUTH_NONE: _ClassVar[DualAuthType]
    DUAL_AUTH_LAST: _ClassVar[DualAuthType]

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    DEFAULT_AUTO_LOCK_TIMEOUT: _ClassVar[Enum]
    DEFAULT_HELD_OPEN_TIMEOUT: _ClassVar[Enum]
    DEFAULT_DUAL_AUTH_TIMEOUT: _ClassVar[Enum]
    MAX_FORCED_OPEN_ALARMS: _ClassVar[Enum]
    MAX_HELD_OPEN_ALARMS: _ClassVar[Enum]
    MAX_DUAL_AUTH_APPROVAL_GROUPS: _ClassVar[Enum]
    MAX_NAME_LENGTH: _ClassVar[Enum]
    DOOR_LOCK_NORMALIZE_TIMER_INFINIT: _ClassVar[Enum]
    DOOR_LOCK_NORMALIZE_TIMER_MAX: _ClassVar[Enum]
    DOOR_UNLOCK_NORMALIZE_TIMER_INFINIT: _ClassVar[Enum]
    DOOR_UNLOCK_NORMALIZE_TIMER_MAX: _ClassVar[Enum]
    DEFAULT_EXTENDED_DOOR_OPEN_TIME: _ClassVar[Enum]
NONE: DoorFlag
SCHEDULED: DoorFlag
EMERGENCY: DoorFlag
OPERATOR: DoorFlag
NO_ALARM: AlarmFlag
FORCED_OPEN: AlarmFlag
HELD_OPEN: AlarmFlag
APB_VIOLATION: AlarmFlag
DUAL_AUTH_NO_DEVICE: DualAuthDevice
DUAL_AUTH_ENTRY_DEVICE_ONLY: DualAuthDevice
DUAL_AUTH_EXIT_DEVICE_ONLY: DualAuthDevice
DUAL_AUTH_BOTH_DEVICE: DualAuthDevice
DUAL_AUTH_NONE: DualAuthType
DUAL_AUTH_LAST: DualAuthType
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_AUTO_LOCK_TIMEOUT: Enum
DEFAULT_HELD_OPEN_TIMEOUT: Enum
DEFAULT_DUAL_AUTH_TIMEOUT: Enum
MAX_FORCED_OPEN_ALARMS: Enum
MAX_HELD_OPEN_ALARMS: Enum
MAX_DUAL_AUTH_APPROVAL_GROUPS: Enum
MAX_NAME_LENGTH: Enum
DOOR_LOCK_NORMALIZE_TIMER_INFINIT: Enum
DOOR_LOCK_NORMALIZE_TIMER_MAX: Enum
DOOR_UNLOCK_NORMALIZE_TIMER_INFINIT: Enum
DOOR_UNLOCK_NORMALIZE_TIMER_MAX: Enum
DEFAULT_EXTENDED_DOOR_OPEN_TIME: Enum

class Relay(_message.Message):
    __slots__ = ("deviceID", "port")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ...) -> None: ...

class Sensor(_message.Message):
    __slots__ = ("deviceID", "port", "type", "apbUseDoorSensor")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APBUSEDOORSENSOR_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    type: _device_pb2.SwitchType
    apbUseDoorSensor: bool
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., apbUseDoorSensor: bool = ...) -> None: ...

class ExitButton(_message.Message):
    __slots__ = ("deviceID", "port", "type")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    port: int
    type: _device_pb2.SwitchType
    def __init__(self, deviceID: _Optional[int] = ..., port: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.SwitchType, str]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("doorID", "isOpen", "isUnlocked", "heldOpen", "unlockFlags", "lockFlags", "alarmFlags", "lastOpenTime")
    DOORID_FIELD_NUMBER: _ClassVar[int]
    ISOPEN_FIELD_NUMBER: _ClassVar[int]
    ISUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    HELDOPEN_FIELD_NUMBER: _ClassVar[int]
    UNLOCKFLAGS_FIELD_NUMBER: _ClassVar[int]
    LOCKFLAGS_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAGS_FIELD_NUMBER: _ClassVar[int]
    LASTOPENTIME_FIELD_NUMBER: _ClassVar[int]
    doorID: int
    isOpen: bool
    isUnlocked: bool
    heldOpen: bool
    unlockFlags: int
    lockFlags: int
    alarmFlags: int
    lastOpenTime: int
    def __init__(self, doorID: _Optional[int] = ..., isOpen: bool = ..., isUnlocked: bool = ..., heldOpen: bool = ..., unlockFlags: _Optional[int] = ..., lockFlags: _Optional[int] = ..., alarmFlags: _Optional[int] = ..., lastOpenTime: _Optional[int] = ...) -> None: ...

class DoorInfo(_message.Message):
    __slots__ = ("doorID", "name", "entryDeviceID", "exitDeviceID", "relay", "sensor", "button", "autoLockTimeout", "heldOpenTimeout", "instantLock", "unlockFlags", "lockFlags", "unconditionalLock", "forcedOpenActions", "heldOpenActions", "dualAuthScheduleID", "dualAuthDevice", "dualAuthType", "dualAuthTimeout", "dualAuthGroupIDs", "apbZone", "extendedDoorOpenTime")
    DOORID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRYDEVICEID_FIELD_NUMBER: _ClassVar[int]
    EXITDEVICEID_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    AUTOLOCKTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HELDOPENTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    INSTANTLOCK_FIELD_NUMBER: _ClassVar[int]
    UNLOCKFLAGS_FIELD_NUMBER: _ClassVar[int]
    LOCKFLAGS_FIELD_NUMBER: _ClassVar[int]
    UNCONDITIONALLOCK_FIELD_NUMBER: _ClassVar[int]
    FORCEDOPENACTIONS_FIELD_NUMBER: _ClassVar[int]
    HELDOPENACTIONS_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHSCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHDEVICE_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DUALAUTHGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    APBZONE_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDDOOROPENTIME_FIELD_NUMBER: _ClassVar[int]
    doorID: int
    name: str
    entryDeviceID: int
    exitDeviceID: int
    relay: Relay
    sensor: Sensor
    button: ExitButton
    autoLockTimeout: int
    heldOpenTimeout: int
    instantLock: bool
    unlockFlags: int
    lockFlags: int
    unconditionalLock: bool
    forcedOpenActions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    heldOpenActions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    dualAuthScheduleID: int
    dualAuthDevice: DualAuthDevice
    dualAuthType: DualAuthType
    dualAuthTimeout: int
    dualAuthGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    apbZone: _apb_zone_pb2.ZoneInfo
    extendedDoorOpenTime: int
    def __init__(self, doorID: _Optional[int] = ..., name: _Optional[str] = ..., entryDeviceID: _Optional[int] = ..., exitDeviceID: _Optional[int] = ..., relay: _Optional[_Union[Relay, _Mapping]] = ..., sensor: _Optional[_Union[Sensor, _Mapping]] = ..., button: _Optional[_Union[ExitButton, _Mapping]] = ..., autoLockTimeout: _Optional[int] = ..., heldOpenTimeout: _Optional[int] = ..., instantLock: bool = ..., unlockFlags: _Optional[int] = ..., lockFlags: _Optional[int] = ..., unconditionalLock: bool = ..., forcedOpenActions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., heldOpenActions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., dualAuthScheduleID: _Optional[int] = ..., dualAuthDevice: _Optional[_Union[DualAuthDevice, str]] = ..., dualAuthType: _Optional[_Union[DualAuthType, str]] = ..., dualAuthTimeout: _Optional[int] = ..., dualAuthGroupIDs: _Optional[_Iterable[int]] = ..., apbZone: _Optional[_Union[_apb_zone_pb2.ZoneInfo, _Mapping]] = ..., extendedDoorOpenTime: _Optional[int] = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("doors",)
    DOORS_FIELD_NUMBER: _ClassVar[int]
    doors: _containers.RepeatedCompositeFieldContainer[DoorInfo]
    def __init__(self, doors: _Optional[_Iterable[_Union[DoorInfo, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ("deviceID", "doors")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doors: _containers.RepeatedCompositeFieldContainer[DoorInfo]
    def __init__(self, deviceID: _Optional[int] = ..., doors: _Optional[_Iterable[_Union[DoorInfo, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "doorIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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

class LockRequest(_message.Message):
    __slots__ = ("deviceID", "doorIDs", "doorFlag", "normalizeTimer")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    DOORFLAG_FIELD_NUMBER: _ClassVar[int]
    NORMALIZETIMER_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    doorFlag: int
    normalizeTimer: int
    def __init__(self, deviceID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ..., doorFlag: _Optional[int] = ..., normalizeTimer: _Optional[int] = ...) -> None: ...

class LockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockRequest(_message.Message):
    __slots__ = ("deviceID", "doorIDs", "doorFlag", "normalizeTimer")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    DOORFLAG_FIELD_NUMBER: _ClassVar[int]
    NORMALIZETIMER_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    doorFlag: int
    normalizeTimer: int
    def __init__(self, deviceID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ..., doorFlag: _Optional[int] = ..., normalizeTimer: _Optional[int] = ...) -> None: ...

class UnlockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseRequest(_message.Message):
    __slots__ = ("deviceID", "doorIDs", "doorFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    DOORFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    doorFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ..., doorFlag: _Optional[int] = ...) -> None: ...

class ReleaseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAlarmRequest(_message.Message):
    __slots__ = ("deviceID", "doorIDs", "alarmFlag")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    alarmFlag: int
    def __init__(self, deviceID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ..., alarmFlag: _Optional[int] = ...) -> None: ...

class SetAlarmResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
