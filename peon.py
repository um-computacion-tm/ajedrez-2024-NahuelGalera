from piezas import Pieza

class Peon(Pieza):
    def __init__(self, color, board):
            super().__init__(color, board)

    @property
    def blanca_str(self):
        return "♙"

    @property
    def negra_str(self):
        return "♟"

    def mover(self, inicio_fila, inicio_col, final_fila, final_col, tablero):
        direction = 1 if self.__color__ == 'BLANCA' else -1

        if inicio_col == final_col:  # Moving forward
            if inicio_fila + direction == final_fila:  # Moving forward one square
                if tablero.get_element(final_fila, final_col) != ' ':  # Check if the destination square is empty
                    return False
            elif inicio_fila + 2 * direction == final_fila and inicio_fila == (6 if self.__color__ == 'NEGRA' else 1):  # Moving forward two squares
                if tablero.get_element(inicio_fila + direction, inicio_col) != ' ' or tablero.get_element(final_fila, final_col) != ' ':  # Check if both destination squares are empty
                    return False
            else:
                return False
        elif abs(inicio_col - final_col) == 1 and inicio_fila + direction == final_fila:  # Capturing
            target_piece = tablero.get_element(final_fila, final_col)
            if target_piece == ' ' or target_piece.color == self.__color__:  # Check if the destination square contains an opponent's piece
                return False
        else:
            return False

        return True
    
    def valid_positions(self, from_fila, from_col, to_fila, to_col):
        if self.__color__ == "BLANCA":
            if from_fila == 1:
                return (to_fila == from_fila + 1 or to_fila == from_fila + 2) and from_col == to_col
            else:
                return to_fila == from_fila + 1 and from_col == to_col
        else:
            if from_fila == 6:
                return (to_fila == from_fila - 1 or to_fila == from_fila - 2) and from_col == to_col
            else:
                return to_fila == from_fila - 1 and from_col == to_col