---
description: Lee la situación financiera de una universidad chilena cuando la pregunta no viene acotada — "¿cómo está X?", "analiza a X", "cuéntame de la situación financiera de X". Funciona para las 55 del sistema: arranca por el resumen sectorial y profundiza sólo si esa universidad tiene expediente auditado. Ordena la lectura, contrasta las partidas que sólo informan juntas y declara lo que no se puede ver. Para un entregable dirigido a un órgano de gobierno, usar además preparar-sesion-de-consejo.
---

# Entender una universidad

Una pregunta sin acotar —«¿cómo está la Universidad de Talca?»— no se responde con una lista
de indicadores. Se responde con una lectura ordenada, y el orden importa: puesto al revés, el
mismo conjunto de cifras produce una impresión distinta.

**Antes de redactar, lee `references/doctrina-de-analisis.md`; y si la respuesta va a ser un documento, lee también `references/contrato-de-informe.md` y produce el spec en vez de escribir HTML.** Trae las reglas comunes a toda
respuesta del plugin. Este archivo sólo aporta el método de lectura.

El destinatario habitual es un consejero que necesita entender para ejercer su rol, no un
especialista que pide un diagnóstico. Si algún concepto de base hace falta,
`references/como-leer-estos-informes.md` lo explica; remite ahí en vez de convertir la
respuesta en un curso.

## Antes de nada: qué capa tiene esta universidad

**La mayoría no tiene expediente completo.** El sistema son cincuenta y cinco universidades y
sólo una docena tiene los estados auditados cargados; para las demás hay el resumen que publica
la Superintendencia. Si esta puerta arranca suponiendo expediente, falla en cuatro de cada cinco
casos.

Primera llamada, siempre:

```
describe_fecu_institution(institution: <lo que la persona nombró>)
```

Responde por sí sola la mitad de la pregunta —montos, razones y posición entre sus pares— y
además trae `deep_dossier.available`, que decide el camino:

| | |
|---|---|
| `false` | **Lectura sectorial.** Es el caso normal. Sigue en «El orden de lectura sectorial». |
| `true` | Puedes profundizar. Sigue en «El orden de lectura completo», y usa la sectorial para la posición entre pares. |

**No anuncies la bifurcación.** A quien pregunta por una universidad sin expediente no le sirve
enterarse de que otras tienen más: le sirve una respuesta buena con lo que hay, y la frontera
dicha cuando su pregunta la toque.

---

## El orden de lectura sectorial

Cuatro bloques, con lo que la planilla sí trae. El orden importa por lo mismo que en el completo:
cada uno condiciona el siguiente.

**1 · ¿Ganó o perdió, y de dónde vino?** La cascada del ingreso al resultado del ejercicio,
pasando por el operacional, otras ganancias y el resultado financiero. El hallazgo casi nunca es
el resultado final: es la distancia entre el primero y el último. Método en `leer-el-resultado`.

**2 · ¿Cómo está parada?** Razón corriente y patrimonio sobre activos, con los montos. **Es
solvencia contable, no caja** — la planilla no informa efectivo, y eso se dice en la misma frase.
Método en `leer-la-solidez`.

**3 · ¿En qué se le va?** Costos operacionales y administración —que **sí** reconstruyen el costo
total— contrastados con el margen: una estructura pesada con margen holgado se está pagando; con
margen estrecho, no deja de dónde recortar. Y el dato que más se entiende: **qué parte del costo de
operar es gente**, con mediana de 63% en el sistema. Las remuneraciones no son una categoría aparte:
están dentro de las otras dos. Método en `leer-los-costos`.

**4 · ¿De qué vive?** Aportes fiscales contra el ingreso, que separan al sistema en dos mitades, y
la composición completa en seis categorías. Es **reparto y no partición** —las seis no suman el
ingreso de la operación, con 8,9% de descuadre mediano—, y los aranceles **no** se leen como
porcentaje del ingreso. Método en `leer-el-sustento`.

