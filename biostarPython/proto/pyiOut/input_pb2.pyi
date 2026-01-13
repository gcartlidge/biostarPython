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
    INPUT_TYPE_NORMAL: _ClassVar[Enum]
    INPUT_TYPE_SUPERVISED: _ClassVar[Enum]
    MAX_NUM_OF_INPUT: _ClassVar[Enum]
    MAX_NUM_OF_INPUT_EX: _ClassVar[Enum]

class SupervisedResistanceValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUPERVISED_REG_1K: _ClassVar[SupervisedResistanceValue]
    SUPERVISED_REG_2_2K: _ClassVar[SupervisedResistanceValue]
    SUPERVISED_REG_4_7K: _ClassVar[SupervisedResistanceValue]
    SUPERVISED_REG_10K: _ClassVar[SupervisedResistanceValue]
    SUPERVISED_REG_UNUSED: _ClassVar[SupervisedResistanceValue]
    SUPERVISED_REG_CUSTOM: _ClassVar[SupervisedResistanceValue]

class AuxInputPort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUX_INPUT_PORT_NORMAL: _ClassVar[AuxInputPort]
    AUX_INPUT_PORT_0: _ClassVar[AuxInputPort]
    AUX_INPUT_PORT_1: _ClassVar[AuxInputPort]
    AUX_INPUT_PORT_2: _ClassVar[AuxInputPort]
INPUT_TYPE_NORMAL: Enum
INPUT_TYPE_SUPERVISED: Enum
MAX_NUM_OF_INPUT: Enum
MAX_NUM_OF_INPUT_EX: Enum
SUPERVISED_REG_1K: SupervisedResistanceValue
SUPERVISED_REG_2_2K: SupervisedResistanceValue
SUPERVISED_REG_4_7K: SupervisedResistanceValue
SUPERVISED_REG_10K: SupervisedResistanceValue
SUPERVISED_REG_UNUSED: SupervisedResistanceValue
SUPERVISED_REG_CUSTOM: SupervisedResistanceValue
AUX_INPUT_PORT_NORMAL: AuxInputPort
AUX_INPUT_PORT_0: AuxInputPort
AUX_INPUT_PORT_1: AuxInputPort
AUX_INPUT_PORT_2: AuxInputPort

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
    __slots__ = ("portIndex", "type", "duration", "resistance", "config")
    PORTINDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RESISTANCE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    portIndex: int
    type: _device_pb2.SwitchType
    duration: int
    resistance: SupervisedResistanceValue
    config: SupervisedInputConfig
    def __init__(self, portIndex: _Optional[int] = ..., type: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., duration: _Optional[int] = ..., resistance: _Optional[_Union[SupervisedResistanceValue, str]] = ..., config: _Optional[_Union[SupervisedInputConfig, _Mapping]] = ...) -> None: ...

class AuxInput(_message.Message):
    __slots__ = ("acFail", "typeAux0", "tamper", "typeAux1", "fire", "typeAux2")
    ACFAIL_FIELD_NUMBER: _ClassVar[int]
    TYPEAUX0_FIELD_NUMBER: _ClassVar[int]
    TAMPER_FIELD_NUMBER: _ClassVar[int]
    TYPEAUX1_FIELD_NUMBER: _ClassVar[int]
    FIRE_FIELD_NUMBER: _ClassVar[int]
    TYPEAUX2_FIELD_NUMBER: _ClassVar[int]
    acFail: AuxInputPort
    typeAux0: _device_pb2.SwitchType
    tamper: AuxInputPort
    typeAux1: _device_pb2.SwitchType
    fire: AuxInputPort
    typeAux2: _device_pb2.SwitchType
    def __init__(self, acFail: _Optional[_Union[AuxInputPort, str]] = ..., typeAux0: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., tamper: _Optional[_Union[AuxInputPort, str]] = ..., typeAux1: _Optional[_Union[_device_pb2.SwitchType, str]] = ..., fire: _Optional[_Union[AuxInputPort, str]] = ..., typeAux2: _Optional[_Union[_device_pb2.SwitchType, str]] = ...) -> None: ...

class InputConfig(_message.Message):
    __slots__ = ("numOfInput", "numOfSupervisedInput", "auxInput", "supervisedInputs")
    NUMOFINPUT_FIELD_NUMBER: _ClassVar[int]
    NUMOFSUPERVISEDINPUT_FIELD_NUMBER: _ClassVar[int]
    AUXINPUT_FIELD_NUMBER: _ClassVar[int]
    SUPERVISEDINPUTS_FIELD_NUMBER: _ClassVar[int]
    numOfInput: int
    numOfSupervisedInput: int
    auxInput: AuxInput
    supervisedInputs: _containers.RepeatedCompositeFieldContainer[SupervisedInput]
    def __init__(self, numOfInput: _Optional[int] = ..., numOfSupervisedInput: _Optional[int] = ..., auxInput: _Optional[_Union[AuxInput, _Mapping]] = ..., supervisedInputs: _Optional[_Iterable[_Union[SupervisedInput, _Mapping]]] = ...) -> None: ...

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
