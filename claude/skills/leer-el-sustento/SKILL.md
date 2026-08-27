---
description: Responde de qué vive una universidad chilena — «¿de dónde vienen sus ingresos?», «¿cuánto recibe del Estado?», «¿depende de los aranceles?», «¿qué pasa si baja la matrícula?», «¿recibe aportes fiscales?». Funciona para las 55 de la planilla sectorial. Las seis categorías que informa la SES muestran reparto pero no suman el ingreso de la operación, y esta puerta existe en buena parte para decirlo bien.
---

# ¿De qué vive?

Es una de las preguntas más útiles que se le pueden hacer a una universidad y **la que más fácil
se responde mal**, porque las dos categorías que la planilla informa —aranceles y aportes
fiscales— parecen las dos mitades de un todo y no lo son.

**Antes de redactar, lee `references/doctrina-de-analisis.md`.**

---

## 1 · La advertencia va primero, porque condiciona todo lo demás

La SES informa dos categorías junto al ingreso de la operación:

| Campo | Qué es, según el diccionario de la fuente |
|---|---|
| `tuition` | «Aranceles y matrículas según definición anual SES; en 2024 la nota explicita que incluye gratuidad» |
| `fiscal_contributions` | «Aportes fiscales según categoría anual SES» |

**No son partes del ingreso.** El propio diccionario advierte que no se suman «como si fueran
categorías necesariamente excluyentes», y los datos lo confirman de forma contundente: **en 19 de
las 54 universidades el arancel informado supera al ingreso de la operación**, hasta 1,49 veces.
La Universidad Mayor informa M$170.832.253 de aranceles sobre M$119.819.999 de ingreso.

La lectura correcta: el arancel es lo **facturado** por aranceles y matrículas, y el ingreso de la
operación es el **neto** que la institución reconoce. No son el mismo plano.

**Lo que no puedes escribir:**

- «Los aranceles son el 82% de sus ingresos» — el cociente puede pasar de 100% y no significa lo
  que el lector va a entender.
- «El resto viene de otras fuentes» — no hay resto: no es una descomposición.
- «Depende en un X% de la matrícula» — eso exige una apertura de ingresos que la planilla no da.

**Lo que sí puedes escribir:** los montos, cada uno con su nombre y su naturaleza, y la relación
sólo cuando la declares. *«Informa M$134.132.588 en aranceles y matrículas —una cifra facturada,
que supera al ingreso de la operación de M$98.902.577 porque no son el mismo plano— y M$2.723.875
en aportes fiscales.»*

---

## 2 · Donde sí hay un hallazgo grande

El aporte fiscal **sí** es comparable contra el ingreso, y separa al sistema en dos mitades
nítidas. En 2024:

| | Aporte fiscal sobre ingreso, mediana | Instituciones en cero |
|---|---:|---:|
| Universidades del Consejo de Rectores | **28,2%** | 0 de 27 |
| Universidades privadas | **0,3%** | 11 de 27 |

Ésa es la respuesta de verdad a «¿de qué vive?» para la mayoría de los casos, y es estructural: no
describe gestión, describe a qué mitad del sistema pertenece la institución.

Cuando la institución se salga del patrón de su tipo —una privada con aporte fiscal material, una
del Cruch con aporte bajo— **eso es el hallazgo** y merece decirse.

---

## 3 · La llamada, y las seis categorías

```
describe_fecu_institution(institution: <nombre o sigla>, year: <ejercicio>)
```

`amounts.nominal_mclp` trae la composición del ingreso declarada por la Superintendencia:

| Campo | Qué es |
|---|---|
| `tuition` | Matrículas y aranceles de pre y postgrado — **incluye la gratuidad** |
| `fiscal_contributions` | Aportes fiscales |
| `service_income` | Prestaciones de servicios |
| `extension_income` | Actividades de extensión y formación continua |
| `advisory_research_income` | Asesorías e investigaciones — **sólo desde 2024** |
| `other_income_reported` | Otros ingresos ordinarios |
| `nonoperating_income` | Ingresos no operacionales — donaciones, arriendos, dividendos, utilidad en ventas |

### Es composición, no partición: la regla que evita la cifra falsa

**Las seis categorías no suman el ingreso de la operación.** El descuadre mediano en 2024 es de
**8,9%**, y en algunos casos la suma lo supera en más de la mitad. No es un defecto de la
extracción: la planilla registra estas categorías **antes** de descontar becas internas,
descuentos y diferencias de arancel asociadas a gratuidad.

Consecuencias prácticas, las tres obligatorias:

1. **Preséntalas como reparto, en porcentaje del total declarado** —no como montos que cuadren
   contra el estado de resultados—.
2. **Nunca calcules una categoría como residuo** del ingreso menos las otras: el residuo carga
   todo el descuadre y no describe nada.
3. **No leas el arancel como porcentaje del ingreso de la operación.** En varias instituciones el
   arancel informado *supera* al ingreso —la Universidad del Desarrollo declara $176.164 millones
   de arancel contra $150.194 millones de ingreso—, y publicar «117% del ingreso» sería absurdo.

