// Recetas de visualización, una por forma declarada en la receta de respuesta.
//
// Cada forma trae sus reglas pegadas y no son negociables desde el spec: base en cero,
// un solo eje, y las marcas de quiebre dibujadas donde la serie se corta. El propósito
// es que dos informes distintos se vean como del mismo producto y que ninguna serie
// con un cambio de presentación se dibuje como si fuera continua.
//
// Las series se distinguen por color **y** por forma de marca: el color solo excluye a
// quien no lo percibe.

const PALETA = ["--s1", "--s2", "--s3", "--s4", "--s5"];
const SIMBOLOS = ["circle", "square", "triangle", "diamond", "cross"];

const tono = nombre => getComputedStyle(document.documentElement).getPropertyValue(nombre).trim();
const tinta = () => tono("--ink-2");
const regla = () => tono("--rule");

function puntos(spec) {
  return spec.series.flatMap((serie, indice) =>
    (serie.points || [])
      .filter(punto => punto.value !== null && punto.value !== undefined)
      .map(punto => ({
        ejercicio: punto.exercise,
        valor: punto.value,
        serie: serie.label || serie.metric_id,
        orden: indice,
      })),
  );
}

/**
 * Marcas de quiebre: una línea vertical con su etiqueta en el ejercicio afectado.
 *
 * Varios quiebres pueden caer en el mismo ejercicio —una institución que cambió a la vez
 * la presentación del flujo y la del activo fijo—. Se dibuja una sola marca por año: dos
 * etiquetas superpuestas se leen como un borrón.
 */
function marcasDeQuiebre(spec, Plot) {
  const porEjercicio = new Map();
  for (const anotacion of spec.annotations || []) {
    const lista = porEjercicio.get(anotacion.exercise) || [];
    lista.push(anotacion);
    porEjercicio.set(anotacion.exercise, lista);
  }
  const marcas = [...porEjercicio.entries()].map(([ejercicio, lista]) => ({
    ejercicio,
    etiqueta: lista.length > 1 ? `cambio de presentación (${lista.length})` : "cambio de presentación",
  }));
  return [
    Plot.ruleX(marcas, { x: "ejercicio", stroke: tono("--alert"), strokeWidth: 1.4, strokeDasharray: "4 3" }),
    Plot.text(marcas, {
      x: "ejercicio", text: "etiqueta", frameAnchor: "top", dy: -8, fontSize: 10,
      fill: tono("--alert"), textAnchor: "middle",
    }),
  ];
}

/**
 * Línea de referencia declarada por la receta.
 *
 * Un umbral con significado —activos corrientes igualando a los pasivos del año— ayuda a
 * leer la serie. Se dibuja sólo si la receta lo declara: inventar una referencia es
 * sugerir un umbral normativo que la metodología no sostiene.
 */
function lineaDeReferencia(spec, Plot) {
  const referencia = spec.reference;
  if (!referencia || typeof referencia.value !== "number") return [];
  return [
    Plot.ruleY([referencia.value], { stroke: tono("--rule-2"), strokeWidth: 1.5, strokeDasharray: "5 4" }),
    Plot.text([referencia], {
      y: "value", text: () => referencia.label || "", frameAnchor: "right", dx: -4, dy: -7,
      fontSize: 10, fill: tono("--ink-3"), textAnchor: "end",
    }),
  ];
}

/** Formato de eje: nunca notación científica en un documento que lee un consejo. */
function formatoEje(spec) {
  if (spec.unit_hint === "razon") return valor => `${Math.round(valor * 100)}%`;
  if (spec.unit_hint === "mclp") return montoCorto;
  return valor => Math.round(valor).toLocaleString("es-CL");
}

/**
 * Un monto de la planilla, legible en un eje.
 *
 * La fuente viene en M$ —miles de pesos— y un eje con «461.248.371» no se lee. Se convierte a
 * pesos y se acorta, porque la magnitud es lo que informa y los dígitos finales no.
 */
