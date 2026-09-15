#!/usr/bin/env python3
"""Compone un informe financiero desde su especificación.

El modelo es dueño de la prosa; este script es dueño de la forma. Recibe un spec con el
texto, las secciones, las figuras declaradas por la receta, las cifras declaradas y el
resultado de `verify_reported_figures`, y produce una página autocontenida.

Tres reglas que el compositor hace cumplir, y que existen porque su incumplimiento no se
ve a simple vista:

1. **El sello nunca falta.** Sin verificación el encabezado dice «sin verificar». Una
   ausencia silenciosa haría que un informe sin comprobar se pareciera a uno comprobado.
2. **Una abstención declara dónde cumple cada obligación.** No se exige un orden fijo de
   secciones —una minuta con la estructura estándar puede abstenerse bien—, se exige que
   el spec apunte a la sección donde está la razón, el documento que respondería y lo que
   sí se puede afirmar.
3. **Una figura con un quiebre en alcance sin marca no se dibuja.** La negativa viaja
   hasta la página como una nota visible, no como un hueco.

Uso:

    python3 construir_informe.py --entrada informe.json --salida informe.html
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path


ASSETS = Path(__file__).resolve().parent
SECCIONES_CONOCIDAS = {
    "pregunta", "respuesta_una_frase", "establecido", "trayectoria",
    "no_concluible", "preguntas", "trazabilidad", "bloque", "nota",
}
OBLIGACIONES_ABSTENCION = ("razon_en", "documento_que_responderia_en", "que_si_se_puede_afirmar_en")


def escapar(texto: object) -> str:
    return html.escape(str(texto if texto is not None else ""), quote=False)


def componer_cifras(texto: str, escritas: dict[str, str], usadas: set[str] | None = None) -> str:
    """Compone con numerales tabulares cada cifra declarada que aparezca en el texto.

    Coincidencia exacta contra `as_written`, no interpretación de la prosa. El efecto
    buscado va más allá de lo tipográfico: una cifra no declarada no se compone y se ve
    distinta al resto, de modo que declarar completo tiene consecuencia visible.
    """
    resultado = escapar(texto)
    # De la más larga a la más corta: «M$19.510.658» antes que «658».
    for escrita in sorted((e for e in escritas if e), key=len, reverse=True):
        marca = escapar(escrita)
        if not marca or marca not in resultado:
            continue
        if usadas is not None:
            usadas.add(escrita)
        estado = escritas[escrita]
        clase = "f" if estado == "verificada" else "f nv"
        titulo = "" if estado == "verificada" else ' title="Esta cifra no pudo comprobarse contra la base."'
        resultado = resultado.replace(marca, f'<span class="{clase}"{titulo}>{marca}</span>')
    return resultado


MESES = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")


def fecha_legible(version: str | None) -> str | None:
    """«financial-knowledge-2026-08-15-51269cb…» → «15 de agosto de 2026».

    El identificador del snapshot le sirve a quien audita, no a quien lee. Va a la
    trazabilidad; en el encabezado sólo la fecha.
    """
    if not version:
        return None
    encontrado = re.search(r"(\d{4})-(\d{2})-(\d{2})", version)
    if not encontrado:
        return None
    anio, mes, dia = (int(parte) for parte in encontrado.groups())
    if not 1 <= mes <= 12:
        return None
    return f"{dia} de {MESES[mes - 1]} de {anio}"


# Las mismas tres formas que el servidor busca en el borrador. Se repiten aquí a propósito:
# el renderizador tiene que poder negarse sin haber hablado con el servicio, que es
# justamente el caso en que el servicio no está.
MONTO = (
    re.compile(r"M\$\s?\d{1,3}(?:\.\d{3})+"),
    re.compile(r"\d{1,3}(?:\.\d{3})*(?:,\d+)?\s+(?:mil\s+)?millones", re.I),
    re.compile(r"-?\d+,\d+\s?%"),
)


def montos_en(html: str) -> list[str]:
    """Los montos que el lector va a ver, buscados sobre el texto y no sobre el marcado."""
    texto = re.sub(r"<[^>]+>", " ", html)
    encontrados: list[str] = []
    for patron in MONTO:
        for hallazgo in patron.findall(texto):
            if hallazgo not in encontrados:
                encontrados.append(hallazgo)
    return encontrados


def sello(verificacion: dict | None, usadas: set[str]) -> str:
    """El sello dice cuántas, cuáles, y **sólo de las que están en el documento**.

    Dos reglas que salieron de leerlo como lector y no como autor:

    - Decir «1 no verificable» sin decir cuál obliga a desconfiar de todas: una cautela sin
      destinatario contamina el documento entero en vez de acotar el problema.
    - Una cifra declarada que no llegó a la prosa no cuenta. El sello describe el documento,
      no la lista de intenciones de quien lo escribió, y anunciar «14 de 15» cuando el
      informe tiene catorce cifras deja al lector buscando una que no existe.
    """
    if not verificacion:
        # Un documento sin verificación sólo llega hasta aquí cuando no cita ninguna cifra: la
        # composición se niega antes si trae montos. Y aun así el sello no calla, porque la
        # ausencia de sello se lee igual que un sello limpio.
        return ('<div class="sello"><b>Este documento no cita cifras de la base.</b> '
                '<span>No hay comprobación que informar.</span></div>')
    en_documento = [r for r in verificacion.get("results", []) if r.get("as_written") in usadas]
    comprobadas = len(en_documento)
    verificadas = len([r for r in en_documento if r.get("status") == "verificada"])
    rechazadas = len([r for r in en_documento if r.get("status") == "rechazada"])
    sueltas = [r for r in en_documento if r.get("status") != "verificada"]
    clase = "sello malo" if rechazadas else "sello"
    etiqueta = (f"<b>{rechazadas} cifra{'s' if rechazadas != 1 else ''} rechazada"
                f"{'s' if rechazadas != 1 else ''}.</b>" if rechazadas
                else f"<b>{verificadas} de {comprobadas} cifras verificadas contra la base.</b>")
    partes = [etiqueta]
    if sueltas:
        nombradas = ", ".join(escapar(r.get("as_written") or "una cifra sin rótulo") for r in sueltas[:3])
        resto = f" y {len(sueltas) - 3} más" if len(sueltas) > 3 else ""
        verbo = "no pudo comprobarse" if len(sueltas) == 1 else "no pudieron comprobarse"
        partes.append(f'<span>{nombradas}{resto} {verbo}, y va{"n" if len(sueltas) != 1 else ""} '
                      f'<span class="nv">subrayada{"s" if len(sueltas) != 1 else ""} en el texto</span>.</span>')
    partes.append('<span>La comprobación no lee la prosa: no certifica que el texto las use bien.</span>')
    fecha = fecha_legible(verificacion.get("knowledge_version"))
    if fecha:
        partes.append(f'<span class="snap">Base de conocimiento al {fecha}.</span>')
    return f'<div class="{clase}">' + "".join(partes) + "</div>"


def bloque_html(bloque: dict, escritas: dict[str, str], figuras: dict, avisos: list[str], usadas: set[str], institucion: str | None = None) -> str:
    tipo = bloque.get("tipo")
    if tipo == "parrafo":
        return f"<p>{componer_cifras(bloque.get('texto', ''), escritas, usadas)}</p>"
    if tipo == "lista":
        items = "".join(f"<li>{componer_cifras(item, escritas, usadas)}</li>" for item in bloque.get("items", []))
        return f"<ul>{items}</ul>"
    if tipo == "preguntas":
        items = "".join(
            f"<li>{componer_cifras(item.get('pregunta', ''), escritas, usadas)}"
            + (f'<span class="who">{escapar(item["a_quien"])}</span>' if item.get("a_quien") else "")
            + "</li>"
            for item in bloque.get("items", [])
        )
        return f'<ol class="q">{items}</ol>'
    if tipo == "tabla":
        encabezados = "".join(f"<th>{escapar(celda)}</th>" for celda in bloque.get("encabezados", []))
        filas = "".join(
            "<tr>" + "".join(f"<td>{componer_cifras(celda, escritas, usadas)}</td>" for celda in fila) + "</tr>"
            for fila in bloque.get("filas", [])
        )
        return f'<div class="tw"><table><thead><tr>{encabezados}</tr></thead><tbody>{filas}</tbody></table></div>'
    if tipo == "figura":
        return figura_html(bloque.get("ref"), figuras, avisos, institucion)
    avisos.append(f"bloque de tipo desconocido: {tipo}")
    return f"<p>{componer_cifras(bloque.get('texto', ''), escritas, usadas)}</p>"


FUENTES = {
    "FECU": "planillas FECU",
    "BENCHMARK": "estados financieros auditados",
}


def mobiliario_de_figura(entrada: dict, institucion: str | None) -> tuple[str, str]:
    """Título y línea de fuente, compuestos desde los datos de la propia figura.

    Un pie escrito a mano puede olvidar la fuente, o nombrar una que no se usó. Derivarlo de
    los `source_refs` de los puntos efectivamente graficados hace que no pueda mentir, y que
    ninguna figura salga sin decir de dónde viene ni qué años cubre.
    """
    spec = entrada.get("figure") or {}
    series = spec.get("series") or []
    ejercicios = sorted({p["exercise"] for s in series for p in (s.get("points") or [])
                         if p.get("value") is not None})
    etiquetas = [s.get("label") or s.get("metric_id") for s in series]
    titulo = entrada.get("titulo") or " y ".join(filter(None, etiquetas))

    familias = []
    for serie in series:
        for punto in serie.get("points") or []:
            for referencia in punto.get("source_refs") or []:
                nombre = FUENTES.get(str(referencia).split("-")[0], "serie canónica de la institución")
                if nombre not in familias:
                    familias.append(nombre)

    partes = []
    if institucion:
        partes.append(institucion)
    if ejercicios:
        rango = f"{ejercicios[0]}–{ejercicios[-1]}" if len(ejercicios) > 1 else str(ejercicios[0])
        partes.append(f"{len(ejercicios)} ejercicio{'s' if len(ejercicios) != 1 else ''}, {rango}")
    if familias:
        partes.append("fuente: " + " y ".join(familias))
    # Un dato agregado dice sobre cuántas instituciones se calculó y con qué criterio: sin eso,
    # una mediana parece una propiedad del sector cuando es una propiedad de nuestra cobertura.
    cohorte = spec.get("cohort") or {}
    if cohorte:
        partes.append(f"n = {cohorte.get('n')} instituciones; el grupo lo define hoy la cobertura de la base "
                      "y no una decisión sobre comparabilidad")
    return titulo, " · ".join(partes)


def figura_html(ref: str | None, figuras: dict, avisos: list[str], institucion: str | None = None) -> str:
    entrada = figuras.get(ref or "")
    if not entrada:
        avisos.append(f"figura referida y no declarada: {ref}")
        return ""
    spec = entrada.get("figure") or {}
    pregunta = entrada.get("pregunta_llana") or ""
    pie = entrada.get("pie") or ""
    titulo, procedencia = mobiliario_de_figura(entrada, institucion)
    en_alcance = list(spec.get("breaks_in_scope") or [])
    marcados = [a.get("break_id") for a in (spec.get("annotations") or [])]
    faltantes = [q for q in en_alcance if q not in marcados]
    partes = ["<figure>"]
    if titulo:
        partes.append(f'<p class="titulo-figura">{escapar(titulo)}</p>')
    if pregunta:
        partes.append(f'<p class="pregunta">{escapar(pregunta)}</p>')
    if faltantes:
        # No se dibuja, y se dice por qué en la página: el lector tiene que saber que
        # falta un gráfico y cuál es la razón, no encontrarse un hueco.
        avisos.append(f"figura «{ref}» no dibujada: quiebres sin marca ({', '.join(faltantes)})")
        partes.append(
            '<div class="quiebre">Esta figura no se dibuja: la serie cruza un cambio de presentación '
            f'({escapar(", ".join(faltantes))}) que no viene marcado, y trazarla la mostraría como continua '
            'cuando no lo es. Los datos van en la tabla.</div>'
        )
    else:
        partes.append(f'<div class="grafico" id="fig-{escapar(ref)}"></div>')
    # El pie estructural va siempre, aunque el modelo no escriba prosa: institución, cuántos
    # ejercicios cubre y de qué fuentes salen los puntos que se dibujaron.
    if procedencia or pie:
        cuerpo = f'<span class="fuente">{escapar(procedencia)}</span>' if procedencia else ""
        if pie:
            cuerpo += f"{' ' if cuerpo else ''}{escapar(pie)}"
        partes.append(f"<figcaption>{cuerpo}</figcaption>")
    partes.append("</figure>")
    return "".join(partes)


def seccion_html(seccion: dict, escritas: dict[str, str], figuras: dict, avisos: list[str], usadas: set[str], institucion: str | None = None) -> str:
    tipo = seccion.get("tipo", "bloque")
    if tipo not in SECCIONES_CONOCIDAS:
        # Degradar y avisar: el documento nunca se rompe por una etiqueta nueva, y una
        # etiqueta que se repite es la señal de que la biblioteca necesita esa clase.
        avisos.append(f"sección de tipo desconocido, compuesta como genérica: {tipo}")
    cuerpo = "".join(bloque_html(bloque, escritas, figuras, avisos, usadas, institucion) for bloque in seccion.get("bloques", []))
    if tipo == "respuesta_una_frase":
        clase = "una abstencion" if seccion.get("es_abstencion") else "una"
        return (f"<section><h2>{escapar(seccion.get('titulo', 'Respuesta en una frase'))}</h2>"
                f'<div class="{clase}">{cuerpo}</div></section>')
    titulo = f"<h2>{escapar(seccion['titulo'])}</h2>" if seccion.get("titulo") else ""
    return f"<section>{titulo}{cuerpo}</section>"


def comprobar_abstencion(spec: dict, avisos: list[str]) -> list[str]:
    """Una abstención declara dónde cumple cada obligación; aquí se comprueba que apunte."""
    una = next((s for s in spec.get("secciones", []) if s.get("tipo") == "respuesta_una_frase"), {})
    if not (una.get("es_abstencion") or spec.get("documento") == "abstencion"):
        return []
    mapeo = spec.get("abstencion") or {}
    tipos = {s.get("tipo") for s in spec.get("secciones", [])}
    errores = []
    for obligacion in OBLIGACIONES_ABSTENCION:
        destino = mapeo.get(obligacion)
        if not destino:
            errores.append(f"la abstención no declara `{obligacion}`")
        elif destino not in tipos:
            errores.append(f"`{obligacion}` apunta a la sección «{destino}», que no está en el informe")
    return errores


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entrada", required=True, type=Path)
    parser.add_argument("--salida", required=True, type=Path)
    args = parser.parse_args()

    spec = json.loads(args.entrada.read_text(encoding="utf-8"))
    avisos: list[str] = []

    errores = comprobar_abstencion(spec, avisos)
    if errores:
        print("El informe es una abstención y no declara dónde cumple sus obligaciones:", file=sys.stderr)
        for error in errores:
            print(f"  - {error}", file=sys.stderr)
        print("Una abstención no se acorta: declare `abstencion` con las tres referencias.", file=sys.stderr)
        return 2

    # Cada cifra declarada, con el veredicto que le corresponde: la composición del texto
    # distingue la comprobada de la que no se pudo comprobar.
    veredictos = {r.get("as_written"): r.get("status")
                  for r in ((spec.get("verificacion") or {}).get("results") or [])}
    escritas = {c["as_written"]: veredictos.get(c["as_written"], "sin_verificar")
                for c in spec.get("cifras_declaradas", []) if c.get("as_written")}
    figuras = spec.get("figuras") or {}

    # El subtítulo llega redactado desde el servidor; si el que viene en el spec trae
    # vocabulario nuestro, es que alguien lo reescribió y el lector paga la diferencia.
    for jerga in ("IES-", "perímetro separado", "Cruch"):
        if jerga.lower() in str(spec.get("subtitulo", "")).lower():
            avisos.append(f"el subtítulo trae vocabulario interno («{jerga}»): use `document_header.subtitulo` del contexto")

    # El nombre completo va en el pie de cada figura; la sigla no le dice nada al lector.
    nombre_institucion = spec.get("institucion_nombre") or spec.get("institucion")

    # El cuerpo se compone primero: el sello necesita saber qué cifras llegaron al texto.
    usadas: set[str] = set()
    secciones = "".join(seccion_html(s, escritas, figuras, avisos, usadas, nombre_institucion) for s in spec.get("secciones", []))
    huerfanas = sorted(set(escritas) - usadas)
    for huerfana in huerfanas:
        avisos.append(f"cifra declarada que no aparece en el texto: {huerfana}")

    encabezado = [
        "<header>",
        f'<div class="kick">{escapar(spec.get("antetitulo", ""))}</div>' if spec.get("antetitulo") else "",
        f'<h1>{escapar(spec.get("titulo", ""))}</h1>',
        f'<div class="sub">{escapar(spec.get("subtitulo", ""))}</div>' if spec.get("subtitulo") else "",
        sello(spec.get("verificacion"), usadas),
        "</header>",
    ]
    cuerpo = "".join(encabezado) + secciones
    if spec.get("pie"):
        cuerpo += f"<footer><p>{escapar(spec['pie'])}</p></footer>"

    # Un informe con cifras y sin verificación no se compone.
    #
    # Antes salía con el sello «Sin verificar» en rojo, que es honesto y no alcanza: el
    # documento igual llegaba entero al lector, y decidir si confiar quedaba de su lado sin
    # que tuviera con qué. Pasó de verdad —con el servicio caído, una lectura de la UFRO se
    # construyó leyendo la base en disco y salió con once cifras sin comprobar—, y ese camino
    # sólo existe en el equipo que tiene el repositorio local: para un cliente no es un
    # respaldo, es una salida que no se puede reproducir.
    #
    # La doctrina ya lo decía —ningún informe se entrega sin pasar por la verificación— y sólo
    # faltaba que el renderizador lo hiciera cumplir, como ya hace con los quiebres sin marca.
    if not spec.get("verificacion"):
        montos = montos_en(cuerpo)
        if montos:
            print("El informe cita cifras y no trae verificación:", file=sys.stderr)
            for monto in montos[:5]:
                print(f"  - {monto}", file=sys.stderr)
            if len(montos) > 5:
                print(f"  - y {len(montos) - 5} más", file=sys.stderr)
            print("Llame a verify_reported_figures y adjunte su respuesta en `verificacion`.", file=sys.stderr)
            print("Si el servicio no responde, la respuesta es una abstención que dice qué "
                  "herramienta falta, no un informe construido con otra fuente.", file=sys.stderr)
            return 2

    dibujables = {
        ref: entrada.get("figure")
        for ref, entrada in figuras.items()
        if not [q for q in (entrada.get("figure", {}).get("breaks_in_scope") or [])
                if q not in [a.get("break_id") for a in (entrada.get("figure", {}).get("annotations") or [])]]
    }

    plantilla = (ASSETS / "informe.template.html").read_text(encoding="utf-8")
    pagina = (plantilla
              .replace("__TITULO__", escapar(spec.get("titulo", "Informe financiero")))
              .replace("__CUERPO__", cuerpo)
              .replace("/* __D3__ */", (ASSETS / "vendor" / "d3.min.js").read_text(encoding="utf-8"))
              .replace("/* __PLOT__ */", (ASSETS / "vendor" / "plot.umd.min.js").read_text(encoding="utf-8"))
              .replace("__RECETAS__", (ASSETS / "recetas_plot.js").read_text(encoding="utf-8"))
              .replace("/* __FIGURAS__ */", json.dumps(dibujables, ensure_ascii=False)))
    args.salida.write_text(pagina, encoding="utf-8")

    print(f"{args.salida}")
    print(f"secciones: {len(spec.get('secciones', []))} | cifras compuestas: {len(usadas)} | "
          f"figuras: {len(dibujables)} de {len(figuras)}")
    for aviso in avisos:
        print(f"  aviso: {aviso}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
