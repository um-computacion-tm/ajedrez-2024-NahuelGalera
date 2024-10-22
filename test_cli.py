import unittest
from io import StringIO
import sys
from ajedrez import Ajedrez
from exceptions import GameOver
from cli import obtener_movimiento, es_posicion_valida, convertir_posicion, mostrar_tablero, anunciar_ganador, obtener_jugador_actual, manejar_turno, finalizar_juego, main

class TestFuncionesSimples(unittest.TestCase):
    def test_es_posicion_valida(self):
        print("Probando es_posicion_valida...")
        self.assertTrue(es_posicion_valida('a2'))
        self.assertTrue(es_posicion_valida('h8'))
        self.assertFalse(es_posicion_valida('i9'))
        self.assertFalse(es_posicion_valida('a9'))
        self.assertFalse(es_posicion_valida('h0'))
        self.assertFalse(es_posicion_valida('a'))
        self.assertFalse(es_posicion_valida('22'))
        print("Pruebas de es_posicion_valida completadas.")

    def test_convertir_posicion(self):
        print("Probando convertir_posicion...")
        self.assertEqual(convertir_posicion('a2'), (6, 0))
        self.assertEqual(convertir_posicion('h8'), (0, 7))
        self.assertEqual(convertir_posicion('d4'), (4, 3))
        print("Pruebas de convertir_posicion completadas.")

class TestFuncionesTablero(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_mostrar_tablero(self):
        print("Probando mostrar_tablero...")
        game = Ajedrez()
        mostrar_tablero(game)
        output = self.output.getvalue()
        print(output)
        self.assertIn('a b c d e f g h', output)
        self.assertIn('8', output)
        self.assertIn('1', output)
        print("Pruebas de mostrar_tablero completadas.")

    def test_anunciar_ganador(self):
        print("Probando anunciar_ganador...")
        game = Ajedrez()
        game.obtener_ganador = lambda: 'Blancas'
        anunciar_ganador(game)
        output = self.output.getvalue()
        print(output)
        self.assertIn('El ganador es: Blancas', output)
        print("Pruebas de anunciar_ganador completadas.")

class TestObtenerMovimiento(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.saved_stdin = sys.stdin
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout
        sys.stdin = self.saved_stdin

    def test_obtener_movimiento_valido(self):
        print("Probando obtener_movimiento con movimiento válido...")
        sys.stdin = StringIO('a2\na3\n')
        from_pos, to_pos = obtener_movimiento('Blancas')
        self.assertEqual(from_pos, 'a2')
        self.assertEqual(to_pos, 'a3')
        print("Pruebas de obtener_movimiento con movimiento válido completadas.")

    def test_obtener_movimiento_rendirse(self):
        print("Probando obtener_movimiento con rendición...")
        sys.stdin = StringIO('r\n')
        from_pos, to_pos = obtener_movimiento('Blancas')
        self.assertEqual(from_pos, 'r')
        self.assertIsNone(to_pos)
        print("Pruebas de obtener_movimiento con rendición completadas.")

class TestJuegoCompleto(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.saved_stdin = sys.stdin
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout
        sys.stdin = self.saved_stdin

    def test_manejar_turno(self):
        print("Probando manejar_turno...")
        game = Ajedrez()
        sys.stdin = StringIO('a2\na3\n')
        manejar_turno(game, max_attempts=1)
        output = self.output.getvalue()
        print(output)
        self.assertIn('a b c d e f g h', output)
        self.assertTrue('Movimiento inválido. Intente de nuevo.', output)
        print("Pruebas de manejar_turno completadas.")

    def test_finalizar_juego(self):
        print("Probando finalizar_juego...")
        game = Ajedrez()
        game.obtener_ganador = lambda: 'Blancas'
        with self.assertRaises(GameOver):
            finalizar_juego(game)
        output = self.output.getvalue()
        print(output)
        self.assertIn('El ganador es: Blancas', output)
        self.assertTrue('Juego terminado', output)
        print("Pruebas de finalizar_juego completadas.")

    def test_main(self):
        print("Probando main...")
        sys.stdin = StringIO('a2\na3\nr\n')
        try:
            main()
        except SystemExit:
            pass
        output = self.output.getvalue()
        print(output)
        self.assertTrue('Blancas se rinde', output)
        self.assertTrue('El ganador es: Negras', output)
        self.assertTrue('Juego interrumpido. Saliendo...', output)
        print("Pruebas de main completadas.")

if __name__ == '__main__':
    unittest.main()