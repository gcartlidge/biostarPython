import err_pb2 as _err_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[Type]
    BIOENTRY_PLUS: _ClassVar[Type]
    BIOENTRY_W: _ClassVar[Type]
    BIOLITE_NET: _ClassVar[Type]
    XPASS: _ClassVar[Type]
    XPASS_S2: _ClassVar[Type]
    ENTRY_MAX: _ClassVar[Type]
    SECURE_IO_2: _ClassVar[Type]
    DOOR_MODULE_20: _ClassVar[Type]
    BIOSTATION_2: _ClassVar[Type]
    BIOSTATION_A2: _ClassVar[Type]
    FACESTATION_2: _ClassVar[Type]
    IO_DEVICE: _ClassVar[Type]
    BIOSTATION_L2: _ClassVar[Type]
    BIOENTRY_W2: _ClassVar[Type]
    RS485_SLAVE: _ClassVar[Type]
    CORESTATION_40: _ClassVar[Type]
    OUTPUT_MODULE: _ClassVar[Type]
    INPUT_MODULE: _ClassVar[Type]
    BIOENTRY_P2: _ClassVar[Type]
    BIOLITE_N2: _ClassVar[Type]
    XPASS2: _ClassVar[Type]
    XPASS_S3: _ClassVar[Type]
    BIOENTRY_R2: _ClassVar[Type]
    XPASS_D2: _ClassVar[Type]
    DOOR_MODULE_21: _ClassVar[Type]
    XPASS_D2_KEYPAD: _ClassVar[Type]
    FACELITE: _ClassVar[Type]
    XPASS2_KEYPAD: _ClassVar[Type]
    XPASS_D2_REV: _ClassVar[Type]
    XPASS_D2_KEYPAD_REV: _ClassVar[Type]
    FACESTATION_F2_FP: _ClassVar[Type]
    FACESTATION_F2: _ClassVar[Type]
    XSTATION_2_QR: _ClassVar[Type]
    XSTATION_2: _ClassVar[Type]
    IM_120: _ClassVar[Type]
    XSTATION_2_FP: _ClassVar[Type]
    BIOSTATION_3: _ClassVar[Type]
    BIOSTATION_2A: _ClassVar[Type]
    BIOENTRY_W3: _ClassVar[Type]
    CORESTATION_20: _ClassVar[Type]
    DOOR_INTERFACE_24: _ClassVar[Type]
    XPASS_Q2: _ClassVar[Type]
    UNKNOWN: _ClassVar[Type]

class SwitchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMALLY_OPEN: _ClassVar[SwitchType]
    NORMALLY_CLOSED: _ClassVar[SwitchType]

class LEDColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LED_COLOR_OFF: _ClassVar[LEDColor]
    LED_COLOR_RED: _ClassVar[LEDColor]
    LED_COLOR_YELLOW: _ClassVar[LEDColor]
    LED_COLOR_GREEN: _ClassVar[LEDColor]
    LED_COLOR_CYAN: _ClassVar[LEDColor]
    LED_COLOR_BLUE: _ClassVar[LEDColor]
    LED_COLOR_MAGENTA: _ClassVar[LEDColor]
    LED_COLOR_WHITE: _ClassVar[LEDColor]

class BuzzerTone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUZZER_TONE_OFF: _ClassVar[BuzzerTone]
    BUZZER_TONE_LOW: _ClassVar[BuzzerTone]
    BUZZER_TONE_MIDDLE: _ClassVar[BuzzerTone]
    BUZZER_TONE_HIGH: _ClassVar[BuzzerTone]
