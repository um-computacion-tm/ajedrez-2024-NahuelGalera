class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero

    @property
    def color(self):
        return self.__color__

    @property
    def tablero(self):
        return self.__tablero__

    def mover(self, inicio_fila, inicio_col, final_fila, final_col):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def is_valid_move(self, tablero, from_x, from_y, to_x, to_y):
        raise NotImplementedError("Este método debe ser implementado por las subclases")