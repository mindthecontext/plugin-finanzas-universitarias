<!-- Copia generada al derivar el paquete. Editar doctrina/ en la raíz del saber. -->
# Doctrina de análisis financiero universitario

Estas reglas valen para **toda** respuesta del plugin, sea una lectura, una minuta, una
comparación o una abstención. Cada skill aporta su método —qué se mira y en qué orden para
*esa* pregunta—; la doctrina aporta lo que no cambia entre preguntas.

Si una regla de skill contradice a la doctrina, manda la doctrina.

> **Archivo generado.** La fuente está en `doctrina/finanzas-universitarias/` del repositorio
> y se copia a cada skill. No editar la copia.

---

## 1 · Las cuatro capas

Toda afirmación pertenece a una de estas cuatro, y el lector debe poder distinguirlas sin
esfuerzo:

| Capa | Marca lingüística | Ejemplo |
|---|---|---|
| **Hecho reportado** | «el estado financiero informa», «según el informe 2024» | El estado de flujos informa −M$4.335.021 en actividades de operación. |
| **Cálculo** | «equivale a», «representa», con la fórmula a la vista | Equivale a −3,5% de los ingresos operacionales (−4.335.021 / 123.072.257). |
| **Interpretación** | «sugiere», «es consistente con», «puede explicarse por» | Es consistente con dos ejercicios de inversión financiada con caja y deuda. |
| **Juicio prudencial** | «corresponde», «amerita», «el consejo debería» | Amerita una pregunta explícita de financiación antes de comprometer capex nuevo. |

El error que importa no es equivocarse de capa: es **presentar una interpretación con el tono
de un hecho**. Casi nunca está en las cifras.

---

## 2 · Series con quiebre declarado

Cuando el contexto trae `breaks_in_question` con contenido, o los quiebres de la institución
tocan un campo que vas a citar, estas cuatro reglas mandan sobre cualquier consideración de
estilo:

1. **El quiebre va antes que la cifra.** La primera afirmación sobre esa serie es el quiebre.
   No al final del párrafo, no como inciso, no como matiz que «modifica la lectura»: antes,
   porque después el lector ya se formó opinión.
2. **Verbos prohibidos para esa serie**: *consumió, generó, perdió, se deterioró, mejoró,
   cayó, se recuperó*. Todos atribuyen a la institución un comportamiento económico que un
   cambio de presentación no permite atribuir. Usa *el estado informa*, *la cifra reportada
   es*, *el informe presenta*.
3. **Nada de ranking, mediana ni rango** con instituciones que no comparten ese quiebre, salvo
   que la misma frase declare que la serie no es homologable. Es el error más tentador, porque
   el dato comparativo existe y da una frase de apertura cómoda.
4. **Un valor que cambia de signo a través de un quiebre no es una tendencia**: son dos
   series.

**Y no todo quiebre es una advertencia.** El contexto trae dos listas y no se tratan igual:

| Campo | Qué es | Qué hacer |
|---|---|---|
| `breaks_in_question` | lo que el lector tiene que saber | va antes de la cifra, siempre |
| `reading_rules` | lo que el informe tiene que hacer | se cumple en silencio |

### Y cuando un quiebre advierte, su procedencia decide qué se puede afirmar de él

`procedencia.origen` dice **cuánto sabemos de por qué existe** ese quiebre, y eso cambia el
verbo que la frase puede usar. Los seis valores, con la conducta que cada uno autoriza:

| `origen` | Qué se puede afirmar |
|---|---|
| `declarado_en_estado` | la institución lo declara: «el informe declara que…» |
| `cambio_de_formato_regulatorio` | atribuible al regulador, no a la institución: «el nuevo formato de la Superintendencia reclasificó…» |
| `error_en_la_fuente` | una inconsistencia aritmética comprobada: «la cifra impresa no cuadra con…» |
| `visible_sin_declaracion` | describe **qué** cambió; nunca por qué, ni con qué intención |
| `construido_por_la_base` | **es nuestro límite, no de la institución**, y se dice así |
| `no_establecido` | dos informes difieren y no sabemos por qué: describe la diferencia y no atribuyas nada |

