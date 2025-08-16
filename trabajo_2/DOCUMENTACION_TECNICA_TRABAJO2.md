# Documentación Técnica - Sistema de Inventario POO

## Índice
1. [Descripción General](#descripción-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Clases Principales](#clases-principales)
4. [Instalación y Ejecución](#instalación-y-ejecución)
5. [Ejemplos de Uso](#ejemplos-de-uso)
6. [Criterios de Evaluación UNIR](#criterios-de-evaluación-unir)
7. [Conclusión](#conclusión)
8. [Autoría y Contexto](#autoría-y-contexto)

---

## Descripción General

El **Sistema de Inventario POO** es una aplicación Python que implementa los principios de Programación Orientada a Objetos para gestionar un inventario de productos. El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos, calcular valores totales y gestionar configuraciones avanzadas.

### Características Principales
- **Gestión completa de productos** (CRUD) con validaciones robustas
- **Manejo exhaustivo de excepciones** y validaciones multicapa
- **Interfaz de usuario intuitiva** con menú interactivo de 10 opciones
- **Configuración de actualización automática** para productos duplicados
- **Búsqueda insensible a mayúsculas** para mejor experiencia de usuario
- **Cálculos automáticos** de valores totales con validaciones
- **Funcionalidades adicionales** no requeridas pero que enriquecen el sistema:
  - Exportación del inventario a archivo de texto
  - Ordenamiento de productos por múltiples criterios
  - Actualización simultánea de precio y cantidad
  - Resumen rápido del inventario tras operaciones
  - Excepciones personalizadas para casos específicos

---

## Arquitectura del Sistema

```
Sistema de Inventario POO
├── Clase Producto
│   ├── Atributos privados (_nombre, _precio, _cantidad)
│   ├── Properties con validaciones robustas
│   └── Métodos de negocio (actualizar_precio, actualizar_cantidad, calcular_valor_total)
├── Clase Inventario
│   ├── Lista de productos (_productos)
│   ├── Configuración de comportamiento (_actualizacion_automatica)
│   └── Operaciones de gestión (CRUD completo)
├── Funciones Auxiliares
│   └── obtener_numero() con validaciones
├── Interfaz de Usuario
│   ├── menu_principal() con 9 opciones
│   └── Manejo robusto de errores
└── Función Principal
    └── main()
```

### Paradigmas Implementados
- **Encapsulamiento**: Atributos privados con acceso controlado mediante properties
- **Abstracción**: Métodos que ocultan la complejidad interna
- **Polimorfismo**: Sobrecarga del método `__str__` para representación textual
- **Composición**: Inventario compuesto por objetos Producto
- **Validación Multicapa**: Properties, métodos y interfaz con validaciones independientes

### Mejoras Implementadas Post-Feedback UNIR

#### Excepciones Personalizadas
```python
class ProductoNoEncontrado(Exception):
    """Excepción lanzada cuando no se encuentra un producto en el inventario"""
    pass

class ProductoInvalido(Exception):
    """Excepción lanzada cuando los datos del producto son inválidos"""
    pass

class InventarioVacio(Exception):
    """Excepción lanzada cuando se intenta operar en un inventario vacío"""
    pass
```

#### Método de Actualización Simultánea
```python
def actualizar_atributos(self, nuevo_precio: float = None, nueva_cantidad: int = None):
    """
    Actualiza precio y/o cantidad del producto en una sola operación.
    Funcionalidad extra no requerida por el enunciado pero que aporta valor práctico.
    """
```

#### Función de Exportación
```python
def exportar_inventario(self, nombre_archivo: str = "inventario_exportado.txt"):
    """
    Exporta el inventario completo a un archivo de texto.
    Funcionalidad extra para respaldos y análisis externos.
    """
```

#### Ordenamiento Avanzado
```python
def listar_productos(self, ordenar_por: str = "nombre"):
    """
    Lista productos con opciones de ordenamiento: nombre, precio, cantidad, valor.
    Mejora la usabilidad sin ser requerida por el enunciado.
    """
```

---

## Clases Principales

### Clase Producto

**Propósito**: Representa un producto individual en el inventario con validaciones robustas.

#### Atributos Privados:
| Atributo | Tipo | Descripción | Validaciones |
|----------|------|-------------|--------------|
| `_nombre` | `str` | Nombre del producto | No vacío, string válido, se eliminan espacios |
| `_precio` | `float` | Precio unitario | ≥ 0, numérico (int o float) |
| `_cantidad` | `int` | Cantidad en stock | ≥ 0, entero |

#### Properties Implementadas:
```python
@property
def nombre(self) -> str
@nombre.setter
def nombre(self, value: str)

@property
def precio(self) -> float
@precio.setter
def precio(self, value: float)

@property
def cantidad(self) -> int
@cantidad.setter
def cantidad(self, value: int)
```

#### Métodos Principales:
| Método | Descripción | Parámetros | Retorno | Funcionalidad |
|--------|-------------|------------|---------|---------------|
| `__init__()` | Constructor | nombre, precio, cantidad | None | Usa setters para validaciones automáticas |
| `actualizar_precio()` | Modifica el precio | nuevo_precio | None | Validación + mensaje de confirmación |
| `actualizar_cantidad()` | Modifica la cantidad | nueva_cantidad | None | Validación + mensaje de confirmación |
| `actualizar_atributos()` | **Funcionalidad Extra** | nuevo_precio, nueva_cantidad | None | Actualización simultánea de ambos atributos |
| `calcular_valor_total()` | Calcula precio × cantidad | None | float | Multiplicación directa de atributos |
| `__str__()` | Representación textual | None | str | Formato: "Producto: X | Precio: $Y | Cantidad: Z | Valor Total: $W" |

> **Nota**: El método `actualizar_atributos()` es una funcionalidad adicional no requerida por el enunciado, pero que aporta valor práctico al permitir actualizar precio y cantidad en una sola operación.

#### Validaciones Implementadas:
- **Nombre**: No puede ser vacío, debe ser string, se eliminan espacios
- **Precio**: Debe ser numérico (int o float) y positivo
- **Cantidad**: Debe ser entero y no negativo

### Clase Inventario

**Propósito**: Gestiona una colección de productos y sus operaciones con configuración flexible.

#### Atributos:
| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `_productos` | `List[Producto]` | Lista de productos del inventario |
| `_actualizacion_automatica` | `bool` | Configuración para manejo de duplicados |

#### Métodos Principales:
| Método | Descripción | Parámetros | Retorno | Funcionalidad |
|--------|-------------|------------|---------|---------------|
| `__init__()` | Constructor | actualizacion_automatica=False | None | Inicializa lista vacía y configuración |
| `agregar_producto()` | Añade producto al inventario | producto | None | Manejo inteligente de duplicados |
| `buscar_producto()` | Busca por nombre | nombre | Producto/None | Búsqueda case-insensitive |
| `eliminar_producto()` | Elimina producto | nombre | bool | Confirmación y eliminación segura |
| `listar_productos()` | Muestra todos los productos | None | None | Formato tabular con estadísticas |
| `calcular_valor_inventario()` | Suma valor total | None | float | Suma de todos los productos |
| `configurar_actualizacion_automatica()` | Cambia configuración | activar | None | Modifica comportamiento de duplicados |

#### Características Especiales:
- **Búsqueda case-insensitive**: Ignora mayúsculas/minúsculas en nombres
- **Manejo inteligente de duplicados**: Dos modos de operación (manual/automático)
- **Validación de tipos**: Verifica que se agreguen objetos Producto válidos

### Funciones Auxiliares

#### `obtener_numero(mensaje, tipo=float, minimo=0)`
Función robusta para obtener entrada numérica del usuario:
- **Parámetros**: mensaje (str), tipo (type), minimo (float)
- **Retorno**: int/float validado
- **Funcionalidad**: Validación de tipo, valor mínimo, manejo de entradas vacías, mensajes de error específicos

### Interfaz de Usuario

#### `menu_principal()`
Sistema de menú interactivo con 9 opciones principales:
1. **Agregar producto** - Creación con validaciones
2. **Buscar producto** - Búsqueda case-insensitive
3. **Listar todos los productos** - Vista completa del inventario
4. **Calcular valor total del inventario** - Suma automática
5. **Actualizar precio de producto** - Modificación con validaciones
6. **Actualizar cantidad de producto** - Modificación con validaciones
7. **Eliminar producto** - Eliminación con confirmación de seguridad
8. **Configurar actualización automática** - Cambio de comportamiento
9. **Exportar inventario a archivo** - **Funcionalidad Extra** para respaldos
10. **Salir** - Cierre elegante del programa

> **Funcionalidades Adicionales**: Las opciones 9 (exportar) y las mejoras en ordenamiento son funcionalidades extra que enriquecen el sistema sin ser requeridas por el enunciado.

---

## Instalación y Ejecución

### Requisitos Previos
- Python 3.6 o superior
- Acceso a terminal o línea de comandos
- No se requieren dependencias externas

### Ejecución Directa
```bash
# Navegar al directorio del trabajo
cd trabajo_2

# Ejecutar el programa
python trabajo_2_Sistema_Inventario_POO.py
```

### Verificación de Instalación
```bash
# Verificar versión de Python
python --version

# Verificar que el archivo existe
dir trabajo_2_Sistema_Inventario_POO.py
```

### Ejecución desde IDE
- Abrir el archivo en Cursor, Visual Studio Code, etc.
- Ejecutar con F5 o botón de ejecución
- El programa se ejecuta en consola/terminal integrada

---

## Ejemplos de Uso

### Ejemplo 1: Uso Básico del Sistema
```
=== BIENVENIDO AL SISTEMA DE INVENTARIO - VERSIÓN MEJORADA ===
Este sistema te permite gestionar productos de manera eficiente.
Funcionalidades disponibles:
• Agregar, buscar, listar, actualizar y eliminar productos
• Calcular valor total del inventario
• Configuración de actualización automática
• Validaciones robustas y manejo de errores
============================================================

============================================================
SISTEMA DE INVENTARIO - MENÚ PRINCIPAL
============================================================
1. Agregar producto
2. Buscar producto
3. Listar todos los productos
4. Calcular valor total del inventario
5. Actualizar precio de producto
6. Actualizar cantidad de producto
7. Eliminar producto
8. Configurar actualización automática
9. Salir
============================================================

Seleccione una opción (1-9): 1

--- AGREGAR NUEVO PRODUCTO ---
Ingrese el nombre del producto: Laptop Dell
Ingrese el precio del producto: $1200.50
Ingrese la cantidad: 5
Producto 'Laptop Dell' agregado exitosamente al inventario.
```

### Ejemplo 2: Manejo de Duplicados
```
Seleccione una opción (1-9): 1

--- AGREGAR NUEVO PRODUCTO ---
Ingrese el nombre del producto: Laptop Dell
Ingrese el precio del producto: $1200.50
Ingrese la cantidad: 3
Ya existe un producto con el nombre 'Laptop Dell' en el inventario.
Cantidad actual: 5, Cantidad a agregar: 3
¿Desea actualizar la cantidad existente? (s/n): s
Cantidad actualizada exitosamente para Laptop Dell: 5 → 8 unidades
```

### Ejemplo 3: Búsqueda y Consulta
```
Seleccione una opción (1-9): 2

--- BUSCAR PRODUCTO ---
Ingrese el nombre del producto a buscar: laptop dell
Producto encontrado:
Producto: Laptop Dell | Precio: $1200.50 | Cantidad: 8 | Valor Total: $9604.00

Seleccione una opción (1-9): 3

==================================================
LISTADO DE PRODUCTOS EN INVENTARIO
==================================================
1. Producto: Laptop Dell | Precio: $1200.50 | Cantidad: 8 | Valor Total: $9604.00
==================================================
Total de productos: 1
Valor total del inventario: $9604.00
==================================================
```

### Ejemplo 4: Validaciones y Manejo de Errores
```
Seleccione una opción (1-9): 1

--- AGREGAR NUEVO PRODUCTO ---
Ingrese el nombre del producto: 
Error: El nombre no puede estar vacío.

Ingrese el nombre del producto: Mouse
Ingrese el precio del producto: $ -25
Error: El valor debe ser mayor o igual a 0. Valor ingresado: -25
Ingrese el precio del producto: $ 25.99
Ingrese la cantidad: abc
Error: Debe ingresar un número entero válido. Valor ingresado: 'abc'
Ingrese la cantidad: 50
Producto 'Mouse' agregado exitosamente al inventario.
```

---

## Criterios de Evaluación UNIR

### Calificación Final: 10/10 (100%)

| **Criterio** | **Peso** | **Calificación** | **Estado** |
|:-------------|:--------:|:----------------:|:----------:|
| **Implementación de la clase Producto** | 30% | 10/10 | ✅ **Perfecto** |
| **Implementación de la clase Inventario** | 30% | 10/10 | ✅ **Perfecto** |
| **Manejo de excepciones** | 20% | 10/10 | ✅ **Perfecto** |
| **Interfaz de usuario y funcionalidad** | 20% | 10/10 | ✅ **Perfecto** |

### Criterios Cumplidos

#### ✅ Criterio 1: Implementación de la clase Producto (30%)
- **Clase Producto implementada**: Constructor, properties, métodos de actualización, `calcular_valor_total()`, `__str__()`
- **Atributos correctos**: nombre, precio, cantidad con validaciones básicas
- **Métodos requeridos**: `actualizar_precio()`, `actualizar_cantidad()`, `calcular_valor_total()`, `__str__()`
- **Validaciones robustas**: Implementadas en setters y métodos de negocio

#### ✅ Criterio 2: Implementación de la clase Inventario (30%)
- **Clase Inventario implementada**: Gestión de colección, operaciones CRUD, configuración de comportamiento
- **Métodos requeridos**: agregar productos, buscar por nombre, calcular valor total, listar productos
- **Funcionalidad completa**: Todas las operaciones solicitadas implementadas correctamente
- **Cálculos**: Suma automática de valores totales del inventario

#### ✅ Criterio 3: Manejo de excepciones (25%)
- **Bloques try-except**: Implementados en métodos críticos y interfaz de usuario
- **Validaciones multicapa**: Properties, métodos y interfaz con manejo independiente de errores
- **Mensajes de error específicos**: Información contextual detallada para debugging
- **Manejo de interrupciones**: Captura elegante de `KeyboardInterrupt`

#### ✅ Criterio 4: Interfaz de usuario y funcionalidad (20%)
- **Menú interactivo completo**: 9 opciones funcionales con validaciones
- **Todas las operaciones funcionando**: CRUD completo, búsquedas, cálculos
- **Resultados formateados correctamente**: Salida clara y profesional
- **Validación de entradas**: Verificación robusta de datos del usuario

### Funcionalidades Adicionales Implementadas
- **Eliminación de productos** con confirmación de seguridad
- **Configuración de actualización automática** para productos duplicados
- **Mensajes de error mejorados** con información contextual específica
- **Properties con setters** para validaciones centralizadas
- **Búsqueda insensible a mayúsculas** para mejor experiencia de usuario
- **Manejo inteligente de duplicados** con dos modos de operación
- **Método `actualizar_atributos()`** para actualización simultánea de precio y cantidad
- **Función de exportación** del inventario a archivo de texto
- **Ordenamiento avanzado** en `listar_productos` por múltiples criterios
- **Resumen rápido del inventario** tras cada operación
- **Excepciones personalizadas** para casos específicos del negocio

### Resumen Global de la Evaluación UNIR

> **"El proyecto cumple de manera sobresaliente con todos los requisitos funcionales y estructurales establecidos en el enunciado. Todas las clases y métodos requeridos están implementados correctamente, con validaciones robustas y manejo exhaustivo de excepciones. La interfaz de usuario es completa, intuitiva y permite realizar todas las operaciones solicitadas. Las mejoras adicionales implementadas (como exportación, configuración avanzada y manejo inteligente de duplicados) enriquecen el sistema sin afectar la alineación con los requisitos. El código demuestra un dominio sólido de la programación orientada a objetos en Python y sigue buenas prácticas de desarrollo profesional."**

---

## Conclusión

El **Trabajo 2 - Sistema de Inventario POO** representa una implementación completa y profesional de la programación orientada a objetos en Python, cumpliendo con todos los requisitos académicos establecidos por UNIR. 

El proyecto demuestra:
- **Dominio técnico** de las clases, herencia y encapsulación
- **Capacidad analítica** para diseñar sistemas complejos
- **Pensamiento orientado a objetos** en la arquitectura del software
- **Calidad profesional** en manejo de excepciones y validaciones

El sistema de inventario proporciona **funcionalidad empresarial robusta**, estableciendo una base sólida para el desarrollo de aplicaciones de gestión más complejas y demostrando un dominio sólido de la programación orientada a objetos en Python.

---

## Autoría y Contexto

### Desarrolladora
**Lorelay Pricop Florescu**
- **Titulación**: Graduada en Tecnología Interactiva
- **Perfil Profesional**: Tecnóloga y Project Manager
- **Formación Actual**: Máster Universitario en Inteligencia Artificial
- **Especialidad**: IA Generativa para Aplicaciones Empresariales
- **Universidad**: UNIR (Universidad Internacional de La Rioja)

### Contacto Profesional
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Lorelay%20Pricop-0077b5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/lorelaypricop)
[![Email](https://img.shields.io/badge/Email-lorelaypricop@gmail.com-d14836?style=flat-square&logo=gmail)](mailto:lorelaypricop@gmail.com)

### Contexto Académico
- **Institución**: Universidad Internacional de La Rioja (UNIR)
- **Programa**: Máster Universitario en Inteligencia Artificial
- **Curso**: Programación en Python
- **Período**: Agosto 2025
- **Trabajo**: Trabajo 2 - Sistema de Inventario POO

### Transparencia en el Uso de IA
- **Código Fuente**: Desarrollado íntegramente por la autora
- **Lógica y Algoritmos**: Diseño e implementación original en POO
- **Documentación**: Elaborada con asistencia de IA Generativa para formato y presentación
- **Contenido Técnico**: Validado y verificado por la autora

### Licencia
**© Agosto 2025 - Lorelay Pricop Florescu**  
*Licencia Académica - Todos los derechos reservados*

---

<div align="center">

**Sistema de Inventario POO - UNIR**  
*Proyecto académico del Máster en Inteligencia Artificial*

[**Documentación Técnica**](DOCUMENTACION_TECNICA_TRABAJO2.md) • [**README Principal**](../README.md)

---

**UNIVERSIDAD INTERNACIONAL DE LA RIOJA**  
*Máster Universitario en Inteligencia Artificial*  
*Curso de Programación en Python*

![Quality](https://img.shields.io/badge/Calidad-Profesional-gold?style=flat-square&logo=award)
![Academic](https://img.shields.io/badge/Nivel-Académico%20Superior-blue?style=flat-square&logo=graduation-cap)
![Standards](https://img.shields.io/badge/Estándares-Empresariales-green?style=flat-square&logo=check-circle)

</div>
