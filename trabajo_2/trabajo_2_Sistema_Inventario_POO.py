"""
Sistema Básico de Inventario con POO
Desarrollado para gestionar productos y realizar operaciones de inventario

Autor: Lorelay Pricop Florescu
Titulación: Graduada en Tecnología Interactiva
Perfil Profesional: Tecnóloga y Project Manager
Contacto: lorelaypricop@gmail.com
LinkedIn: https://www.linkedin.com/in/lorelaypricop
Formación Actual: Máster Universitario en Inteligencia Artificial - UNIR
Especialidad: IA Generativa para Aplicaciones Empresariales

Trabajo 2 - Curso de Programación en Python
Universidad Internacional de La Rioja (UNIR)
Desarrollado en: Agosto 2025

NOTA DE TRANSPARENCIA ACADÉMICA:
- Código fuente: 100% desarrollado por la autora
- Documentación: Elaborada con asistencia de IA Generativa
- Lógica y algoritmos: Competencias auténticas en POO

© Agosto 2025
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
        # Usar los setters para validaciones
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def nombre(self):
        """Getter para el nombre del producto"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        """Setter para el nombre con validación"""
        if not value or not isinstance(value, str) or value.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío y debe ser una cadena de texto")
        self._nombre = value.strip()
    
    @property
    def precio(self):
        """Getter para el precio del producto"""
        return self._precio
    
    @precio.setter
    def precio(self, value):
        """Setter para el precio con validación"""
        if not isinstance(value, (int, float)):
            raise TypeError(f"El precio debe ser un número, se recibió: {type(value).__name__}")
        if value < 0:
            raise ValueError(f"El precio debe ser positivo, se recibió: {value}")
        self._precio = float(value)
    
    @property
    def cantidad(self):
        """Getter para la cantidad del producto"""
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        """Setter para la cantidad con validación"""
        if not isinstance(value, int):
            raise TypeError(f"La cantidad debe ser un número entero, se recibió: {type(value).__name__}")
        if value < 0:
            raise ValueError(f"La cantidad debe ser mayor o igual a cero, se recibió: {value}")
        self._cantidad = value
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto usando el setter
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es negativo o no es un número
        """
        precio_anterior = self._precio
        try:
            self.precio = nuevo_precio
            print(f"Precio actualizado exitosamente para {self._nombre}: ${precio_anterior:.2f} → ${self._precio:.2f}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error al actualizar precio: {e}")
    
    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto usando el setter
        
        Args:
            nueva_cantidad (int): Nueva cantidad del producto
            
        Raises:
            ValueError: Si la cantidad es negativa o no es un entero
        """
        cantidad_anterior = self._cantidad
        try:
            self.cantidad = nueva_cantidad
            print(f"Cantidad actualizada exitosamente para {self._nombre}: {cantidad_anterior} → {self._cantidad} unidades")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error al actualizar cantidad: {e}")
    
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
    
    def __init__(self, actualizacion_automatica=False):
        """
        Constructor de la clase Inventario
        
        Args:
            actualizacion_automatica (bool): Si True, actualiza automáticamente 
                                            la cantidad al agregar productos duplicados
        """
        self._productos = []
        self._actualizacion_automatica = actualizacion_automatica
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario
        
        Args:
            producto (Producto): Objeto de tipo Producto
            
        Raises:
            TypeError: Si el objeto no es de tipo Producto
        """
        if not isinstance(producto, Producto):
            raise TypeError(f"El objeto debe ser de tipo Producto, se recibió: {type(producto).__name__}")
        
        # Verificar si ya existe un producto con el mismo nombre
        producto_existente = self.buscar_producto(producto.nombre)
        if producto_existente:
            if self._actualizacion_automatica:
                # Actualización automática sin confirmación
                cantidad_anterior = producto_existente.cantidad
                nueva_cantidad = cantidad_anterior + producto.cantidad
                producto_existente.actualizar_cantidad(nueva_cantidad)
                print(f"Producto '{producto.nombre}' ya existía. Cantidad actualizada automáticamente: {cantidad_anterior} + {producto.cantidad} = {nueva_cantidad}")
                return
            else:
                # Pedir confirmación al usuario
                print(f"Ya existe un producto con el nombre '{producto.nombre}' en el inventario.")
                print(f"Cantidad actual: {producto_existente.cantidad}, Cantidad a agregar: {producto.cantidad}")
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
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario por su nombre
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto válida")
        
        nombre = nombre.strip().lower()
        for i, producto in enumerate(self._productos):
            if producto.nombre.lower() == nombre:
                producto_eliminado = self._productos.pop(i)
                print(f"Producto '{producto_eliminado.nombre}' eliminado exitosamente del inventario.")
                return True
        
        print(f"No se encontró ningún producto con el nombre '{nombre}' para eliminar.")
        return False
    
    def configurar_actualizacion_automatica(self, activar):
        """
        Configura el modo de actualización automática
        
        Args:
            activar (bool): True para activar, False para desactivar
        """
        self._actualizacion_automatica = bool(activar)
        estado = "activada" if self._actualizacion_automatica else "desactivada"
        print(f"Actualización automática {estado}.")


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
            entrada = input(mensaje).strip()
            if not entrada:
                print("Error: No se puede dejar vacío. Por favor ingrese un valor.")
                continue
            
            valor = tipo(entrada)
            if valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}. Valor ingresado: {valor}")
                continue
            return valor
        except ValueError as e:
            tipo_nombre = "número entero" if tipo == int else "número decimal"
            print(f"Error: Debe ingresar un {tipo_nombre} válido. Valor ingresado: '{entrada}'")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor inténtelo de nuevo.")


