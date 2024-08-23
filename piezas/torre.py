from codigo_ajedrez.pieza import Pieza

class Torre(Pieza):
    def mover(self, inicio, final):
        # A rook can move any number of squares along a rank or file
        # So, either the fila or the column must remain the same
        inicio_fila, inicio_col = inicio
        final_fila, final_col = final
        if inicio_fila == final_fila or inicio_col == final_col:
            return True
        else:
            return False