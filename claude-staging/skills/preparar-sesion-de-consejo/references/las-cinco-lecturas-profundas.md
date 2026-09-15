# Las cinco lecturas que sólo el expediente permite

Este archivo se lee **sólo cuando la institución tiene expediente auditado** y la pregunta
necesita algo que la planilla no informa: caja, deuda financiera, activo fijo, capex o flujos.

Cada una de estas cinco lecturas fue una puerta propia del plugin. Se colapsaron aquí porque
nueve de diecisiete puertas servían al 22% de las universidades, y esa desproporción hacía
ilegible la portada. **Lo que no se colapsó son las trampas**: cada lectura tiene una forma
característica de salir mal con las cifras correctas, y ésa es la parte que costó encontrar.

---

## 1 · La holgura — la plata está en dos bolsillos y la caja es sólo uno

`cash` es el efectivo y sus equivalentes. `other_current_financial_assets` son inversiones de
corto plazo que no son caja pero se convierten en plata. **Las dos se reportan juntas, siempre,
en la misma frase.**

> La Universidad de La Frontera cerró 2024 con M$2.164.961 de caja y M$17.345.697 en otros
> activos financieros corrientes. Contra M$50.252.853 que vencen dentro del año, la caja sola
> cubre el **4,3%** y las dos partidas juntas el **38,8%**.

Nueve veces de diferencia. Citar la primera cifra sola no es incompleto: **es una afirmación
distinta**, y sugiere una estrechez que el estado de situación no respalda.

El error no es sólo hacia abajo. La PUCV pasa de 59,5% con la caja sola a **223,2%** con las dos
partidas: leída por la caja se ve del montón, y tiene más del doble de lo que vence en el año.
La regla protege las dos lecturas, y no depende de que la brecha sea grande —en la Universidad
de Chile va de 60,3% a 78,1%— porque el lector no puede saber de antemano en qué caso está.

El contexto trae ese contraste **ya resuelto** en `plan.contrasts`, con la brecha en `gap`. No lo
rearmes: el error que la regla previene no es olvidar la regla, es armar mal el contraste.

**Y lo que ninguna de las dos cifras dice: cuánto dura.** «¿Cuántos meses aguanta?» no se puede
responder, y conviene decirlo antes de que lo pregunten. `unrestricted_cash_months` vuelve nula
para todas las publicadas: necesita el gasto mensual de caja y el piso operativo, y ambas
evidencias son `privada_requerida`. Además `MISS-CASH-RESTRICTIONS` está `no_estructurada`: la
base no sabe qué parte de esa plata está comprometida con proyectos, convenios o garantías. Una
caja grande no es una caja libre, y esta lectura no puede distinguirlas. La pregunta de gobierno
que corresponde: **¿cuál es el piso mensual de caja libre y en qué escenario se vulnera?**

---

## 2 · El respaldo — el cociente mide contra un denominador que no paga deudas

Deuda financiera sobre patrimonio, al cierre de 2024, sobre las once con expediente entonces:

| | deuda fin. / patrimonio | deuda neta / flujo normalizado | activo fijo / patrimonio | cobertura con dos bolsillos |
|---|---:|---:|---:|---:|
| **UCN** | **0,053** | **5,38** | 101,5% | **31,6%** |
| PUCV | 0,057 | 0,00 | 54,3% | 223,2% |
| **UFRO** | **0,069** | no calculable | 98,0% | **38,8%** |
| UCH | 0,076 | no calculable | 89,5% | 78,1% |
| UTALCA | 0,080 | 0,00 | 89,4% | 251,5% |
| UCSC | 0,153 | 0,00 | 119,6% | 94,1% |
| UCT | 0,204 | 0,46 | 137,2% | 104,0% |
| UCM | 0,223 | 1,74 | 107,7% | 104,7% |
| **UMAG** | **0,298** | **6,98** | 152,9% | **35,3%** |
| **UDP** | **0,429** | **3,18** | 149,2% | **20,5%** |
| **UACH** | **0,755** | **20,54** | 164,4% | 55,7% |

Nueve de las once caen en la banda «objetivo», que el registro fija en 0,3.

**Se equivoca por arriba:** la UCN sale primera y la UFRO tercera, y son dos de las cuatro con
menos caja del grupo —31,6% y 38,8% de lo que vence en el año, contra una mediana de 78,1%—.
**Se equivoca por poco:** la UMAG queda dentro de la banda a dos milésimas del límite, y es la
segunda peor en deuda neta sobre flujo. **Y acierta abajo:** la UDP y la UACH quedan fuera, y son
las dos con la deuda más exigente.

El cociente no está roto: **mide contra un denominador que no paga deudas, y cuando ese
denominador es enorme deja de discriminar.** Nunca se cita solo.

**La segunda columna tiene su propia trampa, y es la mediana.**
`net_debt_to_normalized_ocf` divide la deuda neta por la **mediana** de tres años de flujo, en
pesos de 2024. La mediana evita que un año bueno aislado borre una deuda grande; el precio es que
un año malo aislado la infla.

