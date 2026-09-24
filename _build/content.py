"""All copy and data for the Coastside v2 site.

Rules: Australian English. No em dashes. No emojis. No urgency or discount
language. Phone is never the primary CTA. Never invent testimonials, project
names, stats or prices. Anything unconfirmed goes through tbc() so it shows
as a dashed chip until Steve confirms it.
"""
import html

EMAIL = 'steven@coastsidesp.com.au'          # source unconfirmed, check with Steve
PHONE = '0438 045 585'
PHONE_TEL = '+61438045585'
INSTAGRAM = 'https://www.instagram.com/coast_side_plastering/'
ABN = '75 660 293 041'                        # ABR, Coastside Solid Plastering Pty Ltd
LEGAL_NAME = 'Coastside Solid Plastering Pty Ltd'
WEB3FORMS_KEY = '2870139d-38b7-4118-9f7c-9217fd52c463'  # TSE key: enquiries land with Mel until swapped
SYSTEMS = ['Dulux AcraTex', 'Rockcote', 'Unitex', 'Resene', 'Boral']
AREA = 'Byron Bay to the Gold Coast to South East Brisbane'


def tbc(text):
    return f'<span class="tbc" title="To confirm with Steve">{html.escape(text)}</span>'


# ---------------------------------------------------------------- SECTORS
SECTORS = [
    {'key': 'luxury', 'name': 'Luxury residential', 'img': 'img/ig-3-sm.jpg',
     'blurb': 'Architect-designed and coastal homes where the render is the facade.'},
    {'key': 'multi', 'name': 'Multi-residential', 'img': 'img/project-4-sm.jpg',
     'blurb': 'Apartments and townhouses, with the crew numbers to hold a program.'},
    {'key': 'commercial', 'name': 'Commercial and hospitality', 'img': 'img/project-5-sm.jpg',
     'blurb': 'Retail, hospitality and commercial fitouts, inside and out.'},
    {'key': 'architectural', 'name': 'Architectural finishes', 'img': 'img/project-1-sm.jpg',
     'blurb': 'Venetian plaster, texture coatings and feature walls to spec.'},
]
SECTOR_NAME = {s['key']: s['name'] for s in SECTORS}

# ---------------------------------------------------------------- PROJECTS
# Titles are descriptive, not invented project names. Builder, scope detail
# and suburb stay as tbc() until Steve confirms (with the builder's permission).
PROJECTS = [
    {'id': 'miami', 'title': 'Brakes Crescent, Miami', 'sectors': 'luxury', 'img': 'img/ig-3.jpg',
     'alt': 'Rendered two-storey coastal home at Brakes Crescent, Miami, Gold Coast',
     'location': 'Miami, Gold Coast', 'scope': tbc('scope to confirm'), 'builder': tbc('to confirm')},
    {'id': 'coastal', 'title': 'Coastal residence', 'sectors': 'luxury', 'img': 'img/hero-sm.jpg',
     'alt': 'White rendered coastal home with timber battens, Gold Coast',
     'location': 'Gold Coast ' + tbc('suburb'), 'scope': tbc('scope to confirm'), 'builder': tbc('to confirm')},
    {'id': 'canal', 'title': 'Canal-front residence', 'sectors': 'luxury', 'img': 'img/contact-sm.jpg',
     'alt': 'Coastside crew rendering a canal-front home from scaffolding',
     'location': 'Gold Coast ' + tbc('suburb'), 'scope': 'External render ' + tbc('confirm'), 'builder': tbc('to confirm')},
    {'id': 'multistorey', 'title': 'Multi-storey residential', 'sectors': 'multi', 'img': 'img/project-4-sm.jpg',
     'alt': 'Multi-storey residential building with curved rendered balconies',
     'location': 'Gold Coast ' + tbc('suburb'), 'scope': tbc('scope to confirm'), 'builder': tbc('to confirm')},
    {'id': 'commercial-entry', 'title': 'Commercial entry', 'sectors': 'commercial', 'img': 'img/project-5-sm.jpg',
     'alt': 'Rendered curved entry wall and bench at a commercial building',
     'location': 'Gold Coast ' + tbc('suburb'), 'scope': tbc('scope to confirm'), 'builder': tbc('to confirm')},
    {'id': 'hospitality', 'title': 'Hospitality feature wall', 'sectors': 'commercial architectural', 'img': 'img/project-3-sm.jpg',
     'alt': 'Textured plaster feature wall with built-in bench and stools',
     'location': tbc('location'), 'scope': 'Plaster feature wall ' + tbc('confirm'), 'builder': tbc('to confirm')},
    {'id': 'bathroom', 'title': 'Architectural bathroom', 'sectors': 'architectural luxury', 'img': 'img/project-1-sm.jpg',
     'alt': 'Bathroom with a dark polished plaster wall and freestanding bath',
     'location': tbc('location'), 'scope': 'Polished plaster finish ' + tbc('confirm'), 'builder': tbc('to confirm')},
    {'id': 'landscape', 'title': 'Rendered landscape edging', 'sectors': 'luxury', 'img': 'img/project-2-sm.jpg',
     'alt': 'Rendered garden edging around stepping pavers',
     'location': 'Gold Coast ' + tbc('suburb'), 'scope': 'Render to landscape walls ' + tbc('confirm'), 'builder': tbc('to confirm')},
]
PROJ = {p['id']: p for p in PROJECTS}

