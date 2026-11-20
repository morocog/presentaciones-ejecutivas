const fs = require('fs');
const path = require('path');

const targetFile = path.join(__dirname, '../00-Executive-Decks-EN/04-Commercial-Capabilities-Deck-Harry-and-David/index.html');
const html = fs.readFileSync(targetFile, 'utf8');

const regex = /<(h[1-6]|p|li|span)[^>]*>([\s\S]*?)<\/\1>/gi;
let match;
const lines = [];
while ((match = regex.exec(html)) !== null) {
  let tag = match[1];
  let text = match[2].replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/\s+/g, ' ').trim();
  if (text.length > 25 && !text.includes('function(') && !text.includes('addEventListener') && !text.includes('tailwind.config')) {
    lines.push(`[${tag.toUpperCase()}] ${text}`);
  }
}

fs.writeFileSync(path.join(__dirname, 'extracted_texts.txt'), lines.join('\n'), 'utf8');
console.log('Saved', lines.length, 'text segments to extracted_texts.txt');
