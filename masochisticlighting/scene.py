import math
from pythonosc import dispatcher
from DMXEnttecPro import Controller


class Scene(object):
    controller = Controller
    selected = dict[int: int]
    mode = str
    select_mappings = []
    group_mappings = []
    groups = {}
    fixtures = {}

    def __init__(self, controller: Controller):
        self.controller = controller
        self.mode = 'all'
        self.clear_selected()
        self.define_groups()
        self.define_fixtures()
        self.osc_select_mappings()
        self.osc_group_mappings()
        self.update_all(100, 0, 0)

    def add_fixture(self, fixture):
        fixture.set_controller(self.controller)
        self.fixtures[fixture.address] = fixture

    def add_group(self, name: str, group: list):
        self.groups[name] = group

    def set_selected(self, selected_id: int, include: int = 1):
        self.selected[selected_id] = include

    def clear_selected(self):
        self.selected = {}

    def set_mode(self, mode: int = 0):
        if mode == 0:
            self.mode = 'all'
        else:
            self.mode = 'selected'

    def update(self, bright: int = 100, red: int = -1, green: int = -1, blue: int = -1):
        if self.mode == 'all':
            self.update_all(bright, red, green, blue)
        elif self.mode == 'selected':
            self.update_selected(bright, red, green, blue)

    def update_all(self, bright: int = -1, red: int = -1, green: int = -1, blue: int = -1):
        for address, fixture in self.fixtures.items():
            fixture.color(red, green, blue)
            fixture.bright(bright)
        self.controller.submit()

    def update_selected(self, bright: int = -1, red: int = -1, green: int = -1, blue: int = -1):
        for index, included in self.selected.items():
            if included != 0:
                self.fixtures[index].color(red, green, blue)
                self.fixtures[index].bright(bright)
        self.controller.submit()

    def select_group(self, name: str):
        self.clear_selected()
        self.set_mode(1)
        for fixture_id in self.groups[name]:
            self.set_selected(fixture_id, 1)

    def build_dispatcher(self) -> dispatcher:
        my_dispatcher = dispatcher.Dispatcher()
        my_dispatcher.map("/light/*", self.light_handler)
        my_dispatcher.map("/select/*", self.select_handler)
        my_dispatcher.map("/group/*/1", self.mode_handler)
        my_dispatcher.map("/group/*/2", self.group_handler)
        return my_dispatcher

    # Handle messages to individual lights
    def light_handler(self, address, value):
        update_value = math.floor(float(value))
        if address == '/light/bright':
            self.update(bright=update_value)
        elif address == '/light/red':
            self.update(red=update_value)
        elif address == '/light/green':
            self.update(green=update_value)
        elif address == '/light/blue':
            self.update(blue=update_value)

    # Handle updates to switch current mode
    def mode_handler(self, address, mode):
        if address == '/group/1/1':
            mode = 0
        elif address == '/group/3/1':
            mode = 1
        self.set_mode(mode)

    def select_handler(self, address, enabled):
        parts = address.replace('/select/', '').split('/')
        selected = self.select_mappings[int(parts[1]) - 1][int(parts[0]) - 1]
        self.set_selected(selected, int(enabled))

    def group_handler(self, address, value):
        if value != 0.0:
            parts = address.replace('/group/', '').split('/')
            selected = self.group_mappings[int(parts[0]) - 1]
            self.select_group(selected)

    def define_fixtures(self):
        self.fixtures = {}

    def define_groups(self):
        self.groups = {}

    def osc_select_mappings(self):
        self.select_mappings = []

    def osc_group_mappings(self):
        self.group_mappings = []