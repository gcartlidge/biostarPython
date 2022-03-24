#Python Client for Suprema GSDK<br>

0.1.6 - Added firmwareUpdateMulti to DeviceSvc (Needed for multiple device upgrade internally)<br>
0.1.5 - Added OperatorSvc call so operators above 10 can be added. Supports getList, add, delete, deleteAll, addMulti, deleteMulti and deleteAllMulti<br>
0.1.4 - Added getFinger, getFace and getCard to UserSvc.<br>
        Added getQRConfig, setQRConfig and writeQR to CardSvc()<br>
0.1.3 - Added AuthSvc, AccessSvc, ScheduleSvc, ActionSvc and TNASvc.<br>
        Under UserSvc, added newUser, newUserCard, newUserFinger and newUserFace for ease of calling when enrolling new user info.<br><br>
0.1.2 - Updated initial json file string, so import on linux works<br><br>
0.1.1 - Added Readme<br><br>
0.1.0 - Initial Commit<br>

This is the pip distributable version of the Suprema GSDK Python client, which makes it easier to interact with the GSDK.<br><br>

The examples from the [Suprema GSDK wiki][gsdkwiki] can be used, but with this package, all dependencies are handled via PIP.
The EventCode .json file and device list are also initialized automatically when importing package.<br><br>

On some clients (Particularly android) the  EventCode json can sometimes not be loaded. If this happens, an error will display.
You can then call supremaPython.initCodeMap(JsonFileLocation)<br><br>

To check Event codes, call supremaPython.getEventString(eventCode,subCode)<br>
To check device type, call supremaPython.deviceType\[deviceCode\]

##How to use the rest of the classes.

All classes that can be used are imported under the biostarPython package.
The ones currently written are:<br>
GatewayClient, <br>
ConnectSvc, <br>
DeviceSvc, <br>
FaceSvc, <br>
FingerSvc, <br>
StatusSvc, <br>
UserSvc,<br>
DisplaySvc,<br>
AdminSvc,<br>
WiegandSvc,<br>
TimeSvc,<br>
CardSvc,<br>
EventSvc,<br>
NetworkSvc,<br>
ServerSvc,<br>
SystemSvc,<br>
DoorSvc,<br>
RS485Svc,<br>
AuthSvc,<br>
AccessSvc,<br> 
ScheduleSvc,<br>
ActionSvc,<br>
TNASvc<br>
OperatorSvc<br>

With the remaining being added in a future release.<br>

With all of these services, they are a callable class underneath the biostarPython package. An example of initial setup with the GatewayClient and ConnectSvc is below:
For all of the functions below these services, they are formated with the first letter in lowercase, so to search a device would be searchDevice(), to get info would be getInfo().
The guides on how to use these are present at the the [Suprema GSDK wiki][gsdkwiki] <br><br>

import biostarPython as g<br>
gateway = g.GatewayClient('127.0.0.1',4000,'ca.crt')<br>
channel = gateway.getChannel()<br>
connect = g.ConnectSvc(channel)<br>
connect.searchDevice(300)

[gsdkwiki]: https://biostar-dev.github.io/g-sdk/