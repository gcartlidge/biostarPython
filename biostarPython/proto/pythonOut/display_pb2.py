# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: display.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdisplay.proto\x12\x0cgsdk.display\x1a\terr.proto\"\xf2\x03\n\rDisplayConfig\x12,\n\x08language\x18\x01 \x01(\x0e\x32\x1a.gsdk.display.LanguageType\x12\x30\n\nbackground\x18\x02 \x01(\x0e\x32\x1c.gsdk.display.BackgroundType\x12,\n\x05theme\x18\x03 \x01(\x0e\x32\x1d.gsdk.display.BackgroundTheme\x12\x0e\n\x06volume\x18\x04 \x01(\r\x12\x10\n\x08useVoice\x18\x05 \x01(\x08\x12,\n\ndateFormat\x18\x06 \x01(\x0e\x32\x18.gsdk.display.DateFormat\x12,\n\ntimeFormat\x18\x07 \x01(\x0e\x32\x18.gsdk.display.TimeFormat\x12\x14\n\x0cshowDateTime\x18\x08 \x01(\x08\x12\x13\n\x0bmenuTimeout\x18\t \x01(\r\x12\x12\n\nmsgTimeout\x18\n \x01(\r\x12\x18\n\x10\x62\x61\x63klightTimeout\x18\x0b \x01(\r\x12\x15\n\ruseUserPhrase\x18\x0c \x01(\x08\x12\x17\n\x0fqueryUserPhrase\x18\r \x01(\x08\x12\x16\n\x0euseScreenSaver\x18\x0e \x01(\x08\x12\x34\n\x0eshowOSDPResult\x18\x0f \x01(\x0e\x32\x1c.gsdk.display.ShowOSDPResult\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"@\n\x11GetConfigResponse\x12+\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1b.gsdk.display.DisplayConfig\"Q\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12+\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1b.gsdk.display.DisplayConfig\"\x13\n\x11SetConfigResponse\"W\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12+\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1b.gsdk.display.DisplayConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\";\n\x19UpdateLanguagePackRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1c\n\x1aUpdateLanguagePackResponse\"A\n\x1eUpdateLanguagePackMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"P\n\x1fUpdateLanguagePackMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"7\n\x13UpdateNoticeRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0e\n\x06notice\x18\x02 \x01(\t\"\x16\n\x14UpdateNoticeResponse\"=\n\x18UpdateNoticeMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x0e\n\x06notice\x18\x02 \x01(\t\"J\n\x19UpdateNoticeMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"B\n\x1cUpdateBackgroundImageRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x10\n\x08PNGImage\x18\x02 \x01(\x0c\"\x1f\n\x1dUpdateBackgroundImageResponse\"H\n!UpdateBackgroundImageMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x10\n\x08PNGImage\x18\x02 \x01(\x0c\"S\n\"UpdateBackgroundImageMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"?\n\x18UpdateSlideImagesRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x11\n\tPNGImages\x18\x02 \x03(\x0c\"\x1b\n\x19UpdateSlideImagesResponse\"E\n\x1dUpdateSlideImagesMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x11\n\tPNGImages\x18\x02 \x03(\x0c\"O\n\x1eUpdateSlideImagesMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse\"a\n\x12UpdateSoundRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\'\n\x05index\x18\x02 \x01(\x0e\x32\x18.gsdk.display.SoundIndex\x12\x10\n\x08waveData\x18\x03 \x01(\x0c\"\x15\n\x13UpdateSoundResponse\"g\n\x17UpdateSoundMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\'\n\x05index\x18\x02 \x01(\x0e\x32\x18.gsdk.display.SoundIndex\x12\x10\n\x08waveData\x18\x03 \x01(\x0c\"I\n\x18UpdateSoundMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\x88\x02\n\x04\x45num\x12!\n\x1d\x46IRST_ENUM_VALUE_MUST_BE_ZERO\x10\x00\x12\x18\n\x14\x44\x45\x46\x41ULT_MENU_TIMEOUT\x10\x14\x12\x1c\n\x17\x44\x45\x46\x41ULT_MESSAGE_TIMEOUT\x10\xd0\x0f\x12\x1d\n\x19\x44\x45\x46\x41ULT_BACKLIGHT_TIMEOUT\x10\x14\x12\x12\n\x0e\x44\x45\x46\x41ULT_VOLUME\x10\x32\x12\x0e\n\nMIN_VOLUME\x10\x00\x12\x0e\n\nMAX_VOLUME\x10\x64\x12\x18\n\x13MIN_MESSAGE_TIMEOUT\x10\xf4\x03\x12\x18\n\x13MAX_MESSAGE_TIMEOUT\x10\x88\'\x12\x1a\n\x15OSDP_LED_SHOW_TIMEOUT\x10\xb8\x17\x1a\x02\x10\x01*Z\n\x0cLanguageType\x12\x17\n\x13\x42S2_LANGUAGE_KOREAN\x10\x00\x12\x18\n\x14\x42S2_LANGUAGE_ENGLISH\x10\x01\x12\x17\n\x13\x42S2_LANGUAGE_CUSTOM\x10\x02*V\n\x0e\x42\x61\x63kgroundType\x12\x0f\n\x0b\x42S2_BG_LOGO\x10\x00\x12\x11\n\rBS2_BG_NOTICE\x10\x01\x12\x10\n\x0c\x42S2_BG_SLIDE\x10\x02\x12\x0e\n\nBS2_BG_PDF\x10\x03*e\n\x0f\x42\x61\x63kgroundTheme\x12\x13\n\x0f\x42S2_BG_THEME_01\x10\x00\x12\x13\n\x0f\x42S2_BG_THEME_02\x10\x01\x12\x13\n\x0f\x42S2_BG_THEME_03\x10\x02\x12\x13\n\x0f\x42S2_BG_THEME_04\x10\x03*f\n\nDateFormat\x12\x1c\n\x18\x42S2_DATE_FORMAT_YYYYMMDD\x10\x00\x12\x1c\n\x18\x42S2_DATE_FORMAT_MMDDYYYY\x10\x01\x12\x1c\n\x18\x42S2_DATE_FORMAT_DDMMYYYY\x10\x02*F\n\nTimeFormat\x12\x1b\n\x17\x42S2_TIME_FORMAT_12_HOUR\x10\x00\x12\x1b\n\x17\x42S2_TIME_FORMAT_24_HOUR\x10\x01*K\n\x0eShowOSDPResult\x12\x1b\n\x17\x42S2_SHOW_OSDP_RESULT_ON\x10\x00\x12\x1c\n\x18\x42S2_SHOW_OSDP_RESULT_OFF\x10\x01*\x90\x01\n\nSoundIndex\x12\x17\n\x13SOUND_INDEX_WELCOME\x10\x00\x12\x1c\n\x18SOUND_INDEX_AUTH_SUCCESS\x10\x01\x12\x19\n\x15SOUND_INDEX_AUTH_FAIL\x10\x02\x12\x17\n\x13SOUND_INDEX_ALARM_1\x10\x03\x12\x17\n\x13SOUND_INDEX_ALARM_2\x10\x04\x32\xa5\n\n\x07\x44isplay\x12g\n\x12UpdateLanguagePack\x12\'.gsdk.display.UpdateLanguagePackRequest\x1a(.gsdk.display.UpdateLanguagePackResponse\x12v\n\x17UpdateLanguagePackMulti\x12,.gsdk.display.UpdateLanguagePackMultiRequest\x1a-.gsdk.display.UpdateLanguagePackMultiResponse\x12U\n\x0cUpdateNotice\x12!.gsdk.display.UpdateNoticeRequest\x1a\".gsdk.display.UpdateNoticeResponse\x12\x64\n\x11UpdateNoticeMulti\x12&.gsdk.display.UpdateNoticeMultiRequest\x1a\'.gsdk.display.UpdateNoticeMultiResponse\x12p\n\x15UpdateBackgroundImage\x12*.gsdk.display.UpdateBackgroundImageRequest\x1a+.gsdk.display.UpdateBackgroundImageResponse\x12\x7f\n\x1aUpdateBackgroundImageMulti\x12/.gsdk.display.UpdateBackgroundImageMultiRequest\x1a\x30.gsdk.display.UpdateBackgroundImageMultiResponse\x12\x64\n\x11UpdateSlideImages\x12&.gsdk.display.UpdateSlideImagesRequest\x1a\'.gsdk.display.UpdateSlideImagesResponse\x12s\n\x16UpdateSlideImagesMulti\x12+.gsdk.display.UpdateSlideImagesMultiRequest\x1a,.gsdk.display.UpdateSlideImagesMultiResponse\x12R\n\x0bUpdateSound\x12 .gsdk.display.UpdateSoundRequest\x1a!.gsdk.display.UpdateSoundResponse\x12\x61\n\x10UpdateSoundMulti\x12%.gsdk.display.UpdateSoundMultiRequest\x1a&.gsdk.display.UpdateSoundMultiResponse\x12L\n\tGetConfig\x12\x1e.gsdk.display.GetConfigRequest\x1a\x1f.gsdk.display.GetConfigResponse\x12L\n\tSetConfig\x12\x1e.gsdk.display.SetConfigRequest\x1a\x1f.gsdk.display.SetConfigResponse\x12[\n\x0eSetConfigMulti\x12#.gsdk.display.SetConfigMultiRequest\x1a$.gsdk.display.SetConfigMultiResponseB7\n\x1a\x63om.supremainc.sdk.displayP\x01Z\x17\x62iostar/service/displayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'display_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.supremainc.sdk.displayP\001Z\027biostar/service/display'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=2182
  _globals['_ENUM']._serialized_end=2446
  _globals['_LANGUAGETYPE']._serialized_start=2448
  _globals['_LANGUAGETYPE']._serialized_end=2538
  _globals['_BACKGROUNDTYPE']._serialized_start=2540
  _globals['_BACKGROUNDTYPE']._serialized_end=2626
  _globals['_BACKGROUNDTHEME']._serialized_start=2628
  _globals['_BACKGROUNDTHEME']._serialized_end=2729
  _globals['_DATEFORMAT']._serialized_start=2731
  _globals['_DATEFORMAT']._serialized_end=2833
  _globals['_TIMEFORMAT']._serialized_start=2835
  _globals['_TIMEFORMAT']._serialized_end=2905
  _globals['_SHOWOSDPRESULT']._serialized_start=2907
  _globals['_SHOWOSDPRESULT']._serialized_end=2982
  _globals['_SOUNDINDEX']._serialized_start=2985
  _globals['_SOUNDINDEX']._serialized_end=3129
  _globals['_DISPLAYCONFIG']._serialized_start=43
  _globals['_DISPLAYCONFIG']._serialized_end=541
  _globals['_GETCONFIGREQUEST']._serialized_start=543
  _globals['_GETCONFIGREQUEST']._serialized_end=579
  _globals['_GETCONFIGRESPONSE']._serialized_start=581
  _globals['_GETCONFIGRESPONSE']._serialized_end=645
  _globals['_SETCONFIGREQUEST']._serialized_start=647
  _globals['_SETCONFIGREQUEST']._serialized_end=728
  _globals['_SETCONFIGRESPONSE']._serialized_start=730
  _globals['_SETCONFIGRESPONSE']._serialized_end=749
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=751
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=838
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=840
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=911
  _globals['_UPDATELANGUAGEPACKREQUEST']._serialized_start=913
  _globals['_UPDATELANGUAGEPACKREQUEST']._serialized_end=972
  _globals['_UPDATELANGUAGEPACKRESPONSE']._serialized_start=974
  _globals['_UPDATELANGUAGEPACKRESPONSE']._serialized_end=1002
  _globals['_UPDATELANGUAGEPACKMULTIREQUEST']._serialized_start=1004
  _globals['_UPDATELANGUAGEPACKMULTIREQUEST']._serialized_end=1069
  _globals['_UPDATELANGUAGEPACKMULTIRESPONSE']._serialized_start=1071
  _globals['_UPDATELANGUAGEPACKMULTIRESPONSE']._serialized_end=1151
  _globals['_UPDATENOTICEREQUEST']._serialized_start=1153
  _globals['_UPDATENOTICEREQUEST']._serialized_end=1208
  _globals['_UPDATENOTICERESPONSE']._serialized_start=1210
  _globals['_UPDATENOTICERESPONSE']._serialized_end=1232
  _globals['_UPDATENOTICEMULTIREQUEST']._serialized_start=1234
  _globals['_UPDATENOTICEMULTIREQUEST']._serialized_end=1295
  _globals['_UPDATENOTICEMULTIRESPONSE']._serialized_start=1297
  _globals['_UPDATENOTICEMULTIRESPONSE']._serialized_end=1371
  _globals['_UPDATEBACKGROUNDIMAGEREQUEST']._serialized_start=1373
  _globals['_UPDATEBACKGROUNDIMAGEREQUEST']._serialized_end=1439
  _globals['_UPDATEBACKGROUNDIMAGERESPONSE']._serialized_start=1441
  _globals['_UPDATEBACKGROUNDIMAGERESPONSE']._serialized_end=1472
  _globals['_UPDATEBACKGROUNDIMAGEMULTIREQUEST']._serialized_start=1474
  _globals['_UPDATEBACKGROUNDIMAGEMULTIREQUEST']._serialized_end=1546
  _globals['_UPDATEBACKGROUNDIMAGEMULTIRESPONSE']._serialized_start=1548
  _globals['_UPDATEBACKGROUNDIMAGEMULTIRESPONSE']._serialized_end=1631
  _globals['_UPDATESLIDEIMAGESREQUEST']._serialized_start=1633
  _globals['_UPDATESLIDEIMAGESREQUEST']._serialized_end=1696
  _globals['_UPDATESLIDEIMAGESRESPONSE']._serialized_start=1698
  _globals['_UPDATESLIDEIMAGESRESPONSE']._serialized_end=1725
  _globals['_UPDATESLIDEIMAGESMULTIREQUEST']._serialized_start=1727
  _globals['_UPDATESLIDEIMAGESMULTIREQUEST']._serialized_end=1796
  _globals['_UPDATESLIDEIMAGESMULTIRESPONSE']._serialized_start=1798
  _globals['_UPDATESLIDEIMAGESMULTIRESPONSE']._serialized_end=1877
  _globals['_UPDATESOUNDREQUEST']._serialized_start=1879
  _globals['_UPDATESOUNDREQUEST']._serialized_end=1976
  _globals['_UPDATESOUNDRESPONSE']._serialized_start=1978
  _globals['_UPDATESOUNDRESPONSE']._serialized_end=1999
  _globals['_UPDATESOUNDMULTIREQUEST']._serialized_start=2001
  _globals['_UPDATESOUNDMULTIREQUEST']._serialized_end=2104
  _globals['_UPDATESOUNDMULTIRESPONSE']._serialized_start=2106
  _globals['_UPDATESOUNDMULTIRESPONSE']._serialized_end=2179
  _globals['_DISPLAY']._serialized_start=3132
  _globals['_DISPLAY']._serialized_end=4449
# @@protoc_insertion_point(module_scope)