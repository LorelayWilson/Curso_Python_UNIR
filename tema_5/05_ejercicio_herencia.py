class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año})"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, Puertas: {self.puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        info_basica = super().mostrar_info()
        return f"{info_basica}, Cilindrada: {self.cilindrada}cc"

# Crear instancias de las clases derivadas
auto = Automovil("Toyota", "Corolla", 2022, 4)
moto = Motocicleta("Honda", "CBR", 2021, 600)

# Mostrar información de cada vehículo
print(auto.mostrar_info())
print(moto.mostrar_info())