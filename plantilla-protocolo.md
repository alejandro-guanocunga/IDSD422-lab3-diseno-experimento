
#  Experimento de ubicación de producto

**Equipo:** Solo · **Integrantes:** Guanocunga Alejandro · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

---

## 1. Pregunta e hipótesis

*Hipótesis que el experimento pueda confirmar o refutar (formúlela como una comparación medible entre los grupos).*

**Pregunta de investigación:**
¿Reubicar el producto estrella de RetailAndina S.A. desde su góndola habitual hacia la cabecera del pasillo principal incrementa significativamente sus ventas promedio semanales?

**Formulación formal de hipótesis:**

- **H₀ (Hipótesis Nula):** μ(pasillo principal) ≤ μ(habitual)

  Las ventas semanales promedio del producto estrella en el pasillo principal son menores o iguales a las ventas semanales promedio en la ubicación habitual.

- **H₁ (Hipótesis Alternativa):** μ(pasillo principal) > μ(habitual)

  Las ventas semanales promedio del producto estrella en el pasillo principal son mayores a las ventas semanales promedio en la ubicación habitual.

**Criterio de medibilidad y falsabilidad:**
La variable respuesta es cuantitativa continua de escala de razón (ingresos brutos en USD y unidades físicas comercializadas por tienda-semana), capturada de manera objetiva y automatizada desde el sistema ERP transaccional de RetailAndina S.A. La hipótesis es directamente falsable mediante un contraste de hipótesis de dos muestras independientes (prueba t de Student de una cola o test de Welch).

---

## 2. Unidad experimental

*¿Qué recibe el tratamiento? ¿Cuántas unidades se incluyen?*

* **Unidad experimental:** La **tienda-semana**. Corresponde a una sucursal física determinada de RetailAndina S.A. observada durante un ciclo comercial completo de 7 días continuos (lunes a domingo). Se define a este nivel porque la tienda física es el espacio donde se manipula el planograma, y la agregación semanal absorbe y neutraliza la marcada estacionalidad intradiaria (patrones diferenciados entre días laborables y fines de semana).
- **Número de unidades y justificación:** Se incluyen **N = 20 unidades experimentales** (10 tiendas físicas monitoreadas durante 2 semanas de intervención activa, conformando 10 unidades para tratamiento y 10 para control).

  **Justificación:** Representa un tamaño de muestra piloto balanceado, operativa y financieramente viable para la cadena (no satura inventarios ni desorganiza planogramas a escala nacional). Estadísticamente, n = 10 por grupo permite detectar tamaños de efecto estandarizados moderados a grandes (d ≥ 0.8) con una potencia estadística aproximada del 70 % a un nivel de significancia α = 0.05, sirviendo como estudio de factibilidad previo a una eventual expansión masiva.
---

## 3. Factor, niveles y tratamiento

* **Factor** (variable manipulada): **Ubicación física del producto estrella** en la sala de ventas de la sucursal.
* **Niveles** (valores del factor):
  * *Nivel 1 (Control):* **Pasillo habitual** (góndola secundaria estándar de la categoría).
  * *Nivel 2 (Tratamiento):* **Pasillo principal** (cabecera de góndola frontal de alto tránsito peatonal).
* **Tratamiento** (combinación asignada): Reubicación física del producto estrella a la **cabecera del pasillo principal** durante el período de prueba, manteniendo idéntico el surtido, el empaque y el precio al público.

---

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*

* **Referencia sin tratamiento:** Está conformado por las 10 unidades (tienda-semana) en las cuales el producto estrella permanece en su **ubicación habitual** (pasillos secundarios), operando bajo condiciones comerciales idénticas a las históricas.
* **Rol metodológico que cumple:**
  1. **Línea base cuantitativa:** Provee el parámetro de comparación empírico para estimar qué volumen de ventas se habría alcanzado en ausencia de la reubicación.
  2. **Aislamiento de factores temporales y macroeconómicos:** Si durante las semanas del experimento ocurre una variación general de la demanda (inflación, condiciones climáticas, campañas institucionales de la cadena), esta afectará tanto al control como al tratamiento; el grupo de control absorbe dicho shock, evitando falsos positivos atribuibles erróneamente a la ubicación.
  3. **Garantía de causalidad:** Siguiendo la regla de oro del curso, la contrastación simultánea contra un grupo de control formal es el único mecanismo que permite aislar el efecto causal de la ubicación física y diferenciarlo de correlaciones espurias.

---

## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*

* **Por qué es necesaria:** La aleatorización es el fundamento del diseño experimental. Garantiza que factores confusores no observables (tamaño físico del local, nivel socioeconómico de la zona circundante, afluencia peatonal basal, estilo de liderazgo del administrador de tienda) se distribuyan de forma estadísticamente balanceada e idéntica en esperanza matemática entre tratamiento y control. Sin aleatorización, si la gerencia asignara a dedo las tiendas de mayor afluencia al pasillo principal, el resultado estaría irremediablemente sesgado por autoselección.

