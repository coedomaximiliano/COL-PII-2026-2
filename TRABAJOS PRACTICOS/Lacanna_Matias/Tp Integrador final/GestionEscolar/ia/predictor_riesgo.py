"""
predictor_riesgo.py
Clasificador K-Vecinos Más Cercanos (K-NN) implementado a mano, sin librerías de Machine Learning.
Predice si un alumno está en "riesgo" o "sin riesgo" según su promedio y su asistencia,
comparándolo con casos históricos de alumnos anteriores.

Decisión de diseño (la consigna no lo especifica): el promedio va de 0 a 10 y la asistencia
de 0 a 100. Si se usan tal cual, la asistencia pesaría 10 veces más en la distancia.
Por eso, antes de calcular la distancia, la asistencia se divide por 10 (escala 0-10).

Prueba k=1 vs k=3 (con datos/historicos.txt y datos/escuela.txt de ejemplo):
- María López (promedio 6.33, asistencia 61%):
    k=1 -> "sin riesgo": su vecino más cercano es el caso histórico 6.5;60;sin riesgo.
    k=3 -> "riesgo": los otros dos vecinos (6.0;55 y 5.5;65) son "riesgo" y ganan la votación 2 a 1.
  Con k=1 el modelo es muy sensible a un único caso atípico; con k=3 la decisión es más estable.
- El resto de los alumnos de ejemplo da la misma predicción con k=1 y con k=3.
"""
import math
from collections import Counter


class PredictorRiesgo:
    """Clasificador K-NN de riesgo académico."""

    ETIQUETAS_VALIDAS = ("riesgo", "sin riesgo")

    def __init__(self):
        # Lista privada de casos históricos: tuplas (promedio, asistencia_pct, etiqueta)
        self.__casos = []

    @property
    def cantidad_casos(self):
        return len(self.__casos)

    def entrenar(self, promedio, asistencia_pct, etiqueta):
        """Carga un caso histórico. En K-NN "entrenar" es simplemente guardar los ejemplos."""
        promedio = float(promedio)
        asistencia_pct = float(asistencia_pct)
        etiqueta = str(etiqueta).strip().lower()
        if not 0 <= promedio <= 10:
            raise ValueError(f"promedio fuera de rango: {promedio:g}")
        if not 0 <= asistencia_pct <= 100:
            raise ValueError(f"asistencia fuera de rango: {asistencia_pct:g}")
        if etiqueta not in self.ETIQUETAS_VALIDAS:
            raise ValueError(f"etiqueta desconocida: '{etiqueta}'")
        self.__casos.append((promedio, asistencia_pct, etiqueta))

    @staticmethod
    def distancia(promedio_a, asistencia_a, promedio_b, asistencia_b):
        """Distancia euclídea entre dos alumnos (asistencia llevada a escala 0-10)."""
        return math.sqrt((promedio_a - promedio_b) ** 2 + ((asistencia_a - asistencia_b) / 10) ** 2)

    def vecinos(self, promedio, asistencia_pct, k=3):
        """Devuelve los k casos más cercanos como tuplas (distancia, caso)."""
        distancias = [
            (self.distancia(promedio, asistencia_pct, p, a), (p, a, etiqueta))
            for p, a, etiqueta in self.__casos
        ]
        return sorted(distancias, key=lambda par: par[0])[:k]

    def predecir(self, promedio, asistencia_pct, k=3):
        """Devuelve la etiqueta más repetida entre los k vecinos más cercanos (voto mayoritario).
        En caso de empate gana la etiqueta del vecino más cercano, porque Counter respeta
        el orden de inserción y los vecinos ya vienen ordenados por distancia."""
        if not self.__casos:
            raise ValueError("El predictor no tiene casos históricos cargados")
        if k < 1:
            raise ValueError("k debe ser al menos 1")
        cercanos = self.vecinos(promedio, asistencia_pct, k)
        votos = Counter(caso[2] for _, caso in cercanos)
        return votos.most_common(1)[0][0]
