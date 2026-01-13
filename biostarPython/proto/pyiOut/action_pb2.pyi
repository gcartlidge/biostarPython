import device_pb2 as _device_pb2
import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPEAT_INFINITELY: _ClassVar[Enum]
    DEFAULT_SIGNAL_DURATION: _ClassVar[Enum]
    DEFAULT_SIGNAL_DELAY: _ClassVar[Enum]
    MAX_SIGNALS: _ClassVar[Enum]
    MAX_TRIGGER_ACTIONS: _ClassVar[Enum]

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_NONE: _ClassVar[TriggerType]
    TRIGGER_EVENT: _ClassVar[TriggerType]
    TRIGGER_INPUT: _ClassVar[TriggerType]
    TRIGGER_SCHEDULE: _ClassVar[TriggerType]

class ScheduleTriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEDULE_TRIGGER_ON_START: _ClassVar[ScheduleTriggerType]
    SCHEDULE_TRIGGER_ON_END: _ClassVar[ScheduleTriggerType]

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_NONE: _ClassVar[ActionType]
    ACTION_LOCK_DEVICE: _ClassVar[ActionType]
    ACTION_UNLOCK_DEVICE: _ClassVar[ActionType]
    ACTION_REBOOT_DEVICE: _ClassVar[ActionType]
    ACTION_RELEASE_ALARM: _ClassVar[ActionType]
    ACTION_GENERAL_INPUT: _ClassVar[ActionType]
    ACTION_RELAY: _ClassVar[ActionType]
    ACTION_TTL: _ClassVar[ActionType]
    ACTION_SOUND: _ClassVar[ActionType]
    ACTION_DISPLAY: _ClassVar[ActionType]
    ACTION_BUZZER: _ClassVar[ActionType]
    ACTION_LED: _ClassVar[ActionType]
    ACTION_FIRE_ALARM_INPUT: _ClassVar[ActionType]
    ACTION_AUTH_SUCCESS: _ClassVar[ActionType]
    ACTION_AUTH_FAIL: _ClassVar[ActionType]
    ACTION_LIFT: _ClassVar[ActionType]

class StopFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_NONE: _ClassVar[StopFlag]
    STOP_ON_DOOR_CLOSED: _ClassVar[StopFlag]
    STOP_BY_CMD_RUN_ACTION: _ClassVar[StopFlag]

class LiftActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFT_ACTION_ACTIVATE_FLOORS: _ClassVar[LiftActionType]
    LIFT_ACTION_DEACTIVATE_FLOORS: _ClassVar[LiftActionType]
    LIFT_ACTION_RELEASE_FLOORS: _ClassVar[LiftActionType]
REPEAT_INFINITELY: Enum
DEFAULT_SIGNAL_DURATION: Enum
DEFAULT_SIGNAL_DELAY: Enum
MAX_SIGNALS: Enum
MAX_TRIGGER_ACTIONS: Enum
TRIGGER_NONE: TriggerType
TRIGGER_EVENT: TriggerType
TRIGGER_INPUT: TriggerType
TRIGGER_SCHEDULE: TriggerType
SCHEDULE_TRIGGER_ON_START: ScheduleTriggerType
SCHEDULE_TRIGGER_ON_END: ScheduleTriggerType
ACTION_NONE: ActionType
ACTION_LOCK_DEVICE: ActionType
ACTION_UNLOCK_DEVICE: ActionType
ACTION_REBOOT_DEVICE: ActionType
ACTION_RELEASE_ALARM: ActionType
ACTION_GENERAL_INPUT: ActionType
ACTION_RELAY: ActionType
ACTION_TTL: ActionType
ACTION_SOUND: ActionType
ACTION_DISPLAY: ActionType
ACTION_BUZZER: ActionType
ACTION_LED: ActionType
ACTION_FIRE_ALARM_INPUT: ActionType
ACTION_AUTH_SUCCESS: ActionType
ACTION_AUTH_FAIL: ActionType
ACTION_LIFT: ActionType
STOP_NONE: StopFlag
STOP_ON_DOOR_CLOSED: StopFlag
STOP_BY_CMD_RUN_ACTION: StopFlag
LIFT_ACTION_ACTIVATE_FLOORS: LiftActionType
LIFT_ACTION_DEACTIVATE_FLOORS: LiftActionType
LIFT_ACTION_RELEASE_FLOORS: LiftActionType

class EventTrigger(_message.Message):
    __slots__ = ("eventCode",)
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    eventCode: int
    def __init__(self, eventCode: _Optional[int] = ...) -> None: ...

class InputTrigger(_message.Message):
    __slots__ = ("port", "switchType", "duration", "scheduleID")
    PORT_FIELD_NUMBER: _ClassVar[int]
    SWITCHTYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    port: int
    switchType: _device_pb2.SwitchType
    duration: int
    scheduleID: int
    def __init__(self, port: _Optional[int] = ..., switchType: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., duration: _Optional[int] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class ScheduleTrigger(_message.Message):
    __slots__ = ("type", "scheduleID")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    type: ScheduleTriggerType
    scheduleID: int
    def __init__(self, type: _Optional[_Union[ScheduleTriggerType, str]] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class Trigger(_message.Message):
    __slots__ = ("deviceID", "type", "ignoreSignalTime", "event", "input", "schedule")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IGNORESIGNALTIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: TriggerType
    ignoreSignalTime: int
    event: EventTrigger
    input: InputTrigger
    schedule: ScheduleTrigger
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[TriggerType, str]] = ..., ignoreSignalTime: _Optional[int] = ..., event: _Optional[_Union[EventTrigger, _Mapping]] = ..., input: _Optional[_Union[InputTrigger, _Mapping]] = ..., schedule: _Optional[_Union[ScheduleTrigger, _Mapping]] = ...) -> None: ...

