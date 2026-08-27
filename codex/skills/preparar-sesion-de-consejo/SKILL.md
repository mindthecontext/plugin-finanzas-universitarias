---
name: preparar-sesion-de-consejo
description: Prepara antecedentes financieros universitarios como entregable para un órgano de gobierno — punto de tabla, minuta o informe al consejo. Usar cuando el destinatario es un cuerpo colegiado que debe decidir o tomar conocimiento y hace falta un documento que se sostenga ante preguntas incómodas. También cuando se pida "un resumen para el consejo", "antecedentes para la sesión" o "una minuta". Sirve a las 55 universidades con la planilla sectorial y asciende al expediente auditado sólo en las que lo tienen. Para entender una universidad sin producir un documento, usar entender-una-universidad.
---

# Preparar antecedentes para una sesión de gobierno

Este skill produce un **entregable**: un documento que otros leerán antes de una sesión. Si lo
que hace falta es comprender —un consejero que quiere entender la situación de su
universidad—, el skill es `entender-una-universidad`, que produce la lectura sin el aparato de
un informe.

**Antes de redactar, lee `references/doctrina-de-analisis.md`; y si la respuesta va a ser un documento, lee también `references/contrato-de-informe.md` y produce el spec en vez de escribir HTML.** Trae las cuatro capas, el
tratamiento de los quiebres, el encuadre de cifras, el lenguaje llano y lo que nunca va en una
respuesta. Este archivo sólo aporta lo propio de un entregable de gobierno.

Un consejero no necesita saber más finanzas: necesita saber **qué está en juego, qué está
establecido, qué no lo está y qué debería preguntar**. La diferencia entre un buen informe y
uno peligroso casi nunca está en las cifras: está en el encuadre.

## Antes de escribir

1. **Identifica la pregunta real de gobierno.** Si el usuario pidió «un análisis de la UCT»,
   pregunta qué decisión o qué punto de tabla la motiva: no es lo mismo tomar conocimiento que
   aprobar un endeudamiento. Sin esto, el informe responde algo que nadie preguntó.
2. **Averigua con qué capa vas a escribir**, porque decide qué puedes prometer:

   ```
   describe_fecu_institution(institution: <la universidad>)
   ```

   `deep_dossier.available` manda. Si es `false` —el caso de 43 de las 55— el informe se escribe
   con la planilla, y es un informe legítimo: resultado, solidez, costos, sustento, cada cifra con
   su posición entre pares. Lo que **no** puede llevar es caja, deuda financiera, activo fijo,
   capex ni flujos, y eso se dice como límite de la fuente en la sección 5, no como disculpa.

   Si es `true`, puedes además ascender. **Lee entonces `references/las-cinco-lecturas-profundas.md`**:
   trae las cinco lecturas que sólo el expediente permite y —lo que importa— la forma
   característica que tiene cada una de salir mal con las cifras correctas.

3. Construye la lectura con `entender-una-universidad`, que ya bifurca por capa.
4. Confirma quién es el destinatario y qué puede hacer con la respuesta. Un consejo que toma
   conocimiento necesita otra cosa que uno que vota.

## Estructura del entregable

Plantilla y ejemplo trabajado en `references/plantilla-y-ejemplo.md`.

1. **Qué se pregunta** — una línea, en los términos del punto de tabla.
2. **Respuesta en una frase** — si la pregunta admite respuesta. Si no, la abstención va aquí.
3. **Lo que está establecido** — hechos con su fuente, cálculos con su fórmula.
4. **Cómo llegó hasta aquí** — trayectoria, con los quiebres declarados antes de la tendencia.
5. **Lo que estos antecedentes no permiten concluir** — explícito, nunca una nota al pie.
6. **Preguntas para la mesa** — tres a cinco, accionables, dirigidas a quien puede
   responderlas.
7. **Trazabilidad** — de dónde sale cada cifra material.

Cuando la política de respuesta es `no_respondible`, el entregable **no se acorta, se
reordena**: qué se pregunta, por qué estos antecedentes no la responden, qué documento la
respondería y quién lo tiene, qué sí se puede afirmar mientras tanto, y las preguntas para la
mesa. Una abstención bien hecha le dice al consejo qué pedir antes de la próxima sesión.

## El entregable

Una minuta **siempre** se compone: se produce el JSON del informe y el renderizador arma la
página. Nunca escribas HTML. El formato está en `references/contrato-de-informe.md`.

```bash
python3 assets/construir_informe.py --entrada informe.json --salida informe.html
```

Y **entrega el archivo**. Un antecedente que el consejero no puede abrir no protege ninguna
decisión.

Las secciones de la estructura de arriba corresponden a los `tipo` del contrato:
`pregunta`, `respuesta_una_frase`, `establecido`, `trayectoria`, `no_concluible`,
`preguntas`, `trazabilidad`. Cuando la respuesta sea una abstención, declara además el bloque
`abstencion` con las tres referencias; el renderizador se niega a componer si falta alguna.

Una figura acompaña, nunca reemplaza: el texto debe sostenerse si alguien imprime el informe
sin gráficos.

## Extensión

El entregable se lee **antes** de la sesión, no durante. Apunta a que un consejero lo recorra
en noventa segundos y sepa qué está en juego.

- La respuesta en una frase es **una frase**. Si necesitas dos, la pregunta estaba mal acotada:
  vuelve al paso 1.
- Las secciones 3 y 4 no pasan de cinco párrafos entre ambas.
- Lo que no se puede concluir: cinco puntos como máximo, los más decisivos.
- Todo lo que sobre va a la trazabilidad o a un anexo, no al cuerpo.

Un informe largo no es más riguroso: es menos leído, y un antecedente que no se lee no protege
ninguna decisión.

## Antes de entregar

Además de la lista de la doctrina:

- ¿La pregunta de gobierno quedó identificada, y el informe la responde a ella?
- ¿La respuesta en una frase es realmente una frase?
- ¿La sección de lo que no se puede concluir existe y no está vacía?
- ¿Las preguntas para la mesa son respondibles por alguien concreto?
- ¿Se sostiene el texto sin las figuras?
