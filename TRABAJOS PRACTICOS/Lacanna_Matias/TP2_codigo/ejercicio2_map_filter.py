# Ejercicio 2 

precios = [350, 800, 1200, 450, 2500, 999, 600]

duplicados = list(map(lambda p: p * 2, precios))
mayores_a_1000 = list(filter(lambda p: p > 1000, precios))

print("Lista original:     ", precios)
print("Precios duplicados: ", duplicados)
print("Precios > 1000:     ", mayores_a_1000)
