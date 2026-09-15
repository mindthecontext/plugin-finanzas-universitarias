---
name: leer-los-costos
description: Responde en qué se le va la plata a una universidad chilena y cuánta rigidez tiene — «¿cuánto se va en sueldos?», «¿tiene mucha administración?», «¿qué margen de maniobra le queda?», «¿puede absorber una caída de matrícula?», «¿está muy pesada de planta?». Funciona para las 55 de la planilla sectorial. Lee la estructura de costos —operacionales y administración, que sí reconstruyen el costo total—, cuánto de eso es nómina y cómo se reparte entre académicos, administrativos y directivos, y declara por qué una proporción alta no es por sí sola una mala noticia.
---

# ¿En qué se le va, y cuánto puede moverse?

La pregunta de fondo no es cuánto gasta, es **cuánto de lo que gasta puede dejar de gastar si el
ingreso baja**. Esa es la rigidez, y es lo que decide si un mal año se absorbe o se arrastra.

**Antes de redactar, lee `references/doctrina-de-analisis.md`.**

---

## 1 · La llamada

```
describe_fecu_institution(institution: <nombre o sigla>, year: <ejercicio>)
```

Las dos razones de esta puerta son `remuneration_to_fecu_income` y
`administration_expense_to_fecu_income`, y los montos que las producen están en `amounts`.

---

## 2 · Tres cortes de la misma plata, y sólo dos cierran

La planilla no ofrece un árbol de gastos: ofrece **tres maneras distintas de cortar el mismo
dinero**. Confundirlas es el error propio de esta puerta, y produce cifras imposibles.

| Corte | Campos | ¿Suma? |
|---|---|---|
| **Por naturaleza** | `operating_costs_amount` + `administration_expense_amount` | **Sí** — reconstruye «Costos y gastos» con 0,04% de desvío mediano; 53 de 54 dentro del 5% |
| **Por estamento** | `academic_remuneration`, `administrative_remuneration`, `executive_remuneration`, `other_remuneration` | **Sí, exacto** — suman `remuneration_amount` en las 54 |
| **Las dos proporciones** | `remuneration_to_fecu_income`, `administration_expense_to_fecu_income` | son razones sobre el ingreso, no partes de un todo |

### La regla que evita la cifra imposible

**Las remuneraciones no son una categoría hermana de los costos: están dentro de ellos.** Lo
declaran las notas al pie de la propia planilla — la (3) dice que los costos operacionales
«incluyen remuneraciones del personal y leyes sociales»; la (4) dice lo mismo de la
administración; y la (5) define el total de remuneraciones como «remuneraciones asociadas a
costos **y** remuneraciones asociadas a gastos».

> Restar remuneraciones del costo total para obtener «otros gastos» da un número **negativo en
> 29 de 55 universidades**. No es un error de la planilla: es doble contabilización.

La frase correcta no es «cuánto se va en sueldos *versus* otros», sino **cuánto del costo de
operar es gente**:

```
remuneration_amount / (operating_costs_amount + administration_expense_amount)
```

En 2024 esa proporción tiene una mediana de **63%** por institución. Es la afirmación más clara
que esta puerta puede hacer, y la única de las tres que cierra sin tolerancia.

### La nómina por dentro

Cuando la pregunta va por la estructura de personal, los cuatro estamentos están abiertos y
**disponibles en los seis ejercicios**, no sólo en el último. En el agregado del sistema 2024:
académicos 51,1% de la masa salarial, administrativos 36,9%, directivos 7,4% y otras 4,6%.

Repórtalos como reparto de la nómina, nunca como reparto del ingreso.

### Las dos proporciones sobre el ingreso

| Razón | Qué mide |
|---|---|
| `remuneration_to_fecu_income` | qué parte del ingreso se va en remuneraciones |
| `administration_expense_to_fecu_income` | qué parte se va en gasto de administración |

**Ninguna de las dos tiene banda declarada.** Se describen y no se clasifican. No escribas que un
55% de remuneraciones «está en zona de preocupación»: nadie ha declarado esa zona, y en una
universidad intensiva en docencia una proporción alta puede ser exactamente lo esperable.

**Y una proporción alta no es una mala noticia por sí sola.** Lo que la vuelve relevante es el
contraste con el margen: una institución con remuneraciones altas **y** margen holgado tiene una
estructura pesada que se está pagando; con margen estrecho, tiene poco de dónde recortar si el
ingreso cae. Di siempre las dos cosas juntas.

---

## 3 · El quiebre que sí importa aquí

Esta es la puerta donde los quiebres de la capa muerden de verdad.

**`FECU-B01`**: entre 2019–2021 y 2022 los gastos y remuneraciones **cambian de signo** en la
presentación de la planilla, y la serie usa el valor absoluto. **`FECU-B02` y `FECU-B03`** tocan
también las aperturas de ingresos y gastos.

