from ajedrez import Ajedrez
from exceptions import InvalidMove, GameOver, InvalidPiece, InvalidPlayer

def main():
    print("Bienvenido al juego de Ajedrez.")
    print("Para rendirse, escriba 'r' en cualquier momento.")
    game = Ajedrez()
    while game.is_jugando():
        try:
            jugar(game)
        except GameOver as e:
            print(str(e))
            exit(0)

def jugar(game):
    while game.is_jugando():
        print(game.mostrar_tablero())
        print(f"Turno de las piezas {game.turno}")
        print("Ingrese 'r' para rendirse.")
        from_fila = input("Ingrese la fila de origen: ")
        
        if from_fila.lower() == 'r':
            game.rendirse()
            print(f"El jugador con piezas {game.turno} se ha rendido.")
            break
        
        from_fila = int(from_fila) - 1
        from_col = ord(input("Ingrese la columna de origen: ").lower()) - ord('a')
        to_fila = int(input("Ingrese la fila de destino: ")) - 1
        to_col = ord(input("Ingrese la columna de destino: ").lower()) - ord('a')
        
        try:
            game.move(from_fila, from_col, to_fila, to_col)
        except InvalidMove as e:
            print(str(e))
        except InvalidPiece as e:
            print(str(e))
        except InvalidPlayer as e:
            print(str(e))
        except GameOver as e:
            print(str(e))
            exit(2)

    if game.is_rendicion():
        print(f"El jugador con piezas {game.ganador} ha ganado la partida.")

if __name__ == "__main__":
    main()