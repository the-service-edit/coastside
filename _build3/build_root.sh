#!/bin/bash
# Rebuild the V7 Builder system and deploy it to the site root (coastside.theserviceedit.com/).
# Builds into a temp dir (never touches the /v7/ redirect stubs), rewrites media refs to /v7/img, /v7/assets
# and the capability PDF, then copies HTML + sitemap into the repo root.   Usage: bash _build3/build_root.sh
set -e
R="$(cd "$(dirname "$0")/.." && pwd)"; T="$(mktemp -d)"
ln -s "$R/v7/img" "$T/img"
(cd "$R/_build3" && THEME=v7 OUT_DIR="$T" SITE_URL=https://coastside.theserviceedit.com/ EXPLICIT_INDEX=1 python3 build.py >/dev/null)
rm "$T/img"
python3 - "$T" <<'PY'
import sys,os,re
T=sys.argv[1]
for dp,_,fs in os.walk(T):
  for f in fs:
    if not f.endswith('.html'): continue
    p=os.path.join(dp,f); s=open(p).read()
    s=s.replace('https://coastside.theserviceedit.com/img/','https://coastside.theserviceedit.com/v7/img/')
    s=re.sub(r'(?<=["\'( ])(?:\.\./)*(img|assets)/', r'/v7/\1/', s)
    s=re.sub(r'(?<=["\'( ])(?:\.\./)*builder-pack/coastside-capability-statement\.pdf', '/v7/builder-pack/coastside-capability-statement.pdf', s)
    open(p,'w').write(s)
PY
(cd "$T" && find . -name '*.html' -o -name sitemap.xml) | while read f; do mkdir -p "$R/$(dirname "$f")"; cp "$T/$f" "$R/$f"; done
echo "Root rebuilt from _build3 (robots.txt left as is)."