# ---------------------------------------------------------------- SERVICES
SERVICES = [
    {'slug': 'external-render', 'name': 'External render', 'img': 'img/contact.jpg',
     'short': 'Cement and acrylic render for facades, elevations and boundary walls.',
     'lead': 'Cement and acrylic render for new builds, multi-residential facades and commercial elevations. Finished ready for coating, or as a complete system.',
     'body': [
         'External render is the first thing anyone sees on a building, and it shows every flaw once the light hits it side-on. We render to the substrate and system on your spec, with prep and control joints set out to the manufacturer’s requirements before the first coat goes on.',
         'On larger facades we run enough crew to keep each elevation moving, so the render isn’t what holds up your scaffold.',
     ],
     'where': ['Luxury and coastal homes', 'Multi-residential facades', 'Commercial and retail elevations', 'Boundary, entry and landscape walls'],
     'scope': ['Substrate prep and priming', 'Base coat and finish coat render', 'Control joints to the system spec', 'Ready for coating, or complete with coating'],
     'related': ['miami', 'canal']},
    {'slug': 'internal-solid-plastering', 'name': 'Internal solid plastering', 'img': 'img/project-3.jpg',
     'short': 'Solid plaster to masonry walls for premium homes and commercial interiors.',
     'lead': 'Solid plaster to block and masonry walls for luxury homes, apartments and commercial interiors. Flat, straight and ready for paint or a specialty finish.',
     'body': [
         'Solid plaster gives a harder, more durable wall than sheet lining and suits masonry construction and high-traffic interiors. It is also the base for most specialty finishes, so we set it out with the final finish in mind.',
     ],
     'where': ['Luxury residential interiors', 'Apartments and multi-residential', 'Commercial and hospitality fitouts', 'Base coat for Venetian plaster and feature finishes'],
     'scope': ['Set-out and screeding to level', 'Solid plaster to walls, returns and reveals', 'Corners and junctions', 'Ready for paint or a specialty finish'],
     'related': ['hospitality', 'bathroom']},
    {'slug': 'architectural-coatings', 'name': 'Architectural coatings', 'img': 'img/project-4.jpg',
     'short': 'Specified coating systems for contemporary facades and design-led projects.',
     'lead': 'Architectural coating systems applied to the architect’s specification, from smooth contemporary facades to textured and stone-look finishes.',
     'body': [
         'When an architect specifies a coating system, the finish is part of the design. We apply the named system to the manufacturer’s requirements, and match colour and texture to the approved sample.',
         'Sample panels before full application: ' + tbc('confirm this is offered') + '.',
     ],
     'where': ['Contemporary residential facades', 'Multi-residential and commercial buildings', 'Textured and stone-look facades', 'Design-led fitouts'],
     'scope': ['Substrate and render prep', 'Coating system applied to spec', 'Colour and texture matched to the approved sample', 'System documentation ' + tbc('confirm')],
     'related': ['multistorey', 'coastal']},
    {'slug': 'texture-coatings', 'name': 'Texture coatings', 'img': 'img/project-5.jpg',
     'short': 'Textured render and coating finishes with depth, inside and out.',
     'lead': 'Textured render and coating systems that add depth and character to interior and exterior walls, and hide less-than-perfect substrates better than a flat finish.',
     'body': [
         'Texture coatings range from a fine sand finish to heavy trowelled and bagged textures. We apply them to the system and texture on your spec, and keep the texture consistent across every wall and every day of the job.',
     ],
     'where': ['Residential facades and feature elevations', 'Commercial entries and common areas', 'Hospitality interiors', 'Retaining and boundary walls'],
     'scope': ['Prep and base coat', 'Texture coat to the specified system', 'Consistent texture across large areas', 'Topcoat and sealing to spec'],
     'related': ['commercial-entry', 'landscape']},
    {'slug': 'venetian-plaster', 'name': 'Venetian plaster', 'img': 'img/project-1.jpg',
     'short': 'Hand-applied Venetian plaster with natural stone and marble textures.',
     'lead': 'Hand-applied Venetian and polished plaster for feature walls, bathrooms, hospitality interiors and high-end homes.',
     'body': [
         'Venetian plaster is built up in thin, hand-trowelled layers and burnished to a depth and sheen that paint can’t copy. It relies on a flat, well-prepared substrate, so we plan the base and the finish together.',
     ],
     'where': ['Feature walls and entries', 'Bathrooms and wet-area feature walls ' + tbc('confirm'), 'Hospitality and retail interiors', 'Luxury residential living areas'],
     'scope': ['Substrate prep or solid plaster base', 'Multi-layer hand application', 'Burnishing to the agreed sheen', 'Sealing or waxing to spec'],
     'related': ['bathroom', 'hospitality']},
    {'slug': 'feature-walls', 'name': 'Feature walls', 'img': 'img/project-3.jpg',
     'short': 'Statement plaster and render walls for homes and commercial interiors.',
     'lead': 'Statement plaster and render feature walls for residential and commercial interiors, entries and outdoor areas.',
     'body': [
         'A feature wall gets looked at up close, so the detail matters: clean edges, consistent texture and junctions that don’t catch the light. We work from the designer’s intent and the space it sits in.',
     ],
     'where': ['Entries and foyers', 'Living areas and bedrooms', 'Restaurants, bars and retail', 'Outdoor and landscape walls'],
     'scope': ['Base preparation', 'Plaster, render or coating finish', 'Detailing to edges, niches and joinery', 'Sealing to spec'],
     'related': ['hospitality', 'commercial-entry']},
    {'slug': 'commercial-render-pumping', 'name': 'Commercial render pumping', 'img': 'img/services.jpg',
     'short': 'Machine-applied render for large commercial and multi-residential facades.',
     'lead': 'Pumped render for large areas, where a machine-applied coat keeps a big crew moving and the finish even across the whole building.',
     'body': [
         'On large facades, pumping the render gives an even application across big areas and keeps pace with a commercial program. The crew follows the pump to screed and finish, so the result is the same on every elevation.',
     ],
     'where': ['Multi-storey residential', 'Commercial buildings', 'Large boundary and retaining walls', 'Staged and multi-site programs'],
     'scope': ['Pump set-up and material handling', 'Machine-applied base coat', 'Screeding and hand finishing', 'Coordination with scaffold and program'],
     'related': ['multistorey', 'canal']},
    {'slug': 'repairs-restoration', 'name': 'Repairs and restoration', 'img': 'img/ig-4.jpg',
     'short': 'Render and plaster repairs matched to the existing finish.',
     'lead': 'Repairs to cracked, drummy or damaged render and plaster, matched to the existing finish. For builders on renovation jobs, building managers and homeowners.',
     'body': [
         'Most repair work comes down to matching the texture, profile and colour of what is already there. We look at why it failed before we patch, so the repair lasts instead of cracking again.',
     ],
     'where': ['Renovations and extensions', 'Strata and building maintenance', 'Pre-sale and pre-painting repairs', 'Heritage and older homes'],
     'scope': ['Inspection of the failed area', 'Removal of loose and drummy render', 'Repair to match the existing finish', 'Ready for paint or coating'],
     'related': ['coastal', 'landscape']},
]
SVC = {s['slug']: s for s in SERVICES}