**Cuando la pregunta sea por el tiempo**, la serie ya trae los montos: `series[].nominal_mclp`
para el ejercicio y `series[].real_2024_mclp` para comparar años. **Usa los reales**: la
inflación chilena del período fue alta y una serie nominal muestra un crecimiento que no
ocurrió. La figura es `serie_temporal`, y el quiebre de presentación de 2022–2023 se marca antes
de describir la tendencia.

**Cada cifra con su posición.** Una razón corriente de 0,9 no dice nada; que sea 0,9 con el primer
cuartil de su tipo en 0,80 y la mediana en 1,05, sí. La llamada ya trae el percentil y los
cuartiles: úsalos en la misma frase que la cifra.

**Y la frontera, cuando la pregunta la toque:** la planilla no informa caja, deuda financiera,
activo fijo, capex ni flujos. Dilo como límite de la fuente, no como carencia del análisis, y di
dónde está lo que falta —en los estados auditados de esa universidad—.

---

## El orden de lectura completo

Sólo cuando `deep_dossier.available` es `true`. Cuatro bloques, en este orden. No es negociable:
cada uno condiciona cómo se lee el siguiente.

**1 · ¿Se financia la operación a sí misma?** Margen operacional y su contraparte de caja. Va
primero porque una institución que no cubre sus costos con sus ingresos tiene un problema que
ninguna holgura de balance resuelve, sólo posterga.

**2 · ¿Cuánta holgura hay y cuánta presión encima?** Caja, otros activos financieros
corrientes, obligaciones del año y la parte de la deuda que vence dentro de doce meses. Va
segundo porque acota cuánto tiempo hay para corregir lo del bloque 1.

**3 · ¿Puede seguir invirtiendo?** Inversión del año, con qué se pagó, deuda financiera y
arrendamientos. Sólo se interpreta sabiendo si la operación genera caja y cuánta hay.

> El saldo de deuda que trae `Q-INV-01` alcanza para este bloque. **Lo que no alcanza es el
> patrimonio**: en siete de las once el activo fijo vale más que todo el patrimonio, de modo
> que citarlo como respaldo describe una capacidad que no existe. La lectura completa del
> respaldo —y por qué el cociente de deuda sobre patrimonio se equivoca por arriba y por poco—
> está en `preparar-sesion-de-consejo/references/las-cinco-lecturas-profundas.md`.

**4 · ¿De qué depende?** Composición del ingreso y rigidez del gasto en personas. Explica la
fragilidad de los tres bloques anteriores ante un cambio externo.

### Qué llamadas hacer

**Dos o tres, nunca seis.** Cada contexto pesa entre ocho y diez mil tokens, y las preguntas
canónicas se solapan: `Q-INV-01` ya trae caja, deuda neta, cobertura de pasivos corrientes y
cobertura del capex, de modo que cubre los bloques 2 y 3 en una sola llamada.

| Llamada | Cubre | Cuándo |
|---|---|---|
| `Q-OPS-02` | bloque 1 | siempre |
| `Q-INV-01` | bloques 2 y 3 | siempre |
| `Q-OPS-01` | bloque 1, lado caja | si el margen abre dudas sobre la conversión a caja |
| `Q-LIQ-01` | bloque 2 en detalle | si la liquidez es el centro de la pregunta, o si el bloque 1 quedó abierto |
| `Q-REV-01`, `Q-PERS-01` | bloque 4 | a demanda, no por defecto |
| `Q-ASSET-01` | el respaldo | si la pregunta toca patrimonio, endeudamiento o «con qué responderíamos» |

Si omites un bloque, dilo. **Un bloque no consultado es distinto de un bloque sin hallazgos**,
y confundirlos hace pasar por silencio de la evidencia lo que fue una decisión tuya.

## Las cinco parejas que sólo informan juntas

Un indicador solo, en este dominio, suele mentir. Estas cinco se leen y se reportan en la misma
frase:

