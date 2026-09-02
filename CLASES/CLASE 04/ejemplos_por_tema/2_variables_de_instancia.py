"""
EJEMPLO — Variables de instancia
Son datos propios de cada objeto: se declaran con self. dentro de los
métodos (generalmente en __init__) y cada instancia tiene su propia copia.
"""


class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # variable de instancia
        self.edad = edad      # variable de instancia

    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1  # modificar esta instancia no afecta a las demás


perro = Mascota("Rocky", 3)
gato = Mascota("Michi", 5)

perro.presentarse()
gato.presentarse()

perro.cumplir_anios()
print(f"Después del cumpleaños, {perro.nombre} tiene {perro.edad} años")
print(f"{gato.nombre} sigue teniendo {gato.edad} años (no se vio afectado)")
