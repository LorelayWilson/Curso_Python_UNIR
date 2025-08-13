class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        return f"{self.titulo} escrito por {self.autor} - {self.paginas} páginas."

    def es_largo(self):
        if self.paginas > 300:
            return True
        return False

    def resumir(self, longitud = 50):
        return f"{self.titulo} - Resumen de {longitud} caracteres."
    

libro1 = Libro("Titulo1", "Autor1", 70)
libro2 = Libro("Titulo2", "Autor2", 100)

print(libro1.describir())
print(libro2.describir())
print(libro1.es_largo())
print(libro1.resumir())
print(libro2.resumir(80))