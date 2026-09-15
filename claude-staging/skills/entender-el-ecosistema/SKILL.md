---
description: Describe cómo está el sistema universitario chileno en su conjunto y dónde cae una institución dentro de él — «¿cómo está el sector?», «¿esto le pasa a todas?», «¿dónde estamos frente al resto?», «¿es normal este margen?», «¿cómo ha evolucionado el sistema?». Trabaja sobre las 55 universidades de la planilla FECU y declara sin rodeos lo poco que esa fuente contiene.
---

# Entender el ecosistema

Un consejero necesita saber si lo que ve en su universidad es propio de ella o del sistema. Es
una pregunta legítima y la fuente que la responde es delgada, así que este skill vive de
declarar bien su frontera.

**El riesgo específico de esta puerta: con cincuenta y cinco instituciones detrás, cualquier
afirmación suena más sólida de lo que la fuente sostiene.** La cifra grande presta autoridad
que el dato no tiene.

**Antes de responder, lee `references/doctrina-de-analisis.md`.**

---

## 1 · Lo que la planilla FECU contiene, y lo que no

| Se puede leer del sector | No existe para el sector |
|---|---|
| ingresos de la operación y su escala | caja y otros activos financieros |
| resultado operacional y resultado del ejercicio | deuda financiera y arrendamientos |
| activos, pasivos y patrimonio | activo fijo y capex |
| remuneraciones y gasto de administración sobre ingresos | flujo de la operación |
| razón corriente | las notas explicativas |

**Quién se endeudó, quién invirtió y quién tiene liquidez no se lee del sector.** Eso sólo
existe en las instituciones con estados auditados incorporados, y decirlo del sistema
sería inventarlo. Cuando la pregunta vaya por ahí, la respuesta es que la fuente sectorial no
lo trae y que la lectura profunda existe para ocho.

---

## 2 · La regla que ordena todo lo demás: quién entra al panel

La cobertura de la planilla **no es idéntica todos los años**: oscila entre 53 y 55
universidades entre 2019 y 2024, porque hay instituciones que entran, salen o dejan de reportar.
No es un salto de régimen, son entradas y salidas.

Eso tiene una consecuencia antes de pedir cualquier serie: **una mediana de 2019 sobre 55
instituciones y una de 2024 sobre 54 no comparan a las mismas.** Para leer trayectoria hay que
pedir un panel equilibrado.

| `balanced_since` | n | Composición |
|---|---|---|
| **2019** | 52 | 26 del Consejo de Rectores y 26 privadas |
| **2020** | 52 | las mismas 52 |

**Pide `balanced_since: 2019`**, que cubre los seis ejercicios con las mismas instituciones. El
panel desde 2020 devuelve exactamente las mismas y un año menos.

> **Por qué esta sección se reescribió, y es la advertencia más importante de este archivo.**
> Hasta el 18 de agosto de 2026 decía que las universidades privadas entraban a la planilla en
> 2020, que el panel desde 2019 tenía 26 instituciones y ninguna privada, y que pedirlo y
> llamarlo «el sistema» describía la mitad con el nombre del todo.
>
> **Era falso, y el defecto era nuestro.** El extractor filtraba los tipos por el prefijo
> «Universidades» y la planilla 2019 rotula en singular —«Universidad Privada»— más una
> categoría que después desapareció. **Se perdían 28 de sus 55 universidades**, y de ese hueco
> salió una regla de lectura que se publicó como hallazgo sobre el sistema.
>
> Ninguna de las pruebas lo vio, porque todas leían nuestro derivado. Lo encontró una persona
> abriendo la planilla. **Cuando una afirmación sea sobre lo que la fuente contiene, hay que
> comprobarla contra la fuente y no contra la base.**

---

## 3 · Qué se puede decir del sistema, con cifras