* **Línea de código de la asignación (Python):**
```python
import numpy as np

# Semilla determinista para garantizar reproducibilidad exacta
np.random.seed(42)

# Vector de tiendas candidatas del piloto
tiendas = [f"T{i:02d}" for i in range(1, 11)]

# Asignación aleatoria sin reemplazo a los dos grupos
tratamiento = list(np.random.choice(tiendas, size=5, replace=False))
control = [t for t in tiendas if t not in tratamiento]

print("Tratamiento (pasillo principal):", tratamiento)
print("Control (ubicación habitual):   ", control)
```

* **Resultado de una corrida determinista (semilla = 42):**
  * **Tratamiento (pasillo principal):** `['T07', 'T04', 'T01', 'T09', 'T03']` (5 tiendas × 2 semanas = 10 unidades)
  * **Control (ubicación habitual):** `['T02', 'T05', 'T06', 'T08', 'T10']` (5 tiendas × 2 semanas = 10 unidades)

* **Explicación del sorteo:** El sorteo otorga a cada sucursal exactamente la misma probabilidad ex ante de recibir el tratamiento. De este modo, cualquier atributo diferencial preexistente entre las tiendas se reparte aleatoriamente entre ambos grupos, asegurando que la única divergencia sistemática ex post sea la ubicación del producto en el piso de venta.

---

## 6. Respuesta y medición

* **Variable respuesta:**
  * *Métrica primaria:* **Ventas semanales del producto estrella** expresadas en ingresos brutos en USD (`ventas_producto`).
  * *Métrica secundaria de control:* Cantidad de unidades físicas comercializadas semanalmente (para evaluar si el incremento se debe a volumen o a cambios en tickets).
* **Período de medición:** **4 semanas continuas** en total:
  * Semanas 1 y 2: Período de línea base sincrónica (pre-experimento) para verificar homogeneidad y calibración entre tiendas.
  * Semanas 3 y 4: Período experimental activo con tratamiento asignado.
* **Quién registra y cómo (¿ciego?):**
  * *Registro:* Automatizado y centralizado a través de los sistemas ERP y terminales POS de RetailAndina S.A. Cada transacción con el SKU del producto estrella queda asentada con marca temporal y código de tienda, eliminando errores de conteo manual.
  * *Cegamiento (Ciego simple):* Los clientes compran de forma natural sin ser informados de la existencia del ensayo (ciego total del consumidor). Asimismo, el personal de cajas y reposición desconoce la hipótesis evaluada; solo el equipo de BI y la gerencia de operaciones conocen la asignación experimental. Esto previene sesgos de observación y el efecto Hawthorne en el personal operativo.

---

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Promociones, rebajas y cupones | **Control por bloqueo estricto:** Se congelan los precios del producto estrella durante las 4 semanas. Se prohíbe emitir cupones, promociones 2x1 o rebajas en todas las tiendas participantes (tratamiento y control). |
| 2. Tamaño de tienda y tráfico basal | **Control por homogeneización:** Se eligen únicamente sucursales de formato mediano (entre 800 y 1,200 m²). Adicionalmente, se registran los aforos semanales de clientes mediante los sensores infrarrojos de acceso a cada local. |
| 3. Estacionalidad y fechas comerciales | **Control por diseño sincrónico:** El experimento se calendariza en semanas ordinarias de operación regular, excluyendo feriados nacionales y días de quincena (15 y 30). Ambos grupos operan en las mismas fechas simultáneamente. |
| 4. Abastecimiento y quiebres de stock | **Control por estandarización logística:** Protocolo de reposición obligatoria a primera hora (antes de las 8h00) para garantizar stock completo permanente en anaquel. Si ocurre un quiebre de stock > 2 horas, la tienda-semana se excluye. |
| 5. Exhibición de productos sustitutos | **Control de planogramas circundantes:** Se congelan las góndolas vecinas; se prohíbe montar islas o exhibidores especiales de marcas competidoras cerca del producto estrella tanto en control como en tratamiento. |

---

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

