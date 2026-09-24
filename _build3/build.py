"""Coastside V3 prototype generator.

  python3 _build3/build.py            -> writes the site into v3/
Env: OUT_DIR, SITE_URL, EXPLICIT_INDEX (1 = links end in index.html), CONCEPT (1 = noindex)

Templates query the collections in data.py. Service and location pages list
projects that reference them; nothing is linked by hand.
"""
import os, sys, json, html, glob, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import *  # noqa

OUT = os.path.abspath(os.environ.get('OUT_DIR', os.path.join(HERE, '..', 'v3')))
SITE_URL = os.environ.get('SITE_URL', 'https://coastside.theserviceedit.com/v3/')
EXPLICIT = os.environ.get('EXPLICIT_INDEX', '1') == '1'
CONCEPT = os.environ.get('CONCEPT', '1') == '1'
HERO = os.environ.get('HERO', 'cards')
PALETTE = os.environ.get('PALETTE', '')
THEME = os.environ.get('THEME', '')  # 'v6' = split 'open house' home + DM Sans / Plex Mono type  # e.g. 'b' loads assets/palette-b.css  # 'cards' (v3) or 'strip' (v4)
IMG_DIR = os.path.join(OUT, 'img')
E = html.escape

PUB_SERVICES = [s for s in SERVICES if not s.get('conditional')]
MARQUEE = [('contact', 'Coastside crew rendering a canal-front home from scaffolding'),
           ('hero', 'White rendered coastal home with timber battens, Gold Coast'),
           ('project-4', 'Multi-storey residential building with curved rendered balconies'),
           ('ig-5', 'Coastside plasterer rendering from scaffolding'),
           ('project-5', 'Rendered curved entry wall and bench at a commercial building'),
           ('services', 'Coastside crew pumping and finishing render'),
           ('ig-3', 'Rendered two-storey coastal home at Brakes Crescent, Miami')]
PUB_LOCATIONS = [l for l in LOCATIONS if l['published']]
NAV = [('services/', 'Services'), ('projects/', 'Projects'), ('service-areas/', 'Service areas'),
       ('builder-pack/', 'Builder pack'), ('resources/', 'Resources')]
SITEMAP = []


# ---------------------------------------------------------------- helpers
class Ctx:
    def __init__(self, path):
        self.path = path
        self.depth = 0 if path in ('', '404.html') else path.rstrip('/').count('/') + 1

    def L(self, p):
        r = '../' * self.depth
        if p == '' or p.endswith('/'):
            return r + p + ('index.html' if EXPLICIT else ('' if p else './'))
        return r + p


def img_widths(name):
    ws = sorted(int(m.group(1)) for f in glob.glob(os.path.join(IMG_DIR, f'{name}-*.webp'))
                for m in [re.search(r'-(\d+)\.webp$', f)] if m)
    return ws


_dims = {}
def dims(name):
    if name not in _dims:
        _dims[name] = Image.open(os.path.join(IMG_DIR, name + '.jpg')).size
    return _dims[name]


def pic(c, name, alt, sizes='100vw', eager=False, cls=''):
    ws = img_widths(name)
    w, h = dims(name)
    srcset = ', '.join(f"{c.L(f'img/{name}-{x}.webp')} {x}w" for x in ws)
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture{" class=" + chr(34) + cls + chr(34) if cls else ""}><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img src="{c.L(f"img/{name}.jpg")}" alt="{E(alt)}" width="{w}" height="{h}" {load}></picture>')


def crumbs(c, items):
    lis = ''.join(f'<li><a href="{c.L(p)}">{t}</a></li>' if p is not None else f'<li aria-current="page">{t}</li>' for p, t in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'


def crumb_schema(items):
    el = []
    for i, (p, t) in enumerate(items, 1):
        e = {"@type": "ListItem", "position": i, "name": re.sub('<[^>]+>', '', t)}
        if p is not None:
            e["item"] = SITE_URL + p
        el.append(e)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}


def faq_block(faqs, dark=False):
    if not faqs:
        return ''
    items = ''.join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faqs)
    return f'<div class="faq">{items}</div>'


def faq_schema(faqs):
    clean = [(q, a) for q, a in faqs if 'class="tbc"' not in a and 'class="tbc"' not in q]
    if not clean:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in clean]}


def projects_for(service=None, location=None):
    out = PROJECTS
    if service:
        out = [p for p in out if service in p['services']]
    if location:
        kids = {location} | {l['slug'] for l in LOCATIONS if l.get('parent') == location}
        out = [p for p in out if p['location'] in kids]
    return out


def project_card(c, p, h='h3'):
    tags = ' / '.join([SECTORS[p['sector']], BUILD_TYPES[p['build']]])
    return (f'<a class="card" href="{c.L("projects/" + p["slug"] + "/")}" data-sector="{p["sector"]}" '
            f'data-service="{" ".join(p["services"])}" data-location="{p["location"]}" data-build="{p["build"]}">'
            f'<div class="ph">{pic(c, p["img"], p["alt"], "(max-width:640px) 100vw, (max-width:1100px) 50vw, 400px")}</div>'
            f'<span class="tag">{tags}</span><{h}>{p["title"]}</{h}><p>{p["summary"]}</p>'
            f'<span class="more">View case study</span></a>')


def cta(c, title='Pricing a job? Send the plans.', text='Plans, elevations, the finish schedule and your program. We come back with an itemised price.', q=''):
    return f'''<section class="cta"><div class="wrap">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="btns"><a class="btn btn-primary" href="{c.L('quote/')}{q}" data-track="cta_send_plans">Send plans</a><a class="btn btn-ghost" href="{c.L('builder-pack/')}">Builder pack</a></div>
</div></section>'''


def svc_rows(c, services):
    return '<div class="svc-list">' + ''.join(
        f'<a class="svc-row" href="{c.L("services/" + s["slug"] + "/")}"><span class="n">{i:02d}</span><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="go">View service</span></a>'
        for i, s in enumerate(services, 1)) + '</div>'


def steps_ol():
    return f'''<ol class="steps">
  <li><h3>Send the plans</h3><p>Elevations, finish schedule, substrate and program. A share link is fine.</p></li>
  <li><h3>Itemised quote</h3><p>Priced to your specification and scaffold program. Turnaround {tbc('to confirm')}.</p></li>
  <li><h3>Program locked</h3><p>Start dates and crew numbers agreed per elevation before we mobilise.</p></li>
  <li><h3>Finish and handover</h3><p>Walk-through with your site manager, defects closed out {tbc('confirm')}.</p></li>
</ol>'''


# ---------------------------------------------------------------- layout
def page(c, title, desc, body, ptype='page', active=None, schema=(), og='hero', slug='', index=True, chrome=True):
    L = c.L
    noindex = CONCEPT or not index
    cur = ' aria-current="page"'
    navl = ''.join(f'<li><a href="{L(p)}"{cur if active == p else ""}>{t}</a></li>' for p, t in NAV)
    mnav = ''.join(f'<a href="{L(p)}">{t}</a>' for p, t in [('', 'Home')] + NAV + [('about/', 'About'), ('contact/', 'Contact')])
    canon = SITE_URL + c.path
    HEADER = f'''<header class="nav">
  <a class="nav-logo" href="{L('')}"><img src="{L('img/logo.png')}" alt="" width="52" height="52"><span>Coastside<br>Solid Plastering</span><span class="sr">Home</span></a>
  <nav aria-label="Main"><ul class="nav-links">{navl}<li><a class="nav-cta" href="{L('quote/')}" data-track="nav_send_plans">Send plans</a></li></ul></nav>
  <button class="nav-toggle" aria-controls="mnav" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>
</header>
<div class="mnav" id="mnav" role="dialog" aria-label="Menu"><button class="close" aria-label="Close menu">&times;</button>{mnav}<a class="btn btn-primary" href="{L('quote/')}">Send plans</a></div>
'''
    org = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": SITE_URL + "#business",
           "name": SITE['name'], "legalName": SITE['legal'], "taxID": SITE['abn'], "telephone": SITE['phone_tel'], "email": SITE['email'],
           "url": SITE_URL, "logo": SITE_URL + "img/logo.png", "image": SITE_URL + "img/hero.jpg",
           "address": {"@type": "PostalAddress", "addressLocality": "Gold Coast", "addressRegion": "QLD", "addressCountry": "AU"},
           "areaServed": [l['name'] for l in PUB_LOCATIONS] + ["Byron Bay", "Tweed Heads", "Brisbane"], "sameAs": [SITE['instagram']]}
    blocks = [org] + [s for s in schema if s]
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in blocks)
    svc_links = ''.join(f'<li><a href="{L("services/" + s["slug"] + "/")}">{s["name"]}</a></li>' for s in PUB_SERVICES)
    loc_links = ''.join(f'<li><a href="{L(l["slug"] + "/")}">{l["name"]}</a></li>' for l in PUB_LOCATIONS)
    if index and c.path not in ('404.html',):
        SITEMAP.append(c.path)
    doc = f'''<!DOCTYPE html>
<html lang="en-AU" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{SITE_URL}img/{og}.jpg"><meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2A2A2A">
<link rel="icon" href="{L('img/logo.png')}">
{('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&display=swap">') if HERO == 'strip' and ptype == 'home' else ''}
<link rel="stylesheet" href="{L('assets/site.css')}">{('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&family=IBM+Plex+Mono:wght@400;500&display=swap"><link rel="stylesheet" href="' + L('assets/theme-v6.css') + '">') if THEME == 'v6' else ''}{('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"><link rel="stylesheet" href="' + L('assets/theme-v7.css') + '?v=20260924-5' + '">') if THEME == 'v7' else ''}{('<link rel="stylesheet" href="' + L('assets/palette-' + PALETTE + '.css') + '">') if PALETTE else ''}
{ld}
</head>
<body data-type="{ptype}" data-slug="{slug}"{' class="oh-body"' if not chrome else ''}>
<a class="skip" href="#main">Skip to content</a>
{HEADER if chrome else ''}<main id="main">
{body}
</main>
<footer class="footer dark">
  <div class="fgrid">
    <div><img src="{L('img/logo.png')}" alt="Coastside Solid Plastering" width="64" height="64" loading="lazy"><p>Solid plastering, external render and architectural coatings for builders, architects and developers from {SITE['area']}.</p></div>
    <div><h2>Services</h2><ul>{svc_links}</ul></div>
    <div><h2>Service areas</h2><ul>{loc_links}<li><a href="{L('service-areas/')}">All areas</a></li></ul><h2 style="margin-top:22px">Company</h2><ul><li><a href="{L('about/')}">About</a></li><li><a href="{L('projects/')}">Projects</a></li><li><a href="{L('resources/')}">Resources</a></li></ul></div>
    <div><h2>For builders</h2><ul><li><a href="{L('builder-pack/')}">Builder pack</a></li><li><a href="{L('builder-pack/coastside-capability-statement.pdf')}">Capability statement (PDF)</a></li><li><a href="{L('builder-pack/tender-list/')}">Tender list</a></li><li><a href="{L('quote/')}">Send plans</a></li></ul></div>
    <div><h2>Contact</h2><ul><li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li><li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li><li><a href="{SITE['instagram']}" rel="noopener" target="_blank">Instagram</a></li></ul><p style="margin-top:14px">ABN {SITE['abn']}<br>QBCC licence {tbc('number')}</p></div>
  </div>
  <div class="fbase"><span>&copy; 2026 {SITE['legal']}. <a href="{L('privacy/')}">Privacy</a></span><span>Site by <a href="https://theserviceedit.com" rel="noopener" target="_blank">The Service Edit</a></span></div>
</footer>
{'' if (ptype in ('quote','quote-received','tender') or not chrome) else '<div class="mbar"><a href="' + L('quote/') + '" data-track="mbar_send_plans">Send plans</a></div>'}
<script src="{L('assets/site.js')}" defer></script>
</body>
</html>
'''
    if THEME == 'v7' and 'FOOTER_V7' in globals():
        doc = re.sub(r'<footer class="footer dark">.*?</footer>', lambda m: FOOTER_V7(L), doc, count=1, flags=re.S)
    return doc


