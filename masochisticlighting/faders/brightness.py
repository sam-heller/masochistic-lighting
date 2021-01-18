from DMXEnttecPro import Controller
from ..fader import Fader


class BrightnessFader(Fader):
    def __init__(self, channel: int, controller=Controller):
        super().__init__(channel, controller)
        self.max = 100
