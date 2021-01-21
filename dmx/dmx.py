from DMXEnttecPro import Controller
from singleton_decorator import singleton


@singleton
class Dmx(object):
    controller = None

    def __init__(self, device_address='/dev/ttyUSB0'):
        self.controller = Controller(device_address)

    def set_channel(self, channel: int, value: int, max_val: int):
        value = min(int(value), max_val)
        self.controller.set_channel(channel, value)

    def update(self):
        self.controller.submit()
