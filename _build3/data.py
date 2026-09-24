"""Coastside V3 content collections.

Projects are the hub: each references a location, services, sector and build
type. Service and location pages query projects; nothing is linked by hand.

Rules: Australian English. No em dashes. No invented facts. Anything not
confirmed by Steve goes through tbc() and renders as a dashed chip.
"""
import html


def tbc(text):
    return f'<span class="tbc" title="To confirm with Steve">{html.escape(text)}</span>'


SITE = {
    'name': 'Coastside Solid Plastering',
    'legal': 'Coastside Solid Plastering Pty Ltd',
    'abn': '75 660 293 041',
    'email': 'steven@coastsidesp.com.au',
    'phone': '0438 045 585',
    'phone_tel': '+61438045585',
    'instagram': 'https://www.instagram.com/coast_side_plastering/',
    'area': 'Byron Bay to the Gold Coast to South East Brisbane',
    'systems': ['Dulux AcraTex', 'Rockcote', 'Unitex', 'Resene', 'Boral'],
    'hero_video': None,  # e.g. 'video/hero.mp4' once Steve supplies site footage (Instagram reels, with permission)
    'web3forms_key': '2870139d-38b7-4118-9f7c-9217fd52c463',  # TSE key until the Supabase endpoint is live
}

SECTORS = {
    'luxury': 'Luxury residential',
    'multi': 'Multi-residential',
    'commercial': 'Commercial',
    'hospitality': 'Hospitality',
}
BUILD_TYPES = {'new': 'New build', 'reno': 'Renovation', 'repair': 'Repair and remediation'}