IG = [
    ('https://www.instagram.com/coast_side_plastering/reel/DYB-mexTDvU/', 'img/ig-1.jpg', 'Coastal home at Brakes Crescent, Miami'),
    ('https://www.instagram.com/coast_side_plastering/reel/DbHRJIUTJUs/', 'img/ig-2.jpg', 'Waterfront luxury build, Gold Coast'),
    ('https://www.instagram.com/coast_side_plastering/p/DYB5wBUk21X/', 'img/ig-3.jpg', 'Finished rendered coastal home'),
    ('https://www.instagram.com/coast_side_plastering/p/DaeHVZozc-N/', 'img/ig-4.jpg', 'Coastside crew walking a finished rendered corridor'),
    ('https://www.instagram.com/coast_side_plastering/p/DaShOf0zg-y/', 'img/ig-5.jpg', 'Coastside crew rendering on site'),
    ('https://www.instagram.com/coast_side_plastering/p/DZ3-sHqk29D/', 'img/ig-6.jpg', 'Coastside crew rendering from scaffolding'),
]


# ================================================================= PARTS
def project_card(p, L, heading='h3'):
    sec = ' '.join(SECTOR_NAME[k] for k in p['sectors'].split())
    return f'''<article class="proj" data-sector="{p['sectors']}">
  <div class="proj-img"><img src="{L(p['img'])}" alt="{html.escape(p['alt'])}" loading="lazy"></div>
  <div class="proj-sector">{' / '.join(SECTOR_NAME[k] for k in p['sectors'].split())}</div>
  <{heading}>{p['title']}</{heading}>
  <dl>
    <dt>Builder</dt><dd>{p['builder']}</dd>
    <dt>Scope</dt><dd>{p['scope']}</dd>
    <dt>Location</dt><dd>{p['location']}</dd>
  </dl>
</article>'''


def svc_cards(L, dark=False):
    out = []
    for i, s in enumerate(SERVICES, 1):
        out.append(f'''<a class="svc-card" href="{L('services/' + s['slug'] + '/')}">
  <span class="svc-num">{i:02d}</span>
  <h3>{s['name']}</h3>
  <p>{s['short']}</p>
  <span class="more">View service</span>
</a>''')
    return f'<div class="svc-grid fade-up">{"".join(out)}</div>'


def steps():
    return f'''<div class="steps fade-up">
  <div class="step"><h3>Send the plans</h3><p>Drawings, elevations and the finish spec. A Dropbox or Google Drive link is fine.</p></div>
  <div class="step"><h3>Get an itemised quote</h3><p>Priced to your spec and your program. Turnaround {tbc('to confirm')}.</p></div>
  <div class="step"><h3>Lock in the program</h3><p>Start dates and crew numbers agreed before we mobilise, so you know who is on site and when.</p></div>
  <div class="step"><h3>Finish and hand over</h3><p>Walk-through with your site manager and defects closed out before we leave {tbc('confirm')}.</p></div>
</div>'''


def brands():
    return '<div class="brands-row">' + ''.join(f'<span class="brand-logo">{b}</span>' for b in SYSTEMS) + '</div>'


def cta_band(L, title='Pricing a job? Send the plans.',
             text='Tell us the project, the finish and the program. We come back with an itemised price.',
             img=None):
    return f'''<section class="cta-band">
  <div class="inner">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btns">
      <a class="btn btn-primary" href="{L('quote/')}">Request a quote</a>
      <a class="btn btn-outline" href="{L('builder-pack/')}">Get the builder pack</a>
    </div>
  </div>
</section>'''


def page_hero(L, eyebrow, h1, lead, img, crumbs=None, caption=''):
    cr = ''
    if crumbs:
        cr = '<div class="crumbs">' + ' / '.join(f'<a href="{L(p)}">{t}</a>' if p is not None else t for p, t in crumbs) + '</div>'
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'''<section class="page-hero">
  <div class="inner">
    {cr}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
<figure class="photo-band"><img src="{L(img)}" alt="">{cap}</figure>'''


