# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import server_pb2 as server__pb2


class ServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_stream(
                '/gsdk.server.Server/Subscribe',
                request_serializer=server__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=server__pb2.ServerRequest.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/gsdk.server.Server/Unsubscribe',
                request_serializer=server__pb2.UnsubscribeRequest.SerializeToString,
                response_deserializer=server__pb2.UnsubscribeResponse.FromString,
                )
        self.HandleVerify = channel.unary_unary(
                '/gsdk.server.Server/HandleVerify',
                request_serializer=server__pb2.HandleVerifyRequest.SerializeToString,
                response_deserializer=server__pb2.HandleVerifyResponse.FromString,
                )
        self.HandleIdentify = channel.unary_unary(
                '/gsdk.server.Server/HandleIdentify',
                request_serializer=server__pb2.HandleIdentifyRequest.SerializeToString,
                response_deserializer=server__pb2.HandleIdentifyResponse.FromString,
                )
        self.HandleGlobalAPB = channel.unary_unary(
                '/gsdk.server.Server/HandleGlobalAPB',
                request_serializer=server__pb2.HandleGlobalAPBRequest.SerializeToString,
                response_deserializer=server__pb2.HandleGlobalAPBResponse.FromString,
                )
        self.HandleUserPhrase = channel.unary_unary(
                '/gsdk.server.Server/HandleUserPhrase',
                request_serializer=server__pb2.HandleUserPhraseRequest.SerializeToString,
                response_deserializer=server__pb2.HandleUserPhraseResponse.FromString,
                )


class ServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleVerify(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleIdentify(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleGlobalAPB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleUserPhrase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=server__pb2.SubscribeRequest.FromString,
                    response_serializer=server__pb2.ServerRequest.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=server__pb2.UnsubscribeRequest.FromString,
                    response_serializer=server__pb2.UnsubscribeResponse.SerializeToString,
            ),
            'HandleVerify': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleVerify,
                    request_deserializer=server__pb2.HandleVerifyRequest.FromString,
                    response_serializer=server__pb2.HandleVerifyResponse.SerializeToString,
            ),
            'HandleIdentify': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleIdentify,
                    request_deserializer=server__pb2.HandleIdentifyRequest.FromString,
                    response_serializer=server__pb2.HandleIdentifyResponse.SerializeToString,
            ),
            'HandleGlobalAPB': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleGlobalAPB,
                    request_deserializer=server__pb2.HandleGlobalAPBRequest.FromString,
                    response_serializer=server__pb2.HandleGlobalAPBResponse.SerializeToString,
            ),
            'HandleUserPhrase': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleUserPhrase,
                    request_deserializer=server__pb2.HandleUserPhraseRequest.FromString,
                    response_serializer=server__pb2.HandleUserPhraseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.server.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
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
        return grpc.experimental.unary_stream(request, target, '/gsdk.server.Server/Subscribe',
            server__pb2.SubscribeRequest.SerializeToString,
            server__pb2.ServerRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.server.Server/Unsubscribe',
            server__pb2.UnsubscribeRequest.SerializeToString,
            server__pb2.UnsubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleVerify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.server.Server/HandleVerify',
            server__pb2.HandleVerifyRequest.SerializeToString,
            server__pb2.HandleVerifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleIdentify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.server.Server/HandleIdentify',
            server__pb2.HandleIdentifyRequest.SerializeToString,
            server__pb2.HandleIdentifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleGlobalAPB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.server.Server/HandleGlobalAPB',
            server__pb2.HandleGlobalAPBRequest.SerializeToString,
            server__pb2.HandleGlobalAPBResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleUserPhrase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.server.Server/HandleUserPhrase',
            server__pb2.HandleUserPhraseRequest.SerializeToString,
            server__pb2.HandleUserPhraseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
