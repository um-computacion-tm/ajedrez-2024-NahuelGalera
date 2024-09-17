from piezas import Pieza

class Peon(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♙"

    @property
    def negra_str(self):
        return "♟"

    def mover(self, inicio_fila, inicio_col, final_fila, final_col, tablero):
        direction = 1 if self.color == 'BLANCA' else -1

        if inicio_col == final_col:  # Moving forward
            if inicio_fila + direction == final_fila:  # Moving forward one square
                if tablero.get_piece(final_fila, final_col) is not None:  # Check if the destination square is empty
                    return False
            elif inicio_fila + 2 * direction == final_fila and inicio_fila == (6 if self.color == 'NEGRA' else 1):  # Moving forward two squares
                if tablero.get_piece(inicio_fila + direction, inicio_col) is not None or tablero.get_piece(final_fila, final_col) is not None:  # Check if both destination squares are empty
                    return False
            else:
                return False
        elif abs(inicio_col - final_col) == 1 and inicio_fila + direction == final_fila:  # Capturing
            target_piece = tablero.get_piece(final_fila, final_col)
            if target_piece is None or target_piece.color == self.color:  # Check if the destination square contains an opponent's piece
                return False
        else:
            return False

        # Move the piece
        tablero.set_piece(final_fila, final_col, self)
        tablero.set_piece(inicio_fila, inicio_col, None)
        return True