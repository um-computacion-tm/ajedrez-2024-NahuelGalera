from codigo_ajedrez.piezas import Torre

class Tablero:
    def __init__(self, posiciones):
        self.__posiciones__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__posiciones__.append(col)
        self.__posiciones__[0][0] = Torre("NEGRA")
        self.__posiciones__[0][7] = Torre("NEGRA")
        self.__posiciones__[7][0] = Torre("BLANCA")
        self.__posiciones__[7][7] = Torre("BLANCA")

    def get_pieza(self, row, col):
        return self.__posiciones__[row][col]
