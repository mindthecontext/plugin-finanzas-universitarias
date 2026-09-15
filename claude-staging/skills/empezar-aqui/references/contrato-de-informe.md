<!-- Copia generada al derivar el paquete. Editar doctrina/ en la raíz del saber. -->
<!-- Copia generada por scripts/sync_plugins.py. Editar doctrina/finanzas-universitarias/ en la raíz del repositorio. -->
<!-- Copia generada por scripts/sync_plugins.py. Editar doctrina/finanzas-universitarias/ en la raíz del repositorio. -->
# Contrato del informe

Cuando la respuesta es un documento —una minuta, una lectura, una comparación—, **no se
escribe HTML**. Se produce un archivo JSON con la prosa y la estructura, y el renderizador
compone la página.

> **El modelo es dueño de la prosa. El renderizador es dueño de la forma.**

Tú decides qué se dice, en qué orden, qué figura va dónde y a quién se dirige cada pregunta.
El renderizador decide tipografía, color, modo oscuro, composición de las cifras, el sello,
el dibujo de las figuras con sus marcas, y cómo se ve una abstención.

```bash
python3 ../analizar-finanzas-universitarias/assets/construir_informe.py \
  --entrada informe.json --salida informe.html
```

Después **publica ese HTML** con la herramienta de artefactos del entorno, si la hay: el
consejero recibe una página con enlace, que es lo que va a reenviar. Donde no exista, entrega
el archivo. Mencionar una ruta en el terminal no es entregar nada.

> **No escribas la página tú.** Ya pasó: una minuta salió sin sello, con el código SIES en el
> subtítulo y con los gráficos dibujados a mano, porque redactar HTML directamente parecía más
> corto que producir el spec. El resultado se veía bien y había perdido las tres garantías que
> el documento existe para dar.

---

## Cuándo produce documento y cuándo no

| Situación | Qué corresponde |
|---|---|
| `preparar-sesion-de-consejo` | siempre un documento: es su entregable |
| `entender-una-universidad` | documento cuando la lectura recorre varios bloques; prosa en el chat si es una respuesta corta |
| Pregunta acotada de un dato | prosa en el chat, sin documento |
| El usuario pide «un informe», «una minuta», «algo que pueda circular» | documento |

Un informe de 500 KB para responder cuánta caja hay es peor que una frase bien dicha.

---

## La forma del archivo

```jsonc
{
  "documento": "minuta",            // minuta | lectura | comparacion | abstencion
  "institucion": "UFRO",
  "ejercicio": 2024,

  "antetitulo": "Minuta para el consejo · Toma de conocimiento",
  "titulo": "Liquidez de la Universidad de La Frontera, cierre 2024",
  "subtitulo": "Universidad estatal de La Araucanía · cifras de la universidad sola, sin sus fundaciones ni sociedades relacionadas · montos en M$, miles de pesos",

  "secciones": [ /* ver abajo */ ],
  "figuras":  { /* ver abajo */ },

  "cifras_declaradas": [ /* la misma lista que fue a verify_reported_figures */ ],
  "verificacion":      { /* la respuesta de verify_reported_figures, tal cual */ },

  "abstencion": { /* sólo si la respuesta es una abstención; ver abajo */ },
  "pie": "Cautelas generales que cierran el documento."
}
```

**El encabezado viene escrito.** `build_financial_answer_context` devuelve `document_header`
con el subtítulo ya redactado: qué institución es, qué abarcan las cifras y en qué unidad, en
castellano. Cópialo tal cual. No lo sustituyas por códigos internos —el código SIES, «perímetro
separado», «Cruch»—, que son vocabulario nuestro y no del lector.

---

## Secciones

Cada sección lleva un `tipo` que dice **qué es**, no cómo se ve. El renderizador usa esa
etiqueta para darle su tratamiento.

