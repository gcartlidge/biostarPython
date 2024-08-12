import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_ENUM_VALUE_MUST_BE_ZERO: _ClassVar[Enum]
    DEFAULT_SCAN_TIMEOUT: _ClassVar[Enum]
    DEFAULT_TEMPLATE_SIZE: _ClassVar[Enum]
    FACE_TEMPLATE_SIZE: _ClassVar[Enum]
    MAX_TEMPLATES: _ClassVar[Enum]

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARD_TYPE_UNKNOWN: _ClassVar[Type]
    CARD_TYPE_CSN: _ClassVar[Type]
    CARD_TYPE_SECURE: _ClassVar[Type]
    CARD_TYPE_ACCESS: _ClassVar[Type]
    CARD_TYPE_CSN_MOBILE: _ClassVar[Type]
    CARD_TYPE_WIEGAND_MOBILE: _ClassVar[Type]
    CARD_TYPE_QR: _ClassVar[Type]
    CARD_TYPE_SECURE_QR: _ClassVar[Type]
    CARD_TYPE_WIEGAND: _ClassVar[Type]
    CARD_TYPE_CONFIG_CARD: _ClassVar[Type]
    CARD_TYPE_CUSTOM_SMART: _ClassVar[Type]

class DESFireEncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENC_DES_3DES: _ClassVar[DESFireEncryptionType]
    ENC_AES: _ClassVar[DESFireEncryptionType]

class DESFireOperationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_LEGACY: _ClassVar[DESFireOperationMode]
    OPERATION_APPLEVELKEY: _ClassVar[DESFireOperationMode]

class CardByteOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MSB: _ClassVar[CardByteOrder]
    LSB: _ClassVar[CardByteOrder]

class CardDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_BINARY: _ClassVar[CardDataType]
    DATA_ASCII: _ClassVar[CardDataType]
    DATA_UTF16: _ClassVar[CardDataType]
    DATA_BCD: _ClassVar[CardDataType]
FIRST_ENUM_VALUE_MUST_BE_ZERO: Enum
DEFAULT_SCAN_TIMEOUT: Enum
DEFAULT_TEMPLATE_SIZE: Enum
FACE_TEMPLATE_SIZE: Enum
MAX_TEMPLATES: Enum
CARD_TYPE_UNKNOWN: Type
CARD_TYPE_CSN: Type
CARD_TYPE_SECURE: Type
CARD_TYPE_ACCESS: Type
CARD_TYPE_CSN_MOBILE: Type
CARD_TYPE_WIEGAND_MOBILE: Type
CARD_TYPE_QR: Type
CARD_TYPE_SECURE_QR: Type
CARD_TYPE_WIEGAND: Type
CARD_TYPE_CONFIG_CARD: Type
CARD_TYPE_CUSTOM_SMART: Type
ENC_DES_3DES: DESFireEncryptionType
ENC_AES: DESFireEncryptionType
OPERATION_LEGACY: DESFireOperationMode
OPERATION_APPLEVELKEY: DESFireOperationMode
MSB: CardByteOrder
LSB: CardByteOrder
DATA_BINARY: CardDataType
DATA_ASCII: CardDataType
DATA_UTF16: CardDataType
DATA_BCD: CardDataType

class CSNCardData(_message.Message):
    __slots__ = ("type", "size", "data")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: Type
    size: int
    data: bytes
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., size: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class SmartCardHeader(_message.Message):
    __slots__ = ("headerCRC", "cardCRC", "type", "numOfTemplate", "numOfFaceTemplate", "templateSize", "issueCount", "duressMask", "cardAuthMode", "useAlphanumericID", "cardAuthModeEx")
    HEADERCRC_FIELD_NUMBER: _ClassVar[int]
    CARDCRC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMOFTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NUMOFFACETEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATESIZE_FIELD_NUMBER: _ClassVar[int]
    ISSUECOUNT_FIELD_NUMBER: _ClassVar[int]
    DURESSMASK_FIELD_NUMBER: _ClassVar[int]
    CARDAUTHMODE_FIELD_NUMBER: _ClassVar[int]
    USEALPHANUMERICID_FIELD_NUMBER: _ClassVar[int]
    CARDAUTHMODEEX_FIELD_NUMBER: _ClassVar[int]
    headerCRC: int
    cardCRC: int
    type: Type
    numOfTemplate: int
    numOfFaceTemplate: int
    templateSize: int
    issueCount: int
    duressMask: int
    cardAuthMode: int
    useAlphanumericID: bool
    cardAuthModeEx: int
    def __init__(self, headerCRC: _Optional[int] = ..., cardCRC: _Optional[int] = ..., type: _Optional[_Union[Type, str]] = ..., numOfTemplate: _Optional[int] = ..., numOfFaceTemplate: _Optional[int] = ..., templateSize: _Optional[int] = ..., issueCount: _Optional[int] = ..., duressMask: _Optional[int] = ..., cardAuthMode: _Optional[int] = ..., useAlphanumericID: bool = ..., cardAuthModeEx: _Optional[int] = ...) -> None: ...

