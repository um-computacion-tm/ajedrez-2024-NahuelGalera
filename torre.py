from pieza import Pieza
from tablero import tablero

class Torre(Pieza):
    def mover(self, inicio, final):
        # La torre se puede mover en cualquier direccion de forma recta
        # Asique fila o columna deben ser iguales a la posicion anterior
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final

        # Verificar que el movimiento es en línea recta
        if inicio_fila != final_fila and inicio_col != final_col:
            return False

        # Verificar que no hay otras piezas en el camino
        if inicio_fila == final_fila:  # Movimiento horizontal
            col_paso = 1 if final_col > inicio_col else -1
            for col_actual in range(inicio_col + col_paso, final_col, col_paso):
                if tablero[inicio_fila][col_actual] != ' ':
                    return False
        else:  # Movimiento vertical
            fila_paso = 1 if final_fila > inicio_fila else -1
            for fila_actual in range(inicio_fila + fila_paso, final_fila, fila_paso):
                if tablero[fila_actual][inicio_col] != ' ':
                    return False

        return True