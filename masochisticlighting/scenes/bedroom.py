from ..scene import Scene
from ..fixtures.cheap import Cheap


class Bedroom(Scene):

    def define_fixtures(self):
        self.add_fixture(Cheap(1))
        self.add_fixture(Cheap(6))
        self.add_fixture(Cheap(11))
        self.add_fixture(Cheap(21))
        self.add_fixture(Cheap(26))
        self.add_fixture(Cheap(31))
        self.add_fixture(Cheap(36))
        self.add_fixture(Cheap(41))

    def define_groups(self):
        self.add_group('desk', [1, 6, 11])
        self.add_group('wall', [21, 26, 31, 41])
        self.add_group('bed', [36])

    def osc_group_mappings(self):
        self.group_mappings = [
            'desk', 'wall', 'bed'
        ]

    def osc_select_mappings(self):
        self.select_mappings = [
            [ 1,  6, 11, 21],
            [31, 26, 41, 36]
        ]
