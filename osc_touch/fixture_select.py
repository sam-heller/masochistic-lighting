from pubsub import pub
from singleton_decorator import singleton


@singleton
class FixtureList(object):
    current_list = {}

    def __init__(self):
        pub.subscribe(self.select_handler, 'select')

    def select_handler(self, message):
        if 'item' in message and message['item'] == 'item':
            self.set_list_item_selected_status(message['sub_id'], int(message['value']))

    def set_label(self, label_id, fixture_name):
        pub.sendMessage('client', group='select', item=f'label-{label_id}', value=fixture_name)

    def set_list_item_selected_status(self, item_id, value):
        for fixture in self.current_list.values():
            if fixture['id'] == item_id:
                fixture['enabled'] = value > 0
                FixtureList.set_label(item_id, int(value))

    def init_fixture_list(self, fixture_names: list):
        FixtureList.clear_list()
        for name in fixture_names:
            self.add_fixture(name)

    def add_fixture(self, fixture_name):
        label_id = max(len(self.current_list) - 1, 1)
        if label_id <= 10:
            self.current_list[fixture_name] = dict(id=label_id, name=fixture_name, enabled=False)
            self.set_label(label_id=label_id, fixture_name=fixture_name)

    def clear_list(self):
        for label_id in range(1, 10):
            self.set_label(label_id, '')
        self.current_list = {}

