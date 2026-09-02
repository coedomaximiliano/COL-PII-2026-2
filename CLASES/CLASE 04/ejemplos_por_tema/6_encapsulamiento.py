"""
EJEMPLO — Encapsulamiento
Restringe el acceso directo a los atributos de un objeto para proteger su
estado interno. En Python se aplica por convención:
  - público:   self.atributo     -> se accede libremente
  - protegido: self._atributo    -> "uso interno", no se debería tocar desde afuera
  - privado:   self.__atributo   -> Python le hace name mangling (lo
                                     renombra a _Clase__atributo)
"""


class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre        # público
        self._dni = dni             # protegido: uso interno
        self.__clave_acceso = "1234"  # privado

    def verificar_clave(self, intento):
        return intento == self.__clave_acceso

    def cambiar_clave(self, actual, nueva):
        if self.verificar_clave(actual):
            self.__clave_acceso = nueva
            print("Clave actualizada correctamente")
        else:
            print("Clave actual incorrecta, no se pudo cambiar")


p = Persona("Julián", "30111222")

print(p.nombre)          # OK: es público
print(p._dni)            # funciona, pero por convención no debería usarse así

print(p.verificar_clave("1234"))     # True
p.cambiar_clave("1234", "5678")
print(p.verificar_clave("5678"))     # True

# Esto daría error porque __clave_acceso sufrió name mangling:
# print(p.__clave_acceso)  # AttributeError

# Pero sigue siendo accesible (no es 100% inviolable) con el nombre real:
print(p._Persona__clave_acceso)  # muestra cómo funciona el name mangling