function montoCorto(valor) {
  const pesos = valor * 1000;
  const abs = Math.abs(pesos);
  const corto = (x, u, d) => `$${x.toLocaleString("es-CL", { minimumFractionDigits: d, maximumFractionDigits: d })} ${u}`;
  if (abs >= 1e12) return corto(pesos / 1e12, "bill.", 1);
  if (abs >= 1e9) return corto(pesos / 1e9, "mil M", 0);
  if (abs >= 1e6) return corto(pesos / 1e6, "M", 0);
  return `$${Math.round(pesos).toLocaleString("es-CL")}`;
}

function serieTemporal(spec, Plot) {
  const datos = puntos(spec);
  // Una marca por ejercicio observado. Sin esto la escala continua inventa medios años
  // —2019,5— que no corresponden a ninguna observación; y fijar los ticks a los años
  // efectivamente presentes deja a la vista un hueco cuando falta un ejercicio.
  const ejercicios = [...new Set(datos.map(dato => dato.ejercicio))].sort((a, b) => a - b);
  const colores = spec.series.map((_, indice) => tono(PALETA[indice % PALETA.length]));
  const simbolos = spec.series.map((_, indice) => SIMBOLOS[indice % SIMBOLOS.length]);
  return Plot.plot({
    width: 780, height: 300, marginLeft: 62, marginBottom: 38, marginTop: 34, marginRight: 20,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, ticks: ejercicios, tickFormat: valor => String(valor), inset: 18, grid: false },
    // Base en cero: una serie de cobertura recortada por abajo exagera la pendiente.
    y: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec), nice: true },
    // Con una sola serie la leyenda repite el título: sobra.
    color: { domain: spec.series.map(s => s.label || s.metric_id), range: colores, legend: spec.series.length > 1 },
    symbol: { domain: spec.series.map(s => s.label || s.metric_id), range: simbolos, legend: false },
    marks: [
      Plot.gridY({ stroke: regla(), strokeOpacity: 1 }),
      Plot.ruleY([0], { stroke: tinta(), strokeWidth: 1.2 }),
      ...lineaDeReferencia(spec, Plot),
      ...marcasDeQuiebre(spec, Plot),
      Plot.line(datos, { x: "ejercicio", y: "valor", stroke: "serie", strokeWidth: 2.2, curve: "linear" }),
      Plot.dot(datos, { x: "ejercicio", y: "valor", fill: "serie", symbol: "serie", r: 4 }),
    ],
  });
}

function comparacionPares(spec, Plot) {
  const datos = puntos(spec);
  return Plot.plot({
    width: 780, height: Math.max(180, 34 * datos.length), marginLeft: 128, marginRight: 34, marginTop: 18,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec) },
    y: { label: null },
    marks: [
      Plot.gridX({ stroke: regla(), strokeOpacity: 1 }),
      Plot.barX(datos, {
        x: "valor", y: "serie", sort: { y: "x", reverse: true },
        fill: dato => (dato.destacada ? tono("--s3") : tono("--s1")),
      }),
      Plot.ruleX([0], { stroke: tinta(), strokeWidth: 1.2 }),
    ],
  });
}

/**
 * Balance en dos columnas: lo que tiene contra de quién es.
 *
 * Las dos barras miden lo mismo por definición contable —activos = pasivos + patrimonio— y
 * dibujarlas a la misma altura es el punto: lo que informa no es el total sino **cómo se
 * reparte la de la derecha**. Un balance en dos columnas separadas, con escalas independientes,
 * pierde exactamente eso.
 *
 * Se apila de arriba abajo en el orden declarado, de lo más exigible a lo más propio: primero
 * lo corriente, después lo de largo plazo, y el patrimonio al final.
 */
function balanceApilado(spec, Plot) {
  const datos = (spec.stacks || []).flatMap((columna, ci) =>
    (columna.parts || [])
      .filter(parte => parte.value !== null && parte.value !== undefined)
      .map((parte, pi) => ({
        columna: columna.label,
        parte: parte.label,
        valor: Math.abs(parte.value),
        orden: ci * 100 + pi,
      })),
  );
  if (datos.length === 0) throw new Error("el balance no trae partidas con valor");
  const partes = [...new Map(datos.map(d => [d.parte, d.orden])).entries()]
    .sort((a, b) => a[1] - b[1]).map(([nombre]) => nombre);
  const colores = partes.map((_, i) => tono(PALETA[i % PALETA.length]));
  return Plot.plot({
    width: 780, height: 330, marginLeft: 92, marginBottom: 42, marginTop: 22, marginRight: 20,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, domain: (spec.stacks || []).map(c => c.label) },
    y: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec), nice: true },
    color: { domain: partes, range: colores, legend: true },
    marks: [
      Plot.gridY({ stroke: regla(), strokeOpacity: 1 }),
      Plot.barY(datos, {
        x: "columna", y: "valor", fill: "parte",
        order: partes, sort: { color: null },
        title: dato => `${dato.parte}: ${montoCorto(dato.valor)}`,
      }),
      Plot.ruleY([0], { stroke: tinta(), strokeWidth: 1.2 }),
    ],
  });
}

