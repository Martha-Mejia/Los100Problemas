def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada por burbuja:", ordenamiento_burbuja(lista))
def ordenamiento_seleccion(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada por selección:", ordenamiento_seleccion(lista))
def ordenamiento_seleccion(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada por selección:", ordenamiento_seleccion(lista))
def ordenamiento_rapido(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        izq = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        der = [x for x in arr if x > pivote]
        return ordenamiento_rapido(izq) + centro + ordenamiento_rapido(der)

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada por Quick Sort:", ordenamiento_rapido(lista))
def ordenamiento_mezcla(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        mitad_izquierda = arr[:medio]
        mitad_derecha = arr[medio:]

        ordenamiento_mezcla(mitad_izquierda)
        ordenamiento_mezcla(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1

    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada por Merge Sort:", ordenamiento_mezcla(lista))
