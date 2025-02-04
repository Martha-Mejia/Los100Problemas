#Codigo para seleccionar el divisor
def check_number(num, divisor):
    if num % divisor == 0:
        return f"{num} es múltiplo de {divisor}"
    elif num % 2 == 0:
        return f"{num} es par"
    else:
        return f"{num} es impar"

numero = int(input("Introduce un número: "))
divisor = int(input("Introduce el divisor para verificar múltiplo: "))

#imprimir el resultado
resultado = check_number(numero, divisor)
print(resultado)