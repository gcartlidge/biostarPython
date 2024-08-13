# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from biostarPython.service import device_pb2 as device__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in device_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DeviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInfo = channel.unary_unary(
                '/gsdk.device.Device/GetInfo',
                request_serializer=device__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=device__pb2.GetInfoResponse.FromString,
                _registered_method=True)
        self.GetCapability = channel.unary_unary(
                '/gsdk.device.Device/GetCapability',
                request_serializer=device__pb2.GetCapabilityRequest.SerializeToString,
                response_deserializer=device__pb2.GetCapabilityResponse.FromString,
                _registered_method=True)
        self.GetCapabilityInfo = channel.unary_unary(
                '/gsdk.device.Device/GetCapabilityInfo',
                request_serializer=device__pb2.GetCapabilityInfoRequest.SerializeToString,
                response_deserializer=device__pb2.GetCapabilityInfoResponse.FromString,
                _registered_method=True)
        self.DeleteRootCA = channel.unary_unary(
                '/gsdk.device.Device/DeleteRootCA',
                request_serializer=device__pb2.DeleteRootCARequest.SerializeToString,
                response_deserializer=device__pb2.DeleteRootCAResponse.FromString,
                _registered_method=True)
        self.Lock = channel.unary_unary(
                '/gsdk.device.Device/Lock',
                request_serializer=device__pb2.LockRequest.SerializeToString,
                response_deserializer=device__pb2.LockResponse.FromString,
                _registered_method=True)
        self.LockMulti = channel.unary_unary(
                '/gsdk.device.Device/LockMulti',
                request_serializer=device__pb2.LockMultiRequest.SerializeToString,
                response_deserializer=device__pb2.LockMultiResponse.FromString,
                _registered_method=True)
        self.Unlock = channel.unary_unary(
                '/gsdk.device.Device/Unlock',
                request_serializer=device__pb2.UnlockRequest.SerializeToString,
                response_deserializer=device__pb2.UnlockResponse.FromString,
                _registered_method=True)
        self.UnlockMulti = channel.unary_unary(
                '/gsdk.device.Device/UnlockMulti',
                request_serializer=device__pb2.UnlockMultiRequest.SerializeToString,
                response_deserializer=device__pb2.UnlockMultiResponse.FromString,
                _registered_method=True)
        self.Reboot = channel.unary_unary(
                '/gsdk.device.Device/Reboot',
                request_serializer=device__pb2.RebootRequest.SerializeToString,
                response_deserializer=device__pb2.RebootResponse.FromString,
                _registered_method=True)
        self.RebootMulti = channel.unary_unary(
                '/gsdk.device.Device/RebootMulti',
                request_serializer=device__pb2.RebootMultiRequest.SerializeToString,
                response_deserializer=device__pb2.RebootMultiResponse.FromString,
                _registered_method=True)
        self.FactoryReset = channel.unary_unary(
                '/gsdk.device.Device/FactoryReset',
                request_serializer=device__pb2.FactoryResetRequest.SerializeToString,
                response_deserializer=device__pb2.FactoryResetResponse.FromString,
                _registered_method=True)
        self.FactoryResetMulti = channel.unary_unary(
                '/gsdk.device.Device/FactoryResetMulti',
                request_serializer=device__pb2.FactoryResetMultiRequest.SerializeToString,
                response_deserializer=device__pb2.FactoryResetMultiResponse.FromString,
                _registered_method=True)
        self.ClearDB = channel.unary_unary(
                '/gsdk.device.Device/ClearDB',
                request_serializer=device__pb2.ClearDBRequest.SerializeToString,
                response_deserializer=device__pb2.ClearDBResponse.FromString,
                _registered_method=True)
        self.ClearDBMulti = channel.unary_unary(
                '/gsdk.device.Device/ClearDBMulti',
                request_serializer=device__pb2.ClearDBMultiRequest.SerializeToString,
                response_deserializer=device__pb2.ClearDBMultiResponse.FromString,
                _registered_method=True)
        self.ResetConfig = channel.unary_unary(
                '/gsdk.device.Device/ResetConfig',
                request_serializer=device__pb2.ResetConfigRequest.SerializeToString,
                response_deserializer=device__pb2.ResetConfigResponse.FromString,
                _registered_method=True)
        self.ResetConfigMulti = channel.unary_unary(
                '/gsdk.device.Device/ResetConfigMulti',
                request_serializer=device__pb2.ResetConfigMultiRequest.SerializeToString,
                response_deserializer=device__pb2.ResetConfigMultiResponse.FromString,
                _registered_method=True)
        self.UpgradeFirmware = channel.unary_unary(
                '/gsdk.device.Device/UpgradeFirmware',
                request_serializer=device__pb2.UpgradeFirmwareRequest.SerializeToString,
                response_deserializer=device__pb2.UpgradeFirmwareResponse.FromString,
                _registered_method=True)
        self.UpgradeFirmwareMulti = channel.unary_unary(
                '/gsdk.device.Device/UpgradeFirmwareMulti',
                request_serializer=device__pb2.UpgradeFirmwareMultiRequest.SerializeToString,
                response_deserializer=device__pb2.UpgradeFirmwareMultiResponse.FromString,
                _registered_method=True)
        self.GetHashKey = channel.unary_unary(
                '/gsdk.device.Device/GetHashKey',
                request_serializer=device__pb2.GetHashKeyRequest.SerializeToString,
                response_deserializer=device__pb2.GetHashKeyResponse.FromString,
                _registered_method=True)
        self.SetHashKey = channel.unary_unary(
                '/gsdk.device.Device/SetHashKey',
                request_serializer=device__pb2.SetHashKeyRequest.SerializeToString,
                response_deserializer=device__pb2.SetHashKeyResponse.FromString,
                _registered_method=True)


class DeviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCapability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCapabilityInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRootCA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reboot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RebootMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FactoryReset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FactoryResetMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearDB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearDBMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetConfigMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeFirmware(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeFirmwareMulti(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHashKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetHashKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=device__pb2.GetInfoRequest.FromString,
                    response_serializer=device__pb2.GetInfoResponse.SerializeToString,
            ),
            'GetCapability': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCapability,
                    request_deserializer=device__pb2.GetCapabilityRequest.FromString,
                    response_serializer=device__pb2.GetCapabilityResponse.SerializeToString,
            ),
            'GetCapabilityInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCapabilityInfo,
                    request_deserializer=device__pb2.GetCapabilityInfoRequest.FromString,
                    response_serializer=device__pb2.GetCapabilityInfoResponse.SerializeToString,
            ),
            'DeleteRootCA': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRootCA,
                    request_deserializer=device__pb2.DeleteRootCARequest.FromString,
                    response_serializer=device__pb2.DeleteRootCAResponse.SerializeToString,
            ),
            'Lock': grpc.unary_unary_rpc_method_handler(
                    servicer.Lock,
                    request_deserializer=device__pb2.LockRequest.FromString,
                    response_serializer=device__pb2.LockResponse.SerializeToString,
            ),
            'LockMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.LockMulti,
                    request_deserializer=device__pb2.LockMultiRequest.FromString,
                    response_serializer=device__pb2.LockMultiResponse.SerializeToString,
            ),
            'Unlock': grpc.unary_unary_rpc_method_handler(
                    servicer.Unlock,
                    request_deserializer=device__pb2.UnlockRequest.FromString,
                    response_serializer=device__pb2.UnlockResponse.SerializeToString,
            ),
            'UnlockMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockMulti,
                    request_deserializer=device__pb2.UnlockMultiRequest.FromString,
                    response_serializer=device__pb2.UnlockMultiResponse.SerializeToString,
            ),
            'Reboot': grpc.unary_unary_rpc_method_handler(
                    servicer.Reboot,
                    request_deserializer=device__pb2.RebootRequest.FromString,
                    response_serializer=device__pb2.RebootResponse.SerializeToString,
            ),
            'RebootMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.RebootMulti,
                    request_deserializer=device__pb2.RebootMultiRequest.FromString,
                    response_serializer=device__pb2.RebootMultiResponse.SerializeToString,
            ),
            'FactoryReset': grpc.unary_unary_rpc_method_handler(
                    servicer.FactoryReset,
                    request_deserializer=device__pb2.FactoryResetRequest.FromString,
                    response_serializer=device__pb2.FactoryResetResponse.SerializeToString,
            ),
            'FactoryResetMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.FactoryResetMulti,
                    request_deserializer=device__pb2.FactoryResetMultiRequest.FromString,
                    response_serializer=device__pb2.FactoryResetMultiResponse.SerializeToString,
            ),
            'ClearDB': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearDB,
                    request_deserializer=device__pb2.ClearDBRequest.FromString,
                    response_serializer=device__pb2.ClearDBResponse.SerializeToString,
            ),
            'ClearDBMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearDBMulti,
                    request_deserializer=device__pb2.ClearDBMultiRequest.FromString,
                    response_serializer=device__pb2.ClearDBMultiResponse.SerializeToString,
            ),
            'ResetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetConfig,
                    request_deserializer=device__pb2.ResetConfigRequest.FromString,
                    response_serializer=device__pb2.ResetConfigResponse.SerializeToString,
            ),
            'ResetConfigMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetConfigMulti,
                    request_deserializer=device__pb2.ResetConfigMultiRequest.FromString,
                    response_serializer=device__pb2.ResetConfigMultiResponse.SerializeToString,
            ),
            'UpgradeFirmware': grpc.unary_unary_rpc_method_handler(
                    servicer.UpgradeFirmware,
                    request_deserializer=device__pb2.UpgradeFirmwareRequest.FromString,
                    response_serializer=device__pb2.UpgradeFirmwareResponse.SerializeToString,
            ),
            'UpgradeFirmwareMulti': grpc.unary_unary_rpc_method_handler(
                    servicer.UpgradeFirmwareMulti,
                    request_deserializer=device__pb2.UpgradeFirmwareMultiRequest.FromString,
                    response_serializer=device__pb2.UpgradeFirmwareMultiResponse.SerializeToString,
            ),
            'GetHashKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHashKey,
                    request_deserializer=device__pb2.GetHashKeyRequest.FromString,
                    response_serializer=device__pb2.GetHashKeyResponse.SerializeToString,
            ),
            'SetHashKey': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHashKey,
                    request_deserializer=device__pb2.SetHashKeyRequest.FromString,
                    response_serializer=device__pb2.SetHashKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gsdk.device.Device', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('gsdk.device.Device', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Device(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/GetInfo',
            device__pb2.GetInfoRequest.SerializeToString,
            device__pb2.GetInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCapability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/GetCapability',
            device__pb2.GetCapabilityRequest.SerializeToString,
            device__pb2.GetCapabilityResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCapabilityInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/GetCapabilityInfo',
            device__pb2.GetCapabilityInfoRequest.SerializeToString,
            device__pb2.GetCapabilityInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteRootCA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/DeleteRootCA',
            device__pb2.DeleteRootCARequest.SerializeToString,
            device__pb2.DeleteRootCAResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Lock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/Lock',
            device__pb2.LockRequest.SerializeToString,
            device__pb2.LockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LockMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/LockMulti',
            device__pb2.LockMultiRequest.SerializeToString,
            device__pb2.LockMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Unlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/Unlock',
            device__pb2.UnlockRequest.SerializeToString,
            device__pb2.UnlockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnlockMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/UnlockMulti',
            device__pb2.UnlockMultiRequest.SerializeToString,
            device__pb2.UnlockMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Reboot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/Reboot',
            device__pb2.RebootRequest.SerializeToString,
            device__pb2.RebootResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RebootMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/RebootMulti',
            device__pb2.RebootMultiRequest.SerializeToString,
            device__pb2.RebootMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FactoryReset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/FactoryReset',
            device__pb2.FactoryResetRequest.SerializeToString,
            device__pb2.FactoryResetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FactoryResetMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/FactoryResetMulti',
            device__pb2.FactoryResetMultiRequest.SerializeToString,
            device__pb2.FactoryResetMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClearDB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/ClearDB',
            device__pb2.ClearDBRequest.SerializeToString,
            device__pb2.ClearDBResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClearDBMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/ClearDBMulti',
            device__pb2.ClearDBMultiRequest.SerializeToString,
            device__pb2.ClearDBMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/ResetConfig',
            device__pb2.ResetConfigRequest.SerializeToString,
            device__pb2.ResetConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResetConfigMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/ResetConfigMulti',
            device__pb2.ResetConfigMultiRequest.SerializeToString,
            device__pb2.ResetConfigMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpgradeFirmware(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/UpgradeFirmware',
            device__pb2.UpgradeFirmwareRequest.SerializeToString,
            device__pb2.UpgradeFirmwareResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpgradeFirmwareMulti(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/UpgradeFirmwareMulti',
            device__pb2.UpgradeFirmwareMultiRequest.SerializeToString,
            device__pb2.UpgradeFirmwareMultiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetHashKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/GetHashKey',
            device__pb2.GetHashKeyRequest.SerializeToString,
            device__pb2.GetHashKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetHashKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/gsdk.device.Device/SetHashKey',
            device__pb2.SetHashKeyRequest.SerializeToString,
            device__pb2.SetHashKeyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
