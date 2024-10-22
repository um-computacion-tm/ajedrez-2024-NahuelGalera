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

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        if self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, self.__tablero__):
            self.__tablero__.set_piece(final_fila, final_col, self)
            self.__tablero__.set_piece(inicio_fila, inicio_col, None)
            return True
        return False

    def is_valid_move(self, from_x, from_y, to_x, to_y, tablero):
        direction = -1 if self.color == 'BLANCA' else 1

        # One square forward
        if to_x == from_x + direction and to_y == from_y:
            return tablero.is_empty(to_x, to_y)

        # Two squares forward on initial move
        if (self.color == 'BLANCA' and from_x == 6) or (self.color == 'NEGRA' and from_x == 1):
            if to_x == from_x + 2 * direction and to_y == from_y:
                return tablero.is_empty(to_x, to_y) and tablero.is_empty(from_x + direction, to_y)

        # Capture moves
        if to_x == from_x + direction and (to_y == from_y - 1 or to_y == from_y + 1):
            return tablero.is_enemy(to_x, to_y, self.color)

        return False