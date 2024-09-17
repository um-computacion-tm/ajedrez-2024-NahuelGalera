from piezas import Pieza
from exceptions import InvalidMoveQueenMove

class Reina(Pieza):
    def __init__(self, color, board):
            super().__init__(color, board)

    @property
    def blanca_str(self):
        return "♕"

    @property
    def negra_str(self):
        return "♛"

    def movimientos_validos(self, fila, columna):
        movimientos = []
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]  # horizontal, vertical y diagonal

        for direccion in direcciones:
            for i in range(1, 8):
                nueva_fila = fila + direccion[0] * i
                nueva_columna = columna + direccion[1] * i

                if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:  # dentro del tablero
                    pieza = self.__tablero__[nueva_fila][nueva_columna]
                    if pieza is None:  # casilla vacía
                        movimientos.append((nueva_fila, nueva_columna))
                    elif pieza.color != self.color:  # pieza del oponente
                        movimientos.append((nueva_fila, nueva_columna))
                        break
                    else:  # pieza del mismo color
                        break
                else:  # fuera del tablero
                    break

        return movimientos

    def mover(self, fila, columna):
        if (fila, columna) not in self.movimientos_validos(self.__fila__, self.__columna__):
            raise InvalidMoveQueenMove()
        self.__fila__ = fila
        self.__columna__ = columna

    def __str__(self):
        return super().__str__()