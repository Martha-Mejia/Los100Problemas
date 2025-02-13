def encontrar_mayor(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    return mayor

# Ejemplo de uso
numero1 = 10
numero2 = 25
numero3 = 5

print("El mayor número es:", encontrar_mayor(numero1, numero2, numero3))
