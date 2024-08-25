from pieza import Pieza

class Rey(Pieza):

    def mover(self, inicio, final):
        # El rey se puede mover en cualquier direccion de a 1 lugar
        dx = abs(final[0] - inicio[0])
        dy = abs(final[1] - inicio[1])
        return dx <= 1 and dy <= 1