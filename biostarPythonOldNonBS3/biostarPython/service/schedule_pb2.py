# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schedule.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import err_pb2 as err__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eschedule.proto\x12\x08schedule\x1a\terr.proto\"\xa7\x01\n\x0cScheduleInfo\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x05\x64\x61ily\x18\x03 \x01(\x0b\x32\x17.schedule.DailySchedule\x12(\n\x06weekly\x18\x04 \x01(\x0b\x32\x18.schedule.WeeklySchedule\x12+\n\x08holidays\x18\x05 \x03(\x0b\x32\x19.schedule.HolidaySchedule\"4\n\x0b\x44\x61ySchedule\x12%\n\x07periods\x18\x01 \x03(\x0b\x32\x14.schedule.TimePeriod\"0\n\nTimePeriod\x12\x11\n\tstartTime\x18\x01 \x01(\x05\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\x05\"=\n\x0eWeeklySchedule\x12+\n\x0c\x64\x61ySchedules\x18\x01 \x03(\x0b\x32\x15.schedule.DaySchedule\"O\n\rDailySchedule\x12\x11\n\tstartDate\x18\x01 \x01(\r\x12+\n\x0c\x64\x61ySchedules\x18\x02 \x03(\x0b\x32\x15.schedule.DaySchedule\"N\n\x0fHolidaySchedule\x12\x0f\n\x07groupID\x18\x01 \x01(\r\x12*\n\x0b\x64\x61ySchedule\x18\x02 \x01(\x0b\x32\x15.schedule.DaySchedule\"M\n\x0cHolidayGroup\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x08holidays\x18\x03 \x03(\x0b\x32\x11.schedule.Holiday\"H\n\x07Holiday\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\r\x12/\n\nrecurrence\x18\x02 \x01(\x0e\x32\x1b.schedule.HolidayRecurrence\"\"\n\x0eGetListRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"<\n\x0fGetListResponse\x12)\n\tschedules\x18\x01 \x03(\x0b\x32\x16.schedule.ScheduleInfo\"I\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12)\n\tschedules\x18\x02 \x03(\x0b\x32\x16.schedule.ScheduleInfo\"\r\n\x0b\x41\x64\x64Response\"O\n\x0f\x41\x64\x64MultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12)\n\tschedules\x18\x02 \x03(\x0b\x32\x16.schedule.ScheduleInfo\"<\n\x10\x41\x64\x64MultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"6\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x13\n\x0bscheduleIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"<\n\x12\x44\x65leteMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x13\n\x0bscheduleIDs\x18\x02 \x03(\r\"?\n\x13\x44\x65leteMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"*\n\x15\x44\x65leteAllMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"B\n\x16\x44\x65leteAllMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\")\n\x15GetHolidayListRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"@\n\x16GetHolidayListResponse\x12&\n\x06groups\x18\x01 \x03(\x0b\x32\x16.schedule.HolidayGroup\"M\n\x11\x41\x64\x64HolidayRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\x06groups\x18\x02 \x03(\x0b\x32\x16.schedule.HolidayGroup\"\x14\n\x12\x41\x64\x64HolidayResponse\"S\n\x16\x41\x64\x64HolidayMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\x06groups\x18\x02 \x03(\x0b\x32\x16.schedule.HolidayGroup\"C\n\x17\x41\x64\x64HolidayMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\":\n\x14\x44\x65leteHolidayRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x10\n\x08groupIDs\x18\x02 \x03(\r\"\x17\n\x15\x44\x65leteHolidayResponse\"@\n\x19\x44\x65leteHolidayMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\x10\n\x08groupIDs\x18\x02 \x03(\r\"F\n\x1a\x44\x65leteHolidayMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"+\n\x17\x44\x65leteAllHolidayRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x1a\n\x18\x44\x65leteAllHolidayResponse\"1\n\x1c\x44\x65leteAllHolidayMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\"I\n\x1d\x44\x65leteAllHolidayMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse*\\\n\x11HolidayRecurrence\x12\x10\n\x0c\x44O_NOT_RECUR\x10\x00\x12\x10\n\x0cRECUR_YEARLY\x10\x01\x12\x11\n\rRECUR_MONTHLY\x10\x02\x12\x10\n\x0cRECUR_WEEKLY\x10\x03\x32\xd3\x08\n\x08Schedule\x12>\n\x07GetList\x12\x18.schedule.GetListRequest\x1a\x19.schedule.GetListResponse\x12\x32\n\x03\x41\x64\x64\x12\x14.schedule.AddRequest\x1a\x15.schedule.AddResponse\x12\x41\n\x08\x41\x64\x64Multi\x12\x19.schedule.AddMultiRequest\x1a\x1a.schedule.AddMultiResponse\x12;\n\x06\x44\x65lete\x12\x17.schedule.DeleteRequest\x1a\x18.schedule.DeleteResponse\x12J\n\x0b\x44\x65leteMulti\x12\x1c.schedule.DeleteMultiRequest\x1a\x1d.schedule.DeleteMultiResponse\x12\x44\n\tDeleteAll\x12\x1a.schedule.DeleteAllRequest\x1a\x1b.schedule.DeleteAllResponse\x12S\n\x0e\x44\x65leteAllMulti\x12\x1f.schedule.DeleteAllMultiRequest\x1a .schedule.DeleteAllMultiResponse\x12S\n\x0eGetHolidayList\x12\x1f.schedule.GetHolidayListRequest\x1a .schedule.GetHolidayListResponse\x12G\n\nAddHoliday\x12\x1b.schedule.AddHolidayRequest\x1a\x1c.schedule.AddHolidayResponse\x12V\n\x0f\x41\x64\x64HolidayMulti\x12 .schedule.AddHolidayMultiRequest\x1a!.schedule.AddHolidayMultiResponse\x12P\n\rDeleteHoliday\x12\x1e.schedule.DeleteHolidayRequest\x1a\x1f.schedule.DeleteHolidayResponse\x12_\n\x12\x44\x65leteHolidayMulti\x12#.schedule.DeleteHolidayMultiRequest\x1a$.schedule.DeleteHolidayMultiResponse\x12Y\n\x10\x44\x65leteAllHoliday\x12!.schedule.DeleteAllHolidayRequest\x1a\".schedule.DeleteAllHolidayResponse\x12h\n\x15\x44\x65leteAllHolidayMulti\x12&.schedule.DeleteAllHolidayMultiRequest\x1a\'.schedule.DeleteAllHolidayMultiResponseB9\n\x1b\x63om.supremainc.sdk.scheduleP\x01Z\x18\x62iostar/service/scheduleb\x06proto3')

