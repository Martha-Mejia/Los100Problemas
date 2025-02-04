#  Codigo para calcular la serie Fibonacci
def fibonacci(n):
    if n == 0:
        return "El número debe ser mayor que cero."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Codigo principal. Establece el numero y muestra la serie en pantalla
numero = 11
resultado = fibonacci(numero)
print(f"Los primeros {numero} números de la serie Fibonacci son: {resultado}")
