pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios (por ejemplo, una distribución normal)
datos = np.random.randn(1000)

# Crear el histograma
plt.hist(datos, bins=30, edgecolor='black')

# Agregar título y etiquetas
plt.title('Histograma de Datos')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()
# Calcular estadísticas básicas
media = np.mean(datos)
mediana = np.median(datos)
desviacion_estandar = np.std(datos)

print("Media:", media)
print("Mediana:", mediana)
print("Desviación Estándar:", desviacion_estandar)
