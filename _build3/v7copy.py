"""V7 content layer (Mel's commercial copy, 24 Sep 2026).

install(globals()) from build.py swaps in V7 page templates. V2 to V6 are
unaffected because they are built without THEME=v7.
Rules: Australian English, no em dashes, unconfirmed facts stay as tbc() chips.
"""

ARROW = ' <span aria-hidden="true">&rarr;</span>'

HOME_SERVICES = [
    ('external-rendering', 'External rendering',
     ['Complete external rendering packages across masonry, concrete and approved substrate systems.',
      'From preparation through to final texture and coating, we work to the specified system and architectural finish.']),
    ('commercial-rendering', 'Commercial rendering',
     ['Large-scale rendering packages supported by crew capacity, machine application and structured project delivery.',
      'Built for projects where output, consistency and program matter.']),
    ('solid-plastering', 'Solid plastering',
     ['Traditional solid plaster systems delivered across high-end residential, multi-residential and commercial construction.',
      'Careful substrate preparation and accurate application create the foundation for the final finish.']),
    ('architectural-coatings', 'Architectural coatings',
     ['Specified texture and coating systems for architectural facades, feature elements and design-led projects.',
      'Applied according to system requirements and the intended architectural finish.']),
    ('venetian-plaster', 'Venetian plaster',
     ['Specialist hand-applied finishes for premium residential, hospitality and commercial interiors.',
      'Built in layers to create depth, movement and a finish unique to the surface.']),
]

CAPABILITY = [
    ('15+ crew', 'Enough people on the tools to resource substantial packages, respond to changing site requirements and maintain momentum across staged works.'),
    ('Pumped render', 'Machine-applied render gives us the capacity to cover large elevations efficiently while maintaining consistency across the facade.'),
    ('Commercial systems', 'Experience working with specified systems from leading manufacturers including Dulux AcraTex, Rockcote, Unitex, Resene and Boral.'),
    ('Project delivery', 'Programming, sequencing, access, substrate readiness and coordination with other trades are considered before mobilisation.'),
    ('Documentation', 'Licensing, insurance, SWMS, certificates and supporting project documentation available for commercial procurement requirements.'),
    ('Regional capacity', 'Gold Coast based, with projects delivered throughout South East Queensland and Northern New South Wales.'),
]

PROCESS = [
    ('Send the project', ['Send through the drawings, elevations, finish schedule, specification and relevant construction program.',
                          'Tender documentation can be supplied directly or via your document platform.']),
    ('Scope review', ['We review quantities, substrates, nominated systems, access, architectural details and the proposed sequence of works.',
                      'Where something isn’t clear, we’ll raise it before pricing rather than make assumptions that become variations later.']),
    ('Proposal', ['You’ll receive a clearly defined proposal outlining the package we’ve priced, inclusions and relevant exclusions.']),
    ('Program', ['Once engaged, we coordinate commencement, crew requirements, material supply and sequencing against the construction program.']),
    ('Delivery', ['The crew mobilises and works through the agreed package in coordination with site management and surrounding trades.']),
    ('Handover', ['Works are reviewed, outstanding items addressed and the package prepared for handover.']),
]

AREAS = ['Gold Coast', 'Brisbane', 'Logan', 'Redlands', 'Tweed Coast', 'Kingscliff', 'Casuarina', 'Byron Bay', 'Northern Rivers']

# Per-service page copy. Each block: (eyebrow, heading, [paragraphs], [bullets], [after paragraphs])
SERVICE_COPY = {
    'commercial-rendering': {
        'h1': 'Commercial Rendering', 'title': 'Built to deliver the package.',
        'intro': ['Large rendering packages require more than additional people on site.', 'They require planning.',
                  'Labour needs to align with the construction program. Materials need to arrive when they’re required. Access needs to be coordinated. Substrates need to be ready. Elevations need to be sequenced around other trades.',
                  'Coastside has built the crew, equipment and project systems required to deliver substantial rendering packages without losing control of the finish.'],
        'cta': 'Send us your tender',
        'blocks': [
            ('Capacity', 'Scale without losing control.',
             ['With 15+ crew on the tools, Coastside can resource substantial packages and stage labour around the requirements of the project.',
              'Machine-applied render provides additional output across large elevations, while experienced tradespeople maintain the detailing and finish required around openings, junctions, architectural elements and interfaces.',
              'The objective isn’t simply to put more people on site.',
              'It’s to deploy the right crew, in the right areas, at the right stage of the build.'], [], []),
            ('Project delivery', 'Part of the construction program.',
             ['Rendering rarely happens in isolation.',
              'Our work needs to coordinate with scaffold, waterproofing, windows, roofing, external services, painting, landscaping and multiple other trades.',
              'We review those dependencies before work starts so the package can be programmed around the broader build.',
              'That means clearer sequencing, fewer surprises and a better chance of keeping the project moving.'], [], []),
        ],
        'grid': ('Commercial capability', [
            ('Large facade packages', 'Crew and equipment capacity for substantial external rendering works.'),
            ('Multi-residential', 'Structured delivery across repeated elevations, stages and building zones.'),
            ('Commercial projects', 'Rendering and coating packages delivered within commercial site and documentation requirements.'),
            ('Architectural projects', 'Detailed finishes where texture, junctions, shadow lines and specification are integral to the design.'),
            ('Machine application', 'Pumped render capability for efficient application across large areas.'),
            ('Project documentation', 'SWMS, insurance, licensing and supporting documentation available before mobilisation.'),
        ]),
    },
    'external-rendering': {
        'h1': 'External Rendering', 'title': 'Built from the substrate out.',
        'intro': ['A good rendered finish starts long before the final coat.',
                  'We assess the substrate, nominated system, preparation requirements, junctions, openings and architectural details before application begins.',
                  'Coastside delivers complete external rendering packages across high-end residential, multi-residential and commercial projects.'],
        'cta': 'Send us your plans',
        'blocks': [
            ('What we deliver', 'Our external rendering scope can include:', [],
             ['Substrate assessment and preparation', 'Beads, trims and architectural details', 'Base coat systems', 'Reinforcement where specified',
              'Cement and acrylic render systems', 'Texture coatings', 'Specified architectural finishes', 'Machine-applied render', 'Facade and elevation packages'],
             ['The exact system is determined by the project documentation, substrate and manufacturer specification.']),
            ('Why it matters', 'What sits underneath matters.',
             ['A rendered facade can look perfect at handover and still fail later if the system beneath it wasn’t applied correctly.',
              'Preparation, reinforcement, thickness, curing and compatibility between products all contribute to long-term performance.',
              'That’s why we treat the complete system as the job, not just the visible finish.'], [], []),
        ],
    },
    'solid-plastering': {
        'h1': 'Solid Plastering', 'title': 'Traditional trade. Commercial delivery.',
        'intro': ['Solid plastering remains one of the most effective ways to create durable, straight and consistent masonry surfaces.',
                  'Coastside delivers solid plaster systems across architectural residential, multi-residential and commercial projects, with the preparation and application controlled from substrate through to final finish.'],
        'cta': 'Send us your plans',
        'blocks': [
            ('Applications', 'Solid plastering can be used across:', [],
             ['Masonry walls', 'Concrete substrates', 'Internal wall systems', 'External wall systems', 'Architectural detailing',
              'Renovation and restoration work', 'Commercial and multi-residential construction'],
             ['Each project is assessed against the substrate, specified finish and intended use before the system is confirmed.']),
        ],
    },
    'architectural-coatings': {
        'h1': 'Architectural Coatings', 'title': 'When the finish is part of the architecture.',
        'intro': ['Some surfaces aren’t designed to disappear.',
                  'Texture, movement, depth and colour can become part of the architectural language of a building.',
                  'Coastside applies specified architectural coating systems across facades, feature walls and design-led projects where the quality and consistency of the final surface matter.'],
        'cta': 'Discuss your specification',
        'blocks': [
            ('Specification-led', 'From the documented finish to the completed surface.',
             ['We work from the nominated finish and manufacturer system rather than attempting to reproduce a look with an unsuitable product.',
              'That means understanding the substrate, preparation requirements, application method and environmental conditions before work begins.',
              'For architects and builders, it provides a clearer path from the documented finish to the completed surface.'], [], []),
        ],
    },
    'venetian-plaster': {
        'h1': 'Venetian Plaster', 'title': 'A finish built by hand.',
        'intro': ['Venetian plaster is applied in multiple fine layers, creating natural variation, depth and movement across the finished surface.',
                  'The result isn’t intended to look perfectly uniform.', 'That’s the point.',
                  'Each wall responds differently to the hand application, light and surrounding architecture, creating a finish that can’t be replicated with standard paint.'],
        'cta': 'Discuss a finish',
        'blocks': [
            ('Where we use it', 'Venetian plaster works particularly well across:', [],
             ['Feature walls', 'Entry spaces', 'Hospitality interiors', 'Retail environments', 'High-end residential interiors',
              'Fireplace surrounds', 'Architectural features', 'Selected commercial spaces'],
             ['Samples can be prepared to establish colour, movement and finish before the main application begins.']),
        ],
    },
}


