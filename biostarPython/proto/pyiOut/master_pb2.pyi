from google.protobuf import any_pb2 as _any_pb2
import event_pb2 as _event_pb2
import err_pb2 as _err_pb2
import connect_pb2 as _connect_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscribeRequest(_message.Message):
    __slots__ = ("gatewayCert",)
    GATEWAYCERT_FIELD_NUMBER: _ClassVar[int]
    gatewayCert: str
    def __init__(self, gatewayCert: _Optional[str] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ("sessionID",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionID: int
    def __init__(self, sessionID: _Optional[int] = ...) -> None: ...

class UpdateDeviceListRequest(_message.Message):
    __slots__ = ("sessionID", "deviceIDs")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    sessionID: int
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sessionID: _Optional[int] = ..., deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateDeviceListResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommandRequest(_message.Message):
    __slots__ = ("requestType", "requestID", "deviceIDs", "request")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CMD_WRAPPER: _ClassVar[CommandRequest.RequestType]
        INIT_CHAN: _ClassVar[CommandRequest.RequestType]
    CMD_WRAPPER: CommandRequest.RequestType
    INIT_CHAN: CommandRequest.RequestType
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    requestType: CommandRequest.RequestType
    requestID: int
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    request: _any_pb2.Any
    def __init__(self, requestType: _Optional[_Union[CommandRequest.RequestType, str]] = ..., requestID: _Optional[int] = ..., deviceIDs: _Optional[_Iterable[int]] = ..., request: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class CommandResponse(_message.Message):
    __slots__ = ("sessionID", "requestID", "response")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    sessionID: int
    requestID: int
    response: _any_pb2.Any
    def __init__(self, sessionID: _Optional[int] = ..., requestID: _Optional[int] = ..., response: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class ErrorResponse(_message.Message):
    __slots__ = ("code", "msg", "deviceErrors")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    code: int
    msg: str
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, code: _Optional[int] = ..., msg: _Optional[str] = ..., deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class InitLogChanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RealtimeEvent(_message.Message):
    __slots__ = ("masterChanID", "event")
    MASTERCHANID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    masterChanID: str
    event: _event_pb2.EventLog
    def __init__(self, masterChanID: _Optional[str] = ..., event: _Optional[_Union[_event_pb2.EventLog, _Mapping]] = ...) -> None: ...

class InitDeviceStatusChanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceStatus(_message.Message):
    __slots__ = ("masterChanID", "status")
    MASTERCHANID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    masterChanID: str
    status: _connect_pb2.StatusChange
    def __init__(self, masterChanID: _Optional[str] = ..., status: _Optional[_Union[_connect_pb2.StatusChange, _Mapping]] = ...) -> None: ...
