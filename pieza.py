
class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero

    def __str__(self):
        if self.__color__ == "BLANCA":
            return self.blanca_str
        else:
            return self.negra_str

