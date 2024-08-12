# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: card.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncard.proto\x12\tgsdk.card\x1a\terr.proto\"H\n\x0b\x43SNCardData\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.gsdk.card.Type\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xa2\x02\n\x0fSmartCardHeader\x12\x11\n\theaderCRC\x18\x01 \x01(\r\x12\x0f\n\x07\x63\x61rdCRC\x18\x02 \x01(\r\x12\x1d\n\x04type\x18\x03 \x01(\x0e\x32\x0f.gsdk.card.Type\x12\x17\n\rnumOfTemplate\x18\x04 \x01(\rH\x00\x12\x1b\n\x11numOfFaceTemplate\x18\n \x01(\rH\x00\x12\x14\n\x0ctemplateSize\x18\x05 \x01(\r\x12\x12\n\nissueCount\x18\x06 \x01(\r\x12\x12\n\nduressMask\x18\x07 \x01(\r\x12\x14\n\x0c\x63\x61rdAuthMode\x18\x08 \x01(\r\x12\x19\n\x11useAlphanumericID\x18\t \x01(\x08\x12\x16\n\x0e\x63\x61rdAuthModeEx\x18\x0b \x01(\rB\x0f\n\rtemplateCount\"5\n\x13SmartCardCredential\x12\x0b\n\x03PIN\x18\x01 \x01(\x0c\x12\x11\n\ttemplates\x18\x02 \x03(\x0c\"N\n\x10\x41\x63\x63\x65ssOnCardData\x12\x16\n\x0e\x61\x63\x63\x65ssGroupIDs\x18\x01 \x03(\r\x12\x11\n\tstartTime\x18\x02 \x01(\r\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\r\"\xb2\x01\n\rSmartCardData\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.gsdk.card.SmartCardHeader\x12\x0e\n\x06\x63\x61rdID\x18\x02 \x01(\x0c\x12\x32\n\ncredential\x18\x03 \x01(\x0b\x32\x1e.gsdk.card.SmartCardCredential\x12\x31\n\x0c\x61\x63\x63\x65ssOnData\x18\x04 \x01(\x0b\x32\x1b.gsdk.card.AccessOnCardData\"\x87\x01\n\x08\x43\x61rdData\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.gsdk.card.Type\x12+\n\x0b\x43SNCardData\x18\x02 \x01(\x0b\x32\x16.gsdk.card.CSNCardData\x12/\n\rsmartCardData\x18\x03 \x01(\x0b\x32\x18.gsdk.card.SmartCardData\"\x1f\n\x0bScanRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"5\n\x0cScanResponse\x12%\n\x08\x63\x61rdData\x18\x01 \x01(\x0b\x32\x13.gsdk.card.CardData\" \n\x0c\x45raseRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x0f\n\rEraseResponse\"Q\n\x0cWriteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12/\n\rsmartCardData\x18\x02 \x01(\x0b\x32\x18.gsdk.card.SmartCardData\"\x0f\n\rWriteResponse\"Q\n\x0cMifareConfig\x12\x12\n\nprimaryKey\x18\x01 \x01(\x0c\x12\x14\n\x0csecondaryKey\x18\x02 \x01(\x0c\x12\x17\n\x0fstartBlockIndex\x18\x03 \x01(\x05\"Q\n\x0cIClassConfig\x12\x12\n\nprimaryKey\x18\x01 \x01(\x0c\x12\x14\n\x0csecondaryKey\x18\x02 \x01(\x0c\x12\x17\n\x0fstartBlockIndex\x18\x03 \x01(\x05\"\xca\x01\n\rDESFireConfig\x12\x12\n\nprimaryKey\x18\x01 \x01(\x0c\x12\x14\n\x0csecondaryKey\x18\x02 \x01(\x0c\x12\r\n\x05\x61ppID\x18\x03 \x01(\x0c\x12\x0e\n\x06\x66ileID\x18\x04 \x01(\r\x12\x38\n\x0e\x65ncryptionType\x18\x05 \x01(\x0e\x32 .gsdk.card.DESFireEncryptionType\x12\x36\n\roperationMode\x18\x06 \x01(\x0e\x32\x1f.gsdk.card.DESFireOperationMode\"\x90\x01\n\nSEOSConfig\x12\x0e\n\x06OIDADF\x18\x01 \x01(\x0c\x12\x0f\n\x07sizeADF\x18\x02 \x01(\r\x12\x17\n\x0fOIDDataObjectID\x18\x03 \x03(\r\x12\x16\n\x0esizeDataObject\x18\x04 \x03(\r\x12\x16\n\x0eprimaryKeyAuth\x18\x05 \x01(\x0c\x12\x18\n\x10secondaryKeyAuth\x18\x06 \x01(\x0c\"\xa9\x03\n\nCardConfig\x12+\n\tbyteOrder\x18\x01 \x01(\x0e\x32\x18.gsdk.card.CardByteOrder\x12\x18\n\x10useWiegandFormat\x18\x02 \x01(\x08\x12)\n\x08\x64\x61taType\x18\x03 \x01(\x0e\x32\x17.gsdk.card.CardDataType\x12\x17\n\x0fuseSecondaryKey\x18\x04 \x01(\x08\x12-\n\x0cmifareConfig\x18\x05 \x01(\x0b\x32\x17.gsdk.card.MifareConfig\x12-\n\x0ciClassConfig\x18\x06 \x01(\x0b\x32\x17.gsdk.card.IClassConfig\x12/\n\rDESFireConfig\x18\x07 \x01(\x0b\x32\x18.gsdk.card.DESFireConfig\x12)\n\nSEOSConfig\x18\x08 \x01(\x0b\x32\x15.gsdk.card.SEOSConfig\x12\x10\n\x08\x66ormatID\x18\t \x01(\r\x12\x0e\n\x06\x63ipher\x18\n \x01(\x08\x12\x34\n\x12smartCardByteOrder\x18\x0b \x01(\x0e\x32\x18.gsdk.card.CardByteOrder\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\":\n\x11GetConfigResponse\x12%\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x15.gsdk.card.CardConfig\"K\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.card.CardConfig\"\x13\n\x11SetConfigResponse\"Q\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.gsdk.card.CardConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"3\n\rBlacklistItem\x12\x0e\n\x06\x63\x61rdID\x18\x01 \x01(\x0c\x12\x12\n\nissueCount\x18\x02 \x01(\r\"\'\n\x13GetBlacklistRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"C\n\x14GetBlacklistResponse\x12+\n\tblacklist\x18\x01 \x03(\x0b\x32\x18.gsdk.card.BlacklistItem\"T\n\x13\x41\x64\x64\x42lacklistRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12+\n\tcardInfos\x18\x02 \x03(\x0b\x32\x18.gsdk.card.BlacklistItem\"\x16\n\x14\x41\x64\x64\x42lacklistResponse\"Z\n\x18\x41\x64\x64\x42lacklistMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12+\n\tcardInfos\x18\x02 \x03(\x0b\x32\x18.gsdk.card.BlacklistItem\"J\n\x19\x41\x64\x64\x42lacklistMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"W\n\x16\x44\x65leteBlacklistRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12+\n\tcardInfos\x18\x02 \x03(\x0b\x32\x18.gsdk.card.BlacklistItem\"\x19\n\x17\x44\x65leteBlacklistResponse\"]\n\x1b\x44\x65leteBlacklistMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12+\n\tcardInfos\x18\x02 \x03(\x0b\x32\x18.gsdk.card.BlacklistItem\"M\n\x1c\x44\x65leteBlacklistMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"-\n\x19\x44\x65leteAllBlacklistRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x1c\n\x1a\x44\x65leteAllBlacklistResponse\"3\n\x1e\x44\x65leteAllBlacklistMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"P\n\x1f\x44\x65leteAllBlacklistMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"\xef\x01\n\x0c\x43\x61rd1XConfig\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12\x12\n\nuseCSNOnly\x18\x02 \x01(\x08\x12\x1a\n\x12\x62ioEntryCompatible\x18\x03 \x01(\x08\x12\x17\n\x0fuseSecondaryKey\x18\x04 \x01(\x08\x12\x12\n\nprimaryKey\x18\x05 \x01(\x0c\x12\x14\n\x0csecondaryKey\x18\x06 \x01(\x0c\x12\x10\n\x08\x43ISIndex\x18\x07 \x01(\r\x12\x15\n\rnumOfTemplate\x18\x08 \x01(\r\x12\x14\n\x0ctemplateSize\x18\t \x01(\r\x12\x1b\n\x13templateStartBlocks\x18\n \x03(\r\"&\n\x12Get1XConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\">\n\x13Get1XConfigResponse\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.gsdk.card.Card1XConfig\"O\n\x12Set1XConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.gsdk.card.Card1XConfig\"\x15\n\x13Set1XConfigResponse\"U\n\x17Set1XConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.gsdk.card.Card1XConfig\"I\n\x18Set1XConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"$\n\x12WriteQRCodeRequest\x12\x0e\n\x06QRText\x18\x01 \x01(\t\"?\n\x13WriteQRCodeResponse\x12(\n\x08\x63\x61rdData\x18\x01 \x01(\x0b\x32\x16.gsdk.card.CSNCardData\"Z\n\x08QRConfig\x12\x11\n\tuseQRCode\x18\x01 \x01(\x08\x12\x13\n\x0bscanTimeout\x18\x02 \x01(\r\x12\x12\n\nbypassData\x18\x03 \x01(\x08\x12\x12\n\ntreatAsCSN\x18\x04 \x01(\x08\"&\n\x12GetQRConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\":\n\x13GetQRConfigResponse\x12#\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x13.gsdk.card.QRConfig\"K\n\x12SetQRConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.gsdk.card.QRConfig\"\x15\n\x13SetQRConfigResponse\"Q\n\x17SetQRConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12#\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x13.gsdk.card.QRConfig\"I\n\x18SetQRConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\x8f\x01\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x18\n\x14\x44\x45\x46\x41ULT_SCAN_TIMEOUT\x10\x04\x12\x1a\n\x15\x44\x45\x46\x41ULT_TEMPLATE_SIZE\x10\x80\x03\x12\x17\n\x12\x46\x41\x43\x45_TEMPLATE_SIZE\x10\xa8\x04\x12\x11\n\rMAX_TEMPLATES\x10\x04\x1a\x02\x10\x01*\xd6\x01\n\x04Type\x12\x15\n\x11\x43\x41RD_TYPE_UNKNOWN\x10\x00\x12\x11\n\rCARD_TYPE_CSN\x10\x01\x12\x14\n\x10\x43\x41RD_TYPE_SECURE\x10\x02\x12\x14\n\x10\x43\x41RD_TYPE_ACCESS\x10\x03\x12\x18\n\x14\x43\x41RD_TYPE_CSN_MOBILE\x10\x04\x12\x1c\n\x18\x43\x41RD_TYPE_WIEGAND_MOBILE\x10\x05\x12\x10\n\x0c\x43\x41RD_TYPE_QR\x10\x06\x12\x17\n\x13\x43\x41RD_TYPE_SECURE_QR\x10\x07\x12\x15\n\x11\x43\x41RD_TYPE_WIEGAND\x10\n*6\n\x15\x44\x45SFireEncryptionType\x12\x10\n\x0c\x45NC_DES_3DES\x10\x00\x12\x0b\n\x07\x45NC_AES\x10\x01*G\n\x14\x44\x45SFireOperationMode\x12\x14\n\x10OPERATION_LEGACY\x10\x00\x12\x19\n\x15OPERATION_APPLEVELKEY\x10\x01*!\n\rCardByteOrder\x12\x07\n\x03MSB\x10\x00\x12\x07\n\x03LSB\x10\x01*M\n\x0c\x43\x61rdDataType\x12\x0f\n\x0b\x44\x41TA_BINARY\x10\x00\x12\x0e\n\nDATA_ASCII\x10\x01\x12\x0e\n\nDATA_UTF16\x10\x02\x12\x0c\n\x08\x44\x41TA_BCD\x10\x03\x32\xf8\x0c\n\x04\x43\x61rd\x12\x37\n\x04Scan\x12\x16.gsdk.card.ScanRequest\x1a\x17.gsdk.card.ScanResponse\x12:\n\x05\x45rase\x12\x17.gsdk.card.EraseRequest\x1a\x18.gsdk.card.EraseResponse\x12:\n\x05Write\x12\x17.gsdk.card.WriteRequest\x1a\x18.gsdk.card.WriteResponse\x12\x46\n\tGetConfig\x12\x1b.gsdk.card.GetConfigRequest\x1a\x1c.gsdk.card.GetConfigResponse\x12\x46\n\tSetConfig\x12\x1b.gsdk.card.SetConfigRequest\x1a\x1c.gsdk.card.SetConfigResponse\x12U\n\x0eSetConfigMulti\x12 .gsdk.card.SetConfigMultiRequest\x1a!.gsdk.card.SetConfigMultiResponse\x12O\n\x0cGetBlacklist\x12\x1e.gsdk.card.GetBlacklistRequest\x1a\x1f.gsdk.card.GetBlacklistResponse\x12O\n\x0c\x41\x64\x64\x42lacklist\x12\x1e.gsdk.card.AddBlacklistRequest\x1a\x1f.gsdk.card.AddBlacklistResponse\x12^\n\x11\x41\x64\x64\x42lacklistMulti\x12#.gsdk.card.AddBlacklistMultiRequest\x1a$.gsdk.card.AddBlacklistMultiResponse\x12X\n\x0f\x44\x65leteBlacklist\x12!.gsdk.card.DeleteBlacklistRequest\x1a\".gsdk.card.DeleteBlacklistResponse\x12g\n\x14\x44\x65leteBlacklistMulti\x12&.gsdk.card.DeleteBlacklistMultiRequest\x1a\'.gsdk.card.DeleteBlacklistMultiResponse\x12\x61\n\x12\x44\x65leteAllBlacklist\x12$.gsdk.card.DeleteAllBlacklistRequest\x1a%.gsdk.card.DeleteAllBlacklistResponse\x12p\n\x17\x44\x65leteAllBlacklistMulti\x12).gsdk.card.DeleteAllBlacklistMultiRequest\x1a*.gsdk.card.DeleteAllBlacklistMultiResponse\x12L\n\x0bGet1XConfig\x12\x1d.gsdk.card.Get1XConfigRequest\x1a\x1e.gsdk.card.Get1XConfigResponse\x12L\n\x0bSet1XConfig\x12\x1d.gsdk.card.Set1XConfigRequest\x1a\x1e.gsdk.card.Set1XConfigResponse\x12[\n\x10Set1XConfigMulti\x12\".gsdk.card.Set1XConfigMultiRequest\x1a#.gsdk.card.Set1XConfigMultiResponse\x12L\n\x0bWriteQRCode\x12\x1d.gsdk.card.WriteQRCodeRequest\x1a\x1e.gsdk.card.WriteQRCodeResponse\x12L\n\x0bGetQRConfig\x12\x1d.gsdk.card.GetQRConfigRequest\x1a\x1e.gsdk.card.GetQRConfigResponse\x12L\n\x0bSetQRConfig\x12\x1d.gsdk.card.SetQRConfigRequest\x1a\x1e.gsdk.card.SetQRConfigResponse\x12[\n\x10SetQRConfigMulti\x12\".gsdk.card.SetQRConfigMultiRequest\x1a#.gsdk.card.SetQRConfigMultiResponseB1\n\x17\x63om.supremainc.sdk.cardP\x01Z\x14\x62iostar/service/cardb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'card_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.supremainc.sdk.cardP\001Z\024biostar/service/card'
  _ENUM._options = None
  _ENUM._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=4503
  _globals['_ENUM']._serialized_end=4646
  _globals['_TYPE']._serialized_start=4649
  _globals['_TYPE']._serialized_end=4863
  _globals['_DESFIREENCRYPTIONTYPE']._serialized_start=4865
  _globals['_DESFIREENCRYPTIONTYPE']._serialized_end=4919
  _globals['_DESFIREOPERATIONMODE']._serialized_start=4921
  _globals['_DESFIREOPERATIONMODE']._serialized_end=4992
  _globals['_CARDBYTEORDER']._serialized_start=4994
  _globals['_CARDBYTEORDER']._serialized_end=5027
  _globals['_CARDDATATYPE']._serialized_start=5029
  _globals['_CARDDATATYPE']._serialized_end=5106
  _globals['_CSNCARDDATA']._serialized_start=36
  _globals['_CSNCARDDATA']._serialized_end=108
  _globals['_SMARTCARDHEADER']._serialized_start=111
  _globals['_SMARTCARDHEADER']._serialized_end=401
  _globals['_SMARTCARDCREDENTIAL']._serialized_start=403
  _globals['_SMARTCARDCREDENTIAL']._serialized_end=456
  _globals['_ACCESSONCARDDATA']._serialized_start=458
  _globals['_ACCESSONCARDDATA']._serialized_end=536
  _globals['_SMARTCARDDATA']._serialized_start=539
  _globals['_SMARTCARDDATA']._serialized_end=717
  _globals['_CARDDATA']._serialized_start=720
  _globals['_CARDDATA']._serialized_end=855
  _globals['_SCANREQUEST']._serialized_start=857
  _globals['_SCANREQUEST']._serialized_end=888
  _globals['_SCANRESPONSE']._serialized_start=890
  _globals['_SCANRESPONSE']._serialized_end=943
  _globals['_ERASEREQUEST']._serialized_start=945
  _globals['_ERASEREQUEST']._serialized_end=977
  _globals['_ERASERESPONSE']._serialized_start=979
  _globals['_ERASERESPONSE']._serialized_end=994
  _globals['_WRITEREQUEST']._serialized_start=996
  _globals['_WRITEREQUEST']._serialized_end=1077
  _globals['_WRITERESPONSE']._serialized_start=1079
  _globals['_WRITERESPONSE']._serialized_end=1094
  _globals['_MIFARECONFIG']._serialized_start=1096
  _globals['_MIFARECONFIG']._serialized_end=1177
  _globals['_ICLASSCONFIG']._serialized_start=1179
  _globals['_ICLASSCONFIG']._serialized_end=1260
  _globals['_DESFIRECONFIG']._serialized_start=1263
  _globals['_DESFIRECONFIG']._serialized_end=1465
  _globals['_SEOSCONFIG']._serialized_start=1468
  _globals['_SEOSCONFIG']._serialized_end=1612
  _globals['_CARDCONFIG']._serialized_start=1615
  _globals['_CARDCONFIG']._serialized_end=2040
  _globals['_GETCONFIGREQUEST']._serialized_start=2042
  _globals['_GETCONFIGREQUEST']._serialized_end=2078
  _globals['_GETCONFIGRESPONSE']._serialized_start=2080
  _globals['_GETCONFIGRESPONSE']._serialized_end=2138
  _globals['_SETCONFIGREQUEST']._serialized_start=2140
  _globals['_SETCONFIGREQUEST']._serialized_end=2215
  _globals['_SETCONFIGRESPONSE']._serialized_start=2217
  _globals['_SETCONFIGRESPONSE']._serialized_end=2236
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=2238
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=2319
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=2321
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=2392
  _globals['_BLACKLISTITEM']._serialized_start=2394
  _globals['_BLACKLISTITEM']._serialized_end=2445
  _globals['_GETBLACKLISTREQUEST']._serialized_start=2447
  _globals['_GETBLACKLISTREQUEST']._serialized_end=2486
  _globals['_GETBLACKLISTRESPONSE']._serialized_start=2488
  _globals['_GETBLACKLISTRESPONSE']._serialized_end=2555
  _globals['_ADDBLACKLISTREQUEST']._serialized_start=2557
  _globals['_ADDBLACKLISTREQUEST']._serialized_end=2641
  _globals['_ADDBLACKLISTRESPONSE']._serialized_start=2643
  _globals['_ADDBLACKLISTRESPONSE']._serialized_end=2665
  _globals['_ADDBLACKLISTMULTIREQUEST']._serialized_start=2667
  _globals['_ADDBLACKLISTMULTIREQUEST']._serialized_end=2757
  _globals['_ADDBLACKLISTMULTIRESPONSE']._serialized_start=2759
  _globals['_ADDBLACKLISTMULTIRESPONSE']._serialized_end=2833
  _globals['_DELETEBLACKLISTREQUEST']._serialized_start=2835
  _globals['_DELETEBLACKLISTREQUEST']._serialized_end=2922
  _globals['_DELETEBLACKLISTRESPONSE']._serialized_start=2924
  _globals['_DELETEBLACKLISTRESPONSE']._serialized_end=2949
  _globals['_DELETEBLACKLISTMULTIREQUEST']._serialized_start=2951
  _globals['_DELETEBLACKLISTMULTIREQUEST']._serialized_end=3044
  _globals['_DELETEBLACKLISTMULTIRESPONSE']._serialized_start=3046
  _globals['_DELETEBLACKLISTMULTIRESPONSE']._serialized_end=3123
  _globals['_DELETEALLBLACKLISTREQUEST']._serialized_start=3125
  _globals['_DELETEALLBLACKLISTREQUEST']._serialized_end=3170
  _globals['_DELETEALLBLACKLISTRESPONSE']._serialized_start=3172
  _globals['_DELETEALLBLACKLISTRESPONSE']._serialized_end=3200
  _globals['_DELETEALLBLACKLISTMULTIREQUEST']._serialized_start=3202
  _globals['_DELETEALLBLACKLISTMULTIREQUEST']._serialized_end=3253
  _globals['_DELETEALLBLACKLISTMULTIRESPONSE']._serialized_start=3255
  _globals['_DELETEALLBLACKLISTMULTIRESPONSE']._serialized_end=3335
  _globals['_CARD1XCONFIG']._serialized_start=3338
  _globals['_CARD1XCONFIG']._serialized_end=3577
  _globals['_GET1XCONFIGREQUEST']._serialized_start=3579
  _globals['_GET1XCONFIGREQUEST']._serialized_end=3617
  _globals['_GET1XCONFIGRESPONSE']._serialized_start=3619
  _globals['_GET1XCONFIGRESPONSE']._serialized_end=3681
  _globals['_SET1XCONFIGREQUEST']._serialized_start=3683
  _globals['_SET1XCONFIGREQUEST']._serialized_end=3762
  _globals['_SET1XCONFIGRESPONSE']._serialized_start=3764
  _globals['_SET1XCONFIGRESPONSE']._serialized_end=3785
  _globals['_SET1XCONFIGMULTIREQUEST']._serialized_start=3787
  _globals['_SET1XCONFIGMULTIREQUEST']._serialized_end=3872
  _globals['_SET1XCONFIGMULTIRESPONSE']._serialized_start=3874
  _globals['_SET1XCONFIGMULTIRESPONSE']._serialized_end=3947
  _globals['_WRITEQRCODEREQUEST']._serialized_start=3949
  _globals['_WRITEQRCODEREQUEST']._serialized_end=3985
  _globals['_WRITEQRCODERESPONSE']._serialized_start=3987
  _globals['_WRITEQRCODERESPONSE']._serialized_end=4050
  _globals['_QRCONFIG']._serialized_start=4052
  _globals['_QRCONFIG']._serialized_end=4142
  _globals['_GETQRCONFIGREQUEST']._serialized_start=4144
  _globals['_GETQRCONFIGREQUEST']._serialized_end=4182
  _globals['_GETQRCONFIGRESPONSE']._serialized_start=4184
  _globals['_GETQRCONFIGRESPONSE']._serialized_end=4242
  _globals['_SETQRCONFIGREQUEST']._serialized_start=4244
  _globals['_SETQRCONFIGREQUEST']._serialized_end=4319
  _globals['_SETQRCONFIGRESPONSE']._serialized_start=4321
  _globals['_SETQRCONFIGRESPONSE']._serialized_end=4342
  _globals['_SETQRCONFIGMULTIREQUEST']._serialized_start=4344
  _globals['_SETQRCONFIGMULTIREQUEST']._serialized_end=4425
  _globals['_SETQRCONFIGMULTIRESPONSE']._serialized_start=4427
  _globals['_SETQRCONFIGMULTIRESPONSE']._serialized_end=4500
  _globals['_CARD']._serialized_start=5109
  _globals['_CARD']._serialized_end=6765
# @@protoc_insertion_point(module_scope)
