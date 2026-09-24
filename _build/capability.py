"""Builds builder-pack/coastside-capability-statement.pdf (A4, 2 pages).
Needs Playwright + Chromium: python3 _build/capability.py <site_dir>"""
import os, sys, html, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C
from playwright.sync_api import sync_playwright

site = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'v2'))
img = lambda n: pathlib.Path(site, 'img', n).as_uri()
t = C.tbc

svc = ''.join(f'<li><b>{s["name"]}</b><span>{s["short"]}</span></li>' for s in C.SERVICES)
projs = ''.join(f'''<div class="pj"><img src="{img(os.path.basename(C.PROJ[k]['img']).replace('.jpg','-sm.jpg') if not C.PROJ[k]['img'].endswith('-sm.jpg') else os.path.basename(C.PROJ[k]['img']))}"><div><b>{C.PROJ[k]['title']}</b><span>{' / '.join(C.SECTOR_NAME[x] for x in C.PROJ[k]['sectors'].split())}</span><span>Builder: {C.PROJ[k]['builder']}</span></div></div>''' for k in ['miami','multistorey','commercial-entry','hospitality'])

doc = f'''<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#1A1A1A;-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:9.5pt;line-height:1.5}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#FAF8F5}}
.pg:last-child{{page-break-after:auto}}
.top{{background:#1A1A1A;color:#F5F2ED;padding:10mm 14mm;display:flex;align-items:center;gap:6mm}}
.top img{{width:20mm;height:20mm;border-radius:50%}}
.top h1{{font-size:20pt;font-weight:800;letter-spacing:-.3pt;line-height:1.1}}
.top p{{font-size:7.5pt;letter-spacing:1.6pt;text-transform:uppercase;color:#D4CFC7;margin-top:1.5mm}}
.top .r{{margin-left:auto;text-align:right;font-size:7.5pt;letter-spacing:1.2pt;text-transform:uppercase;color:#D4CFC7}}
.band{{height:42mm;background:url('{img('project-4.jpg')}') center 40%/cover}}
.in{{padding:7mm 14mm 0}}
.eb{{font-size:7pt;letter-spacing:2pt;text-transform:uppercase;color:#6B6760;margin-bottom:2.5mm;font-weight:600}}
h2{{font-size:15pt;letter-spacing:-.3pt;line-height:1.2;margin-bottom:3mm}}
.lead{{font-size:10.5pt;line-height:1.6;color:#4f4d49;max-width:170mm}}
.stats{{display:grid;grid-template-columns:repeat(4,1fr);border-top:.8pt solid #2A2A2A;border-bottom:.5pt solid #D4CFC7;margin:5mm 0 6mm}}
.stats div{{padding:3mm 0}}
.stats b{{display:block;font-size:17pt;font-weight:300;letter-spacing:-.5pt}}
.stats span{{font-size:6.8pt;letter-spacing:1.4pt;text-transform:uppercase;color:#6B6760}}
.cols{{display:grid;grid-template-columns:1.35fr 1fr;gap:9mm}}
ul.svc{{list-style:none}}
ul.svc li{{padding:1.6mm 0;border-bottom:.5pt solid #D4CFC7;display:grid;grid-template-columns:40mm 1fr;gap:3mm}}
ul.svc b{{font-weight:600;font-size:9pt}}
ul.svc span{{color:#4f4d49;font-size:8.3pt}}
.box{{background:#2A2A2A;color:#F5F2ED;padding:6mm}}
.box .eb{{color:#D4CFC7}}
.box p,.box li{{font-size:8.6pt;color:#D4CFC7;line-height:1.55}}
.box ul{{list-style:none;margin-bottom:4mm}}
.box li{{padding:1.4mm 0;border-bottom:.5pt solid rgba(255,255,255,.12)}}
.box li b{{color:#fff;font-weight:600}}
.tbc{{border:.7pt dashed #8B7355;color:#8B7355;background:rgba(139,115,85,.08);padding:0 1.5mm;border-radius:1mm;font-size:.9em;white-space:nowrap}}
.box .tbc{{border-color:#c7ab86;color:#e0c9a8}}
.foot{{position:absolute;left:14mm;right:14mm;bottom:8mm;display:flex;justify-content:space-between;font-size:6.8pt;letter-spacing:1pt;text-transform:uppercase;color:#6B6760;border-top:.5pt solid #D4CFC7;padding-top:3mm}}
table{{width:100%;border-collapse:collapse}}
th,td{{text-align:left;vertical-align:top;padding:2.1mm 0;border-bottom:.5pt solid #D4CFC7;font-size:8.8pt}}
th{{width:48mm;font-size:6.8pt;letter-spacing:1.3pt;text-transform:uppercase;color:#6B6760;font-weight:600;padding-top:2.6mm}}
tr:first-child th,tr:first-child td{{border-top:.8pt solid #2A2A2A}}
.pjs{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.pj{{display:flex;gap:3mm;align-items:flex-start}}
.pj img{{width:30mm;height:22mm;object-fit:cover}}
.pj b{{display:block;font-size:8.8pt;margin-bottom:.6mm}}
.pj span:not(.tbc){{display:block;font-size:7.6pt;color:#4f4d49;margin-bottom:.6mm}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}}
.steps div{{border-top:.8pt solid #8B7355;padding-top:2mm}}
.steps b{{display:block;font-size:8.6pt;margin-bottom:1mm}}
.steps span:not(.tbc){{font-size:7.8pt;color:#4f4d49;line-height:1.5;display:block}}
.contact{{background:#1A1A1A;color:#F5F2ED;padding:6mm 14mm;position:absolute;left:0;right:0;bottom:17mm;display:grid;grid-template-columns:repeat(4,1fr);gap:4mm}}
.contact span:not(.tbc){{display:block;font-size:6.5pt;letter-spacing:1.4pt;text-transform:uppercase;color:#8A8680;margin-bottom:1mm}}
.contact b{{font-size:8.8pt;font-weight:500}}
</style></head><body>
<section class="pg">
  <div class="top"><img src="{img('logo.png')}"><div><h1>Coastside Solid Plastering</h1><p>Capability statement</p></div><div class="r">Draft for review<br>September 2026</div></div>
  <div class="band"></div>
  <div class="in">
    <div class="eb">Who we are</div>
    <h2>Solid plastering, render and architectural coatings for builders, architects and designers.</h2>
    <p class="lead">Coastside is run by Steve, a second-generation plasterer with 25+ years in the trade. A 15+ crew works across luxury residential, multi-residential, commercial and hospitality projects from Byron Bay to the Gold Coast to South East Brisbane.</p>
    <div class="stats"><div><b>25+</b><span>Years in the trade</span></div><div><b>15+</b><span>Crew</span></div><div><b>3</b><span>Regions</span></div><div><b>8</b><span>Services</span></div></div>
    <div class="cols">
      <div><div class="eb">Services</div><ul class="svc">{svc}</ul></div>
      <div class="box">
        <div class="eb">Sectors</div>
        <ul><li><b>Luxury residential</b></li><li><b>Multi-residential</b></li><li><b>Commercial and retail</b></li><li><b>Hospitality fitouts</b></li></ul>
        <div class="eb">Systems we apply</div>
        <p>{', '.join(C.SYSTEMS)}</p>
        <div class="eb" style="margin-top:4mm">Service area</div>
        <p>{C.AREA}</p>
      </div>
    </div>
  </div>
  <div class="foot"><span>Coastside Solid Plastering Pty Ltd · ABN {C.ABN}</span><span>Page 1 of 2</span></div>
</section>
<section class="pg">
  <div class="top"><img src="{img('logo.png')}"><div><h1>Compliance and track record</h1><p>Capability statement</p></div><div class="r">Draft for review<br>September 2026</div></div>
  <div class="in">
    <div class="eb">Compliance</div>
    <table>
      <tr><th>Business</th><td>{C.LEGAL_NAME} · ABN {C.ABN}</td></tr>
      <tr><th>QBCC licence</th><td>{t('licence number and class')}</td></tr>
      <tr><th>NSW licence</th><td>{t('confirm if held')}</td></tr>
      <tr><th>Public liability</th><td>{t('cover amount and insurer')} · certificate of currency on request</td></tr>
      <tr><th>Workers compensation</th><td>{t('WorkCover Queensland policy')} · certificate of currency on request</td></tr>
      <tr><th>Safety</th><td>SWMS supplied for each job {t('confirm')}</td></tr>
      <tr><th>Trade references</th><td>{t('2 to 3 builders or designers, with permission')}</td></tr>
    </table>
    <div class="eb" style="margin-top:7mm">Selected projects</div>
    <div class="pjs">{projs}</div>
    <div class="eb" style="margin-top:7mm">How a job runs</div>
    <div class="steps">
      <div><b>01 Send the plans</b><span>Drawings, elevations and the finish spec.</span></div>
      <div><b>02 Itemised quote</b><span>Priced to your spec and program. Turnaround {t('confirm')}.</span></div>
      <div><b>03 Program locked</b><span>Start dates and crew numbers agreed before we mobilise.</span></div>
      <div><b>04 Finish and handover</b><span>Walk-through with your site manager {t('confirm')}.</span></div>
    </div>
  </div>
  <div class="contact">
    <div><span>Contact</span><b>Steve</b></div>
    <div><span>Email</span><b>{C.EMAIL}</b></div>
    <div><span>Phone</span><b>{C.PHONE}</b></div>
    <div><span>Web</span><b>{t('domain to confirm')}</b></div>
  </div>
  <div class="foot"><span>Coastside Solid Plastering Pty Ltd · ABN {C.ABN}</span><span>Page 2 of 2</span></div>
</section>
</body></html>'''

out_html = os.path.join(site, 'builder-pack', '_capability.html')
pathlib.Path(out_html).write_text(doc, encoding='utf-8')
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(pathlib.Path(out_html).as_uri())
    pg.wait_for_load_state('networkidle')
    pg.pdf(path=os.path.join(site, 'builder-pack', 'coastside-capability-statement.pdf'), format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
os.remove(out_html)
print('ok')
