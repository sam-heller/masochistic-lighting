from DMXEnttecPro import Controller
from .Fader import Fader


class BrightnessFader(Fader):
    def __init__(self, channel: int, controller=Controller):
        super().__init__(channel, controller)
        self.max = 100