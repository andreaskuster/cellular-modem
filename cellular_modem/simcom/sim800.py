from cellular_modem.abstract_modem import AbstractModem
from cellular_modem.io.serial import SerialHandler


class SIM800(AbstractModem, SerialHandler):

    def __init__(self, pin=None, **kwds):
        super().__init__(**kwds)
        self.pin = pin

    def send_sms(self):
        raise NotImplementedError()

    def receive_sms(self):
        print("sms received")

    def data_received(self, data):
        print("data received: {}".format(data))

    def connection_made(self):
        print("connection made")

    def connection_lost(self):
        print("connection closed")
