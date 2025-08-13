# Script para filtrar palabras con más de 4 letras y convertirlas a mayúsculas
# Utiliza list comprehension para procesar listas de palabras de forma eficiente

# Lista original de palabras
palabras = ["python", "programación", "lista", "comprehension", "for", "if", "else", "diccionario"]

# Filtrar palabras con más de 4 letras y convertirlas a mayúsculas
# La list comprehension combina filtrado (if len(palabra) > 4) y transformación (palabra.upper())
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]
print(palabras_filtradas)