# ------------------------------------------------------------------ SERVICES
SERVICES = [
    {
        'slug': 'external-rendering', 'name': 'External rendering', 'img': 'contact',
        'h1': 'External rendering on the Gold Coast',
        'short': 'Cement and acrylic render systems for facades, elevations and boundary walls.',
        'definition': 'External rendering is the application of a cement or acrylic render system to a building\'s external walls, finished smooth or textured and ready for a coating. Coastside renders new builds, multi-residential facades and commercial elevations from Byron Bay to South East Brisbane.',
        'scope': ['Substrate check and preparation', 'Beads, corners and reveals', 'Base coat and finish coat to the nominated system', 'Control joints set out to the system requirements', 'Handover ready for coating, or complete with coating ' + tbc('confirm coating is in scope')],
        'used': ['Architect-designed and coastal homes', 'Townhouses and apartment facades', 'Retail and commercial elevations', 'Boundary, entry and landscape walls'],
        'considerations': [
            ('Substrate and prep', 'Block, brick and lightweight panel substrates each need a different preparation and a render system rated for them. Tell us the substrate on each elevation.'),
            ('Sequencing', 'Render goes on after windows, flashings and penetrations are in and before final coatings and landscaping. Late penetrations mean patching.'),
            ('Access and scaffold', 'Scaffold height, loading and who supplies it change the price more than most builders expect. Say who is providing it.'),
            ('Curing and weather', 'Render needs protection from direct sun, wind and rain while it cures. Summer storms and heat on the coast need an allowance in the program.'),
            ('Tolerances', 'A smooth finish shows every wave in the wall. Agree the finish and the substrate tolerance before we start, not at handover.'),
            ('Other trades', 'Electricians, plumbers and window installers need to be finished on an elevation before it is rendered.'),
        ],
        'faqs': [
            ('Do you do cement render and acrylic render?', 'Yes. The system follows your specification ' + tbc('confirm both') + '. Our article on acrylic and cement render explains the differences.'),
            ('Do you supply scaffold?', tbc('Steve to confirm scaffold policy')),
            ('How far ahead do you need to be booked?', tbc('typical lead time')),
        ],
        'article': 'what-to-send-for-a-render-quote',
    },
    {
        'slug': 'commercial-rendering', 'name': 'Commercial rendering', 'img': 'services',
        'h1': 'Commercial rendering and render pumping',
        'short': 'Crew numbers, machine-applied render and program control for multi-residential and commercial facades.',
        'definition': 'Commercial rendering covers facade render on multi-residential, retail and commercial buildings, where crew size, staging and program matter as much as the finish. Coastside runs a 15+ crew and machine-applied (pumped) render for large elevations.',
        'scope': ['Machine-applied base coats on large elevations', 'Hand finishing and detailing', 'Staged work to suit the scaffold and the program', 'Multiple elevations or buildings running at once', 'Site-specific SWMS for work at height ' + tbc('confirm')],
        'used': ['Multi-storey residential', 'Townhouse developments', 'Retail and commercial buildings', 'Hospitality fitouts, inside and out'],
        'considerations': [
            ('Program', 'Tell us the scaffold dates for each drop or elevation. We plan crew numbers against them rather than one start date.'),
            ('Staging', 'Large facades are rendered in panels between joints so the finish stays consistent. Stop points need to be agreed with the builder.'),
            ('Access', 'Hoist, loading area and material storage on site affect how fast a pump crew can move.'),
            ('Weather', 'On a commercial program, weather days need to be in the allowance. Render cannot go on in rain or strong wind.'),
            ('Interfaces', 'Balustrades, window frames and cladding junctions are where facades fail. Agree the detail and the sequence early.'),
            ('Paperwork', 'Licence, insurances, SWMS and the capability statement are in the builder pack, ready for your pre-start.'),
        ],
        'faqs': [
            ('How many people can you put on a site?', 'Coastside runs a 15+ crew across residential and commercial work. Numbers on a site depend on the program ' + tbc('confirm typical max per site') + '.'),
            ('Do you pump render?', 'Yes. Machine-applied render is used on large elevations to keep the application even and the program moving.'),
            ('Can you get on our tender list?', 'Yes. Use the tender list form in the builder pack and we will respond to invitations to tender.'),
        ],
        'article': 'what-to-send-for-a-render-quote',
    },
    {
        'slug': 'solid-plastering', 'name': 'Solid plastering', 'img': 'project-3',
        'h1': 'Solid plastering on the Gold Coast',
        'short': 'Solid plaster to masonry walls for premium homes, apartments and commercial interiors.',
        'definition': 'Solid plastering is a hard plaster finish applied by hand to block or masonry walls, screeded flat and ready for paint or a specialty finish. It gives a denser, more durable wall than sheet lining and is the usual base for Venetian and polished plaster.',
        'scope': ['Set-out and screeding to level', 'Solid plaster to walls, returns and reveals', 'Corners, junctions and openings', 'Base coat for specialty finishes', 'Handover ready for paint'],
        'used': ['Luxury residential interiors', 'Apartments and multi-residential', 'Commercial and hospitality interiors', 'Base for Venetian plaster and feature finishes'],
        'considerations': [
            ('Substrate', 'Masonry needs to be clean, sound and free of mortar snots. Mixed substrates need the junction detail agreed.'),
            ('Sequencing', 'Services rough-in and window frames before plaster. Joinery and tiling after.'),
            ('Tolerances', 'If a specialty finish is going over it, the base needs to be flatter than for paint. Tell us the final finish when pricing.'),
            ('Drying', 'Plaster needs drying time before paint or a coating. Build it into the program for the trades that follow.'),
        ],
        'faqs': [
            ('Can you plaster over lightweight or panel walls?', tbc('confirm substrates')),
            ('Do you do set plaster as well?', tbc('confirm')),
        ],
        'article': 'what-to-send-for-a-render-quote',
    },
    {
        'slug': 'architectural-coatings', 'name': 'Architectural coatings', 'img': 'project-4',
        'h1': 'Architectural and texture coatings',
        'short': 'Specified coating and texture systems for facades, feature walls and design-led projects.',
        'definition': 'Architectural coatings are specified render and coating systems, from smooth to textured and stone-look finishes, applied to the manufacturer\'s requirements. They include texture coatings and feature walls. The finish is part of the design, so colour and texture are matched to an approved sample.',
        'scope': ['Coating systems applied to the nominated specification', 'Texture coatings from fine sand to heavy trowelled finishes', 'Feature walls, inside and out', 'Colour and texture matched to the approved sample', 'Sample panels before full application ' + tbc('confirm')],
        'used': ['Contemporary residential facades', 'Multi-residential and commercial buildings', 'Entries, foyers and feature walls', 'Hospitality interiors'],
        'considerations': [
            ('Specification', 'Name the system and the finish on the drawings or finish schedule. We price the system you specify.'),
            ('Samples', 'Texture and colour vary with light and application. Approve a sample before the building is coated.'),
            ('Consistency', 'Large areas are finished between natural breaks so the texture stays consistent across days and crews.'),
            ('Warranty paperwork', 'Some systems carry manufacturer warranties with applicator conditions ' + tbc('confirm which Coastside can provide') + '.'),
        ],
        'faqs': [
            ('Which systems do you apply?', ', '.join(SITE['systems']) + '. If your spec names a system, we apply that system.'),
            ('Are you a certified applicator?', tbc('confirm any applicator certifications')),
        ],
        'article': None,
    },
    {
        'slug': 'venetian-plaster', 'name': 'Venetian plaster', 'img': 'project-1',
        'h1': 'Venetian and polished plaster',
        'short': 'Hand-applied Venetian plaster with natural stone and marble textures.',
        'definition': 'Venetian plaster is a lime-based finish built up in thin, hand-trowelled layers and burnished to a depth and sheen paint cannot copy. Coastside applies it to feature walls, bathrooms, hospitality interiors and high-end homes, on a solid plaster base prepared for it.',
        'scope': ['Substrate preparation or solid plaster base', 'Multi-layer hand application', 'Burnishing to the agreed sheen', 'Sealing or waxing to the specification'],
        'used': ['Feature walls and entries', 'Bathrooms and ensuites ' + tbc('confirm wet areas'), 'Hospitality and retail interiors', 'Luxury residential living areas'],
        'considerations': [
            ('Substrate', 'Venetian plaster shows every imperfection in the wall under it. The base has to be flat and sound.'),
            ('Samples', 'Colour and sheen are best approved on a sample board in the room\'s light.'),
            ('Sequencing', 'Apply after dusty trades are finished. Protect it from joinery installation and trades working close by.'),
            ('Care', 'Sealed finishes are cleaned differently from paint. We hand over care instructions ' + tbc('confirm') + '.'),
        ],
        'faqs': [
            ('Can Venetian plaster go in a shower?', tbc('confirm system and approach')),
        ],
        'article': None,
    },
    {
        'slug': 'render-repairs', 'name': 'Render repairs', 'img': 'ig-4', 'conditional': True,
        'h1': 'Render repairs and restoration',
        'short': 'Cracked, drummy and damaged render repaired and matched to the existing finish.',
        'definition': 'Render repair is the removal and replacement of cracked, drummy or damaged render, matched to the existing texture, profile and colour. The cause is assessed before patching so the repair does not fail again.',
        'scope': ['Inspection of the failed area', 'Removal of loose and drummy render', 'Repair matched to the existing finish', 'Ready for paint or coating'],
        'used': ['Renovations and extensions', 'Strata and building maintenance', 'Pre-sale and pre-painting repairs', 'Older homes'],
        'considerations': [
            ('Cause', 'Cracks from movement, water or a failed substrate come back if only the surface is patched.'),
            ('Matching', 'Texture and profile are matched on site. Colour usually needs a full wall or elevation recoat to match.'),
        ],
        'faqs': [],
        'article': None,
    },
]
SVC = {s['slug']: s for s in SERVICES}

