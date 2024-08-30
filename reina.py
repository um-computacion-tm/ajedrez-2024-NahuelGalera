from pieza import Pieza

class Reina(Pieza):
    def __init__(self, color):
        super().__init__(color)

    def mover(self, inicio, final, tablero):
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final

        # Comprobar si el movimiento es horizontal, vertical o diagonal
        if inicio_fila == final_fila or inicio_col == final_col or abs(final_fila - inicio_fila) == abs(final_col - inicio_col):
            # Comprobar si el camino hasta la casilla final está despejado (no hay otras piezas en el camino)
            if inicio_fila == final_fila:  # Movimiento horizontal
                for col in range(min(inicio_col, final_col) + 1, max(inicio_col, final_col)):
                    if tablero.get_element(inicio_fila, col) != ' ':
                        return False
            elif inicio_col == final_col:  # Movimiento vertical
                for fila in range(min(inicio_fila, final_fila) + 1, max(inicio_fila, final_fila)):
                    if tablero.get_element(fila, inicio_col) != ' ':
                        return False
            else:  # Movimiento diagonal
                fila, col = inicio_fila, inicio_col
                fila_step = 1 if final_fila > inicio_fila else -1
                col_step = 1 if final_col > inicio_col else -1
                fila += fila_step
                col += col_step
                while fila != final_fila and col != final_col:
                    if tablero.get_element(fila, col) != ' ':
                        return False
                    fila += fila_step
                    col += col_step

            # Comprobar si la casilla final está vacía o contiene una pieza del oponente
            target_piece = tablero.get_element(final_fila, final_col)
            if target_piece != ' ' and target_piece.color == self.__color__:
                return False

            return True

        return False