UNDEFINED: Type
BIOENTRY_PLUS: Type
BIOENTRY_W: Type
BIOLITE_NET: Type
XPASS: Type
XPASS_S2: Type
ENTRY_MAX: Type
SECURE_IO_2: Type
DOOR_MODULE_20: Type
BIOSTATION_2: Type
BIOSTATION_A2: Type
FACESTATION_2: Type
IO_DEVICE: Type
BIOSTATION_L2: Type
BIOENTRY_W2: Type
RS485_SLAVE: Type
CORESTATION_40: Type
OUTPUT_MODULE: Type
INPUT_MODULE: Type
BIOENTRY_P2: Type
BIOLITE_N2: Type
XPASS2: Type
XPASS_S3: Type
BIOENTRY_R2: Type
XPASS_D2: Type
DOOR_MODULE_21: Type
XPASS_D2_KEYPAD: Type
FACELITE: Type
XPASS2_KEYPAD: Type
XPASS_D2_REV: Type
XPASS_D2_KEYPAD_REV: Type
FACESTATION_F2_FP: Type
FACESTATION_F2: Type
XSTATION_2_QR: Type
XSTATION_2: Type
IM_120: Type
XSTATION_2_FP: Type
BIOSTATION_3: Type
BIOSTATION_2A: Type
BIOENTRY_W3: Type
CORESTATION_20: Type
DOOR_INTERFACE_24: Type
XPASS_Q2: Type
UNKNOWN: Type
NORMALLY_OPEN: SwitchType
NORMALLY_CLOSED: SwitchType
LED_COLOR_OFF: LEDColor
LED_COLOR_RED: LEDColor
LED_COLOR_YELLOW: LEDColor
LED_COLOR_GREEN: LEDColor
LED_COLOR_CYAN: LEDColor
LED_COLOR_BLUE: LEDColor
LED_COLOR_MAGENTA: LEDColor
LED_COLOR_WHITE: LEDColor
BUZZER_TONE_OFF: BuzzerTone
BUZZER_TONE_LOW: BuzzerTone
BUZZER_TONE_MIDDLE: BuzzerTone
BUZZER_TONE_HIGH: BuzzerTone

class GetInfoRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class FactoryInfo(_message.Message):
    __slots__ = ("MACAddr", "modelName", "firmwareVersion", "kernelVersion", "BSCoreVersion", "boardVersion")
    MACADDR_FIELD_NUMBER: _ClassVar[int]
    MODELNAME_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    KERNELVERSION_FIELD_NUMBER: _ClassVar[int]
    BSCOREVERSION_FIELD_NUMBER: _ClassVar[int]
    BOARDVERSION_FIELD_NUMBER: _ClassVar[int]
    MACAddr: str
    modelName: str
    firmwareVersion: str
    kernelVersion: str
    BSCoreVersion: str
    boardVersion: str
    def __init__(self, MACAddr: _Optional[str] = ..., modelName: _Optional[str] = ..., firmwareVersion: _Optional[str] = ..., kernelVersion: _Optional[str] = ..., BSCoreVersion: _Optional[str] = ..., boardVersion: _Optional[str] = ...) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: FactoryInfo
    def __init__(self, info: _Optional[_Union[FactoryInfo, _Mapping]] = ...) -> None: ...

class GetCapabilityRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeviceCapability(_message.Message):
    __slots__ = ("maxUsers", "maxEventLogs", "maxImageLogs", "maxBlacklists", "maxOperators", "maxCards", "maxFaces", "maxFingerprints", "maxUserNames", "maxUserImages", "maxUserJobs", "maxUserPhrases", "maxCardsPerUser", "maxFacesPerUser", "maxFingerprintsPerUser", "maxInputPorts", "maxOutputPorts", "maxRelays", "maxRS485Channels", "cameraSupported", "tamperSupported", "wlanSupported", "displaySupported", "thermalSupported", "maskSupported", "faceExSupported", "voipExSupported", "EMCardSupported", "HIDProxCardSupported", "MifareFelicaCardSupported", "iClassCardSupported", "ClassicPlusCardSupported", "DesFireEV1CardSupported", "SRSECardSupported", "SEOSCardSupported", "NFCSupported", "BLESupported", "CustomClassicPlusSupported", "CustomDesFireEV1Supported", "TOM_NFCSupported", "TOM_BLESupported", "CustomFelicaSupported", "useCardOperation", "extendedAuthSupported", "cardInputSupported", "fingerprintInputSupported", "faceInputSupported", "idInputSupported", "PINInputSupported", "biometricOnlySupported", "biometricPINSupported", "cardOnlySupported", "cardBiometricSupported", "cardPINSupported", "cardBiometricOrPINSupported", "cardBiometricPINSupported", "idBiometricSupported", "idPINSupported", "idBiometricOrPINSupported", "idBiometricPINSupported", "extendedFaceOnlySupported", "extendedFaceFingerprintSupported", "extendedFacePINSupported", "extendedFaceFingerprintOrPINSupported", "extendedFaceFingerprintPINSupported", "extendedFingerprintOnlySupported", "extendedFingerprintFaceSupported", "extendedFingerprintPINSupported", "extendedFingerprintFaceOrPINSupported", "extendedFingerprintFacePINSupported", "extendedCardOnlySupported", "extendedCardFaceSupported", "extendedCardFingerprintSupported", "extendedCardPINSupported", "extendedCardFaceOrFingerprintSupported", "extendedCardFaceOrPINSupported", "extendedCardFingerprintOrPINSupported", "extendedCardFaceOrFingerprintOrPINSupported", "extendedCardFaceFingerprintSupported", "extendedCardFacePINSupported", "extendedCardFingerprintFaceSupported", "extendedCardFingerprintPINSupported", "extendedCardFaceOrFingerprintPINSupported", "extendedCardFaceFingerprintOrPINSupported", "extendedCardFingerprintFaceOrPINSupported", "extendedIdFaceSupported", "extendedIdFingerprintSupported", "extendedIdPINSupported", "extendedIdFaceOrFingerprintSupported", "extendedIdFaceOrPINSupported", "extendedIdFingerprintOrPINSupported", "extendedIdFaceOrFingerprintOrPINSupported", "extendedIdFaceFingerprintSupported", "extendedIdFacePINSupported", "extendedIdFingerprintFaceSupported", "extendedIdFingerprintPINSupported", "extendedIdFaceOrFingerprintPINSupported", "extendedIdFaceFingerprintOrPINSupported", "extendedIdFingerprintFaceOrPINSupported", "intelligentPDSupported", "updateUserSupported", "simulatedUnlockSupported", "smartCardByteOrderSupported", "qrAsCSNSupported", "rtspSupported", "lfdSupported", "visualQRSupported", "maxVoipExtensionNumbers", "osdpStandardCentralSupported", "enableLicenseFuncSupported", "keypadBacklightSupported", "uzWirelessLockDoorSupported", "customSmartCardSupported", "tomSupported", "tomEnrollSupported", "showOsdpResultbyLED", "customSmartCardFelicaSupported", "ignoreInputAfterWiegandOut", "setSlaveBaudrateSupported", "changeRtspResolutionSupported", "changeVoipResolutionSupported", "changeVoipTransportSupported", "showOptionUserInfoSupported", "changeScrambleKeypadSupported", "visualFaceTemplateVersion", "authOnlyUnMaskSupported", "mifareExSupported", "lockOverrideSupported", "doorModeOverrideSupported", "extendedDoorOpenTimeSupported", "realtimeDeviceIOStatusSupported", "dynamicSlaveDeviceSupported", "secureTamperSupported", "customSmartcardSlaveSupported", "serverPrivateMsgSupported", "facilityCodeSupported", "masterAdminSupported", "adminTwoStepAuthSupported")
    MAXUSERS_FIELD_NUMBER: _ClassVar[int]
    MAXEVENTLOGS_FIELD_NUMBER: _ClassVar[int]
    MAXIMAGELOGS_FIELD_NUMBER: _ClassVar[int]
    MAXBLACKLISTS_FIELD_NUMBER: _ClassVar[int]
    MAXOPERATORS_FIELD_NUMBER: _ClassVar[int]
    MAXCARDS_FIELD_NUMBER: _ClassVar[int]
    MAXFACES_FIELD_NUMBER: _ClassVar[int]
    MAXFINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
    MAXUSERNAMES_FIELD_NUMBER: _ClassVar[int]
    MAXUSERIMAGES_FIELD_NUMBER: _ClassVar[int]
    MAXUSERJOBS_FIELD_NUMBER: _ClassVar[int]
    MAXUSERPHRASES_FIELD_NUMBER: _ClassVar[int]
    MAXCARDSPERUSER_FIELD_NUMBER: _ClassVar[int]
    MAXFACESPERUSER_FIELD_NUMBER: _ClassVar[int]
    MAXFINGERPRINTSPERUSER_FIELD_NUMBER: _ClassVar[int]
    MAXINPUTPORTS_FIELD_NUMBER: _ClassVar[int]
    MAXOUTPUTPORTS_FIELD_NUMBER: _ClassVar[int]
    MAXRELAYS_FIELD_NUMBER: _ClassVar[int]
    MAXRS485CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CAMERASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TAMPERSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    WLANSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DISPLAYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    THERMALSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MASKSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FACEEXSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VOIPEXSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EMCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HIDPROXCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MIFAREFELICACARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ICLASSCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CLASSICPLUSCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DESFIREEV1CARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SRSECARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SEOSCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NFCSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BLESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMCLASSICPLUSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMDESFIREEV1SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TOM_NFCSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TOM_BLESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMFELICASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    USECARDOPERATION_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDAUTHSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDINPUTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINTINPUTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FACEINPUTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IDINPUTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    PININPUTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICONLYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BIOMETRICPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDONLYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDBIOMETRICSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDBIOMETRICORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDBIOMETRICPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IDBIOMETRICSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IDPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IDBIOMETRICORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IDBIOMETRICPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFACEONLYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFACEFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFACEPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFACEFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFACEFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFINGERPRINTONLYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFINGERPRINTFACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFINGERPRINTFACEORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDFINGERPRINTFACEPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDONLYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEORFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEORFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFINGERPRINTFACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEORFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFACEFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDCARDFINGERPRINTFACEORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEORFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEORFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEFINGERPRINTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFINGERPRINTFACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEORFINGERPRINTPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFACEFINGERPRINTORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDIDFINGERPRINTFACEORPINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    INTELLIGENTPDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    UPDATEUSERSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SIMULATEDUNLOCKSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SMARTCARDBYTEORDERSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    QRASCSNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RTSPSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    LFDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VISUALQRSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MAXVOIPEXTENSIONNUMBERS_FIELD_NUMBER: _ClassVar[int]
    OSDPSTANDARDCENTRALSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ENABLELICENSEFUNCSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    KEYPADBACKLIGHTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    UZWIRELESSLOCKDOORSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSMARTCARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TOMSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TOMENROLLSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SHOWOSDPRESULTBYLED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSMARTCARDFELICASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IGNOREINPUTAFTERWIEGANDOUT_FIELD_NUMBER: _ClassVar[int]
    SETSLAVEBAUDRATESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CHANGERTSPRESOLUTIONSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CHANGEVOIPRESOLUTIONSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CHANGEVOIPTRANSPORTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SHOWOPTIONUSERINFOSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CHANGESCRAMBLEKEYPADSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VISUALFACETEMPLATEVERSION_FIELD_NUMBER: _ClassVar[int]
    AUTHONLYUNMASKSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MIFAREEXSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    LOCKOVERRIDESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DOORMODEOVERRIDESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDEDDOOROPENTIMESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    REALTIMEDEVICEIOSTATUSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DYNAMICSLAVEDEVICESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SECURETAMPERSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CUSTOMSMARTCARDSLAVESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SERVERPRIVATEMSGSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FACILITYCODESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MASTERADMINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ADMINTWOSTEPAUTHSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    maxUsers: int
    maxEventLogs: int
    maxImageLogs: int
    maxBlacklists: int
    maxOperators: int
    maxCards: int
    maxFaces: int
    maxFingerprints: int
    maxUserNames: int
    maxUserImages: int
    maxUserJobs: int
    maxUserPhrases: int
    maxCardsPerUser: int
    maxFacesPerUser: int
    maxFingerprintsPerUser: int
    maxInputPorts: int
    maxOutputPorts: int
    maxRelays: int
    maxRS485Channels: int
    cameraSupported: bool
    tamperSupported: bool
    wlanSupported: bool
    displaySupported: bool
    thermalSupported: bool
    maskSupported: bool
    faceExSupported: bool
    voipExSupported: bool
    EMCardSupported: bool
    HIDProxCardSupported: bool
    MifareFelicaCardSupported: bool
    iClassCardSupported: bool
    ClassicPlusCardSupported: bool
    DesFireEV1CardSupported: bool
    SRSECardSupported: bool
    SEOSCardSupported: bool
    NFCSupported: bool
    BLESupported: bool
    CustomClassicPlusSupported: bool
    CustomDesFireEV1Supported: bool
    TOM_NFCSupported: bool
    TOM_BLESupported: bool
    CustomFelicaSupported: bool
    useCardOperation: bool
    extendedAuthSupported: bool
    cardInputSupported: bool
    fingerprintInputSupported: bool
    faceInputSupported: bool
    idInputSupported: bool
    PINInputSupported: bool
    biometricOnlySupported: bool
    biometricPINSupported: bool
    cardOnlySupported: bool
    cardBiometricSupported: bool
    cardPINSupported: bool
    cardBiometricOrPINSupported: bool
    cardBiometricPINSupported: bool
    idBiometricSupported: bool
    idPINSupported: bool
    idBiometricOrPINSupported: bool
    idBiometricPINSupported: bool
    extendedFaceOnlySupported: bool
    extendedFaceFingerprintSupported: bool
    extendedFacePINSupported: bool
    extendedFaceFingerprintOrPINSupported: bool
    extendedFaceFingerprintPINSupported: bool
    extendedFingerprintOnlySupported: bool
    extendedFingerprintFaceSupported: bool
    extendedFingerprintPINSupported: bool
    extendedFingerprintFaceOrPINSupported: bool
    extendedFingerprintFacePINSupported: bool
    extendedCardOnlySupported: bool
    extendedCardFaceSupported: bool
    extendedCardFingerprintSupported: bool
    extendedCardPINSupported: bool
    extendedCardFaceOrFingerprintSupported: bool
    extendedCardFaceOrPINSupported: bool
    extendedCardFingerprintOrPINSupported: bool
    extendedCardFaceOrFingerprintOrPINSupported: bool
    extendedCardFaceFingerprintSupported: bool
    extendedCardFacePINSupported: bool
    extendedCardFingerprintFaceSupported: bool
    extendedCardFingerprintPINSupported: bool
    extendedCardFaceOrFingerprintPINSupported: bool
    extendedCardFaceFingerprintOrPINSupported: bool
    extendedCardFingerprintFaceOrPINSupported: bool
    extendedIdFaceSupported: bool
    extendedIdFingerprintSupported: bool
    extendedIdPINSupported: bool
    extendedIdFaceOrFingerprintSupported: bool
    extendedIdFaceOrPINSupported: bool
    extendedIdFingerprintOrPINSupported: bool
    extendedIdFaceOrFingerprintOrPINSupported: bool
    extendedIdFaceFingerprintSupported: bool
    extendedIdFacePINSupported: bool
    extendedIdFingerprintFaceSupported: bool
    extendedIdFingerprintPINSupported: bool
    extendedIdFaceOrFingerprintPINSupported: bool
    extendedIdFaceFingerprintOrPINSupported: bool
    extendedIdFingerprintFaceOrPINSupported: bool
    intelligentPDSupported: bool
    updateUserSupported: bool
    simulatedUnlockSupported: bool
    smartCardByteOrderSupported: bool
    qrAsCSNSupported: bool
    rtspSupported: bool
    lfdSupported: bool
    visualQRSupported: bool
    maxVoipExtensionNumbers: int
    osdpStandardCentralSupported: bool
    enableLicenseFuncSupported: bool
    keypadBacklightSupported: bool
    uzWirelessLockDoorSupported: bool
    customSmartCardSupported: bool
    tomSupported: bool
    tomEnrollSupported: bool
    showOsdpResultbyLED: bool
    customSmartCardFelicaSupported: bool
    ignoreInputAfterWiegandOut: bool
    setSlaveBaudrateSupported: bool
    changeRtspResolutionSupported: bool
    changeVoipResolutionSupported: bool
    changeVoipTransportSupported: bool
    showOptionUserInfoSupported: bool
    changeScrambleKeypadSupported: bool
    visualFaceTemplateVersion: int
    authOnlyUnMaskSupported: bool
    mifareExSupported: bool
    lockOverrideSupported: bool
    doorModeOverrideSupported: bool
    extendedDoorOpenTimeSupported: bool
    realtimeDeviceIOStatusSupported: bool
    dynamicSlaveDeviceSupported: bool
    secureTamperSupported: bool
    customSmartcardSlaveSupported: bool
    serverPrivateMsgSupported: bool
    facilityCodeSupported: bool
    masterAdminSupported: bool
    adminTwoStepAuthSupported: bool
    def __init__(self, maxUsers: _Optional[int] = ..., maxEventLogs: _Optional[int] = ..., maxImageLogs: _Optional[int] = ..., maxBlacklists: _Optional[int] = ..., maxOperators: _Optional[int] = ..., maxCards: _Optional[int] = ..., maxFaces: _Optional[int] = ..., maxFingerprints: _Optional[int] = ..., maxUserNames: _Optional[int] = ..., maxUserImages: _Optional[int] = ..., maxUserJobs: _Optional[int] = ..., maxUserPhrases: _Optional[int] = ..., maxCardsPerUser: _Optional[int] = ..., maxFacesPerUser: _Optional[int] = ..., maxFingerprintsPerUser: _Optional[int] = ..., maxInputPorts: _Optional[int] = ..., maxOutputPorts: _Optional[int] = ..., maxRelays: _Optional[int] = ..., maxRS485Channels: _Optional[int] = ..., cameraSupported: bool = ..., tamperSupported: bool = ..., wlanSupported: bool = ..., displaySupported: bool = ..., thermalSupported: bool = ..., maskSupported: bool = ..., faceExSupported: bool = ..., voipExSupported: bool = ..., EMCardSupported: bool = ..., HIDProxCardSupported: bool = ..., MifareFelicaCardSupported: bool = ..., iClassCardSupported: bool = ..., ClassicPlusCardSupported: bool = ..., DesFireEV1CardSupported: bool = ..., SRSECardSupported: bool = ..., SEOSCardSupported: bool = ..., NFCSupported: bool = ..., BLESupported: bool = ..., CustomClassicPlusSupported: bool = ..., CustomDesFireEV1Supported: bool = ..., TOM_NFCSupported: bool = ..., TOM_BLESupported: bool = ..., CustomFelicaSupported: bool = ..., useCardOperation: bool = ..., extendedAuthSupported: bool = ..., cardInputSupported: bool = ..., fingerprintInputSupported: bool = ..., faceInputSupported: bool = ..., idInputSupported: bool = ..., PINInputSupported: bool = ..., biometricOnlySupported: bool = ..., biometricPINSupported: bool = ..., cardOnlySupported: bool = ..., cardBiometricSupported: bool = ..., cardPINSupported: bool = ..., cardBiometricOrPINSupported: bool = ..., cardBiometricPINSupported: bool = ..., idBiometricSupported: bool = ..., idPINSupported: bool = ..., idBiometricOrPINSupported: bool = ..., idBiometricPINSupported: bool = ..., extendedFaceOnlySupported: bool = ..., extendedFaceFingerprintSupported: bool = ..., extendedFacePINSupported: bool = ..., extendedFaceFingerprintOrPINSupported: bool = ..., extendedFaceFingerprintPINSupported: bool = ..., extendedFingerprintOnlySupported: bool = ..., extendedFingerprintFaceSupported: bool = ..., extendedFingerprintPINSupported: bool = ..., extendedFingerprintFaceOrPINSupported: bool = ..., extendedFingerprintFacePINSupported: bool = ..., extendedCardOnlySupported: bool = ..., extendedCardFaceSupported: bool = ..., extendedCardFingerprintSupported: bool = ..., extendedCardPINSupported: bool = ..., extendedCardFaceOrFingerprintSupported: bool = ..., extendedCardFaceOrPINSupported: bool = ..., extendedCardFingerprintOrPINSupported: bool = ..., extendedCardFaceOrFingerprintOrPINSupported: bool = ..., extendedCardFaceFingerprintSupported: bool = ..., extendedCardFacePINSupported: bool = ..., extendedCardFingerprintFaceSupported: bool = ..., extendedCardFingerprintPINSupported: bool = ..., extendedCardFaceOrFingerprintPINSupported: bool = ..., extendedCardFaceFingerprintOrPINSupported: bool = ..., extendedCardFingerprintFaceOrPINSupported: bool = ..., extendedIdFaceSupported: bool = ..., extendedIdFingerprintSupported: bool = ..., extendedIdPINSupported: bool = ..., extendedIdFaceOrFingerprintSupported: bool = ..., extendedIdFaceOrPINSupported: bool = ..., extendedIdFingerprintOrPINSupported: bool = ..., extendedIdFaceOrFingerprintOrPINSupported: bool = ..., extendedIdFaceFingerprintSupported: bool = ..., extendedIdFacePINSupported: bool = ..., extendedIdFingerprintFaceSupported: bool = ..., extendedIdFingerprintPINSupported: bool = ..., extendedIdFaceOrFingerprintPINSupported: bool = ..., extendedIdFaceFingerprintOrPINSupported: bool = ..., extendedIdFingerprintFaceOrPINSupported: bool = ..., intelligentPDSupported: bool = ..., updateUserSupported: bool = ..., simulatedUnlockSupported: bool = ..., smartCardByteOrderSupported: bool = ..., qrAsCSNSupported: bool = ..., rtspSupported: bool = ..., lfdSupported: bool = ..., visualQRSupported: bool = ..., maxVoipExtensionNumbers: _Optional[int] = ..., osdpStandardCentralSupported: bool = ..., enableLicenseFuncSupported: bool = ..., keypadBacklightSupported: bool = ..., uzWirelessLockDoorSupported: bool = ..., customSmartCardSupported: bool = ..., tomSupported: bool = ..., tomEnrollSupported: bool = ..., showOsdpResultbyLED: bool = ..., customSmartCardFelicaSupported: bool = ..., ignoreInputAfterWiegandOut: bool = ..., setSlaveBaudrateSupported: bool = ..., changeRtspResolutionSupported: bool = ..., changeVoipResolutionSupported: bool = ..., changeVoipTransportSupported: bool = ..., showOptionUserInfoSupported: bool = ..., changeScrambleKeypadSupported: bool = ..., visualFaceTemplateVersion: _Optional[int] = ..., authOnlyUnMaskSupported: bool = ..., mifareExSupported: bool = ..., lockOverrideSupported: bool = ..., doorModeOverrideSupported: bool = ..., extendedDoorOpenTimeSupported: bool = ..., realtimeDeviceIOStatusSupported: bool = ..., dynamicSlaveDeviceSupported: bool = ..., secureTamperSupported: bool = ..., customSmartcardSlaveSupported: bool = ..., serverPrivateMsgSupported: bool = ..., facilityCodeSupported: bool = ..., masterAdminSupported: bool = ..., adminTwoStepAuthSupported: bool = ...) -> None: ...

