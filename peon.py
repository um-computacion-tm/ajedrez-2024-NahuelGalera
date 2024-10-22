from piezas import Pieza

class Peon(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♟"
    
    @property
    def negra_str(self):
        return "♙"

    def __str__(self):
        return 'P' if self.__color__ == 'BLANCA' else 'p'

    def possible_moves(self, row, col):
        moves = []
        direction = -1 if self.__color__ == 'BLANCA' else 1
        start_row = 6 if self.__color__ == 'BLANCA' else 1

        # Forward move
        if self.__tablero__.is_empty(row + direction, col):
            moves.append((row + direction, col))
            if row == start_row and self.__tablero__.is_empty(row + 2 * direction, col):
                moves.append((row + 2 * direction, col))

        # Diagonal moves for capturing
        if col > 0 and not self.__tablero__.is_empty(row + direction, col - 1) and self.__tablero__.get_piece(row + direction, col - 1).color != self.__color__:
            moves.append((row + direction, col - 1))
        if col < 7 and not self.__tablero__.is_empty(row + direction, col + 1) and self.__tablero__.get_piece(row + direction, col + 1).color != self.__color__:
            moves.append((row + direction, col + 1))

        return moves

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        if self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, self.__tablero__):
            self.__tablero__.set_piece(final_fila, final_col, self)
            self.__tablero__.set_piece(inicio_fila, inicio_col, None)
            return True
        return False

    def is_valid_move(self, from_x, from_y, to_x, to_y, tablero):
        direction = -1 if self.__color__ == 'BLANCA' else 1

        # One square forward
        if to_x == from_x + direction and to_y == from_y:
            return tablero.is_empty(to_x, to_y)

        # Two squares forward from the starting position
        start_row = 6 if self.__color__ == 'BLANCA' else 1
        if from_x == start_row and to_x == from_x + 2 * direction and to_y == from_y:
            return tablero.is_empty(to_x, to_y) and tablero.is_empty(from_x + direction, from_y)

        # Diagonal capture
        if to_x == from_x + direction and abs(to_y - from_y) == 1:
            return not tablero.is_empty(to_x, to_y) and tablero.get_piece(to_x, to_y).color != self.__color__

        return False