# ------------------------------------------------------------------ LOCATIONS
LOCATIONS = [
    {
        'slug': 'gold-coast', 'name': 'Gold Coast', 'published': True, 'img': 'ig-2',
        'h1': 'Solid plastering and rendering contractor, Gold Coast',
        'lead': 'Coastside is based on the Gold Coast. Most of our work is here: architect-designed homes, canal-front rebuilds, townhouse and apartment developments and commercial fitouts.',
        'conditions': [
            ('Salt air near the beach and canals', 'Beachfront and canal-front buildings take salt spray and wind-driven rain. System choice, detailing at sills and parapets, and the coating over the render matter more here than inland.'),
            ('Heat, humidity and summer storms', 'Render cures faster in heat and wind, and storms stop work at short notice. Programs through summer need weather allowances and protection for fresh work.'),
            ('Canal-front access', 'Many canal homes have tight side access and limited street frontage, which affects scaffold, pump placement and material handling.'),
            ('Mid and high-rise facades', 'Beachfront residential towers and mid-rise apartments need staged work at height, hoist access and a crew sized to the scaffold program.'),
            ('Knock-down rebuilds and renovations', 'Established suburbs mix new builds with renovations, where new render has to meet or match existing walls.'),
        ],
        'councils': 'City of Gold Coast. Work in Queensland is licensed through the QBCC.',
        'suburbs': tbc('suburbs worked in, from the project list'),
        'faqs': [
            ('Are you licensed in Queensland?', 'Coastside holds a QBCC licence ' + tbc('number and class') + '. Details are in the builder pack.'),
            ('Do you work north of the Gold Coast?', 'Yes, into South East Brisbane ' + tbc('confirm areas') + '.'),
            ('Can you work on canal-front homes with restricted access?', 'Yes. Tell us the access when you send plans so we can plan the scaffold and the material handling.'),
        ],
    },
    {
        'slug': 'northern-rivers', 'name': 'Northern Rivers', 'published': False, 'img': 'hero',
        'h1': 'Rendering and plastering, Tweed Coast to Byron Bay',
        'lead': 'Draft page. Publishes only if Coastside holds a NSW contractor licence and has projects in the area.',
        'conditions': [], 'councils': 'Tweed Shire and Byron Shire councils. NSW work is licensed through NSW Fair Trading.',
        'suburbs': '', 'faqs': [],
    },
]
LOC = {l['slug']: l for l in LOCATIONS}

