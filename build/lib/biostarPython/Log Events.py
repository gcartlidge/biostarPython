import biostarPython as bio    #My Python package for dealing with GSDK
import threading

gateway = bio.GatewayClient('127.0.0.1',4000,'C:\GSDK\Cert\CA.crt') #Setup Gateway
channel = gateway.getChannel() # Setup Channel
connect = bio.ConnectSvc(channel) # Setup Connect
event = bio.EventSvc(channel) # Setup Event

connectEvents = connect.subscribe(300) # Connected events

enabledDevices = []

def enableMonitoring(deviceID):
  event.enableMonitoring(deviceID) # Enable monitoring on recieved Device ID
  if deviceID not in enabledDevices: 
   enabledDevices.append(deviceID)
   stream = event.subscribe(300) # Setup stream for events
   for y in stream:
    print(y) # print events

def connectedCheck():
  for x in connectEvents: # check Connected events
   if x.status == 1: #For TCP connected
    print(x)
    enableMonitorThread = threading.Thread(target=enableMonitoring,args=(x.deviceID,)) #callback to previous enable monitoring to setup a stream
    enableMonitorThread.start()
   
connectedCheckThread = threading.Thread(target=connectedCheck)
connectedCheckThread.start()




