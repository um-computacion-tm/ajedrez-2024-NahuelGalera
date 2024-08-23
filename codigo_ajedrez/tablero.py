from piezas.torre import Torre

class Tablero:
    def __init__(self, posiciones):
        self.__posiciones__ = posiciones

    def dibujar(self):
        for i in range(8):
            for j in range(8):
                pieza = self.__posiciones__[i][j]
                if pieza is None:
                    # Imprime una casilla vacía
                    print("□", end="")
                else:
                    # Imprime la pieza
                    print(pieza, end="")
            print()  # Nueva línea al final de cada fila

# Ejemplo de uso:
posiciones = [
    ["T", "C", "A", "Q", "K", "A", "C", "T"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["t", "c", "a", "q", "k", "a", "c", "t"],
]
tablero = Tablero(posiciones)
tablero.dibujar()

    
