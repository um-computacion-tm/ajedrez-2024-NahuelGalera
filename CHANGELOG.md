# Changelog

## NAHUEL GALERA

## [0.36] -- 04-10-2024

### Agregado
-   Pruebas unitarias para las funciones `main`, `jugar` y `obtener_movimiento` en `cli.py` utilizando el módulo `unittest`.
-   Manejo de la excepción `SystemExit` en la función `main` para asegurar que el programa se cierra correctamente cuando el juego termina.

### Modificado
-   Actualización de la función `main` en `cli.py` para llamar a `sys.exit(0)` cuando se captura la excepción `GameOver`.
-   Corrección de las pruebas unitarias en `test_cli.py` para asegurar que `SystemExit` se maneja correctamente.

### Borrado
-   
