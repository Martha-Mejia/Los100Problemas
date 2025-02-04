# Codigo para calcular el factorial de un numero
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pedir el numero
print('Calcular el factorial del numero 5')
print('')
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")