| `tipo` | Para qué |
|---|---|
| `pregunta` | qué se pregunta, en una línea |
| `respuesta_una_frase` | la respuesta, o la abstención — va en recuadro |
| `establecido` | hechos con su fuente y cálculos con su fórmula |
| `trayectoria` | cómo llegó hasta aquí, con los quiebres antes de la tendencia |
| `no_concluible` | lo que estos antecedentes no permiten concluir |
| `preguntas` | preguntas para la mesa, con su destinatario |
| `trazabilidad` | de dónde sale cada cifra material |
| `bloque` | cualquier otra sección con título |
| `nota` | la escotilla: algo que no encaja en lo anterior |

Un `tipo` que no esté en esta lista **no rompe el documento**: se compone como sección
genérica y el renderizador deja constancia. Si necesitas una clase que no existe, úsala y
avísalo — es así como la biblioteca se entera de lo que falta.

```jsonc
{ "tipo": "establecido", "titulo": "Lo que está establecido", "bloques": [
    { "tipo": "parrafo", "texto": "El estado de situación informa…" },
    { "tipo": "figura", "ref": "cobertura" },
    { "tipo": "lista", "items": ["…", "…"] },
    { "tipo": "preguntas", "items": [ { "pregunta": "…", "a_quien": "Tesorería, con la nota de efectivo" } ] },
    { "tipo": "tabla", "encabezados": ["Cifra", "Fuente", "Revisión"], "filas": [["…","…","…"]] }
]}
```

En `respuesta_una_frase`, agrega `"es_abstencion": true` cuando la respuesta lo sea.

---

## Figuras

Vienen del contexto: `build_financial_answer_context` devuelve `figures`, una por figura que
la receta declara. **No inventes figuras ni decidas por tu cuenta que la respuesta lleva
gráfico.** Si la receta no declara ninguna, el informe va sin figuras.

```jsonc
"figuras": {
  "cobertura": {
    "pregunta_llana": "De todo lo que hay que pagar dentro de los próximos doce meses, ¿cuánto podría cubrirse hoy?",
    "pie": "Porcentaje de los pasivos corrientes de cada ejercicio. Planillas FECU 2019–2024 y estados auditados.",
    "figure": { /* el objeto de `figures[i]` tal cual */ }
  }
}
```

Cada figura lleva tres piezas de mobiliario, y dos de ellas las compone el renderizador:

- **`titulo`** — una frase corta que nombra la magnitud: «Cobertura de las obligaciones del
  año». Si no lo declaras, se compone con las etiquetas de las series, que suele ser peor.
- **`pregunta_llana`** — viene en `figures[i].plain_question`. Va **antes del eje**: dice qué
  responde la figura, en castellano.
- **El pie de procedencia** — lo compone el renderizador a partir de los puntos efectivamente
  dibujados: institución, cuántos ejercicios cubre y de qué fuentes salen. No lo escribas tú:
  derivarlo de los `source_refs` impide que el pie nombre una fuente que la figura no usó. Tu
  `pie` se agrega después, para lo que haga falta explicar.

Declara `institucion_nombre` en la raíz del spec —el nombre completo, no la sigla— porque es
lo que aparece en ese pie.
- Agrega `"unit_hint": "razon"` dentro de `figure` cuando la serie sea un cociente, para que
  el eje se formatee en porcentaje.
- `"reference": {"value": 1, "label": "activos corrientes = pasivos corrientes"}` dibuja un
  umbral **con significado**. Sólo si lo tiene: inventar una referencia sugiere un límite
  normativo que la metodología no sostiene.

### Las formas disponibles

`figure.form` elige la receta. Cada una pide su propia estructura de datos, y el renderizador
se niega si pides una que no existe.

| Forma | Para qué | Qué lleva |
|---|---|---|
| `serie_temporal` | evolución a través de los ejercicios | `series[].points[]` con `exercise` y `value` |
| `comparacion_pares` | una magnitud entre varias instituciones | igual que la anterior, un punto por institución |
| `balance_apilado` | qué tiene y de quién es | `stacks[]` con `label` y `parts[]` |
| `composicion` | reparto de un total en sus partes | `parts[]` con `label` y `value` |
| `cascada` | del ingreso al resultado | `steps[]` con `label`, `value` y `kind` |
| `orden` | las N que encabezan una medida | `items[]` con `label`, `value` y `highlight` opcional |

