# Script para generar y mostrar una matriz de multiplicación 5x5
# Crea una tabla donde cada elemento es el producto de su número de fila por su número de columna

# Crear matriz de multiplicación 5x5 usando list comprehension
# La matriz contendrá el producto de (número de fila) × (número de columna)
# Por ejemplo: posición [2][3] = 2 × 3 = 6
matriz = [[fila * columna for columna in range(5)] for fila in range(5)]

# Mostrar la matriz en formato de tabla usando join
# Para cada fila, formateamos los elementos con ancho fijo y los unimos con espacios
# f"{elemento:2}" asegura que cada número ocupe exactamente 2 espacios para alineación
for fila in matriz:
    print(" ".join(f"{elemento:2}" for elemento in fila))