def write(path, doc):
    out = os.path.join(OUT, path, 'index.html') if (path == '' or path.endswith('/')) else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(doc)


# ---------------------------------------------------------------- templates
def home():
    c = Ctx('')
    if THEME == 'v6':
        return home_split(c)
    L = c.L
    featured = [p for p in PROJECTS if p['featured']][:3]
    if THEME == 'v7':
        hero_html = f'''<section class="v7h" aria-labelledby="h1">
  <picture class="v7h-bg"><source type="image/webp" srcset="{L('img/v7-hero-700.webp')} 700w, {L('img/v7-hero-1100.webp')} 1100w, {L('img/v7-hero-1672.webp')} 1672w" sizes="100vw"><img src="{L('img/v7-hero.jpg')}" alt="Curved rendered entry wall and lit bench at a Gold Coast commercial building, rendered by Coastside" width="1672" height="941" fetchpriority="high"></picture>
  <div class="v7h-shade" aria-hidden="true"></div>
  <div class="v7h-stack">
    <p class="v7h-kicker">Solid plastering &middot; Render &middot; Coatings</p>
    <h1 id="h1"><span class="v7h-wm">coastside</span><span class="v7h-serif"><small>for</small>Gold Coast Builders</span></h1>
  </div>
  <div class="v7h-foot">
    <a href="{L('quote/')}" data-track="hero_send_plans">Send plans</a>
    <span>Byron Bay &middot; Gold Coast &middot; South East Brisbane</span>
    <a href="{L('builder-pack/')}">Builder pack</a>
  </div>
  <a class="v7h-scroll" href="#intro" aria-label="Scroll to content"><span></span></a>
</section>
<section class="v7-intro" id="intro" aria-label="Coastside at a glance">
  <p class="v7-intro-text rise">A second-generation plasterer's crew, rendering and plastering for builders, architects and developers from {SITE['area']}. Finished to the specification and on your program.</p>
  <div class="shero-stats">
    <div class="rise"><strong>25+</strong><span>Years in the trade</span></div><i aria-hidden="true"></i>
    <div class="rise" style="--d:100ms"><strong>15+</strong><span>Crew on the tools</span></div><i aria-hidden="true"></i>
    <div class="rise" style="--d:200ms"><strong>3</strong><span>Regions, Byron to Brisbane</span></div><i aria-hidden="true"></i>
    <div class="rise" style="--d:300ms"><strong>QBCC</strong><span>Licensed {tbc('no.')}</span></div>
  </div>
</section>
'''
    elif HERO == 'strip':
        hero_html = f'''<section class="shero dark" aria-labelledby="h1">
  <div class="shero-head rise"><span class="eyebrow">Solid plastering, render and architectural coatings</span><h1 id="h1">Finish matters.<br>So does turning up.</h1>
    <div class="btns shero-cta"><a class="btn btn-primary" href="{L('quote/')}" data-track="hero_send_plans">Send plans <span aria-hidden="true">&rarr;</span></a><a class="btn btn-ghost" href="{L('builder-pack/')}">Builder pack</a></div></div>
  <div class="shero-strip rise" style="--d:120ms">
    <div class="shero-scroll" tabindex="0" aria-label="Project photos. Swipe to see more."><div class="shero-track">
      {''.join(pic(c, n, a_, '(max-width:479px) 450px, (max-width:991px) 720px, 980px', eager=(i < 3)) for i, (n, a_) in enumerate(MARQUEE))}
    </div></div>
    <svg class="shero-mask top" viewBox="0 0 1000 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0H1000V8Q500 70 0 8Z"/></svg>
    <svg class="shero-mask bottom" viewBox="0 0 1000 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60H1000V52Q500 -10 0 52Z"/></svg>
  </div>
  <div class="shero-body">
    <div class="shero-stats">
      <div class="rise"><strong>25+</strong><span>Years in the trade</span></div><i aria-hidden="true"></i>
      <div class="rise" style="--d:100ms"><strong>15+</strong><span>Crew on the tools</span></div><i aria-hidden="true"></i>
      <div class="rise" style="--d:200ms"><strong>3</strong><span>Regions, Byron to Brisbane</span></div><i aria-hidden="true"></i>
      <div class="rise" style="--d:300ms"><strong>QBCC</strong><span>Licensed {tbc('no.')}</span></div>
    </div>
    <div class="shero-text rise"><p>A second-generation plasterer's crew, rendering and plastering for builders, architects and developers from {SITE['area']}. Finished to the specification and on your program.</p>
</div>
  </div>
</section>
'''
    else:
        hero_html = f'''<section class="vhero" aria-label="Introduction">
  <div class="vhero-media">
    {pic(c, 'hero', 'White rendered coastal home with timber battens, Gold Coast', eager=True)}
    {('<video class="vhero-video" autoplay muted loop playsinline preload="metadata" poster="' + L('img/hero.jpg') + '" aria-hidden="true"><source src="' + L(SITE['hero_video']) + '" type="video/mp4"></video>') if SITE.get('hero_video') else ''}
    <span class="vhero-cap">Coastal residence, Gold Coast</span>
  </div>
  <div class="vhero-inner">
    <div class="vhero-grid">
      <div class="vcard vcard-main rise">
        <a class="vbadge" href="{L('builder-pack/')}"><span class="vbadge-l">For builders</span><span>Licence, insurance and capability in one place</span><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M6 12L10 8L6 4" stroke="currentColor" stroke-opacity=".55" stroke-width="2" stroke-linecap="square"/></svg></a>
        <h1>Finish matters. <span>So does turning up.</span></h1>
      </div>
      <div class="vcard vcard-side rise" style="--d:120ms">
        <p>A 15+ crew rendering and plastering for builders, architects and developers from {SITE['area']}. Finished to the specification and on your program.</p>
        <div class="vcta"><a class="vbtn" href="{L('quote/')}" data-track="hero_send_plans"><span class="vbtn-mask"><span class="vbtn-roll"><span>Send plans</span><span aria-hidden="true">Send plans</span></span></span><span class="vbtn-arrow" aria-hidden="true"><span class="vbtn-roll"><svg viewBox="0 0 13 14" fill="none"><path d="M1.33 7H10M6 2.33 10.67 7 6 11.67" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg><svg viewBox="0 0 13 14" fill="none"><path d="M1.33 7H10M6 2.33 10.67 7 6 11.67" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg></span></span></a>
        <a class="text-link" href="{L('projects/')}">See the work</a></div>
      </div>
    </div>
  </div>
</section>
<div class="facts"><div><strong>25+ years</strong><span>In the trade</span></div><div><strong>15+ crew</strong><span>On the tools</span></div><div><strong>Byron to Brisbane</strong><span>Service area</span></div><div><strong>QBCC licensed</strong><span>{tbc('licence no.')}</span></div></div>
'''
    body = f'''
{hero_html}

<section class="sec dark" aria-labelledby="bc">
  <div class="wrap">
    <div class="head"><span class="eyebrow">The builder check</span><h2 id="bc">What you check before you call,<br>with the evidence linked.</h2></div>
    <div class="check">
      <div><p class="q">Licensed?</p><p class="a">QBCC licensed</p><p>Licence {tbc('number and class')}, checkable on the QBCC register.</p><a class="text-link" href="{L('builder-pack/')}">Licence details</a></div>
      <div><p class="q">Insured?</p><p class="a">Public liability {tbc('cover')}</p><p>Certificates of currency for public liability and workers compensation, current and dated.</p><a class="text-link" href="{L('builder-pack/')}#documents">Request certificates</a></div>
      <div><p class="q">Enough crew?</p><p class="a">15+ on the tools</p><p>Enough people to run residential and commercial sites at the same time, with pumped render for large elevations.</p><a class="text-link" href="{L('services/commercial-rendering/')}">Commercial capacity</a></div>
      <div><p class="q">Right systems?</p><p class="a">{', '.join(SITE['systems'][:-1])} and {SITE['systems'][-1]}</p><p>We price and apply the system on your specification.</p><a class="text-link" href="{L('services/architectural-coatings/')}">Coating systems</a></div>
      <div><p class="q">Done this before?</p><p class="a">Luxury, multi-residential, commercial</p><p>Case studies by sector, service and area, with the builder named where they agreed.</p><a class="text-link" href="{L('projects/')}">Projects</a></div>
      <div><p class="q">Paperwork?</p><p class="a">SWMS, certificates, capability</p><p>Everything your pre-start asks for, in one place.</p><a class="text-link" href="{L('builder-pack/')}">Builder pack</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head-row"><div><span class="eyebrow">Recent work</span><h2>Case studies</h2></div><a class="text-link" href="{L('projects/')}">All projects</a></div>
    <div class="cards">{''.join(project_card(c, p) for p in featured)}</div>
  </div>
</section>

<section class="sec cream">
  <div class="wrap grid-2">
    <div><span class="eyebrow">Services</span><h2>Render and plaster, specified and programmed.</h2><p class="lead">Each service page covers scope, substrates, sequencing, access, curing and exactly what we need to price it.</p></div>
    <div>{svc_rows(c, PUB_SERVICES)}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap grid-2">
    <div>{pic(c, 'ig-2', 'Gold Coast Broadwater and marina from the air', '(max-width:1100px) 100vw, 560px')}</div>
    <div><span class="eyebrow">Service area</span><h2>Byron Bay to South East Brisbane.</h2><p class="lead" style="margin-bottom:28px">Based on the Gold Coast. Coastal exposure, canal-front access and mid-rise facades are the everyday conditions here.</p>
      <ul class="ticks">{''.join(f'<li><a href="{L(l["slug"] + "/")}">{l["name"]}</a></li>' for l in PUB_LOCATIONS)}<li>Northern Rivers {tbc('publishes once NSW licence confirmed')}</li><li>South East Brisbane {tbc('confirm')}</li></ul>
      <a class="text-link" href="{L('service-areas/')}">Service areas</a></div>
  </div>
</section>

<section class="sec stone">
  <div class="wrap"><div class="head"><span class="eyebrow">How it works</span><h2>How a job runs with Coastside</h2></div>{steps_ol()}</div>
</section>

<section class="sec-tight">
  <div class="wrap grid-2">
    <div><span class="eyebrow">From builders</span><h2 style="font-size:28px">Builder testimonial</h2></div>
    <blockquote class="lead">{tbc('2 to 3 builder or designer testimonials, with permission. Shown beside the project they refer to.')}</blockquote>
  </div>
</section>
{cta(c)}'''
    write('', page(c, 'Coastside Solid Plastering | Render and solid plastering contractor, Gold Coast',
                   'Solid plastering, external render and architectural coatings for builders from Byron Bay to South East Brisbane. 15+ crew. Send plans for an itemised price.',
                   body, 'home'))


