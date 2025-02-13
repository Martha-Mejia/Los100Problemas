import numpy as np

# Generar 10 números aleatorios entre 0 y 1
uniformes = np.random.uniform(0, 1, 10)
print("Distribución uniforme:", uniformes)
# Generar 10 números aleatorios con media 0 y desviación estándar 1
normales = np.random.normal(0, 1, 10)
print("Distribución normal:", normales)
# Generar 10 números aleatorios con 10 ensayos y probabilidad de éxito de 0.5
binomiales = np.random.binomial(10, 0.5, 10)
print("Distribución binomial:", binomiales)
# Generar 10 números aleatorios con lambda = 3
poisson = np.random.poisson(3, 10)
print("Distribución de Poisson:", poisson)
# Generar 10 números aleatorios con lambda = 1
exponencial = np.random.exponential(1, 10)
print("Distribución exponencial:", exponencial)
# Generar 10 números aleatorios con parámetros alpha = 2 y beta = 5
beta = np.random.beta(2, 5, 10)
print("Distribución beta:", beta)
