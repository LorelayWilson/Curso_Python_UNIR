import pandas as pd

def crear_dataframe_ventas():
    """Crea un DataFrame de ventas con productos de diferentes categorías"""
    datos = {
        'producto': ['Laptop HP', 'Camiseta Azul', 'Sofá Moderno', 'Smartphone Samsung', 
                     'Pantalón Negro', 'Lámpara LED', 'Auriculares Sony', 'Mesa de Centro'],
        'categoria': ['Electrónica', 'Ropa', 'Hogar', 'Electrónica', 
                      'Ropa', 'Hogar', 'Electrónica', 'Hogar'],
        'precio': [899.99, 25.50, 299.99, 599.99, 45.00, 89.99, 79.99, 120.00],
        'stock': [15, 50, 8, 22, 35, 12, 28, 18]
    }
    
    return pd.DataFrame(datos)

def main():
    """Función principal que ejecuta las operaciones de filtrado solicitadas"""
    # Crear DataFrame
    df_ventas = crear_dataframe_ventas()
    
    print("DataFrame de ventas:")
    print(df_ventas)
    
    # 1. Filtra los productos que pertenecen a la categoría 'Electrónica'
    print("\n1. Productos de categoría 'Electrónica':")
    productos_electronica = df_ventas[df_ventas['categoria'] == 'Electrónica']
    print(productos_electronica)
    
    # 2. Encuentra los productos con precio mayor a 50 y stock menor a 20
    print("\n2. Productos con precio > 50 y stock < 20:")
    filtro_precio_stock = df_ventas[(df_ventas['precio'] > 50) & (df_ventas['stock'] < 20)]
    print(filtro_precio_stock)
    
    # 3. Selecciona los productos que contengan la letra 'a' en su nombre
    print("\n3. Productos que contienen la letra 'a' en su nombre:")
    productos_con_a = df_ventas[df_ventas['producto'].str.contains('a', case=False)]
    print(productos_con_a)
    
    # 4. Utiliza el método query() para encontrar productos de 'Hogar' con precio menor a 30
    print("\n4. Productos de 'Hogar' con precio < 30 (usando query):")
    productos_hogar_baratos = df_ventas.query("categoria == 'Hogar' and precio < 30")
    print(productos_hogar_baratos)

if __name__ == "__main__":
    main()
