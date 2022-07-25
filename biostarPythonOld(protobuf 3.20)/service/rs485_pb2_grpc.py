# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import rs485_pb2 as rs485__pb2


class RS485Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SearchDevice = channel.unary_unary(
        '/rs485.RS485/SearchDevice',
        request_serializer=rs485__pb2.SearchDeviceRequest.SerializeToString,
        response_deserializer=rs485__pb2.SearchDeviceResponse.FromString,
        )
    self.GetDevice = channel.unary_unary(
        '/rs485.RS485/GetDevice',
        request_serializer=rs485__pb2.GetDeviceRequest.SerializeToString,
        response_deserializer=rs485__pb2.GetDeviceResponse.FromString,
        )
    self.SetDevice = channel.unary_unary(
        '/rs485.RS485/SetDevice',
        request_serializer=rs485__pb2.SetDeviceRequest.SerializeToString,
        response_deserializer=rs485__pb2.SetDeviceResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/rs485.RS485/GetConfig',
        request_serializer=rs485__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=rs485__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/rs485.RS485/SetConfig',
        request_serializer=rs485__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=rs485__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/rs485.RS485/SetConfigMulti',
        request_serializer=rs485__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=rs485__pb2.SetConfigMultiResponse.FromString,
        )


class RS485Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SearchDevice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDevice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDevice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RS485Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SearchDevice': grpc.unary_unary_rpc_method_handler(
          servicer.SearchDevice,
          request_deserializer=rs485__pb2.SearchDeviceRequest.FromString,
          response_serializer=rs485__pb2.SearchDeviceResponse.SerializeToString,
      ),
      'GetDevice': grpc.unary_unary_rpc_method_handler(
          servicer.GetDevice,
          request_deserializer=rs485__pb2.GetDeviceRequest.FromString,
          response_serializer=rs485__pb2.GetDeviceResponse.SerializeToString,
      ),
      'SetDevice': grpc.unary_unary_rpc_method_handler(
          servicer.SetDevice,
          request_deserializer=rs485__pb2.SetDeviceRequest.FromString,
          response_serializer=rs485__pb2.SetDeviceResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=rs485__pb2.GetConfigRequest.FromString,
          response_serializer=rs485__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=rs485__pb2.SetConfigRequest.FromString,
          response_serializer=rs485__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=rs485__pb2.SetConfigMultiRequest.FromString,
          response_serializer=rs485__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rs485.RS485', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
