
from excepciones.errores import (EscuelaError, DniInvalidoError, NotaInvalidaError,
                                 PersonaDuplicadaError, PersonaNoEncontradaError,
                                 LegajoInvalidoError)
from modelos.alumno import Alumno
from modelos.persona import Persona
from modelos.profesor import Profesor
from servicios.escuela import Escuela
from utilidades.archivos import RUTA_ESCUELA, RUTA_HISTORICOS, RUTA_REPORTE

VALOR_HORA_CATEDRA = 15000  

MENU = """
================ SISTEMA DE GESTIÓN ESCOLAR ================
 1) Inscribir alumno          6) Buscar por nombre
 2) Inscribir profesor        7) Ranking y aprobados
 3) Cargar nota               8) Estadísticas del curso
 4) Dar de baja               9) Predecir riesgo de un alumno
 5) Listar todos             10) Generar reporte
 0) Guardar y salir
============================================================"""


def pedir_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  [ERROR] El dato no puede quedar vacío.")


def pedir_entero(mensaje, minimo=None):
    """Pide un número entero; repite si se escribe texto (ValueError)."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  [ERROR] Tenés que ingresar un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  [ERROR] El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor



def inscribir_alumno(escuela):
    print("\n-- Inscribir alumno --")
    nombre = pedir_texto("Nombre y apellido: ")
    dni = pedir_texto("DNI (7 u 8 dígitos): ")
    legajo = pedir_texto("Legajo (ej: A-0001): ").upper()
    try:
        asistencia = float(input("Asistencia % (0 a 100): "))
        alumno = Alumno(nombre, dni, legajo, asistencia)
        escuela.inscribir(alumno)
    except ValueError as error:
        print(f"  [ERROR] Dato numérico inválido: {error}")
    except DniInvalidoError as error:
        print(f"  [ERROR] {error}")
    except LegajoInvalidoError as error:
        print(f"  [ERROR] {error}")
    except PersonaDuplicadaError as error:
        print(f"  [ERROR] {error}")
    else:
        print(f"  [OK] Alumno inscripto: {alumno}")


def inscribir_profesor(escuela):
    print("\n-- Inscribir profesor --")
    nombre = pedir_texto("Nombre y apellido: ")
    dni = pedir_texto("DNI (7 u 8 dígitos): ")
    materia = pedir_texto("Materia: ")
    horas = pedir_entero("Horas cátedra: ", minimo=1)
    try:
        profesor = Profesor(nombre, dni, materia, horas)
        escuela.inscribir(profesor)
    except DniInvalidoError as error:
        print(f"  [ERROR] {error}")
    except PersonaDuplicadaError as error:
        print(f"  [ERROR] {error}")
    else:
        print(f"  [OK] Profesor inscripto: {profesor}")


def cargar_nota(escuela):
    print("\n-- Cargar nota --")
    dni = pedir_texto("DNI del alumno: ")
    
    try:
        alumno = escuela.buscar_alumno(dni)
        nota = float(input(f"Nota para {alumno.nombre} (0 a 10): "))
        alumno.cargar_nota(nota)
    except PersonaNoEncontradaError as error:
        print(f"  [ERROR] {error}")
    except ValueError:
        print("  [ERROR] La nota tiene que ser un número (ej: 7 o 7.5).")
    except NotaInvalidaError as error:
        print(f"  [ERROR] {error}")
    else:
        print(f"  [OK] Nota cargada. Nuevo promedio de {alumno.nombre}: {alumno.promedio():.2f}")
    finally:
        print("  (fin de la operación de carga de nota)")


def dar_de_baja(escuela):
    print("\n-- Dar de baja --")
    dni = pedir_texto("DNI de la persona: ")
    try:
        nombre = escuela.dar_de_baja(dni)
    except PersonaNoEncontradaError as error:
        print(f"  [ERROR] {error}")
    else:
        print(f"  [OK] {nombre} fue dado/a de baja.")


def listar_todos(escuela):
    print(f"\n-- Listado de personas ({len(escuela)} inscriptas) --")
    escuela.mostrar_todos()
    print(f"  Personas creadas desde que inició el programa: {Persona.total_creadas()}")


def buscar_por_nombre(escuela):
    print("\n-- Buscar por nombre --")
    texto = pedir_texto("Texto a buscar: ")
    encontrados = escuela.buscar_por_nombre(texto)
    if not encontrados:
        print(f"  No se encontró a nadie que contenga '{texto}'.")
    for persona in encontrados:
        print("  " + persona.descripcion())


def ranking_y_aprobados(escuela):
    print("\n-- Ranking de alumnos (mayor a menor promedio) --")
    for posicion, alumno in enumerate(escuela.ranking(), start=1):
        print(f"  {posicion}. {alumno.nombre} ({alumno.legajo}) - {alumno.promedio():.2f}")
    print("\n-- Aprobados (promedio >= 6) --")
    for texto in escuela.textos_aprobados() or ["(ninguno)"]:
        print("  " + texto)
    print("\n-- Promedios por legajo --")
    for legajo, promedio in escuela.promedios_por_legajo().items():
        print(f"  {legajo}: {promedio}")


def estadisticas(escuela):
    print("\n-- Estadísticas del curso (NumPy) --")
    datos = escuela.estadisticas()
    if datos is None:
        print("  No hay alumnos inscriptos.")
        return
    print(f"  Promedio general: {datos['promedio_general']:.2f}")
    print(f"  Promedio máximo:  {datos['maximo']:.2f}")
    print(f"  Promedio mínimo:  {datos['minimo']:.2f}")
    print(f"  Desvío estándar:  {datos['desvio_estandar']:.2f}")
    condicion = escuela.conteo_condicion()
    print(f"  Condición (Counter): {dict(condicion)}")
    if escuela.predictor_entrenado():
        print(f"  Riesgo (Counter, k=3): {dict(escuela.conteo_riesgo())}")


def predecir_riesgo(escuela):
    print("\n-- Predecir riesgo académico (K-NN) --")
    if not escuela.predictor_entrenado():
        print("  El predictor no tiene casos históricos cargados.")
        return
    dni = input("DNI del alumno (Enter = todos los alumnos): ").strip()
    try:
        alumnos = [escuela.buscar_alumno(dni)] if dni else escuela.alumnos()
    except PersonaNoEncontradaError as error:
        print(f"  [ERROR] {error}")
        return
    for alumno in alumnos:
        k1 = escuela.predecir_riesgo(alumno, k=1)
        k3 = escuela.predecir_riesgo(alumno, k=3)
        aviso = "  <- cambia según k" if k1 != k3 else ""
        print(f"  {alumno.nombre}: promedio {alumno.promedio():.2f}, asistencia {alumno.asistencia_pct:g}%"
              f" -> k=1: {k1.upper()} | k=3: {k3.upper()}{aviso}")


def generar_reporte(escuela):
    print("\n-- Reporte --")
    for linea in escuela.generar_reporte(k=3, valor_hora=VALOR_HORA_CATEDRA):
        print("  " + linea)
    escuela.guardar_reporte(RUTA_REPORTE, k=3, valor_hora=VALOR_HORA_CATEDRA)
    print(f"  [OK] Reporte guardado en {RUTA_REPORTE}")


OPCIONES = {
    1: inscribir_alumno, 2: inscribir_profesor, 3: cargar_nota, 4: dar_de_baja,
    5: listar_todos, 6: buscar_por_nombre, 7: ranking_y_aprobados, 8: estadisticas,
    9: predecir_riesgo, 10: generar_reporte,
}


def main():
    escuela = Escuela("Escuela Técnica N° 1")
    print("Cargando datos...")
    escuela.cargar_desde_archivo(RUTA_ESCUELA)
    casos = escuela.entrenar_predictor(RUTA_HISTORICOS)
    print(f"  [IA] Predictor entrenado con {casos} casos históricos.")

    opcion = None
    while opcion != 0:
        print(MENU)
        try:
            opcion = int(input("Elegí una opción: "))
        except ValueError:
            print("  [ERROR] La opción tiene que ser un número del 0 al 10.")
            continue
        except EOFError:
            opcion = 0  

        if opcion in OPCIONES:
            try:
                OPCIONES[opcion](escuela)
            except EOFError:
                print("\n  [AVISO] Se cerró la entrada: se guarda y se sale.")
                opcion = 0
            except EscuelaError as error:
                
                print(f"  [ERROR] {error}")
        elif opcion != 0:
            print("  [ERROR] Opción inexistente. Elegí un número del 0 al 10.")

        if opcion == 0:
            cantidad = escuela.guardar_en_archivo(RUTA_ESCUELA)
            print(f"  [OK] Se guardaron {cantidad} personas en {RUTA_ESCUELA}. ¡Hasta luego!")

if __name__ == "__main__":
    main()
