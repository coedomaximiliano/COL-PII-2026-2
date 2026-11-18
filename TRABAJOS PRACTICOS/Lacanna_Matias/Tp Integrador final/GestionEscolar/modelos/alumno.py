"""
alumno.py
Clase Alumno: hereda de Persona (herencia simple) y de ExportableMixin (herencia múltiple).
"""
import re
from functools import reduce

from excepciones.errores import NotaInvalidaError, LegajoInvalidoError
from modelos.exportable_mixin import ExportableMixin
from modelos.persona import Persona
from utilidades.decoradores import registrar_operacion


class Alumno(Persona, ExportableMixin):
    """Alumno con legajo, porcentaje de asistencia y lista privada de notas."""

    # Legajo: una letra mayúscula, un guion y 4 dígitos (ej: A-0001).
    PATRON_LEGAJO = re.compile(r"[A-Z]-\d{4}")

    def __init__(self, nombre, dni, legajo, asistencia_pct=100.0, notas=None):
        # Se valida todo ANTES de llamar a Persona.__init__, así un alumno inválido
        # no suma al contador de personas creadas.
        legajo = str(legajo).strip()
        if not Alumno.validar_legajo(legajo):
            raise LegajoInvalidoError(f"Legajo inválido '{legajo}': formato esperado A-0001")
        asistencia_pct = Alumno._validar_asistencia(asistencia_pct)
        notas_validadas = [Alumno._validar_nota(n) for n in (notas or [])]

        super().__init__(nombre, dni)
        self.__legajo = legajo
        self.__asistencia_pct = asistencia_pct
        self.__notas = notas_validadas

    # ---------- validaciones ----------
    @staticmethod
    def validar_legajo(legajo):
        """True si el legajo respeta el formato letra-4 dígitos."""
        return Alumno.PATRON_LEGAJO.fullmatch(str(legajo)) is not None

    @staticmethod
    def _validar_asistencia(valor):
        valor = float(valor)  # puede lanzar ValueError si no es número
        if not 0 <= valor <= 100:
            raise ValueError(f"La asistencia debe estar entre 0 y 100 (se recibió {valor:g})")
        return valor

    @staticmethod
    def _validar_nota(nota):
        nota = float(nota)  # puede lanzar ValueError si no es número
        if not 0 <= nota <= 10:
            raise NotaInvalidaError(f"Nota inválida {nota:g}: debe estar entre 0 y 10")
        return nota

    # ---------- propiedades ----------
    @property
    def legajo(self):
        return self.__legajo

    @property
    def asistencia_pct(self):
        """Porcentaje de asistencia (0 a 100)."""
        return self.__asistencia_pct

    @asistencia_pct.setter
    def asistencia_pct(self, valor):
        self.__asistencia_pct = Alumno._validar_asistencia(valor)

    @property
    def notas(self):
        """Copia de las notas (tupla), para que no se modifique la lista privada desde afuera."""
        return tuple(self.__notas)

    # ---------- comportamiento ----------
    @registrar_operacion
    def cargar_nota(self, nota):
        """Agrega una nota. Lanza NotaInvalidaError si no está entre 0 y 10."""
        self.__notas.append(Alumno._validar_nota(nota))

    def promedio(self):
        """Promedio de notas calculado con functools.reduce. Sin notas devuelve 0."""
        if not self.__notas:
            return 0
        return reduce(lambda acumulado, nota: acumulado + nota, self.__notas, 0) / len(self.__notas)

    def campos_exportables(self):
        notas_txt = ",".join(f"{n:g}" for n in self.__notas)
        return ["ALUMNO", self.nombre, self.dni, self.__legajo, f"{self.__asistencia_pct:g}", notas_txt]

    # ---------- polimorfismo ----------
    def descripcion(self):
        notas_txt = ", ".join(f"{n:g}" for n in self.__notas) or "sin notas"
        return (f"[Alumno]   {self.nombre} | DNI {self.dni} | Legajo {self.__legajo} | "
                f"Asistencia {self.__asistencia_pct:g}% | Notas: {notas_txt} | Promedio {self.promedio():.2f}")

    # ---------- métodos especiales ----------
    def __lt__(self, otro):
        """Permite ordenar alumnos por promedio (sorted, min, max)."""
        if not isinstance(otro, Alumno):
            return NotImplemented
        return self.promedio() < otro.promedio()

    # Al definir __eq__ en Persona, Python necesita que el hash se herede explícitamente.
    __hash__ = Persona.__hash__
