from DMXEnttecPro import Controller

class Fixture(object):
    def __init__(self, address: int, controller: Controller):
        self.address = address
        self.controller = controller