# ---------------------------------------------------------------- V6: split 'open house' home
SCENES = [
    ('intro', 'hero', 'White rendered coastal home, Gold Coast', 'Finish matters.<br>So does turning up.', '01 / Gold Coast, Queensland'),
    ('services', 'services', 'Coastside crew pumping and finishing render', 'Render, plaster<br>and coatings.', '02 / Services'),
    ('check', 'contact', 'Coastside crew rendering a canal-front home from scaffolding', 'Checked before<br>you call.', '03 / The builder check'),
    ('work', 'project-4', 'Multi-storey residential building with curved rendered balconies', 'Recent work.', '04 / Case studies'),
    ('steve', 'steve', 'Steve on a finished rendered home', 'Steve.<br>Second generation.', '05 / Owner'),
    ('builders', 'ig-5', 'Coastside plasterer rendering from scaffolding', 'Pricing a job?', '06 / For builders'),
    ('contact', 'ig-3', 'Rendered coastal home at Brakes Crescent, Miami', 'Send the plans.', '07 / Contact'),
]


def home_split(c):
    L = c.L
    imgs = ''.join(f'<div class="oh-img{" is-visible" if i == 0 else ""}" data-image="{k}">{pic(c, img, alt, "(max-width:700px) 100vw, 43vw", eager=(i == 0))}</div>'
                   for i, (k, img, alt, t, lab) in enumerate(SCENES))
    cur_attr = ' aria-current="true"'
    rail = ''.join(f'<a href="#{k}" aria-label="{lab.split(" / ")[1]}"{cur_attr if i == 0 else ""}></a>' for i, (k, img, alt, t, lab) in enumerate(SCENES))
    def scene(k):
        sc = next(x for x in SCENES if x[0] == k)
        return f'id="{k}" data-scene="{k}" data-title="{E(sc[3])}" data-label="{E(sc[4])}"'
    def idx(n, label):
        return f'<div class="oh-index"><span>{n}</span><span>{label}</span></div>'
    arrow = '<span aria-hidden="true">&#8599;</span>'
    svc = ''.join(f'''<details><summary><span>{i:02d}</span>{s["name"]}</summary><p>{s["short"]} <a href="{L("services/" + s["slug"] + "/")}">View service</a></p></details>''' for i, s in enumerate(PUB_SERVICES, 1))
    systems = ''.join(f'<li>{x}</li>' for x in SITE['systems']) + f'<li class="oh-more"><a href="{L("quote/")}">Your spec {arrow}</a></li>'
    feat = [p for p in PROJECTS if p['featured']][:3]
    work = ''.join(f'''<a class="oh-proj" href="{L("projects/" + p["slug"] + "/")}"><div class="oh-thumb">{pic(c, p["img"], p["alt"], "160px")}</div><div><span class="oh-mono">{SECTORS[p["sector"]]} / {BUILD_TYPES[p["build"]]}</span><strong>{p["title"]}</strong><em>{p["summary"]}</em></div><i aria-hidden="true">&#8599;</i></a>''' for p in feat)
    topics = ''.join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in PUB_SERVICES)
    INTRO_H = '<h1>Solid plastering and render for Gold Coast builders.</h1>'
    body = f'''<div class="oh-layout">
<aside class="oh-window dark" aria-label="Coastside photographs">
  {imgs}
  <a class="oh-logo" href="{L('')}"><img src="{L('img/logo.png')}" alt="Coastside Solid Plastering home" width="64" height="64"><span>Coastside<br>Solid Plastering</span></a>
  <div class="oh-topline"><span>COASTSIDE / GOLD COAST</span><span>28.0&deg; S</span></div>
  <div class="oh-bottom"><p class="oh-title" id="scene-title">Finish matters.<br>So does turning up.</p><div class="oh-mono oh-eyeline"><span id="scene-label">01 / Gold Coast, Queensland</span><span>SCROLL TO EXPLORE &darr;</span></div></div>
  <nav class="oh-rail" aria-label="Sections">{rail}</nav>
</aside>
<div class="oh-content">
  <nav class="oh-mobile-nav" aria-label="Main"><a href="{L('services/')}">Services</a><a href="{L('projects/')}">Projects</a><a href="{L('builder-pack/')}">Builder pack</a><a href="{L('service-areas/')}">Areas</a><a href="{L('quote/')}">Send plans {arrow}</a></nav>

  <section class="oh-chapter oh-intro" {scene('intro')}>
    <header class="oh-header"><nav aria-label="Main"><a href="{L('services/')}">Services</a><a href="{L('projects/')}">Projects</a><a href="{L('builder-pack/')}">Builder pack</a><a href="{L('resources/')}">Resources</a></nav><a href="{L('quote/')}" data-track="nav_send_plans">Send plans {arrow}</a></header>
    <p class="oh-mono">Coastside Solid Plastering</p>
    {INTRO_H}
    <p class="oh-lead">A 15+ crew rendering and plastering for builders, architects and developers from {SITE['area']}. Residential, multi-residential and commercial, finished to the specification and on your program.</p>
    <div class="oh-cta"><a class="oh-pill" href="{L('quote/')}" data-track="hero_send_plans">Send plans {arrow}</a><a class="oh-line" href="{L('builder-pack/')}">Builder pack {arrow}</a><p class="oh-caption">Steve, owner.<br>Second-generation plasterer.</p></div>
    <ul class="oh-stats"><li><strong>25+</strong><span>Years in the trade</span></li><li><strong>15+</strong><span>Crew on the tools</span></li><li><strong>3</strong><span>Regions, Byron to Brisbane</span></li><li><strong>QBCC</strong><span>Licensed {tbc('no.')}</span></li></ul>
  </section>

  <section class="oh-chapter oh-services" {scene('services')}>
    {idx('02', 'Services')}
    <h2>Render, plaster<br>and coatings.</h2>
    <div class="oh-acc">{svc}</div>
    <p class="oh-mono oh-also">Every service page covers scope, substrates, sequencing, scaffold, curing and <a href="{L('resources/what-to-send-for-a-render-quote/')}">what we need to price it</a>.</p>
    <div class="oh-systems"><p class="oh-mono">Systems we apply</p><h3>Priced and applied to your specification.</h3><ul>{systems}</ul></div>
  </section>

  <section class="oh-chapter oh-check dark" {scene('check')}>
    {idx('03', 'The builder check')}
    <h2>What you check<br>before you call.</h2>
    <p class="oh-lead">New to Coastside? These are the questions most builders ask before a first job. The paperwork is in the builder pack.</p>
    <ul class="oh-list">
      <li><span>01</span><b>Licensed</b><em>QBCC licence {tbc('number and class')}</em></li>
      <li><span>02</span><b>Insured</b><em>Public liability {tbc('cover')} and workers compensation, certificates on request</em></li>
      <li><span>03</span><b>Crew</b><em>15+ on the tools, pumped render for large elevations</em></li>
      <li><span>04</span><b>Systems</b><em>{', '.join(SITE['systems'])}</em></li>
      <li><span>05</span><b>Track record</b><em>Luxury residential, multi-residential, commercial</em></li>
      <li><span>06</span><b>Safety</b><em>SWMS for each job {tbc('confirm')}</em></li>
    </ul>
    <a class="oh-pill" href="{L('builder-pack/')}">Get the builder pack {arrow}</a>
  </section>

  <section class="oh-chapter oh-work" {scene('work')}>
    {idx('04', 'Recent work')}
    <h2>Case studies.</h2>
    <p class="oh-lead">Scope, systems and what made each job hard, with the builder named where they agreed.</p>
    <div class="oh-projs">{work}</div>
    <a class="oh-line" href="{L('projects/')}">All projects {arrow}</a>
  </section>

  <section class="oh-chapter oh-steve" {scene('steve')}>
    {idx('05', 'Owner')}
    <h2>Steve.</h2>
    <div class="oh-portrait">{pic(c, 'steve', 'Steve on a finished rendered home', '140px')}</div>
    <p class="oh-lead">Second-generation plasterer. Steve grew up in the trade and now runs a 15+ crew across residential and commercial sites every week. From architectural coatings to large-scale commercial pumping, it is the same standard every time.</p>
    <div class="oh-award"><strong>25+</strong><p>years on the tools, from Byron Bay to South East Brisbane.</p></div>
    <blockquote>{tbc('Builder testimonial, with permission')}<cite>{tbc('Name, company')}</cite></blockquote>
    <a class="oh-line" href="{L('about/')}">About Coastside {arrow}</a>
  </section>

  <section class="oh-chapter oh-tools" {scene('builders')}>
    {idx('06', 'For builders')}
    <h2>Pricing a job?</h2>
    <p class="oh-lead">Everything a builder, estimator or site manager needs, one click away.</p>
    <nav class="oh-links" aria-label="For builders">
      <a href="{L('quote/')}">Send plans for an itemised quote</a>
      <a href="{L('resources/what-to-send-for-a-render-quote/')}">What to send for an accurate render quote</a>
      <a href="{L('builder-pack/')}">Builder pack: licence, insurance, SWMS</a>
      <a href="{L('builder-pack/tender-list/')}">Add Coastside to your tender list</a>
      <a href="{L('service-areas/')}">Service areas</a>
    </nav>
  </section>

  <section class="oh-chapter oh-contact dark" {scene('contact')}>
    {idx('07', 'Contact')}
    <h2>Send Coastside<br>the plans.</h2>
    <p class="oh-lead">Plans, elevations, the finish schedule and your program. We come back with an itemised price.</p>
    <label class="oh-mono" for="oh-topic">What is the job?</label>
    <select id="oh-topic" class="oh-select"><option value="">Choose a service</option>{topics}</select>
    <a class="oh-big" id="oh-go" href="{L('quote/')}" data-track="contact_send_plans">Start your enquiry {arrow}</a>
    <p class="oh-small">Or email <a href="mailto:{SITE['email']}">{SITE['email']}</a> &middot; {SITE['phone']}</p>
    <div class="oh-office"><span>COASTSIDE SOLID PLASTERING<br>ABN {SITE['abn']}</span><span>Gold Coast, Queensland<br>{SITE['area']}</span></div>
  </section>
</div>
</div>'''
    write('', page(c, 'Coastside Solid Plastering | Render and solid plastering contractor, Gold Coast',
                   'Solid plastering, external render and architectural coatings for builders from Byron Bay to South East Brisbane. 15+ crew. Send plans for an itemised price.',
                   body, 'home', chrome=False))


