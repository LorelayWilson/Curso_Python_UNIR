import pandas as pd

# Crear DataFrame con diferentes tipos de datos
datos = {
    'edad': [25, 30, 35, 28, 42, 29, 31, 27, 33, 38],
    'altura': [1.75, 1.68, 1.82, 1.70, 1.78, 1.65, 1.73, 1.69, 1.76, 1.71],
    'nombre': ['Ana', 'Carlos', 'María', 'Luis', 'Sofia', 'Pedro', 'Elena', 'Jorge', 'Carmen', 'Diego'],
    'activo': [True, False, True, True, False, True, False, True, True, False]
}

df = pd.DataFrame(datos)

print("=== DATAFRAME INICIAL ===")
print(df)
print(f"\nTipos iniciales:")
print(df.dtypes)

print(f"\nMemoria inicial: {df.memory_usage(deep=True)} bytes")

# Conversiones de tipos
df['edad'] = df['edad'].astype('float64')
df['altura'] = df['altura'].astype('int64')
df['nombre'] = df['nombre'].astype('category')

print("\n=== DESPUÉS DE LAS CONVERSIONES ===")
print(f"Tipos finales:")
print(df.dtypes)

print(f"\nMemoria final: {df.memory_usage(deep=True)} bytes")

print("\n=== DATAFRAME FINAL ===")
print(df)