**`balance_apilado` dibuja las dos columnas a la misma altura**, porque miden lo mismo por
definición contable. Ése es el punto: lo que informa no es el total sino cómo se reparte la de
la derecha. Apila de lo más exigible a lo más propio — corriente, largo plazo, patrimonio.

**`cascada`** distingue subtotales de movimientos con `kind`: `base` y `sub` y `total` arrancan
en cero; `delta` se apila sobre el acumulado. Así se ve la distancia entre el resultado
operacional y el del ejercicio, que es donde suele estar el hallazgo.

**`composicion` no es una torta a propósito.** Comparar longitudes es más fácil que comparar
ángulos, y aquí el lector necesita ver cuánto más pesa una categoría que otra.

**`orden` dibuja las que caben; el resto se cuenta en el pie.** Un orden es la forma más fácil
de decir algo falso con cifras correctas: declara siempre sobre cuántas se ordenó y cuántas
quedaron fuera por no tener dato.

Y una regla de unidades: **`"unit_hint": "mclp"` para montos**. La fuente viene en M$ —miles de
pesos— y un eje con «461.248.371» no se lee; con la pista, el eje se acorta a pesos legibles.

Si una figura cruza un quiebre declarado sin su marca, el renderizador **no la dibuja** y la
página explica por qué. Es la conducta correcta, no un error que sortear.

---

## Cifras y sello

`cifras_declaradas` es la misma lista que enviaste a `verify_reported_figures`, y
`verificacion` es su respuesta sin modificar. De ahí sale el sello del encabezado.

### Cómo se declara cada clase de cifra

Toda cifra del texto tiene una dirección. Si crees que alguna no la tiene, revisa esta tabla
antes de darla por no comprobable: el hueco suele estar en no saber cómo pedirla.

| La cifra es… | Se declara |
|---|---|
| Un valor del expediente, de cualquier ejercicio | `{"field": "cash", "exercise": 2023}` — el monto nominal, el que imprime el estado |
| El mismo monto reexpresado a pesos de 2024 | `{"field": "cash_real_2024_mclp", "exercise": 2018}` |
| Un cálculo entre valores | `{"derived_from": ["cash", "current_liabilities"], "operation": "razon"}` — también `suma`, `diferencia`, `proporcion` |
| La mediana del grupo de pares | `{"field": "peer_median:current_ratio"}` |
| Un extremo del rango de pares | `{"field": "peer_min:…"}` o `{"field": "peer_max:…"}` |
| El n del grupo | `{"field": "peer_n:current_ratio"}` |
| Un monto citado desde la descripción de un quiebre | `{"field": "break:UTALCA-PDF-D04"}` |
| El promedio de una serie en varios ejercicios | `{"field": "mean:operating_cash_flow_to_income:2019-2024"}` — vuelve con cuántos ejercicios entraron |
| Un estadístico del sector, de la capa FECU | `{"field": "sector:operating_margin_fecu:median", "exercise": 2024, "balanced_since": 2019}` — también `p25`, `p75`, `min`, `max`, `n` |

**El estadístico sectorial exige su ejercicio, y el panel cambia el valor.** La mediana del
margen 2024 es 4,7% en el universo abierto y 4,4% en el panel equilibrado desde 2019: declarar
una por otra sale rechazada, y es la forma más fácil de equivocarse en esta capa. Si el grupo
no es el universo completo, decláralo como `{"group": "escala:cuarto de mayor ingreso"}` o
`{"group": "tipo:Universidades Cruch"}`.

Los estadísticos de pares vuelven con su **cohorte**: qué grupo, con qué n, y la advertencia de
que hoy lo define la cobertura de la base y no una decisión sobre quiénes son comparables. Si
citas uno, cita también esa condición — al ampliarse la base, la cifra cambia.

**Nominal y reexpresado no son intercambiables.** La caja de 2018 de la UFRO son M$4.748.271 en el
estado y M$6.611.649 en pesos de 2024. Declara el que escribiste, y dilo en el texto: si la cifra
está reexpresada, el lector necesita saberlo para no compararla con una nominal.

