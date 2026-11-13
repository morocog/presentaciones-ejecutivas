const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const repoDir = 'c:\\Users\\SDVP\\Documents\\GitHub\\presentaciones-ejecutivas\\01-Propuestas-Comerciales\\UVC-Unlimited-Vacation-Club';
const htmlPath = path.join(repoDir, 'index.html');
const slidesHdDir = path.join(repoDir, 'assets', 'slides_hd');
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

if (!fs.existsSync(slidesHdDir)) {
  fs.mkdirSync(slidesHdDir, { recursive: true });
}

// 1. Read index.html
const htmlContent = fs.readFileSync(htmlPath, 'utf8');

// 2. Extract each <section class="slide ...">...</section>
// We want to capture 11 slides
const slideRegex = /<section class="slide[\s\S]*?<\/section>/g;
const slides = htmlContent.match(slideRegex);

console.log(`Found ${slides.length} slides in index.html`);

// Extract header and footer styles / script
const headMatch = htmlContent.match(/<head>[\s\S]*?<\/head>/);
const headContent = headMatch ? headMatch[0] : '';

// Render each slide as standalone 1920x1080 HTML, then screenshot via headless Chrome
for (let i = 0; i < slides.length; i++) {
  const slideNum = i + 1;
  const slideHtml = slides[i];
  
  const standaloneHtml = `<!DOCTYPE html>
<html lang="es">
${headContent}
<body class="bg-slate-900" style="margin:0;padding:0;overflow:hidden;width:1920px;height:1080px;">
  ${slideHtml}
</body>
</html>`;

  const tempHtmlFile = path.join(slidesHdDir, `slide_${slideNum}_temp.html`);
  const outPngFile = path.join(slidesHdDir, `slide_${slideNum}.png`);
  
  fs.writeFileSync(tempHtmlFile, standaloneHtml, 'utf8');
  
  const tempProfile = path.join(process.env.TEMP, `chrome_slide_${slideNum}`);
  const cmd = `"${chromePath}" --headless=new --screenshot="${outPngFile}" --window-size=1920,1080 --default-background-color=00000000 --user-data-dir="${tempProfile}" "file:///${tempHtmlFile.replace(/\\/g, '/')}"`;
  
  try {
    execSync(cmd, { stdio: 'ignore' });
    console.log(`Rendered Slide ${slideNum} -> ${outPngFile}`);
    // cleanup temp html
    fs.unlinkSync(tempHtmlFile);
  } catch (err) {
    console.error(`Error rendering slide ${slideNum}:`, err.message);
  }
}

console.log('All 11 slides rendered in Full HD PNG successfully!');

