from codigo_ajedrez.pieza import Pieza

class Alfil(Pieza):
    def mover(self, inicio, final):
        # A bishop can move any number of squares diagonally
        # So, the absolute difference between the inicio and final filas
        # must be equal to the absolute difference between the inicio and final columns
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final
        if abs(inicio_fila - final_fila) == abs(inicio_col - final_col):
            return True
        else:
            return False