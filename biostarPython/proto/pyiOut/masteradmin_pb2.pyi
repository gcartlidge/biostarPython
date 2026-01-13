import user_pb2 as _user_pb2
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
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    MAX_NUM_OF_CARD_PER_MASTERADMIN: _ClassVar[Enum]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
MAX_NUM_OF_CARD_PER_MASTERADMIN: Enum

class GetRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("masterAdmin",)
    MASTERADMIN_FIELD_NUMBER: _ClassVar[int]
    masterAdmin: _user_pb2.UserInfo
    def __init__(self, masterAdmin: _Optional[_Union[_user_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class SetRequest(_message.Message):
    __slots__ = ("deviceID", "masterAdmin")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    MASTERADMIN_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    masterAdmin: _user_pb2.UserInfo
    def __init__(self, deviceID: _Optional[int] = ..., masterAdmin: _Optional[_Union[_user_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class SetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "masterAdmin")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    MASTERADMIN_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    masterAdmin: _user_pb2.UserInfo
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., masterAdmin: _Optional[_Union[_user_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class SetMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