def install(g):
    for k, v in g.items():
        globals().setdefault(k, v)
    g.update(home=home, services_hub=services_hub, service_page=service_page, about=about, builder_pack=builder_pack,
             areas_hub=areas_hub, projects_hub=projects_hub, project_page=project_page, quote=quote, contact=contact, cta=cta)
    g['FOOTER_V7'] = footer
    # V7 only: new project photography (Sep 2026). None of the original images are used in V7.
    # Everything is overridden here so v3-v6 builds are untouched.
    for sv in g['SERVICES']:
        if sv['slug'] in V7_SERVICE_IMG:
            sv['img'] = V7_SERVICE_IMG[sv['slug']]
    for lo in g['LOCATIONS']:
        if lo['slug'] in V7_LOCATION_IMG:
            lo['img'] = V7_LOCATION_IMG[lo['slug']]
    keep = []
    for pr in g['PROJECTS']:
        if pr['slug'] in V7_PROJECTS:
            pr.update(V7_PROJECTS[pr['slug']])
            keep.append(pr)
    for slug, d in V7_NEW_PROJECTS.items():
        pr = dict(d, slug=slug, builder=g['tbc']('builder'), year=g['tbc']('year'), systems=g['tbc']('system'), suburb=g['tbc']('suburb'))
        keep.append(pr)
    g['PROJECTS'][:] = keep
    g['PRJ'].clear()
    g['PRJ'].update({pr['slug']: pr for pr in keep})
    # default share image and organisation schema image
    _page = g['page']
    og_map = {'hero': 'street-front', 'services': 'site-overhead', 'project-4': 'apartments-skyline',
              'steve': 'entry-stone', 'contact': 'drone-front'}
    def page_v7(*a, **k):
        a = list(a)
        if len(a) >= 8:
            a[7] = og_map.get(a[7], a[7])
        elif 'og' in k:
            k['og'] = og_map.get(k['og'], k['og'])
        else:
            k['og'] = 'street-front'
        return _page(*a, **k).replace('img/hero.jpg', 'img/street-front.jpg')
    g['page'] = page_v7
    globals()['page'] = page_v7


V7_SERVICE_IMG = {
    'external-rendering': 'rear-pool',
    'commercial-rendering': 'scaffold-canal',
    'solid-plastering': 'side-elevation',
    'architectural-coatings': 'curved-front',
    'venetian-plaster': 'entry-stone',
    'render-repairs': 'pool-overhead',
}
V7_LOCATION_IMG = {'gold-coast': 'apartments-skyline', 'northern-rivers': 'pool-overhead'}
# Projects kept in V7, with their new photography. Projects not listed here have no new images and are hidden in V7.
V7_PROJECTS = {
    'brakes-crescent-miami': {'img': 'curved-front', 'gallery': ['curved-front', 'side-elevation'], 'featured': True,
                              'alt': 'Curved rendered upper level with timber battens and a glass balcony, Brakes Crescent, Miami'},
    'coastal-residence': {'img': 'street-front', 'gallery': ['street-front', 'entry-stone'], 'featured': False},
    'multi-storey-residential': {'img': 'apartments-skyline', 'gallery': ['apartments-skyline', 'site-overhead'], 'featured': True,
                                 'summary': 'Multi-storey apartment buildings in construction, with the Gold Coast skyline behind.',
                                 'alt': 'Multi-storey apartment building under scaffold with the Gold Coast skyline behind'},
    # Edited photography, 25 Sep 2026
    'commercial-entry': {'img': 'commercial-entry', 'gallery': [], 'featured': True,
                         'summary': 'Curved rendered entry arches, a textured feature wall and a rendered bench at a Gold Coast multi-storey building.',
                         'alt': 'Curved rendered entry arches, textured feature wall and lit rendered bench at a Gold Coast multi-storey building'},
}
V7_NEW_PROJECTS = {
    'curved-balcony-residential': {'title': 'Curved-balcony residential', 'location': 'gold-coast',
                                   'services': ['external-rendering', 'architectural-coatings'],
                                   'sector': 'multi', 'build': 'new', 'featured': False,
                                   'img': 'curved-balconies', 'gallery': [],
                                   'summary': 'Three-storey residential building with curved rendered balcony bands, vertical battens and a stone-clad corner.',
                                   'alt': 'Three-storey residential building with curved rendered balcony bands and a stone-clad corner'},
    'contemporary-residence': {'title': 'Contemporary residence', 'location': 'gold-coast', 'services': ['external-rendering'],
                               'sector': 'luxury', 'build': 'new', 'featured': False,
                               'img': 'drone-front', 'gallery': ['drone-front', 'rear-pool', 'pool-overhead'],
                               'summary': 'Rendered two-storey home with a framed upper level, glass balcony and timber battens.',
                               'alt': 'Aerial view of a rendered two-storey home with a framed upper level and glass balcony'},
}
WORK_BAND = ('site-overhead', 'Overhead view of a multi-storey construction site under way')
WORK = [
    ('crew-spraying', 'Two Coastside plasterers spraying render onto a block wall from scaffold'),
    ('commercial-entry', 'Curved rendered entry arches and a lit rendered bench at a Gold Coast multi-storey building'),
    ('scaffold-canal', 'Coastside crew rendering a canal-front building from scaffold, seen from the air'),
    ('curved-balconies', 'Three-storey building with curved rendered balcony bands and a stone-clad corner'),
    ('apartments-skyline', 'Multi-storey apartment building under scaffold with the Gold Coast skyline behind'),
    ('curved-front', 'Curved rendered upper level with timber battens and a glass balcony'),
]


