
from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero
        super().__init__()

    @property
    @abstractmethod
    def blanca_str(self):
        pass

    @property
    @abstractmethod
    def negra_str(self):
        pass

    def __str__(self):
        if self.__color__ == "BLANCA":
            return self.blanca_str
        else:
            return self.negra_str

