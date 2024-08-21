from codigo_ajedrez.piezas import Pieza

class Peon(Pieza):
    def mover(self):
        print("El peon se mueve de a 1 hacia adelante, y come de a 1 en diagonal")