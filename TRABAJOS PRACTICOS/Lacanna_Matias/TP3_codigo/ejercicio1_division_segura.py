# Ejercicio 1 


def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Error: no se puede dividir {a} por cero")
        return None


if __name__ == "__main__":
    print("10 / 4 =", division_segura(10, 4))
    print("10 / 0 =", division_segura(10, 0))
