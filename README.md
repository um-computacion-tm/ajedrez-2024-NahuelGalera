# Ajedrez 2024

## Descripción

Este proyecto es un juego de ajedrez implementado en Python utilizando un enfoque orientado a objetos. 
Permite una partida de dos jugadores utilizando las reglas normales del ajedrez comun.

## Requisitos

- Docker

## Caracteristicas
Reglas normales de ajedrez, el jugador que se quede sin fichas o si se rinde pierde.


### Comandos que debe ejecutar desde la terminal
## Instalación:
# Instalación de Docker

sudo apt install docker

# Clonar el repositorio del juego

git clone https://github.com/um-computacion-tm/ajedrez-2024-NahuelGalera.git

## Ejecutar el juego
# Crear imágen de Docker del juego

docker buildx build -t ajedrez-2024-NahuelGalera .

# Ejecutar los tests y el juego

docker run -i ajedrez-2024-NahuelGalera