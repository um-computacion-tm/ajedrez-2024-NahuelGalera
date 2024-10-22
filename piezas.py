class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero
        self.__reina_rey_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
        self.__torre_directions__ = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.__alfil_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

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

    def possible_moves_general(self, from_row, from_col, directions, single_step=False):
        moves = []
        for direction in directions:
            new_row, new_col = from_row, from_col
            while True:
                new_row += direction[0]
                new_col += direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))
                    if single_step:
                        break
                else:
                    break
        return moves