def form_open(L, subject, success, extra_class=''):
    return f'''<form class="form {extra_class}" action="https://api.web3forms.com/submit" method="POST" data-ajax data-success="{html.escape(success)}">
  <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
  <input type="hidden" name="subject" value="{html.escape(subject)}">
  <input type="hidden" name="from_name" value="Coastside website">
  <div class="hp" aria-hidden="true"><input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></div>'''


# ================================================================= PAGES
def home(link):
    def body(d):
        L = lambda p: link(p, d)
        strip = ''.join(f'<a href="{L("services/" + s["slug"] + "/")}">{s["name"]}</a>' for s in SERVICES)
        sectors = ''.join(f'''<a class="sector-card" href="{L('projects/')}#{s['key']}">
  <div class="sector-img"><img src="{L(s['img'])}" alt="" loading="lazy"></div>
  <h3>{s['name']}</h3><p>{s['blurb']}</p><span class="arrow">See projects</span>
</a>''' for s in SECTORS)
        projs = ''.join(project_card(PROJ[k], L) for k in ['miami', 'multistorey', 'commercial-entry'])
        ig = ''.join(f'<a class="ig-tile" href="{u}" target="_blank" rel="noopener"><img src="{L(i)}" alt="{a}" loading="lazy"></a>' for u, i, a in IG)
        return f'''
<section class="hero">
  <div class="hero-content">
    <span class="eyebrow">Solid plastering, render and architectural coatings</span>
    <h1>Finish matters.<br>So does turning up.</h1>
    <div class="hero-row">
      <p class="lead">A 15+ crew for builders, architects and designers from Byron Bay to South East Brisbane. Residential, multi-residential and commercial, finished to the spec and on your program.</p>
      <div class="hero-btns">
        <a href="{L('quote/')}" class="btn btn-primary">Request a quote</a>
        <a href="{L('builder-pack/')}" class="btn btn-outline">Get the builder pack</a>
      </div>
    </div>
  </div>
</section>
<figure class="photo-band photo-band-hero"><img src="{L('img/hero.jpg')}" alt="White rendered coastal home with timber battens, Gold Coast"><figcaption>Coastal residence, Gold Coast</figcaption></figure>
<div class="fact-bar">
  <div><strong>25+ years</strong>In the trade</div>
  <div><strong>15+ crew</strong>On the tools</div>
  <div><strong>Byron to Brisbane</strong>Service area</div>
  <div><strong>QBCC licensed</strong>{tbc('licence no.')}</div>
</div>


<section class="sec sec-dark" id="builder-check">
  <div class="wrap">
    <div class="head fade-up">
      <span class="eyebrow">The builder check</span>
      <h2>What you check before you call.<br>Answered on one screen.</h2>
      <p class="lead-body">Working with Coastside for the first time? These are the questions most builders ask before a first job. The details and paperwork are in the builder pack.</p>
    </div>
    <div class="check-grid fade-up">
      <div class="check-item"><div class="check-q">Licensed?</div><div class="check-a">QBCC licensed</div><div class="check-note">Licence {tbc('class and number')}, checkable on the QBCC register.</div></div>
      <div class="check-item"><div class="check-q">Insured?</div><div class="check-a">Public liability {tbc('cover')}</div><div class="check-note">Certificates of currency for public liability and workers compensation {tbc('insurer')} sent on request.</div></div>
      <div class="check-item"><div class="check-q">Enough crew?</div><div class="check-a">15+ on the tools</div><div class="check-note">Enough people to run residential and commercial sites at the same time.</div></div>
      <div class="check-item"><div class="check-q">Right systems?</div><div class="check-a">{', '.join(SYSTEMS[:-1])} and {SYSTEMS[-1]}</div><div class="check-note">Tell us the system on your spec and we price to it.</div></div>
      <div class="check-item"><div class="check-q">Done this before?</div><div class="check-a">Luxury, multi-residential, commercial</div><div class="check-note"><a href="{L('projects/')}" style="color:var(--white)">Projects by sector</a>, with the builder named where they have agreed.</div></div>
      <div class="check-item"><div class="check-q">Safe on site?</div><div class="check-a">SWMS for each job</div><div class="check-note">Site-specific safety paperwork supplied before start {tbc('confirm')}.</div></div>
    </div>
    <div class="check-foot fade-up">
      <p>All of this in one PDF, ready to file with your pre-start paperwork.</p>
      <a class="btn btn-primary" href="{L('builder-pack/')}">Get the builder pack</a>
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="head fade-up">
      <span class="eyebrow">Who we work for</span>
      <h2>Four kinds of job.<br>One standard of finish.</h2>
    </div>
    <div class="sector-grid fade-up">{sectors}</div>
  </div>
</section>

<section class="sec sec-cream">
  <div class="wrap">
    <div class="head head-split fade-up">
      <div><span class="eyebrow">Selected work</span><h2>Recent projects</h2></div>
      <a class="text-link" href="{L('projects/')}">All projects by sector</a>
    </div>
    <div class="proj-grid fade-up">{projs}</div>
  </div>
</section>

<section class="sec sec-stone">
  <div class="wrap">
    <div class="head fade-up">
      <span class="eyebrow">How it works</span>
      <h2>How a job runs with Coastside</h2>
    </div>
    {steps()}
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="head head-split fade-up">
      <div><span class="eyebrow">Services</span><h2>What we do</h2></div>
      <a class="text-link" href="{L('services/')}">All services</a>
    </div>
    {svc_cards(L)}
  </div>
</section>

<section class="sec sec-dark">
  <div class="wrap split">
    <div class="split-img fade-up"><img src="{L('img/ig-5.jpg')}" alt="Coastside plasterer rendering from scaffolding" loading="lazy"></div>
    <div class="fade-up">
      <span class="eyebrow">About</span>
      <h2>Second-generation plasterer. 25+ years on the tools.</h2>
      <p class="lead-body" style="margin-bottom:24px">Steve grew up in the trade and now runs a 15+ crew across residential and commercial sites every week. From architectural coatings to large-scale commercial pumping, it is the same standard every time.</p>
      <p class="lead-body" style="margin-bottom:36px">Clean finishes. Reliable crews. Jobs finished on time.</p>
      <a class="btn btn-outline" href="{L('about/')}">About Coastside</a>
    </div>
  </div>
</section>

<section class="sec sec-stone">
  <div class="wrap">
    <div class="head head-split fade-up">
      <div><span class="eyebrow">Straight off the tools</span><h2>Latest work</h2></div>
      <a class="text-link" href="{INSTAGRAM}" target="_blank" rel="noopener">@coast_side_plastering</a>
    </div>
    <div class="ig-grid fade-up">{ig}</div>
  </div>
</section>

<section class="sec sec-warm" style="padding-top:72px;padding-bottom:72px">
  <div class="wrap fade-up" style="text-align:center">
    <span class="eyebrow">Systems we apply</span>
    <div style="margin-top:28px">{brands()}</div>
  </div>
</section>

{cta_band(L)}'''
    schema = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness",
              "name": "Coastside Solid Plastering", "legalName": LEGAL_NAME, "taxID": ABN,
              "description": "Solid plastering, external render and architectural coatings for builders, architects and designers from Byron Bay to South East Brisbane.",
              "telephone": PHONE_TEL, "email": EMAIL,
              "address": {"@type": "PostalAddress", "addressLocality": "Gold Coast", "addressRegion": "QLD", "addressCountry": "AU"},
              "areaServed": ["Gold Coast", "Byron Bay", "Tweed Heads", "Brisbane"],
              "sameAs": [INSTAGRAM],
              "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services",
                                  "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s['name']}} for s in SERVICES]}}
    return {'path': '', 'title': 'Coastside Solid Plastering | Solid plastering and render for builders, Gold Coast',
            'description': 'Solid plastering, external render and architectural coatings for builders, architects and designers from Byron Bay to South East Brisbane. 15+ crew, 25+ years.',
            'body': body, 'schema': schema}


