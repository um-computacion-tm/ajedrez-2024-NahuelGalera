from piezas import Pieza
from exceptions import InvalidMoveSpecific as InvalidMoveBishopMove

class Alfil(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♝"

    @property
    def negra_str(self):
        return "♗"

    def __str__(self):
        return 'B' if self.__color__ == 'BLANCA' else 'b'

    def possible_moves(self, from_row, from_col):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return super().possible_moves_general(from_row, from_col, directions)

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        """
        Verifica si el movimiento del alfil desde la posición inicial hasta la posición final es válido.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        if dx == dy:
            # Verificar si hay piezas en el camino
            step_fila = 1 if to_fila > from_fila else -1
            step_col = 1 if to_col > from_col else -1

            current_fila, current_col = from_fila + step_fila, from_col + step_col
            while current_fila != to_fila or current_col != to_col:
                if tablero.get_piece(current_fila, current_col) is not None:
                    return False
                current_fila += step_fila
                current_col += step_col

            # Verificar si la posición final está vacía o tiene una pieza del color opuesto
            final_piece = tablero.get_piece(to_fila, to_col)
            return final_piece is None or final_piece.color != self.__color__
        return False

    def mover(self, tablero, inicio, final):
        """
        Mueve el alfil desde la posición de inicio hasta la posición final en el tablero dado.
        El alfil se puede mover en cualquier dirección de forma diagonal.
        """
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final

        # Verificar movimiento diagonal y que no haya piezas de por medio
        if not self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, tablero):
            raise InvalidMoveBishopMove("Movimiento inválido: Hay una pieza en el camino o el movimiento no es diagonal")

        # Mover la pieza
        tablero.set_piece(final_fila, final_col, self)
        tablero.set_piece(inicio_fila, inicio_col, None)