Sobre el panel equilibrado desde 2019 —**52 instituciones, mitad y mitad**—, las medianas:

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---:|---:|---:|---:|---:|---:|
| margen de la operación | 4,3% | 4,6% | 7,1% | 4,0% | 4,5% | **4,8%** |
| patrimonio sobre activos | 63,2% | 65,2% | 64,5% | 65,1% | 65,4% | **66,1%** |
| razón corriente | 1,27 | 1,30 | 1,21 | 1,21 | 1,18 | **1,19** |
| remuneraciones sobre ingresos | 61,2% | 61,9% | 61,3% | 61,1% | 62,6% | **59,6%** |

Leído así, el sistema **no mejoró su margen**: lo devolvió a donde estaba tras el pico de 2021,
medio punto por encima de 2019. Lo que sí se movió en seis años es la **cobertura de corto
plazo, que bajó** de 1,27 a 1,19, y el peso de las remuneraciones, que cedió punto y medio.

Y la mediana esconde la dispersión: en 2024, sobre las 54 con dato, el margen va del percentil
25 en 1,8% al 75 en 9,2%. Entre las del Consejo de Rectores el mismo tramo es 1,8% a 7,8%, y
entre las privadas 1,3% a 10,2%: la mediana de las dos se parece y su dispersión no. Da siempre
los cuartiles, no sólo el centro.

Y **nada de esto dice algo sobre endeudamiento financiero ni sobre inversión**, porque la
planilla no los trae.

---

## 4 · Ubicar una institución en el sistema

`describe_fecu_distribution` acepta `institution` y devuelve su valor, su grupo y su percentil.
Tres reglas al usarlo:

**Elige el grupo y explícalo.** Por tipo declarado o por cuartil de ingreso. Ubicar a una
universidad regional mediana contra las cincuenta y cinco mezcla escalas que no se parecen; los
cuartiles de ingreso existen para eso.

**Percentil no es puesto.** «Está sobre el 64% de las de su cuartil de tamaño» describe; «es la
quinta mejor» califica, y eso la base no lo sostiene. Ordenar por una medida declarada sí se
puede —`rank_fecu_institutions`—, y es otra cosa: ver 4 bis.

**Y la posición no explica nada.** Que una institución esté bajo la mediana del sector no dice
por qué. La causa es pregunta de gobierno.

### Cuando la pregunta nombra dos o tres universidades

«¿Cómo se comparan la Universidad de Chile y la Católica?» no es una distribución: es una
comparación entre instituciones nombradas, y la sirve `compare_fecu_metric`.

```
compare_fecu_metric(institutions: ["UCHILE", "PUC"], metric_id: <medida>, year: <ejercicio>)
```

Acepta **cualquier medida** de `list_fecu_measures`, no sólo las seis razones: también los
montos —ingresos, gastos, patrimonio, activos, pasivos— y las derivadas. Y resuelve el nombre
como la gente lo escribe: sigla de uso corriente, nombre parcial o código SIES.

Dos reglas propias de esta comparación:

- **Compara la misma medida, no dos parecidas.** Ingresos contra ingresos. Poner el ingreso de
  una frente al resultado de otra produce una frase que suena bien y no significa nada.
- **Un monto compara tamaños.** Que una facture el triple que otra no dice nada sobre cuál está
  mejor. Si la pregunta es por desempeño, la medida es una razón.

---

## 4 bis · Ordenar, que no es rankear

`rank_fecu_institutions` devuelve las N que encabezan una medida. Es lo que responde «las diez
con más ingresos» o «las que menos dependen del arancel».

```
rank_fecu_institutions(measure: <medida>, year: <ejercicio>, limit: 10, order: "desc")
```

**Un orden por una medida declarada no es un ranking de calidad**, y la distinción no es
retórica. «Las diez con más ingresos» es un hecho verificable sobre una cifra publicada. «Las
diez mejores» es un juicio que esta base no sostiene. Ordena por lo primero y nunca escribas lo
segundo.

La respuesta trae tres defensas y las tres se citan:

- **el universo** — sobre cuántas se ordenó y cuántas quedaron fuera por no tener dato. **Una
  ausencia no es un último lugar**;
- **el corte** — cuántas instituciones hay bajo la línea. Un top diez sin decir que hay
  cuarenta y cuatro más sugiere que el resto no existe;
