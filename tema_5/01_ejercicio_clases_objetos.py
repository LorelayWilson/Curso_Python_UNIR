class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        
        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        """
        Método que devuelve una presentación de la persona.
        
        Returns:
            str: Un mensaje de presentación con el nombre y la edad.
        """
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"


# Crear una instancia de la clase Persona
mi_persona = Persona("Ana", 30)

# Llamar al método presentarse y mostrar el resultado
presentacion = mi_persona.presentarse()
print(presentacion)