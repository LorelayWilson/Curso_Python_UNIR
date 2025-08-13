MIN_CALIF = 0.0
MAX_CALIF = 10.0
UMBRAL_DEFAULT = 5.0


def validar_calificacion(nombre_materia: str) -> float:
    """Solicita y valida la calificación de una materia."""
    while True:
        calif = input(
            f"Ingrese la calificación para '{nombre_materia}' ({MIN_CALIF}-{MAX_CALIF}): "
        ).strip()
        
        if not calif:  # Entrada vacía
            print("Error: La calificación no puede estar vacía. Por favor, ingrese un valor.")
            continue
            
        calif = calif.replace(',', '.')
        try:
            calif = float(calif)
            if MIN_CALIF <= calif <= MAX_CALIF:
                return calif
            print(f"La calificación debe estar entre {MIN_CALIF} y {MAX_CALIF}.")
        except ValueError:
            print("Introduce un número válido.")


def solicitar_continuar() -> str:
    """Pregunta al usuario si desea continuar ingresando materias."""
    while True:
        respuesta = input(
            "¿Deseas ingresar otra materia? (s/n): "
        ).lower().strip()
        if respuesta in ('s', 'n'):
            return respuesta
        print("Respuesta no válida. Por favor, introduce 's' para sí o 'n' para no.")


def ingresar_calificaciones() -> list[tuple[str, float]]:
    """Solicita al usuario ingresar materias y sus calificaciones."""
    datos = []
    while True:
        nombre = input("Ingresa el nombre de la materia: ").strip()
        if not nombre:
            print("El nombre de la materia no puede estar vacío.")
            continue
        calif = validar_calificacion(nombre)
        datos.append((nombre, calif))
        seguir = solicitar_continuar()
        if seguir == 'n':
            break
    return datos


def calcular_promedio(datos: list[tuple[str, float]]) -> float:
    """Calcula el promedio de las calificaciones."""
    if not datos:
        return 0.0
    return round(sum(calif for _, calif in datos) / len(datos), 2)


def determinar_estado(
    datos: list[tuple[str, float]], umbral: float = UMBRAL_DEFAULT
) -> tuple[list[int], list[int]]:
    """Devuelve listas de índices de materias aprobadas y reprobadas."""
    aprobadas = [i for i, (_, calif) in enumerate(datos) if calif >= umbral]
    reprobadas = [i for i, (_, calif) in enumerate(datos) if calif < umbral]
    return aprobadas, reprobadas


def mostrar_encabezado(umbral: float) -> None:
    """Muestra el encabezado del resumen."""
    print("\n===== RESUMEN DE CALIFICACIONES =====")
    print(f"Umbral de aprobación utilizado: {umbral:.2f}\n")


def mostrar_lista_materias(datos: list[tuple[str, float]]) -> None:
    """Muestra la lista numerada de materias y calificaciones."""
    if not datos:
        print("No se ingresaron materias.")
        return
    for i, (mat, calif) in enumerate(datos):
        print(f"{i + 1}. {mat}: {calif:.2f}")


def mostrar_estadisticas(promedio: float) -> None:
    """Muestra las estadísticas principales."""
    print(f"\nPromedio general: {promedio:.2f}")


def mostrar_clasificacion(datos: list[tuple[str, float]], aprobadas: list[int], reprobadas: list[int]) -> None:
    """Muestra la clasificación de materias por estado."""
    if aprobadas:
        print("\nMaterias aprobadas:")
        for i in aprobadas:
            print(f"  - {datos[i][0]} ({datos[i][1]:.2f})")
    else:
        print("\nNo hay materias aprobadas.")
    
    if reprobadas:
        print("\nMaterias reprobadas:")
        for i in reprobadas:
            print(f"  - {datos[i][0]} ({datos[i][1]:.2f})")
    else:
        print("\nNo hay materias reprobadas.")


def mostrar_extremos(datos: list[tuple[str, float]]) -> None:
    """Muestra las materias con mejor y peor calificación."""
    if not datos:
        print("\nNo hay datos de materias para mostrar extremos.")
        return
    
    idx_max = max(range(len(datos)), key=lambda i: datos[i][1])
    idx_min = min(range(len(datos)), key=lambda i: datos[i][1])
    
    print("\nMateria con mejor calificación:")
    print(f"  - {datos[idx_max][0]} ({datos[idx_max][1]:.2f})")
    print("Materia con peor calificación:")
    print(f"  - {datos[idx_min][0]} ({datos[idx_min][1]:.2f})")


def mostrar_resumen(
    datos: list[tuple[str, float]],
    promedio: float,
    aprobadas: list[int],
    reprobadas: list[int],
    umbral: float
) -> None:
    """Muestra un resumen de las calificaciones ingresadas."""
    mostrar_encabezado(umbral)
    mostrar_lista_materias(datos)
    mostrar_estadisticas(promedio)
    mostrar_clasificacion(datos, aprobadas, reprobadas)
    mostrar_extremos(datos)


def main() -> None:
    print("=== Calculadora de Promedios Escolares ===")
    # Permitir al usuario definir el umbral
    while True:
        umbral_input = input(
            f"Introduce el umbral de aprobación (presiona Enter para usar {UMBRAL_DEFAULT}): "
        ).strip()
        
        if umbral_input == '':
            umbral = UMBRAL_DEFAULT
            break
            
        umbral_input = umbral_input.replace(',', '.')
        try:
            umbral = float(umbral_input)
            if MIN_CALIF <= umbral <= MAX_CALIF:
                break
            print(f"El umbral debe estar entre {MIN_CALIF} y {MAX_CALIF}.")
        except ValueError:
            print("Introduce un número válido para el umbral.")
    
    datos = ingresar_calificaciones()
    if not datos:
        print("No se ingresaron datos. ¡Hasta la próxima!")
        return
    promedio = calcular_promedio(datos)
    aprobadas, reprobadas = determinar_estado(datos, umbral)
    mostrar_resumen(datos, promedio, aprobadas, reprobadas, umbral)
    print("\n¡Gracias por usar la calculadora de promedios!")


if __name__ == "__main__":
    main()
