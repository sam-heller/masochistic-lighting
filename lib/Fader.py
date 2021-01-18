from DMXEnttecPro import Controller


class Fader(object):
    def __init__(self, channel: int, controller: Controller):
        self.channel = channel
        self.max = 255
        self.current = 0
        self.controller = controller

    def value(self, value: int = -1):
        self.current = value if value != -1 else self.current
        self.controller.set_channel(channel=self.channel, value=self.current)
        return self.current