_HOLIDAYRECURRENCE = DESCRIPTOR.enum_types_by_name['HolidayRecurrence']
HolidayRecurrence = enum_type_wrapper.EnumTypeWrapper(_HOLIDAYRECURRENCE)
DO_NOT_RECUR = 0
RECUR_YEARLY = 1
RECUR_MONTHLY = 2
RECUR_WEEKLY = 3


_SCHEDULEINFO = DESCRIPTOR.message_types_by_name['ScheduleInfo']
_DAYSCHEDULE = DESCRIPTOR.message_types_by_name['DaySchedule']
_TIMEPERIOD = DESCRIPTOR.message_types_by_name['TimePeriod']
_WEEKLYSCHEDULE = DESCRIPTOR.message_types_by_name['WeeklySchedule']
_DAILYSCHEDULE = DESCRIPTOR.message_types_by_name['DailySchedule']
_HOLIDAYSCHEDULE = DESCRIPTOR.message_types_by_name['HolidaySchedule']
_HOLIDAYGROUP = DESCRIPTOR.message_types_by_name['HolidayGroup']
_HOLIDAY = DESCRIPTOR.message_types_by_name['Holiday']
_GETLISTREQUEST = DESCRIPTOR.message_types_by_name['GetListRequest']
_GETLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetListResponse']
_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_ADDRESPONSE = DESCRIPTOR.message_types_by_name['AddResponse']
_ADDMULTIREQUEST = DESCRIPTOR.message_types_by_name['AddMultiRequest']
_ADDMULTIRESPONSE = DESCRIPTOR.message_types_by_name['AddMultiResponse']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETERESPONSE = DESCRIPTOR.message_types_by_name['DeleteResponse']
_DELETEMULTIREQUEST = DESCRIPTOR.message_types_by_name['DeleteMultiRequest']
_DELETEMULTIRESPONSE = DESCRIPTOR.message_types_by_name['DeleteMultiResponse']
_DELETEALLREQUEST = DESCRIPTOR.message_types_by_name['DeleteAllRequest']
_DELETEALLRESPONSE = DESCRIPTOR.message_types_by_name['DeleteAllResponse']
_DELETEALLMULTIREQUEST = DESCRIPTOR.message_types_by_name['DeleteAllMultiRequest']
_DELETEALLMULTIRESPONSE = DESCRIPTOR.message_types_by_name['DeleteAllMultiResponse']
_GETHOLIDAYLISTREQUEST = DESCRIPTOR.message_types_by_name['GetHolidayListRequest']
_GETHOLIDAYLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetHolidayListResponse']
_ADDHOLIDAYREQUEST = DESCRIPTOR.message_types_by_name['AddHolidayRequest']
_ADDHOLIDAYRESPONSE = DESCRIPTOR.message_types_by_name['AddHolidayResponse']
_ADDHOLIDAYMULTIREQUEST = DESCRIPTOR.message_types_by_name['AddHolidayMultiRequest']
_ADDHOLIDAYMULTIRESPONSE = DESCRIPTOR.message_types_by_name['AddHolidayMultiResponse']
_DELETEHOLIDAYREQUEST = DESCRIPTOR.message_types_by_name['DeleteHolidayRequest']
_DELETEHOLIDAYRESPONSE = DESCRIPTOR.message_types_by_name['DeleteHolidayResponse']
_DELETEHOLIDAYMULTIREQUEST = DESCRIPTOR.message_types_by_name['DeleteHolidayMultiRequest']
_DELETEHOLIDAYMULTIRESPONSE = DESCRIPTOR.message_types_by_name['DeleteHolidayMultiResponse']
_DELETEALLHOLIDAYREQUEST = DESCRIPTOR.message_types_by_name['DeleteAllHolidayRequest']
_DELETEALLHOLIDAYRESPONSE = DESCRIPTOR.message_types_by_name['DeleteAllHolidayResponse']
_DELETEALLHOLIDAYMULTIREQUEST = DESCRIPTOR.message_types_by_name['DeleteAllHolidayMultiRequest']
_DELETEALLHOLIDAYMULTIRESPONSE = DESCRIPTOR.message_types_by_name['DeleteAllHolidayMultiResponse']
ScheduleInfo = _reflection.GeneratedProtocolMessageType('ScheduleInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEINFO,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.ScheduleInfo)
  })
