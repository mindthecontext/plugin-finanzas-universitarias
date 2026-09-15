---
description: Responde si una universidad chilena ganó o perdió en el ejercicio y de dónde vino ese resultado — «¿cómo le fue?», «¿tuvo pérdidas?», «¿cuál fue su margen?», «¿está en números rojos?», «¿le fue mejor que el año pasado?». Funciona para las 55 universidades de la planilla sectorial, no sólo para las que tienen expediente profundo. Separa el resultado de la operación del resultado final y declara cuánto de la diferencia viene de fuera del giro.
---

# ¿Ganó o perdió, y de dónde vino?

Es la primera pregunta que hace cualquiera y la que peor se responde con un número solo, porque
**una universidad puede cerrar en azul sin que la operación haya dado**.

Esta puerta funciona con la **planilla sectorial**, de modo que sirve para las cincuenta y cinco
universidades y no sólo para las que tienen expediente. Lo que la planilla no tiene está en la
sección 6 y se dice antes de que el lector pregunte.

**Antes de redactar, lee `references/doctrina-de-analisis.md`.** Este archivo sólo aporta el
método de esta puerta.

---

## 1 · La llamada

Una sola:

```
describe_fecu_institution(institution: <nombre o sigla>, year: <ejercicio>)
```

Trae los montos en M$ —nominales y reexpresados a 2024—, las seis razones con su posición dentro
de su tipo, la serie de los seis ejercicios y la procedencia hasta la celda de la planilla.

**No enrutes esta puerta.** El enrutador está construido sobre preguntas de institución con
expediente profundo, y «¿cómo le fue?» cae en `Q-OPS-02`, que pide un contexto que cuarenta y dos
de las cincuenta y cinco no pueden dar.

---

## 2 · La cascada, que es la respuesta

La planilla trae los cuatro escalones al 100% de cobertura. Léelos en orden y **en el mismo
párrafo**:

| Escalón | Campo | Qué dice |
|---|---|---|
| Ingreso de la operación | `fecu_operating_income` | de cuánto se parte |
| Resultado operacional | `operating_result` | qué dejó el giro |
| Otras ganancias y pérdidas | `other_gains_losses` | qué entró o salió fuera del giro |
| Resultado financiero | `financial_result` | qué costó o rindió la plata |
| Resultado del ejercicio | `net_result` | con qué se cerró |

**El hallazgo casi nunca es el resultado final: es la distancia entre el primero y el último.**

- Si el resultado neto supera al operacional, el ejercicio se cerró con algo que no es el giro.
  Dilo con la cifra: *«el resultado del ejercicio fue M$X, de los cuales M$Y no vienen de la
  operación»*.
- Si el operacional es positivo y el neto negativo, la operación dio y algo se la comió — casi
  siempre el resultado financiero.
- Si los dos son negativos, la pregunta ya no es de composición.

**Nunca cites el margen sin el monto.** «Margen neto de 8%» no informa; «M$20.609.760 sobre
M$258.369.072 de ingreso, un 8%» sí.

---

## 3 · La posición, que es la mitad del significado

Un margen del 8% no es alto ni bajo. Es alto o bajo **dentro de su tipo**, y la herramienta lo
dice: `ratios[].position` trae el percentil dentro de las universidades del Consejo de Rectores o
de las privadas, con los cuartiles del grupo.

Cita siempre las dos cosas: la cifra y dónde queda. *«Un margen operacional de 11,5%, que la deja
en el percentil 89 de las universidades privadas, cuya mediana es 4,1%.»*

**El percentil no es un puesto.** La propia herramienta lo advierte: es posición descriptiva
dentro del tipo declarado, no un ranking de salud. No escribas «la novena mejor».

**Y el tipo no es la única forma de agrupar.** Si la institución es muy grande o muy pequeña para
su tipo, mira también por escala:

```
describe_fecu_distribution(metric_id: "operating_margin_fecu", year: <e>, group_by: "escala", institution: <nombre>)
```

Cuando tipo y escala dan lecturas distintas, **eso es el hallazgo** y se dice: *«entre las
privadas queda arriba; entre las de su tamaño, al medio»*.

---

## 4 · Las bandas: dos sí, cuatro no

De las seis razones de la planilla sólo **razón corriente** y **margen operacional** tienen banda
declarada en el registro. Las otras cuatro —incluido el margen neto— se describen y **no se
clasifican**.

Eso significa que puedes decir que un margen operacional de 1,2% está en la zona de atención, y
**no** puedes decir lo mismo de un margen neto de 1,2%. La herramienta trae `sin_banda_porque` en
las que no la tienen: si el texto va a hablar de zonas, declara a cuáles aplica.