En el agregado del sistema 2024, sobre la suma de las seis: aranceles 69,8%, aportes fiscales
14,6%, prestaciones de servicios 7,7%, otros ordinarios 3,7%, extensión 2,2% y asesorías 2,0%.

**No hay razón declarada para ninguna de las seis.** No existen como métrica del registro, no
tienen banda y no traen percentil. Si necesitas la comparación con el sistema, calcula la
proporción a mano desde los montos y **declara que es un cálculo tuyo**, con la fórmula a la
vista, en vez de presentarla como una razón de la base.

---

## 4 · La cobertura, que aquí no es completa

`fiscal_contributions` está en el 96% de las observaciones y `tuition` en el 98,8%. Cuando falte,
**es un nulo y no un cero**: significa que la planilla no lo informa para esa institución y ese
año, no que la institución no reciba aportes. Dilo así.

Y hay nulos que son **columnas que ese formulario no tenía**, no ausencias de la institución:
`advisory_research_income` sólo existe desde 2024, y en ese mismo ejercicio 34 de 54
universidades lo informan. Un nulo ahí no dice que la universidad no haga asesorías.

---

## 5 · Lo que esta puerta no puede responder

> La planilla no informa **caja, deuda financiera, activo fijo, capex ni flujos**.

Y sobre el sustento en particular:

- **No abre la gratuidad.** En 2024 está dentro de los aranceles y no se puede separar. Cuánto
  viene de gratuidad y cuánto de arancel pagado es pregunta de gobierno.
- **No distingue pregrado de posgrado**, ni docencia de investigación o de extensión.
- **No trae matrícula en estudiantes.** Todo está en pesos, así que no se puede leer ingreso por
  alumno ni sensibilidad a la matrícula.
- **No dice qué es recurrente.** Un fondo concursable ganado una vez y un aporte basal permanente
  entran en la misma categoría.

---

## 6 · Los followups

| Si en los datos… | Ofrece |
|---|---|
| el aporte fiscal se aparta del patrón de su tipo | «Se financia distinto de las de su grupo, ¿quieres ver el reparto?» |
| el arancel supera al ingreso | «Esas dos cifras no son del mismo plano; ¿quieres que te explique qué informa cada una?» |
| el aporte fiscal cae de forma material en la serie | «¿Quieres la trayectoria 2019–2024?» |
| se preguntó por sensibilidad a la matrícula | «Eso necesita matrícula en estudiantes, que la planilla no trae.» |
| las seis categorías vienen con dato | «¿Quieres ver de dónde viene el resto de su ingreso, además de aranceles y aportes?» |
| la suma de las seis se aparta mucho del ingreso de la operación | «Esa diferencia es lo que la planilla no descuenta: becas internas y descuentos de arancel.» |
| `deep_dossier.available` es `true` | «De ésta además tengo la gratuidad devengada abierta, cuando su nota la separa.» |

---

## La figura de esta puerta

`composicion` — el reparto de las seis categorías declaradas.

```jsonc
{"form": "composicion", "unit_hint": "mclp", "parts": [
  {"label": "Aranceles (incluye gratuidad)", "value": <tuition>},
  {"label": "Aportes fiscales", "value": <fiscal_contributions>},
  {"label": "Prestaciones de servicios", "value": <service_income>},
  {"label": "Otros ingresos ordinarios", "value": <other_income_reported>},
  {"label": "Extensión y formación continua", "value": <extension_income>},
  {"label": "Asesorías e investigación", "value": <advisory_research_income>}]}
```

Es barras y no torta a propósito: comparar longitudes es más fácil que comparar ángulos.

**El pie de la figura declara que es reparto y no partición**, porque el lector que ve seis
barras supone que suman el ingreso de la operación y no lo hacen — se apartan un 8,9% mediano.
La etiqueta de la primera barra dice «incluye gratuidad» **siempre**, dentro de la figura: una
advertencia que sólo vive en el texto no viaja con la imagen cuando alguien la recorta.

Se compone con el renderizador, nunca a mano:

```bash
python3 ../preparar-sesion-de-consejo/assets/construir_informe.py --entrada informe.json --salida informe.html
```

El formato está en `references/contrato-de-informe.md`, y **el texto del chat se sostiene sin
la página**: quien no la abra recibió la respuesta igual.

---

## 7 · Antes de entregar

- ¿Se dijo que aranceles y aportes **no reparten** el ingreso, antes de dar cualquier cifra?
- ¿Se evitó todo porcentaje del arancel sobre el ingreso?
- ¿Si el arancel supera al ingreso, se explicó por qué en vez de esconderlo?
- ¿El aporte fiscal se comparó contra la mediana de su tipo?
- ¿Se declaró como cálculo propio cualquier cociente que no venga de la base?
- ¿Un campo ausente se informó como no divulgado y no como cero?
- ¿Se evitó decir «depende de la matrícula» sin el dato que lo sostenga?
- Si se citó la composición, ¿se presentó como reparto y no como montos que cuadren?
- ¿Se evitó calcular alguna categoría como residuo del ingreso?
- ¿Está la frase de los cinco sustantivos?