_sym_db.RegisterMessage(ScheduleInfo)

DaySchedule = _reflection.GeneratedProtocolMessageType('DaySchedule', (_message.Message,), {
  'DESCRIPTOR' : _DAYSCHEDULE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DaySchedule)
  })
_sym_db.RegisterMessage(DaySchedule)

TimePeriod = _reflection.GeneratedProtocolMessageType('TimePeriod', (_message.Message,), {
  'DESCRIPTOR' : _TIMEPERIOD,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.TimePeriod)
  })
_sym_db.RegisterMessage(TimePeriod)

WeeklySchedule = _reflection.GeneratedProtocolMessageType('WeeklySchedule', (_message.Message,), {
  'DESCRIPTOR' : _WEEKLYSCHEDULE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.WeeklySchedule)
  })
_sym_db.RegisterMessage(WeeklySchedule)

DailySchedule = _reflection.GeneratedProtocolMessageType('DailySchedule', (_message.Message,), {
  'DESCRIPTOR' : _DAILYSCHEDULE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DailySchedule)
  })
_sym_db.RegisterMessage(DailySchedule)

HolidaySchedule = _reflection.GeneratedProtocolMessageType('HolidaySchedule', (_message.Message,), {
  'DESCRIPTOR' : _HOLIDAYSCHEDULE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.HolidaySchedule)
  })
