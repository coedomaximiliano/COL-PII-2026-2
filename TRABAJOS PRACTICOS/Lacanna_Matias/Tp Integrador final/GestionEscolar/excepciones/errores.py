"""
errores.py
Excepciones personalizadas del sistema. Todas heredan de EscuelaError,
así se pueden capturar juntas (except EscuelaError) o por separado.
"""


class EscuelaError(Exception):
    """Excepción base de todo el sistema escolar."""


class DniInvalidoError(EscuelaError):
    """Se lanza cuando un DNI no tiene 7 u 8 dígitos numéricos."""


class NotaInvalidaError(EscuelaError):
    """Se lanza cuando una nota no está entre 0 y 10."""


class PersonaDuplicadaError(EscuelaError):
    """Se lanza al inscribir una persona con un DNI que ya existe en la escuela."""


class PersonaNoEncontradaError(EscuelaError):
    """Se lanza cuando se busca un DNI que no está inscripto."""


class LegajoInvalidoError(EscuelaError):
    """Se lanza cuando el legajo no respeta el formato letra mayúscula + guion + 4 dígitos (ej: A-0001).
    No la pide la consigna, se agregó para informar este error con un mensaje propio."""