def projects(link):
    def body(d):
        L = lambda p: link(p, d)
        filters = '<button class="filter" data-filter="all" aria-pressed="true">All</button>' + ''.join(
            f'<button class="filter" data-filter="{s["key"]}" aria-pressed="false">{s["name"]}</button>' for s in SECTORS)
        cards = ''.join(project_card(p, L, 'h2') for p in PROJECTS)
        return f'''{page_hero(L, 'Projects', 'Work by sector.', 'Luxury residential, multi-residential, commercial and hospitality. Each project lists the scope and, where they have agreed, the builder or architect we did it for.', 'img/project-4.jpg')}
<section class="sec sec-warm">
  <div class="wrap">
    <div class="filters fade-up" role="group" aria-label="Filter projects by sector">{filters}</div>
    <div class="proj-grid fade-up">{cards}</div>
  </div>
</section>
<section class="sec sec-stone" style="padding-top:88px;padding-bottom:88px">
  <div class="wrap head-split fade-up">
    <div><span class="eyebrow">For builders</span><h2 style="margin-bottom:10px">Need references?</h2><p class="lead-body">The builder pack lists key projects and trade references you can call.</p></div>
    <a class="btn btn-dark" href="{L('builder-pack/')}">Get the builder pack</a>
  </div>
</section>
{cta_band(L)}'''
    return {'path': 'projects/', 'title': 'Projects | Coastside Solid Plastering',
            'description': 'Solid plastering, render and architectural coating projects across luxury residential, multi-residential, commercial and hospitality on the Gold Coast.',
            'body': body, 'active': 'projects/', 'og_image': 'img/project-4.jpg'}


def services_hub(link):
    def body(d):
        L = lambda p: link(p, d)
        return f'''{page_hero(L, 'Services', 'Solid plastering, render and architectural coatings.', 'Eight services, one crew. Priced to your spec, applied to the system manufacturer’s requirements and finished to a standard that holds up side-on in full sun.', 'img/services.jpg')}
<section class="sec sec-warm">
  <div class="wrap">{svc_cards(L)}</div>
</section>
<section class="sec sec-stone">
  <div class="wrap">
    <div class="head fade-up"><span class="eyebrow">How it works</span><h2>How a job runs with Coastside</h2></div>
    {steps()}
  </div>
</section>
<section class="sec sec-warm" style="padding-top:72px;padding-bottom:72px">
  <div class="wrap fade-up" style="text-align:center"><span class="eyebrow">Systems we apply</span><div style="margin-top:28px">{brands()}</div></div>
</section>
{cta_band(L)}'''
    return {'path': 'services/', 'title': 'Services | Solid plastering, render and coatings | Coastside',
            'description': 'External render, internal solid plastering, architectural and texture coatings, Venetian plaster, feature walls, commercial render pumping and repairs. Gold Coast to Byron Bay and Brisbane.',
            'body': body, 'active': 'services/', 'og_image': 'img/services.jpg'}


