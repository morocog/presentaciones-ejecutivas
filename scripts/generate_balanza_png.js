const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const svgCode = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="400" height="400">
  <g fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <line x1="26" y1="88" x2="74" y2="88" stroke-width="6.5" />
    <line x1="38" y1="81" x2="62" y2="81" stroke-width="5" />
    <line x1="50" y1="81" x2="50" y2="20" stroke-width="5.5" />
    <circle cx="50" cy="18" r="4.5" fill="#FFFFFF" stroke="none" />
    <line x1="16" y1="22" x2="84" y2="22" stroke-width="5.5" />
    <line x1="22" y1="22" x2="10" y2="54" stroke-width="3" />
    <line x1="22" y1="22" x2="34" y2="54" stroke-width="3" />
    <path d="M 10 54 Q 22 72 34 54 Z" fill="#FFFFFF" fill-opacity="0.3" stroke-width="4.5" />
    <line x1="78" y1="22" x2="66" y2="54" stroke-width="3" />
    <line x1="78" y1="22" x2="90" y2="54" stroke-width="3" />
    <path d="M 66 54 Q 78 72 90 54 Z" fill="#FFFFFF" fill-opacity="0.3" stroke-width="4.5" />
  </g>
</svg>`;

const tempSvg = path.join(__dirname, 'temp_balanza.svg');
const outPng = 'c:\\Users\\SDVP\\Documents\\GitHub\\presentaciones-ejecutivas\\01-Propuestas-Comerciales\\UVC-Unlimited-Vacation-Club\\assets\\icono_balanza_fiscal.png';

fs.writeFileSync(tempSvg, svgCode);

const htmlWrapper = path.join(__dirname, 'render_icon.html');
fs.writeFileSync(htmlWrapper, `<!DOCTYPE html><html><body style="margin:0;background:transparent;"><img src="file:///${tempSvg.replace(/\\/g, '/')}" width="400" height="400"/></body></html>`);

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const cmd = `"${chromePath}" --headless=new --screenshot="${outPng}" --window-size=400,400 --default-background-color=00000000 --user-data-dir="${process.env.TEMP}\\chrome_icon_render" "file:///${htmlWrapper.replace(/\\/g, '/')}"`;

try {
  execSync(cmd);
  console.log('Successfully created PNG icon:', outPng);
} catch (err) {
  console.error('Error generating PNG:', err);
}

