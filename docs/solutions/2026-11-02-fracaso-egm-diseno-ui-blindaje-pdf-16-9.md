# Solución Forense & Lecciones Aprendidas: Fracaso de EGM en Diseño UI/UX y Blindaje de Renderizado PDF 16:9

**Fecha:** 2026-11-02  
**Repositorio:** `presentaciones-ejecutivas`  
**Autor:** Ricardo García (Subdirector de Operaciones / IT & Ops Leader) / Antigravity Assistant  
**Módulos Afectados:** `01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V2`, `@media print`, `scripts/export_auto_glass_v2_pdf.ps1`

---

## 1. Problema Raíz & Diagnóstico del Fallo

Durante el desarrollo de la propuesta comercial ejecutiva para el sector de cristales automotrices en EE. UU. (dirigida a C-Levels como Safelite y Gerber), se intentó aplicar el modelo **Elephant-Goldfish Model (EGM)** (`google/elephant-goldfish-model`) para auditar y "optimizar" la presentación visual (V2).

Esto desató una **regresión visual severa**, deformando una maquetación moderna, compacta y profesional en una interfaz desproporcionada, alargada y rota.

### Las 3 Fallas Críticas Identificadas:

1. **Incompatibilidad Fundamental de EGM con UI/UX Frontend:**
   - **Causa:** EGM está diseñado estrictamente para documentos de texto y especificaciones técnicas (RFCs, PRDs, Markdown de arquitectura backend). 
   - **Efecto:** Sus revisores (`egm-design`, `egm-structural`) interpretan cualquier espacio negativo como una "deficiencia lógica que debe llenarse". Al forzar al Elefante a resolver estas "deficiencias", el agente inyectó textos y micro-métricas redundantes, hinchó tarjetas con `flex-1` ciego y rompió la armonía visual.
   - **Regla:** **Queda estrictamente prohibido usar EGM para juzgar, auditar o refactorizar layouts visuales, CSS o interfaces.**

2. **La Trampa del "Anti-Gap" Mecánico (`flex-1` + `justify-between` indiscriminado):**
   - **Causa:** Intentar forzar que las tarjetas toquen el borde superior e inferior de la pantalla sin tener volumen tipográfico real.
   - **Efecto:** Tarjetas con solo 2 líneas de texto se estiraron a más de 300px de altura, separando antinaturalmente títulos y párrafos por cavernas negras vacías (violación directa del Principio Gestalt de Proximidad).
   - **Regla:** Una caja debe tener su altura determinada por su contenido natural (`content-driven bounding box`) o una cuadrícula simétrica acotada (`max-w-[1540px] items-center justify-center`). El equilibrio y espacio negativo armónico es superior a rellenar la pantalla a la fuerza.

3. **Colapso de Grid a Columna Única en Chromium Headless (`@media print`):**
   - **Causa:** En Tailwind CSS, clases responsivas como `lg:col-span-6` o `lg:col-span-7` dependen de la media query `min-width: 1024px`. Al invocar `chrome.exe --headless=new --print-to-pdf`, el motor de impresión opera bajo `@media print`, donde las media queries de pantalla pueden ser ignoradas o tratadas como viewport móvil.
   - **Efecto:** En pantalla interactiva el HTML se veía perfecto lado a lado (50% / 50%), pero en el PDF las columnas colapsaban a `col-span-12`, apilando la columna derecha debajo de la izquierda y destruyendo el documento.
   - **Regla:** En todo `@media print` de Tailwind para presentaciones 16:9 panorámicas, es **obligatorio forzar las reglas explícitas de grid** sin prefijo de breakpoint:
     ```css
     @media print {
         .grid { display: grid !important; }
         .grid-cols-12 {
             display: grid !important;
             grid-template-columns: repeat(12, minmax(0, 1fr)) !important;
         }
         .col-span-6, .lg\:col-span-6 { grid-column: span 6 / span 6 !important; }
         .col-span-7, .lg\:col-span-7 { grid-column: span 7 / span 7 !important; }
         .col-span-5, .lg\:col-span-5 { grid-column: span 5 / span 5 !important; }
         .grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
         .grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; }
     }
     ```

---

## 2. Acciones Realizadas & Estado Final

1. **Rollback Total de la Regresión:**
   - Se descartaron al 100% las "mejoras" sugeridas por EGM.
   - Se restauró el layout original de V2 en [Auto-Glass-Executive-Pitch-V2/index.html](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V2/index.html): limpio, centrado, geométricamente armónico y altamente legible.
2. **Blindaje del Pipeline de Exportación PDF:**
   - Inyección de las reglas CSS de anulación de grid en `@media print`.
   - Altura de impresión calibrada a `height: 8.85in !important; max-height: 8.85in !important;` con `.slide:last-of-type { break-after: avoid !important; }` para erradicar páginas en blanco intermedias.
   - Recompilación exitosa del PDF en 2 páginas exactas (1.63 MB): [Auto_Glass_Executive_Pitch_V2_Telat.pdf](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V2/Auto_Glass_Executive_Pitch_V2_Telat.pdf).
3. **Registro en Bóveda Central:**
   - La propuesta V2 (Dark 3D 2-Slide Punch) y la propuesta V1 (4 Slides Clásica) conviven en la bóveda de presentaciones ejecutivas (`index.html`).
