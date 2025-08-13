# Script para solicitar entrada de números enteros con manejo de excepciones
# Captura errores de entrada inválida e interrupciones del usuario

def solicitar_numero_entero():
    """
    Función que solicita al usuario un número entero y maneja posibles errores.
    
    Returns:
        int: El número entero introducido por el usuario
    """
    try:
        # Solicitar entrada al usuario
        entrada = input("Por favor, introduce un número entero: ")
        
        # Intentar convertir la entrada a entero
        numero = int(entrada)
        
        # Si la conversión es exitosa, mostrar el resultado
        print(f"Has introducido el número: {numero}")
        return numero
        
    except ValueError:
        # Capturar error cuando la entrada no es un número entero
        print("Error: Debes introducir un número entero.")
        return None
        
    except KeyboardInterrupt:
        # Capturar interrupción del usuario (Ctrl+C)
        print("\nSe ha interrumpido la ejecución del programa.")
        return None

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("=== PROGRAMA DE ENTRADA DE NÚMEROS ENTEROS ===")
    print("Este programa solicita un número entero y maneja posibles errores.")
    print("Puedes interrumpir la ejecución con Ctrl+C.\n")
    
    # Ejecutar la función principal
    resultado = solicitar_numero_entero()
    
    # Mostrar mensaje final según el resultado
    if resultado is not None:
        print(f"\nPrograma completado exitosamente. El número procesado fue: {resultado}")
    else:
        print("\nEl programa no pudo procesar la entrada correctamente.")

# Ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()
