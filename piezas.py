class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero

    def __str__(self):
        return self.__blanca_str__ if self.__color__ == "BLANCA" else self.__negra_str__

