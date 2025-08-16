import numpy as np

# Crear un array bidimensional de 4x5 con números aleatorios entre 0 y 100
array_aleatorio = np.random.randint(0, 101, size=(4, 5))

print("Array aleatorio generado:")
print(array_aleatorio)
print()

# 1. Calcular la media de todo el array
media_total = np.mean(array_aleatorio)

# 2. Calcular la desviación estándar de todo el array
desviacion_estandar = np.std(array_aleatorio)

# 3. Encontrar el valor máximo y mínimo de todo el array
valor_maximo = np.max(array_aleatorio)
valor_minimo = np.min(array_aleatorio)

# 4. Calcular la suma de cada fila del array
suma_filas = np.sum(array_aleatorio, axis=1)

# 5. Calcular la media de cada columna del array
media_columnas = np.mean(array_aleatorio, axis=0)

# Mostrar todos los resultados
print("RESULTADOS DE LAS OPERACIONES:")
print("=" * 40)
print(f"Media total del array: {media_total:.2f}")
print(f"Desviación estándar del array: {desviacion_estandar:.2f}")
print(f"Valor máximo del array: {valor_maximo}")
print(f"Valor mínimo del array: {valor_minimo}")
print(f"Suma de cada fila: {suma_filas}")
print(f"Media de cada columna: {media_columnas}")
print()

