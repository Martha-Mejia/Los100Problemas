def area_cubo(lado):
    return 6 * (lado ** 2)

def volumen_cubo(lado):
    return lado ** 3

# Ejemplo de uso:
lado = 4
print("Área del cubo:", area_cubo(lado))
print("Volumen del cubo:", volumen_cubo(lado))
import math

def area_esfera(radio):
    return 4 * math.pi * (radio ** 2)

def volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

# Ejemplo de uso:
radio = 3
print("Área de la esfera:", area_esfera(radio))
print("Volumen de la esfera:", volumen_esfera(radio))
import math

def area_cilindro(radio, altura):
    return 2 * math.pi * radio * (radio + altura)

def volumen_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura

# Ejemplo de uso:
radio = 2
altura = 5
print("Área del cilindro:", area_cilindro(radio, altura))
print("Volumen del cilindro:", volumen_cilindro(radio, altura))
import math

def area_cono(radio, altura):
    generatriz = math.sqrt((radio ** 2) + (altura ** 2))
    return math.pi * radio * (radio + generatriz)

def volumen_cono(radio, altura):
    return (1/3) * math.pi * (radio ** 2) * altura

# Ejemplo de uso:
radio = 3
altura = 4
print("Área del cono:", area_cono(radio, altura))
print("Volumen del cono:", volumen_cono(radio, altura))
