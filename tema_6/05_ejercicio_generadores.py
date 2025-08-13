# Script para generar números de la secuencia de Fibonacci
# Utiliza generadores para producir valores de forma eficiente en memoria

def fibonacci_generator(n):
    """
    Generador que produce los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n (int): Cantidad de números de Fibonacci a generar
        
    Yields:
        int: Números de la secuencia de Fibonacci uno por uno
        
    Raises:
        TypeError: Si n no es un entero
    """
    # Verificar que n sea un entero
    if not isinstance(n, int):
        raise TypeError("El parámetro n debe ser un entero")
    
    # Verificar que n sea válido
    if n <= 0:
        return
    
    # Generar la secuencia usando un bucle simple
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ejemplo de uso
if __name__ == "__main__":
    # Probar con diferentes valores de n
    print("=== GENERADOR DE FIBONACCI ===")
    
    # Caso del ejemplo: n = 6
    print(f"\nGenerando los primeros 6 números de Fibonacci:")
    for numero in fibonacci_generator(6):
        print(numero, end=" ")
    
    # Casos adicionales para demostrar el funcionamiento
    print(f"\n\nGenerando los primeros 10 números de Fibonacci:")
    for numero in fibonacci_generator(10):
        print(numero, end=" ")
    
    # Caso límite: n = 0
    print(f"\n\nProbando con n = 0 (no debe generar nada):")
    resultado = list(fibonacci_generator(0))
    print(f"Resultado: {resultado}")
    
    # Caso límite: n = 1
    print(f"\nProbando con n = 1:")
    for numero in fibonacci_generator(1):
        print(numero, end=" ")
    
    # Prueba de robustez: tipo incorrecto
    print(f"\n\nProbando robustez con tipo incorrecto:")
    try:
        for numero in fibonacci_generator(3.5):
            print(numero, end=" ")
    except TypeError as e:
        print(f"Error capturado: {e}")