def services_hub():
    c = Ctx('services/')
    L = c.L
    items = [(None, 'Home'), (None, 'Services')]
    items = [('', 'Home'), (None, 'Services')]
    cards = ''.join(f'''<a class="card" href="{L('services/' + s['slug'] + '/')}"><div class="ph">{pic(c, s['img'], '', '(max-width:640px) 100vw, (max-width:1100px) 50vw, 400px')}</div><h3>{s['name']}</h3><p>{s['short']}</p><span class="more">{len(projects_for(s['slug']))} projects &middot; View service</span></a>''' for s in PUB_SERVICES)
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Services</span><h1>Render, plaster and coatings for builders.</h1><p class="lead">Five services, one crew. Each page covers what is in scope, what it needs from the builder and what we need to price it.</p></div></section>
<section class="sec"><div class="wrap"><div class="cards">{cards}</div></div></section>
<section class="sec stone"><div class="wrap"><div class="head"><span class="eyebrow">Systems we apply</span><h2>{', '.join(SITE['systems'])}</h2><p class="lead">If your specification names a system, we price and apply that system. Applicator certifications {tbc('to confirm')}.</p></div>{steps_ol()}</div></section>
{cta(c)}'''
    write('services/', page(c, 'Plastering and rendering services, Gold Coast | Coastside', 'External rendering, commercial rendering, solid plastering, architectural coatings and Venetian plaster for builders across the Gold Coast and Northern Rivers.', body, 'services', 'services/', [crumb_schema(items)], 'services'))


def service_page(s):
    c = Ctx(f"services/{s['slug']}/")
    L = c.L
    items = [('', 'Home'), ('services/', 'Services'), (None, s['name'])]
    projs = projects_for(s['slug'])
    cons = ''.join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in s['considerations'])
    art = ART.get(s['article']) if s.get('article') else None
    others = [o for o in PUB_SERVICES if o['slug'] != s['slug']]
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Service</span><h1>{s['h1']}</h1>
  <div class="hero-row"><p class="lead">{s['short']}</p><div class="btns"><a class="btn btn-primary" href="{L('quote/')}?services={s['slug']}" data-track="service_send_plans" data-label="{s['slug']}">Send plans</a></div></div></div></section>
<figure class="band">{pic(c, s['img'], '', eager=True)}</figure>
<section class="sec"><div class="wrap grid-main">
  <div class="prose">
    <p class="definition">{s['definition']}</p>
    <h2 style="margin-top:56px">What Coastside does</h2><ul>{''.join(f'<li>{x}</li>' for x in s['scope'])}</ul>
    <h2>Where it is used</h2><ul>{''.join(f'<li>{x}</li>' for x in s['used'])}</ul>
    <h2>Systems</h2><p>{', '.join(SITE['systems'])}. We apply the system on your specification. {tbc('confirm which systems apply to this service')}</p>
  </div>
  <aside class="panel sticky" aria-labelledby="q-{s['slug']}"><h2 id="q-{s['slug']}">To price it, send:</h2><p>The more of this we have, the tighter the number.</p>
    <ol><li>Architectural plans and elevations, rendered areas marked</li><li>Finish schedule and nominated system</li><li>Substrate on each elevation</li><li>Project address and site access</li><li>Program, scaffold dates and target start</li><li>Who supplies scaffold</li></ol>
    <a class="btn btn-primary" href="{L('quote/')}?services={s['slug']}" data-track="service_send_plans" data-label="{s['slug']}">Send plans</a>
    <p style="margin-top:16px;font-size:13.5px">New to Coastside? <a href="{L('builder-pack/')}">Builder pack</a></p></aside>
</div></section>
<section class="sec cream"><div class="wrap"><div class="head"><span class="eyebrow">For builders and site managers</span><h2>What to plan for</h2></div><div class="consider">{cons}</div></div></section>
{f'<section class="sec"><div class="wrap"><div class="head-row"><div><span class="eyebrow">Projects using this service</span><h2>{s["name"]} case studies</h2></div><a class="text-link" href="{L("projects/")}?service={s["slug"]}">All {len(projs)} projects</a></div><div class="cards">{"".join(project_card(c, p) for p in projs[:3])}</div></div></section>' if projs else ''}
<section class="sec stone"><div class="wrap grid-2">
  <div><span class="eyebrow">Questions</span><h2>{s['name']} FAQs</h2>{faq_block(s['faqs'])}</div>
  <div><span class="eyebrow">Where we work</span><h2 style="font-size:26px">Service areas</h2><ul class="ticks">{''.join(f'<li><a href="{L(l["slug"] + "/")}">{s["name"]} on the {l["name"]}</a></li>' for l in PUB_LOCATIONS)}<li>Northern Rivers {tbc('conditional')}</li></ul>
  {f'<span class="eyebrow" style="margin-top:36px">Further reading</span><p><a class="text-link" href="{L("resources/" + art["slug"] + "/")}">{art["title"]}</a></p>' if art else ''}
  <span class="eyebrow" style="margin-top:36px">Related services</span><ul class="ticks">{''.join(f'<li><a href="{L("services/" + o["slug"] + "/")}">{o["name"]}</a></li>' for o in others[:3])}</ul></div>
</div></section>
{cta(c, 'Pricing ' + s['name'].lower() + '?', 'Send the plans and the finish schedule. We come back with an itemised price.', '?services=' + s['slug'])}'''
    schema = [crumb_schema(items), faq_schema(s['faqs']),
              {"@context": "https://schema.org", "@type": "Service", "name": s['name'], "serviceType": s['name'], "description": s['definition'],
               "provider": {"@id": SITE_URL + "#business"}, "areaServed": [l['name'] for l in PUB_LOCATIONS]}]
    write(c.path, page(c, f"{s['h1']} | Coastside", s['definition'][:158].rsplit(' ', 1)[0] + '.', body, 'service', 'services/', schema, s['img'], s['slug']))


