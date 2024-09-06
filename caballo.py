from pieza import Pieza

class Caballo(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)
        self.__blanca_str__= "CB"
        self.__negra_str__= "CN"
        self.__posicion__ = None

    def set_posicion(self, posicion):
        self.__posicion__ = posicion

    def mover(self, nueva_posicion):
        dx = abs(nueva_posicion[0] - self.__posicion__[0])
        dy = abs(nueva_posicion[1] - self.__posicion__[1])

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            self.__posicion__ = nueva_posicion
            print("Movimiento válido")
        else:
            print("Movimiento inválido")

    def __str__(self):
        return super().__str__()