"""Coastside v2 (Builder-ready) static site generator.

Run:  python3 _build/build.py
Writes every page into the output folder (default: v2/ at the repo root).
Edit copy in content.py, layout here. No dependencies.

Settings at the top:
  OUT_DIR        where pages are written
  SITE_URL       absolute URL the site will live at (used for og/canonical)
  EXPLICIT_INDEX True  -> links end in index.html (works when opened from disk)
                 False -> clean folder links (use for launch on a real host)
  CONCEPT        True  -> noindex, TBC chips stay visible
"""
import os, sys, html, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as C

OUT_DIR = os.environ.get('OUT_DIR', os.path.join(HERE, '..', 'v2'))
SITE_URL = os.environ.get('SITE_URL', 'https://coastside.theserviceedit.com/v2/')
EXPLICIT_INDEX = os.environ.get('EXPLICIT_INDEX', '1') == '1'
CONCEPT = os.environ.get('CONCEPT', '1') == '1'

NAV = [('projects/', 'Projects'), ('services/', 'Services'), ('about/', 'About'), ('builder-pack/', 'Builder pack')]


def rel(depth):
    return '../' * depth


def link(path, depth):
    """path is site-relative like '' or 'projects/' or 'img/x.jpg'."""
    r = rel(depth)
    if path == '' or path.endswith('/'):
        return r + path + ('index.html' if EXPLICIT_INDEX else ('' if path else './'))
    return r + path


def page(path, title, description, body, depth, active=None, hero_dark=True, og_image='img/hero.jpg', schema=None):
    L = lambda p: link(p, depth)
    cur = ' aria-current="page"'
    nav_items = ''.join(
        f'<li><a href="{L(p)}"{cur if active == p else ""}>{t}</a></li>' for p, t in NAV)
    mob_items = ''.join(f'<a href="{L(p)}" data-menu-close>{t}</a>' for p, t in NAV)
    robots = '<meta name="robots" content="noindex">\n' if CONCEPT else ''
    canonical = SITE_URL + (path if not EXPLICIT_INDEX or path == '' else path)
    schema_tag = f'<script type="application/ld+json">{json.dumps(schema)}</script>\n' if schema else ''
    svc_links = ''.join(f'<li><a href="{L("services/" + s["slug"] + "/")}">{s["name"]}</a></li>' for s in C.SERVICES)
    return f'''<!DOCTYPE html>
<html lang="en-AU" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
{robots}<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:image" content="{SITE_URL}{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{L('img/logo.png')}">
<link rel="stylesheet" href="{L('assets/site.css')}">
{schema_tag}</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<nav class="nav{'' if hero_dark else ' solid'}" id="nav" aria-label="Main">
  <a href="{L('')}" class="nav-logo"><img src="{L('img/logo.png')}" alt="Coastside Solid Plastering home" width="72" height="72"></a>
  <div class="nav-right">
    <ul class="nav-links">{nav_items}</ul>
    <a href="{L('quote/')}" class="nav-cta">Request a quote</a>
    <button class="hamburger" data-menu-open aria-label="Open menu" aria-controls="mobMenu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mob-menu" id="mobMenu">
  <button class="mob-close" data-menu-close aria-label="Close menu">&times;</button>
  <a href="{L('')}" data-menu-close>Home</a>
  {mob_items}
  <a href="{L('quote/')}" class="mob-cta" data-menu-close>Request a quote</a>
</div>

<main id="main">
{body}
</main>

<footer class="footer">
  <div class="footer-grid">
    <div>
      <img src="{L('img/logo.png')}" alt="Coastside Solid Plastering" width="72" height="72" loading="lazy">
      <p>Solid plastering, render and architectural coatings for builders, architects and designers from Byron Bay to South East Brisbane.</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>{svc_links}</ul>
    </div>
    <div>
      <h4>For builders</h4>
      <ul>
        <li><a href="{L('builder-pack/')}">Builder pack</a></li>
        <li><a href="{L('builder-pack/coastside-capability-statement.pdf')}">Capability statement (PDF)</a></li>
        <li><a href="{L('quote/') + '?need=docs'}">Request certificates</a></li>
        <li><a href="{L('projects/')}">Projects</a></li>
        <li><a href="{L('about/')}">About</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="{L('quote/')}">Request a quote</a></li>
        <li><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
        <li><a href="tel:{C.PHONE_TEL}">{C.PHONE}</a></li>
        <li><a href="{C.INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
      <p style="margin-top:18px;font-size:13px">ABN {C.ABN}<br>QBCC licence {C.tbc('no. to confirm')}</p>
    </div>
  </div>
  <div class="footer-base">
    <span>&copy; 2026 Coastside Solid Plastering. Gold Coast, Queensland.</span>
    <span>Site by <a href="https://theserviceedit.com" target="_blank" rel="noopener">The Service Edit</a></span>
  </div>
</footer>

<div class="mob-bar"><a href="{L('quote/')}">Request a quote</a></div>
<script src="{L('assets/site.js')}"></script>
</body>
</html>
'''


def write(path, doc):
    out = os.path.join(OUT_DIR, path, 'index.html') if (path == '' or path.endswith('/')) else os.path.join(OUT_DIR, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(doc)
    return out


def main():
    pages = C.build_pages(link)
    for p in pages:
        depth = 0 if p['path'] == '' else p['path'].rstrip('/').count('/') + 1
        doc = page(p['path'], p['title'], p['description'], p['body'](depth), depth,
                   active=p.get('active'), hero_dark=p.get('hero_dark', True),
                   og_image=p.get('og_image', 'img/hero.jpg'), schema=p.get('schema'))
        print('wrote', write(p['path'], doc))


if __name__ == '__main__':
    main()
