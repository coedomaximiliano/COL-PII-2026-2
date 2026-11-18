# Ejercicio 2 


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


if __name__ == "__main__":
    r = Rectangulo(5, 3)
    print(f"Rectángulo de {r.base} x {r.altura}")
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())
