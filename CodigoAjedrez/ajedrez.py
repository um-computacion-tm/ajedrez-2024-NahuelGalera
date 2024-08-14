from tablero import Tablero

class Ajedrez:
    def __init__(self, tablero):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCAS"

    def move (
            self,
            from_row,
            from_col,
            to_row,
            to_col):
        # Validar coordenadas
        self.validar_coordenadas(from_row, from_col, to_row, to_col)

        pieza = self.__tablero__.get_pieza(from_row, from_col)
        self.cambiar_turno()

    def cambiar_turno(self):
        if self.__turno__ == "BLANCAS":
            self.__turno__ = "NEGRAS"
        else:
            self.__turno__ = "BLANCAS"

    def validar_coordenadas(self, from_row, from_col, to_row, to_col):
        if from_row < 0 or from_row > 7 or from_col < 0 or from_col > 7:
            raise Exception("Coordenadas incorrectas")
        if to_row < 0 or to_row > 7 or to_col < 0 or to_col > 7:
            raise Exception("Coordenadas incorrectas")
        else:
            return True
