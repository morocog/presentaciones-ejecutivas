# Solución Forense & Lecciones Aprendidas: Fracaso de EGM en Diseño UI/UX y Blindaje de Renderizado PDF 16:9

**Fecha:** 2026-11-02  
**Repositorio:** `presentaciones-ejecutivas`  
**Autor:** Ricardo García (Subdirector de Operaciones / IT & Ops Leader) / Antigravity Assistant  
**Módulos Afectados:** `01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V2`, `01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V3`, `00-Executive-Decks-EN`, `@media print`

---

## 1. Problema Raíz & Diagnóstico del Fallo

Durante el desarrollo de la propuesta comercial ejecutiva para el sector de cristales automotrices en EE. UU. (dirigida a C-Levels como Safelite y Gerber) y la consolidación de los 4 decks ejecutivos en inglés (`00-Executive-Decks-EN`), se identificaron y resolvieron 4 riesgos estructurales de diseño y compilación PDF:

### Las 4 Fallas Críticas Identificadas:

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

4. **Texto Crudo de Ligaduras por Fuentes de Iconos CDN en Chromium Headless (`.woff2` Local Obligatorio):**
   - **Causa:** Al compilar PDFs con `chrome.exe --headless=new --print-to-pdf`, las hojas de estilo remotas de Google Material Icons / Material Symbols (`fonts.googleapis.com`) sufren condiciones de carrera de red (`font-display` asíncrono) o contienen nombres de ligaduras inexistentes en la familia clásica (`shield_lock`, `target`).
   - **Efecto:** El PDF exportado imprime el texto literal de la ligadura (`trending_up`, `verified_user`, `shield_lock`) desbordando las cajas de iconos.
   - **Regla:** Empaquetar siempre localmente `material-icons.woff2` y `material-symbols.woff2` en `assets/fonts/` con `@font-face { font-display: block; }` y validar que cada ligadura exista en el mapa oficial de codepoints antes de exportar.

---

## 2. Acciones Realizadas & Estado Final

1. **Rollback Total de la Regresión y Lanzamiento de V3:**
   - Se descartaron al 100% las "mejoras" sugeridas por EGM y se restauró el layout original de V2 en [Auto-Glass-Executive-Pitch-V2/index.html](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V2/index.html), además de construir la versión V3 de dos horizontes en [Auto-Glass-Executive-Pitch-V3/index.html](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V3/index.html).
2. **Consolidación de los 4 Executive Decks en Inglés (`00-Executive-Decks-EN`):**
   - Estandarización de `01-Telat-AI-Solutions`, `02-Operations-Driven-by-Intelligence`, `03-Technology-Differentiators` y `04-Commercial-Capabilities-Deck` con las 4 láminas estructurales de cierre (**SS1:** Mapa de 4 Sedes Binacionales; **SS2:** 9 Certificaciones con logotipos vectoriales; **SS3:** Gobernanza Operativa; **SS4:** Liderazgo de Mauricio Cruz como Operations Director) y fuentes `.woff2` locales.
3. **Blindaje del Pipeline de Exportación PDF:**
   - Inyección de las reglas CSS de anulación de grid en `@media print` y empaquetado local `.woff2` con `font-display: block`.

