/**
 * Static server for the MUK CU clone.
 * Binds 0.0.0.0 so the Arena live preview can reach it, and accepts any Host
 * header (the preview is proxied under https://{port}-{sandbox}.e2b.app).
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const PORT = process.env.PORT || 3000;

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff2': 'font/woff2',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
};

const server = http.createServer((req, res) => {
  let pathname;
  try {
    pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  } catch {
    res.writeHead(400).end('Bad request');
    return;
  }

  if (pathname === '/') pathname = '/index.html';
  // Allow extensionless URLs like the original Squarespace slugs.
  if (!path.extname(pathname)) {
    if (fs.existsSync(path.join(ROOT, pathname + '.html'))) pathname += '.html';
    else pathname = path.join(pathname, 'index.html');
  }

  const filePath = path.join(ROOT, pathname);
  // Prevent path traversal outside the project root.
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403).end('Forbidden');
    return;
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      // Serve the styled 404 page for missing HTML routes; plain text for assets.
      const notFound = path.join(ROOT, '404.html');
      fs.readFile(notFound, (e404, page404) => {
        res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(e404 ? '<h1>404 &mdash; Page not found</h1><p><a href="/">Return home</a></p>' : page404);
      });
      return;
    }
    const ext = path.extname(filePath).toLowerCase();
    const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream' };
    if (ext === '.woff2' || ext === '.jpg' || ext === '.png' || ext === '.webp') {
      headers['Cache-Control'] = 'public, max-age=86400';
    }
    res.writeHead(200, headers);
    res.end(data);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`MUK CU clone running at http://0.0.0.0:${PORT}`);
});
