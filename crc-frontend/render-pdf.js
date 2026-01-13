const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  try {
    const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
    const page = await browser.newPage();

    const filePath = path.join(__dirname, 'printable.html');
    const fileUrl = 'file://' + filePath;

    await page.goto(fileUrl, { waitUntil: 'networkidle0' });
    await page.emulateMediaType('print');

    const outPath = path.join(__dirname, 'Abhishek-resume.pdf');
    await page.pdf({ path: outPath, format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '12mm', right: '12mm' } });

    console.log('PDF generated at:', outPath);
    await browser.close();
  } catch (err) {
    console.error('Error generating PDF:', err);
    process.exit(1);
  }
})();
