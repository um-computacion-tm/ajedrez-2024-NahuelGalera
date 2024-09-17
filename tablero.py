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
        tablero_str = "  a b c d e f g h\n"
        for i, fila in enumerate(reversed(self.__posiciones__)):
            tablero_str += str(8 - i) + " "
            for celda in fila:
                tablero_str += str(celda) if celda is not None else "."
                tablero_str += " "
            tablero_str += "\n"
        return tablero_str

    def get_element(self, fila, col):
        if 0 <= fila < 8 and 0 <= col < 8:
            return self.__posiciones__[fila][col]
        else:
            raise ValueError("Posición fuera de rango")

    def get_pieza(self, fila, col):
        return self.get_element(fila, col)

    def set_pieza(self, fila, col, pieza):
        if 0 <= fila < 8 and 0 <= col < 8:
            self.__posiciones__[fila][col] = pieza
        else:
            raise ValueError("Posición fuera de rango")

    def mover_pieza(self, fila_origen, col_origen, fila_destino, col_destino):
        pieza = self.get_element(fila_origen, col_origen)
        if pieza is not None and pieza.valid_positions(fila_origen, col_origen, fila_destino, col_destino):
            self.set_pieza(fila_destino, col_destino, pieza)
            self.set_pieza(fila_origen, col_origen, None)
        else:
            raise ValueError("Movimiento no válido")
        
    def puede_moverse_a(self, fila, col):
        print(f"Trying to move {self} to ({fila}, {col})")
        return True

tablero = Tablero()
print(tablero)