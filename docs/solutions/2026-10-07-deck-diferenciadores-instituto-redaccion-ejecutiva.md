# 📘 Ficha Técnica: Refactorización Ejecutiva de Redacción & Métricas para la Propuesta Comercial del Instituto

**Fecha:** 2026-10-07  
**Repositorio:** `presentaciones-ejecutivas`  
**Ubicación:** `01-Propuestas-Comerciales/Instituto-1-Infonatel/`  
**Autor:** Ricardo García / Antigravity IDE  
**Estatus:** ✅ Validado por Mauricio Cruz (Director de Operaciones) · En espera de visto bueno final de Luis Cortina (Director General)  

---

## 1. Contexto y Síntomas
Para la licitación del **Instituto**, se preparó una presentación ejecutiva de 2 diapositivas panorámicas (16:9) destacando los diferenciadores tecnológicos y operativos de Telat Group. Tras la primera revisión directiva, se identificó que la propuesta contenía terminología excesivamente técnica de contact center y microdesarrollo (`<350ms`, `<15s`, `SOTA`, `paramétrico`, `100% obligatorio de QA`, o límites fijos de 4 semanas y 150 a 300 agentes). 

Estos términos presentaban dos riesgos críticos:
1. **Riesgo Comercial / Negociación:** Comprometer contractualmente umbrales rígidos no solicitados (como 100% de llamadas en QA o cierres en <15s), o revelar tácitamente la estrategia de segmentación societaria de Telat.
2. **Riesgo de Percepción Ejecutiva:** El comité evaluador está compuesto por directivos de alto nivel que requieren claridad y certeza de impacto, no tecnicismos de micro-desarrollo ni siglas especializadas.

---

## 2. Causa Raíz
- **Sobre-especificación técnica en borradores iniciales:** Se arrastraban parámetros de desarrollo de software (`<350ms`, `wrap-up <15s`, `SOTA`) propios de fichas de ingeniería en lugar de redacción de alto valor de negocio.
- **Asunción externa de partición de licitación:** Se hacía referencia a 150 o 300 posiciones, cuando la estrategia comercial de Telat es ir por el volumen total disponible (desde 0 hasta 450 agentes) sin transparentar supuestos externos.
- **Promesa incondicional de cobertura:** La auditoría con IA afirmaba un "100% de llamadas" absoluto, cuando en licitaciones el alcance de auditoría varía según los requerimientos y presupuesto del pliego (5%, 10%, 50% o hasta 100%).
- **Bloqueo de archivos en Windows al compilar PDF:** Cuando el PDF objetivo está abierto en el visor integrado del IDE o Acrobat, los procesos de exportación fallan silenciosamente si no se invoca un proceso aislado con argumentos explícitos (`scripts/export_instituto_pdf.ps1`).

---

## 3. Solución Implementada
1. **Slide 1 - Tiempo de Respuesta del Copiloto:**
   - Sustituido `<350ms` por redacción ejecutiva natural: **"en un par de segundos"**.
   - Mensaje: Requisitos y catálogo normativo oficial visibles en pantalla en un par de segundos, evitando consultas a manuales.
2. **Slide 1 - Cierre de Expediente y Wrap-up:**
   - Modificado `<15s` a un umbral realista y cómodo: **"20 segundos o menos"** (`≤20s`).
   - Métrica en tarjeta: `≤20s` Cierre y Tipificación | `100%` Expedientes con Folio.
3. **Slide 2 - Garantía de Despliegue Masivo:**
   - Elevada la capacidad oficial a: **"Garantía de Despliegue: Desde 0 hasta 450 Agentes"**.
   - Reflejado en badge superior, título principal, resumen ejecutivo y tarjeta 5 (Capacidad Total en Site).
4. **Slide 2 - Eliminación de Jerga ("SOTA" y "Paramétrico"):**
   - Eliminadas completamente las palabras "SOTA" y "paramétrico".
   - Titulado como: **"Garantía de Despliegue: Desde 0 hasta 450 Agentes"** con un **"Plan Estructurado de Despliegue (Adaptable al Calendario de Semanas del Instituto)"**.
5. **Slide 2 - Flexibilidad de Cronograma:**
   - Eliminado el esquema rígido de "Ola 1, 2, 3 en 4 semanas".
   - Reemplazado por 3 fases claras (Fase 1: Atracción & Filtros, Fase 2: Capacitación & Aulas, Fase 3: Operación en Vivo) con nota explícita de flexibilidad: *"Plan Estructurado en Semanas · Ajustable a los tiempos del Instituto"*.
6. **Slide 2 - Cobertura Flexible de Calidad con IA:**
   - Sustituido el compromiso ciego del 100% por: **"Auditoría con Inteligencia Artificial: Cobertura Flexible de Hasta el 100%"**.
   - Texto: *"Permite evaluar muestras desde el 5%, 10% o 50%, con capacidad de alcanzar hasta el 100% de las llamadas según los requerimientos del Instituto"*.
   - Métrica: `Hasta 100% Supervisión con IA (Muestreo Flexible según Pliego)`.
