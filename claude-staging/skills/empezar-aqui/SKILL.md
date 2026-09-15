---
description: Orienta a quien acaba de instalar el servicio o no sabe qué preguntarle — «¿qué puedes hacer?», «¿por dónde empiezo?», «¿qué universidades tienes?», «¿qué preguntas responde esto?», «ayuda», «no sé qué pedirte». Presenta lo que el servicio responde en el idioma del consejero, con la cobertura consultada en vivo y la frontera dicha desde el principio.
---

# Empezar aquí

Alguien instaló el servicio y no sabe qué pedirle, o lo tiene hace tiempo y no sabe hasta dónde
llega. Esta puerta lo orienta.

**Antes de responder, consulta la cobertura.** Llama a `list_institutions` y a
`list_fecu_institutions` y usa lo que devuelvan. **Nunca escribas de memoria cuántas
universidades hay ni cuáles son**: la base crece, y una bienvenida que envejece mal es peor que
no tenerla. Si una de las dos llamadas falla, dilo y no la sustituyas por una cifra recordada.

De `list_fecu_institutions` toma **el recuento y la cobertura de años, no la lista**: enumerar
cincuenta y cinco nombres en una bienvenida la vuelve ilegible. Ése es el universo y es lo que
importa decir primero: **la planilla las cubre a todas**.

De `list_institutions` toma el recuento, no los nombres. La docena con expediente completo no es
la portada del servicio: es una profundidad extra que unas pocas tienen, y anunciarla por delante
hace que la mayoría de las preguntas empiecen con una decepción.

> **Si las herramientas no responden, ese es el tema y no hay que disimularlo.** El servicio
> vive en un conector que se autoriza **por superficie**: tenerlo habilitado en un cliente no lo
> habilita en otro, y los plugins activos en uno no son los del otro. Es la confusión más
> frecuente al empezar.
>
> Cuando la llamada falle, di las tres cosas en este orden: que el servicio no está conectado
> **en esta superficie**, que los datos y los skills son los mismos una vez conectado, y que la
> autorización se hace desde los ajustes de conectores del cliente que se esté usando.
>
> Y no ofrezcas la orientación igual con cifras recordadas: sin herramientas, lo único honesto
> es explicar qué falta. Una bienvenida que inventa su propia cobertura es peor que una que
> pide conectar.

---

## 1 · Qué decir primero

Una frase de qué es esto, y enseguida el alcance. El alcance no es la letra chica: es lo primero
que un consejero necesita para saber si le sirve.

> Esto lee los estados financieros publicados de las universidades chilenas y responde con la
> fuente a la vista. Cubre **todo el sistema universitario** con el resumen que publica la
> Superintendencia, y de unas pocas instituciones tiene además el expediente auditado completo.

Después las cifras que devolvieron las herramientas, y qué sostiene cada capa:

| | Alcance | Qué trae |
|---|---|---|
| **Resumen sectorial** | todas | la cascada del ingreso al resultado, el balance completo, la composición del ingreso en seis categorías, la estructura de costos y la nómina abierta por estamento |
| **Expediente completo** | unas pocas | además: caja, deuda financiera, arrendamientos, activo fijo, inversión, flujo de la operación, depreciación y las notas |

Y la frase que evita el malentendido más caro, dicha como límite del resumen y no como defecto:
**la planilla no informa caja, deuda financiera, activo fijo, capex ni flujos.** Con ella se puede
saber si el resultado alcanzó; no si alcanzó la plata.

**No presentes la docena como una lista de privilegiadas.** Si la persona nombra una universidad
que la tiene, la profundidad aparece sola cuando su pregunta la necesite. Si nombra una que no,
no debe enterarse de que existía un club mejor.

---

## 2 · Qué puede preguntar, en su idioma

Preséntalo como preguntas, **no como nombres de herramientas**. A un consejero no le sirve
saber que existe algo llamado `describe_fecu_institution`; le sirve saber que puede preguntar
si a su universidad le alcanza para pagar.

**Sobre cualquier universidad del sistema** — éstas son la portada, y valen para todas:

- ¿Cómo le fue el año pasado? ¿Ganó o perdió, y de dónde vino ese resultado?
- ¿En qué se le va la plata? ¿Cuánto se va en sueldos?
- ¿Cómo está parada? ¿Sus activos corrientes cubren lo que vence dentro del año?
- ¿De qué vive? ¿Cuánto recibe del Estado?
- ¿Dónde queda frente a las demás de su tipo?

**Comparando universidades entre sí**

