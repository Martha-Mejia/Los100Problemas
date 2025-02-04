#el codigo usara la funcion de interes compuesto
def interes_compuesto(capital_inicial, tasa_interes, tiempo):
    return capital_inicial * (1 + tasa_interes / 100) ** tiempo

capital = 1000  # Capital inicial
tasa = 5  # Tasa de interés anual en porcentaje
tiempo = 10  # Tiempo en años

#se recibe el capital inicial, taza anual de intereses y el tiempo en 
monto_final = interes_compuesto(capital, tasa, tiempo)
print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")

# El resultado será: El monto final después de 10 años es: 1628.89
