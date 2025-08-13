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

# ===========================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================

class ProductoNoEncontrado(Exception):
    """Excepción lanzada cuando no se encuentra un producto en el inventario"""
    pass

class ProductoInvalido(Exception):
    """Excepción lanzada cuando los datos del producto son inválidos"""
    pass

class InventarioVacio(Exception):
    """Excepción lanzada cuando se intenta operar en un inventario vacío"""
    pass

# ===========================================
# CLASE PRODUCTO
# ===========================================

class Producto:
    """
    Clase para representar un producto individual en el inventario.
    
    Esta clase encapsula toda la información y comportamiento relacionado
    con un producto, incluyendo validaciones robustas para mantener
    la integridad de los datos.
    
    Attributes:
        _nombre (str): Nombre del producto (validado, no vacío)
        _precio (float): Precio unitario del producto (validado, ≥ 0)
        _cantidad (int): Cantidad disponible en inventario (validado, ≥ 0)
    
    Methods:
        actualizar_precio: Modifica el precio con validación
        actualizar_cantidad: Modifica la cantidad con validación
        actualizar_atributos: Actualiza precio y cantidad simultáneamente
        calcular_valor_total: Calcula el valor total del stock
        __str__: Representación textual del producto
    """
    
    def __init__(self, nombre: str, precio: float, cantidad: int):
        """
        Inicializa un nuevo producto con validaciones automáticas.
        
        Args:
            nombre (str): Nombre del producto (no puede estar vacío)
            precio (float): Precio unitario (debe ser ≥ 0)
            cantidad (int): Cantidad en inventario (debe ser ≥ 0)
            
        Raises:
            ValueError: Si nombre está vacío, precio es negativo, o cantidad es negativa
            TypeError: Si los tipos de datos no son correctos
            
        Example:
            >>> producto = Producto("Laptop", 999.99, 5)
            >>> print(producto)
            Producto: Laptop | Precio: $999.99 | Cantidad: 5 | Valor Total: $4999.95
        """
        # Usar los setters para validaciones automáticas
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre del producto.
        
        Returns:
            str: Nombre del producto (sin espacios extra)
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        """
        Establece el nombre del producto con validación.
        
        Args:
            value (str): Nuevo nombre del producto
            
        Raises:
            ValueError: Si el nombre está vacío o solo contiene espacios
            TypeError: Si el valor no es una cadena de texto
            
        Example:
            >>> producto.nombre = "  Laptop Dell  "
            >>> producto.nombre
            'Laptop Dell'
        """
        if not value or not isinstance(value, str) or value.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío y debe ser una cadena de texto")
        self._nombre = value.strip()
    
    @property
    def precio(self) -> float:
        """
        Obtiene el precio unitario del producto.
        
        Returns:
            float: Precio del producto (siempre ≥ 0)
        """
        return self._precio
    
    @precio.setter
    def precio(self, value: float) -> None:
        """
        Establece el precio del producto con validación.
        
        Args:
            value (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es negativo
            TypeError: Si el valor no es numérico
            
        Example:
            >>> producto.precio = 1299.99
            >>> producto.precio
            1299.99
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"El precio debe ser un número, se recibió: {type(value).__name__}")
        if value < 0:
            raise ValueError(f"El precio debe ser positivo, se recibió: {value}")
        self._precio = float(value)
    
    @property
    def cantidad(self) -> int:
        """
        Obtiene la cantidad disponible del producto.
        
        Returns:
            int: Cantidad en inventario (siempre ≥ 0)
        """
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, value: int) -> None:
        """
        Establece la cantidad del producto con validación.
        
        Args:
            value (int): Nueva cantidad del producto
            
        Raises:
            ValueError: Si la cantidad es negativa
            TypeError: Si el valor no es un entero
            
        Example:
            >>> producto.cantidad = 25
            >>> producto.cantidad
            25
        """
        if not isinstance(value, int):
            raise TypeError(f"La cantidad debe ser un número entero, se recibió: {type(value).__name__}")
        if value < 0:
            raise ValueError(f"La cantidad debe ser mayor o igual a cero, se recibió: {value}")
        self._cantidad = value
    
    def actualizar_precio(self, nuevo_precio: float) -> None:
        """
        Actualiza el precio del producto usando el setter con validación.
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
            
        Raises:
            ValueError: Si el precio es negativo o no es un número válido
            
        Example:
            >>> producto.actualizar_precio(1299.99)
            Precio actualizado exitosamente para Laptop: $999.99 → $1299.99
        """
        precio_anterior = self._precio
        try:
            self.precio = nuevo_precio
            print(f"Precio actualizado exitosamente para {self._nombre}: ${precio_anterior:.2f} → ${self._precio:.2f}")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error al actualizar precio: {e}")
    
    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        """
        Actualiza la cantidad del producto usando el setter con validación.
        
        Args:
            nueva_cantidad (int): Nueva cantidad del producto
            
        Raises:
            ValueError: Si la cantidad es negativa o no es un entero válido
            
        Example:
            >>> producto.actualizar_cantidad(30)
            Cantidad actualizada exitosamente para Laptop: 25 → 30 unidades
        """
        cantidad_anterior = self._cantidad
        try:
            self.cantidad = nueva_cantidad
            print(f"Cantidad actualizada exitosamente para {self._nombre}: {cantidad_anterior} → {self._cantidad} unidades")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error al actualizar cantidad: {e}")
    
    def actualizar_atributos(self, nuevo_precio: float = None, nueva_cantidad: int = None) -> None:
        """
        Actualiza precio y/o cantidad del producto en una sola operación.
        
        Este método permite actualizar ambos atributos simultáneamente,
        lo que es útil para operaciones de sincronización o actualizaciones
        masivas de productos.
        
        Args:
            nuevo_precio (float, optional): Nuevo precio del producto. Si es None, no se modifica
            nueva_cantidad (int, optional): Nueva cantidad del producto. Si es None, no se modifica
            
        Raises:
            ValueError: Si alguno de los valores es inválido
            
        Example:
            >>> producto.actualizar_atributos(nuevo_precio=1199.99, nueva_cantidad=35)
            Atributos actualizados exitosamente para Laptop:
            - Precio: $1299.99 → $1199.99
            - Cantidad: 30 → 35 unidades
        """
        cambios = []
        
        if nuevo_precio is not None:
            precio_anterior = self._precio
            self.precio = nuevo_precio
            cambios.append(f"Precio: ${precio_anterior:.2f} → ${self._precio:.2f}")
        
        if nueva_cantidad is not None:
            cantidad_anterior = self._cantidad
            self.cantidad = nueva_cantidad
            cambios.append(f"Cantidad: {cantidad_anterior} → {self._cantidad} unidades")
        
        if cambios:
            print(f"Atributos actualizados exitosamente para {self._nombre}:")
            for cambio in cambios:
                print(f"  - {cambio}")
        else:
            print("No se especificaron cambios para realizar.")
    
    def calcular_valor_total(self) -> float:
        """
        Calcula el valor total del producto (precio × cantidad).
        
        Returns:
            float: Valor total del stock del producto
            
        Example:
            >>> producto.calcular_valor_total()
            4999.95
        """
        return self._precio * self._cantidad
    
    def __str__(self) -> str:
        """
        Representación en cadena del producto para visualización.
        
        Returns:
            str: Cadena formateada con toda la información del producto
            
        Example:
            >>> print(producto)
            Producto: Laptop | Precio: $999.99 | Cantidad: 5 | Valor Total: $4999.95
        """
        return f"Producto: {self._nombre} | Precio: ${self._precio:.2f} | Cantidad: {self._cantidad} | Valor Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    """
    Clase para gestionar una colección de productos con operaciones CRUD completas.
    
    Esta clase implementa todas las operaciones necesarias para gestionar
    un inventario de productos, incluyendo manejo inteligente de duplicados
    y configuración flexible de comportamiento.
    
    Attributes:
        _productos (List[Producto]): Lista de productos en el inventario
        _actualizacion_automatica (bool): Configuración para manejo automático de duplicados
    
    Methods:
        agregar_producto: Añade un producto al inventario
        buscar_producto: Busca un producto por nombre
        eliminar_producto: Elimina un producto del inventario
        listar_productos: Muestra todos los productos
        calcular_valor_inventario: Calcula el valor total del inventario
        configurar_actualizacion_automatica: Cambia la configuración de duplicados
        exportar_inventario: Exporta el inventario a un archivo
        mostrar_resumen: Muestra un resumen rápido del inventario
    """
    
    def __init__(self, actualizacion_automatica: bool = False):
        """
        Inicializa un inventario vacío con configuración opcional.
        
        Args:
            actualizacion_automatica (bool): Si True, actualiza automáticamente 
                                            la cantidad al agregar productos duplicados.
                                            Si False, pide confirmación al usuario.
                                            
        Example:
            >>> inventario = Inventario(actualizacion_automatica=True)
            >>> inventario._actualizacion_automatica
            True
        """
        self._productos = []
        self._actualizacion_automatica = actualizacion_automatica
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto al inventario con manejo inteligente de duplicados.
        
        Si el producto ya existe, el comportamiento depende de la configuración:
        - actualizacion_automatica=True: Actualiza automáticamente la cantidad
        - actualizacion_automatica=False: Pide confirmación al usuario
        
        Args:
            producto (Producto): Objeto de tipo Producto a agregar
            
        Raises:
            TypeError: Si el objeto no es de tipo Producto
            ProductoInvalido: Si el producto tiene datos inválidos
            
        Example:
            >>> inventario.agregar_producto(Producto("Mouse", 25.99, 10))
            Producto 'Mouse' agregado exitosamente al inventario.
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
    
    def mostrar_resumen(self) -> None:
        """
        Muestra un resumen rápido del inventario tras operaciones.
        
        Este método proporciona información concisa sobre el estado
        actual del inventario, útil para mostrar después de cada operación.
        
        Example:
            >>> inventario.mostrar_resumen()
            📊 RESUMEN RÁPIDO: 3 productos | Valor total: $1,245.98
        """
        if not self._productos:
            print("📊 RESUMEN RÁPIDO: Inventario vacío")
            return
        
        total_productos = len(self._productos)
        valor_total = self.calcular_valor_inventario()
        print(f"📊 RESUMEN RÁPIDO: {total_productos} productos | Valor total: ${valor_total:,.2f}")
    
    def buscar_producto(self, nombre: str) -> Producto:
        """
        Busca un producto por su nombre (búsqueda case-insensitive).
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto: Objeto Producto si se encuentra, None si no existe
            
        Raises:
            ValueError: Si el nombre está vacío o no es una cadena válida
            
        Example:
            >>> producto = inventario.buscar_producto("laptop dell")
            >>> if producto:
            ...     print(f"Encontrado: {producto}")
            ... else:
            ...     print("Producto no encontrado")
        """
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre del producto no puede estar vacío y debe ser una cadena de texto")
        
        nombre = nombre.strip().lower()
        for producto in self._productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None
    
    def exportar_inventario(self, nombre_archivo: str = "inventario_exportado.txt") -> None:
        """
        Exporta el inventario completo a un archivo de texto.
        
        Este método crea un archivo con toda la información del inventario,
        útil para respaldos o análisis externos.
        
        Args:
            nombre_archivo (str): Nombre del archivo de salida (por defecto: inventario_exportado.txt)
            
        Raises:
            IOError: Si hay problemas al escribir el archivo
            
        Example:
            >>> inventario.exportar_inventario("mi_inventario.txt")
            Inventario exportado exitosamente a: mi_inventario.txt
        """
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write("=" * 60 + "\n")
                archivo.write("EXPORTACIÓN DE INVENTARIO\n")
                archivo.write("=" * 60 + "\n")
                archivo.write(f"Fecha de exportación: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                archivo.write(f"Total de productos: {len(self._productos)}\n")
                archivo.write(f"Valor total del inventario: ${self.calcular_valor_inventario():.2f}\n")
                archivo.write("=" * 60 + "\n\n")
                
                for i, producto in enumerate(self._productos, 1):
                    archivo.write(f"{i}. {producto}\n")
                
                archivo.write("\n" + "=" * 60 + "\n")
                archivo.write("FIN DE EXPORTACIÓN\n")
                archivo.write("=" * 60 + "\n")
            
            print(f"Inventario exportado exitosamente a: {nombre_archivo}")
            
        except IOError as e:
            print(f"Error al exportar el inventario: {e}")
            raise IOError(f"No se pudo exportar el inventario: {e}")
    
    def calcular_valor_inventario(self) -> float:
        """
        Calcula el valor total del inventario sumando todos los productos.
        
        Returns:
            float: Valor total de todos los productos en inventario
            
        Example:
            >>> valor_total = inventario.calcular_valor_inventario()
            >>> print(f"Valor total: ${valor_total:,.2f}")
            Valor total: $1,245.98
        """
        return sum(producto.calcular_valor_total() for producto in self._productos)
    
    def listar_productos(self, ordenar_por: str = "nombre") -> None:
        """
        Lista todos los productos del inventario con opciones de ordenamiento.
        
        Args:
            ordenar_por (str): Criterio de ordenamiento ('nombre', 'precio', 'cantidad', 'valor')
                               Por defecto ordena por nombre
                               
        Example:
            >>> inventario.listar_productos(ordenar_por="precio")
            # Lista productos ordenados por precio de menor a mayor
        """
        if not self._productos:
            print("\n" + "="*50)
            print("El inventario está vacío.")
            print("="*50)
            return
        
        # Crear una copia ordenada de los productos
        productos_ordenados = self._productos.copy()
        
        if ordenar_por == "nombre":
            productos_ordenados.sort(key=lambda p: p.nombre.lower())
        elif ordenar_por == "precio":
            productos_ordenados.sort(key=lambda p: p.precio)
        elif ordenar_por == "cantidad":
            productos_ordenados.sort(key=lambda p: p.cantidad)
        elif ordenar_por == "valor":
            productos_ordenados.sort(key=lambda p: p.calcular_valor_total())
        
        print("\n" + "="*50)
        print(f"LISTADO DE PRODUCTOS EN INVENTARIO (Ordenado por: {ordenar_por})")
        print("="*50)
        for i, producto in enumerate(productos_ordenados, 1):
            print(f"{i}. {producto}")
        print("="*50)
        print(f"Total de productos: {len(self._productos)}")
        print(f"Valor total del inventario: ${self.calcular_valor_inventario():.2f}")
        print("="*50)
    
    def eliminar_producto(self, nombre: str) -> bool:
        """
        Elimina un producto del inventario por su nombre con confirmación.
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó exitosamente, False si no se encontró
            
        Raises:
            ValueError: Si el nombre está vacío o no es una cadena válida
            ProductoNoEncontrado: Si el producto no existe en el inventario
            
        Example:
            >>> inventario.eliminar_producto("Laptop Dell")
            Producto 'Laptop Dell' eliminado exitosamente del inventario.
            True
        """
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto válida")
        
        nombre = nombre.strip().lower()
        for i, producto in enumerate(self._productos):
            if producto.nombre.lower() == nombre:
                # Confirmar eliminación
                print(f"¿Está seguro de que desea eliminar '{producto.nombre}'?")
                confirmacion = input("Esta acción no se puede deshacer. Escriba 'ELIMINAR' para confirmar: ")
                
                if confirmacion == "ELIMINAR":
                    producto_eliminado = self._productos.pop(i)
                    print(f"Producto '{producto_eliminado.nombre}' eliminado exitosamente del inventario.")
                    return True
                else:
                    print("Eliminación cancelada por el usuario.")
                    return False
        
        print(f"No se encontró ningún producto con el nombre '{nombre}' para eliminar.")
        return False
    
    def configurar_actualizacion_automatica(self, activar: bool) -> None:
        """
        Configura el modo de actualización automática para productos duplicados.
        
        Args:
            activar (bool): True para activar actualización automática, False para desactivar
            
        Example:
            >>> inventario.configurar_actualizacion_automatica(True)
            Actualización automática ACTIVADA. Los productos duplicados se actualizarán automáticamente.
        """
        self._actualizacion_automatica = activar
        estado = "ACTIVADA" if activar else "DESACTIVADA"
        print(f"Actualización automática {estado}. Los productos duplicados se actualizarán automáticamente.")
        
def obtener_numero(mensaje: str, tipo=float, minimo: float = 0) -> float:
    """
    Función auxiliar para obtener y validar entrada numérica del usuario.
    
    Esta función implementa un bucle de validación robusto que maneja
    entradas vacías, tipos incorrectos y valores fuera de rango.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        tipo (type): Tipo de dato esperado (int o float)
        minimo (float): Valor mínimo permitido
        
    Returns:
        float: Número validado del tipo especificado
        
    Raises:
        KeyboardInterrupt: Si el usuario cancela la operación
        
    Example:
        >>> precio = obtener_numero("Ingrese precio: $", float, 0)
        >>> cantidad = obtener_numero("Ingrese cantidad: ", int, 0)
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
        except ValueError:
            tipo_nombre = "número entero" if tipo == int else "número decimal"
            print(f"Error: Debe ingresar un {tipo_nombre} válido. Valor ingresado: '{entrada}'")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            raise
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor inténtelo de nuevo.")


