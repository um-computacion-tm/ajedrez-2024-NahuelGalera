from tablero import Tablero
from exceptions import InvalidMove

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCA"

    def is_jugando(self):
        return True

    def move(self, from_fila, from_col, to_fila, to_col):
        # validate coordenadas
        piece = self.__tablero__.get_pieza(from_fila, from_col)
        if not piece.valid_positions(from_fila, from_col, to_fila, to_col):
            raise InvalidMove()
        self.__tablero__.mover_pieza(from_fila, from_col, to_fila, to_col)
        self.cambiar_turno()


    @property
    def turno(self):
        return self.__turno__

    def mostrar_tablero(self):
        return str(self.__tablero__)

    def cambiar_turno(self):
        if self.__turno__ == "BLANCA":
            self.__turno__ = "NEGRA"
        else:
            self.__turno__ = "BLANCA"