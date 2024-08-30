from rey import Rey
from reina import Reina
from torre import Torre
from alfil import Alfil
from caballo import Caballo
from peon import Peon


class Tablero:
    def __init__(self):
        self.__tablero__ = self.crear_tablero()

    def crear_tablero(self):
        # Crear un tablero de 8x8 con todas las casillas vacías
        tablero = [[' ' for _ in range(8)] for _ in range(8)]

        # Colocar las piezas en sus posiciones iniciales
        # Aquí estamos usando instancias de las clases de piezas
        tablero[0] = [Torre('blanco'), Caballo('blanco'), Alfil('blanco'), Reina('blanco'), Rey('blanco'), Alfil('blanco'), Caballo('blanco'), Torre('blanco')]
        tablero[1] = [Peon('blanco') for _ in range(8)]
        tablero[6] = [Peon('negro') for _ in range(8)]
        tablero[7] = [Torre('negro'), Caballo('negro'), Alfil('negro'), Reina('negro'), Rey('negro'), Alfil('negro'), Caballo('negro'), Torre('negro')]

        return tablero

    def set_element(self, fila, columna, pieza):
        self.__tablero__[fila][columna] = pieza

    def imprimir_tablero(self):
        letras = 'abcdefgh'
        print(' ', ' '.join('\033[1m' + letra + '\033[0m' for letra in letras))
        for i, fila in enumerate(self.__tablero__, start=1):
            print(i, ' '.join(str(pieza) for pieza in fila))

    def get_pieza(self, x, y):
        return self.__tablero__[x][y]

    def __getitem__(self, coordinates):
        fila, col = coordinates
        return self.__tablero__[fila][col]

    def mover_pieza(self, inicio, fin):
        # Verificar que las coordenadas estén dentro del rango del tablero
        for coord in inicio + fin:
            if coord < 0 or coord > 7:
                print("Las coordenadas están fuera del rango del tablero.")
                return

        pieza = self.get_pieza(*inicio)
        if pieza == ' ':
            print("No hay ninguna pieza en la posición de inicio.")
            return
        if pieza.mover(*inicio, *fin, self):
            self.__tablero__[inicio[0]][inicio[1]] = ' '  # remove the piece from the start position
            self.__tablero__[fin[0]][fin[1]] = pieza  # place the piece at the end position
        else:
            print("Movimiento inválido")
        self.imprimir_tablero()  # print the board after moving the piece