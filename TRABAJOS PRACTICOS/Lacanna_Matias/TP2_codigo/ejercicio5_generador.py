# Ejercicio 5 


def multiplos_de(n, limite):
    actual = n
    while actual <= limite:
        yield actual
        actual += n


print("Múltiplos de 3 hasta 20:")
for m in multiplos_de(3, 20):
    print(m, end=" ")
print()

print("Múltiplos de 7 hasta 50:")
for m in multiplos_de(7, 50):
    print(m, end=" ")
print()


gen = multiplos_de(5, 15)
print("Con next():", next(gen), next(gen), next(gen))