def service_page(link, s):
    def body(d):
        L = lambda p: link(p, d)
        paras = ''.join(f'<p>{p}</p>' for p in s['body'])
        where = ''.join(f'<li>{w}</li>' for w in s['where'])
        scope = ''.join(f'<li>{w}</li>' for w in s['scope'])
        rel = ''.join(project_card(PROJ[k], L) for k in s['related'])
        others = ''.join(f'<li><a href="{L("services/" + o["slug"] + "/")}" style="color:var(--white);text-decoration:none">{o["name"]}</a></li>' for o in SERVICES if o['slug'] != s['slug'])
        return f'''{page_hero(L, 'Service', s['name'] + ' on the Gold Coast', s['lead'], s['img'], crumbs=[('', 'Home'), ('services/', 'Services'), (None, s['name'])])}
<section class="sec sec-warm">
  <div class="wrap split wide-left">
    <div class="prose fade-up">
      {paras}
      <h2>Where we use it</h2>
      <ul>{where}</ul>
      <h2>What is in our scope</h2>
      <ul>{scope}</ul>
      <h2>Systems</h2>
      <p>{', '.join(SYSTEMS[:-1])} and {SYSTEMS[-1]}. If your spec names a system, we price and apply that system.</p>
    </div>
    <aside class="aside-box sticky fade-up">
      <h3>To price {s['name'].lower()}, send us:</h3>
      <ul>
        <li><strong>Plans and elevations</strong>With the areas to be finished marked up.</li>
        <li><strong>The finish spec</strong>System, colour and texture, if chosen.</li>
        <li><strong>Your program</strong>Target start and how long you have.</li>
        <li><strong>Site access</strong>Scaffold, levels and who supplies what.</li>
      </ul>
      <a class="btn btn-primary" href="{L('quote/')}" style="width:100%;text-align:center">Request a quote</a>
      <p style="margin-top:18px;font-size:14px">New to Coastside? <a href="{L('builder-pack/')}">Get the builder pack</a>.</p>
    </aside>
  </div>
</section>
<section class="sec sec-cream">
  <div class="wrap">
    <div class="head head-split fade-up"><div><span class="eyebrow">Related work</span><h2>Projects</h2></div><a class="text-link" href="{L('projects/')}">All projects</a></div>
    <div class="proj-grid two fade-up">{rel}</div>
  </div>
</section>
<section class="sec sec-dark" style="padding-top:88px;padding-bottom:88px">
  <div class="wrap">
    <span class="eyebrow">Other services</span>
    <ul class="other-svcs">{others}</ul>
  </div>
</section>
{cta_band(L)}'''
    schema = {"@context": "https://schema.org", "@type": "Service", "name": s['name'], "serviceType": s['name'],
              "description": s['short'], "areaServed": ["Gold Coast", "Byron Bay", "Brisbane"],
              "provider": {"@type": "HomeAndConstructionBusiness", "name": "Coastside Solid Plastering", "telephone": PHONE_TEL}}
    return {'path': f"services/{s['slug']}/", 'title': f"{s['name']} Gold Coast | Coastside Solid Plastering",
            'description': s['lead'][:155], 'body': body, 'active': 'services/', 'og_image': s['img'], 'schema': schema}


def about(link):
    def body(d):
        L = lambda p: link(p, d)
        return f'''{page_hero(L, 'About', 'Second-generation plasterer. 15+ crew. One standard.', 'Coastside is Steve’s business: a solid plastering and render crew working for builders, architects and designers from Byron Bay to South East Brisbane.', 'img/contact.jpg')}
<section class="sec sec-warm">
  <div class="wrap split">
    <div class="split-img fade-up"><img src="{L('img/steve.jpg')}" alt="Steve, owner of Coastside Solid Plastering, on a finished job" style="object-position:62% center"></div>
    <div class="prose fade-up">
      <span class="eyebrow">Steve</span>
      <h2>Built on experience. Backed by scale.</h2>
      <p>From a second-generation plasterer to running a 15+ crew, Steve and the team deliver high-quality finishes across residential and commercial projects every week.</p>
      <p>From architectural coatings to large-scale commercial pumping, it is the same standard every time: clean finishes, reliable crews and jobs completed on time.</p>
      <p>The work runs from high-end homes to multi-site commercial projects, from Byron Bay to the Gold Coast to South East Brisbane. The focus stays the same.</p>
      <div class="stat-row" style="margin-top:40px;padding-top:36px;border-top:1px solid var(--sand)">
        <div><div class="stat-num">25+</div><div class="stat-label">Years in the trade</div></div>
        <div><div class="stat-num">15+</div><div class="stat-label">Crew</div></div>
        <div><div class="stat-num">3</div><div class="stat-label">Regions</div></div>
      </div>
      <p style="margin-top:28px;font-size:14px">Projects completed: {tbc('number to confirm')}</p>
    </div>
  </div>
</section>
<section class="sec sec-dark">
  <div class="wrap">
    <div class="head fade-up"><span class="eyebrow">What builders get</span><h2>Why builders use Coastside</h2></div>
    <div class="steps fade-up" style="counter-reset:none">
      <div class="step"><h3>Crew depth</h3><p>15+ qualified plasterers, enough to run more than one site without stretching a crew thin.</p></div>
      <div class="step"><h3>Commercial capability</h3><p>The people and the pump for multi-storey and commercial facades, without dropping the finish.</p></div>
      <div class="step"><h3>Residential detail</h3><p>Architectural coatings, Venetian plaster and feature walls for high-end homes.</p></div>
      <div class="step"><h3>Straight answers</h3><p>Clear pricing, agreed start dates and crew numbers you can plan around.</p></div>
    </div>
  </div>
</section>
<section class="sec sec-stone">
  <div class="wrap">
    <div class="head fade-up"><span class="eyebrow">The crew</span><h2>On the tools</h2></div>
    <div class="ig-grid grid-4 fade-up">
      <div class="ig-tile"><img src="{L('img/ig-4.jpg')}" alt="Coastside crew member walking a finished rendered corridor" loading="lazy"></div>
      <div class="ig-tile"><img src="{L('img/ig-5.jpg')}" alt="Coastside plasterer working from scaffolding" loading="lazy"></div>
      <div class="ig-tile"><img src="{L('img/ig-6.jpg')}" alt="Two Coastside plasterers rendering a wall" loading="lazy"></div>
      <div class="ig-tile"><img src="{L('img/services-sm.jpg')}" alt="Coastside crew pumping and finishing render" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="sec sec-warm">
  <div class="wrap split">
    <div class="fade-up">
      <span class="eyebrow">Service area</span>
      <h2>Byron Bay to South East Brisbane</h2>
      <p class="lead-body">Based on the Gold Coast, working across three regions.</p>
    </div>
    <div class="fade-up">
      <table class="facts">
        <tr><th>Northern Rivers NSW</th><td>Byron Bay and the Tweed {tbc('confirm areas and NSW licence')}</td></tr>
        <tr><th>Gold Coast</th><td>Gold Coast and hinterland</td></tr>
        <tr><th>South East Brisbane</th><td>{tbc('suburbs to confirm')}</td></tr>
      </table>
    </div>
  </div>
</section>
<section class="sec sec-stone">
  <div class="wrap">
    <div class="head fade-up"><span class="eyebrow">How it works</span><h2>How a job runs with Coastside</h2></div>
    {steps()}
  </div>
</section>
{cta_band(L)}'''
    return {'path': 'about/', 'title': 'About | Coastside Solid Plastering',
            'description': 'Coastside Solid Plastering: a second-generation plasterer running a 15+ crew for builders, architects and designers from Byron Bay to South East Brisbane.',
            'body': body, 'active': 'about/', 'og_image': 'img/steve.jpg'}


