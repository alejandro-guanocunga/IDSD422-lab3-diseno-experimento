# comparacion_experimento.R — Comparación de grupos (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/comparacion_experimento.R

# TODO 1: carga plantillas/registro_experimento.csv (read.csv)
df <- read.csv("IDSD422-lab3-diseno-experimento/plantillas/registro_experimento.csv", stringsAsFactors = FALSE)

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
#         (aggregate)
promedio_ubicacion <- aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean)
print(promedio_ubicacion)

# TODO 3: imprime el número de registros por grupo (table)
print(table(df$ubicacion))

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
cat(
  "Con solo 4 filas hay muy pocas observaciones por grupo, por lo que una diferencia en promedios puede deberse al azar o a factores externos y no a la ubicacion.\n",
  "Para concluir de forma justa se necesita mas muestra, asignacion aleatoria, control de factores externos (promociones, temporalidad) y contraste estadistico.\n"
)
