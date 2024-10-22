from piezas import Pieza

class Reina(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♛"

    @property
    def negra_str(self):
        return "♕"

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        if self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, self.__tablero__):
            self.__tablero__.set_piece(final_fila, final_col, self)
            self.__tablero__.set_piece(inicio_fila, inicio_col, None)
            return True
        return False

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        """
        Verifica si el movimiento de la reina desde la posición inicial hasta la posición final es válido.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        if dx == dy or from_fila == to_fila or from_col == to_col:
            fila_paso = 1 if to_fila > from_fila else -1 if to_fila < from_fila else 0
            col_paso = 1 if to_col > from_col else -1 if to_col < from_col else 0

            fila_actual, col_actual = from_fila + fila_paso, from_col + col_paso
            while fila_actual != to_fila or col_actual != to_col:
                if tablero.get_piece(fila_actual, col_actual) is not None:
                    return False
                fila_actual += fila_paso
                col_actual += col_paso

            # Verificar si la posición final tiene una pieza enemiga
            pieza_destino = tablero.get_piece(to_fila, to_col)
            if pieza_destino is None or pieza_destino.color != self.color:
                return True
        return False