# Plantilla y ejemplo trabajado

La plantilla está abajo; primero el ejemplo, porque discutir sobre prosa concreta es más
productivo que discutir sobre una estructura vacía.

---

# Ejemplo · Universidad de la Frontera, ejercicio 2024

## Qué se pregunta

Si la operación de la universidad alcanzó a financiar su inversión del año, y qué implica
para el ejercicio siguiente.

## Respuesta en una frase

No en 2023 ni en 2024: en esos dos años la operación no sólo no financió la inversión, sino
que consumió caja, y la brecha se cubrió reduciendo el efectivo disponible y aumentando la
deuda financiera.

## Lo que está establecido

**El estado de flujos informa** flujos netos de operación por −M$4.502.620 en 2023 y
−M$4.335.021 en 2024, con compras de propiedades, planta y equipo por M$7.171.828 y
M$5.125.983 en los mismos años (UFRO‑2024.pdf, página 20; ejercicio 2023 en la columna
comparativa del mismo informe, con cotejo visual).

**El estado de situación informa** efectivo y equivalentes por M$2.164.961 al cierre de 2024,
frente a M$9.406.040 en 2021; y otros pasivos financieros por M$17.924.448, frente a
M$2.135.104 en 2021 (UFRO‑2024.pdf, página 15 y 16).

**Cálculo.** La caja cubre 4,3% de los pasivos corrientes (2.164.961 / 50.252.853). La
posición pasa de caja neta de deuda por M$7.270.936 en 2021 a deuda financiera neta de caja
por M$15.759.487 en 2024 (17.924.448 − 2.164.961).

**Ese 4,3% subestima la liquidez disponible.** El mismo estado de situación presenta otros
activos financieros corrientes por M$17.345.697 —ocho veces la caja—, que sumados a ella
cubren 38,8% de los pasivos corrientes. La disponibilidad efectiva de esos instrumentos no
está establecida en el estado de situación.

**En la FECU**, el resultado operacional del ejercicio es −M$14.216.303 y el resultado neto
−M$15.968.547, equivalente a −13,0% de los ingresos operacionales (M$123.072.257).

## Cómo llegó hasta aquí

No hay quiebres de comparabilidad que crucen el flujo operacional ni la inversión en el
período: los informes 2022, 2023 y 2024 reportan las mismas cifras para cada ejercicio
comparativo, sin reexpresión. La serie es leíble de corrido.

Entre 2019 y 2022 la operación cubrió la inversión con holgura decreciente —de 1,62 veces a
0,73—. En 2023 el flujo se vuelve negativo y en 2024 permanece negativo, mientras la
inversión se sostiene sobre M$5.000 millones anuales. En paralelo, el resultado operacional
FECU cae de −M$901.871 (2022) a −M$3.641.667 (2023) y a −M$14.216.303 (2024).

Cuatro indicadores independientes —resultado operacional, flujo operacional, caja y deuda—
se mueven en la misma dirección durante dos ejercicios consecutivos. Es la señal más
consistente entre las ocho universidades con expediente completo.

**Advertencia sobre el activo fijo.** Las propiedades, planta y equipo pasan de M$82.665.824
(2020) a M$253.667.908 (2022), con "Otras reservas" subiendo en paralelo. El capex de esos
dos años suma M$8.508.894: el salto es revalorización, no inversión, y no debe leerse como
esfuerzo de capital.

## Lo que estos antecedentes no permiten concluir

- **Nada sobre solvencia ni sobre incumplimiento.** No se conoce el calendario de
  vencimientos de la deuda, las líneas comprometidas ni los covenants.
- **Nada sobre la causa del resultado 2024.** Podría incluir partidas no recurrentes; los
  estados publicados no lo distinguen.
- **Nada sobre la liquidez efectiva.** No consta qué parte del efectivo y de los otros
  activos financieros está libre de restricción o de destino específico.
- **Nada sobre el plan de inversión.** El compromiso plurianual y su financiamiento no están
  en los estados históricos.

## Preguntas para la mesa

1. ¿Con qué se financió la brecha entre operación e inversión en 2023 y 2024, y qué
   compromisos de pago genera la deuda tomada?
2. ¿Qué parte del efectivo y de los otros activos financieros corrientes está libre de
   restricciones, y con qué plazo de realización?
3. ¿Qué explica el resultado operacional 2024 y qué parte es recurrente?
4. ¿Existe un umbral declarado a partir del cual dos ejercicios consecutivos de resultado
   operacional negativo activan una revisión formal de presupuesto?
5. ¿El ritmo de inversión responde a compromisos ya adquiridos o admite postergación?

## Trazabilidad

| Cifra | Fuente | Revisión |
|---|---|---|
| Caja, PPE 2024 y 2023 | UFRO‑2024.pdf, p. 15 | cotejo visual |
| Deuda financiera, arrendamientos, beneficios | UFRO‑2024.pdf, p. 16 | cotejo visual |
| Flujo operacional y capex | UFRO‑2024.pdf, p. 20 | cotejo visual |
| Resultado operacional, resultado neto, ingresos | FECU 2024, planilla SES | serie normalizada |

---

# Plantilla

```markdown
# [Institución], ejercicio [año]

## Qué se pregunta
[Una línea, en los términos del punto de tabla. Si el usuario no lo dijo, pregúntalo.]

## Respuesta en una frase
[La respuesta, o la abstención. Si `answer_policy.permission` es `no_respondible`,
esta sección dice qué documento respondería la pregunta y a quién pedírselo.]

## Lo que está establecido
[Hechos con documento y página. Cálculos con su fórmula a la vista. Si algún indicador
engaña, el matiz va aquí, no en una nota al pie.]

## Cómo llegó hasta aquí
[Quiebres de comparabilidad primero, tendencia después. Si no hay quiebres, decirlo.]

## Lo que estos antecedentes no permiten concluir
[Explícito. Esta sección nunca está vacía.]

## Preguntas para la mesa
[Tres a cinco, respondibles por alguien concreto.]

## Trazabilidad
[Tabla: cifra, fuente, estado de revisión.]
```

## Variante: cuando la respuesta es una abstención

Cuando la política de respuesta es `no_respondible`, el entregable **no se acorta, se
reordena**:

1. **Qué se pregunta.**
2. **Por qué estos antecedentes no la responden** — con la razón concreta, no "falta
   información".
3. **Qué documento la respondería** y quién lo tiene.
4. **Qué sí se puede afirmar mientras tanto** — lo adyacente que sí está establecido, con la
   advertencia de que no sustituye la respuesta.
5. **Preguntas para la mesa.**

Una abstención bien hecha es un entregable útil: le dice al consejo qué pedir antes de la
próxima sesión.
