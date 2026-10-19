const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const certDir = path.join(__dirname, '..', '02-Direccion-y-Estrategia', 'assets', 'certificaciones');
const svgInputPath = path.join(certDir, 'cert_modelo_cic.svg');
let svgContent = fs.readFileSync(svgInputPath, 'utf8');

// The SVG has specific line ranges for each section:
// Lines 2-35 & 65: "ACREDITACIÓN EN" -> #475569
// Lines 36-45: "VERSIÓN 3.0" -> #6B21A8 (accent)
// Lines 46-51: "MODELO" -> #1E1B4B (deep navy/indigo)
// Lines 52-60: "GLOBAL CIC" -> #6B21A8 (IMT purple)
// Lines 61-64: Isotype curves -> #7C3AED and #9333EA

const lines = svgContent.split(/\r?\n/);

for (let i = 0; i < lines.length; i++) {
    const lineNum = i + 1;
    if (lineNum >= 2 && lineNum <= 35) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#475569"');
    } else if (lineNum >= 36 && lineNum <= 45) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#6B21A8"');
    } else if (lineNum >= 46 && lineNum <= 51) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#1E1B4B"');
    } else if (lineNum >= 52 && lineNum <= 60) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#6B21A8"');
    } else if (lineNum === 61 || lineNum === 63) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#7C3AED"');
    } else if (lineNum === 62 || lineNum === 64) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#9333EA"');
    } else if (lineNum === 65) {
        lines[i] = lines[i].replace('fill="white"', 'fill="#475569"');
    }
}

const coloredSvgContent = lines.join('\n');
fs.writeFileSync(svgInputPath, coloredSvgContent, 'utf8');
console.log('Updated cert_modelo_cic.svg with official corporate colors.');

// Create a standalone HTML page to render the SVG with high DPI
const htmlPath = path.join(certDir, 'render_cic.html');
const pngOutputPath = path.join(certDir, 'cert_modelo_cic.png');

const htmlContent = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body {
    margin: 0;
    padding: 0;
    background: transparent !important;
    overflow: hidden;
  }
  .container {
    width: 612px;
    height: 199px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: transparent !important;
  }
  svg {
    width: 612px;
    height: 199px;
  }
</style>
</head>
<body>
  <div class="container">
    ${coloredSvgContent}
  </div>
</body>
</html>`;

fs.writeFileSync(htmlPath, htmlContent, 'utf8');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const htmlUri = 'file:///' + htmlPath.replace(/\\/g, '/');

const cmd = `"${chromePath}" --headless=new --screenshot="${pngOutputPath}" --window-size=612,199 --default-background-color=00000000 --hide-scrollbars "${htmlUri}"`;
console.log('Running:', cmd);
execSync(cmd);

if (fs.existsSync(pngOutputPath)) {
    console.log('SUCCESS: Generated cert_modelo_cic.png size:', fs.statSync(pngOutputPath).size);
} else {
    console.error('ERROR: Failed to generate PNG');
}

// Clean up temporary HTML
if (fs.existsSync(htmlPath)) {
    fs.unlinkSync(htmlPath);
}
