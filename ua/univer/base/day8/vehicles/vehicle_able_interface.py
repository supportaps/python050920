import abc
from abc import ABC


class MoveAble(ABC):
    @abc.abstractmethod
    def move(self):
        pass

class FlyAble(ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class SwimAble(ABC):
    @abc.abstractmethod
    def swim(self):
        pass