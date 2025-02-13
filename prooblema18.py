import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return raiz,
    else:
        return None

# Ejemplo de uso
a = 1
b = -3
c = 2

resultado = resolver_ecuacion_cuadratica(a, b, c)
if resultado is not None:
    if len(resultado) == 2:
        print(f"Las raíces de la ecuación cuadrática son: {resultado[0]} y {resultado[1]}")
    else:
        print(f"La raíz de la ecuación cuadrática es: {resultado[0]}")
else:
    print("La ecuación cuadrática no tiene raíces reales.")
