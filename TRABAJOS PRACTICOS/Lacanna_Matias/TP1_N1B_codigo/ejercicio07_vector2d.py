# Ejercicio 7 


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        if not isinstance(otro, Vector2D):
            return NotImplemented
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    v3 = Vector2D(3, 4)

    print(f"v1 = {v1}, v2 = {v2}, v3 = {v3}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 == v3 -> {v1 == v3}")  
    print(f"v1 == v2 -> {v1 == v2}")  
