

class Tablero:
    def __init__(self):
        self.__tablero__ = self.crear_tablero()

    def crear_tablero(self):
        # Logic to create the board
        pass
        # Crear un tablero de 8x8 con todas las casillas vacías
        tablero = [[' ' for _ in range(8)] for _ in range(8)]

        # Colocar las piezas en sus posiciones iniciales
        # Aquí solo estamos usando caracteres para representar las piezas,
        # pero en un programa real probablemente querrías usar instancias de las clases de piezas
        tablero[0] = ['T', 'C', 'A', 'Q', 'K', 'A', 'C', 'T']
        tablero[1] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
        tablero[6] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
        tablero[7] = ['t', 'c', 'a', 'q', 'k', 'a', 'c', 't']

        return tablero
        
        
    def imprimir_tablero(self):
        letras = 'abcdefgh'
        print(' ', ' '.join('\033[1m' + letra + '\033[0m' for letra in letras))
        for i, fila in enumerate(self.__tablero__, start=1):
            print(i, ' '.join(fila))

    def get_pieza(self, x, y):
        # Logic to get a piece at the given coordinates
        return self.__tablero__[x][y]
    

tablero = Tablero()
tablero.imprimir_tablero()

