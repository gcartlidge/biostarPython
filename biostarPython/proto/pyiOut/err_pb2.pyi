from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorResponse(_message.Message):
    __slots__ = ("deviceID", "code", "msg")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    code: int
    msg: str
    def __init__(self, deviceID: _Optional[int] = ..., code: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class MultiErrorResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[ErrorResponse, _Mapping]]] = ...) -> None: ...

class GatewayErrorResponse(_message.Message):
    __slots__ = ("gatewayID", "code", "msg")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    code: int
    msg: str
    def __init__(self, gatewayID: _Optional[str] = ..., code: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...
