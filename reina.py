from piezas import Pieza
from exceptions import InvalidMoveQueenMove

class Reina(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♕"

    @property
    def negra_str(self):
        return "♛"

    def mover(self, fila, columna):
        if (fila, columna) not in self.valid_positions(self.__fila__, self.__columna__):
            raise InvalidMoveQueenMove()
        self.__fila__ = fila
        self.__columna__ = columna

    def valid_positions(self, from_fila, from_col, to_fila, to_col):
        """
        Verifica si el movimiento de la reina desde la posición inicial hasta la posición final es válido.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        if dx == dy or from_fila == to_fila or from_col == to_col:
            fila_paso = 1 if to_fila > from_fila else -1 if to_fila < from_fila else 0
            col_paso = 1 if to_col > from_col else -1 if to_col < from_col else 0

            fila_actual, col_actual = from_fila + fila_paso, from_col + col_paso
            while fila_actual != to_fila or col_actual != to_col:
                if self.__tablero__.get_piece(fila_actual, col_actual) is not None:
                    return False
                fila_actual += fila_paso
                col_actual += col_paso

            return True
        return False

    def __str__(self):
        return super().__str__()