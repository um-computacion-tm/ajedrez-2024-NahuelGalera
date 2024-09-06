
class InvalidMove(Exception):
    def __init__(self, message="Movimiento inválido"):
        self.__message__ = message
        super().__init__(self.__message__)
    def __str__(self):
        return f'{self.__message__}'


class InvalidMoveNoPiece(InvalidMove):
    def __init__(self, message="Movimiento inválido: No hay pieza en la posición inicial"):
        super().__init__(message)

# PEON
class InvalidMovePawnMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: El peón se mueve hacia adelante"):
        super().__init__(message)

# TORRE
class InvalidMoveRookMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: La torre se mueve en línea recta horizontal o vertical"):
        super().__init__(message)

# REY
class InvalidMoveKingMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: El rey se puede mover una casilla en cualquier dirección"):
        super().__init__(message)

# CABALLO
class InvalidMoveKnightMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: El caballo se mueve en forma de L"):
        super().__init__(message)

# ALFIL
class InvalidMoveBishopMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: El alfil se mueve en diagonal"):
        super().__init__(message)

# REINA
class InvalidMoveQueenMove(InvalidMove):
    def __init__(self, message="Movimiento inválido: La reina se puede mover en cualquier dirección"):
        super().__init__(message)

# JAQUE
class InvalidMoveCheck(InvalidMove):
    def __init__(self, message="Movimiento inválido: Estás en jaque"):
        super().__init__(message)

# JAQUE MATE
class InvalidMoveCheckmate(InvalidMove):
    def __init__(self, message="Movimiento inválido: Estás en jaque mate"):
        super().__init__(message)