> La UACH sale en 20,54 años, tres veces el siguiente peor. Su flujo de los tres últimos
> ejercicios fue **−M$1.504.300 (2022), M$3.976.105 (2023) y M$14.359.081 (2024)**. La mediana es
> la del medio. Con el flujo de 2024 solo, el mismo cociente daría menos de seis años.
>
> Las dos lecturas son ciertas y ninguna sola es honesta. **Cita el cociente con la serie de flujo
> a la vista** y di si la mediana está deprimida por un ejercicio concreto: venir saliendo de un
> año negativo no es lo mismo que llevar tres iguales.

La UFRO y la UCH salen **no calculable** porque su mediana no es positiva. Eso no es un hueco: es
que no hay flujo contra el cual medir la deuda, y así se dice.

**Y el patrimonio no es respaldo.** En siete de las once el activo fijo vale más que todo el
patrimonio: citarlo como garantía describe una capacidad que no existe.

---

## 3 · La operación — hay dos márgenes del mismo año

Esta base contiene **dos definiciones de ingreso de la operación**, y por lo tanto dos márgenes
para el mismo ejercicio: el de la planilla FECU, que traen `operating_margin_fecu` y las bandas;
y el de la serie analítica propia, que citan los claims del expediente.

En la UCT en 2024 dan **6,5% y 5,0%**. Ninguno está mal: son cocientes distintos.

**Cita el de la FECU** —es el que trae bandas, serie y posición— **y di que es el de la FECU, en
la misma frase.** Trae el analítico sólo si un claim lo cita o si preguntan por él, y entonces di
también que es otro.

Es el error más silencioso de toda la capa profunda: ambas cifras se verifican contra la base,
ninguna alerta salta, y el lector que compara con otra fuente encuentra una diferencia que nadie
explicó.

---

## 4 · La inversión — el activo fijo no mide la inversión

Es el error más caro de esta dimensión porque la cifra es enorme y parece la respuesta obvia.

> Las propiedades, planta y equipo de la Universidad de La Frontera pasaron de M$82.665.824 en
> 2020 a M$253.667.908 en 2022. En esos dos años invirtió **M$8.508.894**. La diferencia es
> revalorización, con su contrapartida en «Otras reservas», y la base la declara.

La inversión del año se lee del estado de flujos, **nunca de la variación del balance**. Cuando el
contexto trae una regla de lectura de clase `revalorizacion`, dice exactamente esto: se informa el
capex, no el salto del activo. Cúmplela en silencio, sin explicar la regla.

---

## 5 · La dependencia — dos magnitudes con el mismo nombre, y una mediana que no informa

**La gratuidad devengada no es lo mismo que los cobros por gratuidad.** La primera es el ingreso
reconocido en el ejercicio; la segunda, la plata que llegó. No se suman, no se comparan entre sí y
no se usan indistintamente. Es el error más frecuente de esta dimensión, precisamente porque las
dos cifras existen y se parecen.

> En la UCT la gratuidad devengada equivale al **51,6%** de los ingresos de la operación
> —M$32.051.660 sobre M$62.078.092—, contra una mediana de 36,8% entre las nueve que la publican,
> que van de 14,1% a 57,1%.

La dispersión importa tanto como el nivel: la más grande del grupo depende un 14,1% porque su
ingreso viene además de postgrado e investigación, mientras las regionales medianas pasan del 50%.
**La dependencia crece cuando el ingreso es más concentrado** — observación sobre el modelo, no
juicio sobre la institución.

**Y hay un indicador cuya mediana no informa.** Las provisiones sobre ingresos al cierre de 2024:

| | |
|---|---|
| Cero o casi | Universidad de Chile 0%, Universidad de La Frontera 0%, Universidad de Talca 0,1% |
| Entre 4,7% y 24,2% | las otras cinco |

No es un continuo con valores atípicos: **son dos poblaciones.** Las tres primeras son estatales y
las otras cinco privadas del Consejo de Rectores, y el régimen de personal no es el mismo. La base
no trae esa variable —`institution_type` dice «Universidades Cruch» para todas—, de modo que la
mediana de 8,7% promedia poblaciones distintas y no describe a ninguna.

**No cites este indicador contra la mediana ni contra el rango.** Repórtalo por institución, y si
comparas, compara con instituciones de la misma naturaleza y dilo en la misma frase. Es la
excepción a la regla general de acompañar toda cifra con algo con qué compararla: aquí la
comparación disponible engaña más de lo que ayuda.

---

## Lo que estas cinco comparten

Ninguna de las cinco trampas es un error de aritmética. En las cinco, **la cifra es correcta y la
frase es falsa**: un bolsillo de dos, un cociente contra un denominador que no paga, uno de dos
márgenes homónimos, una revalorización leída como inversión, dos magnitudes con el mismo nombre.

Por eso la comprobación previa a la entrega no puede ser «¿verifican las cifras?». Verifican todas.
