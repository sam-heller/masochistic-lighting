from pythonosc import udp_client
from pubsub import pub
from .decorators import *


class MessageBroker(object):
    __instance = None
    osc_clients = {}

    def __init__(self):
        if MessageBroker.__instance is not None:
            raise Exception("You can only build One Message Broker")
        else:
            pub.subscribe(MessageBroker.pubsub_to_osc, 'client')
            MessageBroker.__instance = self

    @staticmethod
    def get() :
        if MessageBroker.__instance is None:
            MessageBroker()
        return MessageBroker.__instance

    @staticmethod
    def pubsub_to_osc(group: str, item: str, value):
        for ip, client in MessageBroker.__instance.osc_clients.items():
            client.send_message(f'/{group}/{item}', value)
            print(f'sending message {ip}/{group}/{item} {value} ')

    @staticmethod
    @osc_message()
    def osc_to_pubsub(ip, port, group, message) -> None:
        if ip not in MessageBroker.get().osc_clients:
            MessageBroker.register_osc_client(ip, port)
        pub.sendMessage(group, message=message)

    @staticmethod
    def register_osc_client(ip: str, port: int) -> None:
        MessageBroker.get().osc_clients[ip] = udp_client.SimpleUDPClient(ip, 12345)


