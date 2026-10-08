# 📘 Ficha Técnica: Sincronización Temporal Licitatoria, Controles Stepper y Reporte PDF Landscape (Simulador de Olas)

**Fecha:** 2026-10-07  
**Autor:** Antigravity (Pair Programming con Ricardo García)  
**Módulo:** `01-Propuestas-Comerciales/Instituto-Tecnologico/simulador-olas.html`  
**Estado:** ✅ Implementado, Probado en Chromium & Commiteado en Git  

---

## 1. Contexto y Síntomas

En la revisión operativa del **Simulador de Capacidad & WFM** para la Licitación del Instituto Tecnológico, se detectaron las siguientes restricciones y oportunidades directivas:
1. **Fecha Base Rígida:** La fecha de arranque estaba fija en `2026-06-29` dentro del código, sin posibilidad de calibrarla interactivamente para sincronizarla con el calendario oficial de fallo y firma de contrato del Instituto.
2. **Entrada de Turnos Irreal y Fricción en Inputs:** El campo de turnos en las aulas físicas permitía valores arbitrarios (e.g. 7 turnos diarios), lo cual es operativamente imposible en sites de Contact Center (jornadas de 6 a 8 horas). Asimismo, la edición requería teclear manualmente cada número sin controles táctiles ágiles.
3. **Exportación a PDF Deficiente:** El generador de PDF anterior producía un documento vertical de 3 páginas con márgenes desajustados y un fallo crítico: la gráfica se exportaba con fondo negro puro ilegible debido a la pérdida del canal alfa en `canvas.toDataURL('image/jpeg')`.

---

## 2. Causa Raíz

1. **Fecha Inmutable:** No existía un `<input type="date">` vinculado a `fechaInicioProyecto` con reactividad en cascada sobre las semanas y las olas preprogramadas.
2. **Falta de Validación de Rango de Turnos:** El input de turnos carecía de `min="1"` y `max="2"` y de botones tipo stepper `[-]` / `[+]` que forzaran las únicas dos modalidades reales de operación física en piso: *Solo Matutino (1)* y *Matutino y Vespertino (2)*.
3. **Gráfica Negra en Canvas Export:** Chart.js renderiza por defecto sobre un canvas con fondo transparente (`rgba(0,0,0,0)`). Al convertir dicho lienzo mediante `toDataURL` en formato JPEG, el estándar convierte la transparencia en negro puro (`#000000`).

---

## 3. Solución Implementada

1. **Selector de Fecha Dinámica Sincronizada:**
   - Incorporación de control interactivo `<input type="date" v-model="fechaInicioProyecto">` en el panel de parámetros de la vista *Tablero & Curvas*.
   - Watcher reactivo y función `generarOlasBase(nuevaFecha)` que recalcula en tiempo real el inicio de cada una de las olas y las 30 semanas de la sábana forense.
   - Persistencia automática de la fecha en `localStorage`.

2. **Controles Stepper `[-]` y `[+]` con Límite Estricto de 2 Turnos:**
   - Adición de botones stepper de un solo clic para capacitadores (`±1`) y para la capacidad física de aulas (`±5`).
   - Límite absoluto en turnos diarios: `min="1"` y `max="2"`. Si el turno es 1, el botón `[-]` se deshabilita (`disabled`); si alcanza 2, el botón `[+]` se deshabilita y se muestra el badge de texto *"Matutino y Vesp."*. El evento `@change` aplica `Math.min(2, Math.max(1, turnos))` defensivo ante entradas por teclado.

3. **Rediseño del Informe PDF Ejecutivo a 2 Páginas Horizontales (Landscape):**
   - Configuración de página en modo apaisado: `jsPDF({ orientation: 'landscape', unit: 'pt', format: 'letter' })` (792 × 612 pt).
   - **Corrección de Gráfica Negra:** Se clona el lienzo en un canvas temporal fuera de pantalla (`tempCanvas`), se pinta una base blanca sólida (`tCtx.fillStyle = '#ffffff'; tCtx.fillRect(...)`), se dibuja la gráfica encima y se exporta en PNG de alta nitidez sin canal alfa.
   - **Página 1 (Tablero Ejecutivo):** Barra superior Celeste Telat (`#3284C6`), 5 KPIs ejecutivos en cajas redondeadas, gráfica de capacidad nítida y banner de hito operativo de cobertura (Semana y número de olas).
   - **Página 2 (Infraestructura & Sábana Forense):** Barra Naranja Telat (`#EB5B27`), columna izquierda con premisas WFM e inventario de aulas (desglosando turnos matutino/vespertino y capacidad instalada diaria), y columna derecha con tabla ejecutiva semana a semana hasta la semana 25 con indicadores de altas, roster, producto y cumplimiento.

---

## 4. Anti-Patrones / Prohibiciones

- 🚫 **PROHIBIDO** permitir más de 2 turnos diarios en la configuración física de salones de capacitación (límite operativo estricto: matutino y vespertino).
- 🚫 **PROHIBIDO** exportar lienzos transparentes de Chart.js directamente a PDF sin antes dibujar una capa blanca de fondo en un canvas intermedio.
- 🚫 **PROHIBIDO** forzar reportes directivos a documentos verticales multihébra desordenados; los entregables para comités ejecutivos deben ajustarse a formato panorámico 16:9 o Landscape de exactamente 2 páginas.

---

## 5. Verificación & Evidencia

- **Validación Interactiva en Chromium (Browser Subagent):**
  1. Selector de fecha probado y verificado cargando `29/06/2026`.
  2. Steppers probados en Aula 1: capacidad incrementada exitosamente de 20 a 25 con clic en `[+]`.
  3. Turnos diarios probados en Aula 1: incrementados a 2 turnos con `[+]`, desactivando el botón conforme a la regla de tope.
  4. Generación de PDF activada sin errores en la consola de JavaScript (0 errores detectados).
- **Evidencias Visuales:**
  - `initial_tablero_curvas_1791419603632.png`: Vista inicial con date picker.
  - `recursos_site_steppers_1791419672701.png`: Vista de Recursos de Site con steppers y límite de 2 turnos.
  - `pdf_generation_final_1791419754003.png`: Exportación de PDF ejecutada limpiamente.
