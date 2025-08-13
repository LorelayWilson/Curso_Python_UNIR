# Constante PI
PI = 3.14159

def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números"""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de dos números"""
    return a * b

def dividir(a, b):
    """Devuelve la división de a entre b, maneja división por cero"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b