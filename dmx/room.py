from pubsub import pub

from masochisticlighting.app.config import Config
from dmx.fixture import Fixture
from masochisticlighting.app.mode import Mode


class Room(object):
    fixtures: dict
    name: str
    fixture_library: dict
    config: dict

    def __init__(self, name: str, ):
        self.name = name
        self.config = Config().get('rooms_enriched', name)
        self.fixtures: dict
        self.load_fixtures()

    def load_fixtures(self):
        self.fixtures = {}
        for fixture_name, fixture_config in self.config['fixtures'].items():
            self.fixtures[fixture_name] = Fixture(
                name=fixture_name,
                fixture_config=fixture_config, )

    def update(self, message: dict):
        mode = Mode()
        if mode.is_all():
            self.update_all(message)
        if mode.is_group():
            self.update_group(message)
        if mode.is_manual():
            self.update_manual(message)
        Config().submit()

    def update_all(self, message: dict):
        if 'item' in message:
            if message['item'] == 'all':
                for key, fixture in self.fixtures.items():
                    fixture.update_all(message['value'])
                self.sync_all(message['value'])
            else:
                for key, fixture in self.fixtures.items():
                    fixture.update(message['item'], message['value'])
                pub.sendMessage('client', group='light', item=message['item'], value=message['value'])

    def update_group(self, message):
        print(message)

    def update_manual(self, message):
        print(message)

    def init_state(self):
        for item, value in self.config['startup'].items():
            self.update('all', {'item': item, 'value': value})

    def sync_all(self, value):
        for item in ['red', 'green', 'blue', 'intensity']:
            pub.sendMessage('client', group='light', item=item, value=value)