Los montos de un quiebre se verifican por pertenencia: el valor tiene que ser uno de los que
la descripción declara. Es la forma de que transcribir bien un quiebre no salga castigado.

Dos consecuencias que conviene tener presentes al redactar:

**Cada `as_written` se busca exacto en la prosa.** Escribe la cifra en el texto igual que la
declaraste. Una cifra no declarada no se compone y se ve distinta al resto.

**Manda el borrador junto con las cifras.** `verify_reported_figures` acepta `draft` con el
texto completo y devuelve los montos que aparecen en él y **nadie declaró**, con el fragmento
que los rodea. Sin eso, comprobar la declaración no sirve de nada: la declaración la decides
tú y puede omitir la mitad del documento. Si la respuesta trae `draft_scan.undeclared`,
decláralos y vuelve a verificar, o quítalos del texto si no los puedes sostener.

**Dos cifras distintas pueden escribirse igual.** En un informe de una institución no ocurre; en
un panel comparativo ocurre solo. En el de las once, el margen de la UC del Maule y el
endeudamiento de la UC del Norte dieron ambos «5,3%», y con una sola declaración el sello contó
94 de 95 sin decir cuál faltaba: el aviso de «cifra no declarada» no salta, porque la cifra sí
aparece —la que se pierde es la otra—.

`verify_reported_figures` cuenta ahora las apariciones de cada escritura y las compara con las
declaraciones que la cubren. Si el texto escribe una cifra más veces de las que se declaró, lo
dice en `draft_scan.ambiguous` con el contexto de cada aparición, y el sello queda con reservas.
No lo rechaza: el servidor no puede saber si es la misma cifra repetida a propósito o dos
distintas que coinciden, y quien redacta sí. **Si son dos, decláralas dos veces**: se comprueban,
se cuentan y se componen por separado.

**El sello cuenta sólo lo que llegó al texto.** Una cifra declarada que no aparece en ninguna
sección no cuenta y el renderizador te lo avisa. Declara lo que vas a escribir, no lo que
pensabas escribir.

**Un entregable que cita varias instituciones se comprueba en una sola llamada.** Declara
`institution` en cada cifra y `verify_reported_figures` resuelve cada una contra su propio
expediente. Devuelve `by_institution` con el recuento de cada una y un sello que ya trae el
detalle escrito:

> 95 de 95 cifras verificadas contra la base. El detalle por institución: PUCV: 9 de 9. UACH: 8
> de 8. …

Antes esto exigía una llamada por institución y **el texto del sello lo redactaba el modelo**, que
es exactamente lo que esta doctrina prohíbe para el sello de una institución sola. No era una
excepción razonada: era que el contrato no preveía el caso. Una sigla que no existe rechaza esa
cifra y no la llamada, para que un panel de once no se pierda por un error en la número siete.

**El sello también viene escrito.** `verify_reported_figures` devuelve `seal` con el texto
listo y su `estado`: `limpio`, `con_reservas` o `no_entregable`. Si es `no_entregable`, hay una
cifra que la base no sostiene y el informe no se entrega hasta corregirla.

**Y sin `verificacion` no hay informe.** El renderizador se niega a componer un documento que
cite montos sin la respuesta del verificador, y te dice cuáles encontró. No es un control que
se pueda saltar: si el servicio no responde, la respuesta es una abstención que declara qué
herramienta falta, no un informe construido con otra fuente. Un documento que no cita ninguna
cifra sí se compone, y su sello lo dice.

---

## Abstención

Cuando la respuesta es una abstención, el documento **no se acorta**. No se exige un orden
fijo de secciones —una minuta con la estructura estándar puede abstenerse bien—, pero sí que
declares **dónde** cumple cada obligación:

```jsonc
"abstencion": {
  "razon_en": "respuesta_una_frase",
  "documento_que_responderia_en": "preguntas",
  "que_si_se_puede_afirmar_en": "establecido"
}
```

Las tres referencias deben apuntar a secciones que existan en el informe. Si falta alguna, el
renderizador se niega a componer y dice cuál. No es burocracia: si no puedes señalar dónde
dices por qué no respondes, es que no lo dijiste.
