# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import access_pb2 as access__pb2


class AccessStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetList = channel.unary_unary(
        '/access.Access/GetList',
        request_serializer=access__pb2.GetListRequest.SerializeToString,
        response_deserializer=access__pb2.GetListResponse.FromString,
        )
    self.Add = channel.unary_unary(
        '/access.Access/Add',
        request_serializer=access__pb2.AddRequest.SerializeToString,
        response_deserializer=access__pb2.AddResponse.FromString,
        )
    self.AddMulti = channel.unary_unary(
        '/access.Access/AddMulti',
        request_serializer=access__pb2.AddMultiRequest.SerializeToString,
        response_deserializer=access__pb2.AddMultiResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/access.Access/Delete',
        request_serializer=access__pb2.DeleteRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteResponse.FromString,
        )
    self.DeleteMulti = channel.unary_unary(
        '/access.Access/DeleteMulti',
        request_serializer=access__pb2.DeleteMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteMultiResponse.FromString,
        )
    self.DeleteAll = channel.unary_unary(
        '/access.Access/DeleteAll',
        request_serializer=access__pb2.DeleteAllRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllResponse.FromString,
        )
    self.DeleteAllMulti = channel.unary_unary(
        '/access.Access/DeleteAllMulti',
        request_serializer=access__pb2.DeleteAllMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllMultiResponse.FromString,
        )
    self.GetLevelList = channel.unary_unary(
        '/access.Access/GetLevelList',
        request_serializer=access__pb2.GetLevelListRequest.SerializeToString,
        response_deserializer=access__pb2.GetLevelListResponse.FromString,
        )
    self.AddLevel = channel.unary_unary(
        '/access.Access/AddLevel',
        request_serializer=access__pb2.AddLevelRequest.SerializeToString,
        response_deserializer=access__pb2.AddLevelResponse.FromString,
        )
    self.AddLevelMulti = channel.unary_unary(
        '/access.Access/AddLevelMulti',
        request_serializer=access__pb2.AddLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.AddLevelMultiResponse.FromString,
        )
    self.DeleteLevel = channel.unary_unary(
        '/access.Access/DeleteLevel',
        request_serializer=access__pb2.DeleteLevelRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteLevelResponse.FromString,
        )
    self.DeleteLevelMulti = channel.unary_unary(
        '/access.Access/DeleteLevelMulti',
        request_serializer=access__pb2.DeleteLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteLevelMultiResponse.FromString,
        )
    self.DeleteAllLevel = channel.unary_unary(
        '/access.Access/DeleteAllLevel',
        request_serializer=access__pb2.DeleteAllLevelRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllLevelResponse.FromString,
        )
    self.DeleteAllLevelMulti = channel.unary_unary(
        '/access.Access/DeleteAllLevelMulti',
        request_serializer=access__pb2.DeleteAllLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllLevelMultiResponse.FromString,
        )
    self.GetFloorLevelList = channel.unary_unary(
        '/access.Access/GetFloorLevelList',
        request_serializer=access__pb2.GetFloorLevelListRequest.SerializeToString,
        response_deserializer=access__pb2.GetFloorLevelListResponse.FromString,
        )
    self.AddFloorLevel = channel.unary_unary(
        '/access.Access/AddFloorLevel',
        request_serializer=access__pb2.AddFloorLevelRequest.SerializeToString,
        response_deserializer=access__pb2.AddFloorLevelResponse.FromString,
        )
    self.AddFloorLevelMulti = channel.unary_unary(
        '/access.Access/AddFloorLevelMulti',
        request_serializer=access__pb2.AddFloorLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.AddFloorLevelMultiResponse.FromString,
        )
    self.DeleteFloorLevel = channel.unary_unary(
        '/access.Access/DeleteFloorLevel',
        request_serializer=access__pb2.DeleteFloorLevelRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteFloorLevelResponse.FromString,
        )
    self.DeleteFloorLevelMulti = channel.unary_unary(
        '/access.Access/DeleteFloorLevelMulti',
        request_serializer=access__pb2.DeleteFloorLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteFloorLevelMultiResponse.FromString,
        )
    self.DeleteAllFloorLevel = channel.unary_unary(
        '/access.Access/DeleteAllFloorLevel',
        request_serializer=access__pb2.DeleteAllFloorLevelRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllFloorLevelResponse.FromString,
        )
    self.DeleteAllFloorLevelMulti = channel.unary_unary(
        '/access.Access/DeleteAllFloorLevelMulti',
        request_serializer=access__pb2.DeleteAllFloorLevelMultiRequest.SerializeToString,
        response_deserializer=access__pb2.DeleteAllFloorLevelMultiResponse.FromString,
        )


