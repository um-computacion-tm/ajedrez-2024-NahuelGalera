from piezas import Pieza

class Rey(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♔"

    @property
    def negra_str(self):
        return "♚"

    def mover(self, inicio, final):
        # El rey se puede mover en cualquier direccion de a 1 lugar
        dx = abs(final[0] - inicio[0])
        dy = abs(final[1] - inicio[1])
        return dx <= 1 and dy <= 1

    def valid_positions(self, from_fila, from_col, to_fila, to_col):
        """
        Verifica si el movimiento del rey desde la posición inicial hasta la posición final es válido.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        return dx <= 1 and dy <= 1