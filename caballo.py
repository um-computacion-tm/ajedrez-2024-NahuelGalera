from piezas import Pieza

class Caballo(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)
        self.posicion = None

    @property
    def blanca_str(self):
        return "♞"

    @property
    def negra_str(self):
        return "♘"

    def set_posicion(self, posicion):
        self.posicion = posicion

    def get_posicion(self):
        return self.posicion

    def mover(self, nueva_posicion):
        if self.is_valid_move(self.posicion[0], self.posicion[1], nueva_posicion[0], nueva_posicion[1], self.tablero):
            self.set_posicion(nueva_posicion)
            return True
        return False

    def is_valid_move(self, x1, y1, x2, y2, tablero):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            pieza_destino = tablero.get_piece(x2, y2)
            if pieza_destino is None or pieza_destino.color != self.color:
                return True
        return False