class AccessServicer(object):
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

  def GetLevelList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFloorLevelList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddFloorLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddFloorLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteFloorLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteFloorLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllFloorLevel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllFloorLevelMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccessServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetList': grpc.unary_unary_rpc_method_handler(
          servicer.GetList,
          request_deserializer=access__pb2.GetListRequest.FromString,
          response_serializer=access__pb2.GetListResponse.SerializeToString,
      ),
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=access__pb2.AddRequest.FromString,
          response_serializer=access__pb2.AddResponse.SerializeToString,
      ),
      'AddMulti': grpc.unary_unary_rpc_method_handler(
          servicer.AddMulti,
          request_deserializer=access__pb2.AddMultiRequest.FromString,
          response_serializer=access__pb2.AddMultiResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=access__pb2.DeleteRequest.FromString,
          response_serializer=access__pb2.DeleteResponse.SerializeToString,
      ),
      'DeleteMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMulti,
          request_deserializer=access__pb2.DeleteMultiRequest.FromString,
          response_serializer=access__pb2.DeleteMultiResponse.SerializeToString,
      ),
      'DeleteAll': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAll,
          request_deserializer=access__pb2.DeleteAllRequest.FromString,
          response_serializer=access__pb2.DeleteAllResponse.SerializeToString,
      ),
      'DeleteAllMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllMulti,
          request_deserializer=access__pb2.DeleteAllMultiRequest.FromString,
          response_serializer=access__pb2.DeleteAllMultiResponse.SerializeToString,
      ),
      'GetLevelList': grpc.unary_unary_rpc_method_handler(
          servicer.GetLevelList,
          request_deserializer=access__pb2.GetLevelListRequest.FromString,
          response_serializer=access__pb2.GetLevelListResponse.SerializeToString,
      ),
      'AddLevel': grpc.unary_unary_rpc_method_handler(
          servicer.AddLevel,
          request_deserializer=access__pb2.AddLevelRequest.FromString,
          response_serializer=access__pb2.AddLevelResponse.SerializeToString,
      ),
      'AddLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.AddLevelMulti,
          request_deserializer=access__pb2.AddLevelMultiRequest.FromString,
          response_serializer=access__pb2.AddLevelMultiResponse.SerializeToString,
      ),
      'DeleteLevel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLevel,
          request_deserializer=access__pb2.DeleteLevelRequest.FromString,
          response_serializer=access__pb2.DeleteLevelResponse.SerializeToString,
      ),
      'DeleteLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLevelMulti,
          request_deserializer=access__pb2.DeleteLevelMultiRequest.FromString,
          response_serializer=access__pb2.DeleteLevelMultiResponse.SerializeToString,
      ),
      'DeleteAllLevel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllLevel,
          request_deserializer=access__pb2.DeleteAllLevelRequest.FromString,
          response_serializer=access__pb2.DeleteAllLevelResponse.SerializeToString,
      ),
      'DeleteAllLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllLevelMulti,
          request_deserializer=access__pb2.DeleteAllLevelMultiRequest.FromString,
          response_serializer=access__pb2.DeleteAllLevelMultiResponse.SerializeToString,
      ),
      'GetFloorLevelList': grpc.unary_unary_rpc_method_handler(
          servicer.GetFloorLevelList,
          request_deserializer=access__pb2.GetFloorLevelListRequest.FromString,
          response_serializer=access__pb2.GetFloorLevelListResponse.SerializeToString,
      ),
      'AddFloorLevel': grpc.unary_unary_rpc_method_handler(
          servicer.AddFloorLevel,
          request_deserializer=access__pb2.AddFloorLevelRequest.FromString,
          response_serializer=access__pb2.AddFloorLevelResponse.SerializeToString,
      ),
      'AddFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.AddFloorLevelMulti,
          request_deserializer=access__pb2.AddFloorLevelMultiRequest.FromString,
          response_serializer=access__pb2.AddFloorLevelMultiResponse.SerializeToString,
      ),
      'DeleteFloorLevel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteFloorLevel,
          request_deserializer=access__pb2.DeleteFloorLevelRequest.FromString,
          response_serializer=access__pb2.DeleteFloorLevelResponse.SerializeToString,
      ),
      'DeleteFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteFloorLevelMulti,
          request_deserializer=access__pb2.DeleteFloorLevelMultiRequest.FromString,
          response_serializer=access__pb2.DeleteFloorLevelMultiResponse.SerializeToString,
      ),
      'DeleteAllFloorLevel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllFloorLevel,
          request_deserializer=access__pb2.DeleteAllFloorLevelRequest.FromString,
          response_serializer=access__pb2.DeleteAllFloorLevelResponse.SerializeToString,
      ),
      'DeleteAllFloorLevelMulti': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllFloorLevelMulti,
          request_deserializer=access__pb2.DeleteAllFloorLevelMultiRequest.FromString,
          response_serializer=access__pb2.DeleteAllFloorLevelMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'access.Access', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
