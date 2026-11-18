# Ejercicio 7 

import re

PATRON_DNI = r"\d{7,8}"
PATRON_EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def dni_valido(dni):
    return re.fullmatch(PATRON_DNI, dni) is not None


def email_valido(email):
    return re.fullmatch(PATRON_EMAIL, email) is not None


if __name__ == "__main__":
    print("Validación de DNIs:")
    for dni in ["40123456", "1234567", "123456", "123456789", "40.123.456", "4012345A"]:
        print(f"  {dni:<12} -> {'válido' if dni_valido(dni) else 'inválido'}")

    print("\nValidación de emails:")
    for email in ["matias.lacanna@gmail.com", "alumno_2026@uai.edu.ar",
                  "sin-arroba.com", "usuario@dominio", "@gmail.com"]:
        print(f"  {email:<26} -> {'válido' if email_valido(email) else 'inválido'}")

    texto = """Hola, para consultas escribir a soporte@empresa.com.ar
o al profesor (profe.programacion@uai.edu.ar).
Correos viejos que ya no se usan: info@viejo, contacto@@mal.com
Ventas: ventas2026@tienda.com"""
    print("\nEmails encontrados en el texto:")
    for e in re.findall(PATRON_EMAIL, texto):
        print("  -", e)
