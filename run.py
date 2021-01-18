import math
from pythonosc import dispatcher
from pythonosc import osc_server
from DMXEnttecPro import Controller
from lib.Scene import Scene


# Build the scene containing cheapo type
# lights at the DMX addresses supplied.
def build_scene(controller_port: str = '/dev/ttyUSB0', addresses: list = [1]):
    dmx = Controller(controller_port)
    built_scene = Scene(dmx)
    for address in addresses:
        built_scene.add_cheapo(address=address)
    built_scene.update(100, 0, 0, 0)
    return built_scene


# Build a dispatch handler to parse the OSC
# message and update the lights accordingly
def osc_handler(address, *args):
    update_value = math.floor(float(args[1]))
    target_scene = args[0][0]
    target = address.replace('/light/', '')
    if   target == 'bright': target_scene.update(bright=update_value)
    elif target == 'red'   : target_scene.update(red=update_value)
    elif target == 'green' : target_scene.update(green=update_value)
    elif target == 'blue'  : target_scene.update(blue=update_value)


# Build the Message Handler
room = build_scene(addresses=[1, 6, 11, 21])
osc_dispatcher = dispatcher.Dispatcher()
osc_dispatcher.map("/light/*", osc_handler, room)

# Start the Server
server_address = ("192.168.0.33", 5005)
osc_server.ThreadingOSCUDPServer(server_address, osc_dispatcher).serve_forever()
