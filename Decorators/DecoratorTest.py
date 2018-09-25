import io
import sys
import unittest
from firstClassObjects import say_hello, be_awesome, greet_bob
from innerFunctions import parent, parentFunction
from simpleDecorators import my_decorator, say_whee, say_whee_with_decorator, say_whee_with_arguments
from DecoratorsLib import timer, debug, validate_json
import math


class DecoratorTest(unittest.TestCase):

    def setUp(self):
        self.my_factorial = debug(math.factorial)
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

    def test_inner_functions_return(self):
        first = parentFunction(1)
        second = parentFunction(2)
        self.assertEqual(first(), 'Hi, I am Emma')
        self.assertEqual(second(), 'Call me Liam')

    def test_simpleDecorators(self):
        say = my_decorator(say_whee)
        salida = say()
        salida_esperada = 'Algo pasa antes de llamar a la funcion Soy la funcion! Algo pasa despues de llamar a la funcion'
        self.assertEqual(salida, salida_esperada)

    def test_withDecorators(self):
        salida = say_whee_with_decorator()
        salida_esperada = 'Algo pasa antes de llamar a la funcion Soy la funcion con decorador! Algo pasa despues de llamar a la funcion'
        self.assertEqual(salida, salida_esperada)

    def test_withDecoratorsWithArguments(self):
        salida = say_whee_with_arguments("Argumento1")
        salida_esperada = 'Soy una funcion con el argumento: Argumento1'\
                          'Soy una funcion con el argumento: Argumento1'
        self.assertEqual(salida, salida_esperada)

    def test_DecoratorsIntrospection(self):
        self.assertEqual(str(say_whee_with_decorator)[0:40], '<function my_decorator.<locals>.wrapper ')
        # con el decorador functools para obtener el nombre real de la funcion
        self.assertEqual(str(say_whee_with_arguments)[0:37],'<function say_whee_with_arguments at ')

    def testDecoratorsLib_Timer(self):
        salida = self.waste_some_time(10)
        self.assertEqual(salida[0:52], "Result: 3332833350000 Finished 'waste_some_time' in ")

    def testDecoratorsLib_DebugStandarLibrary(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.approximate_e(5)
        sys.stdout = sys.__stdout__
        salida_esperada = "Calling factorial(0)\n"\
                          "'factorial' returned 1\n"\
                          "Calling factorial(1)\n"\
                          "'factorial' returned 1\n"\
                          "Calling factorial(2)\n"\
                          "'factorial' returned 2\n"\
                          "Calling factorial(3)\n"\
                          "'factorial' returned 6\n"\
                          "Calling factorial(4)\n"\
                          "'factorial' returned 24\n"
        self.assertEqual(capturedOutput.getvalue(), salida_esperada)

    def testDecoratorsLib_ValidateJson(self):
        dicPythonOrigen = {
            "president": {
              "name": "Zaphod Beeblebrox",
              "species": "Betelgeusian"
            }
        }
        salida= self.update_grade(dicPythonOrigen)
        self.assertEqual(salida,"")

    @timer
    def waste_some_time(self, num_times):
        total = 0
        for _ in range(num_times):
            total = total + sum([i**2 for i in range(10000)])
        return total

    @debug
    def make_greeting(self, name, age=None):
        if age is None:
            return f"Howdy {name}!"
        else:
            return f"Whoa {name}! {age} already, you are growing up!"

    def approximate_e(self, terms=18):
        return sum(1 / self.my_factorial(n) for n in range(terms))

    @validate_json("president")
    def update_grade(self, data_json):
        json_data = data_json
        # Update database.
        return "success!"

if __name__ == '__main__':
    unittest.main()
