from tablero import Tablero
from exceptions import InvalidMove, InvalidPlayer, GameOver

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCA"
        self.__rendicion__ = None  # Variable para rastrear si un jugador se ha rendido
        self.__ganador__ = None  # Variable para almacenar el ganador
        self.__historial__ = []  # Historial de movimientos

    def is_jugando(self):
        return not self.is_game_over()

    def move(self, from_fila, from_col, to_fila, to_col):
        piece = self.__tablero__.get_piece(from_fila, from_col)
        if piece is None:
            raise InvalidMove("No hay pieza en la posición inicial.")
        if piece.color != self.__turno__:
            raise InvalidPlayer(f"Movimiento inválido: es el turno de las piezas {self.__turno__}.")
        if not piece.valid_positions(from_fila, from_col, to_fila, to_col):
            raise InvalidMove("Movimiento inválido según la pieza.")
        
        self.__tablero__.mover_pieza(from_fila, from_col, to_fila, to_col)
        self.__historial__.append(((from_fila, from_col), (to_fila, to_col)))
        
        self.__cambiar_turno()
        print(f"Turno cambiado a: {self.__turno__}")
        
        # Check for game-over conditions
        if self.is_game_over():
            raise GameOver(f"El jugador con piezas {self.__turno__} ha perdido.")

    @property
    def turno(self):
        return self.__turno__

    def mostrar_tablero(self):
        return str(self.__tablero__)

    def __cambiar_turno(self):
        self.__turno__ = "NEGRA" if self.__turno__ == "BLANCA" else "BLANCA"

    def rendirse(self):
        self.__rendicion__ = self.__turno__
        self.__ganador__ = "NEGRA" if self.__turno__ == "BLANCA" else "BLANCA"
        raise GameOver(f"El jugador con piezas {self.__turno__} se ha rendido.")

    def is_rendicion(self):
        return self.__rendicion__ is not None

    def is_game_over(self):
        if self.is_rendicion() and (self.__tablero__.no_pieces_left("BLANCA") or self.__tablero__.no_pieces_left("NEGRA")):
            self.__ganador__ = "NEGRA" if self.__tablero__.no_pieces_left("BLANCA") else "BLANCA"
            return True
        return False

    def reiniciar(self):
        self.__init__()

    @property
    def ganador(self):
        return self.__ganador__

    @property
    def historial(self):
        return self.__historial__