import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupervisedRegistanceValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUPERVISED_REG_1K: _ClassVar[SupervisedRegistanceValue]
    SUPERVISED_REG_2_2K: _ClassVar[SupervisedRegistanceValue]
    SUPERVISED_REG_4_7K: _ClassVar[SupervisedRegistanceValue]
    SUPERVISED_REG_10K: _ClassVar[SupervisedRegistanceValue]
    SUPERVISED_REG_CUSTOM: _ClassVar[SupervisedRegistanceValue]
SUPERVISED_REG_1K: SupervisedRegistanceValue
SUPERVISED_REG_2_2K: SupervisedRegistanceValue
SUPERVISED_REG_4_7K: SupervisedRegistanceValue
SUPERVISED_REG_10K: SupervisedRegistanceValue
SUPERVISED_REG_CUSTOM: SupervisedRegistanceValue

class SupervisedInputRange(_message.Message):
    __slots__ = ("MinValue", "MaxValue")
    MINVALUE_FIELD_NUMBER: _ClassVar[int]
    MAXVALUE_FIELD_NUMBER: _ClassVar[int]
    MinValue: int
    MaxValue: int
    def __init__(self, MinValue: _Optional[int] = ..., MaxValue: _Optional[int] = ...) -> None: ...

class SupervisedInputConfig(_message.Message):
    __slots__ = ("short", "open", "on", "off")
    SHORT_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    ON_FIELD_NUMBER: _ClassVar[int]
    OFF_FIELD_NUMBER: _ClassVar[int]
    short: SupervisedInputRange
    open: SupervisedInputRange
    on: SupervisedInputRange
    off: SupervisedInputRange
    def __init__(self, short: _Optional[_Union[SupervisedInputRange, _Mapping]] = ..., open: _Optional[_Union[SupervisedInputRange, _Mapping]] = ..., on: _Optional[_Union[SupervisedInputRange, _Mapping]] = ..., off: _Optional[_Union[SupervisedInputRange, _Mapping]] = ...) -> None: ...

class SupervisedInput(_message.Message):
    __slots__ = ("portIndex", "registance", "config")
    PORTINDEX_FIELD_NUMBER: _ClassVar[int]
    REGISTANCE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    portIndex: int
    registance: SupervisedRegistanceValue
    config: SupervisedInputConfig
    def __init__(self, portIndex: _Optional[int] = ..., registance: _Optional[_Union[SupervisedRegistanceValue, str]] = ..., config: _Optional[_Union[SupervisedInputConfig, _Mapping]] = ...) -> None: ...

class InputConfig(_message.Message):
    __slots__ = ("numOfInput", "numOfSupervisedInput", "supervisedInputs")
    NUMOFINPUT_FIELD_NUMBER: _ClassVar[int]
    NUMOFSUPERVISEDINPUT_FIELD_NUMBER: _ClassVar[int]
    SUPERVISEDINPUTS_FIELD_NUMBER: _ClassVar[int]
    numOfInput: int
    numOfSupervisedInput: int
    supervisedInputs: _containers.RepeatedCompositeFieldContainer[SupervisedInput]
    def __init__(self, numOfInput: _Optional[int] = ..., numOfSupervisedInput: _Optional[int] = ..., supervisedInputs: _Optional[_Iterable[_Union[SupervisedInput, _Mapping]]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: InputConfig
    def __init__(self, config: _Optional[_Union[InputConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: InputConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[InputConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: InputConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[InputConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