class GetCapabilityResponse(_message.Message):
    __slots__ = ("deviceCapability",)
    DEVICECAPABILITY_FIELD_NUMBER: _ClassVar[int]
    deviceCapability: DeviceCapability
    def __init__(self, deviceCapability: _Optional[_Union[DeviceCapability, _Mapping]] = ...) -> None: ...

class GetCapabilityInfoRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class CapabilityInfo(_message.Message):
    __slots__ = ("type", "maxNumOfUser", "PINSupported", "cardSupported", "card1xSupported", "SEOSSupported", "fingerSupported", "faceSupported", "userNameSupported", "userPhotoSupported", "userPhraseSupported", "alphanumericIDSupported", "WLANSupported", "imageLogSupported", "VOIPSupported", "TNASupported", "jobCodeSupported", "wiegandSupported", "wiegandMultiSupported", "triggerActionSupported", "DSTSupported", "DNSSupported", "OSDPKeySupported", "RS485ExtSupported", "QRSupported", "dynamicSlaveDeviceSupported")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MAXNUMOFUSER_FIELD_NUMBER: _ClassVar[int]
    PINSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CARD1XSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SEOSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FINGERSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    FACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    USERNAMESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    USERPHOTOSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    USERPHRASESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ALPHANUMERICIDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    WLANSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IMAGELOGSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VOIPSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TNASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    JOBCODESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    WIEGANDSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    WIEGANDMULTISUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TRIGGERACTIONSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DSTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DNSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    OSDPKEYSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RS485EXTSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    QRSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DYNAMICSLAVEDEVICESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    type: Type
    maxNumOfUser: int
    PINSupported: bool
    cardSupported: bool
    card1xSupported: bool
    SEOSSupported: bool
    fingerSupported: bool
    faceSupported: bool
    userNameSupported: bool
    userPhotoSupported: bool
    userPhraseSupported: bool
    alphanumericIDSupported: bool
    WLANSupported: bool
    imageLogSupported: bool
    VOIPSupported: bool
    TNASupported: bool
    jobCodeSupported: bool
    wiegandSupported: bool
    wiegandMultiSupported: bool
    triggerActionSupported: bool
    DSTSupported: bool
    DNSSupported: bool
    OSDPKeySupported: bool
    RS485ExtSupported: bool
    QRSupported: bool
    dynamicSlaveDeviceSupported: bool
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., maxNumOfUser: _Optional[int] = ..., PINSupported: bool = ..., cardSupported: bool = ..., card1xSupported: bool = ..., SEOSSupported: bool = ..., fingerSupported: bool = ..., faceSupported: bool = ..., userNameSupported: bool = ..., userPhotoSupported: bool = ..., userPhraseSupported: bool = ..., alphanumericIDSupported: bool = ..., WLANSupported: bool = ..., imageLogSupported: bool = ..., VOIPSupported: bool = ..., TNASupported: bool = ..., jobCodeSupported: bool = ..., wiegandSupported: bool = ..., wiegandMultiSupported: bool = ..., triggerActionSupported: bool = ..., DSTSupported: bool = ..., DNSSupported: bool = ..., OSDPKeySupported: bool = ..., RS485ExtSupported: bool = ..., QRSupported: bool = ..., dynamicSlaveDeviceSupported: bool = ...) -> None: ...

