# piezas.py
class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero

    @property
    def color(self):
        return self.__color__

    @property
    def tablero(self):
        return self.__tablero__

    def __str__(self):
        return self.blanca_str if self.__color__ == "BLANCA" else self.negra_str