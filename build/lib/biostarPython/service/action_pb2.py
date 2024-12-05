# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'action.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import device_pb2 as device__pb2
from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x61\x63tion.proto\x12\x0bgsdk.action\x1a\x0c\x64\x65vice.proto\x1a\terr.proto\"!\n\x0c\x45ventTrigger\x12\x11\n\teventCode\x18\x01 \x01(\r\"o\n\x0cInputTrigger\x12\x0c\n\x04port\x18\x01 \x01(\r\x12+\n\nswitchType\x18\x02 \x01(\x0e\x32\x17.gsdk.device.SwitchType\x12\x10\n\x08\x64uration\x18\x03 \x01(\r\x12\x12\n\nscheduleID\x18\x04 \x01(\r\"U\n\x0fScheduleTrigger\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .gsdk.action.ScheduleTriggerType\x12\x12\n\nscheduleID\x18\x02 \x01(\r\"\xf1\x01\n\x07Trigger\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.gsdk.action.TriggerType\x12\x18\n\x10ignoreSignalTime\x18\x03 \x01(\r\x12*\n\x05\x65vent\x18\x04 \x01(\x0b\x32\x19.gsdk.action.EventTriggerH\x00\x12*\n\x05input\x18\x05 \x01(\x0b\x32\x19.gsdk.action.InputTriggerH\x00\x12\x30\n\x08schedule\x18\x06 \x01(\x0b\x32\x1c.gsdk.action.ScheduleTriggerH\x00\x42\x08\n\x06\x65ntity\"a\n\x06Signal\x12\x10\n\x08signalID\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\x12\n\nonDuration\x18\x03 \x01(\r\x12\x13\n\x0boffDuration\x18\x04 \x01(\r\x12\r\n\x05\x64\x65lay\x18\x05 \x01(\r\"J\n\x10OutputPortAction\x12\x11\n\tportIndex\x18\x01 \x01(\r\x12#\n\x06signal\x18\x02 \x01(\x0b\x32\x13.gsdk.action.Signal\"F\n\x0bRelayAction\x12\x12\n\nrelayIndex\x18\x01 \x01(\r\x12#\n\x06signal\x18\x02 \x01(\x0b\x32\x13.gsdk.action.Signal\"R\n\tLEDSignal\x12$\n\x05\x63olor\x18\x01 \x01(\x0e\x32\x15.gsdk.device.LEDColor\x12\x10\n\x08\x64uration\x18\x02 \x01(\r\x12\r\n\x05\x64\x65lay\x18\x03 \x01(\r\"C\n\tLEDAction\x12\'\n\x07signals\x18\x01 \x03(\x0b\x32\x16.gsdk.action.LEDSignal\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"g\n\x0c\x42uzzerSignal\x12%\n\x04tone\x18\x01 \x01(\x0e\x32\x17.gsdk.device.BuzzerTone\x12\x0f\n\x07\x66\x61\x64\x65out\x18\x02 \x01(\x08\x12\x10\n\x08\x64uration\x18\x03 \x01(\r\x12\r\n\x05\x64\x65lay\x18\x04 \x01(\r\"I\n\x0c\x42uzzerAction\x12*\n\x07signals\x18\x01 \x03(\x0b\x32\x19.gsdk.action.BuzzerSignal\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"H\n\rDisplayAction\x12\x10\n\x08\x64uration\x18\x01 \x01(\r\x12\x11\n\tdisplayID\x18\x02 \x01(\r\x12\x12\n\nresourceID\x18\x03 \x01(\r\"?\n\x0bSoundAction\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12\x12\n\nsoundIndex\x18\x02 \x01(\r\x12\r\n\x05\x64\x65lay\x18\x03 \x01(\r\"G\n\nLiftAction\x12\x0e\n\x06liftID\x18\x01 \x01(\r\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.gsdk.action.LiftActionType\"\xba\x03\n\x06\x41\x63tion\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x17.gsdk.action.ActionType\x12\'\n\x08stopFlag\x18\x03 \x01(\x0e\x32\x15.gsdk.action.StopFlag\x12\r\n\x05\x64\x65lay\x18\x04 \x01(\r\x12)\n\x05relay\x18\x05 \x01(\x0b\x32\x18.gsdk.action.RelayActionH\x00\x12\x33\n\noutputPort\x18\x06 \x01(\x0b\x32\x1d.gsdk.action.OutputPortActionH\x00\x12-\n\x07\x64isplay\x18\x07 \x01(\x0b\x32\x1a.gsdk.action.DisplayActionH\x00\x12)\n\x05sound\x18\x08 \x01(\x0b\x32\x18.gsdk.action.SoundActionH\x00\x12%\n\x03LED\x18\t \x01(\x0b\x32\x16.gsdk.action.LEDActionH\x00\x12+\n\x06\x62uzzer\x18\n \x01(\x0b\x32\x19.gsdk.action.BuzzerActionH\x00\x12\'\n\x04lift\x18\x0b \x01(\x0b\x32\x17.gsdk.action.LiftActionH\x00\x42\x08\n\x06\x65ntity\"\xba\x01\n\x13TriggerActionConfig\x12\x46\n\x0etriggerActions\x18\x01 \x03(\x0b\x32..gsdk.action.TriggerActionConfig.TriggerAction\x1a[\n\rTriggerAction\x12%\n\x07trigger\x18\x01 \x01(\x0b\x32\x14.gsdk.action.Trigger\x12#\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x13.gsdk.action.Action\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"E\n\x11GetConfigResponse\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .gsdk.action.TriggerActionConfig\"V\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .gsdk.action.TriggerActionConfig\"\x13\n\x11SetConfigResponse\"\\\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .gsdk.action.TriggerActionConfig\"G\n\x16SetConfigMultiResponse\x12-\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x17.gsdk.err.ErrorResponse*\x84\x01\n\x04\x45num\x12\x15\n\x11REPEAT_INFINITELY\x10\x00\x12\x1c\n\x17\x44\x45\x46\x41ULT_SIGNAL_DURATION\x10\xd0\x0f\x12\x18\n\x14\x44\x45\x46\x41ULT_SIGNAL_DELAY\x10\x00\x12\x0f\n\x0bMAX_SIGNALS\x10\x03\x12\x18\n\x13MAX_TRIGGER_ACTIONS\x10\x80\x01\x1a\x02\x10\x01*[\n\x0bTriggerType\x12\x10\n\x0cTRIGGER_NONE\x10\x00\x12\x11\n\rTRIGGER_EVENT\x10\x01\x12\x11\n\rTRIGGER_INPUT\x10\x02\x12\x14\n\x10TRIGGER_SCHEDULE\x10\x03*Q\n\x13ScheduleTriggerType\x12\x1d\n\x19SCHEDULE_TRIGGER_ON_START\x10\x00\x12\x1b\n\x17SCHEDULE_TRIGGER_ON_END\x10\x01*\xe5\x02\n\nActionType\x12\x0f\n\x0b\x41\x43TION_NONE\x10\x00\x12\x16\n\x12\x41\x43TION_LOCK_DEVICE\x10\x01\x12\x18\n\x14\x41\x43TION_UNLOCK_DEVICE\x10\x02\x12\x18\n\x14\x41\x43TION_REBOOT_DEVICE\x10\x03\x12\x18\n\x14\x41\x43TION_RELEASE_ALARM\x10\x04\x12\x18\n\x14\x41\x43TION_GENERAL_INPUT\x10\x05\x12\x10\n\x0c\x41\x43TION_RELAY\x10\x06\x12\x0e\n\nACTION_TTL\x10\x07\x12\x10\n\x0c\x41\x43TION_SOUND\x10\x08\x12\x12\n\x0e\x41\x43TION_DISPLAY\x10\t\x12\x11\n\rACTION_BUZZER\x10\n\x12\x0e\n\nACTION_LED\x10\x0b\x12\x1b\n\x17\x41\x43TION_FIRE_ALARM_INPUT\x10\x0c\x12\x17\n\x13\x41\x43TION_AUTH_SUCCESS\x10\r\x12\x14\n\x10\x41\x43TION_AUTH_FAIL\x10\x0e\x12\x0f\n\x0b\x41\x43TION_LIFT\x10\x0f*N\n\x08StopFlag\x12\r\n\tSTOP_NONE\x10\x00\x12\x17\n\x13STOP_ON_DOOR_CLOSED\x10\x01\x12\x1a\n\x16STOP_BY_CMD_RUN_ACTION\x10\x02*t\n\x0eLiftActionType\x12\x1f\n\x1bLIFT_ACTION_ACTIVATE_FLOORS\x10\x00\x12!\n\x1dLIFT_ACTION_DEACTIVATE_FLOORS\x10\x01\x12\x1e\n\x1aLIFT_ACTION_RELEASE_FLOORS\x10\x02\x32\x82\x02\n\rTriggerAction\x12J\n\tGetConfig\x12\x1d.gsdk.action.GetConfigRequest\x1a\x1e.gsdk.action.GetConfigResponse\x12J\n\tSetConfig\x12\x1d.gsdk.action.SetConfigRequest\x1a\x1e.gsdk.action.SetConfigResponse\x12Y\n\x0eSetConfigMulti\x12\".gsdk.action.SetConfigMultiRequest\x1a#.gsdk.action.SetConfigMultiResponseB5\n\x19\x63om.supremainc.sdk.actionP\x01Z\x16\x62iostar/service/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.supremainc.sdk.actionP\001Z\026biostar/service/action'
  _globals['_ENUM']._loaded_options = None
  _globals['_ENUM']._serialized_options = b'\020\001'
  _globals['_ENUM']._serialized_start=2345
  _globals['_ENUM']._serialized_end=2477
  _globals['_TRIGGERTYPE']._serialized_start=2479
  _globals['_TRIGGERTYPE']._serialized_end=2570
  _globals['_SCHEDULETRIGGERTYPE']._serialized_start=2572
  _globals['_SCHEDULETRIGGERTYPE']._serialized_end=2653
  _globals['_ACTIONTYPE']._serialized_start=2656
  _globals['_ACTIONTYPE']._serialized_end=3013
  _globals['_STOPFLAG']._serialized_start=3015
  _globals['_STOPFLAG']._serialized_end=3093
  _globals['_LIFTACTIONTYPE']._serialized_start=3095
  _globals['_LIFTACTIONTYPE']._serialized_end=3211
  _globals['_EVENTTRIGGER']._serialized_start=54
  _globals['_EVENTTRIGGER']._serialized_end=87
  _globals['_INPUTTRIGGER']._serialized_start=89
  _globals['_INPUTTRIGGER']._serialized_end=200
  _globals['_SCHEDULETRIGGER']._serialized_start=202
  _globals['_SCHEDULETRIGGER']._serialized_end=287
  _globals['_TRIGGER']._serialized_start=290
  _globals['_TRIGGER']._serialized_end=531
  _globals['_SIGNAL']._serialized_start=533
  _globals['_SIGNAL']._serialized_end=630
  _globals['_OUTPUTPORTACTION']._serialized_start=632
  _globals['_OUTPUTPORTACTION']._serialized_end=706
  _globals['_RELAYACTION']._serialized_start=708
  _globals['_RELAYACTION']._serialized_end=778
  _globals['_LEDSIGNAL']._serialized_start=780
  _globals['_LEDSIGNAL']._serialized_end=862
  _globals['_LEDACTION']._serialized_start=864
  _globals['_LEDACTION']._serialized_end=931
  _globals['_BUZZERSIGNAL']._serialized_start=933
  _globals['_BUZZERSIGNAL']._serialized_end=1036
  _globals['_BUZZERACTION']._serialized_start=1038
  _globals['_BUZZERACTION']._serialized_end=1111
  _globals['_DISPLAYACTION']._serialized_start=1113
  _globals['_DISPLAYACTION']._serialized_end=1185
  _globals['_SOUNDACTION']._serialized_start=1187
  _globals['_SOUNDACTION']._serialized_end=1250
  _globals['_LIFTACTION']._serialized_start=1252
  _globals['_LIFTACTION']._serialized_end=1323
  _globals['_ACTION']._serialized_start=1326
  _globals['_ACTION']._serialized_end=1768
  _globals['_TRIGGERACTIONCONFIG']._serialized_start=1771
  _globals['_TRIGGERACTIONCONFIG']._serialized_end=1957
  _globals['_TRIGGERACTIONCONFIG_TRIGGERACTION']._serialized_start=1866
  _globals['_TRIGGERACTIONCONFIG_TRIGGERACTION']._serialized_end=1957
  _globals['_GETCONFIGREQUEST']._serialized_start=1959
  _globals['_GETCONFIGREQUEST']._serialized_end=1995
  _globals['_GETCONFIGRESPONSE']._serialized_start=1997
  _globals['_GETCONFIGRESPONSE']._serialized_end=2066
  _globals['_SETCONFIGREQUEST']._serialized_start=2068
  _globals['_SETCONFIGREQUEST']._serialized_end=2154
  _globals['_SETCONFIGRESPONSE']._serialized_start=2156
  _globals['_SETCONFIGRESPONSE']._serialized_end=2175
  _globals['_SETCONFIGMULTIREQUEST']._serialized_start=2177
  _globals['_SETCONFIGMULTIREQUEST']._serialized_end=2269
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_start=2271
  _globals['_SETCONFIGMULTIRESPONSE']._serialized_end=2342
  _globals['_TRIGGERACTION']._serialized_start=3214
  _globals['_TRIGGERACTION']._serialized_end=3472
# @@protoc_insertion_point(module_scope)