class GetCapabilityInfoResponse(_message.Message):
    __slots__ = ("capInfo",)
    CAPINFO_FIELD_NUMBER: _ClassVar[int]
    capInfo: CapabilityInfo
    def __init__(self, capInfo: _Optional[_Union[CapabilityInfo, _Mapping]] = ...) -> None: ...

class DeleteRootCARequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class DeleteRootCAResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class LockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class LockMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UnlockRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class UnlockResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class UnlockMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class RebootRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class RebootResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RebootMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class RebootMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class FactoryResetRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class FactoryResetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FactoryResetMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class FactoryResetMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class ClearDBRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class ClearDBResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearDBMultiRequest(_message.Message):
    __slots__ = ("deviceIDs",)
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ClearDBMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class ResetConfigRequest(_message.Message):
    __slots__ = ("deviceID", "withNetwork", "withDB")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    WITHNETWORK_FIELD_NUMBER: _ClassVar[int]
    WITHDB_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    withNetwork: bool
    withDB: bool
    def __init__(self, deviceID: _Optional[int] = ..., withNetwork: bool = ..., withDB: bool = ...) -> None: ...

class ResetConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetConfigMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "withNetwork", "withDB")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    WITHNETWORK_FIELD_NUMBER: _ClassVar[int]
    WITHDB_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    withNetwork: bool
    withDB: bool
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., withNetwork: bool = ..., withDB: bool = ...) -> None: ...

class ResetConfigMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class UpgradeFirmwareRequest(_message.Message):
    __slots__ = ("deviceID", "firmwareData")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREDATA_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    firmwareData: bytes
    def __init__(self, deviceID: _Optional[int] = ..., firmwareData: _Optional[bytes] = ...) -> None: ...

class UpgradeFirmwareResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpgradeFirmwareMultiRequest(_message.Message):
    __slots__ = ("deviceIDs", "firmwareData")
    DEVICEIDS_FIELD_NUMBER: _ClassVar[int]
    FIRMWAREDATA_FIELD_NUMBER: _ClassVar[int]
    deviceIDs: _containers.RepeatedScalarFieldContainer[int]
    firmwareData: bytes
    def __init__(self, deviceIDs: _Optional[_Iterable[int]] = ..., firmwareData: _Optional[bytes] = ...) -> None: ...

class UpgradeFirmwareMultiResponse(_message.Message):
    __slots__ = ("deviceErrors",)
    DEVICEERRORS_FIELD_NUMBER: _ClassVar[int]
    deviceErrors: _containers.RepeatedCompositeFieldContainer[_err_pb2.ErrorResponse]
    def __init__(self, deviceErrors: _Optional[_Iterable[_Union[_err_pb2.ErrorResponse, _Mapping]]] = ...) -> None: ...

class GetHashKeyRequest(_message.Message):
    __slots__ = ("deviceID",)
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    def __init__(self, deviceID: _Optional[int] = ...) -> None: ...

class GetHashKeyResponse(_message.Message):
    __slots__ = ("isDefault", "checksum")
    ISDEFAULT_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    isDefault: bool
    checksum: int
    def __init__(self, isDefault: bool = ..., checksum: _Optional[int] = ...) -> None: ...

class SetHashKeyRequest(_message.Message):
    __slots__ = ("deviceID", "setDefault", "hashKey")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    SETDEFAULT_FIELD_NUMBER: _ClassVar[int]
    HASHKEY_FIELD_NUMBER: _ClassVar[int]
    deviceID: int
    setDefault: bool
    hashKey: bytes
    def __init__(self, deviceID: _Optional[int] = ..., setDefault: bool = ..., hashKey: _Optional[bytes] = ...) -> None: ...

class SetHashKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