def areas_hub():
    c = Ctx('service-areas/')
    L = c.L
    items = [('', 'Home'), (None, 'Service areas')]
    rows = ''.join(f'<tr><th scope="row"><a href="{L(l["slug"] + "/")}">{l["name"]}</a></th><td>{l["councils"]}</td><td>{len(projects_for(location=l["slug"]))} case studies</td></tr>' for l in PUB_LOCATIONS)
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Service areas</span><h1>Byron Bay to South East Brisbane.</h1><p class="lead">Based on the Gold Coast. Area pages cover the local conditions that change a render or plaster job, and the work we have done there.</p></div></section>
<section class="sec"><div class="wrap"><table class="table"><thead><tr><th>Area</th><th>Council and licensing</th><th>Work</th></tr></thead><tbody>{rows}
<tr><th scope="row">Northern Rivers</th><td>Tweed Shire, Byron Shire. NSW Fair Trading licensing.</td><td>{tbc('publishes once NSW licence and projects confirmed')}</td></tr>
<tr><th scope="row">South East Brisbane</th><td>Logan, Brisbane, Redland (QBCC)</td><td>{tbc('publishes if 2+ projects')}</td></tr></tbody></table></div></section>
{cta(c)}'''
    write(c.path, page(c, 'Service areas | Coastside Solid Plastering', 'Coastside works from Byron Bay to the Gold Coast to South East Brisbane. Local conditions, councils and projects by area.', body, 'areas', 'service-areas/', [crumb_schema(items)]))


def location_page(l):
    c = Ctx(f"{l['slug']}/")
    L = c.L
    items = [('', 'Home'), ('service-areas/', 'Service areas'), (None, l['name'])]
    projs = projects_for(location=l['slug'])
    used = []
    for p in projs:
        for s in p['services']:
            if s not in used:
                used.append(s)
    cond = ''.join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in l['conditions'])
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Service area</span><h1>{l['h1']}</h1>
  <div class="hero-row"><p class="lead">{l['lead']}</p><div class="btns"><a class="btn btn-primary" href="{L('quote/')}" data-track="location_send_plans" data-label="{l['slug']}">Send plans</a></div></div></div></section>
<figure class="band">{pic(c, l['img'], 'The Broadwater and marina on the Gold Coast from the air', eager=True)}</figure>
<section class="sec cream"><div class="wrap"><div class="head"><span class="eyebrow">Local conditions</span><h2>What shapes a render job on the {l['name']}</h2><p class="lead">General conditions for the area. Coastside's approach to each {tbc('to confirm in Steve interview')}.</p></div><div class="consider">{cond}</div></div></section>
<section class="sec"><div class="wrap"><div class="head-row"><div><span class="eyebrow">Projects on the {l['name']}</span><h2>Work nearby</h2></div><a class="text-link" href="{L('projects/')}?location={l['slug']}">All {len(projs)} projects</a></div><div class="cards">{''.join(project_card(c, p) for p in projs[:6])}</div></div></section>
<section class="sec dark"><div class="wrap grid-2">
  <div><span class="eyebrow">Services on the {l['name']}</span><h2>What we do here</h2>{svc_rows(c, [SVC[s] for s in [x['slug'] for x in PUB_SERVICES]])}</div>
  <div><span class="eyebrow">Who we work with</span><h2 style="font-size:26px">Builders, developers, architects</h2><p class="lead" style="margin-bottom:28px">Custom-home and commercial builders, developers, architects and designers. Named with permission on each case study.</p>
    <span class="eyebrow">Suburbs</span><p style="color:var(--sand)">{l['suburbs']}</p>
    <span class="eyebrow" style="margin-top:28px">Council and licensing</span><p style="color:var(--sand)">{l['councils']}</p></div>
</div></section>
<section class="sec stone"><div class="wrap grid-2"><div><span class="eyebrow">Questions</span><h2>{l['name']} FAQs</h2></div>{faq_block(l['faqs'])}</div></section>
{cta(c, 'Building on the ' + l['name'] + '?', 'Send the plans with the site address and access. We come back with an itemised price.')}'''
    schema = [crumb_schema(items), faq_schema(l['faqs'])]
    write(c.path, page(c, f"Render and solid plastering contractor, {l['name']} | Coastside",
                       f"Rendering and solid plastering on the {l['name']}: coastal exposure, canal-front access, mid-rise facades. Projects, services and what we need to price your job.",
                       body, 'location', 'service-areas/', schema, l['img'], l['slug']))


def projects_hub():
    c = Ctx('projects/')
    L = c.L
    items = [('', 'Home'), (None, 'Projects')]
    def opts(d):
        return ''.join(f'<option value="{k}">{v}</option>' for k, v in d.items())
    used_svc = {s: SVC[s]['name'] for s in dict.fromkeys(x for p in PROJECTS for x in p['services'])}
    used_loc = {l['slug']: l['name'] for l in PUB_LOCATIONS}
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Projects</span><h1>Work by sector, service and area.</h1><p class="lead">Each case study covers the scope, systems, problems on the job and, where they agreed, the builder or architect.</p></div></section>
<section class="sec"><div class="wrap">
  <form class="filterbar" action="" method="get" aria-label="Filter projects" role="search">
    <label>Sector<select name="sector"><option value="">All sectors</option>{opts(SECTORS)}</select></label>
    <label>Service<select name="service"><option value="">All services</option>{opts(used_svc)}</select></label>
    <label>Area<select name="location"><option value="">All areas</option>{opts(used_loc)}</select></label>
    <label>Type<select name="build"><option value="">New build or renovation</option>{opts(BUILD_TYPES)}</select></label>
    <button class="filter-reset" type="button">Reset</button>
    <noscript><button class="btn btn-line" type="submit">Filter</button></noscript>
    <span class="filter-count" aria-live="polite"></span>
  </form>
  <div class="cards proj-grid">{''.join(project_card(c, p, 'h2') for p in PROJECTS)}</div>
  <p class="empty">No projects match those filters yet. <button class="filter-reset" type="button" onclick="document.querySelector('.filterbar .filter-reset').click()">Show all</button></p>