def builder_pack(link):
    def body(d):
        L = lambda p: link(p, d)
        return f'''{page_hero(L, 'Builder pack', 'Everything your pre-start asks for. In one place.', 'Licence, insurances, safety paperwork, systems and references for builders and project managers bringing Coastside onto a job. Download the capability statement, or ask for the certificates and we send them through.', 'img/project-4.jpg')}
<section class="sec sec-warm">
  <div class="wrap split wide-left">
    <div class="fade-up">
      <span class="eyebrow">At a glance</span>
      <h2>Company details</h2>
      <table class="facts" style="margin-top:28px">
        <tr><th>Business</th><td>{LEGAL_NAME}<small>Trading as Coastside Solid Plastering {tbc('confirm trading entity')}</small></td></tr>
        <tr><th>ABN</th><td>{ABN}</td></tr>
        <tr><th>QBCC licence</th><td>{tbc('licence number and class')}<small>Check it on the QBCC online licence search.</small></td></tr>
        <tr><th>NSW licence</th><td>{tbc('confirm if held for Northern Rivers work')}</td></tr>
        <tr><th>Public liability</th><td>{tbc('cover amount and insurer')}<small>Certificate of currency on request.</small></td></tr>
        <tr><th>Workers compensation</th><td>{tbc('WorkCover Queensland policy')}<small>Certificate of currency on request.</small></td></tr>
        <tr><th>Safety</th><td>SWMS supplied for each job {tbc('confirm')}<small>WHS management approach {tbc('confirm')}</small></td></tr>
        <tr><th>Crew</th><td>15+ plasterers</td></tr>
        <tr><th>Systems</th><td>{', '.join(SYSTEMS)}</td></tr>
        <tr><th>Service area</th><td>{AREA}</td></tr>
        <tr><th>Sectors</th><td>Luxury residential, multi-residential, commercial, hospitality</td></tr>
        <tr><th>Trade references</th><td>{tbc('2 to 3 builders or designers, with permission')}</td></tr>
        <tr><th>Accounts contact</th><td>{tbc('name and email')}</td></tr>
      </table>
    </div>
    <div class="sticky fade-up">
      <span class="eyebrow">Documents</span>
      <div class="doc-list">
        <div class="doc"><div class="doc-ico">PDF</div><div><h3>Capability statement</h3><p>Two pages: who we are, crew, systems, sectors, compliance and key projects.</p><a class="text-link" href="coastside-capability-statement.pdf" download>Download PDF</a></div></div>
        <div class="doc"><div class="doc-ico">PDF</div><div><h3>Certificates of currency</h3><p>Public liability and workers compensation. Sent on request so you always get the current certificates.</p><a class="text-link" href="#request">Request certificates</a></div></div>
        <div class="doc"><div class="doc-ico">PDF</div><div><h3>SWMS</h3><p>Safe work method statements for rendering and work at height, made site-specific for your job {tbc('confirm')}.</p><a class="text-link" href="#request">Request SWMS</a></div></div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-stone" id="request">
  <div class="wrap split">
    <div class="fade-up">
      <span class="eyebrow">Request paperwork</span>
      <h2>Tell us what you need</h2>
      <p class="lead-body">Pick the documents and the project they are for. We email them to you.</p>
    </div>
    <div class="panel fade-up">
      {form_open(L, 'Builder pack request - Coastside website', 'Thanks. We will email the documents to you.')}
        <div class="form-row">
          <div class="field"><label for="bp-name">Name</label><input id="bp-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="bp-company">Company</label><input id="bp-company" name="company" autocomplete="organization" required></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="bp-email">Email</label><input id="bp-email" type="email" name="email" autocomplete="email" required></div>
          <div class="field"><label for="bp-project">Project <span class="opt">(optional)</span></label><input id="bp-project" name="project"></div>
        </div>
        <fieldset class="field">
          <legend>Documents</legend>
          <div class="checks">
            <label><input type="checkbox" data-group="documents" value="Certificates of currency" checked> Certificates of currency</label>
            <label><input type="checkbox" data-group="documents" value="QBCC licence details"> QBCC licence details</label>
            <label><input type="checkbox" data-group="documents" value="SWMS"> SWMS</label>
            <label><input type="checkbox" data-group="documents" value="Trade references"> Trade references</label>
          </div>
        </fieldset>
        <div class="form-status" role="status" aria-live="polite"></div>
        <button type="submit" class="btn btn-primary form-submit">Send request</button>
      </form>
    </div>
  </div>
</section>
{cta_band(L, 'Ready to price the job?', 'Send the plans with the spec and program and we come back with an itemised quote.')}'''
    return {'path': 'builder-pack/', 'title': 'Builder pack | Licence, insurance and capability | Coastside',
            'description': 'Coastside Solid Plastering builder pack: licence, insurances, SWMS, systems, service area and the capability statement PDF for builders and project managers.',
            'body': body, 'active': 'builder-pack/', 'og_image': 'img/project-4.jpg'}


