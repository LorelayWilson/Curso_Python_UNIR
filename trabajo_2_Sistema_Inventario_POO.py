"""
Sistema Básico de Inventario con POO
Desarrollado para gestionar productos y realizar operaciones de inventario
"""

class Producto:
    """Clase para representar un producto en el inventario"""
    
    def __init__(self, nombre, precio, cantidad):
        """
        Constructor de la clase Producto
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            cantidad (int): Cantidad en inventario
            
        Raises:
            ValueError: Si los parámetros no cumplen las validaciones
        """
        if not nombre or not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")
        
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero")
        
        self._nombre = nombre.strip()
        self._precio = float(precio)
        self._cantidad = cantidad
    
    @property
    def nombre(self):
        """Getter para el nombre del producto"""
        return self._nombre
    
    @property
    def precio(self):
        """Getter para el precio del producto"""
        return self._precio
    
    @property
    def cantidad(self):
        """Getter para la cantidad del producto"""
        return self._cantidad
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es negativo o no es un número
        """
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        
        self._precio = float(nuevo_precio)
        print(f"Precio actualizado exitosamente para {self._nombre}: ${self._precio:.2f}")
    
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto
        
        Args:
            nueva_cantidad (int): Nueva cantidad del producto
            
        Raises:
            ValueError: Si la cantidad es negativa o no es un entero
        """
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a cero")
        
        self._cantidad = nueva_cantidad
        print(f"Cantidad actualizada exitosamente para {self._nombre}: {self._cantidad} unidades")
    
    def calcular_valor_total(self):
        """
        Calcula el valor total del producto (precio × cantidad)
        
        Returns:
            float: Valor total del producto
        """
        return self._precio * self._cantidad
    
    def __str__(self):
        """
        Representación en cadena del producto
        
        Returns:
            str: Información del producto formateada
        """
        valor_total = self.calcular_valor_total()
        return f"Producto: {self._nombre} | Precio: ${self._precio:.2f} | Cantidad: {self._cantidad} | Valor Total: ${valor_total:.2f}"


class Inventario:
    """Clase para gestionar el inventario de productos"""
    
    def __init__(self):
        """Constructor de la clase Inventario"""
        self._productos = []
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario
        
        Args:
            producto (Producto): Objeto de tipo Producto
            
        Raises:
            TypeError: Si el objeto no es de tipo Producto
        """
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser de tipo Producto")
        
        # Verificar si ya existe un producto con el mismo nombre
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            print(f"Ya existe un producto con el nombre '{producto.nombre}' en el inventario.")
            respuesta = input("¿Desea actualizar la cantidad existente? (s/n): ").lower()
            if respuesta == 's':
                nueva_cantidad = producto_existente.cantidad + producto.cantidad
                producto_existente.actualizar_cantidad(nueva_cantidad)
                return
            else:
                print("Producto no agregado.")
                return
        
        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado exitosamente al inventario.")
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto: Objeto Producto si se encuentra, None si no existe
        """
        if not nombre or not isinstance(nombre, str):
            return None
        
        nombre = nombre.strip().lower()
        for producto in self._productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None
    
    def calcular_valor_inventario(self):
        """
        Calcula el valor total del inventario
        
        Returns:
            float: Valor total de todos los productos en inventario
        """
        return sum(producto.calcular_valor_total() for producto in self._productos)
    
    def listar_productos(self):
        """
        Lista todos los productos del inventario
        """
        if not self._productos:
            print("\n" + "="*50)
            print("El inventario está vacío.")
            print("="*50)
            return
        
        print("\n" + "="*50)
        print("LISTADO DE PRODUCTOS EN INVENTARIO")
        print("="*50)
        for i, producto in enumerate(self._productos, 1):
            print(f"{i}. {producto}")
        print("="*50)
        print(f"Total de productos: {len(self._productos)}")
        print(f"Valor total del inventario: ${self.calcular_valor_inventario():.2f}")
        print("="*50)


def obtener_numero(mensaje, tipo=float, minimo=0):
    """
    Función auxiliar para obtener y validar entrada numérica del usuario
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        tipo (type): Tipo de dato esperado (int o float)
        minimo (float): Valor mínimo permitido
        
    Returns:
        int/float: Número validado
    """
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}")
                continue
            return valor
        except ValueError:
            print(f"Error: Debe ingresar un número válido.")


def menu_principal():
    """Función que muestra el menú principal y gestiona las opciones del usuario"""
    inventario = Inventario()
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE INVENTARIO - MENÚ PRINCIPAL")
        print("="*50)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar todos los productos")
        print("4. Calcular valor total del inventario")
        print("5. Actualizar precio de producto")
        print("6. Actualizar cantidad de producto")
        print("7. Salir")
        print("="*50)
        
        try:
            opcion = input("Seleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                # Agregar producto
                print("\n--- AGREGAR NUEVO PRODUCTO ---")
                try:
                    nombre = input("Ingrese el nombre del producto: ").strip()
                    if not nombre:
                        print("Error: El nombre no puede estar vacío.")
                        continue
                    
                    precio = obtener_numero("Ingrese el precio del producto: $", float, 0)
                    cantidad = obtener_numero("Ingrese la cantidad: ", int, 0)
                    
                    producto = Producto(nombre, precio, cantidad)
                    inventario.agregar_producto(producto)
                    
                except ValueError as e:
                    print(f"Error al crear el producto: {e}")
                
            elif opcion == "2":
                # Buscar producto
                print("\n--- BUSCAR PRODUCTO ---")
                nombre = input("Ingrese el nombre del producto a buscar: ").strip()
                if not nombre:
                    print("Error: Debe ingresar un nombre.")
                    continue
                
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print("Producto encontrado:")
                    print(producto)
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "3":
                # Listar productos
                inventario.listar_productos()
                
            elif opcion == "4":
                # Calcular valor total
                valor_total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${valor_total:.2f}")
                
            elif opcion == "5":
                # Actualizar precio
                print("\n--- ACTUALIZAR PRECIO ---")
                nombre = input("Ingrese el nombre del producto: ").strip()
                if not nombre:
                    print("Error: Debe ingresar un nombre.")
                    continue
                
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Precio actual: ${producto.precio:.2f}")
                    try:
                        nuevo_precio = obtener_numero("Ingrese el nuevo precio: $", float, 0)
                        producto.actualizar_precio(nuevo_precio)
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "6":
                # Actualizar cantidad
                print("\n--- ACTUALIZAR CANTIDAD ---")
                nombre = input("Ingrese el nombre del producto: ").strip()
                if not nombre:
                    print("Error: Debe ingresar un nombre.")
                    continue
                
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Cantidad actual: {producto.cantidad}")
                    try:
                        nueva_cantidad = obtener_numero("Ingrese la nueva cantidad: ", int, 0)
                        producto.actualizar_cantidad(nueva_cantidad)
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "7":
                # Salir
                print("\n¡Gracias por usar el Sistema de Inventario!")
                print("¡Hasta pronto!")
                break
                
            else:
                print("Error: Opción no válida. Por favor seleccione una opción del 1 al 7.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


def main():
    """Función principal del programa"""
    print("="*50)
    print("BIENVENIDO AL SISTEMA DE INVENTARIO")
    print("="*50)
    print("Este sistema te permite gestionar productos de manera eficiente.")
    print("Puedes agregar, buscar, listar y actualizar productos en tu inventario.")
    
    try:
        menu_principal()
    except Exception as e:
        print(f"Error crítico en el sistema: {e}")
        print("El programa se cerrará.")


if __name__ == "__main__":
    main()