</div></section>
<section class="sec-tight stone"><div class="wrap head-row" style="margin:0"><div><span class="eyebrow">For builders</span><h2 style="margin:0">Need trade references?</h2></div><a class="btn btn-line" href="{L('builder-pack/')}">Builder pack</a></div></section>
{cta(c, 'Pricing a similar project?')}'''
    write(c.path, page(c, 'Projects | Render and plastering case studies | Coastside', 'Render, solid plastering and architectural coating case studies across luxury residential, multi-residential, commercial and hospitality on the Gold Coast.', body, 'projects', 'projects/', [crumb_schema(items)], 'project-4'))


def project_page(p):
    c = Ctx(f"projects/{p['slug']}/")
    L = c.L
    loc = LOC[p['location']]
    items = [('', 'Home'), ('projects/', 'Projects'), (None, p['title'])]
    svcs = ', '.join(f'<a href="{L("services/" + s + "/")}">{SVC[s]["name"]}</a>' for s in p['services'])
    related = [q for q in PROJECTS if q['slug'] != p['slug'] and (set(q['services']) & set(p['services']) or q['sector'] == p['sector'])][:3]
    gal = ''.join(f'<figure>{pic(c, g, p["alt"] if i == 0 else p["title"] + " detail", "(max-width:640px) 100vw, 900px")}</figure>' for i, g in enumerate(p['gallery']))
    note = f'<p class="meta" style="margin-top:12px">{tbc("confirm these images are Coastside work")}</p>' if p.get('confirm_images') else ''
    q = f"?services={p['services'][0]}&amp;sector={p['sector']}"
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">{SECTORS[p['sector']]} &middot; {BUILD_TYPES[p['build']]}</span><h1>{p['title']}</h1><p class="lead">{p['summary']}</p></div></section>
<figure class="band tall">{pic(c, p['img'], p['alt'], eager=True)}</figure>
<section class="sec-tight"><div class="wrap">
  <dl class="spec">
    <div><dt>Location</dt><dd>{p['suburb']}, <a href="{L(loc['slug'] + '/')}">{loc['name']}</a></dd></div>
    <div><dt>Builder</dt><dd>{p['builder']}</dd></div>
    <div><dt>Services</dt><dd>{svcs}</dd></div>
    <div><dt>Year</dt><dd>{p['year']}</dd></div>
  </dl>{note}
</div></section>
<section class="sec" style="padding-top:24px"><div class="wrap grid-main">
  <div class="prose">
    <h2>Overview</h2><p>{p['summary']} {tbc('What the job was: building type, size, storeys, elevations. From Steve interview.')}</p>
    <h2>Coastside scope</h2><p>{tbc('Exactly what Coastside delivered, and what was by others.')}</p>
    <h2>Systems and materials</h2><p>{p['systems']}</p>
    <h2>Challenges</h2><p>{tbc('Only real ones: access, program, exposure, junctions, multiple finishes, occupied site.')}</p>
    <h2>How we approached it</h2><p>{tbc('Sequence, crew, staging and how the challenges were handled.')}</p>
    <h2>Result</h2><p>{tbc('Finished result in two or three sentences, plus builder quote if permitted.')}</p>
  </div>
  <aside class="panel sticky"><h2>Pricing a similar project?</h2><p>Send the plans and we will price it against this one.</p><ol><li>Plans and elevations</li><li>Finish schedule and system</li><li>Address, access and program</li></ol><a class="btn btn-primary" href="{L('quote/')}{q}" data-track="project_send_plans" data-label="{p['slug']}">Send plans</a></aside>
</div></section>
<section class="sec-tight"><div class="wrap"><div class="gallery">{gal}</div></div></section>
{f'<section class="sec cream"><div class="wrap"><div class="head-row"><div><span class="eyebrow">Related</span><h2>Similar projects</h2></div><a class="text-link" href="{L("projects/")}">All projects</a></div><div class="cards">{"".join(project_card(c, r) for r in related)}</div></div></section>' if related else ''}
{cta(c, 'Pricing a similar project?', 'Send the plans, finish schedule and program. We come back with an itemised price.', q)}'''
    schema = [crumb_schema(items), {"@context": "https://schema.org", "@type": "CreativeWork", "name": p['title'], "about": [SVC[s]['name'] for s in p['services']],
                                    "locationCreated": {"@type": "Place", "name": loc['name']}, "creator": {"@id": SITE_URL + "#business"},
                                    "image": [SITE_URL + f"img/{g}.jpg" for g in p['gallery']]}]
    write(c.path, page(c, f"{p['title']} | {SECTORS[p['sector']]} render case study | Coastside",
                       f"{p['summary']} {', '.join(SVC[s]['name'] for s in p['services'])} by Coastside Solid Plastering, {loc['name']}.",
                       body, 'project', 'projects/', schema, p['img'], p['slug']))


def form_head(subject, lead_type, success='', nxt='', event='form_submitted'):
    return (f'<form class="form" action="https://api.web3forms.com/submit" method="post" data-ajax novalidate data-fallback="{SITE["email"]}" '
            f'data-success="{E(success)}" {"data-next=" + chr(34) + nxt + chr(34) if nxt else ""} data-event="{event}">'
            f'<input type="hidden" name="access_key" value="{SITE["web3forms_key"]}"><input type="hidden" name="subject" value="{E(subject)}">'
            f'<input type="hidden" name="from_name" value="Coastside website"><input type="hidden" name="lead_type" value="{lead_type}">'
            f'<div class="hp" aria-hidden="true"><input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></div>')


def fld(id_, label, inp, req=False, opt=False, hint='', err='This is required.'):
    return (f'<div class="field"><label for="{id_}">{label}{" <span class=opt>(optional)</span>" if opt else ""}</label>{inp}'
            f'{f"<span class=hint id={id_}-h>{hint}</span>" if hint else ""}<span class="err" id="{id_}-e">{err}</span></div>')


def builder_pack():
    c = Ctx('builder-pack/')
    L = c.L
    items = [('', 'Home'), (None, 'Builder pack')]
    rows = ''.join(f'''<tr><td class="doc-title">{d['title']}</td><td data-l="Type">{d['type']}</td><td data-l="Access"><span class="pill{' pub' if d['access'] == 'public' else ''}">{'Download' if d['access'] == 'public' else 'On request'}</span></td><td data-l="Issued">{d['issued']}</td><td data-l="Expires">{d['expires']}</td><td class="doc-actions">{f'<a href="{L(d["file"])}" download>Download PDF</a>' if d['file'] else '<a href="#request">Request</a>'}</td></tr>''' for d in DOCUMENTS)
    docs_opts = ''.join(f'<label><input type="checkbox" name="documents" value="{E(d["title"])}"{" checked" if d["type"] == "Insurance" else ""}> {d["title"]}</label>' for d in DOCUMENTS if d['access'] == 'request')
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Builder pack</span><h1>Everything your pre-start asks for.</h1>
  <div class="hero-row"><p class="lead">Company details, licence, insurances, safety documents and references, for builders and procurement teams bringing Coastside onto a job.</p>
  <div class="btns"><a class="btn btn-primary" href="coastside-capability-statement.pdf" download>Capability statement (PDF)</a><a class="btn btn-ghost" href="{L('builder-pack/tender-list/')}" data-track="tender_list_cta">Add us to your tender list</a></div></div></div></section>
<section class="sec"><div class="wrap grid-main">
  <div><span class="eyebrow">Company</span><h2>At a glance</h2>
  <table class="table"><tbody>
    <tr><th scope="row">Legal entity</th><td>{SITE['legal']}<br><small>{tbc('confirm trading entity (Pty Ltd or unit trust)')}</small></td></tr>
    <tr><th scope="row">ABN</th><td>{SITE['abn']}</td></tr>
    <tr><th scope="row">QBCC licence</th><td>{tbc('number and class')} &middot; <a href="https://www.qbcc.qld.gov.au/" rel="noopener" target="_blank">QBCC licence search</a></td></tr>
    <tr><th scope="row">NSW licence</th><td>{tbc('confirm if held')}</td></tr>
    <tr><th scope="row">Public liability</th><td>{tbc('cover and insurer')}</td></tr>
    <tr><th scope="row">Workers compensation</th><td>{tbc('WorkCover Queensland policy')}</td></tr>
    <tr><th scope="row">Crew</th><td>15+ plasterers and renderers</td></tr>
    <tr><th scope="row">Largest project to date</th><td>{tbc('e.g. storeys or facade m2')}</td></tr>
    <tr><th scope="row">Systems</th><td>{', '.join(SITE['systems'])}</td></tr>
    <tr><th scope="row">Service area</th><td>{SITE['area']}</td></tr>
    <tr><th scope="row">Sectors</th><td>{', '.join(SECTORS.values())}</td></tr>
    <tr><th scope="row">Trade references</th><td>{tbc('2 to 3 builders, with permission')}</td></tr>
    <tr><th scope="row">Accounts</th><td>{tbc('name and email for invoices and payment claims')}</td></tr>
  </tbody></table></div>
  <aside class="panel sticky"><h2>Onboarding Coastside?</h2><p>Download the capability statement, then request the current certificates. They come from Coastside directly so they are always in date.</p><ol><li>Capability statement (download)</li><li>Certificates of currency</li><li>SWMS for your site</li><li>Add us to your tender list</li></ol><a class="btn btn-primary" href="#request">Request documents</a></aside>
</div></section>
<section class="sec cream" id="documents"><div class="wrap"><div class="head"><span class="eyebrow">Document register</span><h2>Documents</h2><p class="lead">Certificates past their expiry date are removed automatically and replaced when renewed.</p></div>
  <table class="table register"><thead><tr><th>Document</th><th>Type</th><th>Access</th><th>Issued</th><th>Expires</th><th><span class="sr">Action</span></th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section class="sec stone" id="request"><div class="wrap grid-2">
  <div><span class="eyebrow">Request documents</span><h2>Tell us what you need</h2><p class="lead">Pick the documents and the project. We email them to you.</p></div>
  <div>{form_head('Document request - Coastside website', 'document_request', 'Thanks. The documents will be emailed to you.', event='document_requested')}
    <div class="row2">{fld('dr-name', 'Name', '<input id="dr-name" name="name" autocomplete="name" required aria-describedby="dr-name-e">')}{fld('dr-co', 'Company', '<input id="dr-co" name="company" autocomplete="organization" required aria-describedby="dr-co-e">')}</div>
    <div class="row2">{fld('dr-email', 'Email', '<input id="dr-email" type="email" name="email" autocomplete="email" required aria-describedby="dr-email-e">', err='Enter a valid email.')}{fld('dr-proj', 'Project', '<input id="dr-proj" name="project_name">', opt=True)}</div>
    <fieldset class="field"><legend>Documents</legend><div class="checks">{docs_opts}</div></fieldset>
    <div class="status" role="status" aria-live="polite"></div>
    <div class="btns"><button class="btn btn-primary" type="submit">Request documents</button></div>
  </form></div>
