from piezas import Pieza

class Rey(Pieza):
    def __init__(self, color, board):
            super().__init__(color, board)

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