_sym_db.RegisterMessage(HolidaySchedule)

HolidayGroup = _reflection.GeneratedProtocolMessageType('HolidayGroup', (_message.Message,), {
  'DESCRIPTOR' : _HOLIDAYGROUP,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.HolidayGroup)
  })
_sym_db.RegisterMessage(HolidayGroup)

Holiday = _reflection.GeneratedProtocolMessageType('Holiday', (_message.Message,), {
  'DESCRIPTOR' : _HOLIDAY,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.Holiday)
  })
_sym_db.RegisterMessage(Holiday)

GetListRequest = _reflection.GeneratedProtocolMessageType('GetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.GetListRequest)
  })
_sym_db.RegisterMessage(GetListRequest)

GetListResponse = _reflection.GeneratedProtocolMessageType('GetListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.GetListResponse)
  })
_sym_db.RegisterMessage(GetListResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

AddMultiRequest = _reflection.GeneratedProtocolMessageType('AddMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddMultiRequest)
  })
_sym_db.RegisterMessage(AddMultiRequest)

AddMultiResponse = _reflection.GeneratedProtocolMessageType('AddMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddMultiResponse)
  })
_sym_db.RegisterMessage(AddMultiResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

DeleteMultiRequest = _reflection.GeneratedProtocolMessageType('DeleteMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteMultiRequest)
  })
_sym_db.RegisterMessage(DeleteMultiRequest)

DeleteMultiResponse = _reflection.GeneratedProtocolMessageType('DeleteMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteMultiResponse)
  })
_sym_db.RegisterMessage(DeleteMultiResponse)

DeleteAllRequest = _reflection.GeneratedProtocolMessageType('DeleteAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllRequest)
  })
_sym_db.RegisterMessage(DeleteAllRequest)

DeleteAllResponse = _reflection.GeneratedProtocolMessageType('DeleteAllResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllResponse)
  })
_sym_db.RegisterMessage(DeleteAllResponse)

DeleteAllMultiRequest = _reflection.GeneratedProtocolMessageType('DeleteAllMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllMultiRequest)
  })
_sym_db.RegisterMessage(DeleteAllMultiRequest)

DeleteAllMultiResponse = _reflection.GeneratedProtocolMessageType('DeleteAllMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllMultiResponse)
  })
_sym_db.RegisterMessage(DeleteAllMultiResponse)

GetHolidayListRequest = _reflection.GeneratedProtocolMessageType('GetHolidayListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETHOLIDAYLISTREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.GetHolidayListRequest)
  })
_sym_db.RegisterMessage(GetHolidayListRequest)

GetHolidayListResponse = _reflection.GeneratedProtocolMessageType('GetHolidayListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETHOLIDAYLISTRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.GetHolidayListResponse)
  })
_sym_db.RegisterMessage(GetHolidayListResponse)

AddHolidayRequest = _reflection.GeneratedProtocolMessageType('AddHolidayRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDHOLIDAYREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddHolidayRequest)
  })
_sym_db.RegisterMessage(AddHolidayRequest)

AddHolidayResponse = _reflection.GeneratedProtocolMessageType('AddHolidayResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDHOLIDAYRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddHolidayResponse)
  })
