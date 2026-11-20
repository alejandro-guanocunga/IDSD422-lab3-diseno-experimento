# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import pandas as pd

df = pd.read_csv("IDSD422-lab3-diseno-experimento/plantillas/registro_experimento.csv")

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
promedio_por_ubicacion = df.groupby("ubicacion")["ventas_producto"].mean()
print("Promedio de ventas_producto por ubicacion:")
print(promedio_por_ubicacion)

# TODO 3: imprime el número de registros por grupo (value_counts)
print("\nNumero de registros por grupo (ubicacion):")
print(df["ubicacion"].value_counts())

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
print("\nInterpretacion:")
print(
    "Con solo 4 filas (2 por ubicacion) el promedio es muy sensible a valores puntuales y no permite separar el efecto real de la ubicacion del ruido o diferencias entre tiendas/semanas. "
    "Para un analisis justo faltaria mayor tamano de muestra, asignacion aleatoria controlada, registro de variables confusoras (como promociones o estacionalidad) y una prueba estadistica."
)
