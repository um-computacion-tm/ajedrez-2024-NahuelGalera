from tablero import Tablero
from exceptions import InvalidMove

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCA"
        self.__rendicion__ = None  # Variable para rastrear si un jugador se ha rendido
        self.__ganador__ = None  # Variable para almacenar el ganador

    def is_jugando(self):
        return not self.is_game_over()

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

    def rendirse(self):
        self.__rendicion__ = self.__turno__
        self.__ganador__ = "NEGRA" if self.__turno__ == "BLANCA" else "BLANCA"

    def is_rendicion(self):
        return self.__rendicion__ is not None

    def is_game_over(self):
        if self.is_rendicion():
            return True
        if self.__tablero__.no_pieces_left("BLANCA") or self.__tablero__.no_pieces_left("NEGRA"):
            return True
        return False

    @property
    def ganador(self):
        return self.__ganador__