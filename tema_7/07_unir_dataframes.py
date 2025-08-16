import pandas as pd

def crear_dataframes():
    """Crea los DataFrames de ventas y productos"""
    ventas = pd.DataFrame({
        'id_producto': ['A1', 'A2', 'A3', 'A4', 'A2'],
        'fecha': pd.date_range('2023-01-01', periods=5),
        'unidades_vendidas': [10, 5, 8, 12, 7]
    })
    
    productos = pd.DataFrame({
        'id_producto': ['A1', 'A2', 'A3', 'A5'],
        'nombre': ['Laptop', 'Monitor', 'Teclado', 'Mouse'],
        'precio': [1200, 300, 100, 50]
    })
    
    return ventas, productos

def mostrar_dataframes(ventas, productos):
    """Muestra los DataFrames originales"""
    print("=== DATAFRAME VENTAS ===")
    print(ventas)
    
    print("\n=== DATAFRAME PRODUCTOS ===")
    print(productos)

def realizar_merges(ventas, productos):
    """Realiza los tres tipos de merge solicitados"""
    # Merge tipo 'inner' (solo registros que coinciden en ambos DataFrames)
    print("\n" + "="*50)
    print("1. MERGE TIPO 'INNER'")
    print("="*50)
    merge_inner = pd.merge(ventas, productos, on='id_producto', how='inner')
    print(merge_inner)
    
    # Merge tipo 'left' (todos los registros de ventas)
    print("\n" + "="*50)
    print("2. MERGE TIPO 'LEFT'")
    print("="*50)
    merge_left = pd.merge(ventas, productos, on='id_producto', how='left')
    print(merge_left)
    
    # Merge tipo 'outer' (todos los registros de ambos DataFrames)
    print("\n" + "="*50)
    print("3. MERGE TIPO 'OUTER'")
    print("="*50)
    merge_outer = pd.merge(ventas, productos, on='id_producto', how='outer')
    print(merge_outer)
    
    return merge_inner, merge_left, merge_outer

def crear_columna_calculada(merge_inner):
    """Crea la columna 'valor_total' en el merge 'inner'"""
    print("\n" + "="*50)
    print("4. MERGE 'INNER' CON COLUMNA 'VALOR_TOTAL'")
    print("="*50)
    
    # Crear una copia para evitar modificar el DataFrame original
    merge_inner_con_valor = merge_inner.copy()
    merge_inner_con_valor['valor_total'] = merge_inner_con_valor['unidades_vendidas'] * merge_inner_con_valor['precio']
    print(merge_inner_con_valor)
    
    return merge_inner_con_valor

def mostrar_resumen(merge_inner, merge_left, merge_outer):
    """Muestra un resumen comparativo de todos los merges"""
    print("\n" + "="*60)
    print("RESUMEN DE TODOS LOS MERGES")
    print("="*60)
    
    print(f"\nMerge INNER: {merge_inner.shape[0]} filas")
    print("Solo productos que aparecen en ambos DataFrames")
    print(merge_inner[['id_producto', 'nombre', 'unidades_vendidas', 'precio', 'valor_total']])
    
    print(f"\nMerge LEFT: {merge_left.shape[0]} filas")
    print("Todos los registros de ventas (incluye A4 sin producto)")
    print(merge_left[['id_producto', 'nombre', 'unidades_vendidas', 'precio']])
    
    print(f"\nMerge OUTER: {merge_outer.shape[0]} filas")
    print("Todos los registros de ambos DataFrames (incluye A5 sin ventas)")
    print(merge_outer[['id_producto', 'nombre', 'unidades_vendidas', 'precio']])

def main():
    """Función principal que ejecuta todo el proceso"""
    # Crear DataFrames
    ventas, productos = crear_dataframes()
    
    # Mostrar DataFrames originales
    mostrar_dataframes(ventas, productos)
    
    # Realizar merges
    merge_inner, merge_left, merge_outer = realizar_merges(ventas, productos)
    
    # Crear columna calculada (sin modificar el DataFrame original)
    merge_inner_con_valor = crear_columna_calculada(merge_inner)
    
    # Mostrar resumen
    mostrar_resumen(merge_inner_con_valor, merge_left, merge_outer)

if __name__ == "__main__":
    main()
