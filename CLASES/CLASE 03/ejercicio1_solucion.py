"""
EJERCICIO 1 · INDIVIDUAL — Modelar tu primera clase
Consigna: Definir una clase Persona con atributos nombre y edad, y un método
saludar() que imprima un mensaje usando esos datos. Crear dos objetos Persona
distintos y llamar a saludar() en cada uno.
"""


class Persona:
    # __init__ es el "constructor": se ejecuta automáticamente al crear
    # un objeto nuevo, y sirve para inicializar sus atributos.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo propio de cada objeto
        self.edad = edad

    # Un método es una función definida dentro de la clase; siempre
    # recibe "self" como primer parámetro para poder acceder a los
    # atributos del objeto que lo llama.
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")


# Creamos dos objetos (instancias) distintos de la misma clase.
# Cada uno guarda sus propios valores de nombre y edad.
p1 = Persona("Lucía", 20)
p2 = Persona("Martín", 23)

# Aunque llamamos al mismo método en los dos, cada objeto imprime
# su propio dato: esa es la idea central de "clase vs objeto".
p1.saludar()
p2.saludar()
