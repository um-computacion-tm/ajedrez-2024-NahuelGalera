from torre import Torre
from caballo import Caballo
from alfil import Alfil
from reina import Reina
from rey import Rey
from peon import Peon
from exceptions import *

class Tablero:
    def __init__(self):
        self.__posiciones__ = [[None for _ in range(8)] for _ in range(8)]
        self.__posiciones__[0][0] = Torre("NEGRA", self)
        self.__posiciones__[0][7] = Torre("NEGRA", self)
        self.__posiciones__[7][0] = Torre("BLANCA", self)
        self.__posiciones__[7][7] = Torre("BLANCA", self)
        self.__posiciones__[0][1] = Caballo("NEGRA", self)
        self.__posiciones__[0][6] = Caballo("NEGRA", self)
        self.__posiciones__[7][1] = Caballo("BLANCA", self)
        self.__posiciones__[7][6] = Caballo("BLANCA", self)
        self.__posiciones__[0][2] = Alfil("NEGRA", self)
        self.__posiciones__[0][5] = Alfil("NEGRA", self)
        self.__posiciones__[7][2] = Alfil("BLANCA", self)
        self.__posiciones__[7][5] = Alfil("BLANCA", self)
        self.__posiciones__[7][3] = Reina("BLANCA", self)
        self.__posiciones__[0][3] = Reina("NEGRA", self)
        self.__posiciones__[7][4] = Rey("BLANCA", self)
        self.__posiciones__[0][4] = Rey("NEGRA", self)
        for i in range(8):
            self.__posiciones__[6][i] = Peon("BLANCA", self)
            self.__posiciones__[1][i] = Peon("NEGRA", self)

    def __str__(self):
        posiciones_str = "  a b c d e f g h\n"
        for i, fila in enumerate(reversed(self.__posiciones__)):
            posiciones_str += str(8 - i) + " "
            for celda in fila:
                posiciones_str += str(celda) if celda is not None else "."
                posiciones_str += " "
            posiciones_str += "\n"
        return posiciones_str

    def get_piece(self, fila, col):
        if 0 <= fila < 8 and 0 <= col < 8:
            return self.__posiciones__[fila][col]
        else:
            return None

    def set_piece(self, fila, col, piece):
        if 0 <= fila < 8 and 0 <= col < 8:
            self.__posiciones__[fila][col] = piece

    def mover_pieza(self, inicio_fila, inicio_col, final_fila, final_col):
        pieza = self.get_piece(inicio_fila, inicio_col)
        print(f"Attempting to move piece from ({inicio_fila}, {inicio_col}) to ({final_fila}, {final_col})")
        if pieza is not None:
            print(f"Piece found: {pieza}")
            if pieza.mover(inicio_fila, inicio_col, final_fila, final_col, self):
                print(f"Move valid, updating board")
                self.set_piece(final_fila, final_col, pieza)
                self.set_piece(inicio_fila, inicio_col, None)
            else:
                print(f"Move invalid according to piece rules")
                raise ValueError("Movimiento no válido")
        else:
            print(f"No piece found at starting position")
            raise ValueError("Movimiento no válido")
        
    def puede_moverse_a(self, fila, col):
        print(f"Trying to move {self} to ({fila}, {col})")
        return True

    def no_pieces_left(self, color):
        for fila in self.__posiciones__:
            for pieza in fila:
                if pieza is not None and pieza.color == color:
                    return False
        return True

tablero = Tablero()
print(tablero)