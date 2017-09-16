#!/usr/bin/env python3
import sys

from pytradfri import Gateway
from pytradfri.group import Group
from pytradfri.api.libcoap_api import api_factory

TIMEOUT = 0.2

def find_light(name):
    """
    Find light with given name.
    If no such light is found None is returned.
    """
    device_command = gateway.get_devices()
    device_command._timeout = TIMEOUT
    device_commands = api(device_command)
    
    for cmd in group_commands:
        cmd._timeout = TIMEOUT
    
    devices = api(*device_commands)
    
    for dev in devices:
        if dev.name == name and dev.has_light_control:
            return dev
        
    return None


def find_group(name):
    """
    Find group with given name.
    If no such group is found None is returned.
    """
    group_command = gateway.get_groups()
    group_command._timeout = TIMEOUT
    
    group_commands = api(group_command)
    for cmd in group_commands:
        cmd._timeout = TIMEOUT
        
    groups = api(*group_commands)

    for group in groups:
        if group.name == name:
            return group

    return None
    

def dim(light, arg):
    """
    Dim light according to arg.
    """
    if arg[0] in ["+", "-"]:
        if isinstance(light, Group):
            value = light.dimmer
        else:
            value = light.light_control.lights[0].dimmer
            
        value += int(arg)
    else:
        value = int(arg)

        
    if isinstance(light, Group):
        command = light.set_dimmer(value, transition_time=0.2)
    else:
        command = light.light_control.set_dimmer(value, transition_time=0.2)
        
    api(command)

    
def power(light, arg):
    """
    Power light on or off according to arg.
    """
    if arg not in ["on", "off"]:
        print("Supported operations are 'power on' and 'power off'")
        sys.exit(1)
        
    state = (arg == "on")

    value = 127 if arg == "on" else 0
    dim(light, str(value))
    
    
def color(light, arg):
    """
    Set color of light according to arg (cold, normal, warm).
    """
    if isinstance(light, Group):
        print("Color not supported for groups")
        sys.exit(1)
    
    COLD, NORMAL, WARM = "f5faf6", "f1e0b5", "efd275"

    colors = {"cold": COLD, "normal": NORMAL, "warm": WARM}
    order = [COLD, NORMAL, WARM]
    
    if arg in ["+", "-"]:
        current = light.light_control.lights[0].hex_color
            
        index = order.index(current)        
        index += (1 if arg == "+" else -1)

        c = order[index % len(order)]
    else:
        c = colors[arg]

    command = light.light_control.set_hex_color(c)
    api(command)

    
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Syntax: lights.py <IP> <KEY> <NAME> <COMMAND> <ARGUMENT>")
        sys.exit(1)
    
    ip, key, name, command, arg = sys.argv[1:]

    api = api_factory(ip, key)
    gateway = Gateway()
    
    if name.startswith("group:"):
        light = find_group(name.split(":")[1])
    elif name.startswith("light:"):
        light = find_light(name.split(":")[1])
    else:
        light = find_light(name)
        
    if light == None:
        print("No devices named", name, "found")
        sys.exit(1)

    if command == "dim":
        dim(light, arg)
    elif command == "color":
        color(light, arg)
    elif command == "power":
        power(light, arg)
    else:
        print("No command", command)
    
