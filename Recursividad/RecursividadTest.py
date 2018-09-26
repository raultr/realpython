import unittest
from Recursive import factorial_recursive, sum_recursive_accumulated, sum_recursive_accumulated_global_scope
import math


class DecoratorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_ejemplo1(self):
        resultado = factorial_recursive(5)
        self.assertEqual(resultado, 120)

    def test_acumulado_en_la_funcion(self):
        resultado = sum_recursive_accumulated(1, 0)
        self.assertEqual(resultado, 55)

    def test_acumulado_en_la_funcion_en_ambiente_global(self):
        resultado = sum_recursive_accumulated_global_scope()
        self.assertEqual(resultado, 55)


if __name__ == '__main__':
    unittest.main()