# ------------------------------------------------------------------ PROJECTS
# Only what we know is written as fact. Everything else is a chip to capture in
# Steve's project interview.
PROJECTS = [
    {'slug': 'brakes-crescent-miami', 'title': 'Brakes Crescent, Miami', 'location': 'gold-coast', 'suburb': 'Miami',
     'services': ['external-rendering'], 'sector': 'luxury', 'build': 'new', 'featured': True,
     'img': 'ig-3', 'gallery': ['ig-3', 'steve', 'ig-1'],
     'summary': 'A clean, modern coastal build in Miami on the southern Gold Coast.',
     'builder': tbc('builder, with permission'), 'year': tbc('year'), 'systems': tbc('system used'),
     'alt': 'Two-storey rendered coastal home at Brakes Crescent, Miami'},
    {'slug': 'coastal-residence', 'title': 'Coastal residence', 'location': 'gold-coast', 'suburb': tbc('suburb'),
     'services': ['external-rendering', 'architectural-coatings'], 'sector': 'luxury', 'build': 'new', 'featured': False,
     'img': 'hero', 'gallery': ['hero'], 'summary': 'White rendered facade with battens and a stone base.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'White rendered coastal home with timber battens and a stone base'},
    {'slug': 'canal-front-residence', 'title': 'Canal-front residence', 'location': 'gold-coast', 'suburb': tbc('suburb'),
     'services': ['external-rendering'], 'sector': 'luxury', 'build': 'new', 'featured': False,
     'img': 'contact', 'gallery': ['contact', 'ig-5', 'ig-6'], 'summary': 'External render from scaffold on a canal-front home.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Coastside crew rendering a canal-front home from scaffolding'},
    {'slug': 'multi-storey-residential', 'title': 'Multi-storey residential', 'location': 'gold-coast', 'suburb': tbc('suburb'),
     'services': ['commercial-rendering', 'architectural-coatings'], 'sector': 'multi', 'build': 'new', 'featured': True,
     'img': 'project-4', 'gallery': ['project-4'], 'summary': 'Curved rendered balconies on a multi-storey residential building.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Multi-storey residential building with curved rendered balconies'},
    {'slug': 'commercial-entry', 'title': 'Commercial entry', 'location': 'gold-coast', 'suburb': tbc('suburb'),
     'services': ['commercial-rendering', 'architectural-coatings'], 'sector': 'commercial', 'build': 'new', 'featured': True,
     'img': 'project-5', 'gallery': ['project-5'], 'summary': 'Curved rendered entry wall and bench.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Rendered curved entry wall and bench at a commercial building'},
    {'slug': 'hospitality-feature-wall', 'title': 'Hospitality feature wall', 'location': 'gold-coast', 'suburb': tbc('location'),
     'services': ['solid-plastering', 'architectural-coatings'], 'sector': 'hospitality', 'build': 'reno', 'featured': False,
     'img': 'project-3', 'gallery': ['project-3'], 'summary': 'Textured plaster feature wall with a built-in bench.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Textured plaster feature wall with built-in bench and stools', 'confirm_images': True},
    {'slug': 'architectural-bathroom', 'title': 'Architectural bathroom', 'location': 'gold-coast', 'suburb': tbc('location'),
     'services': ['venetian-plaster', 'solid-plastering'], 'sector': 'luxury', 'build': 'reno', 'featured': False,
     'img': 'project-1', 'gallery': ['project-1'], 'summary': 'Dark polished plaster wall behind a freestanding bath.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Bathroom with a dark polished plaster wall and freestanding bath', 'confirm_images': True},
    {'slug': 'rendered-landscape-walls', 'title': 'Rendered landscape walls', 'location': 'gold-coast', 'suburb': tbc('suburb'),
     'services': ['external-rendering'], 'sector': 'luxury', 'build': 'new', 'featured': False,
     'img': 'project-2', 'gallery': ['project-2'], 'summary': 'Rendered garden edging and walls around stepping pavers.',
     'builder': tbc('builder'), 'year': tbc('year'), 'systems': tbc('system'),
     'alt': 'Rendered garden edging around stepping pavers'},
]
PRJ = {p['slug']: p for p in PROJECTS}

# ------------------------------------------------------------------ ARTICLES
ARTICLES = [
    {
        'slug': 'what-to-send-for-a-render-quote',
        'title': 'What to send for an accurate render quote',
        'question': 'What does a renderer need from a builder to price a job accurately?',
        'summary': 'Plans and elevations with the rendered areas marked, the finish schedule with the nominated system, the substrate, the site address and access, the program, and who supplies scaffold. Missing any of these turns a price into an allowance.',
        'services': ['external-rendering', 'commercial-rendering', 'solid-plastering'],
        'projects': ['multi-storey-residential', 'brakes-crescent-miami'],
        'reviewed': tbc('Steve review date'),
        'sections': [
            ('1. Plans and elevations, with the areas marked', 'Elevations give us wall areas, heights and openings. Mark which walls are rendered, which are cladding or face brick, and where the render stops. Sections help where parapets, sills and balconies are involved.'),
            ('2. The finish schedule and nominated system', 'The system (for example an acrylic render with a texture coat, or a cement render for paint) changes material, labour and the number of coats. If the architect has named a manufacturer, include it.'),
            ('3. The substrate on each elevation', 'Block, brick, lightweight panel or a mix. Each needs a different preparation and a system rated for it. Mixed substrates need junction details.'),
            ('4. Site address and access', 'Street frontage, side access, canal or waterfront, height and parking all change how we set up and move material.'),
            ('5. Program and target start', 'Give us scaffold dates per elevation if you have them. A start date on its own does not tell us how many people to put on.'),
            ('6. Scaffold and who supplies it', 'Say whether scaffold is by the builder or needs pricing, and whether it is in place for the whole job or moved between elevations.'),
            ('7. Inclusions and exclusions you expect', 'Coating over the render, beads, control joints, patching after other trades, and cleaning. Agreeing this at quote stage avoids variations later.'),
            ('8. Tender close date and site contact', 'If it is a tender, the close date. For awarded work, who we speak to on site.'),
        ],
    },
]
ART = {a['slug']: a for a in ARTICLES}

# ------------------------------------------------------------------ BUILDER DOCUMENTS
DOCUMENTS = [
    {'title': 'Capability statement', 'type': 'Capability', 'access': 'public', 'file': 'builder-pack/coastside-capability-statement.pdf', 'issued': 'Sep 2026 (draft)', 'expires': 'Reviewed yearly'},
    {'title': 'QBCC licence', 'type': 'Licence', 'access': 'public', 'file': None, 'issued': tbc('date'), 'expires': tbc('renewal')},
    {'title': 'Certificate of currency: public liability', 'type': 'Insurance', 'access': 'request', 'file': None, 'issued': tbc('date'), 'expires': tbc('expiry')},
    {'title': 'Certificate of currency: workers compensation', 'type': 'Insurance', 'access': 'request', 'file': None, 'issued': tbc('date'), 'expires': tbc('expiry')},
    {'title': 'SWMS: rendering and work at height', 'type': 'Safety', 'access': 'request', 'file': None, 'issued': tbc('date'), 'expires': 'Made site-specific per job'},
    {'title': 'WHS policy', 'type': 'Safety', 'access': 'request', 'file': None, 'issued': tbc('date'), 'expires': tbc('review')},
]
