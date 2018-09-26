from Exceptions import Exceptions_Basic_Test, linux_interaction
import unittest


class DecoratorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_Exeption_Basic(self):
        val_correcto = Exceptions_Basic_Test(3)
        self.assertEqual(val_correcto, "Valor correcto")

        with self.assertRaisesRegex(Exception, "x should not exceed 5. The value of x was: 6"):
            Exceptions_Basic_Test(6)

    def test_try_except(self):
        try:
            linux_interaction()
        except AssertionError as error:
            print(error)
        else:
            print('Executing the else clause.')
        finally:
            print('Termino de ejecucion')

if __name__ == '__main__':
    unittest.main()
