class InvalidMove(Exception):
    def __init__(self, message="Movimiento inválido"):
        self.__message__ = message
        super().__init__(self.__message__)
    def __str__(self):
        return f'{self.__message__}'

class InvalidPiece(Exception):
    def __init__(self, message="Movimiento inválido: Pieza incorrecta"):
        self.__message__ = message
        super().__init__(self.__message__)
    def __str__(self):
        return f'{self.__message__}'

class InvalidPlayer(Exception):
    def __init__(self, message="Movimiento inválido: Jugador incorrecto"):
        self.__message__ = message
        super().__init__(self.__message__)
    def __str__(self):
        return f'{self.__message__}'

class InvalidMoveNoPiece(InvalidMove):
    def __init__(self, message="Movimiento inválido: No hay pieza en la posición inicial"):
        super().__init__(message)

class InvalidMoveSpecific(InvalidMove):
    def __init__(self, message):
        super().__init__(message)

# GAME OVER
class GameOver(Exception):
    def __init__(self, message="Juego terminado"):
        self.__message__ = message
        super().__init__(self.__message__)
    def __str__(self):
        return f'{self.__message__}'