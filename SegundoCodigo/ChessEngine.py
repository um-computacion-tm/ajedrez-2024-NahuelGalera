
class EstadoJuego():
    def __init__(self):
        # El tablero es 8x8 2D, 
        # las piezas negras están en minúsculas y las blancas en mayúsculas
        self.__tablero__ = [
            ["t", "c", "a", "q", "k", "a", "c", "t"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["T", "C", "A", "Q", "K", "A", "C", "T"]]
        self.__mueveBlanco = True
        self.__moveLog = []