def work_band(c):
    return f'<figure class="band v7-band">{pic(c, WORK_BAND[0], WORK_BAND[1])}</figure>'


def work_grid(c):
    L = c.L
    figs = ''.join(f'<figure>{pic(c, n, a, "(max-width:700px) 50vw, (max-width:1400px) 33vw, 460px")}</figure>' for n, a in WORK)
    return f'''<section class="sec v7-work-sec"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow">Recent work</span><h2>On site and finished.</h2></div><a class="text-link" href="{L('projects/')}">View projects{ARROW}</a></div>
  <div class="v7-work">{figs}</div>
</div></section>'''


# Instagram band (home). Six saved posts from @coast_side_plastering, same as the old one-page site. Static tiles until the Behold feed is connected.
IG_POSTS = [
    ('reel/DYB-mexTDvU', 'ig-1', 'Coastal home at Brakes Crescent, Miami, Gold Coast, rendered by Coastside', True),
    ('reel/DbHRJIUTJUs', 'ig-2', 'Waterfront luxury home on the Gold Coast', True),
    ('p/DYB5wBUk21X', 'ig-3', 'Finished rendered coastal home, Gold Coast', False),
    ('p/DaeHVZozc-N', 'ig-4', 'Coastside crew walking a finished rendered corridor', False),
    ('p/DaShOf0zg-y', 'ig-5', 'Coastside crew rendering on a Gold Coast construction site', False),
    ('p/DZ3-sHqk29D', 'ig-6', 'Coastside crew rendering from scaffolding', False),
]


def instagram_band(c):
    base = SITE['instagram']
    handle = '@' + base.rstrip('/').rsplit('/', 1)[-1]
    tiles = ''.join(
        f'<li><a class="v7-ig-tile" href="{base}{path}/" target="_blank" rel="noopener" data-track="instagram_post" aria-label="{"Watch the reel" if reel else "View the post"} on Instagram: {E(alt)}">'
        f'{pic(c, name, alt, "(max-width:700px) 33vw, (max-width:1400px) 17vw, 230px")}{"<span class=" + chr(34) + "v7-ig-reel" + chr(34) + " aria-hidden=" + chr(34) + "true" + chr(34) + "></span>" if reel else ""}</a></li>'
        for path, name, alt, reel in IG_POSTS)
    return f'''<section class="sec cream v7-ig-sec" aria-labelledby="ig"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow">On Instagram</span><h2 id="ig">Follow the work.</h2></div><a class="text-link" href="{base}" target="_blank" rel="noopener" data-track="instagram_profile">{handle}{ARROW}</a></div>
  <ul class="v7-ig">{tiles}</ul>
</div></section>'''


# ------------------------------------------------------------------ pieces
BRAND_LOGOS = [('Dulux AcraTex', 'dulux-acratex.png', 268, 160), ('Rockcote', 'rockcote.svg', 398, 60),
               ('Unitex', 'unitex.svg', 420, 117), ('Resene', 'resene.png', 412, 160), ('Boral', 'boral.png', 175, 160)]


def brand_logos(c):
    # Manufacturer logos shown to identify the systems applied, not as endorsement. Names stay in the alt text.
    items = ''.join(f'<li class="b-{f.split(".")[0]}"><img src="{c.L("img/brands/" + f)}" alt="{n}" width="{w}" height="{h}" loading="lazy" decoding="async"></li>'
                    for n, f, w, h in BRAND_LOGOS)
    return f'<ul class="v7-brands" aria-label="Systems we apply">{items}</ul><p class="v7-brands-note">Logos are trademarks of their owners and are shown to identify the systems we apply.</p>'


def ps(paras, cls=''):
    return ''.join(f'<p{" class=" + chr(34) + cls + chr(34) if cls else ""}>{p}</p>' for p in paras)


def cta(c, title='Commercial rendering.<br>Properly resourced.', text='From the first take-off to the final elevation, Coastside brings the crew, systems and trade experience required to deliver substantial rendering and plastering packages.', q=''):
    L = c.L
    return f'''<section class="cta v7-final"><div class="wrap">
  <div><span class="eyebrow">Get started</span><h2>{title}</h2><p>{text}</p></div>
  <div class="btns"><a class="btn btn-primary" href="{L('quote/')}{q}" data-track="cta_send_plans">Send us your project{ARROW}</a><a class="btn btn-ghost" href="{L('builder-pack/coastside-capability-statement.pdf')}" download>Download capability statement{ARROW}</a></div>
</div></section>'''


def split(eyebrow, h, body, cls='sec', hid=''):
    return f'''<section class="{cls}"><div class="wrap v7-split">
  <div><span class="eyebrow">{eyebrow}</span><h2{' id=' + chr(34) + hid + chr(34) if hid else ''}>{h}</h2></div>
  <div class="v7-copy">{body}</div>
</div></section>'''


