from pieza import Pieza

class Alfil(Pieza):
    def __init__(self, color):
        self.__color__ = color

    def mover(self, tablero, inicio, final):
        """
        Mueve el alfil desde la posición de inicio hasta la posición final en el tablero dado.
        El alfil se puede mover en cualquier dirección de forma diagonal.
        """
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final

        # Verificar movimiento diagional
        if abs(inicio_fila - final_fila) != abs(inicio_col - final_col):
            return False

        # Verificar que no haya piezas de por medio
        fila_paso = 1 if final_fila > inicio_fila else -1
        col_paso = 1 if final_col > inicio_col else -1

        fila_actual, col_actual = inicio_fila + fila_paso, inicio_col + col_paso
        while fila_actual != final_fila and col_actual != final_col:
            if tablero[fila_actual][col_actual] != ' ':
                return False
            fila_actual, col_actual = fila_actual + fila_paso, col_actual + col_paso

        return True