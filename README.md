# Python Client for Suprema GSDK

This is the pip distributable version of the Suprema GSDK Python client, which makes it easier to interact with the GSDK.<br>

The examples from the [Suprema GSDK Wiki](https://supremainc.github.io/g-sdk/) can be used, but with this package, all dependencies are handled via PIP. The EventCode .json file and device list are also initialized automatically when importing package.<br>
### Tips
On some clients (Particularly android) the  EventCode json can sometimes not be loaded. If this happens, an error will display. You can then call 

```python
JsonFileLocation = "C:\\biostarPython\\event_code.json"
biostarPython.initCodeMap(JsonFileLocation)
```
To check Event codes, call 
```python
biostarPython.getEventString(eventCode,subCode)
```
To check device type, call 
```python
biostarPython.deviceType[deviceCode]
```
I'd also recommend checking out [Advanced Installer](https://www.advancedinstaller.com/)! They allow free licences for open-source projects and the features of the program licences are well worth it!

## How to use the rest of the classes.

All classes that can be used are imported under the biostarPython package.
The ones currently written are:<br>
**GatewayClient, ConnectSvc, DeviceSvc, FaceSvc, FingerSvc, StatusSvc, UserSvc, DisplaySvc, AdminSvc, WiegandSvc, TimeSvc, CardSvc, EventSvc, NetworkSvc, ServerSvc, SystemSvc, DoorSvc, RS485Svc, AuthSvc, AccessSvc, ScheduleSvc, ActionSvc, TNASvc, OperatorSvc, LockZoneSvc, TimedAPBZoneSvc, APBZoneSvc, IntrusionZoneSvc, FireZoneSvc, InterlockZoneSvc, UDPSvc & TestSvc**

With the remaining being added in a future release. 
I think im up to date! <br>

With all of these services, they are a callable class underneath the biostarPython package. An example of initial setup with the GatewayClient and ConnectSvc is below:
For all of the functions below these services, they are formated with the first letter in lowercase, so to search a device would be searchDevice(), to get info would be getInfo().<br>
The guides on how to use these are present at the the  [GSDK Homepage](https://supremainc.github.io/g-sdk/)<br>
```python
# import the service duh!
import biostarPython as g
# connect to the gateway, get a channel, then funnel this through to the 
# services!
gateway = g.GatewayClient('127.0.0.1',4000,'ca.crt')
channel = gateway.getChannel()
connect = g.ConnectSvc(channel)
face = g.FaceSvc(channel)
network = g.NetworkSvc(channel)
# will return a list of devices visible on UDP
deviceInfo = connect.searchDevice(300) 
# needs IP address, port and SSL state
bs3 = connect.connect(connect.getConnInfo('192.168.0.50', 51211, False))
# 4 is the default scan threshold
face.scan(bs3,4)
#lets get and change an IP Config
existingConfig = network.getIPConfig(bs3)
existingConfig.useDHCP = False
existingConfig.IPAddress = '192.168.0.20'
network.setIPConfig(bs3, existingConfig)
```

All of the specific APIs can be found at the wiki Above.

### changelog

- 0.4.0.1 - Added UpdateSlideImages to DisplaySvc and added Fingerprint to TestSvc.
- 0.4.0.0 - Updated proto files to 1.7.0 (New Features, BEW3 support), added TestSvc (Waiting on support from device), fixed factoryDefault parameters.
- 0.3.0.5 - Added UDPSvc for changing IP config via UDP, Updated Proto generation to 1.6.0 version of GSDK.
- 0.3.0.2 - Fixed no response recieved from some user commands, also added newEventFilter()
          under event service, to create a new Filter.
- 0.3.0.0 - Support for BS3, VOIP, RTSP and Wiegand User ID
- 0.2.1.4 - Version Push
- 0.2.1.2 - Fixed issue with importing none existent package
- 0.2.1.0 - Addes getJobCode, setJobCode, setJobCodeMulti and setAccessGroupMulti to the UserSvc
- 0.2.0.1 - Added searchInfoToConnectInfo(self, searchInfo, isAsync) under ConnectSvc, allowing generation of Connection Parameters directly from search results
- 0.2.0.0 - Upgraded support for gRPC to the newest version supported by python (Regenerated .py files from .proto)
- 0.1.9.0 - Added zone services, LockZone, APBZone, TimedAPBZone, FireZone, InterlockZone and IntrusionZone are included. Also edited protobuf version to include security fixes (3.20.1)
- 0.1.8.8 - Fixed minor issue with finger.scan (Did not return data)
- 0.1.8.6 - Fixed minor issues
- 0.1.8 - Implemented version check for Protobuf (3.20)
- 0.1.7 - Implemented proper logging, a GSDKlog.log file is now used instead of the standard print command.
- 0.1.6 - Added firmwareUpdateMulti to DeviceSvc (Needed for multiple device upgrade internally)
- 0.1.5 - Added OperatorSvc call so operators above 10 can be added. Supports getList, add, delete, deleteAll, addMulti, deleteMulti and deleteAllMulti
- 0.1.4 - Added getFinger, getFace and getCard to UserSvc. Added getQRConfig, setQRConfig and writeQR to CardSvc()
- 0.1.3 - Added AuthSvc, AccessSvc, ScheduleSvc, ActionSvc and TNASvc.
        Under UserSvc, added newUser, newUserCard, newUserFinger and newUserFace for ease of calling when enrolling new user info.
- 0.1.2 - Updated initial json file string, so import on linux works
- 0.1.1 - Added Readme
- 0.1.0 - Initial Commit

