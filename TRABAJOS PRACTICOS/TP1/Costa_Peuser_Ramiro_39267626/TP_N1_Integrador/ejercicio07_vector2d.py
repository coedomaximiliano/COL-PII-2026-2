#Definí una clase Vector2D con atributos x e y.
#Implementá los métodos especiales __add__, __sub__, __eq__ y __str__ para poder sumar y restar vectores con los operadores + y -, compararlos con == y mostrarlos con print().
#Tu programa debe:
#Crear al menos dos vectores.
#Mostrar la suma, la resta, y el resultado de comparar dos vectores iguales y dos distintos.


class Vector2D: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

vector1 = Vector2D(2, 3)
vector2 = Vector2D(4, 5)

vector3 = vector1 + vector2
print("Suma:", vector3)

vector4 = vector1 - vector2
print("Resta:", vector4)

vector5 = Vector2D(2, 3)
print("Comparación de vectores iguales:",vector1," y ",vector5, vector1 == vector5)
print("Comparación de vectores iguales:",vector1," y ",vector2, vector1 == vector2)