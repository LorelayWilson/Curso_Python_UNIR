class Biblioteca:
    # Variables de clase
    total_libros = 0
    nombre_biblioteca = "Biblioteca Central"
    
    def __init__(self, nombre_seccion):
        # Variables de instancia
        self.nombre_seccion = nombre_seccion
        self.libros = []
    
    def agregar_libro(self, titulo):
        self.libros.append(titulo)
        # Incrementamos la variable de clase
        Biblioteca.total_libros += 1
    
    def obtener_informe(self):
        return f"Sección {self.nombre_seccion} de {Biblioteca.nombre_biblioteca}: {len(self.libros)} libros"

# Creamos dos instancias de la clase con diferentes secciones
seccion_ficcion = Biblioteca("Ficción")
seccion_historia = Biblioteca("Historia")

# Agregamos libros a la sección de ficción
seccion_ficcion.agregar_libro("1984")
seccion_ficcion.agregar_libro("El Señor de los Anillos")
seccion_ficcion.agregar_libro("Cien años de soledad")

# Agregamos libros a la sección de historia
seccion_historia.agregar_libro("Historia de Roma")
seccion_historia.agregar_libro("Segunda Guerra Mundial")

# Mostramos los informes de cada sección
print(seccion_ficcion.obtener_informe())
print(seccion_historia.obtener_informe())

# Verificamos que la variable de clase se comparte correctamente
print(f"Total de libros en la biblioteca: {Biblioteca.total_libros}")