- ¿Cómo se comparan la Universidad de Chile y la Católica en ingresos y en gastos?
- ¿Cuáles son las diez con más ingresos?
- ¿Cuáles dependen menos de los aranceles?

**Sobre el sistema entero**

- ¿Se está deteriorando el sector, o le pasa a algunas?
- ¿Cómo se reparte esto entre las universidades del Consejo de Rectores y las privadas?
- ¿Cómo se comparan en patrimonio? ¿Y en activos frente a pasivos?

**Y si la universidad tiene expediente completo**, además —pero esto **no se ofrece por delante**,
sólo cuando la persona nombre una que lo tenga o su pregunta lo pida:

- ¿Cuánta plata disponible tiene y cuánto vence dentro del año?
- ¿Qué invirtió, con qué lo pagó, y alcanza para reponer lo que se consume?
- Una minuta para un punto de tabla, con trazabilidad y preguntas para la mesa.
- ¿Es cierto lo que dijeron en la sesión pasada?

### Que escriba el nombre como lo dice

No le pidas la forma oficial. El servicio resuelve la sigla de uso corriente —«PUC», «UdeC»,
«USM», «UCHILE», «UC»—, el nombre parcial —«Universidad Autónoma» encuentra a la Autónoma de
Chile— y el código SIES. Cuando lo que escriba corresponda a varias, la respuesta **las nombra
para que elija**; no adivines por él.

Elige tres o cuatro según lo que la persona haya dicho, y **nómbralas con una institución
concreta**. Si ya nombró la suya, úsala — esté o no entre las que tienen expediente. Si no nombró
ninguna, toma una de `list_fecu_institutions`, que son todas. «¿Cómo le fue a la Universidad de
Talca el año pasado?» invita a probar; «puedes preguntar por una universidad» no.

---

## 3 · Qué no responde, dicho al principio

No es una advertencia de cierre: es parte de la orientación, porque ahorra la decepción de la
tercera pregunta.

- **No proyecta.** Nada de «si la matrícula cae 10%, el margen cae X»: los estados publicados no
  traen la separación entre costos fijos y variables.
- **No dice si un plan es financiable.** El costo pendiente por proyecto y las fuentes
  comprometidas están en el plan maestro y en los contratos, que no son públicos.
- **No dice cuántos meses dura la caja.** Necesita el gasto mensual, que tampoco es público.
- **No califica.** No dirá que una universidad está sana o en riesgo. Describe qué puede y qué
  no puede hacer con lo que tiene.
- **No explica causas.** Los estados dicen qué pasó, casi nunca por qué. El porqué se convierte
  en pregunta para la mesa.

---

## 4 · Cómo llegan las respuestas

Dilo en una línea: las preguntas cortas se responden en el chat; lo que va a circular se
entrega como documento con su sello de verificación, y **toda cifra material se comprueba
contra la base antes de salir**.

Si la persona pregunta cómo sabe que puede confiar, esa es la respuesta: cada cifra se declara,
se comprueba y se cita con su documento y su página.

---

**Qué cambió y en qué versión corre** → `ver_cambios()`. Antes de su línea base no hay registro: dilo así.

## 5 · Cierra ofreciendo la primera pregunta

Una bienvenida que termina en «pregúntame lo que quieras» no ayuda. Termina proponiendo **una**
pregunta concreta, con una institución concreta, y quédate esperando.

Si la persona ya nombró su universidad, propón la de ella —**cualquiera de las del sistema
sirve**, no sólo las que tienen expediente—. Si no nombró ninguna, toma una de
`list_fecu_institutions` y ofrece cambiarla.

---

## 6 · Antes de entregar

- ¿La cobertura salió de las herramientas y no de la memoria?
- ¿Se presentó el resumen sectorial como el alcance —todas— y el expediente como el extra?
- ¿Las preguntas propuestas valen para la universidad que la persona nombró, tenga expediente o no?
- ¿Se evitó anunciar la docena como un club, dejando a la mayoría con la sensación de estar fuera?
- Si el conector no respondía, ¿se dijo que la autorización es **por superficie** y no se completó la respuesta con cifras recordadas?
- ¿Las dos capas quedaron distinguidas antes de la primera propuesta de pregunta?
- ¿Se habló en preguntas y no en nombres de skills?
- ¿Se dijo qué no responde, y no sólo qué responde?
- ¿La respuesta termina con una pregunta concreta y no con una invitación vaga?
- ¿Cabe en una pantalla? Una orientación larga se salta entera.
