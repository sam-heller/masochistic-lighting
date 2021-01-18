from .Fixture import Fixture
from DMXEnttecPro import Controller
from .ColorFader import ColorFader
from .BrightnessFader import BrightnessFader


class Cheapo(Fixture):
    def __init__(self, address: int, controller: Controller):
        super().__init__(address=address, controller=controller)
        self.brightness = BrightnessFader(self.address, controller)
        self.red = ColorFader(self.address + 1, controller)
        self.green = ColorFader(self.address + 2, controller)
        self.blue = ColorFader(self.address + 3, controller)

    def bright(self, bright: int = 100):
        return {bright: self.brightness.value(bright)}

    def color(self, red: int, green: int, blue: int):
        return {
            red: self.red.value(red),
            green: self.green.value(green),
            blue: self.blue.value(blue)
        }

    def update(self):
        self.controller.submit()
