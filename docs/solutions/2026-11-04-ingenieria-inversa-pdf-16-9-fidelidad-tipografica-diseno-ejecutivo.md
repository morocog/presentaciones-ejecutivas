# Ficha Técnica & Metodología Forense: Ingeniería Inversa de PDFs 16:9, Fidelidad Tipográfica y Calibración Milimétrica

**Fecha:** 2026-11-04  
**Repositorio:** `presentaciones-ejecutivas`  
**Autor:** Ricardo García (Subdirector de Operaciones / IT & Ops Leader) / Antigravity Assistant  
**Módulos Afectados:** `00-Executive-Decks-ES`, `01-Soluciones-IA-Telat`, `02-Operaciones-Impulsadas-por-Inteligencia`, `04-Portafolio-Capacidades-Comerciales`, Pipeline de Exportación Chromium Headless

---

## 1. Problema Raíz & Diagnóstico de los Fallos

Al trasladar y replicar presentaciones ejecutivas de alto impacto visual desde un PDF de origen hacia código HTML reproducible (y su posterior re-exportación a PDF vectorial 16:9), se cometieron cuatro errores críticos que degradaron severamente la fidelidad estética:

### Los 4 Fallos Críticos Identificados:

1. **Aproximación "a ojo" y Alucinación Tipográfica:**
   - **Fallo:** En lugar de inspeccionar el archivo binario original, se asumieron tipografías genéricas y se forzó una fuente display pesada (`font-momo` / Impact) en el Deck 01 de IA.
   - **Consecuencia:** Cifras como "Hasta 100%", "Instantánea", "Tiempo real" y "28" se renderizaron como carteles de descuento o tabloides grotescos en vez de una interfaz SaaS minimalista y sofisticada.

2. **Empaste por Falso Engrosamiento (*Synthetic Bolding*):**
   - **Fallo:** En Deck 02 y Deck 04, los títulos usaban etiquetas `<h1>`, `<h2>` y `<h4>` combinadas con `font-momo` (Impact / Arial Black). Los navegadores aplican por omisión `font-weight: bold` a los encabezados en su hoja de estilos de agente de usuario.
   - **Consecuencia:** Dado que Impact ya posee un peso geométrico masivo, el motor Chromium ejecutó *synthetic bolding* (dibujar un contorno artificial de trazo alrededor del glifo), provocando que las letras colisionaran y se empastaran en un manchón negro ilegible.

3. **Colapso de Escala (El Síndrome del 50% de Espacio Vacío):**
   - **Fallo:** Se diseñó el HTML asumiendo un viewport estándar de escritorio web con clases de Tailwind pensadas para 16px base (`text-5xl` ~48px, `text-6xl` ~60px, párrafos a 18px).
   - **Consecuencia:** Al compilarse a PDF 16:9, el contenido quedaba diminuto y concentrado al centro, dejando casi la mitad de la diapositiva en blanco, mientras que el documento original llenaba holgadamente la pantalla de borde a borde con titulares de más de 100px.

4. **Desfase Espacial y Geométrico de Elementos Gráficos:**
   - **Fallo:** Los aros concéntricos decorativos (naranja y azul) se posicionaron centrados verticalmente (`top: 50%`), y las listas numeradas se diseñaron con pastillas grises y números oscuros.
   - **Consecuencia:** Ruptura de la identidad visual de la marca y discrepancia evidente con la versión en inglés, donde los aros están anclados a la esquina superior derecha y las listas tienen un aro naranja con índice naranja y titular en azul marino profundo.

---

## 2. Metodología Infalible de Ingeniería Inversa de PDFs (Protocolo SOTA)

Para replicar cualquier PDF del cual **no se disponga de código fuente HTML**, se establece el siguiente protocolo algorítmico obligatorio ejecutado mediante scripts de Node.js sobre el binario:

### Paso 1: Derivación del Lienzo Canónico mediante `/MediaBox`
En un PDF de Skia/Chromium, la caja de medios se declara en puntos tipográficos (`1 pt = 1/72 pulgada`):
$$\text{MediaBox} = [0\quad 0\quad 1440\quad 810]$$

Sabiendo que el estándar web CSS opera a 96 DPI:
$$\text{Ancho en px} = 1440\text{ pt} \times \frac{96\text{ px/in}}{72\text{ pt/in}} = 1920\text{ px}$$
$$\text{Alto en px} = 810\text{ pt} \times \frac{96\text{ px/in}}{72\text{ pt/in}} = 1080\text{ px}$$

