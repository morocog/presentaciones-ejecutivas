const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');

const repoDir = 'c:\\Users\\SDVP\\Documents\\GitHub\\presentaciones-ejecutivas\\01-Propuestas-Comerciales\\UVC-Unlimited-Vacation-Club';
const slidesHdDir = path.join(repoDir, 'assets', 'slides_hd');
const outputPptx = path.join(repoDir, 'Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pptx');
const downloadsPptx = 'C:\\Users\\SDVP\\Downloads\\Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pptx';

async function buildHybridPresentation() {
  console.log('Building Executive Hybrid PPTX for UVC...');
  const pptx = new pptxgen();

  // 16:9 Full HD Presentation
  pptx.layout = 'LAYOUT_16x9'; // 10 x 5.625 inches (or pptx default 16:9 is 13.33 x 7.5 inches)
  // Let's set custom width/height to match 16:9 standard: 13.333 x 7.5 inches
  pptx.defineLayout({ name: 'FHD_16_9', width: 13.333, height: 7.5 });
  pptx.layout = 'FHD_16_9';

  const W = 13.333;
  const H = 7.5;

  for (let i = 1; i <= 11; i++) {
    const slide = pptx.addSlide();
    const bgImage = path.join(slidesHdDir, `slide_${i}.png`);

    // 1. Set Full HD Background Image (Exact 1:1 Pixel Match with PDF)
    slide.addImage({
      path: bgImage,
      x: 0,
      y: 0,
      w: W,
      h: H
    });

    // 2. Overlay Native Editable Fields on Specific Customizable Slides

    // --- SLIDE 1: PORTADA ---
    if (i === 1) {
      // Subtitle / Prospect Name (Editable Box overlaid on subtitle)
      // Coordinates mapped to 1920x1080 -> 13.333 x 7.5
      slide.addText('Propuesta de Servicios y Solución Integral BPO', {
        x: 1.38,
        y: 4.05,
        w: 10.5,
        h: 0.5,
        fontSize: 22,
        fontFace: 'Arial',
        bold: true,
        color: 'EB5B27',
        fill: { color: '0F172A', transparency: 100 }
      });

      slide.addText('Preparada para: Unlimited Vacation Club (UVC)', {
        x: 1.38,
        y: 4.60,
        w: 10.5,
        h: 0.45,
        fontSize: 18,
        fontFace: 'Arial',
        bold: true,
        color: 'F8FAFC',
        fill: { color: '0F172A', transparency: 100 }
      });
    }

    // --- SLIDE 7: SEGURIDAD PCI DSS ---
    if (i === 7) {
      // Editable client banner headline
      slide.addText('Protección Total en Pagos y Datos de Socios UVC', {
        x: 1.85,
        y: 2.10,
        w: 8.5,
        h: 0.45,
        fontSize: 20,
        fontFace: 'Arial',
        bold: true,
        color: 'FFFFFF',
        fill: { color: '0F172A', transparency: 100 }
      });
    }

    // --- SLIDE 9: ¿POR QUÉ TELAT? ---
    if (i === 9) {
      // ROI Card Description (Client specific)
      slide.addText('Nos adaptamos a la escala de Unlimited Vacation Club maximizando rentabilidad.', {
        x: 10.15,
        y: 4.10,
        w: 2.8,
        h: 0.65,
        fontSize: 10,
        fontFace: 'Arial',
        color: '475569',
        fill: { color: 'FFFFFF', transparency: 100 }
      });
    }

    // --- SLIDE 10: PROPUESTA ECONÓMICA (MAX EDITABILITY) ---
    if (i === 10) {
      // 1. Hourly Rate (Agent)
      slide.addText('$17.30', {
        x: 0.85,
        y: 1.85,
        w: 2.2,
        h: 0.7,
        fontSize: 34,
        fontFace: 'Arial',
        bold: true,
        color: '0F172A',
        fill: { color: 'FFFFFF', transparency: 100 }
      });

      // 2. Training Rate
      slide.addText('$15.00', {
        x: 3.85,
        y: 1.85,
        w: 2.2,
        h: 0.7,
        fontSize: 34,
        fontFace: 'Arial',
        bold: true,
        color: '0F172A',
        fill: { color: 'FFFFFF', transparency: 100 }
      });

      // 3. Monthly Budget
      slide.addText('$350,575', {
        x: 6.85,
        y: 1.85,
        w: 2.5,
        h: 0.7,
        fontSize: 30,
        fontFace: 'Arial',
        bold: true,
        color: 'FDE047',
        fill: { color: '0F172A', transparency: 100 }
      });

      // 4. Annual Budget
      slide.addText('$4,206,889', {
        x: 9.85,
        y: 1.85,
        w: 2.6,
        h: 0.7,
        fontSize: 30,
        fontFace: 'Arial',
        bold: true,
        color: '38BDF8',
        fill: { color: '0F172A', transparency: 100 }
      });

      // 5. Fiscal Strip Text (Full text easily editable)
      slide.addText([
        { text: 'Condiciones Fiscales: ', options: { bold: true, color: 'FDE047' } },
        { text: 'Precios expresados en USD antes de impuestos. Aplica IVA (16%) únicamente para facturación en territorio mexicano; facturación corporativa en EE. UU. libre de impuestos trasladados.', options: { color: 'F8FAFC' } }
      ], {
        x: 1.5,
        y: 6.42,
        w: 11.2,
        h: 0.55,
        fontSize: 12,
        fontFace: 'Arial',
        fill: { color: '0F172A', transparency: 100 }
      });
    }

    // --- SLIDE 11: CIERRE EJECUTIVO ---
    if (i === 11) {
      // Luis Cortina - Apoderado Legal
      slide.addText('Luis Cortina', {
        x: 7.5,
        y: 4.85,
        w: 5.0,
        h: 0.45,
        fontSize: 22,
        fontFace: 'Arial',
        bold: true,
        color: '0F172A',
        fill: { color: 'FFFFFF', transparency: 100 }
      });

      slide.addText('Apoderado Legal · Telat Group', {
        x: 7.5,
        y: 5.30,
        w: 5.0,
        h: 0.35,
        fontSize: 14,
        fontFace: 'Arial',
        bold: true,
        color: 'EB5B27',
        fill: { color: 'FFFFFF', transparency: 100 }
      });
    }
  }

  // Save PPTX in Repo
  await pptx.writeFile({ fileName: outputPptx });
  console.log('Hybrid PPTX saved in repo:', outputPptx);

  // Copy to Downloads
  try {
    fs.copyFileSync(outputPptx, downloadsPptx);
    console.log('Hybrid PPTX copied to Downloads:', downloadsPptx);
  } catch (err) {
    console.warn('Could not copy directly to Downloads (might be open):', err.message);
    const altPptx = path.join('C:\\Users\\SDVP\\Downloads', 'Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat_v2.pptx');
    fs.copyFileSync(outputPptx, altPptx);
    console.log('Copied as fallback to Downloads:', altPptx);
  }
}

buildHybridPresentation().then(() => {
  console.log('Complete process finished successfully!');
}).catch(err => {
  console.error('Fatal error building hybrid PPTX:', err);
});

