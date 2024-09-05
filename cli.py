from ajedrez import Ajedrez


def main():
    ajedrez = Ajedrez()
    while ajedrez.is_jugando():
        jugar(ajedrez)


def jugar(ajedrez):
    try:
        print(ajedrez.mostrar_tablero())
        print("turn: ", ajedrez.turn)
        from_fila = int(input("From fila: "))
        from_col = int(input("From columna: "))
        to_fila = int(input("To fila: "))
        to_col = int(input("To columna: "))
        # :)
        ajedrez.move(
            from_fila,
            from_col,
            to_fila,
            to_col,
        )
    except Exception as e:
        print("error", e)



if __name__ == '__main__':
    main()