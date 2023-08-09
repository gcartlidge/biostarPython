# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from biostarPython.service import cert_pb2 as cert__pb2


class CertStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateServerCertificate = channel.unary_unary(
                '/gsdk.cert.Cert/CreateServerCertificate',
                request_serializer=cert__pb2.CreateServerCertificateRequest.SerializeToString,
                response_deserializer=cert__pb2.CreateServerCertificateResponse.FromString,
                )
        self.SetServerCertificate = channel.unary_unary(
                '/gsdk.cert.Cert/SetServerCertificate',
                request_serializer=cert__pb2.SetServerCertificateRequest.SerializeToString,
                response_deserializer=cert__pb2.SetServerCertificateResponse.FromString,
                )
        self.SetGatewayCertificate = channel.unary_unary(
                '/gsdk.cert.Cert/SetGatewayCertificate',
                request_serializer=cert__pb2.SetGatewayCertificateRequest.SerializeToString,
                response_deserializer=cert__pb2.SetGatewayCertificateResponse.FromString,
                )


class CertServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateServerCertificate(self, request, context):
        """Server Certificate
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetServerCertificate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetGatewayCertificate(self, request, context):
        """Set Gatweay Certificate: for Device Gateway only
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CertServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateServerCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateServerCertificate,
                    request_deserializer=cert__pb2.CreateServerCertificateRequest.FromString,
                    response_serializer=cert__pb2.CreateServerCertificateResponse.SerializeToString,
            ),
            'SetServerCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetServerCertificate,
                    request_deserializer=cert__pb2.SetServerCertificateRequest.FromString,
                    response_serializer=cert__pb2.SetServerCertificateResponse.SerializeToString,
            ),
            'SetGatewayCertificate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetGatewayCertificate,
                    request_deserializer=cert__pb2.SetGatewayCertificateRequest.FromString,
                    response_serializer=cert__pb2.SetGatewayCertificateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.cert.Cert', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Cert(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateServerCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.cert.Cert/CreateServerCertificate',
            cert__pb2.CreateServerCertificateRequest.SerializeToString,
            cert__pb2.CreateServerCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetServerCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.cert.Cert/SetServerCertificate',
            cert__pb2.SetServerCertificateRequest.SerializeToString,
            cert__pb2.SetServerCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetGatewayCertificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gsdk.cert.Cert/SetGatewayCertificate',
            cert__pb2.SetGatewayCertificateRequest.SerializeToString,
            cert__pb2.SetGatewayCertificateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)