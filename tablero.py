
from torre import Torre

class Tablero:
    def __init__(self, for_test = False):
        self.__posiciones__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__posiciones__.append(col)
        if not for_test:
            self.__posiciones__[0][0] = Torre("NEGRA", self) # NEGRA
            self.__posiciones__[0][7] = Torre("NEGRA", self) # NEGRA
            self.__posiciones__[7][7] = Torre("BLANCA", self) # BLANCA
            self.__posiciones__[7][0] = Torre("BLANCA", self) # BLANCA

    def __str__(self):
        tablero_str = ""
        for fila in self.__posiciones__:
            for celda in fila:
                if celda is not None:
                    tablero_str += str(celda)
                else:
                    tablero_str += " "
            tablero_str += "\n"
        return tablero_str

    def get_pieza(self, fila, col):
        return self.__posiciones__[fila][col]

    def set_pieza(self, fila, col, pieza):
        self.__posiciones__[fila][col] = pieza