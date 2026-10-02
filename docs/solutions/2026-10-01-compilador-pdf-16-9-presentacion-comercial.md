# 🏛️ Ficha Técnica: Compilación de Presentación Comercial en PDF HD Panorámico (16:9)

**Fecha:** 2026-10-01  
**Autor:** Ricardo García / Antigravity IDE  
**Repositorio:** `presentaciones-ejecutivas`  
**Clasificación:** UI/UX, Impresión & Automatización  

---

## 1. Contexto y Síntomas

Para la acreditación de objetivos trimestrales institucionales, se requería exportar a formato PDF la **Presentación Comercial Macro de Telat Group** (`Presentacion-Comercial-Telat`), diseñada originalmente como una Single Page Application (SPA) web interactiva de pantalla completa (`100vh`, `100vw`, `overflow: hidden`). 

Al intentar imprimir directamente una SPA interactiva con los navegadores tradicionales se presentaban los siguientes defectos críticos:
1. **Pérdida de Diapositivas:** Únicamente se renderizaba la primera diapositiva activa, o las 10 diapositivas se superponían en una sola página rota debido a `position: absolute; inset: 0;`.
2. **Controles Flotantes Indeseados:** Los botones de navegación (`<` / `>`), el menú hamburguesa, el drawer y la barra superior de progreso aparecían sobre el contenido impreso.
3. **Casos Ocultos en Pestañas (Slide 5):** De los 6 casos de éxito operativos, 5 permanecían ocultos tras botones de pestañas interactivas, imposibles de consultar en un PDF estático.
4. **Cajas Negras en Videos:** Los videos enlazados vía iframe (Vimeo) renderizaban como rectángulos negros vacíos en motores de impresión headless.
5. **Colapso de Cuadrículas en Impresión:** Las clases de Tailwind basadas en breakpoints (`lg:grid-cols-12`, `md:grid-cols-3`) no se activaban en el contexto `@media print` de Chromium, apilando los elementos verticalmente y desbordando la página.

---

## 2. Causa Raíz

- Ausencia de reglas especializadas `@media print` calibradas para el tamaño físico de lámina panorámica (`16in 9in`).
- Dependencia de interactividad JavaScript en pantalla para acceder a contenido comercial crítico (pestañas y videos).
- Comportamiento de los navegadores Chromium en modo de impresión, donde los media queries de ancho de pantalla (`min-width`) pueden ignorarse a menos que se fuerce la propiedad CSS `grid-template-columns` directamente en `@media print`.

---

## 3. Solución Implementada

### A. Reestructuración de Casos de Éxito en 2 Láminas Horizontales (3 y 3)
Se desacopló la diapositiva 5 en dos láminas consecutivas ejecutivas:
- **Slide 5 (Casos de Éxito I):** Casos 1, 2 y 3 (Telecomunicaciones USA, E-Commerce Autos y Videovigilancia Inteligente) distribuidos en una cuadrícula de 3 columnas horizontales.
- **Slide 6 (Casos de Éxito II):** Casos 4, 5 y 6 (Pedidos Estacionales, Personalización Omnicanal y Autopartes USA) en 3 columnas horizontales.
- Cada tarjeta conserva íntegramente: Título, Badge de especialidad, Contexto, Proceso Manual Anterior (caja roja), Proceso Automatizado (caja verde) y sus 2 KPIs de impacto con antes y después (`14 min ➔ 3 min`, etc.).

### B. Arquitectura CSS `@media print` Panorámica (16:9)
- **Tamaño de Página Estricto:** `@page { size: 16in 9in; margin: 0; }` (proporción 1.777:1 nativa).
- **Flujo Secuencial:** Cada slide tiene `height: 9in; width: 16in; page-break-after: always; break-after: page; break-inside: avoid; display: flex; align-items: center; justify-content: center;`.
- **Fidelidad Cromática:** `-webkit-print-color-adjust: exact; print-color-adjust: exact;`.
- **Cabecera Institucional Impresa:** Inyección de logotipo oficial Telat (`.slide::before`) y cintillo corporativo en `#3284C6` (`.slide::after`) en cada página.
- **Forzado de Grids:** Reglas CSS forzadas en print para `.grid-cols-2`, `.grid-cols-3` y `.lg:grid-cols-12`, asegurando que el contenido mantenga sus columnas lado a lado sin apilarse.

### C. Fallback Visual HD para Videos (Slide 2, 3 y 4)
Se implementaron tarjetas mockup con gradientes oscuros y micro-datos (`print-mockup-fallback`) para reemplazar los iframes de Vimeo en impresión:
- **Slide 2 (Reclutamiento):** Simulador IA (Precisión 98.4%, Certificación CEFR C1).
- **Slide 3 (Copiloto IA):** Asistente en Vivo (Latencia <350ms, Precisión 99.2%).
- **Slide 4 (Auditoría QA):** Motor QA 100% (Cobertura 100% llamadas, Scorecard Automático).

### D. Script Automatizado de Compilación (`scripts/export_pdf.ps1`)
Se automatizó la generación con Google Chrome en modo Headless (`--headless=new`, `--no-pdf-header-footer`, `--run-all-compositor-stages-before-draw`, `--virtual-time-budget=3000`).

---

## 4. Anti-Patrones y Prohibiciones

1. **PROHIBIDO:** Usar librerías de rasterización como `html2canvas` o `html2pdf.js` para presentaciones comerciales con texto largo; genera PDFs pesados, borrosos y con texto no seleccionable.
2. **PROHIBIDO:** Omitir el forzado de cuadrículas en `@media print` asumiendo que los breakpoints de Tailwind (`md:`, `lg:`) se aplicarán automáticamente.
3. **PROHIBIDO:** Dejar iframes de video sin fallbacks estáticos de impresión, lo que produce recuadros negros en el PDF.

---

## 5. Verificación & Evidencia

- [x] Generado archivo `Presentacion_Comercial_Telat_Group.pdf` (2.76 MB).
- [x] Verificado el número de páginas: Exactamente **11 páginas** vectoriales.
- [x] Verificadas las dimensiones físicas: `MediaBox [0 0 1152 648]` (16 pulgadas de ancho por 9 pulgadas de alto, 16:9 perfecto).
- [x] Inspección visual realizada página por página con captura de pantalla y OCR:
  - Portada con isotipo central Telat.
  - El Problema con tarjetas de dolor y plataforma inteligente.
  - Reclutamiento, Copiloto y QA con mockups tecnológicos nítidos.
  - Casos de Éxito I y II en 3 columnas espaciosas sin cortes ni desbordes.
  - Quién es Telat con gráfica de talento 2005-2026 y Mapa de Hubs (CDMX, Juárez, El Paso).
  - Certificaciones ISO, PCI-DSS, ESR y premios IMT.
  - Metodología de 4 pasos (Diagnóstico, Diseño, Implementación, Optimización).
  - Hoja de Cierre y Perfilamiento Operativo con datos de contacto comercial.
- [x] Script `export_pdf.ps1` validado y documentado.
- [x] `docs/PENDIENTES.md` actualizado.
