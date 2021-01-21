from masochisticlighting.app.config import Config


class Fader(object):
    name: str
    max: int
    current: int
    channel: int

    def __init__(self, name: str, starting_channel: int, fader_config: dict):
        self.name = name
        self.channel = fader_config['channel'] + starting_channel - 1
        self.max = fader_config['max']
        self.config = Config()
        print(f'{self}')

    def set(self, value):

       self.config.set_channel(self.channel, value, self.max)