pip install numpy pandas matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generar datos aleatorios (por ejemplo, una distribución normal)
np.random.seed(0)
datos = np.random.randn(1000)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(datos, columns=['Valores'])

# Calcular estadísticas básicas
media = df['Valores'].mean()
mediana = df['Valores'].median()
desviacion_estandar = df['Valores'].std()
varianza = df['Valores'].var()
percentiles = df['Valores'].quantile([0.25, 0.5, 0.75])

# Mostrar estadísticas
print("Media:", media)
print("Mediana:", mediana)
print("Desviación Estándar:", desviacion_estandar)
print("Varianza:", varianza)
print("Percentiles:")
print(percentiles)

# Crear el histograma de los datos
plt.hist(df['Valores'], bins=30, edgecolor='black')
plt.title('Histograma de Datos')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
