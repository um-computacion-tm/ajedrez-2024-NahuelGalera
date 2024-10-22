from torre import Torre
from caballo import Caballo
from alfil import Alfil
from reina import Reina
from rey import Rey
from peon import Peon


class Tablero:
    def __init__(self):
        self.__board__ = [[None for _ in range(8)] for _ in range(8)]
        self.inicializar_piezas()

    def inicializar_piezas(self):
        piezas = [Torre, Caballo, Alfil, Reina, Rey, Alfil, Caballo, Torre]
        for i, pieza in enumerate(piezas):
            self.__board__[0][i] = pieza('NEGRA', self)
            self.__board__[1][i] = Peon('NEGRA', self)
        for i, pieza in enumerate(piezas):
            self.__board__[7][i] = pieza('BLANCA', self)
            self.__board__[6][i] = Peon('BLANCA', self)

    def is_empty(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.__board__[x][y] is None
        else:
            raise IndexError("Coordenadas fuera del rango del tablero")

    def get_piece(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.__board__[x][y]
        else:
            raise IndexError("Coordenadas fuera del rango del tablero")

    def set_piece(self, x, y, piece):
        if 0 <= x < 8 and 0 <= y < 8:
            self.__board__[x][y] = piece
        else:
            raise IndexError("Coordenadas fuera del rango del tablero")

    def is_enemy(self, x, y, color):
        piece = self.get_piece(x, y)
        return piece is not None and piece.color != color

    def sin_fichas(self, color):
        for row in self.__board__:
            for piece in row:
                if piece and piece.color == color:
                    return False
        return True

    def mover_pieza(self, from_x, from_y, to_x, to_y):
        pieza = self.get_piece(from_x, from_y)
        if pieza:
            print(f"Intentando mover {pieza} de ({from_x}, {from_y}) a ({to_x}, {to_y})")
            if pieza.is_valid_move(from_x, from_y, to_x, to_y, self):
                self.set_piece(to_x, to_y, pieza)
                self.set_piece(from_x, from_y, None)
                print(f"Movimiento exitoso de {pieza} a ({to_x}, {to_y})")
                return True
            else:
                print(f"Movimiento inválido para {pieza} de ({from_x}, {from_y}) a ({to_x}, {to_y})")
        else:
            print(f"No hay pieza en la posición inicial ({from_x}, {from_y})")
        raise ValueError("Movimiento inválido")