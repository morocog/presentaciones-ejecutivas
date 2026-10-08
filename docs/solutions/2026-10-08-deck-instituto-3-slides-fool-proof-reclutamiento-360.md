# 📘 Ficha Técnica: Deck de 3 Slides con Portada Fool Proof (6 Pilares) y Módulo de Reclutamiento 360° para el Instituto

**Fecha:** 2026-10-08  
**Repositorio:** `presentaciones-ejecutivas`  
**Ubicación:** `01-Propuestas-Comerciales/Instituto-1-Infonatel/` (`index.html` y `Diferenciadores_Tecnologicos_Instituto_Telat.pdf`)  
**Autor:** Ricardo García / Antigravity IDE  
**Estatus:** ✅ Implementado y validado en PDF HD (3 páginas vectoriales panorámicas 16:9)  

---

## 1. Contexto y Requerimiento Directivo

Tras la validación previa por el Director de Operaciones (Mauricio Cruz), el Director General de Telat Group, **Luis Cortina**, solicitó una reestructuración de la presentación comercial para el **Instituto**:
1. **Lámina 1 "Fool Proof" (A prueba de fallas):** Una primera diapositiva de alto impacto, limpia y sintética, sin bloques densos de texto ni detalle excesivo, que muestre de un vistazo las **6 capacidades y diferenciadores nucleares de Telat** en una cuadrícula simétrica 3x2.
2. **Incorporación Formal del Ecosistema de Reclutamiento & Selección:** Integrar la suite tecnológica de atracción y filtrado de talento desarrollada en el repositorio [`talent-ecosystem`](file:///c:/Users/SDVP/Documents/GitHub/talent-ecosystem/), destacando las 4 herramientas clave:
   - *Audio Triage con IA:* Análisis de voz, dicción, modulación y templanza emocional.
   - *Computer Skills:* Evaluación práctica de velocidad de captura (WPM), precisión y agilidad en navegación de sistemas.
   - *English Assessment:* Evaluación en 4 habilidades del idioma (Speaking, Listening, Reading, Writing), ratificando la solvencia bilingüe de Telat frente al Instituto ("hay que demostrar que sí lo tenemos").
   - *Dashboard 360°:* Expediente unificado del candidato con trazabilidad integral de resultados.
3. **Estructura en 3 Láminas (Opción A):**
   - **Slide 1:** Visión Ejecutiva *Fool Proof* · Los 6 Pilares de Valor (cuadrícula 3x2).
   - **Slide 2:** Zoom-In Técnico 1 · Tecnología de Piso en Vivo y Privacidad PII (Asistente en vivo, Cierre rápido ≤20s, Ciberseguridad PII).
   - **Slide 3:** Zoom-In Técnico 2 · Selección de Talento 360°, Calidad con IA y Garantía de Despliegue Masivo (0 a 450 agentes).

---

## 2. Implementación Técnica en `index.html`

### 2.1 CSS `@media print`
- Se forzó el comportamiento en Chromium headless agregando:
  ```css
  .grid-rows-2 { grid-template-rows: repeat(2, minmax(0, 1fr)) !important; }
  ```
  Esto garantiza que la cuadrícula 3x2 de la portada divida el lienzo vertical exactamente al 50% sin desbordamientos de página.

### 2.2 Slide 1: Portada "Fool Proof" (Macro-Tarjetas de Alto Impacto Ejecutivo)
- **Cero verborrea ni párrafos explicativos:** Eliminados los párrafos descriptivos densos que duplicaban el contenido técnico de las láminas 2 y 3.
- **Tipografía y números de gran formato:** Títulos de `text-[1.38rem]` (`font-bold font-subheading`), subtítulos de una sola línea (`text-[13px] font-medium`) y cajas de impacto estilo botón con métricas gigantes `text-4xl`:
  1. *1 · Operación en Vivo:* **Asistente Inteligente en Pantalla** (`< 2s` · Sugerencia en Pantalla).
  2. *2 · Cierre de Expediente:* **Cierre de Llamada en Segundos** (`≤ 20s` · Wrap-up Automatizado).
  3. *3 · Ciberseguridad & PII:* **Privacidad Dinámica de Datos PII** (`100%` · Enmascaramiento PII).
  4. *4 · Atracción y Talento:* **Evaluación de Talento 360°** (`4 Filtros` · Suite Integral de Talento).
  5. *5 · Calidad Continua:* **Auditoría Continua de Calidad** (`Hasta 100%` · Supervisión con IA).
  6. *6 · Capacidad y Despliegue:* **Garantía Total de Despliegue** (`0 a 450` · Agentes en Despliegue).

### 2.3 Cintillos Inferiores: Opción A (Catálogo Completo de 9 Certificaciones)
- Se implementó la **Opción A** en la Línea 2 de los cintillos de los Slides 1, 2 y 3:
  - `ISO 9001` (Calidad)
  - `ISO 18295-1` (Contact Centers)
  - `Modelo Global CIC v3.0` (Customer Interaction Center / Interacción con Clientes) ⭐ *Acreditada hoy*
  - `ISO 27001` (Ciberseguridad)
  - `PCI-DSS v4.0 (PSI)` (Seguridad de Medios de Pago)
  - `ISO 20000-1` (Gestión TI)
  - `ISO 22301` (Continuidad del Negocio)
  - `ISO 37001` (Antisoborno)
  - `Distintivo ESR 2026` (Empresa Socialmente Responsable)
- Tira horizontal fluida con micro-píldoras (`text-[9.5px] py-0.5 px-2`), sin saltos de línea ni interferencia en el espacio vertical.

### 2.4 Slide 2: Zoom-In de Operación de Piso
- Re-etiquetado a `id="slide-2" data-slide="2"`.
- Conserva el detalle técnico en 3 columnas de Asistente en Línea, Tipificación & Cierre en ≤20s y Privacidad & Protección PII.

### 2.5 Slide 3: Zoom-In de Talento, Calidad y Despliegue
- Re-etiquetado a `id="slide-3" data-slide="3"`.
- Grid de 3 columnas de ancho homogéneo:
  - *Columna 1 (Talento):* Atracción y Evaluación Integral de Candidatos (con cuadrícula de los 4 módulos: Audio Triage IA, Computer Skills, English Assessment y Dashboard 360°, y métrica de 94.8% de retención).
  - *Columna 2 (Calidad):* Auditoría con IA: Cobertura Flexible de Hasta el 100% (rúbrica de 4 dimensiones, calificación 98.4/100 y apego +95%).
  - *Columna 3 (Despliegue):* Garantía de Despliegue: Desde 0 hasta 450 Agentes (3 fases secuenciales, WFM predictivo y 100% en Día 1).

### 2.6 Script de Navegación Interactivo
- Actualizado a `totalSlides = 3`, `slide-indicator: 1 / 3` y control hash para `#slide-1`, `#slide-2` y `#slide-3`.

---

## 3. Compilación y Validación de PDF

Se compiló mediante el script oficial `scripts/export_instituto_pdf.ps1`:
- **Comando:** `powershell -ExecutionPolicy Bypass -File "scripts/export_instituto_pdf.ps1"`
- **Resultado:**
  - Archivo: `01-Propuestas-Comerciales/Instituto-1-Infonatel/Diferenciadores_Tecnologicos_Instituto_Telat.pdf`
  - Tamaño: 1,237,097 bytes (~1.2 MB)
  - Páginas generadas: **3 páginas vectoriales perfectas** (confirmado mediante parser PDF).
