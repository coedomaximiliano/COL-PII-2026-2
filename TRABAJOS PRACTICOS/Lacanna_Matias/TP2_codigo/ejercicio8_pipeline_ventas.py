# Ejercicio 8 

from ejercicio7_decorador import mide_tiempo

ventas = [
    {"producto": "Notebook", "monto": 950000, "region": "CABA"},
    {"producto": "Mouse", "monto": 4500, "region": "CABA"},
    {"producto": "Monitor", "monto": 210000, "region": "Córdoba"},
    {"producto": "Pendrive", "monto": 3200, "region": "Mendoza"},
    {"producto": "Teclado", "monto": 28000, "region": "Mendoza"},
    {"producto": "Impresora", "monto": 165000, "region": "Córdoba"},
    {"producto": "Cable HDMI", "monto": 5000, "region": "CABA"},   
    {"producto": "Auriculares", "monto": 42000, "region": "CABA"},
]

DESCUENTO = 0.05


def generar_reporte(ventas_procesadas):
    """Generador: produce una línea del reporte por cada venta."""
    yield f"{'Producto':<12} {'Región':<9} {'Monto final':>12}"
    yield "-" * 35
    for v in ventas_procesadas:
        yield f"{v['producto']:<12} {v['region']:<9} ${v['monto']:>11,.2f}"


@mide_tiempo
def procesar_ventas(ventas):
    significativas = list(filter(lambda v: v["monto"] > 5000, ventas))
    con_descuento = list(map(lambda v: {**v, "monto": v["monto"] * (1 - DESCUENTO)}, significativas))
    regiones = {v["region"] for v in con_descuento}  
    total_por_region = {
        region: sum(v["monto"] for v in con_descuento if v["region"] == region)
        for region in regiones
    }
    return con_descuento, total_por_region


if __name__ == "__main__":
    procesadas, totales = procesar_ventas(ventas)

    print(f"\nVentas significativas: {len(procesadas)} de {len(ventas)}\n")
    for linea in generar_reporte(procesadas):
        print(linea)

    print("\nTotal facturado por región:")
    for region, total in sorted(totales.items()):
        print(f"  {region:<9} ${total:>12,.2f}")
