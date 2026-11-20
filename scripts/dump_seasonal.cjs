const fs = require('fs');
const path = require('path');
const html = fs.readFileSync('C:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/01-Propuestas-Comerciales/Seasonal-Contact-Center/Propuesta_Comercial_TELAT_Seasonal_Contact_Center.html', 'utf8');

const regex = /<(h[1-6]|p|li|td|th|span|strong)[^>]*>([\s\S]*?)<\/\1>/gi;
let match;
const lines = [];
while ((match = regex.exec(html)) !== null) {
  let tag = match[1];
  let text = match[2].replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/\s+/g, ' ').trim();
  if (text.length > 25 && !text.includes('function(') && !text.includes('addEventListener') && !text.includes('tailwind.config') && !text.includes('data:image')) {
    lines.push(`[${tag.toUpperCase()}] ${text}`);
  }
}

fs.writeFileSync('C:/Users/SDVP/Documents/GitHub/presentaciones-ejecutivas/scripts/seasonal_extracted.txt', lines.join('\n'), 'utf8');
console.log('Saved', lines.length, 'text segments to seasonal_extracted.txt');
