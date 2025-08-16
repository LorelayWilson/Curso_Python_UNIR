import numpy as np

# Generar un array tridimensional de tamaño 4x3x2 con valores aleatorios enteros entre 1 y 100
array_3d = np.random.randint(1, 101, size=(4, 3, 2))

print("Array tridimensional generado:")
print(array_3d)
print("\n" + "="*50)
print("INFORMACIÓN SOBRE EL ARRAY")
print("="*50)

# Mostrar la forma (shape) del array
print(f"Forma (shape) del array: {array_3d.shape}")

# Mostrar el número de dimensiones (ndim) del array
print(f"Número de dimensiones (ndim): {array_3d.ndim}")

# Mostrar el número total de elementos (size) del array
print(f"Número total de elementos (size): {array_3d.size}")

# Mostrar el tipo de datos (dtype) del array
print(f"Tipo de datos (dtype): {array_3d.dtype}")

# Mostrar el tamaño en bytes de cada elemento (itemsize) del array
print(f"Tamaño en bytes de cada elemento (itemsize): {array_3d.itemsize}")

# Mostrar el tamaño total en bytes (nbytes) del array
print(f"Tamaño total en bytes (nbytes): {array_3d.nbytes}")

print("\n" + "="*50)
print("VERIFICACIÓN")
print("="*50)

# Verificar si el tamaño total en bytes es igual al producto del número de elementos por el tamaño de cada elemento
producto_calculado = array_3d.size * array_3d.itemsize
print(f"Producto calculado (size × itemsize): {array_3d.size} × {array_3d.itemsize} = {producto_calculado}")
print(f"Tamaño total en bytes (nbytes): {array_3d.nbytes}")

if array_3d.nbytes == producto_calculado:
    print("✓ VERIFICACIÓN EXITOSA: nbytes = size × itemsize")
else:
    print("✗ VERIFICACIÓN FALLIDA: nbytes ≠ size × itemsize")

print("\n" + "="*50)
print("EXPLICACIÓN DE LOS ATRIBUTOS")
print("="*50)
print("• shape: Tupla que indica el tamaño de cada dimensión")
print("• ndim: Número de dimensiones del array")
print("• size: Número total de elementos en el array")
print("• dtype: Tipo de datos de los elementos del array")
print("• itemsize: Tamaño en bytes de cada elemento individual")
print("• nbytes: Tamaño total en bytes del array completo")
