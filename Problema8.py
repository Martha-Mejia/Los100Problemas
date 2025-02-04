import math

#codigo principa
print(f"La circunferencia del círculo es: {circunferencia:.2f}")l para calcular el area y circunfererncia
def calcular_area_y_circunferencia(radio):
    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area, circunferencia

radio = float(input("Introduce el radio del círculo: "))
area, circunferencia = calcular_area_y_circunferencia(radio)

#imprimir el resultado

print(f"El área del círculo es: {area:.2f}")