8. **Eliminación de Pastillas Superiores Redundantes:**
   - Retiradas las píldoras repetitivas en la cabecera de Slide 1 (*"Canal Telefónico & Continuidad en Ventanilla"*) y Slide 2 (*"Garantía de Despliegue: Desde 0 hasta 450 Agentes"*), ya que dicha información se encuentra desarrollada de forma destacada en las tarjetas inferiores.
   - Sustituidas por branding corporativo sobrio: `TELAT GROUP · 2026`.
9. **Presencia Sutil de Inteligencia Artificial en las 5 Tarjetas:**
   - Siguiendo la directriz del Director General (Luis Cortina), se evidenció de forma sutil y orgánica la presencia de IA en cada tarjeta sin saturar la lectura:
     - *Tarjeta 1 (Asistencia en Línea):* Copiloto con IA contextual en pantalla durante la llamada.
     - *Tarjeta 2 (Cierre Inmediato):* Algoritmo de IA para síntesis automática de notas, expediente y folio en CRM.
     - *Tarjeta 3 (Seguridad y Privacidad):* Detección inteligente por IA que activa silenciamiento y enmascaramiento de datos personales sensibles (PII).
     - *Tarjeta 4 (Calidad Integral):* Algoritmos de IA para analítica multidimensional continua sobre voz y transcripción.
     - *Tarjeta 5 (Certeza de Despliegue):* Modelado predictivo de Workforce Management e IA para proyectar curvas de aprendizaje, rotación y capacidad de aulas.
10. **Reestructuración de Cintillos Inferiores en 2 Líneas Completas:**
    - Se eliminó el truncamiento con puntos suspensivos (`...`) en los cintillos institucionales.
    - *Línea Superior:* Mensaje descriptivo al 100% de ancho (Impacto Directo al Ciudadano en Slide 1; Gobernanza Institucional & Blindaje de SLA en Slide 2).
    - *Línea Inferior:* Categoría de certificación + 4 píldoras distintivas (ISO 18295-1, ISO 27001, ISO 20000-1 y PCI-DSS en Slide 1; ISO 9001, ISO 22301, ISO 37001 y ESR en Slide 2).
11. **Optimización de Espacios Muertos y Tipografía Ejecutiva para PDF:**
    - Ajustado el padding de las diapositivas a `2.2rem 3.5rem 1.6rem 3.5rem` tanto en pantalla como en `@media print`.
    - Ampliado el padding interno de tarjetas a `p-6`, incrementando tamaños tipográficos (títulos `text-[1.28rem] - text-[1.32rem]`, párrafos `13.2px - 13.5px`, cajas `12px - 12.2px`, métricas `text-4xl`).
    - Eliminadas las franjas de espacio muerto vertical marcadas en rojo, logrando una presentación llena, imponente y legible de un vistazo sin requerir zoom.

---

## 4. Anti-Patrones / Prohibiciones
- ❌ **PROHIBIDO** incluir delimitadores de microdesarrollo como `<350ms`, `latencia <0.3s` o `determinista` en presentaciones ejecutivas. Usar *"en un par de segundos"* o *"en segundos"*.
- ❌ **PROHIBIDO** comprometer wrap-up nominales estrechos como `<15s` en propuestas iniciales. La política comercial debe indicar *"20 segundos o menos"*.
- ❌ **PROHIBIDO** revelar o mencionar cifras vinculadas a particiones de razones sociales (ej. 150 o 300). Telat se presenta con capacidad plena de *"desde 0 hasta 450 agentes"*.
- ❌ **PROHIBIDO** usar términos de laboratorio o investigación como `SOTA` (State of the Art) o `paramétrico`. Usar términos directivos como *"plan estructurado"*, *"modelo integral"* o *"adaptable"*.
- ❌ **PROHIBIDO** comprometer auditorías fijas al 100% como única alternativa. Siempre redactar como *"cobertura flexible de hasta el 100%"*.
- ❌ **PROHIBIDO** dejar textos truncados con puntos suspensivos en cintillos institucionales. Usar estructura en dos niveles horizontales.

---

## 5. Verificación & Evidencia
- **Código Fuente Actualizado:** [`index.html`](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Instituto-1-Infonatel/index.html).
- **PDF Vectorial HD Compilado:** [`Diferenciadores_Tecnologicos_Instituto_Telat.pdf`](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Instituto-1-Infonatel/Diferenciadores_Tecnologicos_Instituto_Telat.pdf) (848.07 KB, 16x9 pulgadas vectoriales).
- **Capturas de Verificación en Navegador (1920x1080):**
  - Slide 1: `slide_1_verification_1791415425503.png` (verificado "en un par de segundos", "≤20s", IA sutil en 3 tarjetas, cintillo en 2 líneas sin `...`, cero espacios muertos).
  - Slide 2: `slide_2_verification_1791415599843.png` (verificado "0 hasta 450 agentes", "Hasta 100% con IA", modelado predictivo, cintillo en 2 líneas sin `...`, cero espacios muertos, render 100% limpio).
