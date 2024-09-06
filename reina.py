from pieza import Pieza

class Reina(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)
        self.__blanca_str__ = "RB"
        self.__negra_str__ = "RN"

    def mover(self):
        print("La reina se puede mover en cualquier direccion")

    def __str__(self):
        return super().__str__()