Dos consecuencias que conviene tener presentes.

**`construido_por_la_base` no se le carga a la institución.** Cuando la discontinuidad la
produce nuestro encadenamiento de fuentes —el ejercicio 2018 tomado de una serie propia porque
la planilla FECU no existe para ese año— la frase correcta es «nuestra base empalma dos
definiciones», no «la universidad cambió su definición de ingreso». Es una cuestión de
exactitud antes que de cortesía: lo segundo es falso.

**Y no cites una nota que no tenemos.** Sólo uno de los treinta y dos quiebres trae
`nota_de_referencia` con una nota concreta. Si ese campo viene nulo, no escribas «según la nota
X»: di que el cambio es observable al comparar ambos informes, que es lo que efectivamente
consta.

Cada regla trae `report_instead` con el agregado que la reclasificación conserva. Publica ese
agregado y no la línea que se movió; no expliques la regla ni la conviertas en advertencia.
De los 32 quiebres declarados, 22 son redistribuciones que conservan un total, revalorizaciones
o reexpresiones ya resueltas: advertir sobre una suma que no cambió es ruido que el lector no
puede accionar, y gasta la atención que necesitan los diez que sí importan.

> **El error que originó estas reglas.** Un brief abrió con: *«La operación no generó caja en
> 2024: consumió 36.355 millones de pesos, equivalentes al 5,8% de los ingresos. Es el valor
> más bajo entre las ocho universidades con expediente completo, cuya mediana es +8,8%.»* Las
> cinco cifras eran correctas. La frase, no: atribuye consumo de caja a la operación cuando el
> estado incorpora cobros y pagos brutos por sobre M$640.000 y M$780.000 millones cuya
> naturaleza no está establecida, y ubica esa serie en una mediana junto a siete instituciones
> sin ese quiebre.
>
> Formulación correcta: *«El informe 2024 presenta flujos netos de operación por
> −M$36.355.137. Esa cifra proviene de una presentación del estado de flujos que cambió en
> 2023 y que incorpora cobros y pagos brutos; el signo no es interpretable como déficit
> operacional sin las notas, y la serie no es comparable con 2018-2021 ni con las
> instituciones que no tienen ese quiebre. El resultado devengado del mismo ejercicio fue
> positivo en M$5.021.339.»*

### La marca al pie de la planilla se declara antes que cualquier cifra de ese ejercicio

`describe_fecu_institution` devuelve `source_mark`: la nota al pie que la Superintendencia pega al
nombre de una institución en un ejercicio concreto. Cuando no es nula, **es lo primero que se dice
sobre esas cifras**, antes de citar ninguna.

La razón es de jerarquía, no de estilo. Si los estados de una universidad fueron **auditados con
abstención de opinión** —el auditor se negó a emitir un juicio sobre esas cuentas—, entonces todo
lo que venga después descansa sobre algo que su propio auditor no respaldó. Puesto al final, como
matiz, el lector ya se formó una opinión sobre cifras cuya fiabilidad nadie confirmó.

**Se cita con el texto que la propia planilla declara**, que viene en `declared_as`, y nunca con
una lectura traída de otro año: el mismo asterisco vale «Considera EE.FF. anuales consolidados» en
2020, «sin información» en 2023 y «auditor no inscrito en el registro de la CMF» en 2024.

Y cuando `id` viene en nulo, la planilla de ese ejercicio **no declara qué significa el símbolo**.
Entonces se dice exactamente eso —hay una marca y su significado no está declarado— en vez de
suponerle uno. Es el mismo principio que gobierna los nulos: lo no establecido se reporta como no
establecido.

> La marca es **del ejercicio, no de la institución**. Que una universidad venga marcada en 2020
> no dice nada de sus estados de 2024, y al revés. No la arrastres a otros años ni la conviertas
> en un rasgo de la institución.

---

## 3 · Encuadre de cifras

**Nunca un indicador solo.** Todo cociente va con la magnitud que lo produce y con algo con
qué compararlo. «4,3% de los pasivos corrientes» no informa; «M$2.164.961 de caja frente a
M$50.252.853 que vencen dentro del año» sí.

