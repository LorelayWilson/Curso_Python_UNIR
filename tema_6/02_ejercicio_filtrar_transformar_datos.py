# Script para filtrar números pares y duplicar sus valores
# Utiliza las funciones filter() y map() para procesar listas de números

def procesar_numeros(lista_numeros):
    """
    Función que filtra números pares y los duplica usando filter() y map().
    
    Args:
        lista_numeros (list): Lista de números enteros
        
    Returns:
        list: Lista con los números pares duplicados
    """
    # Filtrar solo los números pares usando filter()
    numeros_pares = filter(lambda x: x % 2 == 0, lista_numeros)
    
    # Duplicar cada número par usando map()
    numeros_duplicados = map(lambda x: x * 2, numeros_pares)
    
    # Convertir el resultado a lista y retornarlo
    return list(numeros_duplicados)

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo del enunciado
    lista_ejemplo = [1, 2, 3, 4, 5, 6]
    
    print(f"Lista original: {lista_ejemplo}")
    resultado = procesar_numeros(lista_ejemplo)
    print(f"Resultado: {resultado}")
    
    # Verificación del ejemplo solicitado
    # [1, 2, 3, 4, 5, 6] → números pares: [2, 4, 6] → duplicados: [4, 8, 12]
    print(f"Verificación: 2*2=4, 4*2=8, 6*2=12 → [4, 8, 12] ✓")