class SmartCardCredential(_message.Message):
    __slots__ = ("PIN", "templates")
    PIN_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PIN: bytes
    templates: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, PIN: _Optional[bytes] = ..., templates: _Optional[_Iterable[bytes]] = ...) -> None: ...

class AccessOnCardData(_message.Message):
    __slots__ = ("accessGroupIDs", "startTime", "endTime")
    ACCESSGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    accessGroupIDs: _containers.RepeatedScalarFieldContainer[int]
    startTime: int
    endTime: int
    def __init__(self, accessGroupIDs: _Optional[_Iterable[int]] = ..., startTime: _Optional[int] = ..., endTime: _Optional[int] = ...) -> None: ...

class SmartCardData(_message.Message):
    __slots__ = ("header", "cardID", "credential", "accessOnData")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CARDID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    ACCESSONDATA_FIELD_NUMBER: _ClassVar[int]
    header: SmartCardHeader
    cardID: bytes
    credential: SmartCardCredential
    accessOnData: AccessOnCardData
    def __init__(self, header: _Optional[_Union[SmartCardHeader, _Mapping]] = ..., cardID: _Optional[bytes] = ..., credential: _Optional[_Union[SmartCardCredential, _Mapping]] = ..., accessOnData: _Optional[_Union[AccessOnCardData, _Mapping]] = ...) -> None: ...

class CardData(_message.Message):
    __slots__ = ("type", "CSNCardData", "smartCardData")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CSNCARDDATA_FIELD_NUMBER: _ClassVar[int]
    SMARTCARDDATA_FIELD_NUMBER: _ClassVar[int]
    type: Type
    CSNCardData: CSNCardData
    smartCardData: SmartCardData
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., CSNCardData: _Optional[_Union[CSNCardData, _Mapping]] = ..., smartCardData: _Optional[_Union[SmartCardData, _Mapping]] = ...) -> None: ...

class ScanRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class ScanResponse(_message.Message):
    __slots__ = ("cardData",)
    CARDDATA_FIELD_NUMBER: _ClassVar[int]
    cardData: CardData
    def __init__(self, cardData: _Optional[_Union[CardData, _Mapping]] = ...) -> None: ...

class EraseRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class EraseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("deviceID", "smartCardData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SMARTCARDDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    smartCardData: SmartCardData
    def __init__(self, deviceID: _Optional[int] = ..., smartCardData: _Optional[_Union[SmartCardData, _Mapping]] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MifareConfig(_message.Message):
    __slots__ = ("primaryKey", "secondaryKey", "startBlockIndex")
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    STARTBLOCKINDEX_FIELD_NUMBER: _ClassVar[int]
    primaryKey: bytes
    secondaryKey: bytes
    startBlockIndex: int
    def __init__(self, primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., startBlockIndex: _Optional[int] = ...) -> None: ...

class IClassConfig(_message.Message):
    __slots__ = ("primaryKey", "secondaryKey", "startBlockIndex")
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    STARTBLOCKINDEX_FIELD_NUMBER: _ClassVar[int]
    primaryKey: bytes
    secondaryKey: bytes
    startBlockIndex: int
    def __init__(self, primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., startBlockIndex: _Optional[int] = ...) -> None: ...

class DESFireConfig(_message.Message):
    __slots__ = ("primaryKey", "secondaryKey", "appID", "fileID", "encryptionType", "operationMode")
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONMODE_FIELD_NUMBER: _ClassVar[int]
    primaryKey: bytes
    secondaryKey: bytes
    appID: bytes
    fileID: int
    encryptionType: DESFireEncryptionType
    operationMode: DESFireOperationMode
    def __init__(self, primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., appID: _Optional[bytes] = ..., fileID: _Optional[int] = ..., encryptionType: _Optional[_Union[DESFireEncryptionType, str]] = ..., operationMode: _Optional[_Union[DESFireOperationMode, str]] = ...) -> None: ...

class SEOSConfig(_message.Message):
    __slots__ = ("OIDADF", "sizeADF", "OIDDataObjectID", "sizeDataObject", "primaryKeyAuth", "secondaryKeyAuth")
    OIDADF_FIELD_NUMBER: _ClassVar[int]
    SIZEADF_FIELD_NUMBER: _ClassVar[int]
    OIDDATAOBJECTID_FIELD_NUMBER: _ClassVar[int]
    SIZEDATAOBJECT_FIELD_NUMBER: _ClassVar[int]
    PRIMARYKEYAUTH_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEYAUTH_FIELD_NUMBER: _ClassVar[int]
    OIDADF: bytes
    sizeADF: int
    OIDDataObjectID: _containers.RepeatedScalarFieldContainer[int]
    sizeDataObject: _containers.RepeatedScalarFieldContainer[int]
    primaryKeyAuth: bytes
    secondaryKeyAuth: bytes
    def __init__(self, OIDADF: _Optional[bytes] = ..., sizeADF: _Optional[int] = ..., OIDDataObjectID: _Optional[_Iterable[int]] = ..., sizeDataObject: _Optional[_Iterable[int]] = ..., primaryKeyAuth: _Optional[bytes] = ..., secondaryKeyAuth: _Optional[bytes] = ...) -> None: ...

class CardConfig(_message.Message):
    __slots__ = ("byteOrder", "useWiegandFormat", "dataType", "useSecondaryKey", "mifareConfig", "iClassConfig", "DESFireConfig", "SEOSConfig", "formatID", "cipher", "smartCardByteOrder")
    BYTEORDER_FIELD_NUMBER: _ClassVar[int]
    USEWIEGANDFORMAT_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    USESECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    MIFARECONFIG_FIELD_NUMBER: _ClassVar[int]
    ICLASSCONFIG_FIELD_NUMBER: _ClassVar[int]
    DESFIRECONFIG_FIELD_NUMBER: _ClassVar[int]
    SEOSCONFIG_FIELD_NUMBER: _ClassVar[int]
    FORMATID_FIELD_NUMBER: _ClassVar[int]
    CIPHER_FIELD_NUMBER: _ClassVar[int]
    SMARTCARDBYTEORDER_FIELD_NUMBER: _ClassVar[int]
    byteOrder: CardByteOrder
    useWiegandFormat: bool
    dataType: CardDataType
    useSecondaryKey: bool
    mifareConfig: MifareConfig
    iClassConfig: IClassConfig
    DESFireConfig: DESFireConfig
    SEOSConfig: SEOSConfig
    formatID: int
    cipher: bool
    smartCardByteOrder: CardByteOrder
    def __init__(self, byteOrder: _Optional[_Union[CardByteOrder, str]] = ..., useWiegandFormat: bool = ..., dataType: _Optional[_Union[CardDataType, str]] = ..., useSecondaryKey: bool = ..., mifareConfig: _Optional[_Union[MifareConfig, _Mapping]] = ..., iClassConfig: _Optional[_Union[IClassConfig, _Mapping]] = ..., DESFireConfig: _Optional[_Union[DESFireConfig, _Mapping]] = ..., SEOSConfig: _Optional[_Union[SEOSConfig, _Mapping]] = ..., formatID: _Optional[int] = ..., cipher: bool = ..., smartCardByteOrder: _Optional[_Union[CardByteOrder, str]] = ...) -> None: ...

class GetConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: CardConfig
    def __init__(self, config: _Optional[_Union[CardConfig, _Mapping]] = ...) -> None: ...

class SetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: CardConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[CardConfig, _Mapping]] = ...) -> None: ...

class SetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: CardConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[CardConfig, _Mapping]] = ...) -> None: ...

class SetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class BlacklistItem(_message.Message):
    __slots__ = ("cardID", "issueCount")
    CARDID_FIELD_NUMBER: _ClassVar[int]
    ISSUECOUNT_FIELD_NUMBER: _ClassVar[int]
    cardID: bytes
    issueCount: int
    def __init__(self, cardID: _Optional[bytes] = ..., issueCount: _Optional[int] = ...) -> None: ...

class GetBlacklistRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetBlacklistResponse(_message.Message):
    __slots__ = ("blacklist",)
    BLACKLIST_FIELD_NUMBER: _ClassVar[int]
    blacklist: _containers.RepeatedCompositeFieldContainer[BlacklistItem]
    def __init__(self, blacklist: _Optional[_Iterable[_Union[BlacklistItem, _Mapping]]] = ...) -> None: ...

class AddBlacklistRequest(_message.Message):
    __slots__ = ("deviceID", "cardInfos")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CARDINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    cardInfos: _containers.RepeatedCompositeFieldContainer[BlacklistItem]
    def __init__(self, deviceID: _Optional[int] = ..., cardInfos: _Optional[_Iterable[_Union[BlacklistItem, _Mapping]]] = ...) -> None: ...

class AddBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddBlacklistMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "cardInfos")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CARDINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    cardInfos: _containers.RepeatedCompositeFieldContainer[BlacklistItem]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., cardInfos: _Optional[_Iterable[_Union[BlacklistItem, _Mapping]]] = ...) -> None: ...

class AddBlacklistMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteBlacklistRequest(_message.Message):
    __slots__ = ("deviceID", "cardInfos")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CARDINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    cardInfos: _containers.RepeatedCompositeFieldContainer[BlacklistItem]
    def __init__(self, deviceID: _Optional[int] = ..., cardInfos: _Optional[_Iterable[_Union[BlacklistItem, _Mapping]]] = ...) -> None: ...

class DeleteBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteBlacklistMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "cardInfos")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CARDINFOS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    cardInfos: _containers.RepeatedCompositeFieldContainer[BlacklistItem]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., cardInfos: _Optional[_Iterable[_Union[BlacklistItem, _Mapping]]] = ...) -> None: ...

class DeleteBlacklistMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DeleteAllBlacklistRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteAllBlacklistResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllBlacklistMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteAllBlacklistMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class Card1XConfig(_message.Message):
    __slots__ = ("disabled", "useCSNOnly", "bioEntryCompatible", "useSecondaryKey", "primaryKey", "secondaryKey", "CISIndex", "numOfTemplate", "templateSize", "templateStartBlocks")
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    USECSNONLY_FIELD_NUMBER: _ClassVar[int]
    BIOENTRYCOMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    USESECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    CISINDEX_FIELD_NUMBER: _ClassVar[int]
    NUMOFTEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATESIZE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATESTARTBLOCKS_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    useCSNOnly: bool
    bioEntryCompatible: bool
    useSecondaryKey: bool
    primaryKey: bytes
    secondaryKey: bytes
    CISIndex: int
    numOfTemplate: int
    templateSize: int
    templateStartBlocks: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, disabled: bool = ..., useCSNOnly: bool = ..., bioEntryCompatible: bool = ..., useSecondaryKey: bool = ..., primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., CISIndex: _Optional[int] = ..., numOfTemplate: _Optional[int] = ..., templateSize: _Optional[int] = ..., templateStartBlocks: _Optional[_Iterable[int]] = ...) -> None: ...

class Get1XConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class Get1XConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: Card1XConfig
    def __init__(self, config: _Optional[_Union[Card1XConfig, _Mapping]] = ...) -> None: ...

class Set1XConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: Card1XConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[Card1XConfig, _Mapping]] = ...) -> None: ...

class Set1XConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Set1XConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: Card1XConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[Card1XConfig, _Mapping]] = ...) -> None: ...

class Set1XConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class WriteQRCodeRequest(_message.Message):
    __slots__ = ("QRText",)
    QRTEXT_FIELD_NUMBER: _ClassVar[int]
    QRText: str
    def __init__(self, QRText: _Optional[str] = ...) -> None: ...

class WriteQRCodeResponse(_message.Message):
    __slots__ = ("cardData",)
    CARDDATA_FIELD_NUMBER: _ClassVar[int]
    cardData: CSNCardData
    def __init__(self, cardData: _Optional[_Union[CSNCardData, _Mapping]] = ...) -> None: ...

class QRConfig(_message.Message):
    __slots__ = ("useQRCode", "scanTimeout", "bypassData", "treatAsCSN")
    USEQRCODE_FIELD_NUMBER: _ClassVar[int]
    SCANTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BYPASSDATA_FIELD_NUMBER: _ClassVar[int]
    TREATASCSN_FIELD_NUMBER: _ClassVar[int]
    useQRCode: bool
    scanTimeout: int
    bypassData: bool
    treatAsCSN: bool
    def __init__(self, useQRCode: bool = ..., scanTimeout: _Optional[int] = ..., bypassData: bool = ..., treatAsCSN: bool = ...) -> None: ...

class GetQRConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetQRConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: QRConfig
    def __init__(self, config: _Optional[_Union[QRConfig, _Mapping]] = ...) -> None: ...

class SetQRConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: QRConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[QRConfig, _Mapping]] = ...) -> None: ...

class SetQRConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetQRConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: QRConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[QRConfig, _Mapping]] = ...) -> None: ...

class SetQRConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class DESFireAppLevelKey(_message.Message):
    __slots__ = ("appMasterKey", "fileReadKey", "fileWriteKey", "fileReadKeyNumber", "fileWriteKeyNumber")
    APPMASTERKEY_FIELD_NUMBER: _ClassVar[int]
    FILEREADKEY_FIELD_NUMBER: _ClassVar[int]
    FILEWRITEKEY_FIELD_NUMBER: _ClassVar[int]
    FILEREADKEYNUMBER_FIELD_NUMBER: _ClassVar[int]
    FILEWRITEKEYNUMBER_FIELD_NUMBER: _ClassVar[int]
    appMasterKey: bytes
    fileReadKey: bytes
    fileWriteKey: bytes
    fileReadKeyNumber: int
    fileWriteKeyNumber: int
    def __init__(self, appMasterKey: _Optional[bytes] = ..., fileReadKey: _Optional[bytes] = ..., fileWriteKey: _Optional[bytes] = ..., fileReadKeyNumber: _Optional[int] = ..., fileWriteKeyNumber: _Optional[int] = ...) -> None: ...

class CustomMifareCard(_message.Message):
    __slots__ = ("primaryKey", "secondaryKey", "startBlockIndex", "dataSize", "skipBytes")
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    STARTBLOCKINDEX_FIELD_NUMBER: _ClassVar[int]
    DATASIZE_FIELD_NUMBER: _ClassVar[int]
    SKIPBYTES_FIELD_NUMBER: _ClassVar[int]
    primaryKey: bytes
    secondaryKey: bytes
    startBlockIndex: int
    dataSize: int
    skipBytes: int
    def __init__(self, primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., startBlockIndex: _Optional[int] = ..., dataSize: _Optional[int] = ..., skipBytes: _Optional[int] = ...) -> None: ...

class CustomDESFireCard(_message.Message):
    __slots__ = ("primaryKey", "secondaryKey", "appID", "fileID", "encryptionType", "operationMode", "dataSize", "skipBytes", "desfireAppKey")
    PRIMARYKEY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONMODE_FIELD_NUMBER: _ClassVar[int]
    DATASIZE_FIELD_NUMBER: _ClassVar[int]
    SKIPBYTES_FIELD_NUMBER: _ClassVar[int]
    DESFIREAPPKEY_FIELD_NUMBER: _ClassVar[int]
    primaryKey: bytes
    secondaryKey: bytes
    appID: bytes
    fileID: int
    encryptionType: DESFireEncryptionType
    operationMode: DESFireOperationMode
    dataSize: int
    skipBytes: int
    desfireAppKey: DESFireAppLevelKey
    def __init__(self, primaryKey: _Optional[bytes] = ..., secondaryKey: _Optional[bytes] = ..., appID: _Optional[bytes] = ..., fileID: _Optional[int] = ..., encryptionType: _Optional[_Union[DESFireEncryptionType, str]] = ..., operationMode: _Optional[_Union[DESFireOperationMode, str]] = ..., dataSize: _Optional[int] = ..., skipBytes: _Optional[int] = ..., desfireAppKey: _Optional[_Union[DESFireAppLevelKey, _Mapping]] = ...) -> None: ...

class CustomConfig(_message.Message):
    __slots__ = ("dataType", "useSecondaryKey", "mifare", "desfire", "smartCardByteOrder", "formatID")
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    USESECONDARYKEY_FIELD_NUMBER: _ClassVar[int]
    MIFARE_FIELD_NUMBER: _ClassVar[int]
    DESFIRE_FIELD_NUMBER: _ClassVar[int]
    SMARTCARDBYTEORDER_FIELD_NUMBER: _ClassVar[int]
    FORMATID_FIELD_NUMBER: _ClassVar[int]
    dataType: CardDataType
    useSecondaryKey: bool
    mifare: CustomMifareCard
    desfire: CustomDESFireCard
    smartCardByteOrder: CardByteOrder
    formatID: int
    def __init__(self, dataType: _Optional[_Union[CardDataType, str]] = ..., useSecondaryKey: bool = ..., mifare: _Optional[_Union[CustomMifareCard, _Mapping]] = ..., desfire: _Optional[_Union[CustomDESFireCard, _Mapping]] = ..., smartCardByteOrder: _Optional[_Union[CardByteOrder, str]] = ..., formatID: _Optional[int] = ...) -> None: ...

class GetCustomConfigRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetCustomConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: CustomConfig
    def __init__(self, config: _Optional[_Union[CustomConfig, _Mapping]] = ...) -> None: ...

class SetCustomConfigRequest(_message.Message):
    __slots__ = ("deviceID", "config")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    config: CustomConfig
    def __init__(self, deviceID: _Optional[int] = ..., config: _Optional[_Union[CustomConfig, _Mapping]] = ...) -> None: ...

class SetCustomConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCustomConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "config")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    config: CustomConfig
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., config: _Optional[_Union[CustomConfig, _Mapping]] = ...) -> None: ...

class SetCustomConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...
