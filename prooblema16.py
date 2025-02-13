def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0

    for char in cadena:
        if char.isalpha():
            if char in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1

    return num_vocales, num_consonantes

# Ejemplo de uso
cadena = "Hola, ¿cómo estás?"
vocales, consonantes = contar_vocales_consonantes(cadena)

print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
