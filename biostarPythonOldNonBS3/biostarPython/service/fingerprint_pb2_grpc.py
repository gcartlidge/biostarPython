# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import fingerprint_pb2 as fingerprint__pb2


class FingerprintStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_unary(
                '/fingerprint.Fingerprint/Scan',
                request_serializer=fingerprint__pb2.ScanRequest.SerializeToString,
                response_deserializer=fingerprint__pb2.ScanResponse.FromString,
                )
        self.GetImage = channel.unary_unary(
                '/fingerprint.Fingerprint/GetImage',
                request_serializer=fingerprint__pb2.GetImageRequest.SerializeToString,
                response_deserializer=fingerprint__pb2.GetImageResponse.FromString,
                )


class FingerprintServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Scan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FingerprintServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=fingerprint__pb2.ScanRequest.FromString,
                    response_serializer=fingerprint__pb2.ScanResponse.SerializeToString,
            ),
            'GetImage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImage,
                    request_deserializer=fingerprint__pb2.GetImageRequest.FromString,
                    response_serializer=fingerprint__pb2.GetImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fingerprint.Fingerprint', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Fingerprint(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fingerprint.Fingerprint/Scan',
            fingerprint__pb2.ScanRequest.SerializeToString,
            fingerprint__pb2.ScanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fingerprint.Fingerprint/GetImage',
            fingerprint__pb2.GetImageRequest.SerializeToString,
            fingerprint__pb2.GetImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)