</div></section>
{cta(c, 'Ready to price the job?')}'''
    write(c.path, page(c, 'Builder pack | Licence, insurance and capability | Coastside', 'Coastside Solid Plastering company details, ABN, QBCC licence, insurances, SWMS, capability statement and tender list for builders and procurement teams.', body, 'builder-pack', 'builder-pack/', [crumb_schema(items)], 'project-4'))


def tender_list():
    c = Ctx('builder-pack/tender-list/')
    L = c.L
    items = [('', 'Home'), ('builder-pack/', 'Builder pack'), (None, 'Tender list')]
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Tender list</span><h1>Add Coastside to your tender list.</h1><p class="lead">Tell us how you send invitations to tender and the work you usually price. We respond to every invitation {tbc('confirm')}.</p></div></section>
<section class="sec"><div class="wrap grid-main"><div>{form_head('Tender list request - Coastside website', 'tender_invite', 'Thanks. We have your details and will respond to invitations to tender.', event='tender_list_joined')}
  <div class="row2">{fld('t-co', 'Company', '<input id="t-co" name="company" autocomplete="organization" required>')}{fld('t-name', 'Your name', '<input id="t-name" name="name" autocomplete="name" required>')}</div>
  <div class="row2">{fld('t-email', 'Email for invitations', '<input id="t-email" type="email" name="email" autocomplete="email" required>', err='Enter a valid email.')}{fld('t-phone', 'Phone', '<input id="t-phone" type="tel" name="phone" autocomplete="tel">', opt=True)}</div>
  <fieldset class="field"><legend>How you send tenders</legend><div class="checks"><label><input type="checkbox" name="tender_platform" value="Email"> Email</label><label><input type="checkbox" name="tender_platform" value="EstimateOne"> EstimateOne</label><label><input type="checkbox" name="tender_platform" value="Other platform"> Other platform</label></div></fieldset>
  <fieldset class="field"><legend>Work you usually tender</legend><div class="checks">{''.join(f'<label><input type="checkbox" name="sectors" value="{v}"> {v}</label>' for v in SECTORS.values())}</div></fieldset>
  {fld('t-notes', 'Anything else', '<textarea id="t-notes" name="message" placeholder="Typical project size, areas, upcoming jobs"></textarea>', opt=True)}
  <div class="status" role="status" aria-live="polite"></div>
  <div class="btns"><button class="btn btn-primary" type="submit">Add Coastside</button></div></form></div>
  <aside class="panel"><h2>While you are here</h2><p>The capability statement and document register are in the builder pack.</p><a class="btn btn-primary" href="{L('builder-pack/')}">Builder pack</a></aside></div></section>'''
    write(c.path, page(c, 'Add Coastside to your tender list | Coastside', 'Send invitations to tender to Coastside Solid Plastering.', body, 'tender', 'builder-pack/', [crumb_schema(items)], index=False))


def quote():
    c = Ctx('quote/')
    L = c.L
    items = [('', 'Home'), (None, 'Send plans')]
    roles = ['Builder', 'Developer', 'Architect / designer', 'Project manager', 'Homeowner', 'Other']
    trade = 'Builder|Developer|Architect / designer|Project manager|Other'
    role_ch = ''.join(f'<label class="choice"><input type="radio" name="role" value="{r}" required><span>{r}</span></label>' for r in roles)
    svc_ch = ''.join(f'<label><input type="checkbox" name="services" value="{s["slug"]}"> {s["name"]}</label>' for s in PUB_SERVICES)
    sect = ''.join(f'<option value="{k}">{v}</option>' for k, v in SECTORS.items())
    build = ''.join(f'<option value="{k}">{v}</option>' for k, v in BUILD_TYPES.items())
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Send plans</span><h1>Send the job through.</h1><p class="lead">Three short steps. The more we know about scope, finish and program, the faster and tighter the price.</p></div></section>
<section class="sec"><div class="wrap grid-main">
<div>
<ol class="stepper" aria-label="Progress"><li class="on">Step 1<b>About you</b></li><li>Step 2<b>The project</b></li><li>Step 3<b>Plans</b></li></ol>
{form_head('Quote request - Coastside website', 'quote', '', L('quote/received/'), 'quote_submitted')}
  <fieldset class="step on" data-step="1"><h2>About you</h2>
    <fieldset class="field"><legend>You are</legend><div class="choices">{role_ch}</div><span class="err">Choose one.</span></fieldset>
    <div class="row2">{fld('q-name', 'Name', '<input id="q-name" name="name" autocomplete="name" required>')}<div class="field" data-show-if="role={trade}"><label for="q-co">Company</label><input id="q-co" name="company" autocomplete="organization"><span class="err"></span></div></div>
    <div class="row2">{fld('q-email', 'Email', '<input id="q-email" type="email" name="email" autocomplete="email" required>', err='Enter a valid email.')}{fld('q-phone', 'Phone', '<input id="q-phone" type="tel" name="phone" autocomplete="tel">', opt=True)}</div>
    <div class="step-nav"><span></span><button class="btn btn-primary next" type="button">Next: the project</button></div>
  </fieldset>
  <fieldset class="step" data-step="2"><h2>The project</h2>
    <div class="row2">{fld('q-pname', 'Project name', '<input id="q-pname" name="project_name">', opt=True)}{fld('q-addr', 'Project address or suburb', '<input id="q-addr" name="project_address" autocomplete="off" required>')}</div>
    <div class="row2">{fld('q-sector', 'Sector', f'<select id="q-sector" name="sector" required><option value="">Select</option>{sect}</select>')}{fld('q-build', 'New build or renovation', f'<select id="q-build" name="build_type" required><option value="">Select</option>{build}</select>')}</div>
    <fieldset class="field"><legend>Services needed</legend><div class="checks">{svc_ch}</div></fieldset>
    <div class="row2">{fld('q-start', 'Target start', '<select id="q-start" name="target_start"><option value="">Select</option><option>Pricing only for now</option><option>Within a month</option><option>1 to 3 months</option><option>3 to 6 months</option><option>6 months or more</option></select>', opt=True)}
      <div class="field" data-show-if="role={trade}"><label for="q-value">Approximate value of our scope <span class="opt">(optional)</span></label><select id="q-value" name="estimated_value"><option value="">Select</option><option>Under $25k</option><option>$25k to $75k</option><option>$75k to $200k</option><option>$200k to $500k</option><option>Over $500k</option><option>Not sure</option></select><span class="err"></span></div></div>
    <div class="field" data-show-if="role={trade}"><label for="q-tender">Is this a tender?</label><select id="q-tender" name="is_tender"><option value="">Select</option><option>Yes</option><option>No, awarded or negotiated</option></select><span class="err"></span></div>
    <div class="field" data-show-if="is_tender=Yes"><label for="q-close">Tender closing date</label><input id="q-close" type="date" name="tender_close"><span class="err"></span></div>
    <div class="step-nav"><button class="btn btn-line back" type="button">Back</button><button class="btn btn-primary next" type="button">Next: plans</button></div>
  </fieldset>
  <fieldset class="step" data-step="3"><h2>Plans and notes</h2>
    <div class="field"><span style="font-size:11px;letter-spacing:1.8px;text-transform:uppercase;color:var(--concrete-dk)">Upload plans <span class="opt">(optional)</span></span>
      <div class="drop" tabindex="0" role="button" aria-label="Upload plans: choose files or drag them here"><input type="file" name="plans" multiple accept=".pdf,.dwg,.dxf,.jpg,.jpeg,.png,.zip"><strong>Drop plans here or choose files</strong><small>PDF, DWG, images or ZIP. Up to 25 MB each {tbc('file storage connects at launch; prototype sends file names only')}</small></div>
      <ul class="files" aria-live="polite"></ul></div>
    {fld('q-link', 'Or a link to plans', '<input id="q-link" type="url" name="plans_link" placeholder="Dropbox, Google Drive, EstimateOne">', opt=True, err='Enter a full link starting with https://')}
    {fld('q-msg', 'Project notes', '<textarea id="q-msg" name="message" placeholder="Finish or system on the spec, substrate, access, scaffold, anything else."></textarea>', opt=True)}
    <div class="checks" style="grid-template-columns:1fr"><label><input type="checkbox" name="also_send" value="Builder pack and certificates"> Send me the builder pack and certificates of currency</label></div>
    <div class="status" role="status" aria-live="polite"></div>
    <div class="step-nav"><button class="btn btn-line back" type="button">Back</button><button class="btn btn-primary" type="submit">Send enquiry</button></div>
    <p class="hint" style="font-size:13px;color:var(--concrete-dk)">Your details go to Coastside only and are used to reply to this enquiry. <a href="{L('privacy/')}">Privacy</a></p>
  </fieldset>
</form></div>
<aside class="panel sticky"><h2>What happens next</h2><ol><li>We review the plans and scope {tbc('within X business days')}</li><li>If anything is missing, we ask once, by email</li><li>You get an itemised quote with inclusions and exclusions</li></ol><p>Prefer email? <a href="mailto:{SITE['email']}">{SITE['email']}</a><br>Phone {SITE['phone']}</p></aside>
</div></section>'''
    write(c.path, page(c, 'Send plans for a render or plastering quote | Coastside', 'Send plans and scope to Coastside Solid Plastering for an itemised render, solid plastering or coating quote.', body, 'quote', None, [crumb_schema(items)], 'contact'))

    c2 = Ctx('quote/received/')
    body2 = f'''<section class="hero dark"><div class="wrap"><span class="eyebrow">Enquiry received</span><h1>Thanks. We have the job.</h1><p class="lead">Your enquiry is with Steve.</p></div></section>
