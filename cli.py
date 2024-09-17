import sys
from ajedrez import Ajedrez
from exceptions import InvalidMove, GameOver, InvalidPiece, InvalidPlayer

def main():
    game = Ajedrez()
    print("Bienvenido al juego de Ajedrez.")
    print("Para rendirse, escriba 'r' en cualquier momento.")
    while True:
        try:
            jugar(game)
        except GameOver as e:
            print(e)
            sys.exit() # Exit the program
        except InvalidMove as e:
            print(e)
        except InvalidPlayer as e:
            print(e)

def jugar(game):
    from_fila, from_col, to_fila, to_col = obtener_movimiento()
    if from_fila == 'r':
        game.rendirse()
    else:
        game.move(from_fila, from_col, to_fila, to_col)
    print(game)
    print(f"Turno de las piezas {game.turno}")

    if game.is_rendicion():
        print(f"El jugador con piezas {game.ganador} ha ganado la partida.")

def obtener_movimiento():
    while True:
        from_fila = input("Ingrese la fila de origen: ")
        if from_fila.lower() == 'r':
            return from_fila, None, None, None
        
        try:
            from_fila = int(from_fila) - 1
            from_col = ord(input("Ingrese la columna de origen: ").lower()) - ord('a')
            to_fila = int(input("Ingrese la fila de destino: ")) - 1
            to_col = ord(input("Ingrese la columna de destino: ").lower()) - ord('a')
            return from_fila, from_col, to_fila, to_col
        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    main()