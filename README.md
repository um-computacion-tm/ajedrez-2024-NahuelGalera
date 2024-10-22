# Ajedrez 2024

## Descripción

Ajedrez 2024 es una aplicación de ajedrez desarrollada para proporcionar una experiencia de juego completa y una suite de pruebas para garantizar la calidad del código. Este documento proporciona instrucciones detalladas sobre cómo poner en funcionamiento la aplicación en modo de prueba y en modo de juego utilizando Docker.

## Requisitos

- Docker

## Como se Juega
Reglas normales de ajedrez, el jugador que se quede sin fichas o si se rinde pierde.


### Clonar el Repositorio

Primero, clona el repositorio del proyecto:

```bash
git clone git@github.com:um-computacion-tm/ajedrez-2024-NahuelGalera.git

### Ejecutar el juego

Crear imágen de Docker del juego

docker buildx build -t ajedrez-2024-NahuelGalera .
Ejecutar los tests y el juego

docker run -i ajedrez-2024-NahuelGalera