
from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color):
        self.__color__ = color

    @abstractmethod
    def mover(self):
        pass

    @property
    def color(self):
        return self.__color__
    

