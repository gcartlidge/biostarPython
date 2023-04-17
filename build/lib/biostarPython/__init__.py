__version__ = "0.3.0.1"
__author__ = 'SupremaUK'
__credits__ = 'SupremaInc'

from os.path import dirname
from sys import exc_info
from json import load as jsonload
from biostarPython.service import access_pb2_grpc, action_pb2_grpc, admin_pb2_grpc, apb_zone_pb2_grpc, auth_pb2_grpc, card_pb2_grpc, cert_pb2_grpc, connect_master_pb2_grpc, connect_pb2_grpc, device_pb2_grpc, display_pb2_grpc, door_pb2_grpc, err_pb2_grpc, event_pb2_grpc, face_pb2_grpc, finger_pb2_grpc, fire_zone_pb2_grpc, gateway_pb2_grpc, input_pb2_grpc, interlock_zone_pb2_grpc, intrusion_zone_pb2_grpc, lift_pb2_grpc, lift_zone_pb2_grpc, lock_zone_pb2_grpc, login_pb2_grpc, network_pb2_grpc, operator_pb2_grpc, rs485_pb2_grpc, schedule_pb2_grpc, server_pb2_grpc, status_pb2_grpc, system_pb2_grpc, tenant_pb2_grpc, thermal_pb2_grpc, timed_apb_zone_pb2_grpc, time_pb2_grpc, tna_pb2_grpc, user_pb2_grpc, voip_pb2_grpc, wiegand_pb2_grpc, rtsp_pb2_grpc, voip_pb2_grpc
import grpc
import logging
from logging.handlers import TimedRotatingFileHandler

#setup logging
logger = logging.getLogger(__name__)
handler = TimedRotatingFileHandler(filename='GSDKlog.log', when='D', interval=1, backupCount=45, encoding='utf-8', delay=False)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(lineno)d %(name)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def initDeviceList():
 deviceType = {}
 deviceType[0x01] = 'BioEntry Plus'
 deviceType[0x02] = 'BioEntry W'
 deviceType[0x03] = 'BioLite Net'  
 deviceType[0x04] = 'XPass'  
 deviceType[0x05] = 'XPass S2'   
 deviceType[0x06] = 'SecureIO 2'  
 deviceType[0x07] = 'DM20'  
 deviceType[0x08] = 'BioStation 2'  
 deviceType[0x09] = 'BioStation A2'  
 deviceType[0x0A] = 'Facestation 2'  
 deviceType[0x0B] = 'IO Device'  
 deviceType[0x0C] = 'BioStation L2'  
 deviceType[0x0D] = 'BioEntry W2'  
 deviceType[0x80] = 'RS485 Slave'  
 deviceType[0x0E] = 'CoreStation'  
 deviceType[0x0F] = 'Output Module'  
 deviceType[0x10] = 'Input Module'  
 deviceType[0x11] = 'BioEntry P2'  
 deviceType[0x12] = 'BioLite N2'  
 deviceType[0x13] = 'XPass 2'  
 deviceType[0x14] = 'XPass S3'  
 deviceType[0x15] = 'BioEntry R2'  
 deviceType[0x16] = 'XPass D2'  
 deviceType[0x17] = 'DM21'  
 deviceType[0x18] = 'XPass D2 Keypad'  
 deviceType[0x19] = 'FaceLite'  
 deviceType[0x1A] = 'XPass 2 Keypad'  
 deviceType[0x1D] = 'FaceStation F2 ODP'  
 deviceType[0x1E] = 'FaceStation F2 AB/DB'  
 deviceType[0x1F] = 'XStation 2 QR'  
 deviceType[0x20] = 'XStation 2'
 deviceType[0x21] = 'IM-120' 
 deviceType[0x22] = 'XStation 2 Fingerprint' 
 deviceType[0x23] = 'BioStation 3' 
 return deviceType
deviceType = initDeviceList()  

def initCodeMap(codemapfile):
    try:
      with open(codemapfile) as f:
        return jsonload(f)
    except:
      e = exc_info()[0]
      logger.error(f'Cannot init the event code map: {e}') 

global codeMap    
try:
 codeMap = initCodeMap(f'{dirname(__file__)}//event_code.json')
except:
 logger.error('Included BioStar code map failed to init')
 codeMap = none
 
def getEventString(eventCode, subCode):
    if codeMap == None:
      return "No code map(%#X)" % (eventCode | subCode)
    else:
      for entry in codeMap['entries']:
        if eventCode == entry['event_code'] and subCode == entry['sub_code']:
          return entry['desc']

