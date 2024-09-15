from ajedrez import Ajedrez
from exceptions import InvalidMove


def main():
    game = Ajedrez()
    while game.is_jugando():
        print(game.mostrar_tablero())
        print(f"Turno de las piezas {game.turno}")
        from_fila = int(input("Ingrese la fila de origen: ")) - 1
        from_col = ord(input("Ingrese la columna de origen: ").lower()) - ord('a')
        to_fila = int(input("Ingrese la fila de destino: ")) - 1
        to_col = ord(input("Ingrese la columna de destino: ").lower()) - ord('a')
        try:
            game.move(from_fila, from_col, to_fila, to_col)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()