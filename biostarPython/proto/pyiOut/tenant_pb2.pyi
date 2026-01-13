import cert_pb2 as _cert_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TenantInfo(_message.Message):
    __slots__ = ("tenantID", "gatewayIDs")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantID: _Optional[str] = ..., gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetListResponse(_message.Message):
    __slots__ = ("tenantIDs",)
    TENANTIDS_FIELD_NUMBER: _ClassVar[int]
    tenantIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("tenantIDs",)
    TENANTIDS_FIELD_NUMBER: _ClassVar[int]
    tenantIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("tenantInfos",)
    TENANTINFOS_FIELD_NUMBER: _ClassVar[int]
    tenantInfos: _containers.RepeatedCompositeFieldContainer[TenantInfo]
    def __init__(self, tenantInfos: _Optional[_Iterable[_Union[TenantInfo, _Mapping]]] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ("tenantInfos",)
    TENANTINFOS_FIELD_NUMBER: _ClassVar[int]
    tenantInfos: _containers.RepeatedCompositeFieldContainer[TenantInfo]
    def __init__(self, tenantInfos: _Optional[_Iterable[_Union[TenantInfo, _Mapping]]] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("tenantIDs",)
    TENANTIDS_FIELD_NUMBER: _ClassVar[int]
    tenantIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddGatewayRequest(_message.Message):
    __slots__ = ("tenantID", "gatewayIDs")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantID: _Optional[str] = ..., gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class AddGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ("tenantID", "gatewayIDs")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    GATEWAYIDS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    gatewayIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantID: _Optional[str] = ..., gatewayIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteGatewayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCertificateRequest(_message.Message):
    __slots__ = ("tenantID", "subject", "expireAfterYears")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EXPIREAFTERYEARS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    subject: _cert_pb2.PKIName
    expireAfterYears: int
    def __init__(self, tenantID: _Optional[str] = ..., subject: _Optional[_Union[_cert_pb2.PKIName, _Mapping]] = ..., expireAfterYears: _Optional[int] = ...) -> None: ...

class CreateCertificateResponse(_message.Message):
    __slots__ = ("tenantCert", "tenantKey")
    TENANTCERT_FIELD_NUMBER: _ClassVar[int]
    TENANTKEY_FIELD_NUMBER: _ClassVar[int]
    tenantCert: str
    tenantKey: str
    def __init__(self, tenantCert: _Optional[str] = ..., tenantKey: _Optional[str] = ...) -> None: ...

class GetIssuanceHistoryRequest(_message.Message):
    __slots__ = ("tenantIDs",)
    TENANTIDS_FIELD_NUMBER: _ClassVar[int]
    tenantIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class CertificateInfo(_message.Message):
    __slots__ = ("tenantID", "subject", "serialNO", "issueDate", "expiryDate", "blacklisted")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SERIALNO_FIELD_NUMBER: _ClassVar[int]
    ISSUEDATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRYDATE_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    subject: _cert_pb2.PKIName
    serialNO: int
    issueDate: int
    expiryDate: int
    blacklisted: bool
    def __init__(self, tenantID: _Optional[str] = ..., subject: _Optional[_Union[_cert_pb2.PKIName, _Mapping]] = ..., serialNO: _Optional[int] = ..., issueDate: _Optional[int] = ..., expiryDate: _Optional[int] = ..., blacklisted: bool = ...) -> None: ...

class GetIssuanceHistoryResponse(_message.Message):
    __slots__ = ("certInfos",)
    CERTINFOS_FIELD_NUMBER: _ClassVar[int]
    certInfos: _containers.RepeatedCompositeFieldContainer[CertificateInfo]
    def __init__(self, certInfos: _Optional[_Iterable[_Union[CertificateInfo, _Mapping]]] = ...) -> None: ...

class GetCertificateBlacklistRequest(_message.Message):
    __slots__ = ("tenantIDs",)
    TENANTIDS_FIELD_NUMBER: _ClassVar[int]
    tenantIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenantIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCertificateBlacklistResponse(_message.Message):
    __slots__ = ("certInfos",)
    CERTINFOS_FIELD_NUMBER: _ClassVar[int]
    certInfos: _containers.RepeatedCompositeFieldContainer[CertificateInfo]
    def __init__(self, certInfos: _Optional[_Iterable[_Union[CertificateInfo, _Mapping]]] = ...) -> None: ...

class AddCertificateBlacklistRequest(_message.Message):
    __slots__ = ("tenantID", "serialNOs")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    SERIALNOS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    serialNOs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tenantID: _Optional[str] = ..., serialNOs: _Optional[_Iterable[int]] = ...) -> None: ...

class AddCertificateBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCertificateBlacklistRequest(_message.Message):
    __slots__ = ("tenantID", "serialNOs")
    TENANTID_FIELD_NUMBER: _ClassVar[int]
    SERIALNOS_FIELD_NUMBER: _ClassVar[int]
    tenantID: str
    serialNOs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tenantID: _Optional[str] = ..., serialNOs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteCertificateBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
