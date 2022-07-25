# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import schedule_pb2 as schedule__pb2


class ScheduleStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetList = channel.unary_unary(
        '/schedule.Schedule/GetList',
        request_serializer=schedule__pb2.GetListRequest.SerializeToString,
        response_deserializer=schedule__pb2.GetListResponse.FromString,
        )
    self.Add = channel.unary_unary(
        '/schedule.Schedule/Add',
        request_serializer=schedule__pb2.AddRequest.SerializeToString,
        response_deserializer=schedule__pb2.AddResponse.FromString,
        )
    self.AddMulti = channel.unary_unary(
        '/schedule.Schedule/AddMulti',
        request_serializer=schedule__pb2.AddMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.AddMultiResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/schedule.Schedule/Delete',
        request_serializer=schedule__pb2.DeleteRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteResponse.FromString,
        )
    self.DeleteMulti = channel.unary_unary(
        '/schedule.Schedule/DeleteMulti',
        request_serializer=schedule__pb2.DeleteMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteMultiResponse.FromString,
        )
    self.DeleteAll = channel.unary_unary(
        '/schedule.Schedule/DeleteAll',
        request_serializer=schedule__pb2.DeleteAllRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteAllResponse.FromString,
        )
    self.DeleteAllMulti = channel.unary_unary(
        '/schedule.Schedule/DeleteAllMulti',
        request_serializer=schedule__pb2.DeleteAllMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteAllMultiResponse.FromString,
        )
    self.GetHolidayList = channel.unary_unary(
        '/schedule.Schedule/GetHolidayList',
        request_serializer=schedule__pb2.GetHolidayListRequest.SerializeToString,
        response_deserializer=schedule__pb2.GetHolidayListResponse.FromString,
        )
    self.AddHoliday = channel.unary_unary(
        '/schedule.Schedule/AddHoliday',
        request_serializer=schedule__pb2.AddHolidayRequest.SerializeToString,
        response_deserializer=schedule__pb2.AddHolidayResponse.FromString,
        )
    self.AddHolidayMulti = channel.unary_unary(
        '/schedule.Schedule/AddHolidayMulti',
        request_serializer=schedule__pb2.AddHolidayMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.AddHolidayMultiResponse.FromString,
        )
    self.DeleteHoliday = channel.unary_unary(
        '/schedule.Schedule/DeleteHoliday',
        request_serializer=schedule__pb2.DeleteHolidayRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteHolidayResponse.FromString,
        )
    self.DeleteHolidayMulti = channel.unary_unary(
        '/schedule.Schedule/DeleteHolidayMulti',
        request_serializer=schedule__pb2.DeleteHolidayMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteHolidayMultiResponse.FromString,
        )
    self.DeleteAllHoliday = channel.unary_unary(
        '/schedule.Schedule/DeleteAllHoliday',
        request_serializer=schedule__pb2.DeleteAllHolidayRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteAllHolidayResponse.FromString,
        )
    self.DeleteAllHolidayMulti = channel.unary_unary(
        '/schedule.Schedule/DeleteAllHolidayMulti',
        request_serializer=schedule__pb2.DeleteAllHolidayMultiRequest.SerializeToString,
        response_deserializer=schedule__pb2.DeleteAllHolidayMultiResponse.FromString,
        )


class ScheduleServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHolidayList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHoliday(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHolidayMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHoliday(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHolidayMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllHoliday(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllHolidayMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ScheduleServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetList': grpc.unary_unary_rpc_method_handler(
          servicer.GetList,
          request_deserializer=schedule__pb2.GetListRequest.FromString,
          response_serializer=schedule__pb2.GetListResponse.SerializeToString,
      ),
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=schedule__pb2.AddRequest.FromString,
          response_serializer=schedule__pb2.AddResponse.SerializeToString,
      ),
      'AddMulti': grpc.unary_unary_rpc_method_handler(
          servicer.AddMulti,
          request_deserializer=schedule__pb2.AddMultiRequest.FromString,
          response_serializer=schedule__pb2.AddMultiResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=schedule__pb2.DeleteRequest.FromString,
          response_serializer=schedule__pb2.DeleteResponse.SerializeToString,
      ),
      'DeleteMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMulti,
          request_deserializer=schedule__pb2.DeleteMultiRequest.FromString,
          response_serializer=schedule__pb2.DeleteMultiResponse.SerializeToString,
      ),
      'DeleteAll': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAll,
          request_deserializer=schedule__pb2.DeleteAllRequest.FromString,
          response_serializer=schedule__pb2.DeleteAllResponse.SerializeToString,
      ),
      'DeleteAllMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllMulti,
          request_deserializer=schedule__pb2.DeleteAllMultiRequest.FromString,
          response_serializer=schedule__pb2.DeleteAllMultiResponse.SerializeToString,
      ),
      'GetHolidayList': grpc.unary_unary_rpc_method_handler(
          servicer.GetHolidayList,
          request_deserializer=schedule__pb2.GetHolidayListRequest.FromString,
          response_serializer=schedule__pb2.GetHolidayListResponse.SerializeToString,
      ),
      'AddHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.AddHoliday,
          request_deserializer=schedule__pb2.AddHolidayRequest.FromString,
          response_serializer=schedule__pb2.AddHolidayResponse.SerializeToString,
      ),
      'AddHolidayMulti': grpc.unary_unary_rpc_method_handler(
          servicer.AddHolidayMulti,
          request_deserializer=schedule__pb2.AddHolidayMultiRequest.FromString,
          response_serializer=schedule__pb2.AddHolidayMultiResponse.SerializeToString,
      ),
      'DeleteHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHoliday,
          request_deserializer=schedule__pb2.DeleteHolidayRequest.FromString,
          response_serializer=schedule__pb2.DeleteHolidayResponse.SerializeToString,
      ),
      'DeleteHolidayMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHolidayMulti,
          request_deserializer=schedule__pb2.DeleteHolidayMultiRequest.FromString,
          response_serializer=schedule__pb2.DeleteHolidayMultiResponse.SerializeToString,
      ),
      'DeleteAllHoliday': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllHoliday,
          request_deserializer=schedule__pb2.DeleteAllHolidayRequest.FromString,
          response_serializer=schedule__pb2.DeleteAllHolidayResponse.SerializeToString,
      ),
      'DeleteAllHolidayMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllHolidayMulti,
          request_deserializer=schedule__pb2.DeleteAllHolidayMultiRequest.FromString,
          response_serializer=schedule__pb2.DeleteAllHolidayMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'schedule.Schedule', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
