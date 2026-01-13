import cert_pb2 as _cert_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISCONNECTED: _ClassVar[Status]
    CONNECTED: _ClassVar[Status]
DISCONNECTED: Status
CONNECTED: Status

class GatewayInfo(_message.Message):
    __slots__ = ("gatewayID", "deviceIDs", "isConnected")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    ISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    isConnected: bool
    def __init__(self, gatewayID: _Optional[str] = ..., deviceIDs: _Optional[_Iterable[int]] = ..., isConnected: bool = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("gatewayInfos",)
    GATEWAYINFOS_FIELD_NUMBER: _ClassVar[int]
    gatewayInfos: _containers.RepeatedCompositeFieldContainer[GatewayInfo]
    def __init__(self, gatewayInfos: _Optional[_Iterable[_Union[GatewayInfo, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCertificateRequest(_message.Message):
    __slots__ = ("gatewayID", "subject", "expireAfterYears")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EXPIREAFTERYEARS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    subject: _cert_pb2.PKIName
    expireAfterYears: int
    def __init__(self, gatewayID: _Optional[str] = ..., subject: _Optional[_Union[_cert_pb2.PKIName, _Mapping]] = ..., expireAfterYears: _Optional[int] = ...) -> None: ...

class CreateCertificateResponse(_message.Message):
    __slots__ = ("gatewayCert", "gatewayKey")
    GATEWAYCERT_FIELD_NUMBER: _ClassVar[int]
    GATEWAYKEY_FIELD_NUMBER: _ClassVar[int]
    gatewayCert: str
    gatewayKey: str
    def __init__(self, gatewayCert: _Optional[str] = ..., gatewayKey: _Optional[str] = ...) -> None: ...

class GetIssuanceHistoryRequest(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class CertificateInfo(_message.Message):
    __slots__ = ("gatewayID", "subject", "serialNO", "issueDate", "expiryDate", "blacklisted")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SERIALNO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRYDATE_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    subject: _cert_pb2.PKIName
    serialNO: int
    issueDate: int
    expiryDate: int
    blacklisted: bool
    def __init__(self, gatewayID: _Optional[str] = ..., subject: _Optional[_Union[_cert_pb2.PKIName, _Mapping]] = ..., serialNO: _Optional[int] = ..., issueDate: _Optional[int] = ..., expiryDate: _Optional[int] = ..., blacklisted: bool = ...) -> None: ...

class GetIssuanceHistoryResponse(_message.Message):
    __slots__ = ("certInfos",)
    CERTINFOS_FIELD_NUMBER: _ClassVar[int]
    certInfos: _containers.RepeatedCompositeFieldContainer[CertificateInfo]
    def __init__(self, certInfos: _Optional[_Iterable[_Union[CertificateInfo, _Mapping]]] = ...) -> None: ...

class GetCertificateBlacklistRequest(_message.Message):
    __slots__ = ("gatewayIDs",)
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCertificateBlacklistResponse(_message.Message):
    __slots__ = ("certInfos",)
    CERTINFOS_FIELD_NUMBER: _ClassVar[int]
    certInfos: _containers.RepeatedCompositeFieldContainer[CertificateInfo]
    def __init__(self, certInfos: _Optional[_Iterable[_Union[CertificateInfo, _Mapping]]] = ...) -> None: ...

class AddCertificateBlacklistRequest(_message.Message):
    __slots__ = ("gatewayID", "serialNOs")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SERIALNOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    serialNOs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gatewayID: _Optional[str] = ..., serialNOs: _Optional[_Iterable[int]] = ...) -> None: ...

class AddCertificateBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCertificateBlacklistRequest(_message.Message):
    __slots__ = ("gatewayID", "serialNOs")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    SERIALNOS_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    serialNOs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gatewayID: _Optional[str] = ..., serialNOs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteCertificateBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeStatusRequest(_message.Message):
    __slots__ = ("queueSize",)
    QUEUESIZE_FIELD_NUMBER: _ClassVar[int]
    queueSize: int
    def __init__(self, queueSize: _Optional[int] = ...) -> None: ...

class StatusChange(_message.Message):
    __slots__ = ("gatewayID", "status", "timestamp")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    gatewayID: str
    status: Status
    timestamp: int
    def __init__(self, gatewayID: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...
