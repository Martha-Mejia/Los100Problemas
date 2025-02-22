def suma_serie_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Ejemplo de uso:
n = 10
print("Suma de los primeros", n, "números naturales es:", suma_serie_for(n))
def suma_serie_formula(n):
    return n * (n + 1) // 2

# Ejemplo de uso:
n = 10
print("Suma de los primeros", n, "números naturales es:", suma_serie_formula(n))
def suma_serie_sum(n):
    return sum(range(1, n+1))

# Ejemplo de uso:
n = 10
print("Suma de los primeros", n, "números naturales es:", suma_serie_sum(n))