/**
 * Reparto de un total declarado en sus partes.
 *
 * Barras horizontales ordenadas de mayor a menor, con la participación a la vista. **No es un
 * gráfico de torta a propósito**: comparar ángulos es peor que comparar longitudes, y aquí el
 * lector necesita ver cuánto más pesa una categoría que otra, no adivinarlo.
 */
function composicion(spec, Plot) {
  const total = (spec.parts || []).reduce((suma, parte) => suma + Math.abs(parte.value || 0), 0);
  if (!total) throw new Error("la composición no suma nada que repartir");
  const datos = (spec.parts || [])
    .filter(parte => parte.value !== null && parte.value !== undefined)
    .map(parte => ({ parte: parte.label, valor: Math.abs(parte.value), share: Math.abs(parte.value) / total }))
    .sort((a, b) => b.valor - a.valor);
  return Plot.plot({
    width: 780, height: Math.max(170, 36 * datos.length + 40), marginLeft: 210, marginRight: 86, marginTop: 16,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec) },
    y: { label: null, domain: datos.map(d => d.parte) },
    marks: [
      Plot.gridX({ stroke: regla(), strokeOpacity: 1 }),
      Plot.barX(datos, { x: "valor", y: "parte", fill: tono("--s1"), title: d => montoCorto(d.valor) }),
      Plot.text(datos, {
        x: "valor", y: "parte", text: d => `${(d.share * 100).toFixed(1).replace(".", ",")}%`,
        textAnchor: "start", dx: 7, fontSize: 11, fill: tinta(),
      }),
      Plot.ruleX([0], { stroke: tinta(), strokeWidth: 1.2 }),
    ],
  });
}

/**
 * Cascada: del ingreso al resultado, paso a paso.
 *
 * Los subtotales arrancan en cero y los movimientos se apilan sobre el acumulado, que es lo
 * que hace visible **la distancia entre el resultado operacional y el del ejercicio** — el
 * hallazgo de esta lectura casi nunca es la última cifra, sino cuánto la separa de la primera.
 */
function cascada(spec, Plot) {
  let acumulado = 0;
  const datos = (spec.steps || []).map((paso, indice) => {
    const valor = paso.value || 0;
    const esTotal = paso.kind === "base" || paso.kind === "total" || paso.kind === "sub";
    const desde = esTotal ? 0 : acumulado;
    const hasta = esTotal ? valor : acumulado + valor;
    acumulado = esTotal ? valor : hasta;
    return {
      paso: paso.label, orden: indice, desde: Math.min(desde, hasta), hasta: Math.max(desde, hasta),
      valor, clase: esTotal ? (paso.kind === "base" ? "base" : "subtotal") : (valor >= 0 ? "suma" : "resta"),
    };
  });
  if (datos.length === 0) throw new Error("la cascada no trae pasos");
  const color = { base: tono("--rule"), subtotal: tono("--s1"), suma: tono("--s2"), resta: tono("--alert") };
  return Plot.plot({
    width: 780, height: Math.max(200, 42 * datos.length + 40), marginLeft: 210, marginRight: 96, marginTop: 16,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec) },
    y: { label: null, domain: datos.map(d => d.paso) },
    marks: [
      Plot.gridX({ stroke: regla(), strokeOpacity: 1 }),
      Plot.barX(datos, { x1: "desde", x2: "hasta", y: "paso", fill: d => color[d.clase] }),
      Plot.text(datos, {
        x: "hasta", y: "paso", text: d => `${d.valor < 0 ? "−" : ""}${montoCorto(Math.abs(d.valor))}`,
        textAnchor: "start", dx: 7, fontSize: 11, fill: tinta(),
      }),
      Plot.ruleX([0], { stroke: tinta(), strokeWidth: 1.2 }),
    ],
  });
}

