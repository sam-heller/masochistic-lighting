from pythonosc import osc_server
from DMXEnttecPro import Controller
from masochisticlighting.scenes.bedroom import Bedroom

# Configuration
controller_address = '/dev/ttyUSB0'
osc_server_ip = "192.168.0.33"
osc_server_port = 5005

# Build the scene
scene = Bedroom(Controller(controller_address))

# Start the Server
osc_server.ThreadingOSCUDPServer((osc_server_ip, osc_server_port), scene.build_dispatcher()).serve_forever()
