def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso:
num = 5
print(f"Factorial de {num} es:", factorial(num))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso:
num = 10
print(f"Fibonacci de {num} es:", fibonacci(num))

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso:
lista = [1, 2, 3, 4, 5]
print("Suma de la lista es:", suma_lista(lista))

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Ejemplo de uso:
a = 48
b = 18
print(f"MCD de {a} y {b} es:", mcd(a, b))