class GatewayClient:
  channel = None
  def __init__(self, ipAddr, port, caFile):
    try:
      with open(caFile, 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        self.channel = grpc.secure_channel("{}:{}".format(ipAddr, port), creds, options=[
        ('grpc.max_send_message_length', 1000 * 1024 * 1024),
        ('grpc.max_receive_message_length', 1000 * 1024 * 1024)
        ])
    except grpc.RpcError as e:
      logger.error(f'Cannot create the gateway client: {e}')
      raise
  def getChannel(self):
    return self.channel
class ConnectSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = connect_pb2_grpc.ConnectStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the connect stub: {e}')
      raise
  def getConnInfo(self, ipAddr, port, useSSL):
   try:
    info = connect_pb2_grpc.connect__pb2.ConnectInfo(IPAddr=ipAddr, port=port, useSSL=useSSL)
    return info
   except:
    logger.error('Cannot get connection Info')
    raise
  def getAsyncConnInfo(self, deviceID, ipAddr, port, useSSL):
   try:
    info = connect_pb2_grpc.connect__pb2.AsyncConnectInfo(deviceID=deviceID, IPAddr=ipAddr, port=port, useSSL=useSSL)
    return info
   except:
    logger.error('Cannot get Async connection Info')
    raise
  def getConnectedInfo(self, devID):
     for x in self.getDeviceList():
      if x.deviceID == devID:
       return x
      else:
       logger.error('DeviceID given not in Connected list')
  def searchInfoToConnectInfo(self, searchInfo, isAsync):
   try:
    if isAsync == True:
     info = self.getAsyncConnInfo(searchInfo.deviceID,searchInfo.IPAddr,searchInfo.port,searchInfo.useSSL)
     return info
    elif isAsync == False: 
     info = self.getConnInfo(searchInfo.IPAddr,searchInfo.port,searchInfo.useSSL)
     return info
    else:
     raise ValueError('isAsync is meant to be Boolean, Try again')    
   except Exception as e:
    logger.error(f'Failed to get ConnectInfo from SearchInfo: {e}')
    raise
  def connectInfoToAsyncInfo(self, devID):
   try:
    for x in self.getDeviceList():
      if x.deviceID == devID:
       return self.getAsyncConnInfo(x.deviceID,x.IPAddr,x.port,x.useSSL)
      else:
       logger.error('DeviceID given not in list')
   except Exception as e:
      logger.error(f'Cannot get Aysnc info for connected device: {e}')
      raise
  def searchDevice(self, timeout):
    try:
      response = self.stub.SearchDevice(connect_pb2_grpc.connect__pb2.SearchDeviceRequest(timeout=timeout))
      return response.deviceInfos
    except grpc.RpcError as e:
      logger.error(f'Cannot get search device: {e}')
      raise
  def getDeviceList(self):
    try:
      response = self.stub.GetDeviceList(connect_pb2_grpc.connect__pb2.GetDeviceListRequest())
      return response.deviceInfos
    except grpc.RpcError as e:
      logger.error(f'Cannot get the device list: {e}')
      raise
  def connect(self, connInfo):
    try:
      response = self.stub.Connect(connect_pb2_grpc.connect__pb2.ConnectRequest(connectInfo=connInfo))
      return response.deviceID
    except grpc.RpcError as e:
      logger.error(f'Cannot connect to the device: {e}')
      raise
  def disconnect(self, deviceIDs):
    try:
      self.stub.Disconnect(connect_pb2_grpc.connect__pb2.DisconnectRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot disconnect devices: {e}')
      raise
  def disconnectAll(self):
    try:
      self.stub.DisconnectAll(connect_pb2_grpc.connect__pb2.DisconnectAllRequest())
    except grpc.RpcError as e:
      logger.error(f'Cannot disconnect all devices: {e}')
      raise
  def addAsyncConnection(self, connInfos):
    try:
      self.stub.AddAsyncConnection(connect_pb2_grpc.connect__pb2.AddAsyncConnectionRequest(connectInfos=connInfos))
    except grpc.RpcError as e:
      logger.error(f'Cannot add async connections: {e}')
      raise
  def deleteAsyncConnection(self, deviceIDs):
    try:
      self.stub.DeleteAsyncConnection(connect_pb2_grpc.connect__pb2.DeleteAsyncConnectionRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete async connections: {e}')
      raise    
  def getPendingList(self):
    try:
      response = self.stub.GetPendingList(connect_pb2_grpc.connect__pb2.GetPendingListRequest())
      return response.deviceInfos
    except grpc.RpcError as e:
      logger.error(f'Cannot get the pending list: {e}')
      raise    
  def getAcceptFilter(self):
    try:
      response = self.stub.GetAcceptFilter(connect_pb2_grpc.connect__pb2.GetAcceptFilterRequest())
      return response.filter
    except grpc.RpcError as e:
      logger.error(f'Cannot get the accept filter: {e}')
      raise      
  def setAcceptFilter(self, filter):
    try:
      self.stub.SetAcceptFilter(connect_pb2_grpc.connect__pb2.SetAcceptFilterRequest(filter=filter))      
    except grpc.RpcError as e:
      logger.error(f'Cannot set the accept filter: {e}')
      raise 
  def setConnectionMode(self, deviceIDs, mode):
    try:
      self.stub.SetConnectionModeMulti(connect_pb2_grpc.connect__pb2.SetConnectionModeMultiRequest(deviceIDs=deviceIDs, connectionMode=mode))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the connection mode: {e}')
      raise 
  def enableSSL(self, deviceIDs):
    try:
      self.stub.EnableSSLMulti(connect_pb2_grpc.connect__pb2.EnableSSLMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot enable SSL: {e}')
      raise 
  def disableSSL(self, deviceIDs):
    try:
      self.stub.DisableSSLMulti(connect_pb2_grpc.connect__pb2.DisableSSLMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot disable SSL: {e}')
      raise 
  def subscribe(self, queueSize):
    try:
      return self.stub.SubscribeStatus(connect_pb2_grpc.connect__pb2.SubscribeStatusRequest(queueSize=queueSize))
    except grpc.RpcError as e:
      logger.error(f'Cannot subscribe: {e}')
      raise   
  def getSlaveDevice(self):
    try:
      return self.stub.GetSlaveDevice(connect_pb2_grpc.connect__pb2.GetSlaveDeviceRequest())
    except grpc.RpcError as e:
      logger.error(f'Cannot get Slave Device: {e}')
      raise
  def setSlaveDevice(self, slaveDeviceInfos):
    try:
      return self.stub.SetSlaveDevice(connect_pb2_grpc.connect__pb2.SetSlaveDeviceRequest(slaveDeviceInfos=slaveDeviceInfos))
    except grpc.RpcError as e:
      logger.error(f'Cannot set Slave Device: {e}')
      raise        
class DeviceSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = device_pb2_grpc.DeviceStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the device stub: {e}')
      raise
  def getInfo(self, deviceID):
    try:
      response = self.stub.GetInfo(device_pb2_grpc.device__pb2.GetInfoRequest(deviceID=deviceID))
      return response.info
    except grpc.RpcError as e:
      logger.error(f'Cannot get the device info: {e}')
      raise
  def getCap(self, deviceID):
    try:
      response = self.stub.GetCapability(device_pb2_grpc.device__pb2.GetCapabilityRequest(deviceID=deviceID))
      return response.deviceCapability
    except grpc.RpcError as e:
      logger.error(f'Cannot get the capability: {e}')
      raise
  def getCapInfo(self, deviceID):
    try:
      response = self.stub.GetCapabilityInfo(device_pb2_grpc.device__pb2.GetCapabilityInfoRequest(deviceID=deviceID))
      return response.capInfo
    except grpc.RpcError as e:
      logger.error(f'Cannot get the capability info: {e}')
      raise
  def deleteRootCA(self, deviceID):
    try:
      response = self.stub.DeleteRootCA(device_pb2_grpc.device__pb2.DeleteRootCARequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete Root CA: {e}')
      raise
  def reboot(self, deviceID):
    try:
      response = self.stub.Reboot(device_pb2_grpc.device__pb2.RebootRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot reboot: {e}')
      raise
  def rebootMulti(self, deviceIDs):
    try:
      response = self.stub.RebootMulti(device_pb2_grpc.device__pb2.RebootMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot reboot Multiple Devices: {e}')
      raise
  def lock(self, deviceID):
    try:
      response = self.stub.Lock(device_pb2_grpc.device__pb2.LockRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Lock Device: {e}')
      raise
  def lockMulti(self, deviceIDs):
    try:
      response = self.stub.LockMulti(device_pb2_grpc.device__pb2.LockMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot Lock Devices: {e}')
      raise
  def unlock(self, deviceID):
    try:
      response = self.stub.Unlock(device_pb2_grpc.device__pb2.UnlockRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Unlock Device: {e}')
      raise
  def unlockMulti(self, deviceIDs):
    try:
      response = self.stub.UnlockMulti(device_pb2_grpc.device__pb2.UnlockRequestMulti(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot Unlock Devices: {e}')
      raise
  def factoryReset(self, deviceID):
    try:
      response = self.stub.FactoryReset(device_pb2_grpc.device__pb2.FactoryResetRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot Factory Reset Device: {e}')
      raise
  def factoryResetMulti(self, deviceIDs):
    try:
      response = self.stub.FactoryResetMulti(device_pb2_grpc.device__pb2.FactoryResetMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot Factory Reset Device: {e}')
      raise
  def resetConfig(self, deviceID, withNetwork, withDB):
    try:
      response = self.stub.ResetConfig(device_pb2_grpc.device__pb2.ResetConfigRequest(deviceID=deviceID, withNetwork=withNetwork, withDB=withDB))
    except grpc.RpcError as e:
      logger.error(f'Cannot Reset Device Config: {e}')
      raise
  def resetConfigMulti(self, deviceID, withNetwork, withDB):
    try:
      response = self.stub.ResetConfigMulti(device_pb2_grpc.device__pb2.ResetConfigMultiRequest(deviceIDs=deviceIDs, withNetwork=withNetwork, withDB=withDB))
    except grpc.RpcError as e:
      logger.error(f'Cannot Reset Device Config: {e}')
      raise
  def clearDB(self, deviceID):
    try:
      response = self.stub.ClearDB(device_pb2_grpc.device__pb2.ClearDBRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Clear DB: {e}')
      raise
  def clearDBMulti(self, deviceID):
    try:
      response = self.stub.ClearDBMulti(device_pb2_grpc.device__pb2.ClearDBMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot Clear DBs: {e}')
      raise
  def firmwareUpdate(self, deviceID, firmwareData):
    try:
      response = self.stub.UpgradeFirmware(device_pb2_grpc.device__pb2.UpgradeFirmwareRequest(deviceID=deviceID, firmwareData = firmwareData))
    except grpc.RpcError as e:
      logger.error(f'Cannot Upgrade Device: {e}')
      raise
  def firmwareUpdateMulti(self, deviceIDs, firmwareData):
    try:
      response = self.stub.UpgradeFirmwareMulti(device_pb2_grpc.device__pb2.UpgradeFirmwareMultiRequest(deviceIDs=deviceIDs, firmwareData = firmwareData))
    except grpc.RpcError as e:
      logger.error(f'Cannot Upgrade Multiple Devices: {e}')
      raise
  def getHashKey(self, deviceID):
    try:
      response = self.stub.GetHashKey(device_pb2_grpc.device__pb2.GetHashKeyRequest(deviceID=deviceID))
      return response
    except grpc.RpcError as e:
      logger.error(f'Cannot Get Hash Key: {e}')
      raise
  def setHashKey(self, deviceID, setDefault, hashKey):
    try:
      response = self.stub.SetHashKey(device_pb2_grpc.device__pb2.SetHashKeyRequest(deviceID=deviceID, setDefault=setDefault, hashKey=hashKey))
    except grpc.RpcError as e:
      logger.error(f'Cannot Set Hash Key: {e}')
      raise
class FaceSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = face_pb2_grpc.FaceStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the face stub: {e}')
      raise
  def scan(self, deviceID, enrollThreshold):
    try:
      response = self.stub.Scan(face_pb2_grpc.face__pb2.ScanRequest(deviceID=deviceID, enrollThreshold=enrollThreshold))
      return response.faceData
    except grpc.RpcError as e:
      logger.error(f'Cannot scan a face: {e}')
      raise
  def extract(self, deviceID, imageData, isWarped):
    try:
      response = self.stub.Extract(face_pb2_grpc.face__pb2.ExtractRequest(deviceID=deviceID, imageData=imageData, isWarped=isWarped))
      return response.templateData
    except grpc.RpcError as e:
      logger.error(f'Cannot scan a face: {e}')
      raise  
  def normalize(self, deviceID, unwrappedImageData):
    try:
      response = self.stub.Normalize(face_pb2_grpc.face__pb2.NormalizeRequest(deviceID=deviceID, unwrappedImageData=unwrappedImageData))
      return response.wrappedImageData
    except grpc.RpcError as e:
      logger.error(f'Cannot normalize Image: {e}')
      raise      
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(face_pb2_grpc.face__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the face config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      response = self.stub.SetConfig(face_pb2_grpc.face__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the face config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      response = self.stub.SetConfigMulti(face_pb2_grpc.face__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the face configs: {e}')
      raise
class FingerSvc:
   stub = None
   def __init__(self, channel):
    try:
      self.stub = finger_pb2_grpc.FingerStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the finger stub: {e}')
      raise
   def scan(self, deviceID, templateFormat, qualityThreshold):
    try:
      response = self.stub.Scan(finger_pb2_grpc.finger__pb2.ScanRequest(deviceID=deviceID, templateFormat=templateFormat, qualityThreshold=qualityThreshold))
      return response
    except grpc.RpcError as e:
      logger.error(f'Cannot scan a finger: {e}')
      raise
   def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(finger_pb2_grpc.finger__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get Finger Config: {e}')
      raise
   def setConfig(self, deviceID, config):
    try:
      response = self.stub.SetConfig(finger_pb2_grpc.finger__pb2.SetConfigRequest(deviceID=deviceID, config=config))
      return response
    except grpc.RpcError as e:
      logger.error(f'Cannot Set Finger Config: {e}')
      raise
   def setConfigMulti(self, deviceIDs,config):
    try:
      response = self.stub.SetConfigMulti(finger_pb2_grpc.finger__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs))
      return response
    except grpc.RpcError as e:
      logger.error(f'Cannot set Finger Multi Config: {e}')
      raise
   def getImage(self, deviceID):
    try:
      response = self.stub.GetImage(finger_pb2_grpc.finger__pb2.GetImageRequest(deviceID=deviceID))
      return response.BMPImage
    except grpc.RpcError as e:
      logger.error(f'Cannot get finger image: {e}')
      raise
class StatusSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = status_pb2_grpc.StatusStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the status stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(status_pb2_grpc.status__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the status config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(status_pb2_grpc.status__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the status config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(status_pb2_grpc.status__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the status config: {e}')
      raise
class UserSvc:
  # allow calling UserSvc.newUser() to make a new user easily, using UserInfo from user_pb2 that is imported into user_pb2_grpc
  newUser = user_pb2_grpc.user__pb2.UserInfo
  newUserCard = user_pb2_grpc.user__pb2.UserCard
  newUserFinger = user_pb2_grpc.user__pb2.UserFinger
  newUserFace = user_pb2_grpc.user__pb2.UserFace
  newUserJobCode = user_pb2_grpc.user__pb2.UserJobCode
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = user_pb2_grpc.UserStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the user stub: {e}')
      raise
  def getList(self, deviceID):
    try:
      response = self.stub.GetList(user_pb2_grpc.user__pb2.GetListRequest(deviceID=deviceID))
      return response.hdrs
    except grpc.RpcError as e:
      logger.error(f'Cannot get the user list: {e}')
      raise
  def getUser(self, deviceID, userIDs):
    try:
      response = self.stub.Get(user_pb2_grpc.user__pb2.GetRequest(deviceID=deviceID, userIDs=userIDs))
      return response.users    
    except grpc.RpcError as e:
      logger.error(f'Cannot get the users: {e}')
      raise
  def getPartial(self, deviceID, infoMask):
    try:
      response = self.stub.GetPartial(user_pb2_grpc.user__pb2.GetPartialRequest(deviceID=deviceID, userIDs=userIDs, infoMask = infoMask))
      return response.users
    except grpc.RpcError as e:
      logger.error(f'Cannot get the partial user list: {e}')
      raise
  def enroll(self, deviceID, users, overwrite):
    try:
      self.stub.Enroll(user_pb2_grpc.user__pb2.EnrollRequest(deviceID=deviceID, users=users, overwrite=overwrite))
    except grpc.RpcError as e:
      logger.error(f'Cannot enroll users: {e}')
      raise
  def enrollMulti(self, deviceIDs, users, overwrite):
    try:
      self.stub.EnrollMulti(user_pb2_grpc.user__pb2.EnrollMultiRequest(deviceIDs=deviceIDs, users=users, overwrite=overwrite))
    except grpc.RpcError as e:
      logger.error(f'Cannot enroll users multi: {e}')
      raise
  def delete(self, deviceID, userIDs):
    try:
      self.stub.Delete(user_pb2_grpc.user__pb2.DeleteRequest(deviceID=deviceID, userIDs=userIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete users: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(user_pb2_grpc.user__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all users: {e}')
      raise
  def deleteMulti(self, deviceIDs, userIDs):
    try:
      self.stub.DeleteMulti(user_pb2_grpc.user__pb2.DeleteMultiRequest(deviceIDs=deviceIDs, userIDs=userIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete users multi: {e}')
      raise
  def deleteAllMulti(self, deviceIDs, userIDs):
    try:
      self.stub.DeleteAllMulti(user_pb2_grpc.user__pb2.DeleteAllMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all users multi: {e}')
      raise
  def getFinger(self, deviceID, userIDs):
    try:
      self.stub.GetFinger(user_pb2_grpc.user__pb2.GetFingerRequest(deviceID=deviceID, userIDs=userIDs))
      return response.userFingers
    except grpc.RpcError as e:
      logger.error(f'Cannot get user fingers: {e}')
      raise
  def setFinger(self, deviceID, userFingers):
    try:
      self.stub.SetFinger(user_pb2_grpc.user__pb2.SetFingerRequest(deviceID=deviceID, userFingers=userFingers))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user fingers: {e}')
      raise
  def setFingerMulti(self, deviceIDs, userFingers):
    try:
      self.stub.SetFingerMulti(user_pb2_grpc.user__pb2.SetFingerMultiRequest(deviceIDs=deviceIDs, userFingers=userFingers))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user fingers multi: {e}')
      raise
  def getCard(self, deviceID, userIDs):
    try:
      self.stub.GetCard(user_pb2_grpc.user__pb2.GetCardRequest(deviceID=deviceID, userIDs=userIDs))
      return response.userCards
    except grpc.RpcError as e:
      logger.error(f'Cannot get user cards: {e}')
      raise
  def setCard(self, deviceID, userCards):
    try:
      self.stub.SetCard(user_pb2_grpc.user__pb2.SetCardRequest(deviceID=deviceID, userCards=userCards))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user cards: {e}')
      raise 
  def setCardMulti(self, deviceIDs, userCards):
    try:
      self.stub.SetCardMulti(user_pb2_grpc.user__pb2.SetCardMultiRequest(deviceIDs=deviceIDs, userCards=userCards))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user cards multi: {e}')
      raise   
  def getFace(self, deviceID, userIDs):
    try:
      self.stub.GetFace(user_pb2_grpc.user__pb2.GetFaceRequest(deviceID=deviceID, userIDs=userIDs))
      return response.userFaces
    except grpc.RpcError as e:
      logger.error(f'Cannot get user faces: {e}')
      raise      
  def setFace(self, deviceID, userFaces):
    try:
      self.stub.SetFace(user_pb2_grpc.user__pb2.SetFaceRequest(deviceID=deviceID, userFaces=userFaces))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user faces: {e}')
      raise
  def setFaceMulti(self, deviceIDs, userFaces):
    try:
      self.stub.SetFaceMulti(user_pb2_grpc.user__pb2.SetFaceMultiRequest(deviceIDs=deviceIDs, userFaces=userFaces))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user faces: {e}')
      raise       
  def setAccessGroup(self, deviceID, userAccessGroups):
    try:
      self.stub.SetAccessGroup(user_pb2_grpc.user__pb2.SetAccessGroupRequest(deviceID=deviceID, userAccessGroups=userAccessGroups))
    except grpc.RpcError as e:
      logger.error(f'Cannot set user access groups: {e}')
      raise 
  def getAccessGroup(self, deviceID, userIDs):
    try:
      response = self.stub.GetAccessGroup(user_pb2_grpc.user__pb2.GetAccessGroupRequest(deviceID=deviceID, userIDs=userIDs))
      return response.userAccessGroups
    except grpc.RpcError as e:
      logger.error(f'Cannot get user access groups: {e}')
      raise 
  def getPINHash(self, PIN):
    try:
      response = self.stub.GetPINHash(user_pb2_grpc.user__pb2.GetPINHashRequest(PIN=PIN))
      return response.hashVal
    except grpc.RpcError as e:
      logger.error(f'Cannot get PIN Hash: {e}')
      raise 
  def setAccessGroupMulti(self, deviceIDs, userAccessGroups):
    try:
      self.stub.SetAccessGroupMulti(user_pb2_grpc.user__pb2.SetAccessGroupMultiRequest(deviceIDs=deviceIDs, userAccessGroups=userAccessGroups))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple user access groups: {e}')
      raise 
  def setJobCode(self, deviceID, userJobCodes):
    try:
      self.stub.SetJobCode(user_pb2_grpc.user__pb2.SetJobCodeRequest(deviceID=deviceID, userJobCodes=userJobCodes))
    except grpc.RpcError as e:
      logger.error(f'Cannot set Job Codes: {e}')
      raise 
  def getJobCode(self, deviceID, userIDs):
    try:
      response = self.stub.GetJobCode(user_pb2_grpc.user__pb2.GetJobCodeRequest(deviceID=deviceID, userIDs=userIDs))
      return response.userJobCodes
    except grpc.RpcError as e:
      logger.error(f'Cannot get Job Codes: {e}')
      raise 
  def setJobCodeMulti(self, deviceIDs, userAccessGroups):
    try:
      self.stub.SetJobCodeMulti(user_pb2_grpc.user__pb2.SetJobCodeMultiRequest(deviceIDs=deviceIDs, userJobCodes=userJobCodes))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple Job Codes: {e}')
      raise   
class DisplaySvc:
  stub = None
  
  def __init__(self, channel): 
    try:
      self.stub = display_pb2_grpc.DisplayStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Display stub: {e}')
      raise
  def updateLanguagePack(self, deviceID, data):
    try:
      self.stub.UpdateLanguagePack(display_pb2_grpc.display__pb2.UpdateLanguagePackRequest(deviceID=deviceID, data=data))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Language Pack: {e}')
      raise
  def updateLanguagePackMulti(self, deviceIDs, data):
    try:
      self.stub.UpdateLanguagePackMulti(display_pb2_grpc.display__pb2.UpdateLanguagePackMultiRequest(deviceIDs=deviceIDs, data=data))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Multiple Language Packs: {e}')
      raise
  def updateNotice(self, deviceID, notice):
    try:
      self.stub.UpdateNotice(display_pb2_grpc.display__pb2.UpdateNoticeRequest(deviceID=deviceID, notice=notice))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Notice: {e}')
      raise
  def updateSound(self, deviceID, index, waveData):
    try:
      self.stub.UpdateSound(display_pb2_grpc.display__pb2.UpdateSoundRequest(deviceID=deviceID, index=index, waveData=waveData))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Sound: {e}')
      raise
  def updateSoundMulti(self, deviceIDs, index, waveData):
    try:
      self.stub.UpdateSoundMulti(display_pb2_grpc.display__pb2.UpdateSoundMultiRequest(deviceIDs=deviceIDs, index=index, waveData=waveData))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Sounds: {e}')
      raise
  def updateNoticeMulti(self, deviceID, notice):
    try:
      self.stub.UpdateNoticeMulti(display_pb2_grpc.display__pb2.UpdateNoticeMultiRequest(deviceIDs=deviceIDs, notice=notice))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Multiple Notices: {e}')
      raise
  def updateBackgroundImage(self, deviceID, PNGImage):
    try:
      self.stub.UpdateBackgroundImage(display_pb2_grpc.display__pb2.UpdateBackgroundImageRequest(deviceID=deviceID, PNGImage=PNGImage))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Background Image: {e}')
      raise
  def updateBackgroundImageMulti(self, deviceIDs, PNGImage):
    try:
      self.stub.UpdateBackgroundImageMulti(display_pb2_grpc.display__pb2.UpdateBackgroundImageMultiRequest(deviceIDs=deviceIDs, PNGImage=PNGImage))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Multiple Background Images: {e}')
      raise   
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(display_pb2_grpc.display__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot Get Config: {e}')
      raise   
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(display_pb2_grpc.display__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot Set Config: {e}')
      raise         
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(display_pb2_grpc.display__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot Update Multiple Config: {e}')
      raise new
class AdminSvc:
   stub = None
   def __init__(self, channel):
    try:
      self.stub = admin_pb2_grpc.AdminStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the admin stub: {e}')
      raise
   def getInfo(self):
    try:
      response = self.stub.GetInfo(admin_pb2_grpc.admin__pb2.GetInfoRequest())
      return response
    except grpc.RpcError as e:
      logger.error(f'Cannot Get GSDK Server Info: {e}')
      raise
class WiegandSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = wiegand_pb2_grpc.WiegandStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the wiegand stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(wiegand_pb2_grpc.wiegand__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the wiegand config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(wiegand_pb2_grpc.wiegand__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the wiegand config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(wiegand_pb2_grpc.wiegand__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the wiegand Multi config: {e}')
      raise
class TimeSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = time_pb2_grpc.TimeStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the time stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(time_pb2_grpc.time__pb2.GetRequest(deviceID=deviceID))
      return response.GMTTime
    except grpc.RpcError as e:
      logger.error(f'Cannot get the time: {e}')
      raise
  def set(self, deviceID, GMTTime):
    try:
      self.stub.Set(time_pb2_grpc.time__pb2.SetRequest(deviceID=deviceID, GMTTime=GMTTime))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the time: {e}')
      raise
  def setMulti(self, deviceIDs, GMTTime):
    try:
      self.stub.SetMulti(time_pb2_grpc.time__pb2.SetMultiRequest(deviceIDs=deviceIDs, GMTTime=GMTTime))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple times: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(time_pb2_grpc.time__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the time config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(time_pb2_grpc.time__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the time config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(time_pb2_grpc.time__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple time config: {e}')
      raise
  def getDSTConfig(self, deviceID):
    try:
      response = self.stub.GetDSTConfig(time_pb2_grpc.time__pb2.GetDSTConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the DST config: {e}')
      raise
  def setDSTConfig(self, deviceID, config):
    try:
      self.stub.SetDSTConfig(time_pb2_grpc.time__pb2.SetDSTConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the DST: {e}')
      raise
  def setDSTConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetDSTConfigMulti(time_pb2_grpc.time__pb2.SetDSTMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple DST: {e}')
      raise
class CardSvc:
  stub = None
  newCard = card_pb2_grpc.card__pb2.CardData
  newSmartCard = card_pb2_grpc.card__pb2.SmartCardData
  newAccessOnCard = card_pb2_grpc.card__pb2.AccessOnCardData
  newSmartCardHeader = card_pb2_grpc.card__pb2.SmartCardHeader
  def __init__(self, channel): 
    try:
      self.stub = card_pb2_grpc.CardStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the card stub: {e}')
      raise
  def scan(self, deviceID):
    try:
      response = self.stub.Scan(card_pb2_grpc.card__pb2.ScanRequest(deviceID=deviceID))
      return response.cardData
    except grpc.RpcError as e:
      logger.error(f'Cannot scan a card: {e}')
      raise
  def erase(self, deviceID):
    try:
      self.stub.Erase(card_pb2_grpc.card__pb2.EraseRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot erase a card: {e}')
      raise
  def write(self, deviceID, smartCardData):
    try:
      self.stub.Write(card_pb2_grpc.card__pb2.WriteRequest(deviceID=deviceID, smartCardData=smartCardData))
    except grpc.RpcError as e:
      logger.error(f'Cannot Write a card: {e}')
      raise
  def writeQRCode(self, QRText):
    try:
      response = self.stub.WriteQRCode(card_pb2_grpc.card__pb2.WriteQRCodeRequest(QRText=QRText))
      return response.cardData
    except grpc.RpcError as e:
      logger.error(f'Cannot Write a QR: {e}')
      raise
  def getBlacklist(self, deviceID):
    try:
      response = self.stub.GetBlacklist(card_pb2_grpc.card__pb2.GetBlacklistRequest(deviceID=deviceID))
      return response.blacklist
    except grpc.RpcError as e:
      logger.error(f'Cannot get the blacklist: {e}')
      raise
  def addBlacklist(self, deviceID, cardInfos):
    try:
      self.stub.AddBlacklist(card_pb2_grpc.card__pb2.AddBlacklistRequest(deviceID=deviceID, cardInfos=cardInfos))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the cards to the blacklist: {e}')
      raise
  def deleteBlacklist(self, deviceID, cardInfos):
    try:
      self.stub.DeleteBlacklist(card_pb2_grpc.card__pb2.DeleteBlacklistRequest(deviceID=deviceID, cardInfos=cardInfos))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the cards from the blacklist: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(card_pb2_grpc.card__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(card_pb2_grpc.card__pb2.SetConfigRequest(deviceID=deviceID,config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(card_pb2_grpc.card__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs,config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple config: {e}')
      raise
  def getQRConfig(self, deviceID):
    try:
      response = self.stub.GetQRConfig(card_pb2_grpc.card__pb2.GetQRConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the QRconfig: {e}')
      raise
  def setQRConfig(self, deviceID, config):
    try:
      self.stub.SetQRConfig(card_pb2_grpc.card__pb2.SetQRConfigRequest(deviceID=deviceID,config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the QRconfig: {e}')
      raise
  def setQRConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetQRConfigMulti(card_pb2_grpc.card__pb2.SetQRConfigMultiRequest(deviceIDs=deviceIDs,config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple QRconfig: {e}')
      raise
class EventSvc:
  stub = None

  def __init__(self, channel): 
    try:
      self.stub = event_pb2_grpc.EventStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the event stub: {e}')
      raise
  def getLog(self, deviceID, startEventID, maxNumOfLog):
    try:
      response = self.stub.GetLog(event_pb2_grpc.event__pb2.GetLogRequest(deviceID=deviceID, startEventID=startEventID, maxNumOfLog=maxNumOfLog))
      return response.events
    except grpc.RpcError as e:
      logger.error(f'Cannot get the event log: {e}')
      raise

  def getLogWithFilter(self, deviceID, startEventID, maxNumOfLog, filter):
    try:
      response = self.stub.GetLogWithFilter(event_pb2_grpc.event__pb2.GetLogWithFilterRequest(deviceID=deviceID, startEventID=startEventID, maxNumOfLog=maxNumOfLog, filters=[filter]))
      return response.events
    except grpc.RpcError as e:
      logger.error(f'Cannot get the event log: {e}')
      raise


  def getImageLog(self, deviceID, startEventID, maxNumOfLog):
    try:
      response = self.stub.GetImageLog(event_pb2_grpc.event__pb2.GetImageLogRequest(deviceID=deviceID, startEventID=startEventID, maxNumOfLog=maxNumOfLog))
      return response.imageEvents
    except grpc.RpcError as e:
      logger.error(f'Cannot get the image events: {e}')
      raise    

  def clearLog(self, deviceID):
    try:
      response = self.stub.ClearLog(event_pb2_grpc.event__pb2.ClearLogRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear logs: {e}')
      raise
      
  def clearLogMulti(self, deviceIDs):
    try:
      response = self.stub.ClearLogMulti(event_pb2_grpc.event__pb2.ClearLogMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear logs: {e}')
      raise

  def enableMonitoring(self, deviceID):
    try:
      self.stub.EnableMonitoring(event_pb2_grpc.event__pb2.EnableMonitoringRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot enable monitoring: {e}')
      raise

  def disableMonitoring(self, deviceID):
    try:
      self.stub.DisableMonitoring(event_pb2_grpc.event__pb2.DisableMonitoringRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot disable monitoring: {e}')
      raise

  def subscribe(self, queueSize): 
    try:
      return self.stub.SubscribeRealtimeLog(event_pb2_grpc.event__pb2.SubscribeRealtimeLogRequest(queueSize=queueSize))
    except grpc.RpcError as e:
      logger.error(f'Cannot subscribe: {e}')
      raise
class NetworkSvc:
   stub = None
   def __init__(self, channel):
    try:
      self.stub = network_pb2_grpc.NetworkStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the network stub: {e}')
      raise
   def getIPConfig(self,deviceID):
    try:
      response = self.stub.GetIPConfig(network_pb2_grpc.network__pb2.GetIPConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot Get IP Config: {e}')
      raise
   def setIPConfig(self, deviceID, config):
    try:
      self.stub.SetIPConfig(network_pb2_grpc.network__pb2.SetIPConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the IP config: {e}')
      raise
   def setIPConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetIPConfigMulti(network_pb2_grpc.network__pb2.SetIPConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the IP Multi config: {e}')
      raise
   def getWLANConfig(self, deviceID):
    try:
      response = self.stub.GetWLANConfig(network_pb2_grpc.network__pb2.GetWLANConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot Get WLAN Config: {e}')
      raise
   def setWLANConfig(self, deviceID, config):
    try:
      self.stub.SetWLANConfig(network_pb2_grpc.network__pb2.SetWLANConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the WLAN config: {e}')
      raise
   def setWLANConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetWLANConfigMulti(network_pb2_grpc.network__pb2.SetWLANConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the WLAN Multi config: {e}')
      raise
class ServerSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = server_pb2_grpc.ServerStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the server stub: {e}')
      raise
  def subscribe(self, queueSize): 
    try:
      return self.stub.Subscribe(server_pb2_grpc.server__pb2.SubscribeRequest(queueSize=queueSize))
    except grpc.RpcError as e:
      logger.error(f'Cannot subscribe: {e}')
      raise
  def unsubscribe(self): 
    try:
      self.stub.Unsubscribe(server_pb2_grpc.server__pb2.UnsubscribeRequest())
    except grpc.RpcError as e:
      logger.error(f'Cannot unsubscribe: {e}')
      raise
  def handleVerify(self, serverReq, errCode, userInfo):
    try:
      self.stub.HandleVerify(server_pb2_grpc.server__pb2.HandleVerifyRequest(deviceID=serverReq.deviceID, seqNO=serverReq.seqNO, errCode=errCode, user=userInfo))
    except grpc.RpcError as e:
      logger.error(f'Cannot handle verify: {e}')
      raise
  def handleIdentify(self, serverReq, errCode, userInfo):
    try:
      self.stub.HandleIdentify(server_pb2_grpc.server__pb2.HandleIdentifyRequest(deviceID=serverReq.deviceID, seqNO=serverReq.seqNO, errCode=errCode, user=userInfo))
    except grpc.RpcError as e:
      logger.error(f'Cannot handle identify: {e}')
      raise
  def handleUserPhrase(self, serverReq, errCode, userPhrase):
    try:
      self.stub.HandleUserPhrase(server_pb2_grpc.server__pb2.HandleUserPhraseRequest(deviceID=serverReq.deviceID, seqNO=serverReq.seqNO, errCode=errCode, userPhrase=userPhrase))
    except grpc.RpcError as e:
      logger.error(f'Cannot handle userPhrase: {e}')
      raise      
class SystemSvc:
  stub = None
  def __init__(self, channel):
    try:
      self.stub = system_pb2_grpc.SystemStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the system stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(system_pb2_grpc.system__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the System config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(system_pb2_grpc.system__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the System config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(system_pb2_grpc.system__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set multiple System config: {e}')
      raise
class DoorSvc:
  stub = None
  newDoor = door_pb2_grpc.door__pb2.DoorInfo
  def __init__(self, channel): 
    try:
      self.stub = door_pb2_grpc.DoorStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the door stub: {e}')
      raise
  def getList(self, deviceID):
    try:
      response = self.stub.GetList(door_pb2_grpc.door__pb2.GetListRequest(deviceID=deviceID))
      return response.doors
    except grpc.RpcError as e:
      logger.error(f'Cannot get the door list: {e}')
      raise
  def getStatus(self, deviceID):
    try:
      response = self.stub.GetStatus(door_pb2_grpc.door__pb2.GetStatusRequest(deviceID=deviceID))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the door status: {e}')
      raise
  def add(self, deviceID, doors):
    try:
      self.stub.Add(door_pb2_grpc.door__pb2.AddRequest(deviceID=deviceID, doors=doors))
    except grpc.RpcError as e:
      logger.error(f'Cannot add doors: {e}')
      raise
  def delete(self, deviceID, doorIDs):
    try:
      self.stub.Delete(door_pb2_grpc.door__pb2.DeleteRequest(deviceID=deviceID, doorIDs=doorIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the door: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(door_pb2_grpc.door__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the doors: {e}')
      raise
  def lock(self, deviceID, doorIDs, doorFlag):
    try:
      self.stub.Lock(door_pb2_grpc.door__pb2.LockRequest(deviceID=deviceID, doorIDs=doorIDs, doorFlag=doorFlag))
    except grpc.RpcError as e:
      logger.error(f'Cannot lock the doors: {e}')
      raise
  def unlock(self, deviceID, doorIDs, doorFlag):
    try:
      self.stub.Unlock(door_pb2_grpc.door__pb2.UnlockRequest(deviceID=deviceID, doorIDs=doorIDs, doorFlag=doorFlag))
    except grpc.RpcError as e:
      logger.error(f'Cannot unlock the doors: {e}')
      raise
  def release(self, deviceID, doorIDs, doorFlag):
    try:
      self.stub.Release(door_pb2_grpc.door__pb2.ReleaseRequest(deviceID=deviceID, doorIDs=doorIDs, doorFlag=doorFlag))
    except grpc.RpcError as e:
      logger.error(f'Cannot release the door flags: {e}')
      raise
  def setAlarm(self, deviceID, doorIDs, alarmFlag):
    try:
      self.stub.SetAlarm(door_pb2_grpc.door__pb2.SetAlarmRequest(deviceID=deviceID, doorIDs=doorIDs, alarmFlag=alarmFlag))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the alarm flags: {e}')
      raise
class RS485Svc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = rs485_pb2_grpc.RS485Stub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the rs485 stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(rs485_pb2_grpc.rs485__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the rs485 config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(rs485_pb2_grpc.rs485__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the rs485 config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(rs485_pb2_grpc.rs485__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the rs485 config: {e}')
      raise
  def searchSlave(self, deviceID):
    try:
      response = self.stub.SearchDevice(rs485_pb2_grpc.rs485__pb2.SearchDeviceRequest(deviceID=deviceID))
      return response.slaveInfos
    except grpc.RpcError as e:
      logger.error(f'Cannot search slave devices: {e}')
      raise
  def getSlave(self, deviceID):
    try:
      response = self.stub.GetDevice(rs485_pb2_grpc.rs485__pb2.GetDeviceRequest(deviceID=deviceID))
      return response.slaveInfos
    except grpc.RpcError as e:
      logger.error(f'Cannot get slave devices: {e}')
      raise    
  def setSlave(self, deviceID, slaveInfos):
    try:
      self.stub.SetDevice(rs485_pb2_grpc.rs485__pb2.SetDeviceRequest(deviceID=deviceID, slaveInfos=slaveInfos))
    except grpc.RpcError as e:
      logger.error(f'Cannot set slave devices: {e}')
      raise    
class AuthSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = auth_pb2_grpc.AuthStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the auth stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(auth_pb2_grpc.auth__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the auth config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(auth_pb2_grpc.auth__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the auth config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(auth_pb2_grpc.auth__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the auth config: {e}')
      raise
class AccessSvc:
  stub = None
  newAccessGroup = access_pb2_grpc.access__pb2.AccessGroup
  newAccessLevel = access_pb2_grpc.access__pb2.AccessLevel
  def __init__(self, channel): 
    try:
      self.stub = access_pb2_grpc.AccessStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the access stub: {e}')
      raise
  def getList(self, deviceID):
    try:
      response = self.stub.GetList(access_pb2_grpc.access__pb2.GetListRequest(deviceID=deviceID))
      return response.groups
    except grpc.RpcError as e:
      logger.error(f'Cannot get the access groups: {e}')
      raise
  def add(self, deviceID, groups):
    try:
      self.stub.Add(access_pb2_grpc.access__pb2.AddRequest(deviceID=deviceID, groups=groups))
    except grpc.RpcError as e:
      logger.error(f'Cannot add access groups: {e}')
      raise
  def delete(self, deviceID, groupIDs):
    try:
      self.stub.Delete(access_pb2_grpc.access__pb2.DeleteRequest(deviceID=deviceID, groupIDs=groupIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the access groups: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(access_pb2_grpc.access__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the access groups: {e}')
      raise
  def getLevelList(self, deviceID):
    try:
      response = self.stub.GetLevelList(access_pb2_grpc.access__pb2.GetLevelListRequest(deviceID=deviceID))
      return response.levels
    except grpc.RpcError as e:
      logger.error(f'Cannot get the access levels: {e}')
      raise
  def addLevel(self, deviceID, levels):
    try:
      self.stub.AddLevel(access_pb2_grpc.access__pb2.AddLevelRequest(deviceID=deviceID, levels=levels))
    except grpc.RpcError as e:
      logger.error(f'Cannot add access levels: {e}')
      raise
  def deleteLevel(self, deviceID, levelIDs):
    try:
      self.stub.DeleteLevel(access_pb2_grpc.access__pb2.DeleteLevelRequest(deviceID=deviceID, levelIDs=levelIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the access levels: {e}')
      raise
  def deleteAllLevel(self, deviceID):
    try:
      self.stub.DeleteAllLevel(access_pb2_grpc.access__pb2.DeleteAllLevelRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the access levels: {e}')
      raise
class ScheduleSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = schedule_pb2_grpc.ScheduleStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the schedule stub: {e}')
      raise
  def getList(self, deviceID):
    try:
      response = self.stub.GetList(schedule_pb2_grpc.schedule__pb2.GetListRequest(deviceID=deviceID))
      return response.schedules
    except grpc.RpcError as e:
      logger.error(f'Cannot get the schedule list: {e}')
      raise
  def add(self, deviceID, schedules):
    try:
      self.stub.Add(schedule_pb2_grpc.schedule__pb2.AddRequest(deviceID=deviceID, schedules=schedules))
    except grpc.RpcError as e:
      logger.error(f'Cannot add schedules: {e}')
      raise
  def delete(self, deviceID, scheduleIDs):
    try:
      self.stub.Delete(schedule_pb2_grpc.schedule__pb2.DeleteAllRequest(deviceID=deviceID,scheduleIDs=scheduleIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the schedules: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(schedule_pb2_grpc.schedule__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the schedules: {e}')
      raise
  def getHolidayList(self, deviceID):
    try:
      response = self.stub.GetHolidayList(schedule_pb2_grpc.schedule__pb2.GetHolidayListRequest(deviceID=deviceID))
      return response.groups
    except grpc.RpcError as e:
      logger.error(f'Cannot get the holiday list: {e}')
      raise
  def addHoliday(self, deviceID, groups):
    try:
      self.stub.AddHoliday(schedule_pb2_grpc.schedule__pb2.AddHolidayRequest(deviceID=deviceID, groups=groups))
    except grpc.RpcError as e:
      logger.error(f'Cannot add holiday groups: {e}')
      raise
  def deleteHoliday(self, deviceID, groupIDs):
    try:
      self.stub.DeleteAllHoliday(schedule_pb2_grpc.schedule__pb2.DeleteAllHolidayRequest(deviceID=deviceID, groupIDs=groupIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the holiday groups: {e}')
      raise
  def deleteAllHoliday(self, deviceID):
    try:
      self.stub.DeleteAllHoliday(schedule_pb2_grpc.schedule__pb2.DeleteAllHolidayRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the holiday groups: {e}')
      raise
class ActionSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = action_pb2_grpc.TriggerActionStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the action stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(action_pb2_grpc.action__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the action config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(action_pb2_grpc.action__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the action config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(action_pb2_grpc.action__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the action config on multiple: {e}')
      raise
class TNASvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = tna_pb2_grpc.TNAStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the tna stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(tna_pb2_grpc.tna__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the tna config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(tna_pb2_grpc.tna__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the tna config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfig(tna_pb2_grpc.tna__pb2.SetConfigRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the tna config on multiple devices: {e}')
      raise
  def getTNALog(self, deviceID, startEventID, maxNumOfLog):
    try:
      response = self.stub.GetTNALog(tna_pb2_grpc.tna__pb2.GetTNALogRequest(deviceID=deviceID, startEventID=startEventID, maxNumOfLog=maxNumOfLog))
      return response.TNAEvents
    except grpc.RpcError as e:
      logger.error(f'Cannot get the TNA event log: {e}')
  def getJobCodeLog(self, deviceID, startEventID, maxNumOfLog):
    try:
      response = self.stub.GetJobCodeLog(tna_pb2_grpc.tna__pb2.GetJobCodeLogRequest(deviceID=deviceID, startEventID=startEventID, maxNumOfLog=maxNumOfLog))
      return response.TNAEvents
    except grpc.RpcError as e:
      logger.error(f'Cannot get the JobCode event log: {e}')
      raise
class OperatorSvc:
  newOperator = auth_pb2_grpc.auth__pb2.Operator
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = operator_pb2_grpc.OperatorStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Operator stub: {e}')
      raise
  def getList(self, deviceID):
    try:
      response = self.stub.GetList(operator_pb2_grpc.operator__pb2.GetListRequest(deviceID=deviceID))
      return response.operators
    except grpc.RpcError as e:
      logger.error(f'Cannot get the operator list: {e}')
      raise
  def add(self, deviceID, operators):
    try:
      self.stub.Add(operator_pb2_grpc.operator__pb2.AddRequest(deviceID=deviceID, operators=operators))
    except grpc.RpcError as e:
      logger.error(f'Cannot add Operators: {e}')
      raise
  def addMulti(self, deviceIDs, operators):
    try:
      self.stub.AddMulti(operator_pb2_grpc.operator__pb2.AddMultiRequest(deviceIDs=deviceIDs, operators=operators))
    except grpc.RpcError as e:
      logger.error(f'Cannot add Multiple Operators: {e}')
      raise
  def delete(self, deviceID, operatorIDs):
    try:
      self.stub.Delete(operator_pb2_grpc.operator__pb2.DeleteRequest(deviceID=deviceID, operatorIDs=operatorIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the Operators: {e}')
      raise
  def deleteMulti(self, deviceIDs, operatorIDs):
    try:
      self.stub.DeleteMulti(operator_pb2_grpc.operator__pb2.DeleteMultiRequest(deviceIDs=deviceIDs, operatorIDs=operatorIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete multiple Operators: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(operator_pb2_grpc.operator__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the Operators: {e}')
      raise
  def deleteAllMulti(self, deviceIDs):
    try:
      self.stub.DeleteAllMulti(operator_pb2_grpc.operator__pb2.DeleteAllMultiRequest(deviceIDs=deviceIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete all the Operators on multiple devices: {e}')
      raise
class RTSPSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = rtsp_pb2_grpc.RTSPStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the RTSP stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(rtsp_pb2_grpc.rtsp__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the RTSP config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(rtsp_pb2_grpc.rtsp__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the RTSP config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(rtsp_pb2_grpc.rtsp__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the RTSP config on multiple: {e}')
      raise
class VOIPSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = voip_pb2_grpc.VOIPStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the VOIP stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(voip_pb2_grpc.voip__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the VOIP config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(voip_pb2_grpc.voip__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the VOIP config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(voip_pb2_grpc.voip__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the VOIP config on multiple: {e}')
      raise
#Zoned Svc's
class LockZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = lock_zone_pb2_grpc.LockZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Lock Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(lock_zone_pb2_grpc.lock__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the lock Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(lock_zone_pb2_grpc.lock__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the lock Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(lock_zone_pb2_grpc.lock__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the lock Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(lock_zone_pb2_grpc.lock__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the lock Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(lock_zone_pb2_grpc.lock__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all lock Zones: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(lock_zone_pb2_grpc.lock__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on lock Zones: {e}')
      raise    
class TimedAPBZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = timed_apb_zone_pb2_grpc.TimedAPBZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Timed APB Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Timed APB Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Timed APB Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the Timed APB Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the Timed APB Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all Timed APB Zones: {e}')
      raise      
  def clear(self, deviceID, zoneID, userIDs):
    try:
      self.stub.Clear(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.ClearRequest(deviceID=deviceID, zoneID=zoneID, userIDs=userIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear the Timed APB Zones for IDs: {e}')
      raise
  def clearAll(self, deviceID, zoneID):
    try:
      self.stub.ClearAll(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.ClearAllRequest(deviceID=deviceID, zoneID=zoneID))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear all users Timed APB Zones: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(timed_apb_zone_pb2_grpc.timed__apb__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on Timed APB Zones: {e}')
      raise    
class APBZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = apb_zone_pb2_grpc.APBZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the APB Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(apb_zone_pb2_grpc.apb__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the APB Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(apb_zone_pb2_grpc.apb__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the APB Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(apb_zone_pb2_grpc.apb__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the APB Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(apb_zone_pb2_grpc.apb__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the APB Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(apb_zone_pb2_grpc.apb__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all APB Zones: {e}')
      raise      
  def clear(self, deviceID, zoneID, userIDs):
    try:
      self.stub.Clear(apb_zone_pb2_grpc.apb__zone__pb2.ClearRequest(deviceID=deviceID, zoneID=zoneID, userIDs=userIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear the APB Zone for IDs: {e}')
      raise
  def clearAll(self, deviceID, zoneID):
    try:
      self.stub.ClearAll(apb_zone_pb2_grpc.apb__zone__pb2.ClearAllRequest(deviceID=deviceID, zoneID=zoneID))
    except grpc.RpcError as e:
      logger.error(f'Cannot clear all users on APB Zone: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(apb_zone_pb2_grpc.apb__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on APB Zones: {e}')
      raise    
class IntrusionZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = intrusion_zone_pb2_grpc.IntrusionAlarmZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Intrusion Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(intrusion_zone_pb2_grpc.intrusion__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Intrusion Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(intrusion_zone_pb2_grpc.intrusion__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Intrusion Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(intrusion_zone_pb2_grpc.intrusion__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the Intrusion Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(intrusion_zone_pb2_grpc.intrusion__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the Intrusion Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(intrusion_zone_pb2_grpc.intrusion__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all Intrusion Zones: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(intrusion_zone_pb2_grpc.intrusion__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on Intrusion Zones: {e}')
      raise      
  def setArm(self, deviceID, zoneIDs, armed):
    try:
      response = self.stub.SetArm(intrusion_zone_pb2_grpc.intrusion__zone__pb2.SetArmRequest(deviceID=deviceID, zoneIDs=zoneIDs, armed=armed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set arm on Intrusion Zones: {e}')
      raise  
class FireZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = fire_zone_pb2_grpc.FireAlarmZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Fire Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(fire_zone_pb2_grpc.fire__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Fire Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(fire_zone_pb2_grpc.fire__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Fire Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(fire_zone_pb2_grpc.fire__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the Fire Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(fire_zone_pb2_grpc.fire__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the Fire Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(fire_zone_pb2_grpc.fire__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all Fire Zones: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(fire_zone_pb2_grpc.fire__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on Fire Zones: {e}')
      raise      
class InterlockZoneSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = interlock_zone_pb2_grpc.InterlockZoneStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Interlock Zone stub: {e}')
      raise
  def get(self, deviceID):
    try:
      response = self.stub.Get(interlock_zone_pb2_grpc.interlock__zone__pb2.GetRequest(deviceID=deviceID))
      return response.zones
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Interlock Zones: {e}')
      raise
  def getStatus(self, deviceID, zoneIDs):
    try:
      response = self.stub.GetStatus(interlock_zone_pb2_grpc.interlock__zone__pb2.GetStatusRequest(deviceID=deviceID, zoneIDs=zoneIDs))
      return response.status
    except grpc.RpcError as e:
      logger.error(f'Cannot get the Interlock Zones Status: {e}')
      raise
  def add(self, deviceID, zones):
    try:
      self.stub.Add(interlock_zone_pb2_grpc.interlock__zone__pb2.AddRequest(deviceID=deviceID, zones=zones))
    except grpc.RpcError as e:
      logger.error(f'Cannot add the Interlock Zones: {e}')
      raise
  def delete(self, deviceID, zoneIDs):
    try:
      self.stub.Delete(interlock_zone_pb2_grpc.interlock__zone__pb2.DeleteRequest(deviceID=deviceID, zoneIDs=zoneIDs))
    except grpc.RpcError as e:
      logger.error(f'Cannot delete the Interlock Zones: {e}')
      raise
  def deleteAll(self, deviceID):
    try:
      self.stub.DeleteAll(interlock_zone_pb2_grpc.interlock__zone__pb2.DeleteAllRequest(deviceID=deviceID))
    except grpc.RpcError as e:
      logger.error(f'Cannot Delete all Interlock Zones: {e}')
      raise      
  def setAlarm(self, deviceID, zoneIDs, alarmed):
    try:
      response = self.stub.SetAlarm(interlock_zone_pb2_grpc.interlock__zone__pb2.SetAlarmRequest(deviceID=deviceID, zoneIDs=zoneIDs, alarmed=alarmed))
    except grpc.RpcError as e:
      logger.error(f'Cannot set alarm on Interlock Zones: {e}')
      raise  
#below currently not implemented in server.exe
'''
class InputSvc:
  stub = None
  def __init__(self, channel): 
    try:
      self.stub = input_pb2_grpc.InputStub(channel)
    except grpc.RpcError as e:
      logger.error(f'Cannot get the input stub: {e}')
      raise
  def getConfig(self, deviceID):
    try:
      response = self.stub.GetConfig(input_pb2_grpc.input__pb2.GetConfigRequest(deviceID=deviceID))
      return response.config
    except grpc.RpcError as e:
      logger.error(f'Cannot get the input config: {e}')
      raise
  def setConfig(self, deviceID, config):
    try:
      self.stub.SetConfig(input_pb2_grpc.input__pb2.SetConfigRequest(deviceID=deviceID, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the input config: {e}')
      raise
  def setConfigMulti(self, deviceIDs, config):
    try:
      self.stub.SetConfigMulti(input_pb2_grpc.input__pb2.SetConfigMultiRequest(deviceIDs=deviceIDs, config=config))
    except grpc.RpcError as e:
      logger.error(f'Cannot set the input config on multiple: {e}')
      raise
'''