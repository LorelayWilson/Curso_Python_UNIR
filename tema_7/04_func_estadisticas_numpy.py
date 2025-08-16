import numpy as np

# Datos de temperaturas para tres ciudades
temperaturas = np.array([
    [25, 28, 30, 32, 29, 27, 26, 25, 24, 28, 31, 30, 29, 28, 27, 29, 30, 31, 32, 33, 34, 31, 29, 28, 27, 26, 25, 24, 25, 26],  # Ciudad A
    [18, 17, 19, 20, 21, 20, 19, 18, 17, 16, 15, 16, 17, 18, 19, 20, 21, 22, 21, 20, 19, 18, 17, 16, 15, 14, 15, 16, 17, 18],  # Ciudad B
    [31, 32, 33, 34, 35, 36, 35, 34, 33, 32, 31, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 38, 36, 34, 32, 30, 31, 32, 33]   # Ciudad C
])

ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

print("ANÁLISIS DE TEMPERATURAS")
print("=" * 30)

# Análisis para cada ciudad
for i, ciudad in enumerate(ciudades):
    datos = temperaturas[i]
    
    print(f"\n{ciudad}:")
    print(f"  Media: {np.mean(datos):.1f}°C")
    print(f"  Máximo: {np.max(datos)}°C")
    print(f"  Mínimo: {np.min(datos)}°C")
    print(f"  Mediana: {np.median(datos):.1f}°C")
    
    # IQR simple
    Q1 = np.percentile(datos, 25)
    Q3 = np.percentile(datos, 75)
    IQR = Q3 - Q1
    print(f"  IQR: {IQR:.1f}°C")
    
    # Outliers básicos
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    outliers = datos[(datos < limite_inf) | (datos > limite_sup)]
    print(f"  Outliers: {outliers}")

print(f"\nMedia global: {np.mean(temperaturas):.1f}°C")
