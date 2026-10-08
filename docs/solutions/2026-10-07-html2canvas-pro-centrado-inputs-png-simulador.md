# 📘 Ficha Técnica: Migración a html2canvas-pro, Centrado Milimétrico y Renderizado de Inputs en PNG (Simulador de Olas)

**Fecha:** 2026-10-07  
**Autor:** Antigravity (Pair Programming con Ricardo García)  
**Módulo:** `01-Propuestas-Comerciales/Instituto-Tecnologico/simulador-olas.html`  
**Estado:** ✅ Implementado, Probado en Chromium & Registrado en Memoria Ecosistémica  

---

## 1. Contexto y Síntomas

Al utilizar el botón de descarga en imagen **PNG** del Simulador de Capacidad WFM:
1. **Hundimiento de Textos y Emojis:** En los badges superiores (ej. `LICITACIÓN INSTITUTO - META: 450 CONTRATOS`, `✓ Roster 100% Cubierto`), el texto aparecía recargado contra el borde inferior de la pastilla. En el banner de hito operativo, el emoji de la meta (🎯) dentro del contenedor verde `w-9 h-9` salía desplazado hacia el fondo, perdiendo su centrado simétrico.
2. **Campos de Formulario Vacíos o Cortados:** En el panel izquierdo de Parámetros WFM, los campos `<input>` (Fecha de inicio `2026-06-29`, Meta `450`, etc.) no renderizaban el valor escrito en el canvas, saliendo como cajas semivacías o machucadas.

---

## 2. Causa Raíz

1. **Bug Histórico de `html2canvas 1.4.1`:**
   - La librería `html2canvas 1.4.1` (abandonada en 2022) calcula la coordenada de dibujo en canvas de nodos de texto (`TextNode` y emojis) sumando la altura completa del contenedor (`bounds.top + bounds.height`) con `textBaseline = 'bottom'`. Esto ignora la propiedad `align-items: center` de Flexbox y ancla el texto en el borde inferior.
   - `html2canvas 1.4.1` no tiene acceso nativo al DOM interno ni renderiza correctamente el atributo `.value` de los elementos `<input>` en formularios interactivos.
2. **Silo de Memoria Previo:**
   - Este mismo problema se había resuelto el 30 de septiembre de 2026 en **El Panóptico (V9.9.20 @114)** para la tabla ACT HD, pero la lección quedó confinada a la carpeta de soluciones de ese repositorio, sin haberse elevado a `.agents/instincts/registry.json` ni a las reglas transversales `AGENTS.md`.

---

## 3. Solución Implementada

1. **Sustitución Obligatoria por `html2canvas-pro`:**
   - Se reemplazó el script por el CDN oficial moderno:
     `https://cdn.jsdelivr.net/npm/html2canvas-pro/dist/html2canvas-pro.min.js`
   - Corrige el cálculo de baselines tipográficos y compatibilidad con Flexbox moderno.

2. **Encapsulamiento con `inline-flex` y `line-height: 1`:**
   - El emoji 🎯 se encapsuló en un contenedor discreto:
     `<span style="display:inline-flex; align-items:center; justify-content:center; line-height:1;">🎯</span>`
   - Los badges y pastillas de estado recibieron `inline-flex items-center leading-none`.

3. **Gancho `onclone` para Sustitución Transparente de Inputs:**
   - En la función `exportarPNG`, se configuró el gancho `onclone: (clonedDoc) => { ... }`:
     Todos los `<input>` y `<select>` son sustituidos en el documento clonado por elementos `<div>` que conservan sus dimensiones exactas (`getBoundingClientRect()`), estilos y clases, renderizando `innerText = input.value` centrado con `display: inline-flex; align-items: center; line-height: 1.2; box-sizing: border-box;`.
   - Esto garantiza que en el PNG final todos los valores numéricos y fechas salgan 100% nítidos, legibles y centrados.

4. **Blindaje de Memoria Global (Transversal):**
   - Registro del instinto `html2canvas-pro-inline-flex-centering` en `.agents/instincts/registry.json`.
   - Incorporación de la sección **2.6** en `.agents/AGENTS.md`.
   - Adición de la **FASE 16** en `MANUAL_ARQUITECTURA_TELAT.md` y actualización en `MEGA_PROMPT_TELAT_v10.md`.
   - Mandato obligatorio en el flujo de trabajo (Fase 1) de consultar `registry.json` y `docs/solutions/` antes de codificar.

---

## 4. Anti-Patrones & Prohibiciones

- 🚫 **PROHIBIDO** importar `html2canvas 1.4.1` en cualquier repositorio (corporativo o personal).
- 🚫 **PROHIBIDO** dejar textos o emojis crudos sueltos dentro de contenedores Flexbox en componentes que deban ser rasterizados a canvas.
- 🚫 **PROHIBIDO** exportar formularios interactivos a imagen sin sustituir o clonar el valor de los inputs en el gancho `onclone`.

---

## 5. Verificación & Evidencia

- **Validación en Navegador (Chromium):**
  - Carga limpia de `html2canvas-pro`.
  - Disparo de la exportación PNG mediante clic en botón `PNG`.
  - 0 errores de consola JavaScript.
- **Evidencias Visuales:**
  - `png_export_executed_1791420455855.png` demostrando la ejecución sin bloqueos.