> **Regla de Oro:** Todo PDF con `MediaBox [0 0 1440 810]` fue maquetado exactamente sobre un lienzo base de **1920 × 1080 px** a escala 1:1.

### Paso 2: Descompresión de Flujos de Contenido (`zlib.inflateSync`)
El contenido de cada lámina reside comprimido con FlateDecode. Con Node.js se descomprimen los bloques `stream ... endstream`:
```javascript
const fs = require('fs');
const zlib = require('zlib');
const buf = fs.readFileSync('documento.pdf');

// Búsqueda de streams de página y descompresión con zlib
let pos = 0;
while ((pos = buf.indexOf('stream', pos)) !== -1) {
  let start = pos + 6;
  if (buf[start] === 13 && buf[start+1] === 10) start += 2;
  else if (buf[start] === 10) start += 1;
  let end = buf.indexOf('endstream', start);
  try {
    const uncompressed = zlib.inflateSync(buf.slice(start, end)).toString('latin1');
    // Inspección de operadores de texto BT...ET y transformaciones cm/Do
  } catch(e) {}
  pos = end + 9;
}
```

### Paso 3: Identificación de Fuentes Reales embebidas en el PDF
Consultando `/Type /Font` y `/BaseFont`, se extrae la familia auténtica sin conjeturas:
- `/BaseFont /AAAAAA+BricolageGrotesque96ptExtraBold-ExtraBold` -> **Bricolage Grotesque ExtraBold (800)**
- `/BaseFont /DAAAAA+BricolageGrotesque96ptExtraBold-Bold` -> **Bricolage Grotesque Bold (700)**
- `/BaseFont /CAAAAA+DMSans9pt-Bold` -> **DM Sans Bold (700)**
- `/BaseFont /BAAAAA+DMSans9pt-Regular` -> **DM Sans Regular (400)**

### Paso 4: Extracción de la Jerarquía Tipográfica Exacta en Píxeles (`Tf`)
Al analizar los operadores `/F... <size> Tf` de cada diapositiva:
- **Titulares colosales (Portada / Cierre):** `118 – 128 Tf` (118px a 128px).
- **Métricas numéricas destacadas:** `106 – 116 Tf` (106px a 116px).
- **Titulares de láminas de producto:** `80 – 84 Tf` (80px a 84px).
- **Titulares de láminas operativas ("Cómo funciona"):** `64 – 68 Tf` (64px a 68px).
- **Subtítulos de portada:** `36 – 40 Tf` (36px a 40px).
- **Párrafos descriptivos:** `32 – 34 Tf` (32px a 34px).
- **Títulos de pasos numerados:** `30 – 34 Tf` (30px a 34px).
- **Insignias y cápsulas:** `28 – 30 Tf` (28px a 30px).
- **Cuerpo de pasos y descripciones:** `24 – 26 Tf` (24px a 26px).
- **Pies de página / firmas corporativas:** `20 – 22 Tf` (20px a 22px).

### Paso 5: Extracción de Coordenadas Geométricas y Curvas Bézier (`m / c`)
Analizando las coordenadas de los vectores XForm en el PDF:
- El aro concéntrico naranja (`.9333 .3529 .1529 RG` = `#EB5B27`) tiene un rango de X de 1315 a 2145 y de Y de -225 a 605.
- Centro exacto: $X = \frac{1315 + 2145}{2} = 1730\text{ px}$, $Y = \frac{-225 + 605}{2} = 190\text{ px}$.
- Radio: $R = 415\text{ px}$, espesor de trazo $= 70\text{ px}$.
- Círculo sólido azul interior (`#2079C8`): Centro `(1730, 190)` con radio $R = 250\text{ px}$.
- **Conclusión:** Se plasma en un SVG directo sobre la esquina superior derecha:
  ```html
  <svg class="absolute top-0 right-0 w-[1920px] h-[1080px] pointer-events-none" viewBox="0 0 1920 1080" fill="none">
    <circle cx="1730" cy="190" r="415" stroke="#EB5B27" stroke-width="70" fill="none" opacity="0.95" />
    <circle cx="1730" cy="190" r="250" fill="#2079C8" opacity="0.95" />
  </svg>
  ```

### Paso 6: Extracción de la Paleta Cromática Exacta
- Azul marino corporativo (Fondo portada y cierre): `.0784 .1608 .3608 RG` -> **`#14295C`**
- Marfil cálido (Fondo de diapositivas internas): `.9647 .9569 .9412 RG` -> **`#F6F4F0`**
- Naranja corporativo Telat: `.9333 .3529 .1529 RG` -> **`#EB5B27`**
- Azul brillante corporativo: `.1255 .4745 .7843 RG` -> **`#2079C8`**

