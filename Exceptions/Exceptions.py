import sys

def FunctionError(mensaje):
    raise Exception(mensaje)


def Exceptions_Basic_Test(num):
    if num > 5:
        mensaje_error = 'x should not exceed 5. The value of x was: {}'.format(num)
        FunctionError(mensaje_error)
    else:
        return "Valor correcto"


def linux_interaction():
    print(sys.platform)
    assert ('win32' in sys.platform), "Function can only run on Win32 systems."
    print('Doing something.')
