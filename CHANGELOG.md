# Changelog

## NAHUEL GALERA

## [0.35] -- 03-10-2024

### Agregado
-   Validación de entrada en el método `obtener_movimiento` en `cli.py` para asegurar que las coordenadas estén dentro del rango válido del tablero de ajedrez.
-   Manejo de excepciones en `game.move` en `cli.py` para capturar y manejar errores de movimiento inválido.

### Modificado
-   Mejorada la documentación y comentarios en `cli.py` para mayor claridad.
-   Separación de la lógica del juego y la interfaz de usuario en `cli.py` para mejorar la modularidad.

### Borrado
-   Código redundante en `cli.py`
