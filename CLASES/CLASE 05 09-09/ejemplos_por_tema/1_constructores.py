"""
EJEMPLO — Constructores
El constructor __init__ se ejecuta automáticamente al crear un objeto.
Sirve para inicializar sus atributos y puede recibir parámetros, incluso
con valores por defecto.
"""


class Perfil:
    def __init__(self, usuario, seguidores=0):
        self.usuario = usuario
        self.seguidores = seguidores  # valor por defecto si no se indica
        print(f"[CONSTRUCTOR] Se creó el perfil de {self.usuario}")


p1 = Perfil("ana_dev")
p2 = Perfil("juli_py", seguidores=150)

print(f"{p1.usuario} tiene {p1.seguidores} seguidores")
print(f"{p2.usuario} tiene {p2.seguidores} seguidores")