class Signal(_message.Message):
    __slots__ = ("signalID", "count", "onDuration", "offDuration", "delay")
    SIGNALID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ONDURATION_FIELD_NUMBER: _ClassVar[int]
    OFFDURATION_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    signalID: int
    count: int
    onDuration: int
    offDuration: int
    delay: int
    def __init__(self, signalID: _Optional[int] = ..., count: _Optional[int] = ..., onDuration: _Optional[int] = ..., offDuration: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class OutputPortAction(_message.Message):
    __slots__ = ("portIndex", "signal")
    PORTINDEX_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    portIndex: int
    signal: Signal
    def __init__(self, portIndex: _Optional[int] = ..., signal: _Optional[_Union[Signal, _Mapping]] = ...) -> None: ...

class RelayAction(_message.Message):
    __slots__ = ("relayIndex", "signal")
    RELAYINDEX_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    relayIndex: int
    signal: Signal
    def __init__(self, relayIndex: _Optional[int] = ..., signal: _Optional[_Union[Signal, _Mapping]] = ...) -> None: ...

class LEDSignal(_message.Message):
    __slots__ = ("color", "duration", "delay")
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    color: _device_pb2.LEDColor
    duration: int
    delay: int
    def __init__(self, color: _Optional[_Union[_device_pb2.LEDColor, str]] = ..., duration: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class LEDAction(_message.Message):
    __slots__ = ("signals", "count")
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    signals: _containers.RepeatedCompositeFieldContainer[LEDSignal]
    count: int
    def __init__(self, signals: _Optional[_Iterable[_Union[LEDSignal, _Mapping]]] = ..., count: _Optional[int] = ...) -> None: ...

class BuzzerSignal(_message.Message):
    __slots__ = ("tone", "fadeout", "duration", "delay")
    TONE_FIELD_NUMBER: _ClassVar[int]
    FADEOUT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    tone: _device_pb2.BuzzerTone
    fadeout: bool
    duration: int
    delay: int
    def __init__(self, tone: _Optional[_Union[_device_pb2.BuzzerTone, str]] = ..., fadeout: bool = ..., duration: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class BuzzerAction(_message.Message):
    __slots__ = ("signals", "count")
    SIGNALS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    signals: _containers.RepeatedCompositeFieldContainer[BuzzerSignal]
    count: int
    def __init__(self, signals: _Optional[_Iterable[_Union[BuzzerSignal, _Mapping]]] = ..., count: _Optional[int] = ...) -> None: ...

class DisplayAction(_message.Message):
    __slots__ = ("duration", "displayID", "resourceID")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAYID_FIELD_NUMBER: _ClassVar[int]
    RESOURCEID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    displayID: int
    resourceID: int
    def __init__(self, duration: _Optional[int] = ..., displayID: _Optional[int] = ..., resourceID: _Optional[int] = ...) -> None: ...

class SoundAction(_message.Message):
    __slots__ = ("count", "soundIndex", "delay")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SOUNDINDEX_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    count: int
    soundIndex: int
    delay: int
    def __init__(self, count: _Optional[int] = ..., soundIndex: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class LiftAction(_message.Message):
    __slots__ = ("liftID", "type")
    LIFTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    liftID: int
    type: LiftActionType
    def __init__(self, liftID: _Optional[int] = ..., type: _Optional[_Union[LiftActionType, str]] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("deviceID", "type", "stopFlag", "delay", "relay", "outputPort", "display", "sound", "LED", "buzzer", "lift")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STOPFLAG_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    OUTPUTPORT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    LED_FIELD_NUMBER: _ClassVar[int]
    BUZZER_FIELD_NUMBER: _ClassVar[int]
    LIFT_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    type: ActionType
    stopFlag: StopFlag
    delay: int
    relay: RelayAction
    outputPort: OutputPortAction
    display: DisplayAction
    sound: SoundAction
    LED: LEDAction
    buzzer: BuzzerAction
    lift: LiftAction
    def __init__(self, deviceID: _Optional[int] = ..., type: _Optional[_Union[ActionType, str]] = ..., stopFlag: _Optional[_Union[StopFlag, str]] = ..., delay: _Optional[int] = ..., relay: _Optional[_Union[RelayAction, _Mapping]] = ..., outputPort: _Optional[_Union[OutputPortAction, _Mapping]] = ..., display: _Optional[_Union[DisplayAction, _Mapping]] = ..., sound: _Optional[_Union[SoundAction, _Mapping]] = ..., LED: _Optional[_Union[LEDAction, _Mapping]] = ..., buzzer: _Optional[_Union[BuzzerAction, _Mapping]] = ..., lift: _Optional[_Union[LiftAction, _Mapping]] = ...) -> None: ...

class TriggerActionConfig(_message.Message):
    __slots__ = ("triggerActions",)
    class TriggerAction(_message.Message):
        __slots__ = ("trigger", "action")
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        trigger: Trigger
        action: Action
        def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...
    TRIGGERACTIONS_FIELD_NUMBER: _ClassVar[int]
    triggerActions: _containers.RepeatedCompositeFieldContainer[TriggerActionConfig.TriggerAction]
    def __init__(self, triggerActions: _Optional[_Iterable[_Union[TriggerActionConfig.TriggerAction, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TriggerActionConfig
    def __init__(self, config: _Optional[_Union[TriggerActionConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: TriggerActionConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[TriggerActionConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: TriggerActionConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[TriggerActionConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class RunActionRequest(_message.Message):
    __slots__ = ("deviceID", "action")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    action: Action
    def __init__(self, deviceID: _Optional[int] = ..., action: _Optional[_Union[Action, _Mapping]] = ...) -> None: ...

class RunActionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
