from piezas import Pieza

class Torre(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♜"

    @property
    def negra_str(self):
        return "♖"

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        # Verificar si el movimiento es en línea recta (vertical u horizontal)
        if from_fila != to_fila and from_col != to_col:
            return False

        # Calcular los pasos para iterar a través de las posiciones intermedias
        step_fila = 0 if from_fila == to_fila else (1 if to_fila > from_fila else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)

        # Iterar a través de las posiciones intermedias
        current_fila, current_col = from_fila + step_fila, from_col + step_col
        while current_fila != to_fila or current_col != to_col:
            if tablero.get_piece(current_fila, current_col) is not None:
                return False
            current_fila += step_fila
            current_col += step_col

        # Verificar si la posición de destino tiene una pieza del mismo color
        target_piece = tablero.get_piece(to_fila, to_col)
        if target_piece is not None and target_piece.color == self.color:
            return False

        return True

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        # Verificar si la posición final es válida
        if not self.is_valid_move(inicio_fila, inicio_col, final_fila, final_col, self.tablero):
            return False

        # Mover la pieza
        self.tablero.set_piece(final_fila, final_col, self)
        self.tablero.set_piece(inicio_fila, inicio_col, None)

        return True

if __name__ == "__main__":
    pass