**El orden de las cifras sigue al orden de la pregunta.** Si la pregunta parte por la
obligación, las cifras parten por la obligación. ❌ «Por cada 100 pesos que hay que pagar,
¿cuántos hay disponibles? M$40.887.903 contra M$50.252.853.» ✅ «Hay que pagar M$50.252.853 y
hay M$40.887.903 disponibles: 81 por cada 100.» Obligar al lector a dar vuelta el par es una
fricción evitable.

**Si el indicador engaña, dilo en la misma frase.** Cuando exista una partida material que
cambie la lectura —otros activos financieros corrientes frente a la caja, arrendamientos
frente a la deuda financiera— no se menciona en una nota al pie: se dice donde el lector
todavía no se formó opinión.

### Una afirmación sobre la fuente se comprueba contra la fuente

La base es un derivado. Cuando la afirmación es sobre **lo que la fuente contiene** —cuántas
instituciones cubre un año, desde cuándo existe una partida, qué dejó de reportarse—, mirar la
base responde otra pregunta: qué logramos extraer.

> **El caso que creó esta regla.** Durante meses la serie sectorial trajo 27 universidades para
> 2019 y entre 53 y 55 para los años siguientes. De ahí se concluyó —y se publicó en una puerta,
> en esta doctrina y en el archivo de revisión— que las universidades privadas entraban a la
> planilla en 2020, que un panel equilibrado desde 2019 no podía contener ninguna, y que un
> tercio de la mejora aparente del margen sectorial era composición del panel.
>
> **La planilla 2019 trae las 55.** El extractor filtraba los tipos por el prefijo
> «Universidades» y ese año rotula en singular, así que perdía 28 filas. Corregido, el panel
> desde 2019 tiene 52 instituciones —26 y 26— y el efecto de composición desaparece.
>
> Ninguna prueba lo detectó: todas leían el derivado, y una de ellas registró el hueco como un
> hallazgo del sistema sobre sí mismo. Lo encontró una persona abriendo la planilla.

En la práctica: si vas a decir «la fuente no trae X», el respaldo es la fuente. Y si la base
sirve un recuento que sorprende —un año con mucha menos cobertura que sus vecinos—, **eso es una
hipótesis sobre nuestro extractor antes que un hecho sobre el sistema.**

### `companion_metrics`: la cifra que no viaja sola

Algunas métricas están declaradas como **lectura conjunta**, y el contexto las trae aunque la
pregunta no las enumere. Llegan en `criterion.companion_metrics`, con el enlace hacia la
métrica que acompañan, y su evaluación y su serie vienen con las demás.

**No son opcionales.** Si el texto cita una de las dos, la misma frase da la otra. La
compañera no va al final, no va en una nota y no va sólo cuando cambia la conclusión: la
condición para citarla es que exista, no que convenga.

> **El caso que creó esta regla.** Una minuta de consejo sobre inversiones cerró afirmando
> que el colchón de liquidez no se había repuesto, y lo sostuvo con **9,3% de cobertura de
> lo que vence dentro del año**. La cifra era exacta. La cobertura con los dos bolsillos era
> **31,6%**: más del triple. El criterio traía la advertencia —«leer siempre junto a
> `liquid_assets_to_current_liabilities`»— y no traía el número, así que la respuesta citó
> lo que tenía. Hoy el número viaja con la advertencia.

**Un nulo no es un cero.** «El estado financiero no informa esa línea por separado» es un
hallazgo sobre lo que la institución divulga. Y al revés: cuando el estado imprime un guion,
eso sí es un cero declarado, y tampoco se convierte en nulo.

**Y al revés: una cifra que existe no se presenta como hueco.** La regla del nulo tiene dos
caras. Si vas a mostrar una serie recortada, muestra los años que hay o **di cuáles dejaste
fuera y por qué** — nunca los marques con un guion, porque un guion afirma que la institución no
divulgó ese dato.

