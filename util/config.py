import os

import yaml
from DMXEnttecPro import Controller
from singleton_decorator import singleton


@singleton
class Config(object):
    rooms: dict
    fixtures: dict
    rooms_enriched: dict

    def __init__(self):
        self.rooms = self.load_yaml('rooms.yaml')
        self.fixtures = self.load_yaml('fixtures.yaml')
        self.rooms_enriched = self.enrich_room_config()
        self.controller = Controller('/dev/ttyUSB0')

    def load_yaml(self, filename):
        path = f'{os.getcwd()}/masochisticlighting/config/{filename}'
        with open(path) as f:
            loaded = yaml.load(f, Loader=yaml.FullLoader)
        return loaded

    def enrich_room_config(self):
        enriched = dict()
        for room_name, room in self.rooms.items():
            for fixture_name, fixture_config in room['fixtures'].items():
                fixture_config.update(self.fixtures[fixture_config['model']])
                enriched[room_name] = room
        return enriched

    def fixture_defined(self, key: str):
        return key in self.fixtures

    def get_fixture(self, key: str, subkey=None):
        if self.fixture_defined(key):
            fixtures = self.fixtures[key]
            if subkey is not None:
                return fixtures[subkey]
            return fixtures

    def get(self, config_name: str, key="root"):
        if hasattr(self, config_name):
            root = getattr(self, config_name)
            if key == 'root':
                return root
            if key in root:
                return root[key]

    def set_channel(self, channel: int, value: int, max_val: int):
        value = min(int(value), max_val)
        print(f'update {channel}, {value}')
        self.controller.set_channel(channel, value)

    def submit(self):
        print('Config submit')
        self.controller.submit()