Y las bandas que hay son **heurísticas piloto**, no umbrales normativos. Donde existan límites
legales, contractuales o de política interna, prevalecen.

---

## 5 · La trayectoria, cuando la pregunta la pide

`series` trae los seis ejercicios de una vez. Dos precauciones:

**Usa los montos reexpresados a 2024** para comparar años. Una serie en pesos nominales describe
la inflación tanto como a la institución. Los tienes en `amounts.real_2024_mclp`.

**Declara el quiebre antes de la tendencia.** La capa tiene cuatro quiebres de presentación
declarados y `comparability_breaks` te dice cuáles tocan tus razones. El de 2022–2023 —la
normativa contable nueva de la SES— alcanza a los dos márgenes: una serie que lo cruce se describe
por tramos, no como una curva.

---

## 6 · Lo que esta puerta no puede responder

Dilo antes de que lo pregunten, y con estos cinco sustantivos:

> La planilla no informa **caja, deuda financiera, activo fijo, capex ni flujos**.

En concreto, con el resultado en la mano **todavía no sabes**:

- Si ese resultado se convirtió en plata. Resultado y caja no son lo mismo y la planilla sólo
  trae el primero.
- Si la institución puede pagar lo que vence. Eso es `leer-la-solidez`, y aun ahí es solvencia
  contable y no caja.
- Cuánto de la utilidad es recurrente. La planilla no separa lo extraordinario dentro de «otras
  ganancias y pérdidas».

---

## 7 · Los followups: se ganan con el dato

No ofrezcas un menú. Ofrece lo que **este** resultado hace pertinente:

| Si en los datos… | Ofrece |
|---|---|
| el percentil es menor a 25 o mayor a 75 | «¿Quieres ver cómo se reparte el sistema?» |
| la serie cambia de signo en algún año | «¿Quieres la trayectoria 2019–2024?» |
| el neto y el operacional difieren de forma material | «¿Quieres ver de qué vive?» → `leer-el-sustento` |
| tipo y escala dan lecturas distintas | «Se ve distinta según con quién la compares, ¿con cuál?» |
| `deep_dossier.available` es `true` **y** la pregunta rozó la caja | «De ésta además tengo caja, deuda y flujos.» |
| `deep_dossier.available` es `false` **y** la pregunta rozó la caja | «Eso está en su estado de flujos auditado, que la planilla no resume.» |

**Uno o dos, no seis.** Un followup que el usuario no pidió compite con la respuesta.

---

## La figura de esta puerta

`cascada` — del ingreso al resultado del ejercicio.

```jsonc
{"form": "cascada", "unit_hint": "mclp", "steps": [
  {"label": "Ingresos de la operación", "value": <fecu_operating_income>, "kind": "base"},
  {"label": "Costos y gastos", "value": -<costs_and_expenses_operation_amount>, "kind": "delta"},
  {"label": "Resultado operacional", "value": <operating_result>, "kind": "sub"},
  {"label": "Otras ganancias/pérdidas", "value": <other_gains_losses>, "kind": "delta"},
  {"label": "Resultado financiero", "value": <financial_result>, "kind": "delta"},
  {"label": "Resultado del ejercicio", "value": <net_result>, "kind": "total"}]}
```

`base`, `sub` y `total` arrancan en cero; `delta` se apila sobre el acumulado. Así queda visible
**la distancia entre el resultado operacional y el del ejercicio**, que es donde suele estar el
hallazgo de esta lectura y casi nunca en la última cifra.

Va siempre que la respuesta muestre la cascada completa. Si la pregunta se resolvió en dos
cifras, no hace falta.

Se compone con el renderizador, nunca a mano:

```bash
python3 ../preparar-sesion-de-consejo/assets/construir_informe.py --entrada informe.json --salida informe.html
```

El formato está en `references/contrato-de-informe.md`, y **el texto del chat se sostiene sin
la página**: quien no la abra recibió la respuesta igual.

---

## 8 · Antes de entregar

Además de la lista de la doctrina:

- ¿Está el monto junto a cada margen, y no el margen solo?
- ¿Se dijo la distancia entre resultado operacional y neto, con su cifra?
- ¿Se citó la posición con su grupo y su n?
- ¿Se evitó convertir el percentil en un puesto o en un ranking?
- ¿Se dijo a qué razones aplica una banda y a cuáles no?
- ¿La serie que cruza el quiebre de 2022–2023 se describió por tramos?
- ¿Está la frase de los cinco sustantivos, antes de que el lector pregunte?
- ¿Los followups salen de los datos de esta respuesta y no de una lista?
- ¿Se ofreció profundidad sólo si la institución la tiene?
