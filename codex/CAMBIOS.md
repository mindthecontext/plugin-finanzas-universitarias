# Cambios · Finanzas Universitarias

<!-- Generado al derivar el paquete desde cambios.yaml. No editar a mano. -->

Qué cambia para quien usa este saber, versión por versión. Lo que corre de verdad el servicio lo dice su herramienta `ver_cambios`; esto es la copia del paquete.

## v2.2.0 · 2026-09-15

El saber dice qué cambió de una versión a otra y en qué versión está corriendo: aparece `ver_cambios`. Y si tienes un asiento y es la primera vez que te conectas —o te conectas desde una cuenta que el servicio todavía no conoce, con tu mismo correo—, ahora entras en tu primera consulta también cuando el servicio acaba de arrancar. Lo que ya respondía sigue igual.

- Herramientas: `build_financial_answer_context`, `build_sector_answer_context`, `compare_fecu_metric`, `compare_financial_metric`, `describe_fecu_distribution`, `describe_fecu_institution`, `get_analysis_criteria`, `list_fecu_institutions`, `list_fecu_measures`, `list_institutions`, `rank_fecu_institutions`, `route_financial_question`, `trace_financial_claim`, `ver_cambios`, `verify_reported_figures`
- Skills: `empezar-aqui`, `entender-el-ecosistema`, `entender-una-universidad`, `leer-el-resultado`, `leer-el-sustento`, `leer-la-solidez`, `leer-los-costos`, `preparar-sesion-de-consejo`
- Datos: sin manifiesto

## Línea base · v2.1.1 · 2026-09-15

Así está el saber cuando empieza este registro. Lee la situación financiera de las universidades chilenas en dos capas: expedientes auditados de 12 universidades, entre 2018 y 2024, con criterios, claims trazables y reglas de lectura (`list_institutions`, `build_financial_answer_context`, `compare_financial_metric`, `trace_financial_claim`), y la planilla FECU de la Subsecretaría de Educación Superior para las 55 del sistema, entre 2019 y 2024 (`describe_fecu_institution`, `compare_fecu_metric`, `describe_fecu_distribution`, `rank_fecu_institutions`, `list_fecu_measures`, `list_fecu_institutions`, `build_sector_answer_context`). Enruta preguntas a su pregunta canónica (`route_financial_question`), sirve el criterio de cada métrica (`get_analysis_criteria`) y comprueba las cifras de un entregable contra la base (`verify_reported_figures`). Declara «no derivable» en vez de completar, y la planilla no trae caja, deuda financiera, activo fijo, capex ni notas.

- Herramientas: no derivable
- Skills: `empezar-aqui`, `entender-el-ecosistema`, `entender-una-universidad`, `leer-el-resultado`, `leer-el-sustento`, `leer-la-solidez`, `leer-los-costos`, `preparar-sesion-de-consejo`
- Datos: sin manifiesto

Antes de v2.1.1 no hay registro de cambios.