_sym_db.RegisterMessage(AddHolidayResponse)

AddHolidayMultiRequest = _reflection.GeneratedProtocolMessageType('AddHolidayMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDHOLIDAYMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddHolidayMultiRequest)
  })
_sym_db.RegisterMessage(AddHolidayMultiRequest)

AddHolidayMultiResponse = _reflection.GeneratedProtocolMessageType('AddHolidayMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDHOLIDAYMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.AddHolidayMultiResponse)
  })
_sym_db.RegisterMessage(AddHolidayMultiResponse)

DeleteHolidayRequest = _reflection.GeneratedProtocolMessageType('DeleteHolidayRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHOLIDAYREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteHolidayRequest)
  })
_sym_db.RegisterMessage(DeleteHolidayRequest)

DeleteHolidayResponse = _reflection.GeneratedProtocolMessageType('DeleteHolidayResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHOLIDAYRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteHolidayResponse)
  })
_sym_db.RegisterMessage(DeleteHolidayResponse)

DeleteHolidayMultiRequest = _reflection.GeneratedProtocolMessageType('DeleteHolidayMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHOLIDAYMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteHolidayMultiRequest)
  })
_sym_db.RegisterMessage(DeleteHolidayMultiRequest)

DeleteHolidayMultiResponse = _reflection.GeneratedProtocolMessageType('DeleteHolidayMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHOLIDAYMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteHolidayMultiResponse)
  })
_sym_db.RegisterMessage(DeleteHolidayMultiResponse)

DeleteAllHolidayRequest = _reflection.GeneratedProtocolMessageType('DeleteAllHolidayRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLHOLIDAYREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllHolidayRequest)
  })
_sym_db.RegisterMessage(DeleteAllHolidayRequest)

DeleteAllHolidayResponse = _reflection.GeneratedProtocolMessageType('DeleteAllHolidayResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLHOLIDAYRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllHolidayResponse)
  })
_sym_db.RegisterMessage(DeleteAllHolidayResponse)

DeleteAllHolidayMultiRequest = _reflection.GeneratedProtocolMessageType('DeleteAllHolidayMultiRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLHOLIDAYMULTIREQUEST,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllHolidayMultiRequest)
  })
_sym_db.RegisterMessage(DeleteAllHolidayMultiRequest)

DeleteAllHolidayMultiResponse = _reflection.GeneratedProtocolMessageType('DeleteAllHolidayMultiResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALLHOLIDAYMULTIRESPONSE,
  '__module__' : 'schedule_pb2'
  # @@protoc_insertion_point(class_scope:schedule.DeleteAllHolidayMultiResponse)
  })
_sym_db.RegisterMessage(DeleteAllHolidayMultiResponse)

