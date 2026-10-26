const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2]; const b = await chromium.launch();
  for (const [w, name] of [[1440, 'desk'], [390, 'mob']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 2 });
    await p.goto('file://' + d + '/prototipo.html'); await p.evaluate(() => document.fonts.ready);
    await p.addStyleTag({ content: '.head{position:static!important}.wa-float{position:absolute!important}' });
    await p.screenshot({ path: `${d}/shots/proto-${name}.png`, fullPage: true });
    const sw = await p.evaluate(() => document.documentElement.scrollWidth); console.log(name, 'scrollWidth', sw);
    await p.close();
  }
  await b.close();
})();
