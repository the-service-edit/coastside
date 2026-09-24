# Coastside V3 prototype

    python3 _build3/build.py     # writes v3/ (needs Pillow)

- data.py: collections (SERVICES, LOCATIONS, PROJECTS, ARTICLES, DOCUMENTS). Projects reference services and a location; service and location pages list matching projects automatically.
- build.py: templates, schema, sitemap.
- v3/assets/site.js: nav, filters, 3-step quote, attribution (first/last touch UTMs), dataLayer events.
- tbc() chips mark facts Steve must confirm. CONCEPT=1 adds noindex.
- Not in this prototype: file storage for uploads (Supabase at launch), GA4 ID, Northern Rivers and render repairs pages (conditional), Astro migration.
