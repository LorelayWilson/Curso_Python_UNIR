# Importar todas las funciones y la constante PI del módulo
from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI

def main():
    print("=== CALCULADORA USANDO MÓDULO DE OPERACIONES ===\n")
    
    # Calcular y mostrar la suma de 15 y 7
    resultado_suma = sumar(15, 7)
    print(f"Suma de 15 y 7: {resultado_suma}")
    
    # Calcular y mostrar el producto de 3.5 por 2
    resultado_multiplicacion = multiplicar(3.5, 2)
    print(f"Multiplicación de 3.5 por 2: {resultado_multiplicacion}")
    
    # Calcular y mostrar el área de un círculo con radio 5
    radio = 5
    area_circulo = PI * radio ** 2
    print(f"Área de un círculo con radio {radio}: {area_circulo:.2f}")
    
    # Mostrar algunos ejemplos adicionales
    print(f"\n=== EJEMPLOS ADICIONALES ===")
    print(f"Resta de 20 y 8: {restar(20, 8)}")
    print(f"División de 15 entre 3: {dividir(15, 3)}")
    print(f"División por cero: {dividir(10, 0)}")
    print(f"Valor de PI: {PI}")

if __name__ == "__main__":
    main()