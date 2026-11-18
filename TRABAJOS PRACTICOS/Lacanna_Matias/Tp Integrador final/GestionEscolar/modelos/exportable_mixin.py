"""
exportable_mixin.py
Mixin (herencia múltiple) que agrega a una clase la capacidad de convertirse
en una línea de texto para guardarla en un archivo.
"""


class ExportableMixin:
    """Mixin de exportación. La clase que lo use debe implementar campos_exportables()."""

    SEPARADOR = ";"

    def campos_exportables(self):
        """Devuelve la lista de campos a guardar. Cada subclase la sobrescribe."""
        raise NotImplementedError("La clase debe implementar campos_exportables()")

    def a_linea(self):
        """Convierte el objeto en una línea de texto separada por ';'."""
        return self.SEPARADOR.join(str(campo) for campo in self.campos_exportables())