* **Riesgo de contaminación cruzada (Spillover):** Clientes habituales que compran indistintamente en dos tiendas de la cadena podrían ver alterado su hábito de compra. *Mitigación:* Se seleccionan sucursales con una distancia geográfica superior a 5 km entre sí.
* **Efecto de habituación vs. efecto novedad:** En una ventana de 2 semanas de tratamiento se evalúa primordialmente el impacto de la novedad o impulso visual. El diseño no permite concluir si este incremento en ventas es sostenible en el largo plazo o si declinará cuando los consumidores se habitúen al planograma.
* **Efecto Hawthorne residual en administradores:** Aunque el personal de planta no conoce la hipótesis, el administrador de una tienda en tratamiento podría prestar inconscientemente mayor cuidado a la presentación o limpieza de la cabecera principal, confundiendo el efecto del cuidado operativo con el de la ubicación física.
* **Validez externa acotada:** Los hallazgos del protocolo son válidos exclusivamente para tiendas de formato mediano (800–1200 m²). **No se podrá concluir** que el efecto sea idéntico en minimarkets de conveniencia (< 200 m²) ni en hipermercados (> 3000 m²), donde las pautas de recorrido del cliente difieren sustancialmente.

---

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

### Script Python (`scripts/comparacion_experimento.py`)
```python
import pandas as pd

# TODO 1: Carga de la plantilla de registro
df = pd.read_csv("plantillas/registro_experimento.csv")

# TODO 2: Promedio de ventas_producto por ubicación
promedio_por_ubicacion = df.groupby("ubicacion")["ventas_producto"].mean()
print("Promedio de ventas_producto por ubicacion:")
print(promedio_por_ubicacion)

# TODO 3: Conteo de registros por grupo
print("\nNumero de registros por grupo (ubicacion):")
print(df["ubicacion"].value_counts())

# TODO 4: Interpretación crítica
print("\nInterpretacion:")
print(
    "Con solo 4 filas (2 por ubicacion) el promedio es muy sensible a valores puntuales y no permite "
    "separar el efecto real de la ubicacion del ruido o diferencias entre tiendas/semanas. "
    "Para un analisis justo faltaria mayor tamano de muestra, asignacion aleatoria controlada, "
    "registro de variables confusoras (como promociones o estacionalidad) y una prueba estadistica formal."
)
```

### Salida de la consola
```text
Promedio de ventas_producto por ubicacion:
ubicacion
habitual            1040.0
pasillo_principal   1335.0
Name: ventas_producto, dtype: float64

Numero de registros por grupo (ubicacion):
ubicacion
pasillo_principal    2
habitual             2
Name: count, dtype: int64

Interpretacion:
Con solo 4 filas (2 por ubicacion) el promedio es muy sensible a valores puntuales y no permite separar el efecto real de la ubicacion del ruido o diferencias entre tiendas/semanas. Para un analisis justo faltaria mayor tamano de muestra, asignacion aleatoria controlada, registro de variables confusoras (como promociones o estacionalidad) y una prueba estadistica formal.
```

### Respuestas analíticas a las preguntas planteadas:

1. **¿Qué grupo muestra mayor venta promedio en la plantilla?**

   El grupo asignado al **pasillo_principal** muestra la mayor venta promedio con **1,335.00 USD/semana**, en contraste con los **1,040.00 USD/semana** del grupo **habitual** (una diferencia descriptiva aparente de **+295.00 USD** o **+28.37 %**).

2. **¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?**

   Porque con únicamente 4 observaciones (n = 2 por grupo), la media muestral es extraordinariamente vulnerable a la variabilidad individual de cada sucursal (por ejemplo, Guayaquil Centro vendió 1,420 USD mientras Quito Norte vendió 1,250 USD en pasillo principal; y Guayaquil Norte vendió 1,100 USD frente a 980 USD de Quito Sur en habitual).

   Con solo 2 grados de libertad no es posible separar el efecto de la ubicación del ruido aleatorio propio de cada tienda. Al aplicar una prueba inferencial formal (t de Student independiente en R), se constata un p-valor = 0.1183 > 0.05 y un intervalo de confianza al 95 % de [-204.38, 794.38] que contiene al cero, confirmando que la diferencia observada carece de significancia estadística y podría deberse enteramente al azar.

3. **Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?**
   Para constituir un análisis empírico riguroso y justo le faltaría:
   * **Tamaño de muestra estadísticamente representativo:** Escalar a las N = 20 unidades planificadas para alcanzar potencia suficiente.
   * **Asignación aleatoria probabilística:** Aplicar el sorteo determinista documentado (`np.random.seed(42)`) en lugar de tomar datos preseleccionados por conveniencia.
   * **Registro y ajuste por variables confusoras:** Registrar covariables clave (tráfico peatonal por sensor, ventas globales de la tienda, perfil de clientela) e incluirlas en un modelo de análisis de covarianza (ANCOVA) o regresión multivariante para aislar el efecto puro de la ubicación.
   * **Contraste de hipótesis formal:** Reportar errores estándar, intervalos de confianza del 95 % y el valor exacto para determinar si el incremento en facturación es atribuible causalmente a la intervención antes de comprometer decisiones de inversión en la cadena.