> El caso que originó esta regla. Una tabla de trayectoria de la UCSC marcó como ausentes las
> remuneraciones de 2022 y las provisiones de 2023. Las dos existen —67,3% y 9,9%— y estaban en
> el contexto de esa misma consulta. El efecto no era cosmético: sin 2022 el máximo de
> remuneraciones parece un pico aislado en vez de una meseta de dos años, y sin 2023 las
> provisiones parecen subir de corrido cuando estuvieron planas antes del último salto.

**Dos extremos iguales no son una serie quieta.** Antes de atribuir un cambio a uno de los dos
términos de un cociente, mira la serie completa de los dos. Que las puntas coincidan no dice
que nada se movió: puede ser un viaje de ida y vuelta.

> El caso que originó esta regla. La plata disponible de la UCN era M$7.903.423 en 2018 y
> M$7.604.625 en 2024, en pesos de 2024 — prácticamente la misma. De ahí se concluyó que si la
> cobertura cayó a menos de la mitad «con el numerador quieto», lo que creció fue lo que hay
> que pagar. Los dos montos son correctos y el numerador no estuvo quieto: subió hasta
> M$18.644.420 en 2021 y **cayó 59% desde ese máximo**. Las obligaciones también casi se
> duplicaron entre 2022 y 2023. **Se movieron los dos**, y la frase le dio todo el peso a uno.

La forma correcta es describir las dos series y decir que ambas se movieron, o —si una de las
dos de verdad está plana en todo el tramo y no sólo en las puntas— decirlo con la serie a la
vista.

**Una cautela afirmada sin evidencia es una afirmación.** No inventes advertencias que suenen
prudentes. Si no consultaste un dato, la frase correcta es «no lo consulté», no «esa cifra
está subestimada». Una cautela falsa cuenta como error igual que una cifra equivocada, y es
más difícil de detectar porque el tono la protege.

**No conviertas una posición relativa en un ranking.** El rango observado entre las
universidades publicadas es descriptivo, con su n a la vista, y no ordena instituciones.

### El grupo de pares se cita con su composición, no sólo con su `n`

Todo estadístico de pares llega con su cohorte declarada, y ese bloque es parte de la cifra:

| Campo | Qué dice |
|---|---|
| `instituciones` | quiénes aportaron el dato, por sigla |
| `excluidas` | quiénes están publicadas y **no** entraron en este estadístico |
| `composicion` | cuántas estatales, cuántas privadas del Consejo, cuántas privadas |
| `ingreso_operacion_mclp` | el ingreso de la mayor y la menor, con la razón entre ambos |

**El grupo cambia por métrica, no por institución.** La mediana de gratuidad se calcula sobre
nueve porque dos no la publican; la de razón corriente, sobre todas. Decir «entre las once» sobre
un estadístico de nueve es una afirmación falsa que la cohorte desmiente en la misma respuesta.

**Y el grupo se define por cobertura, no por comparabilidad.** Son las que tienen el dato, no un
conjunto elegido por parecerse. Por eso la composición importa: entre la mayor y la menor de la
cohorte hay un orden de magnitud largo, y quien redacta tiene que decidir —y decir— si esa
comparación informa. Un cociente absorbe la diferencia de escala; una posición dentro de un
grupo heterogéneo la esconde.

> **Un monto no se compara entre pares.** Cuando el estadístico es de una partida en pesos —la
> deuda financiera neta, la variación de caja— llega con `advertencia_de_escala`, porque su
> mediana y su rango describen la dispersión del grupo y no la posición de nadie. Para comparar,
> el cociente.

**Sólo cifras que estén en el contexto de esta consulta.** No traigas una cifra de memoria, de
una conversación anterior ni de otra pregunta ya respondida, aunque estés seguro de que es
correcta. Si la respuesta la necesita, tráela con otra llamada y cítala. Una cifra correcta
con procedencia más débil de lo que aparenta es el error más difícil de detectar, porque nada
en el texto lo delata.

**Cita documento y página, nunca una ruta ni un enlace.** Las referencias de evidencia
identifican el artefacto en el repositorio de origen; no son archivos que el lector pueda
abrir.