def quote(link):
    def body(d):
        L = lambda p: link(p, d)
        sectors = ''.join(f'<option>{o}</option>' for o in ['Luxury residential', 'Residential', 'Multi-residential', 'Commercial', 'Hospitality', 'Other'])
        types = ''.join(f'<option>{o}</option>' for o in ['New build', 'Renovation / extension', 'Commercial fitout', 'Multi-residential', 'Repairs & restoration', 'Maintenance', 'Other'])
        svcs = ''.join(f'<label><input type="checkbox" data-group="services" value="{s["name"]}"> {s["name"]}</label>' for s in SERVICES)
        return f'''{page_hero(L, 'Request a quote', 'Send the job through.', 'The more we know about the scope, the finish and the program, the faster and tighter the price.', 'img/contact.jpg')}
<section class="sec sec-warm">
  <div class="wrap split wide-left">
    <div class="panel fade-up">
      {form_open(L, 'Quote request - Coastside website', 'Thanks. Your enquiry is with Steve and he will be in touch to talk through the job.')}
        <div class="form-row">
          <div class="field"><label for="q-name">Name</label><input id="q-name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="q-company">Company / builder <span class="opt">(if applicable)</span></label><input id="q-company" name="company" autocomplete="organization"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="q-email">Email</label><input id="q-email" type="email" name="email" autocomplete="email" required></div>
          <div class="field"><label for="q-phone">Phone</label><input id="q-phone" type="tel" name="phone" autocomplete="tel"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="sector">Sector</label><select id="sector" name="sector"><option value="">Select</option>{sectors}</select></div>
          <div class="field"><label for="q-type">Project type</label><select id="q-type" name="project_type"><option value="">Select</option>{types}</select></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="q-loc">Project location</label><input id="q-loc" name="project_location" placeholder="Suburb"></div>
          <div class="field"><label for="q-start">Target start</label><select id="q-start" name="target_start"><option value="">Select</option><option>Pricing only for now</option><option>Within a month</option><option>1 to 3 months</option><option>3 months or more</option></select></div>
        </div>
        <fieldset class="field">
          <legend>Services needed <span class="opt" style="text-transform:none;letter-spacing:0">(tick any)</span></legend>
          <div class="checks">{svcs}</div>
        </fieldset>
        <div class="form-row">
          <div class="field"><label for="q-value">Estimated value <span class="opt">(optional)</span></label><input id="q-value" name="estimated_value" placeholder="e.g. $85k"></div>
          <div class="field"><label for="q-plans">Link to plans <span class="opt">(optional)</span></label><input id="q-plans" type="url" name="plans_link" placeholder="Dropbox or Google Drive link"></div>
        </div>
        <div class="field"><label for="q-msg">Project details</label><textarea id="q-msg" name="message" placeholder="Scope, finish or system on the spec, access, anything else we should know." required></textarea></div>
        <div class="checks" style="grid-template-columns:1fr"><label><input type="checkbox" id="need-docs" data-group="also_send" value="Builder pack and certificates of currency"> Also send me the builder pack and certificates of currency</label></div>
        <div class="form-status" role="status" aria-live="polite"></div>
        <button type="submit" class="btn btn-primary form-submit">Send enquiry</button>
        <p class="form-note">Your details go to Coastside only and are used to reply to this enquiry.</p>
      </form>
    </div>
    <aside class="aside-box sticky fade-up">
      <h3>To price it quickly, send:</h3>
      <ul>
        <li><strong>Plans and elevations</strong>With the areas to be finished marked up.</li>
        <li><strong>The finish spec</strong>System, colour and texture, if chosen.</li>
        <li><strong>Your program</strong>Target start and how long you have.</li>
        <li><strong>Site access</strong>Scaffold, levels and who supplies what.</li>
      </ul>
      <p style="font-size:14px;line-height:1.8">Prefer email? <a href="mailto:{EMAIL}">{EMAIL}</a><br>Phone {PHONE}</p>
    </aside>
  </div>
</section>'''
    return {'path': 'quote/', 'title': 'Request a quote | Coastside Solid Plastering',
            'description': 'Send plans and scope to Coastside Solid Plastering for an itemised quote on solid plastering, render and architectural coatings.',
            'body': body, 'og_image': 'img/contact.jpg'}


def build_pages(link):
    pages = [home(link), projects(link), services_hub(link), about(link), builder_pack(link), quote(link)]
    pages += [service_page(link, s) for s in SERVICES]
    return pages
