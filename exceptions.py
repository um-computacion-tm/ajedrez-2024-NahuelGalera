
class InvalidMove(Exception):
    def __init__(self, message="Movimiento inválido"):
        self.__message__ = message
        super().__init__(self.__message__)

    def __str__(self):
        return f'{self.__message__}'


class InvalidMoveNoPiece(InvalidMove):
    def __init__(self, message="Movimiento inválido: No hay pieza en la posición inicial"):
        super().__init__(message)

class InvalidMoveRookMove(InvalidMove):
    ...

