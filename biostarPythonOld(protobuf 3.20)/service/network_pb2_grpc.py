# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import network_pb2 as network__pb2


class NetworkStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetIPConfig = channel.unary_unary(
        '/network.Network/GetIPConfig',
        request_serializer=network__pb2.GetIPConfigRequest.SerializeToString,
        response_deserializer=network__pb2.GetIPConfigResponse.FromString,
        )
    self.SetIPConfig = channel.unary_unary(
        '/network.Network/SetIPConfig',
        request_serializer=network__pb2.SetIPConfigRequest.SerializeToString,
        response_deserializer=network__pb2.SetIPConfigResponse.FromString,
        )
    self.SetIPConfigMulti = channel.unary_unary(
        '/network.Network/SetIPConfigMulti',
        request_serializer=network__pb2.SetIPConfigMultiRequest.SerializeToString,
        response_deserializer=network__pb2.SetIPConfigMultiResponse.FromString,
        )
    self.GetWLANConfig = channel.unary_unary(
        '/network.Network/GetWLANConfig',
        request_serializer=network__pb2.GetWLANConfigRequest.SerializeToString,
        response_deserializer=network__pb2.GetWLANConfigResponse.FromString,
        )
    self.SetWLANConfig = channel.unary_unary(
        '/network.Network/SetWLANConfig',
        request_serializer=network__pb2.SetWLANConfigRequest.SerializeToString,
        response_deserializer=network__pb2.SetWLANConfigResponse.FromString,
        )
    self.SetWLANConfigMulti = channel.unary_unary(
        '/network.Network/SetWLANConfigMulti',
        request_serializer=network__pb2.SetWLANConfigMultiRequest.SerializeToString,
        response_deserializer=network__pb2.SetWLANConfigMultiResponse.FromString,
        )


class NetworkServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetIPConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetIPConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetIPConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWLANConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetWLANConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetWLANConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetIPConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetIPConfig,
          request_deserializer=network__pb2.GetIPConfigRequest.FromString,
          response_serializer=network__pb2.GetIPConfigResponse.SerializeToString,
      ),
      'SetIPConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetIPConfig,
          request_deserializer=network__pb2.SetIPConfigRequest.FromString,
          response_serializer=network__pb2.SetIPConfigResponse.SerializeToString,
      ),
      'SetIPConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetIPConfigMulti,
          request_deserializer=network__pb2.SetIPConfigMultiRequest.FromString,
          response_serializer=network__pb2.SetIPConfigMultiResponse.SerializeToString,
      ),
      'GetWLANConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetWLANConfig,
          request_deserializer=network__pb2.GetWLANConfigRequest.FromString,
          response_serializer=network__pb2.GetWLANConfigResponse.SerializeToString,
      ),
      'SetWLANConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetWLANConfig,
          request_deserializer=network__pb2.SetWLANConfigRequest.FromString,
          response_serializer=network__pb2.SetWLANConfigResponse.SerializeToString,
      ),
      'SetWLANConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetWLANConfigMulti,
          request_deserializer=network__pb2.SetWLANConfigMultiRequest.FromString,
          response_serializer=network__pb2.SetWLANConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'network.Network', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
