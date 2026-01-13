import err_pb2 as _err_pb2
import auth_pb2 as _auth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetListRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("operators",)
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    operators: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Operator]
    def __init__(self, operators: _Optional[_Iterable[_Union[_auth_pb2.Operator, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("deviceID", "operators")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    operators: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Operator]
    def __init__(self, deviceID: _Optional[int] = ..., operators: _Optional[_Iterable[_Union[_auth_pb2.Operator, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "operators")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    operators: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Operator]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., operators: _Optional[_Iterable[_Union[_auth_pb2.Operator, _Mapping]]] = ...) -> None: ...

class AddMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("deviceID", "operatorIDs")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    OPERATORIDS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    operatorIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceID: _Optional[int] = ..., operatorIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "operatorIDs")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    OPERATORIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    operatorIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., operatorIDs: _Optional[_Iterable[str]] = ...) -> None: ...

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
