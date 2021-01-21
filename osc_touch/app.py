from pubsub import pub
from singleton_decorator import singleton

from osc_touch.mode import Mode
from util.config import Config
from util.decorators import app_message_hacks
from dmx.room import Room

@singleton
class App(object):
    config: Config
    mode: Mode

    def __init__(self, room='bedroom'):
        pub.subscribe(self.light_message_handler, 'light')
        self.current_room = Room(name=room)


    @app_message_hacks()
    def light_message_handler(self, message):
        self.current_room.update(message)


