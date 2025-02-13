def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Ejemplo de uso
lista = [2, 3, 4, 10, 40]
x = 10
resultado = busqueda_lineal(lista, x)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")
def busqueda_binaria(arr, x):
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] < x:
            bajo = medio + 1
        elif arr[medio] > x:
            alto = medio - 1
        else:
            return medio
    return -1

# Ejemplo de uso
lista = [2, 3, 4, 10, 40]
x = 10
resultado = busqueda_binaria(lista, x)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")
