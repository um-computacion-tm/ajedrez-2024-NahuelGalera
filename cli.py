from ajedrez import Ajedrez
from exceptions import GameOver

def obtener_movimiento(jugador):
    while True:
        from_pos = input(f"{jugador}, ingrese la posición de origen (ej.: a2) o 'r' para rendirse: ").strip().lower()
        if from_pos == 'r':
            return from_pos, None
        to_pos = input("Ingrese la posición de destino (e.g., a3): ").strip().lower()
        if es_posicion_valida(from_pos) and es_posicion_valida(to_pos):
            return from_pos, to_pos
        return None, None  # Indica que la posición es inválida

def es_posicion_valida(pos):
    return len(pos) == 2 and 'a' <= pos[0] <= 'h' and '1' <= pos[1] <= '8'

def convertir_posicion(pos):
    return 8 - int(pos[1]), ord(pos[0]) - ord('a')

def mostrar_tablero(game):
    columnas = '  a b c d e f g h'
    print(columnas)
    for i, row in enumerate(game.__tablero__.__board__):
        fila = f"{8 - i} " + ' '.join(
            [pieza.blanca_str if pieza and pieza.color == 'BLANCA' else pieza.negra_str if pieza and pieza.color == 'NEGRA' else '.' for pieza in row]
        )
        print(fila)
    print(columnas)

def anunciar_ganador(game):
    ganador = game.obtener_ganador()
    print(f"El ganador es: {ganador}")

def obtener_jugador_actual(game):
    return "Blancas" if game.__turno__ == 'BLANCA' else "Negras"

def manejar_turno(game, max_attempts=None):
    attempts = 0
    while True:
        if max_attempts is not None and attempts >= max_attempts:
            break
        jugador = obtener_jugador_actual(game)
        from_pos, to_pos = obtener_movimiento(jugador)
        if from_pos == 'r':
            print(f"{jugador} se rinde")
            raise GameOver(f"El ganador es: {'Negras' if jugador == 'Blancas' else 'Blancas'}")
        if from_pos is None or to_pos is None:
            print("Movimiento inválido. Intente de nuevo.")
            attempts += 1
            continue
        from_pos = convertir_posicion(from_pos)
        to_pos = convertir_posicion(to_pos)
        if game.move(from_pos[0], from_pos[1], to_pos[0], to_pos[1]):
            mostrar_tablero(game)
            if game.is_terminado():
                finalizar_juego(game)
            break
        print("Movimiento inválido. Intente de nuevo.")
        attempts += 1

def finalizar_juego(game):
    anunciar_ganador(game)
    raise GameOver("Juego terminado")

def main():
    game = Ajedrez()
    try:
        while not game.is_terminado():
            mostrar_tablero(game)
            manejar_turno(game)
        finalizar_juego(game)
    except GameOver as e:
        print(e)
    except KeyboardInterrupt:
        print("\nJuego interrumpido. Saliendo...")

if __name__ == '__main__':
    main()