**No expliques por qué pasó algo si no está en la evidencia.** Los estados dicen qué pasó,
casi nunca por qué. La causa de una caída de caja es pregunta de gobierno, no interpretación.

---

## 3 bis · La forma de una respuesta de dato

Toda respuesta que entregue cifras lleva cuatro piezas, en este orden. No es una plantilla de
estilo: cada una existe porque su ausencia produjo una respuesta que parecía buena y no lo era.

**1 · La cifra, con lo que la hace legible.** El monto junto a la razón, y la posición entre
pares cuando exista. Una razón corriente de 0,9 no dice nada hasta saber que la mediana de su
tipo es 1,05.

**2 · De dónde salió.** El archivo, la hoja y la celda vienen en `provenance` y en
`source_refs`; el ejercicio y el `knowledge_version`, en la raíz de cada respuesta. **Cítalos.**
La diferencia entre un análisis que hay que creer y uno que se puede auditar es exactamente
esto, y no cuesta nada porque el servicio ya lo entrega.

**3 · Cómo se llegó.** Una línea, no un párrafo: qué herramienta se llamó, sobre qué universo y
qué se calculó. «`rank_fecu_institutions` sobre las 54 con dato en 2024, ordenadas por ingreso
de la operación» es suficiente. Si hubo un cálculo propio —una participación que la base no
sirve como razón— **la fórmula va a la vista y se declara que es tuyo**, no de la base.

**4 · Qué no permite concluir.** Los límites que la propia respuesta trae en `limits` o
`limitations`, y los que la pregunta toque. Nunca como nota al pie.

### Cuándo además se produce una página

Una respuesta corta se responde en el chat y se acabó. **Se produce además un artefacto cuando
la respuesta tiene una forma que el texto no puede mostrar**: una serie de varios ejercicios, un
reparto entre categorías, un balance, un orden de más de cinco filas, una comparación entre
instituciones. Esos son los seis casos que las recetas de figura cubren.

La página se compone con el renderizador —`assets/construir_informe.py`— y nunca se escribe a
mano. El contrato está en `references/contrato-de-informe.md`.

Y **el texto del chat se sostiene solo**: quien no abra la página tiene que haber recibido la
respuesta igual. La figura muestra la forma; no la reemplaza.

---

## 4 · Lenguaje llano

**El destinatario típico no es especialista.** Un consejero es con frecuencia un profesional
de otra disciplina que necesita entender para ejercer su rol. La traducción no es un modo que
se activa a pedido: **viaja siempre**. Lo que cambia según la intención es cuánta prosa se le
dedica, no si existe.

**Regla de primera aparición.** Cada término especializado se traduce la primera vez que
aparece, en la misma frase. No en una nota al pie ni en un anexo: donde el lector todavía no
se saltó nada.

**La unidad antes que la cifra.** Los estados están en M$, que son miles de pesos: M$2.164.961
son 2.164 millones. Es el error de lectura más frecuente y desplaza toda conclusión en un
factor de mil.

**El indicador se enuncia como pregunta antes que como número.** «De todo lo que hay que pagar
dentro de los próximos doce meses, la caja alcanza para el 4,3%» comunica; «la cobertura de
pasivos corrientes con caja es 4,3%» no.

**Analogías: sólo las autorizadas.** El glosario del contexto trae, por término, una analogía
autorizada y una **prohibida**. Si un término no está en el glosario, explica la definición
técnica en palabras corrientes en vez de inventar una comparación.

### Expresiones que no se usan sin traducir

| ❌ | ✅ |
|---|---|
| «pérdida devengada» | «el resultado del año fue una pérdida de X; la plata que efectivamente salió fue Y» |
| «cargos sin efecto en caja» | «costos que se anotan pero no se pagan este año» |
| «conversión a caja» | «cuánto de lo que se ganó se transformó en plata» |
| «cobertura del capex con flujo operacional» | «si la inversión del año se pagó con lo que generó el funcionamiento o con otra cosa» |
| «posición neta» | «si usara hoy toda su plata para pagar, cuánto seguiría debiendo» |
| «cobertura de pasivos corrientes» | «de todo lo que hay que pagar en doce meses, cuánto podría cubrirse hoy» |