`comparability_breaks` te los devuelve con la razón a la que toca cada uno. **Los tres alcanzan a
las dos razones de esta puerta.** Consecuencia práctica:

> Una serie de remuneraciones sobre ingreso que cruce 2021–2022 o 2022–2023 se describe por
> tramos y con el quiebre declarado antes de la cifra. No como una curva.

Es el error más fácil de esta puerta: la proporción «sube» o «baja» y en realidad cambió cómo se
presenta.

---

## 4 · La posición

Las dos razones traen su percentil dentro del tipo. Úsalo, porque el nivel absoluto significa
poco: una universidad del Consejo de Rectores y una privada de posgrado tienen estructuras
distintas por diseño, no por gestión.

Y mira **también por escala** cuando la institución sea grande o pequeña para su tipo:

```
describe_fecu_distribution(metric_id: "remuneration_to_fecu_income", year: <e>, group_by: "escala", institution: <nombre>)
```

---

## 5 · Lo que esta puerta no puede responder

> La planilla no informa **caja, deuda financiera, activo fijo, capex ni flujos**.

Y en particular, sobre costos:

- **No distingue planta permanente de honorarios.** La rigidez real depende de esa mezcla y la
  planilla no la abre. Es pregunta de gobierno, no dato.
- **No trae beneficios a los empleados** como pasivo. La obligación acumulada con el personal
  —indemnizaciones, vacaciones— no está.
- **No dice cuánto del gasto es docencia y cuánto es otra cosa.** No hay apertura funcional.
- **La apertura por naturaleza no está en todos los ejercicios.** `operating_costs_amount` abre
  desde 2023; antes de eso la planilla traía otras columnas. Un nulo ahí es **una columna que ese
  formulario no tenía**, y así se dice — nunca como un cero.

Cuando la pregunta necesite algo de esto, dilo y ofrece el camino: está en los estados auditados.

---

## 6 · Los followups

| Si en los datos… | Ofrece |
|---|---|
| la proporción de remuneraciones está sobre el p75 de su tipo **y** el margen operacional bajo la mediana | «¿Quieres ver cuánto margen le queda?» → `leer-el-resultado` |
| la serie cruza 2021–2022 o 2022–2023 | «Esa serie cruza un cambio de presentación, ¿quieres verla por tramos?» |
| el percentil por tipo y por escala difieren | «Se ve distinta según con quién la compares.» |
| `deep_dossier.available` es `true` y se preguntó por rigidez | «De ésta además tengo los beneficios a los empleados del balance auditado.» |
| los cuatro estamentos vienen con dato | «¿Quieres ver cómo se reparte la nómina entre académicos, administrativos y directivos?» |
| `operating_costs_amount` viene nulo (ejercicios anteriores a 2023) | «Ese año el formulario no abría los costos operacionales; puedo mostrarte la serie desde 2023.» |

---

## La figura de esta puerta

Dos figuras posibles, y se elige una según lo que la pregunta pida.

**`composicion` de la nómina**, cuando la pregunta va por la estructura de personal: los cuatro
estamentos, que suman exacto.

```jsonc
{"form": "composicion", "unit_hint": "mclp", "parts": [
  {"label": "Académicos", "value": <academic_remuneration>},
  {"label": "Administrativos", "value": <administrative_remuneration>},
  {"label": "Directivos", "value": <executive_remuneration>},
  {"label": "Otras remuneraciones", "value": <other_remuneration>}]}
```

**`serie_temporal`**, cuando la pregunta va por la evolución del gasto. Los montos están en
`series[].nominal_mclp`; usa los de `real_2024_mclp` si comparas años, porque la inflación del
período fue alta y una serie nominal muestra un crecimiento que no ocurrió.

**Nunca dibujes remuneraciones y costos operacionales como partes de un mismo reparto**: las
remuneraciones están dentro de los costos, y la figura sugeriría una partición que no existe.

Se compone con el renderizador, nunca a mano:

```bash
python3 ../preparar-sesion-de-consejo/assets/construir_informe.py --entrada informe.json --salida informe.html
```

El formato está en `references/contrato-de-informe.md`, y **el texto del chat se sostiene sin
la página**: quien no la abra recibió la respuesta igual.

---

## 7 · Antes de entregar

- ¿Están los montos junto a las proporciones?
- ¿Se dijo explícitamente que ninguna de las dos tiene banda?
- ¿Se evitó sumar las proporciones como si repartieran el ingreso?
- ¿Se evitó restar remuneraciones del costo total para inventar un «otros gastos»?
- Si se citó la nómina por estamento, ¿se presentó como reparto de la nómina y no del ingreso?
- ¿Se contrastó la proporción con el margen, en la misma frase?
- ¿Se declaró el quiebre antes de cualquier tendencia que lo cruce?
- ¿Se evitó llamar «rigidez» a lo que sólo es una proporción alta?
- ¿Está la frase de los cinco sustantivos?