_SCHEDULE = DESCRIPTOR.services_by_name['Schedule']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.supremainc.sdk.scheduleP\001Z\030biostar/service/schedule'
  _HOLIDAYRECURRENCE._serialized_start=2179
  _HOLIDAYRECURRENCE._serialized_end=2271
  _SCHEDULEINFO._serialized_start=40
  _SCHEDULEINFO._serialized_end=207
  _DAYSCHEDULE._serialized_start=209
  _DAYSCHEDULE._serialized_end=261
  _TIMEPERIOD._serialized_start=263
  _TIMEPERIOD._serialized_end=311
  _WEEKLYSCHEDULE._serialized_start=313
  _WEEKLYSCHEDULE._serialized_end=374
  _DAILYSCHEDULE._serialized_start=376
  _DAILYSCHEDULE._serialized_end=455
  _HOLIDAYSCHEDULE._serialized_start=457
  _HOLIDAYSCHEDULE._serialized_end=535
  _HOLIDAYGROUP._serialized_start=537
  _HOLIDAYGROUP._serialized_end=614
  _HOLIDAY._serialized_start=616
  _HOLIDAY._serialized_end=688
  _GETLISTREQUEST._serialized_start=690
  _GETLISTREQUEST._serialized_end=724
  _GETLISTRESPONSE._serialized_start=726
  _GETLISTRESPONSE._serialized_end=786
  _ADDREQUEST._serialized_start=788
  _ADDREQUEST._serialized_end=861
  _ADDRESPONSE._serialized_start=863
  _ADDRESPONSE._serialized_end=876
  _ADDMULTIREQUEST._serialized_start=878
  _ADDMULTIREQUEST._serialized_end=957
  _ADDMULTIRESPONSE._serialized_start=959
  _ADDMULTIRESPONSE._serialized_end=1019
  _DELETEREQUEST._serialized_start=1021
  _DELETEREQUEST._serialized_end=1075
  _DELETERESPONSE._serialized_start=1077
  _DELETERESPONSE._serialized_end=1093
  _DELETEMULTIREQUEST._serialized_start=1095
  _DELETEMULTIREQUEST._serialized_end=1155
  _DELETEMULTIRESPONSE._serialized_start=1157
  _DELETEMULTIRESPONSE._serialized_end=1220
  _DELETEALLREQUEST._serialized_start=1222
  _DELETEALLREQUEST._serialized_end=1258
  _DELETEALLRESPONSE._serialized_start=1260
  _DELETEALLRESPONSE._serialized_end=1279
  _DELETEALLMULTIREQUEST._serialized_start=1281
  _DELETEALLMULTIREQUEST._serialized_end=1323
  _DELETEALLMULTIRESPONSE._serialized_start=1325
  _DELETEALLMULTIRESPONSE._serialized_end=1391
  _GETHOLIDAYLISTREQUEST._serialized_start=1393
  _GETHOLIDAYLISTREQUEST._serialized_end=1434
  _GETHOLIDAYLISTRESPONSE._serialized_start=1436
  _GETHOLIDAYLISTRESPONSE._serialized_end=1500
  _ADDHOLIDAYREQUEST._serialized_start=1502
  _ADDHOLIDAYREQUEST._serialized_end=1579
  _ADDHOLIDAYRESPONSE._serialized_start=1581
  _ADDHOLIDAYRESPONSE._serialized_end=1601
  _ADDHOLIDAYMULTIREQUEST._serialized_start=1603
  _ADDHOLIDAYMULTIREQUEST._serialized_end=1686
  _ADDHOLIDAYMULTIRESPONSE._serialized_start=1688
  _ADDHOLIDAYMULTIRESPONSE._serialized_end=1755
  _DELETEHOLIDAYREQUEST._serialized_start=1757
  _DELETEHOLIDAYREQUEST._serialized_end=1815
  _DELETEHOLIDAYRESPONSE._serialized_start=1817
  _DELETEHOLIDAYRESPONSE._serialized_end=1840
  _DELETEHOLIDAYMULTIREQUEST._serialized_start=1842
  _DELETEHOLIDAYMULTIREQUEST._serialized_end=1906
  _DELETEHOLIDAYMULTIRESPONSE._serialized_start=1908
  _DELETEHOLIDAYMULTIRESPONSE._serialized_end=1978
  _DELETEALLHOLIDAYREQUEST._serialized_start=1980
  _DELETEALLHOLIDAYREQUEST._serialized_end=2023
  _DELETEALLHOLIDAYRESPONSE._serialized_start=2025
  _DELETEALLHOLIDAYRESPONSE._serialized_end=2051
  _DELETEALLHOLIDAYMULTIREQUEST._serialized_start=2053
  _DELETEALLHOLIDAYMULTIREQUEST._serialized_end=2102
  _DELETEALLHOLIDAYMULTIRESPONSE._serialized_start=2104
  _DELETEALLHOLIDAYMULTIRESPONSE._serialized_end=2177
  _SCHEDULE._serialized_start=2274
  _SCHEDULE._serialized_end=3381
# @@protoc_insertion_point(module_scope)