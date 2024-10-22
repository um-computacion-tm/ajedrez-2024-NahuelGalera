from piezas import Pieza

class Rey(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♚"

    @property
    def negra_str(self):
        return "♔"

    def __str__(self):
        return 'K' if self.__color__ == 'BLANCA' else 'k'

    def possible_moves(self, from_row, from_col):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        return super().possible_moves_general(from_row, from_col, directions, single_step=True)

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        """
        Verifica si el movimiento del rey desde la posición inicial hasta la posición final es válido.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        if max(dx, dy) == 1:
            # Verificar si la posición final está vacía o tiene una pieza del color opuesto
            final_piece = tablero.get_piece(to_fila, to_col)
            return final_piece is None or final_piece.color != self.__color__
        return False

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        if self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, self.__tablero__):
            self.__tablero__.set_piece(final_fila, final_col, self)
            self.__tablero__.set_piece(inicio_fila, inicio_col, None)
            return True
        return False