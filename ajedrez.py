from tablero import Tablero

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = 'blanco'

    def cambiar_turno(self):
        self.__turno__ = 'negro' if self.__turno__ == 'blanco' else 'blanco'

    def es_movimiento_valido(self, inicio, fin):
        # Check if the move is within the bounds of the board
        if not (0 <= inicio[0] < 8 and 0 <= inicio[1] < 8 and 0 <= fin[0] < 8 and 0 <= fin[1] < 8):
            return False

        # Check if the piece being moved belongs to the current player
        pieza = self.__tablero__.get_pieza(*inicio)
        if (self.__turno__ == 'blanco' and pieza.isupper()) or (self.__turno__ == 'negro' and pieza.islower()):
            return False

        # TODO: Check if the move is valid according to the rules of the game for that piece

        return True
    
    def mover_pieza(self, inicio, fin):
        if not self.es_movimiento_valido(inicio, fin):
            print("Invalid move")
            return

        self.__tablero__.mover_pieza(inicio, fin)
        self.cambiar_turno()

    def verificar_victoria(self):
        # Aquí deberías agregar la lógica para verificar si un jugador ha ganado
        # Por ejemplo, puedes verificar si el rey del jugador contrario está en jaque mate
        pass

    def jugar(self):
        while True:
            self.__tablero__.imprimir_tablero()
            print(f"Turno de las piezas {self.__turno__}")

            # Aquí deberías agregar la lógica para obtener el movimiento del jugador
            # Por ejemplo, puedes pedirle al usuario que introduzca las posiciones inicial y final
            inicio = self.obtener_posicion()
            fin = self.obtener_posicion()
            self.mover_pieza(inicio, fin)
            if self.verificar_victoria():
                print(f"Las piezas {self.__turno__} han ganado!")
                break
    def obtener_posicion(self):
        fila = int(input("Enter the row: "))
        columna = input("Enter the column: ").lower()
        columna = ord(columna) - ord('a')  # Convert the column from a letter to a number
        return fila, columna

ajedrez = Ajedrez()
ajedrez.jugar()
