# Ambiente global
current_number = 1
accumulated_sum = 0


def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        print(f'n:{n} ')
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        print(f"Calculando {n}")
        fun_Fact= factorial_recursive(n-1)

        print(f'n:{n} funcion_recur: {fun_Fact}')
        return n * fun_Fact


def sum_recursive_accumulated(current_number, accumulated_sum):
    if current_number == 11:
        return accumulated_sum

    # El valor acumulado se mantiene en la funcion
    else:
        return sum_recursive_accumulated(current_number + 1, accumulated_sum + current_number)

def sum_recursive_accumulated_global_scope():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive_accumulated_global_scope()
