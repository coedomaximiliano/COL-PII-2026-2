"""
profesor.py
Clase Profesor: hereda de Persona y de ExportableMixin (herencia múltiple).
"""
from modelos.exportable_mixin import ExportableMixin
from modelos.persona import Persona


class Profesor(Persona, ExportableMixin):
    """Profesor con materia y horas cátedra."""

    def __init__(self, nombre, dni, materia, horas_catedra):
        materia = str(materia).strip()
        if not materia:
            raise ValueError("La materia no puede estar vacía")
        horas_catedra = int(horas_catedra)  # puede lanzar ValueError
        if horas_catedra <= 0:
            raise ValueError("Las horas cátedra deben ser mayores a 0")
        super().__init__(nombre, dni)
        self.__materia = materia
        self.__horas_catedra = horas_catedra

    @property
    def materia(self):
        return self.__materia

    @property
    def horas_catedra(self):
        return self.__horas_catedra

    def calcular_sueldo(self, valor_hora):
        """Sueldo = horas cátedra x valor de la hora."""
        if valor_hora < 0:
            raise ValueError("El valor hora no puede ser negativo")
        return self.__horas_catedra * valor_hora

    def campos_exportables(self):
        return ["PROFESOR", self.nombre, self.dni, self.__materia, self.__horas_catedra]

    # ---------- polimorfismo ----------
    def descripcion(self):
        return (f"[Profesor] {self.nombre} | DNI {self.dni} | Materia {self.__materia} | "
                f"{self.__horas_catedra} horas cátedra")

    __hash__ = Persona.__hash__
