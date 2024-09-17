from piezas import Pieza
from reina import Reina
from torre import Torre
from alfil import Alfil
from caballo import Caballo

class Peon(Pieza):
    @property
    def blanca_str(self):
        return "♙"

    @property
    def negra_str(self):
        return "♟"

    def mover(self, inicio_fila, inicio_col, final_fila, final_col, tablero):
        if not self.valid_positions(inicio_fila, inicio_col, final_fila, final_col, tablero):
            return False

        # Move the piece
        tablero.set_piece(final_fila, final_col, self)
        tablero.set_piece(inicio_fila, inicio_col, None)

        # Check for promotion
        if final_fila == 0 or final_fila == 7:
            self.promocionar(tablero, final_fila, final_col)

        return True

    def promocionar(self, tablero, fila, col):
        # Permitir al jugador elegir la pieza de promoción
        print("Elige una pieza para la promoción (Q, R, B, N): ")
        eleccion = input().upper()
        if eleccion == 'Q':
            pieza_promocionada = Reina(self.__color__, tablero)
        elif eleccion == 'R':
            pieza_promocionada = Torre(self.__color__, tablero)
        elif eleccion == 'B':
            pieza_promocionada = Alfil(self.__color__, tablero)
        elif eleccion == 'N':
            pieza_promocionada = Caballo(self.__color__, tablero)
        else:
            print("Elección inválida. Promocionando a Reina por defecto.")
            pieza_promocionada = Reina(self.__color__, tablero)

        tablero.set_piece(fila, col, pieza_promocionada)

    def valid_positions(self, inicio_fila, inicio_col, final_fila, final_col, tablero):
        direction = 1 if self.__color__ == 'BLANCA' else -1

        if inicio_col == final_col:  # Moving forward
            if inicio_fila + direction == final_fila:  # Moving forward one square
                if tablero.get_piece(final_fila, final_col) is not None:  # Check if the destination square is empty
                    return False
            elif inicio_fila + 2 * direction == final_fila and inicio_fila == (6 if self.__color__ == 'NEGRA' else 1):  # Moving forward two squares
                if tablero.get_piece(inicio_fila + direction, inicio_col) is not None or tablero.get_piece(final_fila, final_col) is not None:  # Check if both destination squares are empty
                    return False
        else:  # Capturing diagonally
            if abs(inicio_col - final_col) == 1 and inicio_fila + direction == final_fila:
                if tablero.get_piece(final_fila, final_col) is None or tablero.get_piece(final_fila, final_col).color == self.__color__:
                    return False

        return True