import err_pb2 as _err_pb2
import tna_pb2 as _tna_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    MAX_EVENT_FILTERS: _ClassVar[Enum]

class PortValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPEN: _ClassVar[PortValue]
    CLOSED: _ClassVar[PortValue]
    SUPERVISED_SHORT: _ClassVar[PortValue]
    SUPERVISED_OPEN: _ClassVar[PortValue]

class ParamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TNA_KEY: _ClassVar[ParamType]
    ON_DEVICE: _ClassVar[ParamType]
    FLOOR_INDEX: _ClassVar[ParamType]
    ALARM_FLAG: _ClassVar[ParamType]
    LICENSE_TYPE: _ClassVar[ParamType]
    NONE: _ClassVar[ParamType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_EVENT_FILTERS: Enum
OPEN: PortValue
CLOSED: PortValue
SUPERVISED_SHORT: PortValue
SUPERVISED_OPEN: PortValue
TNA_KEY: ParamType
ON_DEVICE: ParamType
FLOOR_INDEX: ParamType
ALARM_FLAG: ParamType
LICENSE_TYPE: ParamType
NONE: ParamType

class DetectInputInfo(_message.Message):
    __slots__ = ("ioDeviceID", "port", "value")
    IODEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ioDeviceID: int
    port: int
    value: PortValue
    def __init__(self, ioDeviceID: _Optional[int] = ..., port: _Optional[int] = ..., value: _Optional[_Union[PortValue, str]] = ...) -> None: ...

class AlarmZoneInfo(_message.Message):
    __slots__ = ("zoneID", "doorID", "ioDeviceID", "port")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    DOORID_FIELD_NUMBER: _ClassVar[int]
    IODEVICEID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    doorID: int
    ioDeviceID: int
    port: int
    def __init__(self, zoneID: _Optional[int] = ..., doorID: _Optional[int] = ..., ioDeviceID: _Optional[int] = ..., port: _Optional[int] = ...) -> None: ...

class InterlockZoneInfo(_message.Message):
    __slots__ = ("zoneID", "doorIDs")
    ZONEID_FIELD_NUMBER: _ClassVar[int]
    DOORIDS_FIELD_NUMBER: _ClassVar[int]
    zoneID: int
    doorIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, zoneID: _Optional[int] = ..., doorIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class EventLog(_message.Message):
    __slots__ = ("ID", "timestamp", "deviceID", "userID", "entityID", "eventCode", "subCode", "TNAKey", "hasImage", "changedOnDevice", "temperature", "cardData", "inputInfo", "alarmZoneInfo", "interlockZoneInfo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SUBCODE_FIELD_NUMBER: _ClassVar[int]
    TNAKEY_FIELD_NUMBER: _ClassVar[int]
    HASIMAGE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDONDEVICE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    CARDDATA_FIELD_NUMBER: _ClassVar[int]
    INPUTINFO_FIELD_NUMBER: _ClassVar[int]
    ALARMZONEINFO_FIELD_NUMBER: _ClassVar[int]
    INTERLOCKZONEINFO_FIELD_NUMBER: _ClassVar[int]
    ID: int
    timestamp: int
    deviceID: int
    userID: str
    entityID: int
    eventCode: int
    subCode: int
    TNAKey: _tna_pb2.Key
    hasImage: bool
    changedOnDevice: bool
    temperature: int
    cardData: bytes
    inputInfo: DetectInputInfo
    alarmZoneInfo: AlarmZoneInfo
    interlockZoneInfo: InterlockZoneInfo
    def __init__(self, ID: _Optional[int] = ..., timestamp: _Optional[int] = ..., deviceID: _Optional[int] = ..., userID: _Optional[str] = ..., entityID: _Optional[int] = ..., eventCode: _Optional[int] = ..., subCode: _Optional[int] = ..., TNAKey: _Optional[_Union[_tna_pb2.Key, str]] = ..., hasImage: bool = ..., changedOnDevice: bool = ..., temperature: _Optional[int] = ..., cardData: _Optional[bytes] = ..., inputInfo: _Optional[_Union[DetectInputInfo, _Mapping]] = ..., alarmZoneInfo: _Optional[_Union[AlarmZoneInfo, _Mapping]] = ..., interlockZoneInfo: _Optional[_Union[InterlockZoneInfo, _Mapping]] = ...) -> None: ...

class EventFilter(_message.Message):
    __slots__ = ("userID", "startTime", "endTime", "eventCode", "TNAKey", "onDevice", "floorIndex", "alarmFlag", "licenseType")
    USERID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    TNAKEY_FIELD_NUMBER: _ClassVar[int]
    ONDEVICE_FIELD_NUMBER: _ClassVar[int]
    FLOORINDEX_FIELD_NUMBER: _ClassVar[int]
    ALARMFLAG_FIELD_NUMBER: _ClassVar[int]
    LICENSETYPE_FIELD_NUMBER: _ClassVar[int]
    userID: str
    startTime: int
    endTime: int
    eventCode: int
    TNAKey: _tna_pb2.Key
    onDevice: int
    floorIndex: int
    alarmFlag: int
    licenseType: int
    def __init__(self, userID: _Optional[str] = ..., startTime: _Optional[int] = ..., endTime: _Optional[int] = ..., eventCode: _Optional[int] = ..., TNAKey: _Optional[_Union[_tna_pb2.Key, str]] = ..., onDevice: _Optional[int] = ..., floorIndex: _Optional[int] = ..., alarmFlag: _Optional[int] = ..., licenseType: _Optional[int] = ...) -> None: ...

class EnableMonitoringRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class EnableMonitoringResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnableMonitoringMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class EnableMonitoringMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DisableMonitoringRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DisableMonitoringResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableMonitoringMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DisableMonitoringMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class SubscribeRealtimeLogRequest(_message.Message):
    __slots__ = ("queueSize", "deviceIDs", "eventCodes")
    QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    EVENTCODES_FIELD_NUMBER: _ClassVar[int]
    queueSize: int
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    eventCodes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, queueSize: _Optional[int] = ..., deviceIDs: _Optional[_Iterable[int]] = ..., eventCodes: _Optional[_Iterable[int]] = ...) -> None: ...

class SubscribeRealtimeLogResponse(_message.Message):
    __slots__ = ("logChanID",)
    LOGCHANID_FIELD_NUMBER: _ClassVar[int]
    logChanID: str
    def __init__(self, logChanID: _Optional[str] = ...) -> None: ...

class GetLogRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ...) -> None: ...

class GetLogResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EventLog]
    def __init__(self, events: _Optional[_Iterable[_Union[EventLog, _Mapping]]] = ...) -> None: ...

class GetLogWithFilterRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog", "filters")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    filters: _containers.RepeatedCompositeFieldContainer[EventFilter]
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[EventFilter, _Mapping]]] = ...) -> None: ...

class GetLogWithFilterResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EventLog]
    def __init__(self, events: _Optional[_Iterable[_Union[EventLog, _Mapping]]] = ...) -> None: ...

class ImageLog(_message.Message):
    __slots__ = ("ID", "timestamp", "deviceID", "userID", "eventCode", "subCode", "JPGImage")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SUBCODE_FIELD_NUMBER: _ClassVar[int]
    JPGIMAGE_FIELD_NUMBER: _ClassVar[int]
    ID: int
    timestamp: int
    deviceID: int
    userID: str
    eventCode: int
    subCode: int
    JPGImage: bytes
    def __init__(self, ID: _Optional[int] = ..., timestamp: _Optional[int] = ..., deviceID: _Optional[int] = ..., userID: _Optional[str] = ..., eventCode: _Optional[int] = ..., subCode: _Optional[int] = ..., JPGImage: _Optional[bytes] = ...) -> None: ...

class GetImageLogRequest(_message.Message):
    __slots__ = ("deviceID", "startEventID", "maxNumOfLog")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    STARTEVENTID_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFLOG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    startEventID: int
    maxNumOfLog: int
    def __init__(self, deviceID: _Optional[int] = ..., startEventID: _Optional[int] = ..., maxNumOfLog: _Optional[int] = ...) -> None: ...

class GetImageLogResponse(_message.Message):
    __slots__ = ("imageEvents",)
    IMAGEEVENTS_FIELD_NUMBER: _ClassVar[int]
    imageEvents: _containers.RepeatedCompositeFieldContainer[ImageLog]
    def __init__(self, imageEvents: _Optional[_Iterable[_Union[ImageLog, _Mapping]]] = ...) -> None: ...

class ImageFilter(_message.Message):
    __slots__ = ("eventCode", "scheduleID")
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULEID_FIELD_NUMBER: _ClassVar[int]
    eventCode: int
    scheduleID: int
    def __init__(self, eventCode: _Optional[int] = ..., scheduleID: _Optional[int] = ...) -> None: ...

class GetImageFilterRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetImageFilterResponse(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[ImageFilter]
    def __init__(self, filters: _Optional[_Iterable[_Union[ImageFilter, _Mapping]]] = ...) -> None: ...

class SetImageFilterRequest(_message.Message):
    __slots__ = ("deviceID", "filters")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    filters: _containers.RepeatedCompositeFieldContainer[ImageFilter]
    def __init__(self, deviceID: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[ImageFilter, _Mapping]]] = ...) -> None: ...

class SetImageFilterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetImageFilterMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "filters")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    filters: _containers.RepeatedCompositeFieldContainer[ImageFilter]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., filters: _Optional[_Iterable[_Union[ImageFilter, _Mapping]]] = ...) -> None: ...

class SetImageFilterMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class ClearLogRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class ClearLogResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearLogMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ClearLogMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
