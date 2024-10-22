from piezas import Pieza

class Rey(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♚"

    @property
    def negra_str(self):
        return "♔"

    def mover(self, inicio, final):
        # El rey se puede mover en cualquier direccion de a 1 lugar
        dx = abs(final[0] - inicio[0])
        dy = abs(final[1] - inicio[1])
        return dx <= 1 and dy <= 1

    def is_valid_move(self, from_fila, from_col, to_fila, to_col, tablero):
        """
        Verifica si el movimiento del rey es válido, considerando el estado del tablero.
        """
        dx = abs(to_fila - from_fila)
        dy = abs(to_col - from_col)
        
        # Verifica si el movimiento es de un cuadro en cualquier dirección
        if dx > 1 or dy > 1:
            return False

        # Verifica si la posición final está ocupada por una pieza del mismo color
        pieza_destino = tablero.get_piece(to_fila, to_col)
        if pieza_destino and pieza_destino.color == self.color:
            return False

        return True