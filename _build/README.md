# Coastside v2 (Builder-ready) build

Static multi-page site generated from `content.py` (copy and data) and `build.py` (layout).
Jekyll ignores this `_build` folder, so GitHub Pages never serves it.

## Rebuild
    python3 _build/build.py                 # writes pages into v2/
    python3 _build/capability.py v2         # rebuilds the capability statement PDF (needs Playwright)

For launch at the site root on a real domain:
    OUT_DIR=. SITE_URL=https://<domain>/ EXPLICIT_INDEX=0 CONCEPT=0 python3 _build/build.py
(and copy v2/assets, v2/img, v2/builder-pack/*.pdf across).

## TBC chips
Anything unconfirmed is wrapped in tbc() and shows as a dashed bronze chip.
Search content.py for tbc( to find every open item. Remove the wrapper once Steve confirms.

## Known before launch
- Forms post to Web3Forms with TSE's key, so enquiries land with Mel. Swap to Steve's key or the enquiry-dashboard endpoint.
- project-1 (bathroom) and project-3 (hospitality) images: confirm they are Coastside's own work.
- CONCEPT=1 adds noindex. Turn off at launch.
