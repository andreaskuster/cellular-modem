from abc import ABC, abstractmethod


class SMS(ABC):

    @abstractmethod
    def send_sms(self):
        raise NotImplementedError()

    @abstractmethod
    def receive_sms(self):
        raise NotImplementedError()
