const fs = require('fs');
const path = require('path');

const targetFile = process.argv[2] || path.join(__dirname, '../00-Executive-Decks-EN/04-Commercial-Capabilities-Deck-Harry-and-David/index.html');
const content = fs.readFileSync(targetFile, 'utf8');

const aiWords = [
  'seamless', 'seamlessly', 'tapestry', 'beacon', 'testament', 'delve', 
  'foster', 'fostering', 'unlock', 'unlocking', 'harness', 'harnessing', 
  'elevate', 'elevating', 'synergy', 'paradigm', 'cutting-edge', 'game-changer', 
  'pivotal', 'fast-paced', 'revolutionize', 'spearhead', 'complexities', 
  'dynamic landscape', 'furthermore', 'moreover', 'comprehensive', 'robust',
  'vital', 'crucial', 'empower', 'empowering', 'unwavering', 'transformative',
  'groundbreaking', 'bespoke', 'supercharge', 'myriad', 'paramount', 'ever-evolving',
  'revolutionizing', 'game changer', 'cornerstone', 'holistic', 'realm'
];

console.log('--- SCANNING FOR AI DETECTOR BUZZWORDS IN: ' + path.basename(targetFile) + ' ---');

let foundTotal = 0;
aiWords.forEach(w => {
  const reg = new RegExp('\\b' + w + '\\b', 'gi');
  let match;
  let lines = [];
  const linesArr = content.split('\n');
  linesArr.forEach((l, idx) => {
    if (reg.test(l)) {
      lines.push(idx + 1);
    }
  });
  if (lines.length > 0) {
    foundTotal += lines.length;
    console.log(`[ALERT] "${w}": found ${lines.length} time(s) on line(s): ${lines.join(', ')}`);
  }
});

console.log('Total flagged markers:', foundTotal);

// Also look for excessive em-dashes
const emDashMatches = content.match(/—/g);
console.log('Em-dashes (—) found:', emDashMatches ? emDashMatches.length : 0);
