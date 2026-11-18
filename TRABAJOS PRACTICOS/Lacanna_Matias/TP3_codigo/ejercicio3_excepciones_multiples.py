# Ejercicio 3 

def dividir_cien(texto):
    try:
        numero = int(texto)
        resultado = 100 / numero
    except ValueError:
        print(f"Error: '{texto}' no es un número entero")
    except ZeroDivisionError:
        print("Error: no se puede dividir por 0")
    else:
        print(f"100 / {numero} = {resultado}")
    finally:
        print(f"[finally] Fin del procesamiento de '{texto}'\n")


if __name__ == "__main__":
    dividir_cien("4")      
    dividir_cien("hola") 
    dividir_cien("0")      
