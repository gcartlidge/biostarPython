# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import config_pb2 as config__pb2


class ConfigStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSystem = channel.unary_unary(
        '/config.Config/GetSystem',
        request_serializer=config__pb2.GetSystemRequest.SerializeToString,
        response_deserializer=config__pb2.GetSystemResponse.FromString,
        )
    self.SetSystem = channel.unary_unary(
        '/config.Config/SetSystem',
        request_serializer=config__pb2.SetSystemRequest.SerializeToString,
        response_deserializer=config__pb2.SetSystemResponse.FromString,
        )
    self.SetSystemMulti = channel.unary_unary(
        '/config.Config/SetSystemMulti',
        request_serializer=config__pb2.SetSystemMultiRequest.SerializeToString,
        response_deserializer=config__pb2.SetSystemMultiResponse.FromString,
        )


class ConfigServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSystem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSystem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSystemMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConfigServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSystem': grpc.unary_unary_rpc_method_handler(
          servicer.GetSystem,
          request_deserializer=config__pb2.GetSystemRequest.FromString,
          response_serializer=config__pb2.GetSystemResponse.SerializeToString,
      ),
      'SetSystem': grpc.unary_unary_rpc_method_handler(
          servicer.SetSystem,
          request_deserializer=config__pb2.SetSystemRequest.FromString,
          response_serializer=config__pb2.SetSystemResponse.SerializeToString,
      ),
      'SetSystemMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetSystemMulti,
          request_deserializer=config__pb2.SetSystemMultiRequest.FromString,
          response_serializer=config__pb2.SetSystemMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'config.Config', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
