# lights
Small command line tool for controlling IKEA Trådfri lights.

Mainly built to allow dimming of lights with key bindings.
### Installation
 ```
 # ./install.sh
 ```
## Usage
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> <LIGHT> <OPERATION> <ARGUMENT>
```

### <GATEWAY-IP>
The IP of your Trådfri gateway.

### <GATEWAY-KEY>
The security key found on the bottom of your gateway.

### <LIGHT>
The name of the light or group. If controlling a group the <LIGHT> argument should be prefixed with ```group:```:
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> floor1 <OPERATION> <ARGUMENT>
```
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> group:living-room <OPERATION> <ARGUMENT>
```  
 
### <OPERATION>
The desired operation on selected light(s):

#### dim
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> <LIGHT> dim +32
```
##### <ARGUMENT>
A integer between 0 and 255. Relative dimming is done by placing a ```+``` or ```-``` before the integer.
  
#### color
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> <LIGHT> color warm
```
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> <LIGHT> color +
```

##### <ARGUMENT>
```cold```, ```normal``` or ```warm```. You can also cycle between given colors by using ```+``` or ```-```.

#### power
```
$ lights <GATEWAY-IP> <GATEWAY-KEY> <LIGHT> power on
```

##### <ARGUMENT>
```on``` or ```off```.


