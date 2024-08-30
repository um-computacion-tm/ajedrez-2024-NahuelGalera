
from torre import Torre

class tablero:
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
            for cell in fila:
                if cell is not None:
                    tablero_str += str(cell)
                else:
                    tablero_str += " "
            tablero_str += "\n"
        return tablero_str

    def get_piece(self, fila, col):
        return self.__posiciones__[fila][col]

    def set_piece(self, fila, col, piece):
        self.__posiciones__[fila][col] = piece