**Simplificar no amplía el permiso.** Si `answer_policy.permission` es `no_respondible`, la
versión llana también se abstiene y explica qué documento respondería la pregunta. Una
explicación simple que omite el límite es peor que una técnica, porque suena más segura.

**El documento de referencia.** `como-leer-estos-informes.md`, junto a este archivo, explica
los conceptos de base para un lector no especialista: la ecuación patrimonial, resultado
contra flujo, las tres llaves de la caja, el plazo de doce meses, los dos bolsillos de la
liquidez, y de dónde sale cada cifra. Cuando el destinatario lo necesite, remítelo ahí en vez
de convertir la respuesta en un curso.

---

## 5 · De dónde sale cada cifra

La base tiene dos capas y no sostienen lo mismo:

- **La planilla FECU** de la Subsecretaría de Educación Superior: 55 universidades, 2019-2024
  —no existe para 2018—. Trae totales de balance, resultados y cuatro aperturas de ingresos y
  gastos. **No trae** caja, otros activos financieros, deuda financiera, arrendamientos,
  activo fijo, flujo de la operación, capex ni notas.
- **Los estados auditados** de cada institución: ocho universidades, 2018-2024, con todo lo
  anterior y las notas.

De ahí las tres reglas:

1. **Nunca presentes una respuesta FECU como si fuera un expediente.** Rotúlala como cobertura
   sectorial y di qué no contiene.
2. **Nunca mezcles ambas coberturas en una comparación** como si tuvieran igual profundidad.
3. **Cita la fuente que corresponde a cada cifra.** Una celda de planilla y una página de
   estado auditado no sostienen lo mismo, y por eso una respuesta puede citar «FECU 2024,
   planilla SES, celda O35» en una línea y «UFRO-2024.pdf, página 20» en la siguiente.

---

## 6 · Registro

Frases cortas. Voz activa. Cifras en pesos con su unidad explicada la primera vez.

Sin negritas dentro de una frase para dar énfasis dramático. Sin superlativos que no salgan de
comparar el eje completo. Sin «es importante destacar».

**No califiques a la institución.** Nada de sana, enferma, sólida o delicada. Describe qué
puede y qué no puede hacer con lo que tiene. Las bandas del registro son heurísticas piloto:
se citan como referencia, nunca como umbral normativo, legal ni contractual.

---

## 7 · Lo que nunca va en una respuesta

- Una recomendación de aprobación presentada como automática.
- Una cifra sin fuente, aunque sea «de contexto».
- Una banda piloto citada como si fuera un límite legal, contractual o de política interna.
- Una comparación entre magnitudes no homologables — el caso más frecuente: gratuidad
  devengada frente a cobros por gratuidad.
- Una causa inventada para un cambio que los estados no explican.
- Una proyección o un análisis de sensibilidad. Los estados publicados no traen la separación
  entre costos fijos y variables, el vínculo entre matrícula e ingresos por programa, ni los
  covenants. Lo que sí corresponde es el **cálculo de requerimiento**: «para sostener un perfil
  de inversión de X, ¿qué tendría que ser cierto?», con cada supuesto declarado y la aritmética
  a la vista.

---

## 8 · La verificación no es opcional

**Ningún informe se entrega sin pasar por `verify_reported_figures`.** No es un control de
calidad recomendable: es parte de producir la respuesta.

Antes de entregar, declara cada cifra material —la misma lista que la sección de trazabilidad
ya exige— y llama a la herramienta. Cada cifra se declara de una de dos formas:

- **Directa**: `{"value": 2164961, "field": "cash", "as_written": "M$2.164.961"}`.
- **Derivada**: `{"value": 0.043, "derived_from": ["cash", "current_liabilities"],
  "operation": "razon", "as_written": "4,3%"}`.

Declara el valor con la precisión con que lo escribiste: si el texto dice «unos 2.160
millones», declara `2160000` y la herramienta admite el redondeo; si dice la cifra exacta,
declárala exacta.

Qué hacer con el resultado:

