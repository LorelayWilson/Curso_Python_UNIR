import pandas as pd
from datetime import datetime, timedelta

# Crear datos de ventas
datos_ventas = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares'],
    'precio': [1200, 25, 80, 300, 150],
    'unidades_vendidas': [15, 120, 85, 30, 200],
    'fecha_venta': [
        datetime.now() - timedelta(days=5),
        datetime.now() - timedelta(days=3),
        datetime.now() - timedelta(days=1),
        datetime.now() - timedelta(days=2),
        datetime.now()
    ]
}

# Crear DataFrame
df_ventas = pd.DataFrame(datos_ventas)

print("DATAFRAME DE VENTAS ORIGINAL:")
print(df_ventas)
print()

# 1. Añadir columna de ingresos totales
df_ventas['ingresos_totales'] = df_ventas['precio'] * df_ventas['unidades_vendidas']

print("DATAFRAME CON INGRESOS TOTALES:")
print(df_ventas)
print()

# 2. Productos ordenados por ingreso total (mayor a menor)
df_ordenado = df_ventas.sort_values('ingresos_totales', ascending=False)

print("PRODUCTOS ORDENADOS POR INGRESO TOTAL:")
print(df_ordenado[['producto', 'ingresos_totales']])
print()

# 3. Precio promedio de todos los productos
precio_promedio = df_ventas['precio'].mean()
print(f"PRECIO PROMEDIO: ${precio_promedio:.2f}")
print()

# 4. Producto con más unidades vendidas
producto_mas_vendido = df_ventas.loc[df_ventas['unidades_vendidas'].idxmax()]
print("PRODUCTO CON MÁS UNIDADES VENDIDAS:")
print(f"  Producto: {producto_mas_vendido['producto']}")
print(f"  Unidades: {producto_mas_vendido['unidades_vendidas']}")
print(f"  Precio: ${producto_mas_vendido['precio']}")
print(f"  Ingresos: ${producto_mas_vendido['ingresos_totales']}")
print()

# Información adicional del DataFrame
print("INFORMACIÓN DEL DATAFRAME:")
print(f"  Forma: {df_ventas.shape}")
print(f"  Columnas: {list(df_ventas.columns)}")
print(f"  Tipos de datos:")
print(df_ventas.dtypes)
