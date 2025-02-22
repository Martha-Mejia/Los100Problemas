pip install numpy
import numpy as np

# Crear matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Sumar matrices
suma = A + B

# Restar matrices
resta = A - B

# Multiplicar matrices (elemento a elemento)
multiplicacion_elemento = A * B

# Multiplicar matrices (producto matricial)
producto_matricial = np.dot(A, B)

# Transponer matriz
transpuesta = A.T

# Inversa de una matriz (si es cuadrada y no singular)
inversa = np.linalg.inv(A)

# Mostrar resultados
print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Suma de A y B:\n", suma)
print("Resta de A y B:\n", resta)
print("Multiplicación elemento a elemento de A y B:\n", multiplicacion_elemento)
print("Producto matricial de A y B:\n", producto_matricial)
print("Transpuesta de A:\n", transpuesta)
print("Inversa de A:\n", inversa)
