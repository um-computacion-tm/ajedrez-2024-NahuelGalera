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

        return True

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        """
        Verifica si el movimiento del alfil desde la posición inicial hasta la posición final es válido.
        """
        # Movimiento diagonal
        if abs(from_fila - to_fila) != abs(from_col - to_col):
            return False

        # Verificar que no haya piezas de por medio
        fila_paso = 1 if to_fila > from_fila else -1
        col_paso = 1 if to_col > from_col else -1

        fila_actual, col_actual = from_fila + fila_paso, from_col + col_paso
        while fila_actual != to_fila and col_actual != to_col:
            if tablero.get_piece(fila_actual, col_actual) is not None:
                return False
            fila_actual, col_actual = fila_actual + fila_paso, col_actual + col_paso

        # Verificar si la posición de destino tiene una pieza del mismo color
        target_piece = tablero.get_piece(to_fila, to_col)
        if target_piece is not None and target_piece.color == self.color:
            return False

        return True

if __name__ == "__main__":
    pass