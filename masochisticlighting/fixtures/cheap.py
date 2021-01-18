from ..fixture import Fixture
from ..faders.color import ColorFader
from ..faders.brightness import BrightnessFader


class Cheap(Fixture):
    brightness = BrightnessFader
    red = ColorFader
    green = ColorFader
    blue = ColorFader

    def __init__(self, address: int):
        super().__init__(address=address)

    def add_faders(self):
        self.brightness = BrightnessFader(channel=self.address, controller=self.controller)
        self.red = ColorFader(channel=self.address + 1, controller=self.controller)
        self.green = ColorFader(channel=self.address + 2, controller=self.controller)
        self.blue = ColorFader(channel=self.address + 3, controller=self.controller)

    def bright(self, bright: int = 100):
        return {bright: self.brightness.value(bright)}

    def color(self, red: int = -1, green: int = -1, blue: int = -1):
        return {
            red: self.red.value(red),
            green: self.green.value(green),
            blue: self.blue.value(blue)
        }
