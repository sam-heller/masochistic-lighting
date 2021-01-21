from DMXEnttecPro import Controller

from dmx.fader import Fader
from masochisticlighting.app.fixture_list import FixtureList


class Fixture(object):
    name: str
    config: dict
    dmx: Controller
    faders: dict

    def __init__(self, name: str, fixture_config: dict):
        self.name = name
        self.channel = fixture_config['channel']
        self.config = fixture_config
        self.faders = {}
        self.load_faders()
        FixtureList().add_fixture(name)

    def load_faders(self):
        for name, fader_config in self.config['faders'].items():
            self.faders[name] = Fader(
                name=name,
                starting_channel=self.channel,
                fader_config=fader_config)

    def update(self, fader: str, value: int):
        self.faders[fader].set(value)

    def update_all(self, value: int):
        for name, fader in self.faders.items():
            self.update(name, value)
