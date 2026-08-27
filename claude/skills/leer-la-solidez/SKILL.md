---
description: Responde cómo está parada una universidad chilena según su balance — «¿está sólida?», «¿puede pagar lo que debe?», «¿cuánto debe?», «¿tiene patrimonio suficiente?», «¿está muy apalancada?». Funciona para las 55 de la planilla sectorial. Es solvencia contable, no caja: la planilla no informa efectivo, y esta puerta lo dice antes que nada.
---

# ¿Cómo está parada?

Esta puerta responde con el balance, y el balance responde una pregunta más estrecha de la que
suele hacerse. **La planilla no informa efectivo**, así que aquí no se puede decir si una
institución tiene con qué pagar: sólo si sus activos corrientes cubren contablemente sus pasivos
corrientes, que no es lo mismo.

Esa distinción va **en la primera frase**, no en una nota al pie. Es la diferencia entre informar
y engañar.

**Antes de redactar, lee `references/doctrina-de-analisis.md`.**

---

## 1 · La llamada

```
describe_fecu_institution(institution: <nombre o sigla>, year: <ejercicio>)
```

Las razones son `current_ratio` y `equity_to_assets`; los montos que las producen están en
`amounts.nominal_mclp` —`current_assets`, `current_liabilities`, `equity`, `total_assets`, y los
tramos no corrientes—.

---

## 2 · Las dos razones, y qué se puede decir con cada una

**Razón corriente** (`current_ratio`) — **tiene banda declarada**: objetivo desde 1,3, aceptable
desde 1,0, preocupación bajo 1,0. Es una de las dos únicas razones de la planilla que se pueden
clasificar.

Su limitación declarada es dura y va con la cifra: *no identifica restricciones de uso ni
velocidad de realización de los activos*. Un peso en efectivo y un peso en cuentas por cobrar a
doce meses cuentan igual, y no valen igual.

**Patrimonio sobre activos** (`equity_to_assets`) — **no tiene banda**. Se describe y no se
clasifica. Y trae su propia trampa: **una revaluación de activo fijo infla patrimonio y activo a
la vez sin generar un peso de caja**, de modo que el cociente puede mejorar sin que cambie nada
de la capacidad de pago. La planilla no permite detectar la revaluación; los estados auditados sí.

---

## 3 · El monto, que aquí es más importante que el cociente

Una razón corriente de 0,72 no dice cuánto falta. **M$X de activos corrientes frente a M$Y que
vencen dentro del año** sí.

Da siempre las dos magnitudes. Y cuando la razón esté bajo 1,0, di la diferencia en pesos: es la
cifra que un consejero puede llevarse a una conversación.

---

## 4 · La posición

Las dos razones traen su percentil dentro del tipo. Aquí importa especialmente, porque **las dos
mitades del sistema se comportan distinto**: en 2024 la mediana de razón corriente de las
universidades del Consejo de Rectores es 1,42 y la de las privadas 1,05.

Decir que una privada con 1,05 «está justa» sin decir que ésa es exactamente la mediana de su
tipo es dar una alarma que los datos no sostienen.

---

## 5 · Lo que esta puerta no puede responder

> La planilla no informa **caja, deuda financiera, activo fijo, capex ni flujos**.

Sobre solidez en concreto:

- **No hay efectivo.** No se puede decir cuánta plata tiene ni cuántos meses cubre.
- **No se distingue la deuda financiera del resto del pasivo.** «Pasivos corrientes» mezcla
  proveedores, deuda bancaria, arrendamientos e ingresos diferidos, y no se pueden separar.
- **No hay vencimientos.** El pasivo corriente vence «dentro del año», y dentro de ese año puede
  estar todo en enero o repartido.
- **No hay garantías, restricciones ni covenants.** Viven en las notas.

Por eso esta puerta **no concluye solvencia**. Describe una posición de balance.

---

## 6 · Los followups

| Si en los datos… | Ofrece |
|---|---|
| la razón corriente está bajo 1,0 | «¿Quieres ver si el resultado da para sostenerlo?» → `leer-el-resultado` |
| el percentil está bajo 25 en su tipo | «¿Quieres ver cómo se reparte el sistema?» |
| `equity_to_assets` sube fuerte en un año | «Ese salto puede ser una revaluación, que no trae caja. ¿Miramos la trayectoria?» |
| `deep_dossier.available` es `true` | «De ésta además tengo caja, otros activos financieros y deuda financiera, que es lo que la planilla no separa.» |
| `deep_dossier.available` es `false` **y** se preguntó por caja | «Eso está en su estado de situación auditado; la planilla sólo trae el agregado corriente.» |

El penúltimo es el más valioso de todo el diseño: es donde la frontera deja de ser un muro.

---

## La figura de esta puerta

`balance_apilado` — dos columnas: lo que tiene y de quién es.

```jsonc
{"form": "balance_apilado", "unit_hint": "mclp", "stacks": [
  {"label": "Lo que tiene", "parts": [
    {"label": "Activos corrientes", "value": <current_assets>},
    {"label": "Activos no corrientes", "value": <noncurrent_assets>}]},
  {"label": "De quién es", "parts": [
    {"label": "Pasivos corrientes", "value": <current_liabilities>},
    {"label": "Pasivos no corrientes", "value": <noncurrent_liabilities>},
    {"label": "Patrimonio", "value": <equity>}]}]}
```

**Las dos columnas salen a la misma altura y ése es el punto**: miden lo mismo por definición
contable, así que lo que informa no es el total sino cómo se reparte la de la derecha. Apila de
lo más exigible a lo más propio — corriente, largo plazo, patrimonio.

Va cuando la pregunta sea por el patrimonio, por la solidez o por «cuánto debe»: en texto, tres
cifras del balance se leen como una lista; en la figura se ve de un vistazo qué proporción es
propia.

Se compone con el renderizador, nunca a mano:

```bash
python3 ../preparar-sesion-de-consejo/assets/construir_informe.py --entrada informe.json --salida informe.html
```

El formato está en `references/contrato-de-informe.md`, y **el texto del chat se sostiene sin
la página**: quien no la abra recibió la respuesta igual.

---

## 7 · Antes de entregar

- ¿Dice en la primera frase que es solvencia contable y no caja?
- ¿Están los dos montos junto a la razón corriente, y la diferencia en pesos si está bajo 1,0?
- ¿Se dijo que `equity_to_assets` no tiene banda?
- ¿Se advirtió de la revaluación si el patrimonio sube de forma material?
- ¿Se citó la mediana del tipo antes de calificar un nivel como estrecho?
- ¿Se evitó la palabra «solvente» y cualquier veredicto?
- ¿Está la frase de los cinco sustantivos?
