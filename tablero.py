from torre import Torre
from caballo import Caballo
from alfil import Alfil
from reina import Reina
from rey import Rey
from peon import Peon
from exceptions import *

class Tablero:
    def __init__(self):
        self.__tablero__ = [[None for _ in range(8)] for _ in range(8)]
        self.__tablero__[0][0] = Torre("NEGRA", self)
        self.__tablero__[0][7] = Torre("NEGRA", self)
        self.__tablero__[7][0] = Torre("BLANCA", self)
        self.__tablero__[7][7] = Torre("BLANCA", self)
        self.__tablero__[0][1] = Caballo("NEGRA", self)
        self.__tablero__[0][6] = Caballo("NEGRA", self)
        self.__tablero__[7][1] = Caballo("BLANCA", self)
        self.__tablero__[7][6] = Caballo("BLANCA", self)
        self.__tablero__[0][2] = Alfil("NEGRA", self)
        self.__tablero__[0][5] = Alfil("NEGRA", self)
        self.__tablero__[7][2] = Alfil("BLANCA", self)
        self.__tablero__[7][5] = Alfil("BLANCA", self)
        self.__tablero__[7][3] = Reina("BLANCA", self)
        self.__tablero__[0][3] = Reina("NEGRA", self)
        self.__tablero__[7][4] = Rey("BLANCA", self)
        self.__tablero__[0][4] = Rey("NEGRA", self)
        for i in range(8):
            self.__tablero__[6][i] = Peon("BLANCA", self)
            self.__tablero__[1][i] = Peon("NEGRA", self)

    def __str__(self):
        tablero_str = "  a b c d e f g h\n"
        for i, fila in enumerate(reversed(self.__tablero__)):
            tablero_str += str(8 - i) + " "
            for celda in fila:
                tablero_str += str(celda) if celda is not None else "."
                tablero_str += " "
            tablero_str += "\n"
        return tablero_str

    def get_piece(self, fila, col):
        # Ensure the coordinates are within the tablero limits
        if 0 <= fila < 8 and 0 <= col < 8:
            return self.__tablero__[fila][col]
        else:
            return None

    def set_piece(self, fila, col, piece):
        # Ensure the coordinates are within the tablero limits
        if 0 <= fila < 8 and 0 <= col < 8:
            self.__tablero__[fila][col] = piece

    def mover_pieza(self, fila_origen, col_origen, fila_destino, col_destino):
        pieza = self.get_piece(fila_origen, col_origen)
        if pieza is not None and pieza.valid_positions(fila_origen, col_origen, fila_destino, col_destino):
            self.set_piece(fila_destino, col_destino, pieza)
            self.set_piece(fila_origen, col_origen, None)
        else:
            raise ValueError("Movimiento no válido")
        
    def puede_moverse_a(self, fila, col):
        print(f"Trying to move {self} to ({fila}, {col})")
        return True

    def no_pieces_left(self, color):
        for fila in self.__tablero__:
            for pieza in fila:
                if pieza is not None and pieza.color == color:
                    return False
        return True

tablero = Tablero()
print(tablero)