| Pareja | Por qué | Qué revela leerlas separadas |
|---|---|---|
| Resultado del ejercicio ↔ flujo operacional | uno es devengo, el otro es caja | resultado positivo con flujo negativo es un problema de conversión, no de rentabilidad |
| Caja ↔ otros activos financieros corrientes | la liquidez se reparte entre ambas | la caja sola puede subestimar la liquidez varias veces |
| Deuda financiera ↔ pasivos por arrendamiento | esta base los informa separados | leer sólo la deuda subestima el compromiso de pago |
| Propiedades, planta y equipo ↔ capex | el saldo cambia por revalorización | un salto de activo fijo puede no ser inversión |
| Gratuidad devengada ↔ cobros por gratuidad | son magnitudes distintas | sumarlas o compararlas produce una cifra que no existe |

**Cómo se reporta la segunda.** `Q-LIQ-01` trae los dos cocientes: la caja sobre los pasivos
corrientes, y la caja más los otros activos financieros corrientes sobre los mismos pasivos.
Van en la misma frase, con las dos magnitudes a la vista. Nunca cites el primero solo: en la
UFRO al cierre de 2024 la diferencia es 4,3% contra 38,8%, y la caja sola sugiere una estrechez
que el estado de situación no respalda. El segundo cociente no tiene banda piloto y no
significa caja libre.

## Cómo se arruina una lectura

**Empezar por el balance.** El estado de situación es una fotografía y siempre se ve más
tranquilizador que el flujo. Si abres con patrimonio y razón corriente, el lector ya tiene una
impresión formada cuando llega la operación.

**Tratar un año como una tendencia.** El calendario de cobros y pagos mueve el flujo de un año
sin que cambie nada estructural. Ninguna afirmación de trayectoria se sostiene con menos de
tres observaciones comparables.

**Comparar sin homologar.** El rango de las universidades publicadas es descriptivo, con su n a
la vista.

Y no des por hecho cuántas están afectadas: **compruébalo en el contexto de la consulta.** Cinco
de ellas traen algún quiebre declarado que toca el flujo operacional, pero desde que sus
agregados entraron a la base la mayoría son reglas de lectura silenciosas y sólo una sigue
advirtiendo. Lo que decide si una serie entra o no en una mediana es `breaks_in_question` de esa
respuesta, no un recuento aprendido: este párrafo decía «cuatro» y ya estaba desactualizado.

**Explicar la causa.** Los estados dicen qué pasó, casi nunca por qué. La causa de una caída de
caja es pregunta de gobierno.

## Forma de la salida

1. **Qué es esta institución** — escala en ingresos y perímetro, en dos líneas. Sin esto,
   ninguna cifra siguiente tiene tamaño.
2. **Los cuatro bloques**, en orden, cada uno con su pareja contrastada y su pregunta
   enunciada en castellano antes de la primera cifra.
3. **Lo que no se puede ver con estos antecedentes.**
4. **Las tres preguntas que yo haría**, dirigidas a quien puede responderlas.

Sin veredicto de salud. Una lectura describe qué puede y qué no puede hacer la institución con
lo que tiene; no la califica.

## El entregable

Si la lectura recorre los cuatro bloques, componla como documento en vez de dejarla en el
chat: es lo que el consejero va a releer antes de la sesión. Se produce el JSON del informe y
el renderizador arma la página; nunca escribas HTML. El formato está en
`references/contrato-de-informe.md`, y el `documento` es `"lectura"`.

```bash
python3 ../preparar-sesion-de-consejo/assets/construir_informe.py --entrada informe.json --salida informe.html
```

Entrega el archivo al usuario. Si la pregunta se resolvió en dos párrafos, responde en el
chat y no produzcas documento.

## Extensión

Una lectura se responde, no se despacha. Tres a cinco párrafos por bloque consultado, y la
sección de lo que no se puede ver por debajo de cinco puntos. Si el texto pasa de una pantalla
y media, sobra encuadre o falta decisión sobre qué es lo importante.

## Antes de entregar

Además de la lista de la doctrina:

- ¿La operación se leyó antes que el balance?
- ¿Cada una de las cinco parejas relevantes se reportó junta?
- ¿Se declararon los bloques que no se consultaron?
- ¿Se hicieron dos o tres llamadas, y no seis?