/**
 * Orden por una medida, con el corte a la vista.
 *
 * Un orden es la manera más fácil de decir algo falso con cifras correctas, así que el pie
 * declara sobre cuántas se ordenó y cuántas quedaron fuera. La figura dibuja sólo las que
 * caben; **el resto no desaparece, se cuenta**.
 */
function orden(spec, Plot) {
  const datos = (spec.items || [])
    .filter(item => item.value !== null && item.value !== undefined)
    .map(item => ({ nombre: item.label, valor: item.value, destacada: Boolean(item.highlight) }));
  if (datos.length === 0) throw new Error("el orden no trae filas con valor");
  return Plot.plot({
    width: 780, height: Math.max(200, 30 * datos.length + 46), marginLeft: 250, marginRight: 92, marginTop: 16,
    style: { background: "transparent", color: tinta(), fontSize: "11px" },
    x: { label: null, zero: true, grid: true, tickFormat: formatoEje(spec) },
    y: { label: null, domain: datos.map(d => d.nombre) },
    marks: [
      Plot.gridX({ stroke: regla(), strokeOpacity: 1 }),
      Plot.barX(datos, { x: "valor", y: "nombre", fill: d => (d.destacada ? tono("--s3") : tono("--s1")) }),
      Plot.text(datos, {
        x: "valor", y: "nombre",
        text: d => (spec.unit_hint === "razon"
          ? `${(d.valor * 100).toFixed(1).replace(".", ",")}%`
          : montoCorto(d.valor)),
        textAnchor: "start", dx: 7, fontSize: 11, fill: tinta(),
      }),
      Plot.ruleX([0], { stroke: tinta(), strokeWidth: 1.2 }),
    ],
  });
}

const FORMAS = {
  serie_temporal: serieTemporal,
  comparacion_pares: comparacionPares,
  balance_apilado: balanceApilado,
  composicion,
  cascada,
  orden,
};

/**
 * Dibuja una figura, o se niega.
 *
 * La negativa es la conducta correcta, no un error que sortear: un quiebre en alcance
 * sin su marca produciría un gráfico que muestra como continua una serie que no lo es.
 */
function dibujar(spec) {
  const Plot = window.Plot;
  const enAlcance = spec.breaks_in_scope || [];
  const marcados = (spec.annotations || []).map(anotacion => anotacion.break_id);
  const faltantes = enAlcance.filter(id => !marcados.includes(id));
  if (faltantes.length > 0) {
    throw new Error(`hay quiebres en alcance sin marca (${faltantes.join(", ")}); se entrega la tabla en su lugar`);
  }
  const receta = FORMAS[spec.form];
  if (!receta) throw new Error(`la forma «${spec.form}» todavía no está implementada`);
  return escalable(receta(spec, Plot));
}

/**
 * Hace el gráfico responsivo sin deformarlo.
 *
 * Plot emite `width` y `height` pero no `viewBox`, y sin viewBox un `height:auto` del CSS
 * resuelve a cero: el gráfico existe en el DOM y ocupa cero píxeles. Derivar el viewBox de
 * los atributos y soltar el ancho fijo lo deja escalar conservando la proporción.
 */
function escalable(nodo) {
  const graficos = nodo.tagName === "svg" ? [nodo] : nodo.querySelectorAll("svg");
  for (const svg of graficos) {
    const ancho = Number(svg.getAttribute("width"));
    const alto = Number(svg.getAttribute("height"));
    if (!ancho || !alto || svg.getAttribute("viewBox")) continue;
    // Las muestras de color de la leyenda también son SVG, de quince píxeles: escalarlas
    // al ancho del contenedor las convierte en bloques enormes.
    if (ancho < 80 || svg.closest("[class*=swatch]")) continue;
    svg.setAttribute("viewBox", `0 0 ${ancho} ${alto}`);
    svg.setAttribute("preserveAspectRatio", "xMinYMin meet");
    svg.removeAttribute("width");
    svg.setAttribute("height", String(alto));
    svg.style.width = "100%";
    svg.style.height = "auto";
  }
  return nodo;
}
