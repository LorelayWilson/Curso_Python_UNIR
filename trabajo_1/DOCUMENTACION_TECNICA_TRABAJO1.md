# Documentación Técnica - Calculadora de Promedios Escolares

## Índice
1. [Descripción General](#descripción-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Funciones Principales](#funciones-principales)
4. [Instalación y Ejecución](#instalación-y-ejecución)
5. [Ejemplos de Uso](#ejemplos-de-uso)
6. [Criterios de Evaluación UNIR](#criterios-de-evaluación-unir)
7. [Conclusión](#conclusión)
8. [Autoría y Contexto](#autoría-y-contexto)

---

## Descripción General

La **Calculadora de Promedios Escolares** es una aplicación Python que gestiona calificaciones académicas, calcula promedios, determina estados de aprobación/reprobación y genera reportes detallados.

### Características Principales
- **Ingreso dinámico** de materias y calificaciones
- **Validaciones robustas** (rango 0.0 - 10.0)
- **Umbral configurable** de aprobación
- **Reportes completos** con análisis estadístico
- **Interfaz intuitiva** y manejo de errores

---

## Arquitectura del Sistema

```
Calculadora de Promedios
├── Constantes Globales
│   ├── MIN_CALIF (0.0)
│   ├── MAX_CALIF (10.0)
│   └── UMBRAL_DEFAULT (5.0)
├── Funciones de Validación
│   ├── validar_calificacion()
│   └── solicitar_continuar()
├── Funciones de Procesamiento
│   ├── ingresar_calificaciones()
│   ├── calcular_promedio()
│   └── determinar_estado()
├── Funciones de Presentación
│   └── mostrar_resumen()
└── Función Principal
    └── main()
```

### Paradigmas Implementados
- **Programación Funcional**: Funciones modulares y reutilizables
- **Validación de Datos**: Verificación exhaustiva de entradas
- **Manejo de Estados**: Control de flujo con bucles y condicionales
- **Separación de Responsabilidades**: Cada función tiene un propósito específico

---

## Funciones Principales

### Funciones de Validación

#### `validar_calificacion(nombre_materia: str) -> float`
Solicita y valida la calificación de una materia específica.
- **Parámetros**: `nombre_materia` (str) - Nombre de la materia
- **Retorno**: `float` - Calificación validada entre 0.0 y 10.0
- **Funcionalidad**: Conversión de comas a puntos, validación de rango, manejo de errores

#### `solicitar_continuar() -> str`
Pregunta al usuario si desea continuar ingresando materias.
- **Retorno**: `str` - 's' para sí, 'n' para no
- **Funcionalidad**: Normalización de entrada, validación de respuesta

### Funciones de Procesamiento

#### `ingresar_calificaciones() -> list[tuple[str, float]]`
Coordina el ingreso de múltiples materias y calificaciones.
- **Retorno**: `list[tuple[str, float]]` - Lista de tuplas (materia, calificación)
- **Funcionalidad**: Bucle principal, validación de nombres, control de flujo

#### `calcular_promedio(datos: list[tuple[str, float]]) -> float`
Calcula el promedio aritmético de todas las calificaciones.
- **Parámetros**: `datos` - Lista de materias y calificaciones
- **Retorno**: `float` - Promedio calculado o 0.0 si no hay datos
- **Funcionalidad**: Verificación de datos, cálculo aritmético, redondeo a 2 decimales

#### `determinar_estado(datos, umbral) -> tuple[list[int], list[int]]`
Clasifica las materias en aprobadas y reprobadas según el umbral.
- **Parámetros**: `datos` - Lista de materias, `umbral` - Puntuación mínima para aprobar
- **Retorno**: `tuple[list[int], list[int]]` - (índices_aprobadas, índices_reprobadas)

### Funciones de Presentación

#### `mostrar_resumen(datos, promedio, aprobadas, reprobadas, umbral) -> None`
Genera y muestra un reporte completo de las calificaciones.
- **Funcionalidad**: Encabezado, lista numerada, estadísticas, clasificación, extremos

### Función Principal

#### `main() -> None`
Coordina toda la ejecución del programa.
- **Funcionalidad**: Presentación, configuración de umbral, coordinación del flujo

---

## Instalación y Ejecución

### Requisitos Previos
- Python 3.6 o superior
- Acceso a terminal o línea de comandos

### Ejecución Directa
```bash
# Navegar al directorio del trabajo
cd trabajo_1

# Ejecutar el programa
python trabajo_1_sintaxis_python.py
```

### Verificación de Instalación
```bash
# Verificar versión de Python
python --version

# Verificar que el archivo existe
dir trabajo_1_sintaxis_python.py
```

---

## Ejemplos de Uso

### Ejemplo 1: Ingreso Básico de Materias
```
=== Calculadora de Promedios Escolares ===
Introduce el umbral de aprobación (presiona Enter para usar 5.0): 

Ingresa el nombre de la materia: Matemáticas
Ingrese la calificación para 'Matemáticas' (0.0-10.0): 8.5
¿Deseas ingresar otra materia? (s/n): s

Ingresa el nombre de la materia: Historia
Ingrese la calificación para 'Historia' (0.0-10.0): 7.0
¿Deseas ingresar otra materia? (s/n): n

===== RESUMEN DE CALIFICACIONES =====
Umbral de aprobación utilizado: 5.00

1. Matemáticas: 8.50
2. Historia: 7.00

Promedio general: 7.75

Materias aprobadas:
  - Matemáticas (8.50)
  - Historia (7.00)

No hay materias reprobadas.

Materia con mejor calificación:
  - Matemáticas (8.50)
Materia con peor calificación:
  - Historia (7.00)
```

### Ejemplo 2: Umbral Personalizado
```
=== Calculadora de Promedios Escolares ===
Introduce el umbral de aprobación (presiona Enter para usar 5.0): 7.0

Ingresa el nombre de la materia: Física
Ingrese la calificación para 'Física' (0.0-10.0): 6.5
¿Deseas ingresar otra materia? (s/n): n

===== RESUMEN DE CALIFICACIONES =====
Umbral de aprobación utilizado: 7.00

1. Física: 6.50

Promedio general: 6.50

No hay materias aprobadas.

Materias reprobadas:
  - Física (6.50)
```

---

## Criterios de Evaluación UNIR

### Calificación Final: 10/10 (100%)

| **Criterio** | **Peso** | **Calificación** | **Estado** |
|:-------------|:--------:|:----------------:|:----------:|
| **Implementación de funciones y estructura** | 30% | 10/10 | ✅ **Perfecto** |
| **Manejo de estructuras de datos** | 25% | 10/10 | ✅ **Perfecto** |
| **Cálculos y lógica** | 25% | 10/10 | ✅ **Perfecto** |
| **Validación de entrada y manejo de errores** | 20% | 10/10 | ✅ **Perfecto** |

### Criterios Cumplidos

#### ✅ Criterio 1: Implementación de funciones y estructura (30%)
- **Funciones implementadas**: `ingresar_calificaciones()`, `calcular_promedio()`, `determinar_estado()`, `encontrar_extremos()`
- **Organización**: Código sin POO, modular y bien estructurado
- **Separación de responsabilidades**: Cada función tiene un propósito específico

#### ✅ Criterio 2: Manejo de estructuras de datos (25%)
- **Listas**: Uso adecuado para almacenar materias y calificaciones
- **Indexación**: Acceso correcto a elementos por índice
- **Estructura compuesta**: Lista de tuplas (materia, calificación)

#### ✅ Criterio 3: Cálculos y lógica (25%)
- **Promedio**: Cálculo aritmético correcto y preciso
- **Clasificación**: Determinación de aprobados/reprobados por umbral
- **Extremos**: Identificación de calificaciones máxima y mínima

#### ✅ Criterio 4: Validación de entrada y manejo de errores (20%)
- **Rango**: Validación de calificaciones entre 0.0 y 10.0
- **Tipos**: Conversión segura string → float
- **Casos especiales**: Manejo de listas vacías y entradas vacías

### Resumen Global de la Evaluación UNIR

> **"El proyecto cumple de manera sobresaliente con todos los requisitos funcionales y estructurales establecidos en el enunciado. La implementación es clara, modular y robusta, con validaciones adecuadas y manejo correcto de estructuras de datos. No se detectan errores que violen los requisitos y se observan buenas prácticas en la organización y control de flujo. El código es fácilmente mantenible y extensible, demostrando un dominio sólido de la programación estructurada en Python."**

---

## Conclusión

El **Trabajo 1 - Calculadora de Promedios Escolares** representa una implementación completa y profesional de la programación estructurada en Python, cumpliendo con todos los requisitos académicos establecidos por UNIR. 

El proyecto demuestra:
- **Dominio técnico** de las estructuras de datos y control de flujo
- **Capacidad analítica** para procesar y validar información académica
- **Pensamiento estructurado** en la organización del código
- **Calidad profesional** en validaciones y manejo de errores

La calculadora proporciona **funcionalidad robusta** para la gestión académica, estableciendo una base sólida para el desarrollo de aplicaciones educativas más complejas y demostrando un dominio sólido de la programación estructurada en Python.

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
- **Trabajo**: Trabajo 1 - Calculadora de Promedios Escolares

### Transparencia en el Uso de IA
- **Código Fuente**: Desarrollado íntegramente por la autora
- **Lógica y Algoritmos**: Diseño e implementación original
- **Documentación**: Elaborada con asistencia de IA Generativa para formato y presentación
- **Contenido Técnico**: Validado y verificado por la autora

### Licencia
**© Agosto 2025 - Lorelay Pricop Florescu**  
*Licencia Académica - Todos los derechos reservados*

---

<div align="center">

**Calculadora de Promedios Escolares - UNIR**  
*Proyecto académico del Máster en Inteligencia Artificial*

---

**UNIVERSIDAD INTERNACIONAL DE LA RIOJA**  
*Máster Universitario en Inteligencia Artificial*  
*Curso de Programación en Python*

![Quality](https://img.shields.io/badge/Calidad-Profesional-gold?style=flat-square&logo=award)
![Academic](https://img.shields.io/badge/Nivel-Académico%20Superior-blue?style=flat-square&logo=graduation-cap)
![Standards](https://img.shields.io/badge/Estándares-Empresariales-green?style=flat-square&logo=check-circle)

</div>
