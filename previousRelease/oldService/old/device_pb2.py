# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x64\x65vice.proto\x12\x0bgsdk.device\x1a\terr.proto\"\"\n\x0eGetInfoRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x8e\x01\n\x0b\x46\x61\x63toryInfo\x12\x0f\n\x07MACAddr\x18\x02 \x01(\t\x12\x11\n\tmodelName\x18\x03 \x01(\t\x12\x17\n\x0f\x66irmwareVersion\x18\x04 \x01(\t\x12\x15\n\rkernelVersion\x18\x05 \x01(\t\x12\x15\n\rBSCoreVersion\x18\x06 \x01(\t\x12\x14\n\x0c\x62oardVersion\x18\x07 \x01(\t\"9\n\x0fGetInfoResponse\x12&\n\x04info\x18\x01 \x01(\x0b\x32\x18.gsdk.device.FactoryInfo\"(\n\x14GetCapabilityRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\xd9\x19\n\x10\x44\x65viceCapability\x12\x10\n\x08maxUsers\x18\x01 \x01(\r\x12\x14\n\x0cmaxEventLogs\x18\x02 \x01(\r\x12\x14\n\x0cmaxImageLogs\x18\x03 \x01(\r\x12\x15\n\rmaxBlacklists\x18\x04 \x01(\r\x12\x14\n\x0cmaxOperators\x18\x05 \x01(\r\x12\x10\n\x08maxCards\x18\x06 \x01(\r\x12\x10\n\x08maxFaces\x18\x07 \x01(\r\x12\x17\n\x0fmaxFingerprints\x18\x08 \x01(\r\x12\x14\n\x0cmaxUserNames\x18\t \x01(\r\x12\x15\n\rmaxUserImages\x18\n \x01(\r\x12\x13\n\x0bmaxUserJobs\x18\x0b \x01(\r\x12\x16\n\x0emaxUserPhrases\x18\x0c \x01(\r\x12\x17\n\x0fmaxCardsPerUser\x18\r \x01(\r\x12\x17\n\x0fmaxFacesPerUser\x18\x0e \x01(\r\x12\x1e\n\x16maxFingerprintsPerUser\x18\x0f \x01(\r\x12\x15\n\rmaxInputPorts\x18\x10 \x01(\r\x12\x16\n\x0emaxOutputPorts\x18\x11 \x01(\r\x12\x11\n\tmaxRelays\x18\x12 \x01(\r\x12\x18\n\x10maxRS485Channels\x18\x13 \x01(\r\x12\x17\n\x0f\x63\x61meraSupported\x18\x14 \x01(\x08\x12\x17\n\x0ftamperSupported\x18\x15 \x01(\x08\x12\x15\n\rwlanSupported\x18\x16 \x01(\x08\x12\x18\n\x10\x64isplaySupported\x18\x17 \x01(\x08\x12\x18\n\x10thermalSupported\x18\x18 \x01(\x08\x12\x15\n\rmaskSupported\x18\x19 \x01(\x08\x12\x17\n\x0f\x66\x61\x63\x65\x45xSupported\x18\x1a \x01(\x08\x12\x17\n\x0f\x45MCardSupported\x18\x1b \x01(\x08\x12\x1c\n\x14HIDProxCardSupported\x18\x1c \x01(\x08\x12!\n\x19MifareFelicaCardSupported\x18\x1d \x01(\x08\x12\x1b\n\x13iClassCardSupported\x18\x1e \x01(\x08\x12 \n\x18\x43lassicPlusCardSupported\x18\x1f \x01(\x08\x12\x1f\n\x17\x44\x65sFireEV1CardSupported\x18  \x01(\x08\x12\x19\n\x11SRSECardSupported\x18! \x01(\x08\x12\x19\n\x11SEOSCardSupported\x18\" \x01(\x08\x12\x14\n\x0cNFCSupported\x18# \x01(\x08\x12\x14\n\x0c\x42LESupported\x18$ \x01(\x08\x12\x18\n\x10useCardOperation\x18% \x01(\x08\x12\x1d\n\x15\x65xtendedAuthSupported\x18& \x01(\x08\x12\x1a\n\x12\x63\x61rdInputSupported\x18\' \x01(\x08\x12!\n\x19\x66ingerprintInputSupported\x18( \x01(\x08\x12\x1a\n\x12\x66\x61\x63\x65InputSupported\x18) \x01(\x08\x12\x18\n\x10idInputSupported\x18* \x01(\x08\x12\x19\n\x11PINInputSupported\x18+ \x01(\x08\x12\x1e\n\x16\x62iometricOnlySupported\x18, \x01(\x08\x12\x1d\n\x15\x62iometricPINSupported\x18- \x01(\x08\x12\x19\n\x11\x63\x61rdOnlySupported\x18. \x01(\x08\x12\x1e\n\x16\x63\x61rdBiometricSupported\x18/ \x01(\x08\x12\x18\n\x10\x63\x61rdPINSupported\x18\x30 \x01(\x08\x12#\n\x1b\x63\x61rdBiometricOrPINSupported\x18\x31 \x01(\x08\x12!\n\x19\x63\x61rdBiometricPINSupported\x18\x32 \x01(\x08\x12\x1c\n\x14idBiometricSupported\x18\x33 \x01(\x08\x12\x16\n\x0eidPINSupported\x18\x34 \x01(\x08\x12!\n\x19idBiometricOrPINSupported\x18\x35 \x01(\x08\x12\x1f\n\x17idBiometricPINSupported\x18\x36 \x01(\x08\x12!\n\x19\x65xtendedFaceOnlySupported\x18\x37 \x01(\x08\x12(\n extendedFaceFingerprintSupported\x18\x38 \x01(\x08\x12 \n\x18\x65xtendedFacePINSupported\x18\x39 \x01(\x08\x12-\n%extendedFaceFingerprintOrPINSupported\x18: \x01(\x08\x12+\n#extendedFaceFingerprintPINSupported\x18; \x01(\x08\x12(\n extendedFingerprintOnlySupported\x18< \x01(\x08\x12(\n extendedFingerprintFaceSupported\x18= \x01(\x08\x12\'\n\x1f\x65xtendedFingerprintPINSupported\x18> \x01(\x08\x12-\n%extendedFingerprintFaceOrPINSupported\x18? \x01(\x08\x12+\n#extendedFingerprintFacePINSupported\x18@ \x01(\x08\x12!\n\x19\x65xtendedCardOnlySupported\x18\x41 \x01(\x08\x12!\n\x19\x65xtendedCardFaceSupported\x18\x42 \x01(\x08\x12(\n extendedCardFingerprintSupported\x18\x43 \x01(\x08\x12 \n\x18\x65xtendedCardPINSupported\x18\x44 \x01(\x08\x12.\n&extendedCardFaceOrFingerprintSupported\x18\x45 \x01(\x08\x12&\n\x1e\x65xtendedCardFaceOrPINSupported\x18\x46 \x01(\x08\x12-\n%extendedCardFingerprintOrPINSupported\x18G \x01(\x08\x12\x33\n+extendedCardFaceOrFingerprintOrPINSupported\x18H \x01(\x08\x12,\n$extendedCardFaceFingerprintSupported\x18I \x01(\x08\x12$\n\x1c\x65xtendedCardFacePINSupported\x18J \x01(\x08\x12,\n$extendedCardFingerprintFaceSupported\x18K \x01(\x08\x12+\n#extendedCardFingerprintPINSupported\x18L \x01(\x08\x12\x31\n)extendedCardFaceOrFingerprintPINSupported\x18M \x01(\x08\x12\x31\n)extendedCardFaceFingerprintOrPINSupported\x18N \x01(\x08\x12\x31\n)extendedCardFingerprintFaceOrPINSupported\x18O \x01(\x08\x12\x1f\n\x17\x65xtendedIdFaceSupported\x18P \x01(\x08\x12&\n\x1e\x65xtendedIdFingerprintSupported\x18Q \x01(\x08\x12\x1e\n\x16\x65xtendedIdPINSupported\x18R \x01(\x08\x12,\n$extendedIdFaceOrFingerprintSupported\x18S \x01(\x08\x12$\n\x1c\x65xtendedIdFaceOrPINSupported\x18T \x01(\x08\x12+\n#extendedIdFingerprintOrPINSupported\x18U \x01(\x08\x12\x31\n)extendedIdFaceOrFingerprintOrPINSupported\x18V \x01(\x08\x12*\n\"extendedIdFaceFingerprintSupported\x18W \x01(\x08\x12\"\n\x1a\x65xtendedIdFacePINSupported\x18X \x01(\x08\x12*\n\"extendedIdFingerprintFaceSupported\x18Y \x01(\x08\x12)\n!extendedIdFingerprintPINSupported\x18Z \x01(\x08\x12/\n\'extendedIdFaceOrFingerprintPINSupported\x18[ \x01(\x08\x12/\n\'extendedIdFaceFingerprintOrPINSupported\x18\\ \x01(\x08\x12/\n\'extendedIdFingerprintFaceOrPINSupported\x18] \x01(\x08\x12\x1e\n\x16intelligentPDSupported\x18^ \x01(\x08\x12\x1b\n\x13updateUserSupported\x18_ \x01(\x08\x12 \n\x18simulatedUnlockSupported\x18` \x01(\x08\x12#\n\x1bsmartCardByteOrderSupported\x18\x61 \x01(\x08\x12\x18\n\x10qrAsCSNSupported\x18\x62 \x01(\x08\"P\n\x15GetCapabilityResponse\x12\x37\n\x10\x64\x65viceCapability\x18\x01 \x01(\x0b\x32\x1d.gsdk.device.DeviceCapability\",\n\x18GetCapabilityInfoRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x91\x05\n\x0e\x43\x61pabilityInfo\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.gsdk.device.Type\x12\x14\n\x0cmaxNumOfUser\x18\x02 \x01(\r\x12\x14\n\x0cPINSupported\x18\x03 \x01(\x08\x12\x15\n\rcardSupported\x18\x04 \x01(\x08\x12\x17\n\x0f\x63\x61rd1xSupported\x18\x05 \x01(\x08\x12\x15\n\rSEOSSupported\x18\x06 \x01(\x08\x12\x17\n\x0f\x66ingerSupported\x18\x07 \x01(\x08\x12\x15\n\rfaceSupported\x18\x08 \x01(\x08\x12\x19\n\x11userNameSupported\x18\n \x01(\x08\x12\x1a\n\x12userPhotoSupported\x18\x0b \x01(\x08\x12\x1b\n\x13userPhraseSupported\x18\x0c \x01(\x08\x12\x1f\n\x17\x61lphanumericIDSupported\x18\r \x01(\x08\x12\x15\n\rWLANSupported\x18\x14 \x01(\x08\x12\x19\n\x11imageLogSupported\x18\x15 \x01(\x08\x12\x15\n\rVOIPSupported\x18\x16 \x01(\x08\x12\x14\n\x0cTNASupported\x18\x1e \x01(\x08\x12\x18\n\x10jobCodeSupported\x18\x1f \x01(\x08\x12\x18\n\x10wiegandSupported\x18( \x01(\x08\x12\x1d\n\x15wiegandMultiSupported\x18) \x01(\x08\x12\x1e\n\x16triggerActionSupported\x18* \x01(\x08\x12\x14\n\x0c\x44STSupported\x18+ \x01(\x08\x12\x14\n\x0c\x44NSSupported\x18, \x01(\x08\x12\x18\n\x10OSDPKeySupported\x18\x32 \x01(\x08\x12\x19\n\x11RS485ExtSupported\x18\x33 \x01(\x08\x12\x13\n\x0bQRSupported\x18< \x01(\x08\"I\n\x19GetCapabilityInfoResponse\x12,\n\x07\x63\x61pInfo\x18\x01 \x01(\x0b\x32\x1b.gsdk.device.CapabilityInfo\"\'\n\x13\x44\x65leteRootCARequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x16\n\x14\x44\x65leteRootCAResponse\"\x1f\n\x0bLockRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x0e\n\x0cLockResponse\"%\n\x10LockMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"B\n\x11LockMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"!\n\rUnlockRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x10\n\x0eUnlockResponse\"\'\n\x12UnlockMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"D\n\x13UnlockMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"!\n\rRebootRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x10\n\x0eRebootResponse\"\'\n\x12RebootMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"D\n\x13RebootMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\'\n\x13\x46\x61\x63toryResetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x16\n\x14\x46\x61\x63toryResetResponse\"-\n\x18\x46\x61\x63toryResetMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"J\n\x19\x46\x61\x63toryResetMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\"\n\x0e\x43learDBRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x11\n\x0f\x43learDBResponse\"(\n\x13\x43learDBMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"E\n\x14\x43learDBMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"K\n\x12ResetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x13\n\x0bwithNetwork\x18\x02 \x01(\x08\x12\x0e\n\x06withDB\x18\x03 \x01(\x08\"\x15\n\x13ResetConfigResponse\"Q\n\x17ResetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x13\n\x0bwithNetwork\x18\x02 \x01(\x08\x12\x0e\n\x06withDB\x18\x03 \x01(\x08\"I\n\x18ResetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"@\n\x16UpgradeFirmwareRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0c\x66irmwareData\x18\x02 \x01(\x0c\"\x19\n\x17UpgradeFirmwareResponse\"F\n\x1bUpgradeFirmwareMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x14\n\x0c\x66irmwareData\x18\x02 \x01(\x0c\"M\n\x1cUpgradeFirmwareMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"%\n\x11GetHashKeyRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"9\n\x12GetHashKeyResponse\x12\x11\n\tisDefault\x18\x01 \x01(\x08\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\r\"J\n\x11SetHashKeyRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x12\n\nsetDefault\x18\x02 \x01(\x08\x12\x0f\n\x07hashKey\x18\x03 \x01(\x0c\"\x14\n\x12SetHashKeyResponse*\x81\x05\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\x11\n\rBIOENTRY_PLUS\x10\x01\x12\x0e\n\nBIOENTRY_W\x10\x02\x12\x0f\n\x0b\x42IOLITE_NET\x10\x03\x12\t\n\x05XPASS\x10\x04\x12\x0c\n\x08XPASS_S2\x10\x05\x12\r\n\tENTRY_MAX\x10\x05\x12\x0f\n\x0bSECURE_IO_2\x10\x06\x12\x12\n\x0e\x44OOR_MODULE_20\x10\x07\x12\x10\n\x0c\x42IOSTATION_2\x10\x08\x12\x11\n\rBIOSTATION_A2\x10\t\x12\x11\n\rFACESTATION_2\x10\n\x12\r\n\tIO_DEVICE\x10\x0b\x12\x11\n\rBIOSTATION_L2\x10\x0c\x12\x0f\n\x0b\x42IOENTRY_W2\x10\r\x12\x10\n\x0bRS485_SLAVE\x10\x80\x01\x12\x12\n\x0e\x43ORESTATION_40\x10\x0e\x12\x11\n\rOUTPUT_MODULE\x10\x0f\x12\x10\n\x0cINPUT_MODULE\x10\x10\x12\x0f\n\x0b\x42IOENTRY_P2\x10\x11\x12\x0e\n\nBIOLITE_N2\x10\x12\x12\n\n\x06XPASS2\x10\x13\x12\x0c\n\x08XPASS_S3\x10\x14\x12\x0f\n\x0b\x42IOENTRY_R2\x10\x15\x12\x0c\n\x08XPASS_D2\x10\x16\x12\x12\n\x0e\x44OOR_MODULE_21\x10\x17\x12\x13\n\x0fXPASS_D2_KEYPAD\x10\x18\x12\x0c\n\x08\x46\x41\x43\x45LITE\x10\x19\x12\x11\n\rXPASS2_KEYPAD\x10\x1a\x12\x15\n\x11\x46\x41\x43\x45STATION_F2_FP\x10\x1d\x12\x12\n\x0e\x46\x41\x43\x45STATION_F2\x10\x1e\x12\x11\n\rXSTATION_2_QR\x10\x1f\x12\x0e\n\nXSTATION_2\x10 \x12\n\n\x06IM_120\x10!\x12\x11\n\rXSTATION_2_FP\x10\"\x12\x10\n\x0c\x42IOSTATION_3\x10#\x12\x0c\n\x07UNKNOWN\x10\xff\x01\x1a\x02\x10\x01*4\n\nSwitchType\x12\x11\n\rNORMALLY_OPEN\x10\x00\x12\x13\n\x0fNORMALLY_CLOSED\x10\x01*\xaf\x01\n\x08LEDColor\x12\x11\n\rLED_COLOR_OFF\x10\x00\x12\x11\n\rLED_COLOR_RED\x10\x01\x12\x14\n\x10LED_COLOR_YELLOW\x10\x02\x12\x13\n\x0fLED_COLOR_GREEN\x10\x03\x12\x12\n\x0eLED_COLOR_CYAN\x10\x04\x12\x12\n\x0eLED_COLOR_BLUE\x10\x05\x12\x15\n\x11LED_COLOR_MAGENTA\x10\x06\x12\x13\n\x0fLED_COLOR_WHITE\x10\x07*d\n\nBuzzerTone\x12\x13\n\x0f\x42UZZER_TONE_OFF\x10\x00\x12\x13\n\x0f\x42UZZER_TONE_LOW\x10\x01\x12\x16\n\x12\x42UZZER_TONE_MIDDLE\x10\x02\x12\x14\n\x10\x42UZZER_TONE_HIGH\x10\x03\x32\x82\r\n\x06\x44\x65vice\x12\x44\n\x07GetInfo\x12\x1b.gsdk.device.GetInfoRequest\x1a\x1c.gsdk.device.GetInfoResponse\x12V\n\rGetCapability\x12!.gsdk.device.GetCapabilityRequest\x1a\".gsdk.device.GetCapabilityResponse\x12\x62\n\x11GetCapabilityInfo\x12%.gsdk.device.GetCapabilityInfoRequest\x1a&.gsdk.device.GetCapabilityInfoResponse\x12S\n\x0c\x44\x65leteRootCA\x12 .gsdk.device.DeleteRootCARequest\x1a!.gsdk.device.DeleteRootCAResponse\x12;\n\x04Lock\x12\x18.gsdk.device.LockRequest\x1a\x19.gsdk.device.LockResponse\x12J\n\tLockMulti\x12\x1d.gsdk.device.LockMultiRequest\x1a\x1e.gsdk.device.LockMultiResponse\x12\x41\n\x06Unlock\x12\x1a.gsdk.device.UnlockRequest\x1a\x1b.gsdk.device.UnlockResponse\x12P\n\x0bUnlockMulti\x12\x1f.gsdk.device.UnlockMultiRequest\x1a .gsdk.device.UnlockMultiResponse\x12\x41\n\x06Reboot\x12\x1a.gsdk.device.RebootRequest\x1a\x1b.gsdk.device.RebootResponse\x12P\n\x0bRebootMulti\x12\x1f.gsdk.device.RebootMultiRequest\x1a .gsdk.device.RebootMultiResponse\x12S\n\x0c\x46\x61\x63toryReset\x12 .gsdk.device.FactoryResetRequest\x1a!.gsdk.device.FactoryResetResponse\x12\x62\n\x11\x46\x61\x63toryResetMulti\x12%.gsdk.device.FactoryResetMultiRequest\x1a&.gsdk.device.FactoryResetMultiResponse\x12\x44\n\x07\x43learDB\x12\x1b.gsdk.device.ClearDBRequest\x1a\x1c.gsdk.device.ClearDBResponse\x12S\n\x0c\x43learDBMulti\x12 .gsdk.device.ClearDBMultiRequest\x1a!.gsdk.device.ClearDBMultiResponse\x12P\n\x0bResetConfig\x12\x1f.gsdk.device.ResetConfigRequest\x1a .gsdk.device.ResetConfigResponse\x12_\n\x10ResetConfigMulti\x12$.gsdk.device.ResetConfigMultiRequest\x1a%.gsdk.device.ResetConfigMultiResponse\x12\\\n\x0fUpgradeFirmware\x12#.gsdk.device.UpgradeFirmwareRequest\x1a$.gsdk.device.UpgradeFirmwareResponse\x12k\n\x14UpgradeFirmwareMulti\x12(.gsdk.device.UpgradeFirmwareMultiRequest\x1a).gsdk.device.UpgradeFirmwareMultiResponse\x12M\n\nGetHashKey\x12\x1e.gsdk.device.GetHashKeyRequest\x1a\x1f.gsdk.device.GetHashKeyResponse\x12M\n\nSetHashKey\x12\x1e.gsdk.device.SetHashKeyRequest\x1a\x1f.gsdk.device.SetHashKeyResponseB5\n\x19\x63om.supremainc.sdk.deviceP\x01Z\x16\x62iostar/service/deviceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'device_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.supremainc.sdk.deviceP\001Z\026biostar/service/device'
  _TYPE._options = None
  _TYPE._serialized_options = b'\020\001'
  _TYPE._serialized_start=6081
  _TYPE._serialized_end=6722
  _SWITCHTYPE._serialized_start=6724
  _SWITCHTYPE._serialized_end=6776
  _LEDCOLOR._serialized_start=6779
  _LEDCOLOR._serialized_end=6954
  _BUZZERTONE._serialized_start=6956
  _BUZZERTONE._serialized_end=7056
  _GETINFOREQUEST._serialized_start=40
  _GETINFOREQUEST._serialized_end=74
  _FACTORYINFO._serialized_start=77
  _FACTORYINFO._serialized_end=219
  _GETINFORESPONSE._serialized_start=221
  _GETINFORESPONSE._serialized_end=278
  _GETCAPABILITYREQUEST._serialized_start=280
  _GETCAPABILITYREQUEST._serialized_end=320
  _DEVICECAPABILITY._serialized_start=323
  _DEVICECAPABILITY._serialized_end=3612
  _GETCAPABILITYRESPONSE._serialized_start=3614
  _GETCAPABILITYRESPONSE._serialized_end=3694
  _GETCAPABILITYINFOREQUEST._serialized_start=3696
  _GETCAPABILITYINFOREQUEST._serialized_end=3740
  _CAPABILITYINFO._serialized_start=3743
  _CAPABILITYINFO._serialized_end=4400
  _GETCAPABILITYINFORESPONSE._serialized_start=4402
  _GETCAPABILITYINFORESPONSE._serialized_end=4475
  _DELETEROOTCAREQUEST._serialized_start=4477
  _DELETEROOTCAREQUEST._serialized_end=4516
  _DELETEROOTCARESPONSE._serialized_start=4518
  _DELETEROOTCARESPONSE._serialized_end=4540
  _LOCKREQUEST._serialized_start=4542
  _LOCKREQUEST._serialized_end=4573
  _LOCKRESPONSE._serialized_start=4575
  _LOCKRESPONSE._serialized_end=4589
  _LOCKMULTIREQUEST._serialized_start=4591
  _LOCKMULTIREQUEST._serialized_end=4628
  _LOCKMULTIRESPONSE._serialized_start=4630
  _LOCKMULTIRESPONSE._serialized_end=4696
  _UNLOCKREQUEST._serialized_start=4698
  _UNLOCKREQUEST._serialized_end=4731
  _UNLOCKRESPONSE._serialized_start=4733
  _UNLOCKRESPONSE._serialized_end=4749
  _UNLOCKMULTIREQUEST._serialized_start=4751
  _UNLOCKMULTIREQUEST._serialized_end=4790
  _UNLOCKMULTIRESPONSE._serialized_start=4792
  _UNLOCKMULTIRESPONSE._serialized_end=4860
  _REBOOTREQUEST._serialized_start=4862
  _REBOOTREQUEST._serialized_end=4895
  _REBOOTRESPONSE._serialized_start=4897
  _REBOOTRESPONSE._serialized_end=4913
  _REBOOTMULTIREQUEST._serialized_start=4915
  _REBOOTMULTIREQUEST._serialized_end=4954
  _REBOOTMULTIRESPONSE._serialized_start=4956
  _REBOOTMULTIRESPONSE._serialized_end=5024
  _FACTORYRESETREQUEST._serialized_start=5026
  _FACTORYRESETREQUEST._serialized_end=5065
  _FACTORYRESETRESPONSE._serialized_start=5067
  _FACTORYRESETRESPONSE._serialized_end=5089
  _FACTORYRESETMULTIREQUEST._serialized_start=5091
  _FACTORYRESETMULTIREQUEST._serialized_end=5136
  _FACTORYRESETMULTIRESPONSE._serialized_start=5138
  _FACTORYRESETMULTIRESPONSE._serialized_end=5212
  _CLEARDBREQUEST._serialized_start=5214
  _CLEARDBREQUEST._serialized_end=5248
  _CLEARDBRESPONSE._serialized_start=5250
  _CLEARDBRESPONSE._serialized_end=5267
  _CLEARDBMULTIREQUEST._serialized_start=5269
  _CLEARDBMULTIREQUEST._serialized_end=5309
  _CLEARDBMULTIRESPONSE._serialized_start=5311
  _CLEARDBMULTIRESPONSE._serialized_end=5380
  _RESETCONFIGREQUEST._serialized_start=5382
  _RESETCONFIGREQUEST._serialized_end=5457
  _RESETCONFIGRESPONSE._serialized_start=5459
  _RESETCONFIGRESPONSE._serialized_end=5480
  _RESETCONFIGMULTIREQUEST._serialized_start=5482
  _RESETCONFIGMULTIREQUEST._serialized_end=5563
  _RESETCONFIGMULTIRESPONSE._serialized_start=5565
  _RESETCONFIGMULTIRESPONSE._serialized_end=5638
  _UPGRADEFIRMWAREREQUEST._serialized_start=5640
  _UPGRADEFIRMWAREREQUEST._serialized_end=5704
  _UPGRADEFIRMWARERESPONSE._serialized_start=5706
  _UPGRADEFIRMWARERESPONSE._serialized_end=5731
  _UPGRADEFIRMWAREMULTIREQUEST._serialized_start=5733
  _UPGRADEFIRMWAREMULTIREQUEST._serialized_end=5803
  _UPGRADEFIRMWAREMULTIRESPONSE._serialized_start=5805
  _UPGRADEFIRMWAREMULTIRESPONSE._serialized_end=5882
  _GETHASHKEYREQUEST._serialized_start=5884
  _GETHASHKEYREQUEST._serialized_end=5921
  _GETHASHKEYRESPONSE._serialized_start=5923
  _GETHASHKEYRESPONSE._serialized_end=5980
  _SETHASHKEYREQUEST._serialized_start=5982
  _SETHASHKEYREQUEST._serialized_end=6056
  _SETHASHKEYRESPONSE._serialized_start=6058
  _SETHASHKEYRESPONSE._serialized_end=6078
  _DEVICE._serialized_start=7059
  _DEVICE._serialized_end=8725
# @@protoc_insertion_point(module_scope)