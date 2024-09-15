from piezas import Pieza
from exceptions import InvalidMoveKnightMove

class Caballo(Pieza):
    def __init__(self, color, board):
            super().__init__(color, board)

    @property
    def blanca_str(self):
        return "♘"

    @property
    def negra_str(self):
        return "♞"

    def set_posicion(self, posicion):
        self.__posicion__ = posicion

    def get_posicion(self):
        return self.__posicion__

    def mover(self, nueva_posicion):
        dx = abs(nueva_posicion[0] - self.__posicion__[0])
        dy = abs(nueva_posicion[1] - self.__posicion__[1])

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            self.__posicion__ = nueva_posicion
        else:
            raise InvalidMoveKnightMove()

    def __str__(self):
        return super().__str__()