#Definí una clase Rectangulo con atributos base y altura.
#Agregále dos métodos: area() y perimetro().
#Tu programa debe:
#Crear un rectángulo con valores a elección.
#Mostrar por consola su área y su perímetro.


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

rectangulo = Rectangulo(base, altura)
print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")
    
