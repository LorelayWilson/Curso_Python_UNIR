class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def __str__(self):
        """Representación en string del libro"""
        return f"'{self.titulo}' por {self.autor} ({self.año_publicacion})"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        # Composición: la biblioteca "tiene" una colección de libros
        self.libros = []
    
    def agregar_libro(self, titulo, autor, año_publicacion):
        """Agrega un nuevo libro a la colección"""
        nuevo_libro = Libro(titulo, autor, año_publicacion)
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado exitosamente a {self.nombre}")
    
    def buscar_por_titulo(self, cadena_busqueda):
        """Busca libros cuyo título contenga la cadena de búsqueda"""
        libros_encontrados = []
        cadena_busqueda = cadena_busqueda.lower()
        
        for libro in self.libros:
            if cadena_busqueda in libro.titulo.lower():
                libros_encontrados.append(libro)
        
        return libros_encontrados
    
    def contar_libros_por_autor(self, autor):
        """Cuenta cuántos libros hay de un autor específico"""
        contador = 0
        autor = autor.lower()
        
        for libro in self.libros:
            if autor == libro.autor.lower():
                contador += 1
        
        return contador
    
    def mostrar_todos_los_libros(self):
        """Muestra todos los libros en la biblioteca"""
        if not self.libros:
            print(f"No hay libros en {self.nombre}")
            return
        
        print(f"\n=== LIBROS EN {self.nombre.upper()} ===")
        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro}")


# Ejemplo de uso para probar el sistema
if __name__ == "__main__":
    # Crear una biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Central")
    
    # Agregar algunos libros
    mi_biblioteca.agregar_libro("Don Quijote", "Miguel de Cervantes", 1605)
    mi_biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    mi_biblioteca.agregar_libro("El señor de los anillos", "J.R.R. Tolkien", 1954)
    mi_biblioteca.agregar_libro("El Quijote de la Mancha", "Miguel de Cervantes", 1605)
    mi_biblioteca.agregar_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)
    
    # Mostrar todos los libros
    mi_biblioteca.mostrar_todos_los_libros()
    
    # Buscar libros por título
    print("\n=== BÚSQUEDA POR TÍTULO ===")
    busqueda = "Quijote"
    libros_encontrados = mi_biblioteca.buscar_por_titulo(busqueda)
    if libros_encontrados:
        print(f"Libros que contienen '{busqueda}' en el título:")
        for libro in libros_encontrados:
            print(f"  - {libro}")
    else:
        print(f"No se encontraron libros con '{busqueda}' en el título")
    
    # Contar libros por autor
    print("\n=== CONTEO POR AUTOR ===")
    autores = ["Miguel de Cervantes", "Gabriel García Márquez", "J.R.R. Tolkien"]
    for autor in autores:
        cantidad = mi_biblioteca.contar_libros_por_autor(autor)
        print(f"{autor}: {cantidad} libro(s)")
    
    # Buscar un libro que no existe
    print("\n=== BÚSQUEDA SIN RESULTADOS ===")
    busqueda_vacia = mi_biblioteca.buscar_por_titulo("Harry Potter")
    if not busqueda_vacia:
        print("No se encontraron libros con 'Harry Potter' en el título")