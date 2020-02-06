from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def network_status(self):
        raise NotImplementedError()

    @abstractmethod
    def connect(self, pin=None):
        pass

    @abstractmethod
    def disconnect(self):
        pass