def tiles(items, dark=True):
    return '<div class="v7-tiles' + (' on-dark' if dark else '') + '">' + ''.join(
        f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'


def process_ol():
    return '<ol class="v7-steps">' + ''.join(
        f'<li><span class="n">{i:02d}</span><h3>{t}</h3>{ps(p)}</li>' for i, (t, p) in enumerate(PROCESS, 1)) + '</ol>'


def page_hero(c, items, eyebrow, h1, lead_paras=(), btn=None):
    L = c.L
    b = f'<div class="btns"><a class="btn btn-primary" href="{btn[1]}">{btn[0]}{ARROW}</a></div>' if btn else ''
    return f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1>
  <div class="hero-row"><div class="lead v7-lead">{ps(lead_paras)}</div>{b}</div></div></section>'''


# ------------------------------------------------------------------ home
def home():
    c = Ctx('')
    L = c.L
    featured = [p for p in PROJECTS if p['featured']][:3]
    hero = f'''<section class="v7h" aria-labelledby="h1">
  <div class="v7h-bg"><video class="v7h-video" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover" autoplay muted loop playsinline preload="metadata" poster="{L('img/v7-hero-poster.jpg')}" data-desktop="{L('img/v7-hero-desktop.mp4')}" data-desktop-poster="{L('img/v7-hero-desktop-poster.jpg')}" aria-hidden="true"><source src="{L('img/v7-hero.mp4')}" type="video/mp4"></video></div>
  <script>(function(){{var v=document.querySelector('.v7h-video');if(!v)return;var mm=window.matchMedia||function(){{return{{matches:false}}}};if(mm('(min-width: 900px)').matches){{v.poster=v.dataset.desktopPoster;v.querySelector('source').src=v.dataset.desktop;v.load();}}if(mm('(prefers-reduced-motion: reduce)').matches){{v.removeAttribute('autoplay');v.pause();}}else{{var p=v.play();if(p&&p.catch)p.catch(function(){{}});}}}})();</script>
  <div class="v7h-shade" aria-hidden="true"></div>
  <div class="v7h-stack">
    <p class="v7h-kicker">Commercial rendering &middot; Solid plastering &middot; Architectural finishes</p>
    <h1 id="h1"><span class="v7h-wm">coastside</span><span class="v7h-serif"><small>Built for the finish.</small>Structured for the job.</span></h1>
  </div>
  <div class="v7h-foot">
    <a href="{L('quote/')}" data-track="hero_send_plans">Send us your project</a>
    <span>Gold Coast &middot; South East Queensland &middot; Northern New South Wales</span>
    <a href="{L('builder-pack/coastside-capability-statement.pdf')}" download>Capability statement</a>
  </div>
  <a class="v7h-scroll" href="#intro" aria-label="Scroll to content"><span></span></a>
</section>'''
    bigger = split('Built for bigger jobs', 'The finish is only part of the job.',
                   ps(['On a commercial project, good plastering is expected.',
                       'What matters just as much is having the labour to meet program, understanding the specification, coordinating with other trades, maintaining communication and having the documentation sorted before the crew arrives.'])
                   + '<p class="v7-pull">That’s the operation we’ve built.</p>'
                   + ps(['Coastside combines more than 25 years of trade experience with the crew capacity, equipment and systems required to deliver high-end residential, multi-residential and commercial packages across Queensland and Northern New South Wales.'])
                   + f'<a class="text-link" href="{L("about/")}">About Coastside{ARROW}</a>', 'sec v7-intro-sec', 'intro')
    capability = f'''<section class="sec dark" aria-labelledby="cap"><div class="wrap">
  <div class="head"><span class="eyebrow">Capability</span><h2 id="cap">The capability behind the finish.</h2></div>
  {tiles(CAPABILITY)}
</div></section>'''
    svc = ''.join(f'''<a class="v7-svc" href="{L('services/' + slug + '/')}"><span class="n">{i:02d}</span><h3>{name}</h3><div>{ps(d)}</div><span class="go">{name}{ARROW}</span></a>'''
                  for i, (slug, name, d) in enumerate(HOME_SERVICES, 1))
    services = f'''<section class="sec cream"><div class="wrap">
  <div class="v7-split"><div><span class="eyebrow">Services</span><h2>Rendering and plastering at commercial scale.</h2></div>
  <div class="v7-copy"><p>From architectural residences through to multi-residential developments and large commercial facades, our work is built around the same principle:</p><p class="v7-pull">Understand the specification. Resource the job properly. Deliver the finish.</p></div></div>
  <div class="v7-svcs">{svc}</div>
</div></section>'''
    systems = split('Systems', 'The specification comes first.',
                    ps(['The performance of a render or coating system depends on more than what you see when the scaffold comes down.',
                        'Substrate preparation, compatibility, application thickness, curing conditions and finishing methodology all affect the result.',
                        'We work with specified systems from established manufacturers and follow the requirements of the nominated system from preparation through to completion.'])
                    + brand_logos(c)
                    + f'<a class="text-link" href="{L("quote/")}">Discuss your specification{ARROW}</a>', 'sec stone')
    projects = f'''<section class="sec"><div class="wrap">
  <div class="head-row"><div><span class="eyebrow">Selected projects</span><h2>The work is the proof.</h2></div><a class="text-link" href="{L('projects/')}">View projects{ARROW}</a></div>
  <div class="cards">{''.join(project_card(c, p) for p in featured)}</div>
</div></section>'''
    process = f'''<section class="sec stone"><div class="wrap">
  <div class="v7-split"><div><span class="eyebrow">Our process</span><h2>From tender to handover.</h2></div>
  <div class="v7-copy"><p class="v7-pull">Clear scope before anyone starts.</p><p>The easiest problems to solve on a construction project are the ones identified before work begins. Our process is designed to establish scope, specification, access, sequencing and program requirements before mobilisation.</p></div></div>
  {process_ol()}
</div></section>'''
    body = hero + bigger + work_band(c) + capability + services + work_grid(c) + systems + projects + instagram_band(c) + process + cta(c)
    write('', page(c, 'Coastside Solid Plastering | Commercial rendering and solid plastering, Gold Coast',
                   'Commercial rendering, external rendering, solid plastering and architectural finishes across South East Queensland and Northern NSW. 15+ crew, pumped render, specified systems.',
                   body, 'home'))


# ------------------------------------------------------------------ services
def services_hub():
    c = Ctx('services/')
    L = c.L
    items = [('', 'Home'), (None, 'Services')]
    svc = ''.join(f'''<a class="v7-svc" href="{L('services/' + slug + '/')}"><span class="n">{i:02d}</span><h3>{name}</h3><div>{ps(d)}</div><span class="go">{name}{ARROW}</span></a>'''
                  for i, (slug, name, d) in enumerate(HOME_SERVICES, 1))
    body = page_hero(c, items, 'Services', 'Rendering and plastering at commercial scale.',
                     ['From architectural residences through to multi-residential developments and large commercial facades, our work is built around the same principle: understand the specification, resource the job properly, deliver the finish.'])
    body += f'<section class="sec"><div class="wrap"><div class="v7-svcs">{svc}</div></div></section>'
    body += split('Systems', 'The specification comes first.',
                  ps(['The performance of a render or coating system depends on more than what you see when the scaffold comes down.',
                      'We work with specified systems from established manufacturers and follow the requirements of the nominated system from preparation through to completion.'])
                  + brand_logos(c), 'sec stone')
    body += cta(c)
    write('services/', page(c, 'Rendering and plastering services | Coastside', 'External rendering, commercial rendering, solid plastering, architectural coatings and Venetian plaster for commercial, multi-residential and architectural projects.', body, 'services', 'services/', [crumb_schema(items)], 'services'))


def service_page(s):
    c = Ctx(f"services/{s['slug']}/")
    L = c.L
    v = SERVICE_COPY[s['slug']]
    items = [('', 'Home'), ('services/', 'Services'), (None, v['h1'])]
    q = f"{L('quote/')}?services={s['slug']}"
    body = page_hero(c, items, 'Services', v['h1'], [], (v['cta'], q))
    body += f'<figure class="band">{pic(c, s["img"], "", eager=True)}</figure>'
    body += f'<section class="sec"><div class="wrap v7-split"><div><span class="eyebrow">{v["h1"]}</span><h2>{v["title"]}</h2></div><div class="v7-copy">{ps(v["intro"])}</div></div></section>'
    for i, (eb, h, paras, bullets, after) in enumerate(v['blocks']):
        cls = 'sec cream' if i % 2 == 0 else 'sec'
        inner = ps(paras) + (('<ul class="v7-list">' + ''.join(f'<li>{b}</li>' for b in bullets) + '</ul>') if bullets else '') + ps(after)
        body += split(eb, h, inner, cls)
    if v.get('grid'):
        body += f'<section class="sec dark"><div class="wrap"><div class="head"><span class="eyebrow">{v["grid"][0]}</span><h2>Where the capacity counts.</h2></div>{tiles(v["grid"][1])}</div></section>'
    projs = projects_for(s['slug'])
    if projs:
        body += f'<section class="sec"><div class="wrap"><div class="head-row"><div><span class="eyebrow">Selected projects</span><h2>{v["h1"]} projects</h2></div><a class="text-link" href="{L("projects/")}?service={s["slug"]}">View projects{ARROW}</a></div><div class="cards">{"".join(project_card(c, p) for p in projs[:3])}</div></div></section>'
    body += cta(c, q='?services=' + s['slug'])
    schema = [crumb_schema(items), {"@context": "https://schema.org", "@type": "Service", "name": v['h1'], "serviceType": v['h1'],
                                    "description": ' '.join(v['intro'])[:300], "provider": {"@id": SITE_URL + "#business"}}]
    write(c.path, page(c, f"{v['h1']} | Coastside Solid Plastering", ' '.join(v['intro'])[:158].rsplit(' ', 1)[0] + '.', body, 'service', 'services/', schema, s['img'], s['slug']))


# ------------------------------------------------------------------ projects
def projects_hub():
    c = Ctx('projects/')
    L = c.L
    items = [('', 'Home'), (None, 'Projects')]
    def opts(d):
        return ''.join(f'<option value="{k}">{v}</option>' for k, v in d.items())
    used_svc = {x: SVC[x]['name'] for x in dict.fromkeys(y for p in PROJECTS for y in p['services'])}
    body = page_hero(c, items, 'Selected projects', 'The work is the proof.',
                     ['Commercial. Multi-residential. Architectural residential.',
                      'A selection of rendering, solid plastering and specialist finish projects delivered by Coastside across Queensland and Northern New South Wales.'])
    body += f'''<section class="sec"><div class="wrap">
  <form class="filterbar" action="" method="get" aria-label="Filter projects" role="search">
    <label>Sector<select name="sector"><option value="">All sectors</option>{opts(SECTORS)}</select></label>
    <label>Service<select name="service"><option value="">All services</option>{opts(used_svc)}</select></label>
    <label>Type<select name="build"><option value="">New build or renovation</option>{opts(BUILD_TYPES)}</select></label>
    <button class="filter-reset" type="button">Reset</button>
    <span class="filter-count" aria-live="polite"></span>
  </form>
  <div class="cards proj-grid">{''.join(project_card(c, p, 'h2').replace('View case study', 'View project') for p in PROJECTS)}</div>
  <p class="empty">No projects match those filters yet. <button class="filter-reset" type="button" onclick="document.querySelector('.filterbar .filter-reset').click()">Show all</button></p>
</div></section>''' + cta(c)
    write(c.path, page(c, 'Selected projects | Coastside Solid Plastering', 'Commercial, multi-residential and architectural residential rendering, solid plastering and specialist finish projects by Coastside.', body, 'projects', 'projects/', [crumb_schema(items)], 'project-4'))


def project_page(p):
    c = Ctx(f"projects/{p['slug']}/")
    L = c.L
    loc = LOC[p['location']]
    items = [('', 'Home'), ('projects/', 'Projects'), (None, p['title'])]
    svcs = ', '.join(f'<a href="{L("services/" + s + "/")}">{SVC[s]["name"]}</a>' for s in p['services'])
    gal = ''.join(f'<figure>{pic(c, g, p["alt"] if i == 0 else p["title"] + " detail", "(max-width:640px) 100vw, 900px")}</figure>' for i, g in enumerate(p['gallery']))
    body = f'''<section class="hero dark"><div class="wrap">{crumbs(c, items)}<span class="eyebrow">{SECTORS[p['sector']]}</span><h1>{p['title']}</h1><p class="lead">{p['summary']}</p></div></section>
<figure class="band tall">{pic(c, p['img'], p['alt'], eager=True)}</figure>
<section class="sec-tight"><div class="wrap"><dl class="spec">
  <div><dt>Location</dt><dd>{p['suburb']}, {loc['name']}</dd></div>
  <div><dt>Project type</dt><dd>{SECTORS[p['sector']]} / {BUILD_TYPES[p['build']]}</dd></div>
  <div><dt>Builder / client</dt><dd>{p['builder']}</dd></div>
  <div><dt>Scope</dt><dd>{svcs}</dd></div>
</dl></div></section>
<section class="sec" style="padding-top:24px"><div class="wrap grid-main"><div class="prose">
  <h2>The project</h2><p>{p['summary']} {tbc('The development, architectural intent and Coastside’s involvement.')}</p>
  <h2>Our scope</h2><p>Coastside was engaged to deliver {tbc('specific scope')}, including {tbc('systems / elevations / specialist elements')}.</p>
  <h2>Delivery</h2><p>{tbc('Scale of the package, crew requirements, access constraints, sequencing, program or technical challenges.')}</p>
  <h2>The finish</h2><p>{p['systems']} {tbc('What was required to achieve the completed result.')}</p>
</div><aside class="panel sticky"><h2>Have a similar project?</h2><p>Send through the available documentation and we’ll take a look.</p><a class="btn btn-primary" href="{L('quote/')}" data-track="project_send_plans" data-label="{p['slug']}">Send us the package{ARROW}</a></aside></div></section>
{('<section class="sec-tight"><div class="wrap"><div class="gallery">' + gal + '</div></div></section>') if gal else ''}
{cta(c)}'''
    schema = [crumb_schema(items)]
    write(c.path, page(c, f"{p['title']} | Coastside project", f"{p['summary']} Delivered by Coastside Solid Plastering.", body, 'project', 'projects/', schema, p['img'], p['slug']))


# ------------------------------------------------------------------ about
def about():
    c = Ctx('about/')
    L = c.L
    items = [('', 'Home'), (None, 'About')]
    body = page_hero(c, items, 'Coastside Solid Plastering', 'Built on the trade.<br>Built for bigger projects.',
                     ['Coastside is a second-generation plastering contractor delivering rendering, solid plastering and architectural finishes across Queensland and Northern New South Wales.'])
    body += f'<figure class="band">{pic(c, "rear-pool", "Rendered two-storey home with a pool, seen from the air", eager=True)}</figure>'
    body += split('About', 'Know the system. Know the specification.',
                  ps(['The business has grown from decades on the tools into a crew of 15+ tradespeople capable of delivering substantial residential, multi-residential and commercial packages.',
                      'But growth hasn’t changed what the business is built around.'])
                  + '<p class="v7-pull">Know the system.<br>Know the specification.<br>Put the right people on the job.<br>And deliver what you said you would.</p>')
    body += split('Experience', '25+ years doesn’t replace the specification.<br>It helps you understand it.',
                  ps(['Experience matters most when something isn’t straightforward.',
                      'An unusual substrate. A difficult junction. A tight construction sequence. A large elevation. A specified finish that needs to remain consistent across hundreds of square metres.',
                      'That’s where years on the tools become useful.',
                      'Not as a number on a website, but in the decisions made before and during the work.']), 'sec cream')
    body += f'''<section class="sec"><div class="wrap grid-2"><div>{pic(c, 'crew-spraying', 'Two Coastside plasterers spraying render onto a block wall from scaffold', '(max-width:1100px) 100vw, 560px')}</div>
<div class="v7-copy"><span class="eyebrow">The crew</span><h2>Enough capacity to make a difference.</h2>{ps(['Coastside operates with a crew of 15+ across rendering, plastering and specialist finish work.', 'That capacity allows us to allocate labour according to project requirements rather than trying to make every job fit the same crew.', 'For larger projects, it means we can build a team around the package, stage works across elevations and maintain production as the project progresses.'])}</div></div></section>'''
    body += f'''<section class="sec dark"><div class="wrap"><div class="v7-split"><div><span class="eyebrow">Our process</span><h2>From tender to handover.</h2></div><div class="v7-copy"><p class="v7-pull">Clear scope before anyone starts.</p></div></div>{process_ol()}</div></section>'''
    body += cta(c)
    write(c.path, page(c, 'About Coastside Solid Plastering', 'A second-generation plastering contractor with a 15+ crew delivering rendering, solid plastering and architectural finishes across Queensland and Northern NSW.', body, 'about', None, [crumb_schema(items)], 'steve'))


# ------------------------------------------------------------------ builders / procurement
def builder_pack():
    c = Ctx('builder-pack/')
    L = c.L
    items = [('', 'Home'), (None, 'Working with Coastside')]
    rows = ''.join(f'''<tr><td class="doc-title">{d['title']}</td><td data-l="Type">{d['type']}</td><td data-l="Access"><span class="pill{' pub' if d['access'] == 'public' else ''}">{'Download' if d['access'] == 'public' else 'On request'}</span></td><td data-l="Issued">{d['issued']}</td><td data-l="Expires">{d['expires']}</td><td class="doc-actions">{f'<a href="{L(d["file"])}" download>Download PDF</a>' if d['file'] else '<a href="#request">Request</a>'}</td></tr>''' for d in DOCUMENTS)
    docs_opts = ''.join(f'<label><input type="checkbox" name="documents" value="{E(d["title"])}"{" checked" if d["type"] == "Insurance" else ""}> {d["title"]}</label>' for d in DOCUMENTS if d['access'] == 'request')
    docs = [
        ('QBCC licence', f'Current licence details available for verification. {tbc("licence number and class")}', ('View licence', 'https://www.qbcc.qld.gov.au/')),
        ('Insurance', 'Current certificates of currency available on request.', ('Request certificates', '#request')),
        ('SWMS', 'Project-specific Safe Work Method Statements prepared where required.', None),
        ('Capability statement', 'Company profile, services, capability, regions and supporting information for estimating and procurement teams.', ('Download capability statement', 'coastside-capability-statement.pdf')),
        ('Product systems', 'Experience across specified systems from leading render and coating manufacturers.', None),
        ('Project documentation', 'Additional compliance and pre-start documentation supplied according to project requirements.', None),
    ]
    def link(a):
        if not a:
            return ''
        label, href = a
        extra = ' download' if href.endswith('.pdf') else (' rel="noopener" target="_blank"' if href.startswith('http') else '')
        return f'<a class="text-link" href="{href}"{extra}>{label}{ARROW}</a>'
    tiles_html = '<div class="v7-tiles">' + ''.join(f'<div><h3>{t}</h3><p>{d}</p>{link(a)}</div>' for t, d, a in docs) + '</div>'
    body = page_hero(c, items, 'Builders / procurement', 'Everything you need before we arrive on site.',
                     ['Commercial procurement shouldn’t involve chasing a subcontractor for basic documentation.',
                      'We maintain the licensing, insurance and project documentation required to work across commercial and multi-residential construction.'],
                     ('Download capability statement', 'coastside-capability-statement.pdf'))
    body += f'<section class="sec"><div class="wrap">{tiles_html}</div></section>'
    body += f'''<section class="sec cream" id="documents"><div class="wrap"><div class="head"><span class="eyebrow">Document register</span><h2>Documents</h2></div>
  <table class="table register"><thead><tr><th>Document</th><th>Type</th><th>Access</th><th>Issued</th><th>Expires</th><th><span class="sr">Action</span></th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section class="sec stone" id="request"><div class="wrap grid-2">
  <div><span class="eyebrow">Request documents</span><h2>Tell us what you need.</h2><p class="lead">Pick the documents and the project. We email them to you.</p></div>
  <div>{form_head('Document request - Coastside website', 'document_request', 'Thanks. The documents will be emailed to you.', event='document_requested')}
    <div class="row2">{fld('dr-name', 'Name', '<input id="dr-name" name="name" autocomplete="name" required>')}{fld('dr-co', 'Company', '<input id="dr-co" name="company" autocomplete="organization" required>')}</div>
    <div class="row2">{fld('dr-email', 'Email', '<input id="dr-email" type="email" name="email" autocomplete="email" required>', err='Enter a valid email.')}{fld('dr-proj', 'Project', '<input id="dr-proj" name="project_name">', opt=True)}</div>
    <fieldset class="field"><legend>Documents</legend><div class="checks">{docs_opts}</div></fieldset>
    <div class="status" role="status" aria-live="polite"></div>
    <div class="btns"><button class="btn btn-primary" type="submit">Request documents</button></div>
  </form></div>
</div></section>
<section class="sec-tight"><div class="wrap head-row" style="margin:0"><div><span class="eyebrow">Tendering</span><h2 style="margin:0">Add Coastside to your tender list.</h2></div><a class="btn btn-primary" href="{L('builder-pack/tender-list/')}">Tender list{ARROW}</a></div></section>
{cta(c)}'''
    write(c.path, page(c, 'Working with Coastside | Licence, insurance, SWMS and capability', 'QBCC licence, insurance, SWMS, capability statement and project documentation for builders and procurement teams.', body, 'builder-pack', 'builder-pack/', [crumb_schema(items)], 'project-4'))


# ------------------------------------------------------------------ service area
def areas_hub():
    c = Ctx('service-areas/')
    L = c.L
    items = [('', 'Home'), (None, 'Service area')]
    area_li = ''.join(f'<li>{"<a href=" + chr(34) + L("gold-coast/") + chr(34) + ">Gold Coast</a>" if a == "Gold Coast" else a}</li>' for a in AREAS)
    body = page_hero(c, items, 'Service area', 'Gold Coast based.<br>Built to travel.',
                     ['Coastside is based on the Gold Coast and regularly services projects throughout South East Queensland and Northern New South Wales.'])
    body += f'''<section class="sec"><div class="wrap v7-split"><div><span class="eyebrow">Primary service areas</span><h2>Where we work.</h2></div>
<div class="v7-copy"><ul class="v7-areas">{area_li}</ul><p>For substantial commercial and multi-residential packages outside these areas, talk to us about the project.</p><a class="text-link" href="{L('quote/')}">Discuss a project{ARROW}</a></div></div></section>''' + cta(c)
    write(c.path, page(c, 'Service area | Coastside Solid Plastering', 'Gold Coast based, servicing South East Queensland and Northern New South Wales: Gold Coast, Brisbane, Logan, Redlands, Tweed Coast, Kingscliff, Casuarina, Byron Bay and the Northern Rivers.', body, 'areas', 'service-areas/', [crumb_schema(items)]))


# ------------------------------------------------------------------ contact / tender
def quote():
    c = Ctx('quote/')
    L = c.L
    items = [('', 'Home'), (None, 'Project enquiries')]
    roles = ['Builder', 'Developer', 'Architect / designer', 'Project manager', 'Homeowner', 'Other']
    trade = 'Builder|Developer|Architect / designer|Project manager|Other'
    role_ch = ''.join(f'<label class="choice"><input type="radio" name="role" value="{r}" required><span>{r}</span></label>' for r in roles)
    svc_ch = ''.join(f'<label><input type="checkbox" name="services" value="{s["slug"]}"> {s["name"]}</label>' for s in PUB_SERVICES)
    sect = ''.join(f'<option value="{k}">{v}</option>' for k, v in SECTORS.items())
    build = ''.join(f'<option value="{k}">{v}</option>' for k, v in BUILD_TYPES.items())
    include = ['Drawings and elevations', 'Render / finish specification', 'Finish schedule', 'Approximate quantities, if available', 'Construction program', 'Site location', 'Tender closing date']
    body = page_hero(c, items, 'Contact / tender', 'Have a project coming up?<br>Send us the package.',
                     ['If you’re pricing a commercial, multi-residential or architectural project, send through the available documentation and we’ll take a look.',
                      'The more information we have upfront, the more accurately we can assess the scope.'])
    body += f'''<section class="sec"><div class="wrap grid-main">
<div>
<ol class="stepper" aria-label="Progress"><li class="on">Step 1<b>About you</b></li><li>Step 2<b>The project</b></li><li>Step 3<b>Documents</b></li></ol>
{form_head('Project enquiry - Coastside website', 'quote', '', L('quote/received/'), 'quote_submitted')}
  <fieldset class="step on" data-step="1"><h2>About you</h2>
    <fieldset class="field"><legend>You are</legend><div class="choices">{role_ch}</div><span class="err">Choose one.</span></fieldset>
    <div class="row2">{fld('q-name', 'Name', '<input id="q-name" name="name" autocomplete="name" required>')}<div class="field" data-show-if="role={trade}"><label for="q-co">Company</label><input id="q-co" name="company" autocomplete="organization"><span class="err"></span></div></div>
    <div class="row2">{fld('q-email', 'Email', '<input id="q-email" type="email" name="email" autocomplete="email" required>', err='Enter a valid email.')}{fld('q-phone', 'Phone', '<input id="q-phone" type="tel" name="phone" autocomplete="tel">', opt=True)}</div>
    <div class="step-nav"><span></span><button class="btn btn-primary next" type="button">Next: the project</button></div>
  </fieldset>
  <fieldset class="step" data-step="2"><h2>The project</h2>
    <div class="row2">{fld('q-pname', 'Project name', '<input id="q-pname" name="project_name">', opt=True)}{fld('q-addr', 'Site location', '<input id="q-addr" name="project_address" autocomplete="off" required>')}</div>
    <div class="row2">{fld('q-sector', 'Sector', f'<select id="q-sector" name="sector" required><option value="">Select</option>{sect}</select>')}{fld('q-build', 'New build or renovation', f'<select id="q-build" name="build_type" required><option value="">Select</option>{build}</select>')}</div>
    <fieldset class="field"><legend>Scope</legend><div class="checks">{svc_ch}</div></fieldset>
    <div class="field" data-show-if="role={trade}"><label for="q-tender">Is this a tender?</label><select id="q-tender" name="is_tender"><option value="">Select</option><option>Yes</option><option>No, awarded or negotiated</option></select><span class="err"></span></div>
    <div class="field" data-show-if="is_tender=Yes"><label for="q-close">Tender closing date</label><input id="q-close" type="date" name="tender_close"><span class="err"></span></div>
    <div class="step-nav"><button class="btn btn-line back" type="button">Back</button><button class="btn btn-primary next" type="button">Next: documents</button></div>
  </fieldset>
  <fieldset class="step" data-step="3"><h2>Project documents</h2>
    <div class="field"><span style="font-size:11px;letter-spacing:1.8px;text-transform:uppercase;color:var(--concrete-dk)">Upload project documents <span class="opt">(optional)</span></span>
      <div class="drop" tabindex="0" role="button" aria-label="Upload project documents: choose files or drag them here"><input type="file" name="plans" multiple accept=".pdf,.dwg,.dxf,.jpg,.jpeg,.png,.zip"><strong>Drop documents here or choose files</strong><small>PDF, DWG, images or ZIP {tbc('file storage connects at launch; prototype sends file names only')}</small></div>
      <ul class="files" aria-live="polite"></ul></div>
    {fld('q-link', 'Or a link to your document platform', '<input id="q-link" type="url" name="plans_link" placeholder="EstimateOne, Dropbox, Google Drive">', opt=True, err='Enter a full link starting with https://')}
    {fld('q-msg', 'Notes', '<textarea id="q-msg" name="message" placeholder="Specification, quantities, program, access, anything else."></textarea>', opt=True)}
    <div class="status" role="status" aria-live="polite"></div>
    <div class="step-nav"><button class="btn btn-line back" type="button">Back</button><button class="btn btn-primary" type="submit">Send the package</button></div>
    <p class="hint" style="font-size:13px;color:var(--concrete-dk)">Your details go to Coastside only and are used to reply to this enquiry. <a href="{L('privacy/')}">Privacy</a></p>
  </fieldset>
</form></div>
<aside class="panel sticky"><h2>Ideally include</h2><ul class="v7-list">{''.join(f'<li>{x}</li>' for x in include)}</ul>
<h2 style="margin-top:32px">Prefer to talk first?</h2><p>Call Coastside to discuss the project, scope and timing.</p><a class="text-link" href="tel:{SITE['phone_tel']}">Call Coastside{ARROW}</a></aside>
</div></section>'''
    body += f'<section class="sec dark"><div class="wrap"><div class="v7-split"><div><span class="eyebrow">Our process</span><h2>From tender to handover.</h2></div><div class="v7-copy"><p class="v7-pull">Clear scope before anyone starts.</p></div></div>{process_ol()}</div></section>'
    write(c.path, page(c, 'Project enquiries and tenders | Coastside', 'Send drawings, elevations, specification, program and tender closing date to Coastside for commercial, multi-residential and architectural projects.', body, 'quote', None, [crumb_schema(items)], 'contact'))
    c2 = Ctx('quote/received/')
    body2 = f'''<section class="hero dark"><div class="wrap"><span class="eyebrow">Enquiry received</span><h1>Thanks. We have the package.</h1><p class="lead">We’ll review the scope and come back to you. If anything isn’t clear, we’ll raise it before pricing.</p></div></section>
<section class="sec"><div class="wrap"><h2>What happens next</h2>{process_ol()}</div></section>'''
    write(c2.path, page(c2, 'Enquiry received | Coastside', 'Thanks for your enquiry.', body2, 'quote-received', index=False))


def contact():
    c = Ctx('contact/')
    L = c.L
    items = [('', 'Home'), (None, 'Contact')]
    body = page_hero(c, items, 'Contact', 'Have a project coming up?',
                     ['Send through the available documentation and we’ll take a look.'], ('Send us the package', L('quote/')))
    body += f'''<section class="sec"><div class="wrap grid-main"><table class="table"><tbody>
<tr><th scope="row">Project enquiries</th><td><a href="{L('quote/')}">Send the package</a></td></tr>
<tr><th scope="row">Email</th><td><a href="mailto:{SITE['email']}">{SITE['email']}</a></td></tr>
<tr><th scope="row">Phone</th><td><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></td></tr>
<tr><th scope="row">Instagram</th><td><a href="{SITE['instagram']}" target="_blank" rel="noopener">@coast_side_plastering</a></td></tr>
<tr><th scope="row">Based</th><td>Gold Coast, Queensland</td></tr>
<tr><th scope="row">ABN</th><td>{SITE['abn']}</td></tr></tbody></table>
<aside class="panel"><h2>Procurement?</h2><p>Licence, insurance and capability documents in one place.</p><a class="btn btn-primary" href="{L('builder-pack/')}">Working with Coastside</a></aside></div></section>'''
    write(c.path, page(c, 'Contact | Coastside Solid Plastering', 'Contact Coastside Solid Plastering, Gold Coast.', body, 'contact', None, [crumb_schema(items)]))


# ------------------------------------------------------------------ footer
def footer(L):
    svc = ''.join(f'<li><a href="{L("services/" + s + "/")}">{n}</a></li>' for s, n in
                  [('commercial-rendering', 'Commercial Rendering'), ('external-rendering', 'External Rendering'), ('solid-plastering', 'Solid Plastering'),
                   ('architectural-coatings', 'Architectural Coatings'), ('venetian-plaster', 'Venetian Plaster')])
    return f'''<footer class="footer dark v7-footer">
  <div class="fgrid">
    <div><img src="{L('img/logo.png')}" alt="Coastside Solid Plastering" width="64" height="64" loading="lazy"><p class="v7-sign">Built for the finish.<br>Structured for the job.</p></div>
    <div><h2>Coastside Solid Plastering</h2><ul>{svc}</ul></div>
    <div><h2>Regions</h2><ul><li><a href="{L('gold-coast/')}">Gold Coast</a></li><li><a href="{L('service-areas/')}">South East Queensland</a></li><li><a href="{L('service-areas/')}">Northern New South Wales</a></li></ul></div>
    <div><h2>Compliance</h2><ul><li>QBCC Licensed {tbc('number')}</li><li>Insured</li><li><a href="{L('builder-pack/')}">Working with Coastside</a></li><li><a href="{L('builder-pack/coastside-capability-statement.pdf')}">Capability statement (PDF)</a></li></ul></div>
    <div><h2>Contact</h2><ul><li><a href="{L('quote/')}">Project enquiries{ARROW}</a></li><li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li><li><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></li><li><a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a></li></ul><p style="margin-top:14px">ABN {SITE['abn']}</p></div>
  </div>
  <div class="fbase"><span>&copy; 2026 {SITE['legal']}. <a href="{L('privacy/')}">Privacy</a></span><span>Site by <a href="https://theserviceedit.com" rel="noopener" target="_blank">The Service Edit</a></span></div>
</footer>'''