- **la clase de la medida** — si es un monto, la propia respuesta advierte que ordena por
  tamaño. Esa advertencia va en el texto, no se omite por incómoda.

Cuando la respuesta lleve más de cinco filas, la figura es `orden`.

---

## 5 · Los extremos mienten más que la mediana

Un extremo puede venir de una institución de escala mínima: ahí el cociente es aritméticamente
correcto y no describe nada. En 2024 hay márgenes de tres y cuatro dígitos que salen de
universidades que declaran unos pocos millones de ingreso al año.

**No cites de memoria cuál es ese extremo.** La respuesta lo trae: `income_at_extremes_mclp` da
el ingreso de quien sostiene cada punta, `income_median_mclp` da contra qué compararlo, y
`limitations` incluye el aviso **sólo cuando hay algo de qué advertir** — por grupo, y con las
cifras de esa consulta.

Esta puerta tenía aquí una cifra fija que había dejado de coincidir con la que el servicio
sirve. Es el mismo defecto que el servidor ya corrigió: un dato escrito con cuidado para una
consulta y repetido en otra.

**Si citas el rango, cita también la escala de sus puntas.** Si no lo haces, el lector supondrá
una universidad grande en crisis.

Los cuartiles resisten ese caso y los extremos no. Cuando dudes, cita p25, mediana y p75.

---

## 6 · Las dos capas no se mezclan

Una respuesta puede citar una cifra sectorial y una de expediente completo en párrafos
contiguos, y debe rotular cada una. Lo que no puede es **ponerlas en la misma comparación**: la
razón corriente FECU de una universidad y la cobertura con dos bolsillos de otra no son la
misma medida, aunque ambas hablen de liquidez.

Regla práctica: si la frase compara, las dos cifras tienen que venir de la misma capa.

---

## 7 · Cómo se arruina esta lectura

**Decir «el sector» sobre las de expediente completo**, o «el sistema» sobre las cincuenta y cinco sin
decir que sólo describe lo que la planilla trae.

**Afirmar una estrategia sectorial.** «Las universidades se están endeudando para invertir» es
exactamente lo que esta fuente no puede sostener: no tiene deuda financiera ni capex.

**Encadenar 2019 con 2024 sin panel equilibrado.** La cobertura oscila entre 53 y 55, y la
diferencia entre dos años mezcla trayectoria con entradas y salidas.

**Convertir la dispersión en tipología.** Que existan cuatro cuartiles de tamaño no crea cuatro
clases de universidad.

**Explicar la posición.** Descríbela y convierte el porqué en pregunta.

---

## 8 · Forma de la salida

1. **Qué se pregunta del sistema**, en una línea.
2. **Qué contiene esta fuente y qué no**, antes de la primera cifra. En esta puerta la frontera
   va al principio, no al final.
3. **El sistema**, con cuartiles, con el `n` del panel a la vista y con los años del medio.
4. **La institución dentro de él**, si la pregunta la nombra, con su grupo declarado.
5. **Lo que habría que mirar en la lectura profunda** —las de expediente completo— si la pregunta lo pedía y la
   capa sectorial no alcanza.

---

## 9 · Antes de entregar

- ¿La frontera de la fuente se declaró antes de la primera cifra?
- ¿Toda comparación entre ejercicios usó `balanced_since` y declaró su `n`?
- ¿Toda serie de varios años se pidió con `balanced_since` y no como diferencia entre dos universos abiertos?
- ¿La trayectoria se pidió por años y no sólo por sus extremos?
- ¿Cada estadístico citado se declaró como `sector:<metrica>:<estadistico>` con su ejercicio, su grupo y su panel?
- ¿Se dieron cuartiles y no sólo la mediana?
- ¿Si se citó un extremo, se citó la escala de quien lo sostiene?
- ¿Ninguna frase compara una cifra FECU con una de expediente completo?
- ¿Se evitó atribuir al sistema deuda, inversión o liquidez, que la planilla no trae?
- ¿Ningún percentil se enunció como puesto?