def menu_principal():
    """Función que muestra el menú principal y gestiona las opciones del usuario"""
    inventario = Inventario(actualizacion_automatica=False)
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE INVENTARIO - MENÚ PRINCIPAL")
        print("="*60)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar todos los productos")
        print("4. Calcular valor total del inventario")
        print("5. Actualizar precio de producto")
        print("6. Actualizar cantidad de producto")
        print("7. Eliminar producto")
        print("8. Configurar actualización automática")
        print("9. Salir")
        print("="*60)
        
        try:
            opcion = input("Seleccione una opción (1-9): ").strip()
            
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
                    
                except (ValueError, TypeError) as e:
                    print(f"Error al crear el producto: {e}")
                except Exception as e:
                    print(f"Error inesperado al crear el producto: {e}")
                
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
                    except (ValueError, TypeError) as e:
                        print(f"Error al actualizar precio: {e}")
                    except Exception as e:
                        print(f"Error inesperado: {e}")
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
                    except (ValueError, TypeError) as e:
                        print(f"Error al actualizar cantidad: {e}")
                    except Exception as e:
                        print(f"Error inesperado: {e}")
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "7":
                # Eliminar producto
                print("\n--- ELIMINAR PRODUCTO ---")
                nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
                if not nombre:
                    print("Error: Debe ingresar un nombre.")
                    continue
                
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print(f"Producto encontrado: {producto}")
                    confirmacion = input(f"¿Está seguro de que desea eliminar '{producto.nombre}'? (s/n): ").lower()
                    if confirmacion == 's':
                        try:
                            inventario.eliminar_producto(nombre)
                        except ValueError as e:
                            print(f"Error al eliminar producto: {e}")
                        except Exception as e:
                            print(f"Error inesperado: {e}")
                    else:
                        print("Eliminación cancelada.")
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "8":
                # Configurar actualización automática
                print("\n--- CONFIGURACIÓN DE ACTUALIZACIÓN AUTOMÁTICA ---")
                estado_actual = "activada" if inventario._actualizacion_automatica else "desactivada"
                print(f"Estado actual: {estado_actual}")
                print("La actualización automática permite agregar cantidades de productos")
                print("duplicados sin solicitar confirmación.")
                
                respuesta = input("¿Desea activar la actualización automática? (s/n): ").lower()
                if respuesta == 's':
                    inventario.configurar_actualizacion_automatica(True)
                elif respuesta == 'n':
                    inventario.configurar_actualizacion_automatica(False)
                else:
                    print("Opción no válida. Configuración sin cambios.")
                
            elif opcion == "9":
                # Salir
                print("\n¡Gracias por usar el Sistema de Inventario!")
                print("¡Hasta pronto!")
                break
                
            else:
                print("Error: Opción no válida. Por favor seleccione una opción del 1 al 9.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("¡Hasta pronto!")
            break
        except Exception as e:
            print(f"Error inesperado en el menú principal: {e}")
            print("Por favor inténtelo de nuevo o contacte al administrador del sistema.")


def main():
    """Función principal del programa"""
    print("="*60)
    print("BIENVENIDO AL SISTEMA DE INVENTARIO - VERSIÓN MEJORADA")
    print("="*60)
    print("Este sistema te permite gestionar productos de manera eficiente.")
    print("Funcionalidades disponibles:")
    print("• Agregar, buscar, listar, actualizar y eliminar productos")
    print("• Calcular valor total del inventario")
    print("• Configuración de actualización automática")
    print("• Validaciones robustas y manejo de errores")
    print("="*60)
    
    try:
        menu_principal()
    except Exception as e:
        print(f"Error crítico en el sistema: {e}")
        print("El programa se cerrará.")


if __name__ == "__main__":
    main()
