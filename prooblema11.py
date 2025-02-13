def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()  # Eliminar espacios y convertir a minúsculas
    return cadena == cadena[::-1]

# Ejemplo de uso
cadena = "Anita lava la tina"
if es_palindromo(cadena):
    print(f'La cadena "{cadena}" es un palíndromo.')
else:
    print(f'La cadena "{cadena}" no es un palíndromo.')
