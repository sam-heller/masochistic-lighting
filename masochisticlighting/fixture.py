from DMXEnttecPro import Controller


class Fixture(object):
    address = int
    controller = Controller

    def __init__(self, address: int):
        self.address = address

    def set_controller(self, controller: Controller):
        self.controller = controller
        self.add_faders()

    def add_faders(self):
        print('Fader definitions go here')

    def update(self):
        self.controller.submit()

    def color(self, red: int = -1, green: int = -1, blue: int = -1):
        print(f'Set fixture color to {red}.{green},{blue}')

    def bright(self, bright: int = -1):
        print(f'Set fixture brightness to {bright}')
