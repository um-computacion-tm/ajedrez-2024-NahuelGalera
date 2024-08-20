

import pygame as p 
import ChessEngine



ANCHO = ALTO = 512 #sino pruebo con 400
DIMENSION = 8
TamanoCuadro = ALTO // DIMENSION
MAX_FPS = 15 #para las animaciones a testear
IMAGENES = {}

def cargarImagenes():
    piezas = ['P', 'T', 'C', 'A', 'Q', 'K', 
            'p', 't', 'c', 'a', 'q', 'k']
    for pieza in piezas:
        IMAGENES[pieza] = p.transform.scale(p.image.load("imagenes/" + pieza + ".png"), (TamanoCuadro, TamanoCuadro))


def main():
    p.init()
    pantalla = p.display.set_mode((ANCHO, ALTO))
    reloj = p.time.Clock()
    pantalla.fill(p.Color("white"))
    estadoJuego = ChessEngine.EstadoJuego()
    print(estadoJuego.__tablero__)

    cargarImagenes() #esto solo se llama una vez
    corriendo = True

    while corriendo:
        for e in p.event.get():
            if e.type == p.QUIT:
                corriendo = False
        
        DibujoJuego(pantalla, estadoJuego)
        reloj.tick(MAX_FPS)
        p.display.flip()

def DibujoJuego(pantalla, estadoJuego):
    DibujarTablero(pantalla)
    #en esta seccion podria agregar marcado de piezas o movimientos
    DibujarPiezas(pantalla, estadoJuego.__tablero__)

def DibujarTablero(pantalla):
    colores = [p.Color("white"), p.Color("gray")]
    for filas in range(DIMENSION):
        for columnas in range(DIMENSION):
            color = colores[((filas+columnas) % 2)]
            p.draw.rect(pantalla, color, p.Rect(columnas*TamanoCuadro, filas*TamanoCuadro, TamanoCuadro, TamanoCuadro))

def DibujarPiezas(pantalla, tablero):
    for filas in range(DIMENSION):
        for columnas in range(DIMENSION):
            pieza = tablero[filas][columnas]
            if pieza != "--":
                pantalla.blit(IMAGENES[pieza], p.Rect(columnas*TamanoCuadro, filas*TamanoCuadro, TamanoCuadro, TamanoCuadro))


if __name__ == "__main__":
    main()



















