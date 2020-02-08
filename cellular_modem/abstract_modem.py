from abc import ABC, abstractmethod
from cellular_modem.abstract_sms import SMS


class AbstractModem(SMS, ABC):

    def __init__(self, **kwds):
        super().__init__(**kwds)