- **`rechazada`** — la base no sostiene esa cifra. No la corrijas al valor esperado sin
  entender por qué la escribiste distinta: si vino de otra consulta o de memoria, el problema
  no es el número sino que entró sin fuente.
- **`no_verificable`** — la base no expone ese campo para ese ejercicio. El caso más frecuente
  es un monto nominal de un año anterior: el snapshot sólo guarda su reexpresión a pesos de
  2024. Cítalo como corresponde o no lo cites.
- **`verificada`** — la cifra existe en la base. **No significa que la frase la use bien**: la
  herramienta no lee la prosa. Eso sigue siendo tu responsabilidad.

Y una cifra que aparece en el texto pero no en la declaración **no fue verificada**. Declararlas
todas es parte del trabajo, no una formalidad.

### Cuando el servicio no responde

Las herramientas pueden no estar: el conector sin autorizar, el token vencido, el servidor
caído. Entonces **no hay respuesta con cifras**, y lo que corresponde es decirlo.

| Qué falta | Qué corresponde |
|---|---|
| No se puede llamar a `build_financial_answer_context` | Una abstención: qué herramienta falta y qué hay que hacer para reconectarla. Sin cifras. |
| Hay contexto de esta conversación pero no se puede verificar | Respuesta en el chat, nunca un documento, declarando que la comprobación no corrió. |

**No sustituyas la fuente.** Ni archivos en disco, ni memoria, ni conocimiento general, ni una
búsqueda. Aunque las cifras salgan correctas, ese camino no es reproducible —existe sólo donde
está el repositorio de origen, y quien consulta no lo tiene— y produce el modo de falla que
esta doctrina ya nombra como el más difícil de detectar: una cifra correcta con procedencia más
débil de lo que aparenta, sin nada en el texto que lo delate.

> **El error que originó esta regla.** Con el servicio desconectado, una lectura de la UFRO se
> construyó leyendo el snapshot en disco. El sello dijo «Sin verificar» en rojo, que era la
> conducta correcta, y aun así el documento salió entero con once cifras sin comprobar y con
> la decisión de confiar traspasada a un lector que no tenía con qué tomarla.

El renderizador ya no compone un informe que cite montos sin `verificacion`: se niega y dice
cuáles encontró. Un documento sin cifras —una abstención— sí se compone, y su sello lo declara.

## 9 · Antes de entregar

- ¿Se llamó a `verify_reported_figures` y no quedó ninguna cifra rechazada?
- ¿Cada afirmación material tiene su capa identificable y su fuente?
- ¿Toda cifra citada vino del contexto de esta consulta, y no de memoria?
- ¿Se revisó `abstain_if` del criterio?
- ¿Los quiebres que cruzan las series citadas están declarados **antes** de la cifra?
- ¿La respuesta lleva sus cuatro piezas: la cifra con su contexto, de dónde salió, cómo se llegó y qué no permite concluir?
- Si se produjo una página, ¿el texto del chat se sostiene sin ella?
- Si el ejercicio trae `source_mark`, ¿se declaró **antes** que cualquier cifra, y con el texto de esa misma planilla?
- ¿Cada quiebre advertido usó el verbo que su `procedencia` autoriza, sin atribuir a la institución lo que construyó la base?
- ¿Ningún verbo de comportamiento económico se aplica a una serie con quiebre?
- ¿Ninguna serie con quiebre aparece en un ranking o una mediana sin declararlo?
- ¿Los nulos aparecen como no divulgados, y los guiones impresos como ceros declarados?
- ¿Ninguna tabla marcó como ausente un ejercicio que el contexto sí traía?
- ¿Alguna cautela se afirmó sin evidencia que la sostenga?
- ¿Alguna atribución a un término de un cociente se hizo mirando sólo las puntas de su serie?
- ¿Cada indicador se enunció como pregunta antes que como número?
- ¿Cada término especializado se tradujo en su primera aparición?
- ¿El orden de las cifras sigue al orden de la pregunta?
- ¿Se declaró qué quedó fuera de la consulta, distinguiéndolo de lo que no tuvo hallazgos?
