from abc import ABC, abstractmethod


class Lockable(ABC):

    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def unlock(self):
        pass
