import pandas as pd
import numpy as np

# Datos de ventas mensuales
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [15200, 14800, 16700, 17500, 18200],
    'unidades': [120, 115, 140, 150, 160],
    'gastos': [5100, 4800, 5400, 5800, 6000]
}

# Crea el DataFrame
df_ventas = pd.DataFrame(data)

print("DataFrame de ventas mensuales:")
print(df_ventas)

# 1. Utiliza el método describe() para obtener un resumen estadístico completo
print("\n1. Resumen estadístico completo (describe()):")
print(df_ventas.describe())

# 2. Calcula la media, mediana y desviación estándar de la columna 'ventas'
print("\n2. Medidas de la columna 'ventas':")
print(f"Media: {df_ventas['ventas'].mean():.2f}")
print(f"Mediana: {df_ventas['ventas'].median():.2f}")
print(f"Desviación estándar: {df_ventas['ventas'].std():.2f}")

# 3. Encuentra el valor máximo y mínimo de la columna 'unidades'
print("\n3. Valores extremos de la columna 'unidades':")
print(f"Máximo: {df_ventas['unidades'].max()}")
print(f"Mínimo: {df_ventas['unidades'].min()}")

# 4. Calcula la correlación entre las columnas 'ventas' y 'unidades'
print("\n4. Correlación entre 'ventas' y 'unidades':")
correlacion = df_ventas['ventas'].corr(df_ventas['unidades'])
print(f"Coeficiente de correlación: {correlacion:.4f}")

# 5. Matriz de correlación completa del DataFrame
print("\n5. Matriz de correlación completa:")
print(df_ventas.corr())