def menu_principal():
    """
    Función principal que muestra el menú interactivo y gestiona todas las operaciones.
    
    Esta función implementa un bucle principal que presenta opciones al usuario
    y ejecuta las operaciones correspondientes del inventario.
    
    Features:
        - Menú interactivo con 10 opciones
        - Manejo robusto de errores y excepciones
        - Resumen rápido del inventario tras operaciones
        - Opción de exportar inventario
        - Salida elegante con Ctrl+C
    """
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
        print("9. Exportar inventario a archivo")
        print("10. Salir")
        print("="*60)
        
        try:
            opcion = input("Seleccione una opción (1-10): ").strip()
            
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
                    inventario.mostrar_resumen()  # Mostrar resumen tras operación
                    
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
                
                try:
                    producto = inventario.buscar_producto(nombre)
                    if producto:
                        print("Producto encontrado:")
                        print(producto)
                    else:
                        print(f"No se encontró ningún producto con el nombre '{nombre}'.")
                except ValueError as e:
                    print(f"Error en la búsqueda: {e}")
                if producto:
                    print("Producto encontrado:")
                    print(producto)
                else:
                    print(f"No se encontró ningún producto con el nombre '{nombre}'")
                
            elif opcion == "3":
                # Listar productos
                inventario.listar_productos()
                inventario.mostrar_resumen()  # Mostrar resumen tras listar
                
            elif opcion == "4":
                # Calcular valor total
                valor_total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${valor_total:.2f}")
                inventario.mostrar_resumen()  # Mostrar resumen tras calcular
                
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
                        inventario.mostrar_resumen()  # Mostrar resumen tras actualizar
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
                        inventario.mostrar_resumen()  # Mostrar resumen tras actualizar
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
                            inventario.mostrar_resumen()  # Mostrar resumen tras eliminar
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
                # Exportar inventario
                print("\n--- EXPORTAR INVENTARIO ---")
                if not inventario._productos:
                    print("El inventario está vacío. No hay nada que exportar.")
                    continue
                
                nombre_archivo = input("Ingrese el nombre del archivo (o presione Enter para usar el predeterminado): ").strip()
                if not nombre_archivo:
                    nombre_archivo = "inventario_exportado.txt"
                
                try:
                    inventario.exportar_inventario(nombre_archivo)
                    print("✅ Exportación completada exitosamente.")
                except Exception as e:
                    print(f"❌ Error al exportar: {e}")
                
            elif opcion == "10":
                # Salir
                print("\n¡Gracias por usar el Sistema de Inventario!")
                print("¡Hasta pronto!")
                break
                
            else:
                print("Error: Opción no válida. Por favor seleccione una opción del 1 al 10.")
                
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
