import io
import sys
import unittest
from firstClassObjects import say_hello, be_awesome, greet_bob
from innerFunctions import parent


class DecoratorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_objetos_de_primera_clase(self):
        self.assertEqual(greet_bob(say_hello), "Hello Bob")
        self.assertEqual(greet_bob(be_awesome), "Yo Bob, together we are the"
                                                " awesomest!")

    def test_inner_functions(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        parent()
        sys.stdout = sys.__stdout__
        # El orden de la definicion de la funcion no importa
        # Las funciones second_child() y first_child() solo existen dentro del padre
        # y no se pueden llamar de manera individual.
        salida_esperada = "Printing from the parent() function\n"\
                          "Printing from the second_child() function\n"\
                          "Printing from the first_child() function\n"

        self.assertEqual(capturedOutput.getvalue(), salida_esperada)


if __name__ == '__main__':
    unittest.main()


