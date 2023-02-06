# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import master_pb2 as master__pb2


class MasterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_unary(
                '/gsdk.master.Master/Subscribe',
                request_serializer=master__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=master__pb2.SubscribeResponse.FromString,
                )
        self.UpdateDeviceList = channel.unary_unary(
                '/gsdk.master.Master/UpdateDeviceList',
                request_serializer=master__pb2.UpdateDeviceListRequest.SerializeToString,
                response_deserializer=master__pb2.UpdateDeviceListResponse.FromString,
                )
        self.InitCommandChan = channel.stream_stream(
                '/gsdk.master.Master/InitCommandChan',
                request_serializer=master__pb2.CommandResponse.SerializeToString,
                response_deserializer=master__pb2.CommandRequest.FromString,
                )
        self.InitLogChan = channel.stream_unary(
                '/gsdk.master.Master/InitLogChan',
                request_serializer=master__pb2.RealtimeEvent.SerializeToString,
                response_deserializer=master__pb2.InitLogChanResponse.FromString,
                )
        self.InitDeviceStatusChan = channel.stream_unary(
                '/gsdk.master.Master/InitDeviceStatusChan',
                request_serializer=master__pb2.DeviceStatus.SerializeToString,
                response_deserializer=master__pb2.InitDeviceStatusChanResponse.FromString,
                )


class MasterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDeviceList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitCommandChan(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitLogChan(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitDeviceStatusChan(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=master__pb2.SubscribeRequest.FromString,
                    response_serializer=master__pb2.SubscribeResponse.SerializeToString,
            ),
            'UpdateDeviceList': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDeviceList,
                    request_deserializer=master__pb2.UpdateDeviceListRequest.FromString,
                    response_serializer=master__pb2.UpdateDeviceListResponse.SerializeToString,
            ),
            'InitCommandChan': grpc.stream_stream_rpc_method_handler(
                    servicer.InitCommandChan,
                    request_deserializer=master__pb2.CommandResponse.FromString,
                    response_serializer=master__pb2.CommandRequest.SerializeToString,
            ),
            'InitLogChan': grpc.stream_unary_rpc_method_handler(
                    servicer.InitLogChan,
                    request_deserializer=master__pb2.RealtimeEvent.FromString,
                    response_serializer=master__pb2.InitLogChanResponse.SerializeToString,
            ),
            'InitDeviceStatusChan': grpc.stream_unary_rpc_method_handler(
                    servicer.InitDeviceStatusChan,
                    request_deserializer=master__pb2.DeviceStatus.FromString,
                    response_serializer=master__pb2.InitDeviceStatusChanResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.master.Master', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Master(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.master.Master/Subscribe',
            master__pb2.SubscribeRequest.SerializeToString,
            master__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDeviceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.master.Master/UpdateDeviceList',
            master__pb2.UpdateDeviceListRequest.SerializeToString,
            master__pb2.UpdateDeviceListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitCommandChan(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gsdk.master.Master/InitCommandChan',
            master__pb2.CommandResponse.SerializeToString,
            master__pb2.CommandRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitLogChan(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/gsdk.master.Master/InitLogChan',
            master__pb2.RealtimeEvent.SerializeToString,
            master__pb2.InitLogChanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitDeviceStatusChan(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/gsdk.master.Master/InitDeviceStatusChan',
            master__pb2.DeviceStatus.SerializeToString,
            master__pb2.InitDeviceStatusChanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
