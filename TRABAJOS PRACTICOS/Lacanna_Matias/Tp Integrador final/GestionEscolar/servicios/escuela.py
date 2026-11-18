"""
escuela.py
Clase Escuela: contiene (composición) a todas las personas y al predictor de riesgo.
Concentra la lógica del sistema: inscripciones, búsquedas, estadísticas, reportes y archivos.
"""
import re
from collections import Counter
from datetime import datetime

import numpy as np

from excepciones.errores import (DniInvalidoError, NotaInvalidaError,
                                 PersonaDuplicadaError, PersonaNoEncontradaError,
                                 LegajoInvalidoError)
from ia.predictor_riesgo import PredictorRiesgo
from modelos.alumno import Alumno
from modelos.profesor import Profesor
from utilidades.archivos import asegurar_carpeta, escribir_lineas
from utilidades.decoradores import mide_tiempo, registrar_operacion

NOTA_APROBACION = 6


class Escuela:
    """Escuela con su lista de personas (alumnos y profesores) y su modelo de IA."""

    def __init__(self, nombre="Escuela"):
        self.nombre = nombre
        self.__personas = []                 # composición: la escuela es dueña de la lista
        self.__predictor = PredictorRiesgo()  # composición: la escuela tiene su predictor

    def __len__(self):
        """len(escuela) devuelve la cantidad de personas inscriptas."""
        return len(self.__personas)

    def __str__(self):
        return f"Escuela '{self.nombre}' ({len(self)} personas)"

    # ================== ABM de personas ==================
    def _agregar(self, persona):
        """Agrega una persona controlando que el DNI no esté repetido (usa Persona.__eq__)."""
        if persona in self.__personas:
            raise PersonaDuplicadaError(f"Ya existe una persona inscripta con DNI {persona.dni}")
        self.__personas.append(persona)

    @registrar_operacion
    def inscribir(self, persona):
        """Inscribe una persona nueva. Lanza PersonaDuplicadaError si el DNI ya existe."""
        self._agregar(persona)

    def buscar(self, dni):
        """Devuelve la persona con ese DNI o lanza PersonaNoEncontradaError."""
        dni = str(dni).strip()
        for persona in self.__personas:
            if persona.dni == dni:
                return persona
        raise PersonaNoEncontradaError(f"No hay ninguna persona inscripta con DNI {dni}")

    def buscar_alumno(self, dni):
        """Igual que buscar(), pero exige que la persona sea un Alumno."""
        persona = self.buscar(dni)
        if not isinstance(persona, Alumno):
            raise PersonaNoEncontradaError(f"El DNI {dni} corresponde a un profesor, no a un alumno")
        return persona

    def dar_de_baja(self, dni):
        """Elimina a la persona de la escuela. Al no quedar referencias se ejecuta su __del__."""
        persona = self.buscar(dni)
        nombre = persona.nombre
        self.__personas.remove(persona)
        del persona
        return nombre

    def mostrar_todos(self):
        """Listado polimórfico: llama a descripcion() sin importar si es Alumno o Profesor."""
        if not self.__personas:
            print("  (no hay personas inscriptas)")
        for persona in self.__personas:
            print("  " + persona.descripcion())

    def buscar_por_nombre(self, texto):
        """Busca por nombre con re.search, sin distinguir mayúsculas/minúsculas."""
        patron = re.escape(texto.strip())
        return [p for p in self.__personas if re.search(patron, p.nombre, re.IGNORECASE)]

    # ================== Consultas (programación funcional) ==================
    def alumnos(self):
        """Comprensión de listas: solo los alumnos."""
        return [p for p in self.__personas if isinstance(p, Alumno)]

    def profesores(self):
        return [p for p in self.__personas if isinstance(p, Profesor)]

    def aprobados(self):
        """filter + lambda: alumnos con promedio >= 6."""
        return list(filter(lambda a: a.promedio() >= NOTA_APROBACION, self.alumnos()))

    def desaprobados(self):
        return list(filter(lambda a: a.promedio() < NOTA_APROBACION, self.alumnos()))

    def textos_aprobados(self):
        """map + lambda: textos 'nombre: promedio' de los aprobados."""
        return list(map(lambda a: f"{a.nombre}: {a.promedio():.2f}", self.aprobados()))

    def ranking(self):
        """Alumnos de mayor a menor promedio. sorted() usa Alumno.__lt__.
        Equivale a: sorted(self.alumnos(), key=lambda a: a.promedio(), reverse=True)"""
        return sorted(self.alumnos(), reverse=True)

    def promedios_por_legajo(self):
        """Comprensión de diccionario: legajo -> promedio."""
        return {a.legajo: round(a.promedio(), 2) for a in self.alumnos()}

    # ================== Estadísticas (NumPy y Counter) ==================
    def estadisticas(self):
        """Estadísticas del curso con NumPy. Devuelve None si no hay alumnos."""
        promedios = np.array([a.promedio() for a in self.alumnos()])
        if promedios.size == 0:
            return None
        return {
            "promedio_general": float(np.mean(promedios)),
            "maximo": float(np.max(promedios)),
            "minimo": float(np.min(promedios)),
            "desvio_estandar": float(np.std(promedios)),
        }

    def conteo_condicion(self):
        """Counter de aprobados / desaprobados."""
        return Counter("aprobado" if a.promedio() >= NOTA_APROBACION else "desaprobado"
                       for a in self.alumnos())

    def conteo_riesgo(self, k=3):
        """Counter de 'riesgo' / 'sin riesgo' según el modelo de IA."""
        return Counter(self.predecir_riesgo(a, k) for a in self.alumnos())

    # ================== Inteligencia Artificial ==================
    def entrenar_predictor(self, ruta_historicos):
        """Lee historicos.txt (promedio;asistencia;etiqueta) y entrena el predictor."""
        cargados = 0
        try:
            with open(ruta_historicos, "r", encoding="utf-8") as archivo:
                for numero, linea in enumerate(archivo, start=1):
                    linea = linea.strip()
                    if not linea or linea.startswith("#"):
                        continue
                    try:
                        promedio, asistencia, etiqueta = linea.split(";")
                        self.__predictor.entrenar(promedio, asistencia, etiqueta)
                        cargados += 1
                    except ValueError as error:
                        print(f"  [HISTÓRICOS] Línea {numero} descartada: {error}")
        except FileNotFoundError:
            print(f"  [AVISO] No se encontró {ruta_historicos}: el predictor queda sin entrenar.")
        return cargados

    def predecir_riesgo(self, alumno, k=3):
        """Predice el riesgo del alumno usando su promedio() y su asistencia_pct."""
        return self.__predictor.predecir(alumno.promedio(), alumno.asistencia_pct, k)

    def predictor_entrenado(self):
        return self.__predictor.cantidad_casos > 0

    # ================== Reporte (generador) ==================
    def generar_reporte(self, k=3, valor_hora=None):
        """Generador: produce el reporte completo línea por línea con yield."""
        yield "=" * 70
        yield f"REPORTE - {self.nombre}"
        yield f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        yield "=" * 70
        yield f"Personas inscriptas: {len(self)} "\
              f"({len(self.alumnos())} alumnos, {len(self.profesores())} profesores)"
        yield ""
        yield "--- LISTADO DE PERSONAS ---"
        for persona in self.__personas:
            yield persona.descripcion()
        if valor_hora is not None and self.profesores():
            yield ""
            yield f"--- SUELDOS DE PROFESORES (valor hora ${valor_hora:,.0f}) ---".replace(",", ".")
            for prof in self.profesores():
                yield f"{prof.nombre}: ${prof.calcular_sueldo(valor_hora):,.0f}".replace(",", ".")
        yield ""
        yield f"--- ALUMNOS APROBADOS (promedio >= {NOTA_APROBACION}) ---"
        for texto in self.textos_aprobados() or ["(ninguno)"]:
            yield texto
        yield ""
        yield "--- ALUMNOS DESAPROBADOS ---"
        for alumno in self.desaprobados() or []:
            yield f"{alumno.nombre}: {alumno.promedio():.2f}"
        if not self.desaprobados():
            yield "(ninguno)"
        yield ""
        yield "--- RANKING POR PROMEDIO ---"
        for posicion, alumno in enumerate(self.ranking(), start=1):
            yield f"{posicion}. {alumno.nombre} ({alumno.legajo}) - {alumno.promedio():.2f}"
        yield ""
        yield "--- ESTADÍSTICAS DEL CURSO (NumPy) ---"
        estadisticas = self.estadisticas()
        if estadisticas is None:
            yield "(no hay alumnos)"
        else:
            yield f"Promedio general: {estadisticas['promedio_general']:.2f}"
            yield f"Promedio máximo:  {estadisticas['maximo']:.2f}"
            yield f"Promedio mínimo:  {estadisticas['minimo']:.2f}"
            yield f"Desvío estándar:  {estadisticas['desvio_estandar']:.2f}"
        condicion = self.conteo_condicion()
        yield f"Aprobados: {condicion['aprobado']} | Desaprobados: {condicion['desaprobado']}"
        yield ""
        yield f"--- PREDICCIÓN DE RIESGO (K-NN, k={k}) ---"
        if not self.predictor_entrenado():
            yield "(el predictor no está entrenado)"
        else:
            for alumno in self.alumnos():
                yield (f"{alumno.nombre}: promedio {alumno.promedio():.2f}, "
                       f"asistencia {alumno.asistencia_pct:g}% -> {self.predecir_riesgo(alumno, k).upper()}")
            riesgo = self.conteo_riesgo(k)
            yield f"En riesgo: {riesgo['riesgo']} | Sin riesgo: {riesgo['sin riesgo']}"
        yield "=" * 70

    def guardar_reporte(self, ruta, k=3, valor_hora=None):
        """Escribe en el archivo el reporte que va produciendo el generador."""
        escribir_lineas(ruta, self.generar_reporte(k, valor_hora))

    # ================== Archivos ==================
    @mide_tiempo
    def guardar_en_archivo(self, ruta):
        """Guarda todas las personas en el archivo, una por línea, usando a_linea()."""
        asegurar_carpeta(ruta)
        with open(ruta, "w", encoding="utf-8") as archivo:
            for persona in self.__personas:
                archivo.write(persona.a_linea() + "\n")
        return len(self.__personas)

    @staticmethod
    def _crear_desde_linea(linea):
        """Convierte una línea del archivo en un Alumno o Profesor (o lanza una excepción)."""
        campos = [c.strip() for c in linea.split(";")]
        tipo = campos[0].upper()
        if tipo == "ALUMNO":
            if len(campos) != 6:
                raise ValueError(f"un ALUMNO lleva 6 campos y la línea tiene {len(campos)}")
            _, nombre, dni, legajo, asistencia, notas_txt = campos
            notas = [n for n in notas_txt.split(",") if n.strip()]
            return Alumno(nombre, dni, legajo, asistencia, notas)
        if tipo == "PROFESOR":
            if len(campos) != 5:
                raise ValueError(f"un PROFESOR lleva 5 campos y la línea tiene {len(campos)}")
            _, nombre, dni, materia, horas = campos
            return Profesor(nombre, dni, materia, horas)
        raise ValueError(f"tipo de registro desconocido '{campos[0]}'")

    @mide_tiempo
    def cargar_desde_archivo(self, ruta):
        """Lee el archivo y reconstruye Alumnos y Profesores.
        Las líneas inválidas se descartan informando número de línea y motivo."""
        cargadas = 0
        descartadas = 0
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            print(f"  [AVISO] No existe {ruta}: se arranca con la escuela vacía.")
        else:
            # El else solo se ejecuta si el archivo se pudo abrir sin errores.
            for numero, linea in enumerate(lineas, start=1):
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue  # líneas vacías o comentarios
                motivo = None
                try:
                    self._agregar(self._crear_desde_linea(linea))
                    cargadas += 1
                except DniInvalidoError as error:
                    motivo = f"DNI inválido -> {error}"
                except LegajoInvalidoError as error:
                    motivo = f"Legajo inválido -> {error}"
                except NotaInvalidaError as error:
                    motivo = f"Nota inválida -> {error}"
                except PersonaDuplicadaError as error:
                    motivo = f"Duplicado -> {error}"
                except ValueError as error:
                    motivo = f"Línea mal formada -> {error}"
                if motivo:
                    descartadas += 1
                    print(f"  [CARGA] Línea {numero} descartada. {motivo}")
            print(f"  [CARGA] {cargadas} personas cargadas, {descartadas} líneas descartadas.")
        finally:
            print("  [CARGA] Fin de la lectura de escuela.txt")
        return cargadas, descartadas
