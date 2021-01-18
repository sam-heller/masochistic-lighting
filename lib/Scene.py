from DMXEnttecPro import Controller

from lib.Cheapo import Cheapo


class Scene(object):
    def __init__(self, controller: Controller):
        self.dmx = controller
        self.fixtures = []

    def add_cheapo(self, **kwargs):
        address = kwargs.get('address')
        self.fixtures.append(Cheapo(address=address, controller=self.dmx))

    def update(self, bright: int = -1, red: int = -1, green: int = -1, blue: int = -1):
        for fixture in self.fixtures:
            fixture.color(red, green, blue)
            fixture.bright(bright)
        self.dmx.submit()
