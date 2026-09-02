"""
EJEMPLO — Métodos de clase (@classmethod) y métodos estáticos (@staticmethod)
- @classmethod recibe la clase (cls) y puede crear instancias alternativas
  o acceder/modificar variables de clase.
- @staticmethod no recibe ni self ni cls: es una función utilitaria que
  simplemente vive agrupada dentro de la clase.
"""


class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo: crea una Fecha a partir de 'dd-mm-aaaa'"""
        dia, mes, anio = texto.split("-")
        return cls(int(dia), int(mes), int(anio))

    @staticmethod
    def es_bisiesto(anio):
        """No necesita self ni cls: solo depende del parámetro recibido."""
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


f1 = Fecha(15, 8, 2026)
print(f"Fecha normal: {f1}")

f2 = Fecha.desde_texto("01-05-2024")  # uso del @classmethod
print(f"Fecha creada desde texto: {f2}")

print(f"¿2024 es bisiesto? {Fecha.es_bisiesto(2024)}")  # uso del @staticmethod
print(f"¿2026 es bisiesto? {Fecha.es_bisiesto(2026)}")
