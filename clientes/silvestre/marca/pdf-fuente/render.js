const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + process.argv[2] + '/manual.html'); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[3], width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  const n = await p.$$eval('.page', e => e.length);
  for (let i = 0; i < n; i++) { const el = (await p.$$('.page'))[i]; await el.screenshot({ path: `${process.argv[2]}/shots/p${String(i+1).padStart(2,'0')}.png` }); }
  await b.close();
})();
