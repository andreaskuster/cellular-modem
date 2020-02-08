from abc import ABC, abstractmethod


class SMS(ABC):

    def __init__(self, **kwds):
        super().__init__(**kwds)

    @abstractmethod
    def send_sms(self):
        raise NotImplementedError()

    @abstractmethod
    def receive_sms(self):
        raise NotImplementedError()
