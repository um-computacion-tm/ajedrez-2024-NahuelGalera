from piezas import Pieza

class Torre(Pieza):
    def __init__(self, color, board):
            super().__init__(color, board)

    @property
    def blanca_str(self):
        return "♖"

    @property
    def negra_str(self):
        return "♜"


    def valid_posiciones(self,from_fila,from_col,to_fila,to_col):
            posibles_posiciones = (
                self.posibles_posiciones_vd(from_fila, from_col) +
                self.posibles_posiciones_va(from_fila, from_col)
            )
            return (to_fila, to_col) in posibles_posiciones

    def posibles_posiciones_vd(self, fila, col):
        posibles = []
        for next_fila in range(fila + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_fila, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    posibles.append((next_fila, col))
                break
            posibles.append((next_fila, col))
        return posibles

    def posibles_posiciones_va(self, fila, col):
        posibles = []
        for next_fila in range(fila - 1, -1, -1):
            posibles.append((next_fila, col))
        return posibles