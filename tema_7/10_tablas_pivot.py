import pandas as pd
import numpy as np

# Crear datos de ejemplo
np.random.seed(42)  # Para reproducibilidad

# Generar 30 valores distribuidos entre las categorías
categorias = np.random.choice(['Electrónica', 'Ropa', 'Hogar'], size=30)

# Generar 30 valores distribuidos entre las regiones
regiones = np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=30)

# Generar 30 valores aleatorios de ventas entre 100 y 1000
ventas = np.random.randint(100, 1001, size=30)

# Generar 30 valores aleatorios de unidades entre 1 y 20
unidades = np.random.randint(1, 21, size=30)

# Crear el DataFrame
data = {
    'categoría': categorias,
    'región': regiones,
    'ventas': ventas,
    'unidades': unidades
}

df_ventas = pd.DataFrame(data)

print("DataFrame de ventas por categoría y región:")
print(df_ventas)

# Crear tabla pivotante con suma de ventas, totales por fila y columna
tabla_pivot = df_ventas.pivot_table(
    values='ventas',
    index='categoría',
    columns='región',
    aggfunc='sum',
    margins=True,
    margins_name='Total'
)

# Reemplazar valores NaN con ceros
tabla_pivot = tabla_pivot.fillna(0)

print("\nTabla pivotante (suma de ventas):")
print(tabla_pivot)
