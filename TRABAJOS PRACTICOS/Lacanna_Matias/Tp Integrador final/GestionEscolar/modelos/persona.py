"""
persona.py
Clase base Persona: datos comunes a alumnos y profesores (nombre y DNI).
"""
import re

from excepciones.errores import DniInvalidoError


class Persona:
    """Persona de la escuela. Nombre y DNI son privados y se exponen con @property."""

    # Variable de clase: cuenta cuántas personas se crearon en total.
    _total_creadas = 0

    # Expresión regular: el DNI debe tener exactamente 7 u 8 dígitos.
    PATRON_DNI = re.compile(r"\d{7,8}")

    def __init__(self, nombre, dni):
        dni = str(dni).strip()
        if not Persona.validar_dni(dni):
            raise DniInvalidoError(f"DNI inválido '{dni}': debe tener 7 u 8 dígitos")
        nombre = str(nombre).strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre
        self.__dni = dni
        Persona._total_creadas += 1

    # ---------- propiedades ----------
    @property
    def nombre(self):
        """Nombre completo (solo lectura)."""
        return self.__nombre

    @property
    def dni(self):
        """DNI (solo lectura)."""
        return self.__dni

    # ---------- métodos de clase y estáticos ----------
    @classmethod
    def total_creadas(cls):
        """Informa cuántas personas (alumnos y profesores) se crearon desde que arrancó el programa."""
        return Persona._total_creadas

    @staticmethod
    def validar_dni(dni):
        """Devuelve True si el DNI tiene 7 u 8 dígitos (validado con regex)."""
        return Persona.PATRON_DNI.fullmatch(str(dni)) is not None

    # ---------- polimorfismo ----------
    def descripcion(self):
        """Descripción genérica. Alumno y Profesor la sobrescriben."""
        return f"[Persona] {self.__nombre} | DNI {self.__dni}"

    # ---------- métodos especiales ----------
    def __str__(self):
        return f"{self.__nombre} (DNI {self.__dni})"

    def __eq__(self, otra):
        """Dos personas son iguales si tienen el mismo DNI."""
        if not isinstance(otra, Persona):
            return NotImplemented
        return self.__dni == otra.dni

    def __hash__(self):
        # Al definir __eq__ hay que definir __hash__ para poder usar la persona en sets/dicts.
        return hash(self.__dni)

    def __del__(self):
        """Destructor: avisa cuando el objeto se elimina de memoria (por ejemplo, al darlo de baja)."""
        nombre = getattr(self, "_Persona__nombre", None)
        if nombre is not None:
            print(f"  [DESTRUCTOR] Se eliminó de memoria a {nombre}")