<section class="sec"><div class="wrap grid-main"><div><h2>What happens next</h2><ol class="steps" style="grid-template-columns:repeat(3,1fr)"><li><h3>Review</h3><p>We go through the plans and scope {tbc('within X business days')}.</p></li><li><h3>Questions</h3><p>If anything is missing we ask once, by email.</p></li><li><h3>Quote</h3><p>An itemised quote with inclusions, exclusions and program assumptions.</p></li></ol></div>
<aside class="panel"><h2>Onboarding us?</h2><p>The capability statement and certificates are in the builder pack.</p><a class="btn btn-primary" href="{c2.L('builder-pack/')}">Builder pack</a></aside></div></section>'''
    write(c2.path, page(c2, 'Enquiry received | Coastside', 'Thanks for your enquiry.', body2, 'quote-received', index=False))


def resources():
    c = Ctx('resources/')
    L = c.L
    items = [('', 'Home'), (None, 'Resources')]
    cards = ''.join(f'<a class="card" href="{L("resources/" + a["slug"] + "/")}"><span class="tag">Guide</span><h2 style="font-size:24px">{a["title"]}</h2><p>{a["summary"]}</p><span class="more">Read</span></a>' for a in ARTICLES)
    planned = ['Acrylic vs cement render', 'Rendering coastal buildings', 'Where render sits in the construction program', 'What belongs in a render scope of works', 'How scaffold and access change a render price']
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Resources</span><h1>Straight answers for builders and site managers.</h1><p class="lead">Written from the job, reviewed by Steve. No filler.</p></div></section>
<section class="sec"><div class="wrap grid-2"><div class="cards two" style="grid-template-columns:1fr">{cards}</div><div><span class="eyebrow">Coming next {tbc('after Steve interview')}</span><ul class="ticks">{''.join(f'<li>{t}</li>' for t in planned)}</ul></div></div></section>
{cta(c)}'''
    write(c.path, page(c, 'Resources for builders | Render and plastering guides | Coastside', 'Guides for builders, estimators and site managers on render quotes, systems, sequencing and scope.', body, 'resources', 'resources/', [crumb_schema(items)]))
    for a in ARTICLES:
        c = Ctx(f"resources/{a['slug']}/")
        L = c.L
        items = [('', 'Home'), ('resources/', 'Resources'), (None, a['title'])]
        secs = ''.join(f'<h2>{t}</h2><p>{p}</p>' for t, p in a['sections'])
        body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Guide</span><h1>{a['title']}</h1><p class="lead">By Steve, Coastside Solid Plastering. Reviewed {a['reviewed']}</p></div></section>
<section class="sec"><div class="wrap grid-main"><article class="prose"><p class="definition">{a['summary']}</p><div style="height:40px"></div>{secs}
<h2>Related services</h2><ul>{''.join(f'<li><a href="{L("services/" + s + "/")}">{SVC[s]["name"]}</a></li>' for s in a['services'])}</ul></article>
<aside class="panel sticky"><h2>Got the plans ready?</h2><p>Upload them in step 3. A share link works too.</p><a class="btn btn-primary" href="{L('quote/')}" data-track="article_send_plans">Send plans</a></aside></div></section>
<section class="sec cream"><div class="wrap"><div class="head"><span class="eyebrow">Examples</span><h2>Projects priced this way</h2></div><div class="cards">{''.join(project_card(c, PRJ[p]) for p in a['projects'])}</div></div></section>'''
        schema = [crumb_schema(items), {"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['summary'],
                                        "author": {"@type": "Person", "name": "Steve"}, "publisher": {"@id": SITE_URL + "#business"}}]
        write(c.path, page(c, f"{a['title']} | Coastside", a['summary'][:158].rsplit(' ', 1)[0] + '.', body, 'article', 'resources/', schema))


def about():
    c = Ctx('about/')
    L = c.L
    items = [('', 'Home'), (None, 'About')]
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">About</span><h1>Second-generation plasterer. 15+ crew.</h1><p class="lead">Coastside is Steve's business: a solid plastering and render crew working for builders, architects and developers from {SITE['area']}.</p></div></section>
<figure class="band">{pic(c, 'contact', 'Coastside crew rendering a canal-front home from scaffolding', eager=True)}</figure>
<section class="sec"><div class="wrap grid-2"><div>{pic(c, 'steve', 'Steve on a finished rendered home', '(max-width:1100px) 100vw, 560px')}</div>
<div class="prose"><span class="eyebrow">Steve</span><h2>Built on experience. Backed by scale.</h2><p>From a second-generation plasterer to running a 15+ crew, Steve and the team finish residential and commercial projects every week.</p><p>From architectural coatings to large-scale commercial pumping, it is the same standard every time: clean finishes, reliable crews and jobs completed on time.</p><p>Projects completed: {tbc('number')}. Years trading as Coastside: {tbc('confirm')}.</p></div></div></section>
<section class="sec dark"><div class="wrap"><div class="head"><span class="eyebrow">How it works</span><h2>How a job runs with Coastside</h2></div>{steps_ol()}</div></section>
<section class="sec"><div class="wrap"><div class="head"><span class="eyebrow">The crew</span><h2>On the tools</h2></div><div class="cards four tall">{''.join(f'<div class="card"><div class="ph">{pic(c, n, a, "(max-width:640px) 100vw, 300px")}</div></div>' for n, a in [('ig-4', 'Crew member walking a finished rendered corridor'), ('ig-5', 'Plasterer working from scaffolding'), ('ig-6', 'Two plasterers rendering a wall'), ('services', 'Crew pumping and finishing render')])}</div></div></section>
{cta(c)}'''
    write(c.path, page(c, 'About Coastside Solid Plastering | Gold Coast', 'Coastside Solid Plastering: a second-generation plasterer running a 15+ crew for builders and developers from Byron Bay to South East Brisbane.', body, 'about', None, [crumb_schema(items)], 'steve'))


def contact():
    c = Ctx('contact/')
    L = c.L
    items = [('', 'Home'), (None, 'Contact')]
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">Contact</span><h1>Contact Coastside.</h1><p class="lead">Pricing a job? The fastest route is to send the plans.</p></div></section>
<section class="sec"><div class="wrap grid-main"><table class="table"><tbody>
<tr><th scope="row">Send plans</th><td><a href="{L('quote/')}">Quote form with upload</a></td></tr>
<tr><th scope="row">Email</th><td><a href="mailto:{SITE['email']}">{SITE['email']}</a></td></tr>
<tr><th scope="row">Phone</th><td><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></td></tr>
<tr><th scope="row">Based</th><td>Gold Coast, Queensland</td></tr>
<tr><th scope="row">Hours</th><td>{tbc('office hours')}</td></tr>
<tr><th scope="row">ABN</th><td>{SITE['abn']}</td></tr></tbody></table>
<aside class="panel"><h2>Procurement?</h2><p>Licence, insurance and capability documents are in the builder pack.</p><a class="btn btn-primary" href="{L('builder-pack/')}">Builder pack</a></aside></div></section>'''
    write(c.path, page(c, 'Contact | Coastside Solid Plastering', 'Contact Coastside Solid Plastering on the Gold Coast. Send plans, email or phone.', body, 'contact', None, [crumb_schema(items)]))


def privacy():
    c = Ctx('privacy/')
    body = f'''<section class="hero dark"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy</h1></div></section>
<section class="sec"><div class="wrap prose"><p>{tbc('Draft for review before launch. Not legal advice.')}</p><h2>What we collect</h2><p>Details you enter in our forms (name, company, contact details, project details and any plans you upload), and anonymous usage data about how the site is used, including the page and campaign that brought you here.</p><h2>How we use it</h2><p>To reply to your enquiry, prepare a quote, send documents you request, and understand which pages and channels bring enquiries.</p><h2>Where it is stored</h2><p>Enquiries are stored with our enquiry system provider in Australia {tbc('confirm region at launch')}. Analytics are processed by {tbc('analytics provider')}.</p><h2>Contact</h2><p>Questions or requests to access or correct your information: <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p></div></section>'''
    write(c.path, page(c, 'Privacy | Coastside Solid Plastering', 'How Coastside Solid Plastering handles information from this website.', body, 'privacy', index=False))


def not_found():
    c = Ctx('404.html')
    L = c.L
    body = f'''<section class="sec nf"><div class="wrap"><span class="eyebrow">404</span><h1>That page is not here.</h1><p class="lead" style="margin:20px 0 32px">It may have moved. These are the pages most people look for.</p><div class="btns"><a class="btn btn-primary" href="{L('quote/')}">Send plans</a><a class="btn btn-line" href="{L('projects/')}">Projects</a><a class="btn btn-line" href="{L('services/')}">Services</a><a class="btn btn-line" href="{L('builder-pack/')}">Builder pack</a></div></div></section>'''
    write('404.html', page(c, 'Page not found | Coastside', 'Page not found.', body, '404', index=False))


def main():
    if THEME == 'v7':
        import v7copy
        v7copy.install(globals())
    home(); services_hub()
    for s in PUB_SERVICES:
        service_page(s)
    areas_hub()
    for l in PUB_LOCATIONS:
        location_page(l)
    projects_hub()
    for p in PROJECTS:
        project_page(p)
    builder_pack(); tender_list(); quote(); resources(); about(); contact(); privacy(); not_found()
    urls = ''.join(f'<url><loc>{SITE_URL}{p}</loc></url>' for p in SITEMAP)
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(('User-agent: *\nDisallow: /\n' if CONCEPT else 'User-agent: *\nAllow: /\n') + f'Sitemap: {SITE_URL}sitemap.xml\n')
    print(len(SITEMAP), 'indexable pages written to', OUT)


if __name__ == '__main__':
    main()
