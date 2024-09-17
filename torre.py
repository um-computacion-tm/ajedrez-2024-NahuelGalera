# torre.py
from piezas import Pieza

class Torre(Pieza):
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    @property
    def blanca_str(self):
        return "♖"

    @property
    def negra_str(self):
        return "♜"

    def valid_positions(self, from_fila, from_col, to_fila, to_col):
        posibles_posiciones = (
            self.posibles_posiciones_vd(from_fila, from_col) +
            self.posibles_posiciones_va(from_fila, from_col) +
            self.posibles_posiciones_hd(from_fila, from_col) +
            self.posibles_posiciones_ha(from_fila, from_col)
        )
        return (to_fila, to_col) in posibles_posiciones

    def posibles_posiciones_vd(self, fila, col):
        posibles = []
        for next_fila in range(fila + 1, 8):
            other_piece = self.tablero.get_piece(next_fila, col)
            if other_piece is not None:
                if other_piece.color != self.color:
                    posibles.append((next_fila, col))
                break
            posibles.append((next_fila, col))
        return posibles

    def posibles_posiciones_va(self, fila, col):
        posibles = []
        for next_fila in range(fila - 1, -1, -1):
            other_piece = self.tablero.get_piece(next_fila, col)
            if other_piece is not None:
                if other_piece.color != self.color:
                    posibles.append((next_fila, col))
                break
            posibles.append((next_fila, col))
        return posibles

    def posibles_posiciones_hd(self, fila, col):
        posibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.tablero.get_piece(fila, next_col)
            if other_piece is not None:
                if other_piece.color != self.color:
                    posibles.append((fila, next_col))
                break
            posibles.append((fila, next_col))
        return posibles

    def posibles_posiciones_ha(self, fila, col):
        posibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.tablero.get_piece(fila, next_col)
            if other_piece is not None:
                if other_piece.color != self.color:
                    posibles.append((fila, next_col))
                break
            posibles.append((fila, next_col))
        return posibles

    def mover(self, inicio_fila, inicio_col, final_fila, final_col, tablero):
        # Rooks move in straight lines
        if inicio_fila != final_fila and inicio_col != final_col:
            return False
        
        # Check for obstacles in the path
        if inicio_fila == final_fila:  # Horizontal move
            step = 1 if final_col > inicio_col else -1
            for col in range(inicio_col + step, final_col, step):
                if tablero.get_piece(inicio_fila, col) is not None:
                    return False
        elif inicio_col == final_col:  # Vertical move
            step = 1 if final_fila > inicio_fila else -1
            for fila in range(inicio_fila + step, final_fila, step):
                if tablero.get_piece(fila, inicio_col) is not None:
                    return False
        
        # Move the piece
        tablero.set_piece(final_fila, final_col, self)
        tablero.set_piece(inicio_fila, inicio_col, None)
        return True