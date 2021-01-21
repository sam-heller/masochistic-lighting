from pubsub import pub
from singleton_decorator import singleton


class Mode(object):
    modes = {
        "ALL": 1,
        "GROUP": 2,
        "MANUAL": 3
    }
    state: int

    def __init(self):
        pub.subscribe(self.pubsub_receive, 'select')

    def pubsub_receive(self, message):
        if 'sub_id' in message:
            if int(message['sub_id']) in self.modes.values():
                self.current_mode = int(message['sub_id'])

    class Decorators(object):
        def key(self, key):
            if type(key) is str:
                key = key.strip().upper()
                if key in Mode.modes.keys():
                    return
            if type(key) is int:
                pass


    @Decorators.key()
    def pubsub_send(self):
        pub.sendMessage('client', group='select', item=f'mode/{self.current_mode}/1', value=1)

    def is_currently(self, mode_key: str = "", mode_value: int = -1) -> bool:
        if mode_value in self.modes.values():
            return self.state == mode_value
        elif mode_key != "" and mode_key.upper() in self.modes.keys():
            return self.state == self.modes[mode_key.upper()]
        else:
            raise Exception(f"Invalid  mode key or no mode key used for mode check {mode_key}")

    def change(self):
        print('ok')

