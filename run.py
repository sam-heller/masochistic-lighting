from DMXEnttecPro import Controller
from pythonosc import osc_server, dispatcher

from masochisticlighting.app import App
from masochisticlighting.message_broker import MessageBroker


#####
# Configuration
#####
dmx_controller_address = '/dev/ttyUSB0'
osc_server_ip = "192.168.0.33"
osc_server_port = 5005
# MessageBroker.send_to_pubsub(server=('10.1.1.1', 1234), path='/group/item', message=10)


####
# Load the App
####
app = App()
# MessageBroker.

######
# Build the Dispatcher
######
dispatch = dispatcher.Dispatcher()
dispatch.set_default_handler(MessageBroker.osc_to_pubsub, True)
# dispatch.set_default_handler(print, True)


######
# Start the Server
# noinspection PyTypeChecker
#######
osc_server.ThreadingOSCUDPServer(
    (osc_server_ip, osc_server_port),
    dispatch
).serve_forever()
