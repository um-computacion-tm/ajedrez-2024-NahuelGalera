from tablero import Tablero

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = 'blanco'

    def cambiar_turno(self):
        self.__turno__ = 'negro' if self.__turno__ == 'blanco' else 'blanco'

    def mover_pieza(self, inicio, fin):
        # Aquí deberías agregar validaciones para asegurarte de que el movimiento es legal
        # Por ejemplo, verificar que la pieza en la posición inicial es del color correcto,
        # que la pieza puede moverse a la posición final, que el rey no queda en jaque, etc.
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
        # Aquí deberías agregar la lógica para obtener una posición del usuario
        # Por ejemplo, puedes pedirle al usuario que introduzca una fila y una columna
        pass

ajedrez = Ajedrez()
ajedrez.jugar()
