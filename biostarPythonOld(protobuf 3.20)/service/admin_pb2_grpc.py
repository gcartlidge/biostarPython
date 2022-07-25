# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import admin_pb2 as admin__pb2


class AdminStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetInfo = channel.unary_unary(
        '/admin.Admin/GetInfo',
        request_serializer=admin__pb2.GetInfoRequest.SerializeToString,
        response_deserializer=admin__pb2.GetInfoResponse.FromString,
        )


class AdminServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfo,
          request_deserializer=admin__pb2.GetInfoRequest.FromString,
          response_serializer=admin__pb2.GetInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'admin.Admin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))