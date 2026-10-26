const { chromium } = require('playwright');
(async () => { const d = process.argv[2]; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + d + '/manual.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.pdf({ path: process.argv[3], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  const els = await p.$$('.page'); for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${d}/shots/pg${String(i+1).padStart(2,'0')}.png` });
  await b.close(); })();
