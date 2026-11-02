# Design System & Heurísticas de Diseño: Versión 3 (Impeccable Craft)

Esta versión experimental (V3) implementa las heurísticas de diseño editorial y anti-"AI Slop" del repositorio [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) (Paul Bakaus), adaptadas al branding corporativo oficial de **Telat Group** para presentaciones ejecutivas 16:9 dirigidas a directores C-Suite de cadenas de auto glass en EE. UU.

---

## 🎯 Modo de Superficie: *Persuade* (C-Suite Sales Deck)

En el marco de Impeccable, una presentación ejecutiva comercial opera bajo el modo **Persuade**:
- **Objetivo:** Capturar la convicción del decisor (CRO, VP de Operaciones, Dueño de Franquicia) en menos de 10 segundos.
- **Principio:** El diseño no es un adorno superfluo ni una herramienta operativa; el diseño **es el producto** y la primera prueba tangible de la excelencia operativa de Telat.

---

## 🚫 Erradicación de Clichés Visuales de IA ("AI Slop" & Craft Floor)

| Patrón Descartado (V2 o EGM) | Corrección Aplicada en V3 (Impeccable) | Justificación Técnica |
| :--- | :--- | :--- |
| **Kickers / Eyebrow Pill Badges:** Etiquetas redondeadas sobre los títulos (`WHERE AUTO GLASS CHAINS BLEED MARGIN`). | **Línea de contexto tipográfica sobria:** Marcador discreto `font-mono text-[0.68rem] text-telatOrange` con punto geométrico sin borde hinchado. | Impeccable prohíbe los kickers/eyebrows artificiales; el encabezado debe tener la autoridad para hablar por sí mismo sin "muletas". |
| **Cajas anidadas (Card-in-card):** Tarjetas dentro de tarjetas para cada punto de dolor. | **Micro-cuadrícula integrada:** 3 columnas de tensión operativa con bordes sutiles de 1px (`border-white/10`) y ritmo vertical armónico. | Evita el efecto claustrofóbico de marcos redundantes y jerarquía visual confusa. |
| **Halos y resplandores falsos (Neon Blobs):** Sombras radiales borrosas de color puro (`blur-xl` en esquinas). | **Profundidad física direccional:** Sombreado realista (`0 16px 36px -10px rgba(0,0,0,0.65)`) con micro-iluminación superior (`inset 0 1px 0 rgba(255,255,255,0.09)`). | La profundidad real comunica solidez y sobriedad ejecutiva; los halos de neón lucen como plantilla de hackathon. |
| **Rayas laterales gruesas (`border-l-4`):** Barras gruesas de colores en el lateral de cada paso. | **Filas de flujo horizontal limpias:** Indicador numérico circular sutil (`01`, `02`, `03`, `04`) y fondo reactivo suave (`craft-process-row`). | Las líneas laterales de más de 1px son uno de los atajos más comunes de IA para disfrazar falta de composición. |
| **Texto con gradientes cromáticos:** Títulos con degradados de celeste a naranja. | **Contraste tipográfico absoluto:** Blanco de alta luminosidad (`#FFFFFF`), pesos deliberados (`font-extrabold`) y acentos de color estratégicos. | La jerarquía real proviene de la escala y peso del tipo, no de gradientes distractores. |

---

## 🎨 Paleta y Tokens de Color

- **Fondo Primario (Canvas):** `#080A10` (Negro óptico profundo de alta densidad).
- **Superficie de Tarjetas (Cards):** `#10131E` (Gris azulado oscuro con micro-textura).
- **Bordes y Divisores:** `rgba(255, 255, 255, 0.08)` (1px de precisión).
- **Acentos Telat:**
  - Celeste Institucional: `#3284C6` (Datos de conversión y credenciales).
  - Naranja Enérgico: `#EB5B27` (Puntos de tensión, llamadas a la acción, piloto).
  - Amarillo Canario: `#FECA66` (Precisión NAGS y objeciones de costo).
  - Verde Esmeralda: `#10B981` (Resultados de ventas, estatus en vivo y escalabilidad).

---

## 🖨️ Blindaje de Exportación PDF 16:9

Se preservan intactas las reglas `@media print` en [index.html](file:///c:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Auto-Glass-Executive-Pitch-V3/index.html):
- Tamaño de página exacto: `16in 9in` (1920x1080 px).
- Forzado de cuadrícula CSS en motor de impresión (`.grid-cols-12 { display: grid !important; }`).
- Compilación automatizada mediante `scripts/export_auto_glass_v3_pdf.ps1`.
- Resultado verificado: **Exactamente 2 páginas en PDF (1.03 MB)** con columnas paralelas y alineación milimétrica.
