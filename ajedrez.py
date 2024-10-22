from tablero import Tablero
from exceptions import GameOver

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = 'BLANCA'  # El turno inicial es de las piezas blancas
        self.__terminado__ = False
        self.__ganador__ = None

    def move(self, from_x, from_y, to_x, to_y):
        piece = self.__tablero__.get_piece(from_x, from_y)
        if piece and piece.color == self.__turno__:
            if piece.is_valid_move(from_x, from_y, to_x, to_y, self.__tablero__):
                self.__tablero__.mover_pieza(from_x, from_y, to_x, to_y)
                self.cambiar_turno()
                if self.is_terminado():
                    self.__ganador__ = self.obtener_ganador()
                return True
            else:
                print("Movimiento inválido.")
                return False
        else:
            print("No es el turno de esta pieza o no hay pieza en la posición inicial.")
            return False

    def cambiar_turno(self):
        self.__turno__ = 'NEGRA' if self.__turno__ == 'BLANCA' else 'BLANCA'

    def rendirse(self, color):
        self.__terminado__ = True
        self.__ganador__ = 'NEGRA' if color == 'BLANCA' else 'BLANCA'
        raise GameOver(f"El jugador con piezas {color} se ha rendido. El ganador es: {self.__ganador__}")

    def empate(self):
        self.__terminado__ = True
        self.__ganador__ = 'Empate'
        raise GameOver("El juego ha terminado en empate.")

    def is_terminado(self):
        # El juego termina si uno de los jugadores ha perdido todas sus piezas
        piezas_blancas = any(pieza for fila in self.__tablero__.__board__ for pieza in fila if pieza and pieza.color == 'BLANCA')
        piezas_negras = any(pieza for fila in self.__tablero__.__board__ for pieza in fila if pieza and pieza.color == 'NEGRA')
        return self.__terminado__ or not piezas_blancas or not piezas_negras

    def obtener_ganador(self):
        # El ganador es el jugador que aún tiene piezas en el tablero
        piezas_blancas = any(pieza for fila in self.__tablero__.__board__ for pieza in fila if pieza and pieza.color == 'BLANCA')
        piezas_negras = any(pieza for fila in self.__tablero__.__board__ for pieza in fila if pieza and pieza.color == 'NEGRA')
        if not piezas_blancas:
            return 'NEGRA'
        elif not piezas_negras:
            return 'BLANCA'
        return self.__ganador__