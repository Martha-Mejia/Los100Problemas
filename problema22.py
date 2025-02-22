import random

def lanzar_moneda():
    resultado = random.choice(['cara', 'cruz'])
    return resultado

# Ejemplo de uso:
print("Resultado del lanzamiento de la moneda:", lanzar_moneda())
import random

def lanzar_dado():
    resultado = random.randint(1, 6)
    return resultado

# Ejemplo de uso:
print("Resultado del lanzamiento del dado:", lanzar_dado())