---

## 3. Blindaje Contra el Falso Engrosamiento (*Anti-Synthetic Bolding*)

Para evitar que fuentes display o robustas como `font-momo` (Impact / Arial Black) o `Bricolage Grotesque` colapsen en manchas de tinta negra ilegibles al colocarse dentro de encabezados HTML:

```css
@font-face {
  font-family: 'Momo Trust';
  src: local('Impact'), local('Arial Black');
  font-weight: normal; /* Declarar normal para que el navegador no aplique doble peso */
  font-display: swap;
}

.font-momo {
  font-family: 'Momo Trust', 'Impact', sans-serif;
  font-weight: normal !important;
  letter-spacing: -0.01em;
}

/* Neutralización obligatoria del default user-agent bolding en h1..h4 */
h1.font-momo, h2.font-momo, h3.font-momo, h4.font-momo, .font-momo {
  font-weight: normal !important;
}
```

---

## 4. Arquitectura de Pantalla y Pipeline de Exportación 16:9

Para conciliar la visualización interactiva en cualquier monitor (desde laptops 13" hasta monitores 4K) con la compilación milimétrica en Chromium:

1. **Estructura HTML (Lienzo Fijo 1920×1080):**
   ```html
   <div class="viewport-scaler">
     <section class="slide" id="slide-1">...</section>
     ...
   </div>
   ```

2. **Escalador Reactivo en JavaScript (Modo Pantalla):**
   ```javascript
   function fitToWindow() {
     const scaler = document.querySelector('.viewport-scaler');
     if (!scaler) return;
     const scale = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
     scaler.style.transform = `scale(${scale})`;
   }
   window.addEventListener('resize', fitToWindow);
   fitToWindow();
   ```

3. **Reglas Estrictas en `@media print` (Modo Impresión PDF):**
   ```css
   @media print {
     @page {
       size: 1920px 1080px;
       margin: 0;
     }
     html, body {
       width: 1920px !important;
       height: 1080px !important;
       background: #F6F4F0 !important;
       overflow: visible !important;
       display: block !important;
     }
     .viewport-scaler {
       transform: none !important;
       width: 1920px !important;
       height: auto !important;
       position: static !important;
       display: block !important;
     }
     .slide {
       display: flex !important;
       position: relative !important;
       width: 1920px !important;
       height: 1080px !important;
       page-break-after: always !important;
       break-after: page !important;
       box-sizing: border-box !important;
       padding: 96px 120px 64px 120px !important;
       overflow: hidden !important;
     }
   }
   ```

4. **Script de Compilación CLI:**
   ```powershell
   chrome.exe --headless=new --disable-gpu --no-pdf-header-footer `
              --run-all-compositor-stages-before-draw --virtual-time-budget=5000 `
              --print-to-pdf="salida.pdf" "file:///ruta/index.html"
   ```

---

## 5. Resumen de Aciertos vs. Errores para Proyectos Futuros

| Factor | Error Común (Evitar) | Acierto Demostrado (Aplicar) |
| :--- | :--- | :--- |
| **Tipografía** | Usar fuentes genéricas o inventar pesos display como `Impact` en software SaaS. | Inspeccionar `/BaseFont` en el PDF original. En este caso: `Bricolage Grotesque` y `DM Sans`. |
| **Pesos en Títulos** | Dejar que `<h1>` o `<h2>` apliquen negrita automática a fuentes display pesadas. | Forzar `font-weight: normal !important;` en encabezados display para evitar *synthetic bolding*. |
| **Dimensiones** | Diseñar con tamaños web estándar (`text-5xl` ~48px) dejando la mitad del slide vacío. | Trabajar sobre lienzo canónico de 1920×1080 px con titulares de 80–124 px y métricas de 106–116 px. |
| **Geometría** | Alinear vectores u ornamentos al centro por intuición. | Calcular centro y radios mediante las coordenadas `m/c` del PDF: `(1730, 190)`, `r=415` y `r=250`. |
| **Listas de Pasos** | Pastillas genéricas grises con números oscuros. | Círculo con borde `#EB5B27`, número interior naranja `#EB5B27` y título en azul marino `#14295C`. |
| **Visualización** | Desbordar la pantalla en monitores pequeños o colapsar en impresión. | `viewport-scaler` reactivo en navegador y `@page { size: 1920px 1080px; }` con `transform: none` en impresión. |
