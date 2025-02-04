# generar listas que toma un parametro limite
#crear dos listas: pares e inpares

def generar_listas(limite):
    pares = []
    impares = []

#usar el bucle for para llegar de 0 al limite
#codigo para verificar par o inpar
    
    for i in range(limite + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

limite = int(input("Introduce el límite: "))
pares, impares = generar_listas(limite)

#imprimir las dos listas

print("Números pares:", pares)
print("Números impares:", impares)