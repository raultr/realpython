import functools


def my_decorator(func):
    def wrapper():
        saludo_funcion = func()
        resultado = f'Algo pasa antes de llamar a la funcion {saludo_funcion} Algo pasa despues de llamar a la funcion'
        return resultado
    return wrapper


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        a= func(*args, **kwargs)
        b= func(*args, **kwargs)
        return a + b
    return wrapper_do_twice


def say_whee():
    return "Soy la funcion!"


@my_decorator
def say_whee_with_decorator():
    return "Soy la funcion con decorador!"


@do_twice
def say_whee_with_arguments(name):
    return f"Soy una funcion con el argumento: {name}"
