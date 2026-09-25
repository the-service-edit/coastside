/**
 * Coastside enquiry mailer (Google Apps Script web app)
 * ---------------------------------------------------
 * Website quote form -> this script -> two emails:
 *   1. To NOTIFY_TO: "New enquiry CSP-0001" with the enquiry summary PDF attached (and the same summary in the body).
 *   2. To the person who enquired: the auto-reply, with a copy of their enquiry.
 * Returns {"success":true,"ref":"CSP-0001"} to the website.
 *
 * Only Google permission needed: "Send email as you". No Drive, Sheets or external requests.
 * Deploy: Deploy > New deployment > Web app > Execute as: Me > Who has access: Anyone.
 */

var CONFIG = {
  NOTIFY_TO: 'hello@theserviceedit.com',          // who receives new enquiries. Change to Steve's address once confirmed.
  NOTIFY_CC: '',                                   // optional second inbox
  AUTOREPLY: true,                                 // send the auto-reply to the enquirer
  REPLY_TO: 'hello@theserviceedit.com',            // where the enquirer's replies go. Change to Steve's address once confirmed.
  FROM_NAME: 'Coastside Solid Plastering',
  REF_PREFIX: 'CSP-',
  TIMEZONE: 'Australia/Brisbane',
  MAX_PER_HOUR: 30,                                // global cap, stops abuse of the auto-reply
  RESPONSE_TIME: ''                                // e.g. 'within one business day'. Leave blank until Steve confirms.
};

var LOGO = 'data:image/jpeg;base64,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';

var SERVICE_NAMES = {
  'external-rendering': 'External rendering', 'commercial-rendering': 'Commercial rendering',
  'solid-plastering': 'Solid plastering', 'architectural-coatings': 'Architectural coatings',
  'venetian-plaster': 'Venetian plaster', 'render-repairs': 'Render repairs'
};
var TRADE_ROLES = ['builder', 'developer', 'architect / designer', 'project manager', 'architect', 'designer'];

function doGet() {
  return json_({ ok: true, service: 'coastside-enquiry' });
}

function doPost(e) {
  try {
    var d = parse_(e);
    if (d.botcheck) return json_({ success: true });                      // honeypot: pretend success
    if (!clean_(d.name) || !isEmail_(d.email)) return json_({ success: false, error: 'missing name or email' });
    if (!underCap_()) return json_({ success: false, error: 'busy' });

    var ref = nextRef_();
    var now = new Date();
    var v = view_(d, ref, now);

    var autoreplyOk = false;
    if (CONFIG.AUTOREPLY && firstReplyToday_(v.emailRaw)) {
      try {
        MailApp.sendEmail({
          to: v.emailRaw, replyTo: CONFIG.REPLY_TO, name: CONFIG.FROM_NAME,
          subject: 'Thanks for your enquiry, ' + v.firstNameRaw,
          htmlBody: autoreplyHtml_(v), body: autoreplyText_(v)
        });
        autoreplyOk = true;
      } catch (err) { console.error('autoreply failed', err); }
    }
    v.autoreplyLine = autoreplyOk
      ? '<b>Auto-reply sent</b> to ' + v.email + ' at ' + v.time + '. They\'ve been asked to send plans, specification, stage and timing by replying.'
      : '<b>No auto-reply sent</b> to ' + v.email + '. Reply to them directly.';
    var html = pdfHtml_(v);
    var pdf = Utilities.newBlob(html, 'text/html', ref + '.html').getAs('application/pdf').setName('Coastside enquiry ' + ref + '.pdf');

    var notify = {
      to: CONFIG.NOTIFY_TO, replyTo: v.emailRaw, name: 'Coastside website',
      subject: 'New enquiry ' + ref + ': ' + v.nameRaw + (v.companyRaw ? ', ' + v.companyRaw : '') + ' (' + v.headlineRaw + ')',
      htmlBody: html.replace(LOGO, 'cid:logo'), body: notifyText_(v), attachments: [pdf],
      inlineImages: { logo: Utilities.newBlob(Utilities.base64Decode(LOGO.split(',')[1]), 'image/jpeg', 'logo.jpg') }
    };
    if (CONFIG.NOTIFY_CC) notify.cc = CONFIG.NOTIFY_CC;
    MailApp.sendEmail(notify);

    return json_({ success: true, ref: ref });
  } catch (err) {
    console.error(err);
    return json_({ success: false, error: 'server' });
  }
}

/* ---------- helpers ---------- */
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

function parse_(e) {
  var d = {};
  if (e && e.postData && e.postData.contents) {
    try { d = JSON.parse(e.postData.contents); } catch (x) { d = {}; }
  }
  if (e && e.parameter) for (var k in e.parameter) if (!(k in d)) d[k] = e.parameter[k];
  return d;
}

function clean_(s, max) {
  if (s === undefined || s === null) return '';
  s = String(s).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim();
  return s.slice(0, max || 300);
}
function esc_(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}
function isEmail_(s) { return /^[^\s@<>"]+@[^\s@<>"]+\.[^\s@<>"]+$/.test(clean_(s)); }
var NP = '<span style="color:#A39E96;">Not provided</span>';
function orNP_(s) { return s ? esc_(s) : NP; }

function underCap_() {
  var c = CacheService.getScriptCache(), k = 'count_' + Utilities.formatDate(new Date(), 'UTC', 'yyyyMMddHH');
  var n = Number(c.get(k) || 0);
  if (n >= CONFIG.MAX_PER_HOUR) return false;
  c.put(k, String(n + 1), 3700);
  return true;
}
function firstReplyToday_(email) {
  var c = CacheService.getScriptCache(), k = 'ar_' + Utilities.base64EncodeWebSafe(email.toLowerCase()).slice(0, 200);
  if (c.get(k)) return false;
  c.put(k, '1', 21600);
  return true;
}
function nextRef_() {
  var lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    var p = PropertiesService.getScriptProperties();
    var n = Number(p.getProperty('REF_COUNTER') || 0) + 1;
    p.setProperty('REF_COUNTER', String(n));
    return CONFIG.REF_PREFIX + ('0000' + n).slice(-4);
  } finally { lock.releaseLock(); }
}

function view_(d, ref, now) {
  var role = clean_(d.role, 60);
  var trade = TRADE_ROLES.indexOf(role.toLowerCase()) > -1;
  var services = clean_(d.services, 300).split(/\s*,\s*/).filter(String).map(function (s) { return SERVICE_NAMES[s] || s; });
  var build = clean_(d.build_type, 60), sector = clean_(d.sector, 60);
  var type = [services.join(', '), build ? build.toLowerCase() : ''].filter(String).join(', ');
  var loc = clean_(d.project_address, 160);
  var tender = clean_(d.is_tender, 20), close = clean_(d.tender_close, 20);
  var tenderTxt = tender ? (tender + (close ? ', closes ' + fmtDate_(close) : '')) : '';
  var plans = [];
  if (clean_(d.documents, 600)) plans.push('Files named (not uploaded): ' + clean_(d.documents, 600));
  if (clean_(d.plans_link, 400)) plans.push('Link: ' + clean_(d.plans_link, 400));
  var name = clean_(d.name, 120), company = clean_(d.company, 160), email = clean_(d.email, 200), phone = clean_(d.phone, 40);
  var firstName = name.split(/\s+/)[0] || 'there';
  var headParts = [type || 'Project enquiry', loc, sector].filter(String);
  var msg = clean_(d.message, 4000);
  var time = Utilities.formatDate(now, CONFIG.TIMEZONE, 'h:mm a').toLowerCase();
  return {
    ref: ref, received: Utilities.formatDate(now, CONFIG.TIMEZONE, 'EEE d MMM yyyy') + ', ' + time, time: time,
    leadLabel: trade ? 'Trade enquiry' : 'Homeowner enquiry', leadBg: trade ? '#8B7355' : '#5E5A55',
    role: orNP_(role), nameRaw: name, name: esc_(name), companyRaw: company, company: orNP_(company),
    emailRaw: email, email: esc_(email), phone: orNP_(phone), phoneLink: esc_(phone.replace(/[^\d+]/g, '')), hasPhone: !!phone,
    firstName: esc_(firstName), firstNameRaw: firstName,
    headline: headParts.map(esc_).join(' &nbsp;&middot;&nbsp; '), headlineRaw: headParts.join(' / '),
    projectName: orNP_(clean_(d.project_name, 160)), type: orNP_(type), location: orNP_(loc), sector: orNP_(sector),
    tender: orNP_(tenderTxt), plans: plans.length ? plans.map(esc_).join('<br>') : 'None yet',
    typeRaw: type || 'your project',
    message: msg ? esc_(msg).replace(/\n/g, '<br>') : NP, messageRaw: msg,
    source: esc_(clean_(d.submitted_from, 120) || 'website quote form'),
    utm: [clean_(d.utm_source, 60), clean_(d.utm_medium, 60), clean_(d.utm_campaign, 80)].filter(String).join(' / '),
    replyLink: 'mailto:' + encodeURIComponent(email) + '?subject=' + encodeURIComponent('Your Coastside enquiry ' + ref),
    autoreplyLine: ''
  };
}
function fmtDate_(iso) {
  var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso); if (!m) return iso;
  return Utilities.formatDate(new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3])), CONFIG.TIMEZONE, 'd MMM yyyy');
}

function row_(label, value, first) {
  return '<tr><td style="padding:11px 0;border-bottom:1px solid #E8E4DF;color:#8A8680;' + (first ? 'width:38%;' : '') + '">' + label +
    '</td><td style="padding:11px 0;border-bottom:1px solid #E8E4DF;">' + value + '</td></tr>';
}
function head_(t) {
  return '<div style="font-size:10px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:#8B7355;padding-bottom:10px;border-bottom:2px solid #1A1A1A;">' + t + '</div>';
}

/* ---------- enquiry summary (PDF + notify email body) ---------- */
function pdfHtml_(v) {
  var call = v.hasPhone
    ? '<td style="width:10px;">&nbsp;</td><td style="border:1px solid #1A1A1A;padding:12px 22px;"><a href="tel:' + v.phoneLink + '" style="color:#1A1A1A;font-size:13px;font-weight:700;letter-spacing:0.3px;text-decoration:none;">Call ' + v.phone + '</a></td>'
    : '';
  return '<!DOCTYPE html><html lang="en-AU"><head><meta charset="UTF-8"><title>Coastside enquiry ' + v.ref + '</title>' +
    '<style>@page{size:A4;margin:0}body{margin:0;padding:0;background:#FFFFFF;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;color:#1A1A1A}table{border-collapse:collapse}td{vertical-align:top}a{color:inherit;text-decoration:none}</style></head><body>' +
    '<table width="100%" cellpadding="0" cellspacing="0" style="width:100%;">' +
    '<tr><td style="background:#1A1A1A;padding:34px 48px 30px;"><table width="100%" cellpadding="0" cellspacing="0"><tr>' +
    '<td style="width:82px;vertical-align:middle;"><img src="' + LOGO + '" width="68" height="68" alt="Coastside Solid Plastering" style="display:block;width:68px;height:68px;"></td>' +
    '<td style="vertical-align:middle;padding-left:4px;"><div style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#D4CFC7;">Coastside Solid Plastering</div>' +
    '<div style="font-size:26px;font-weight:700;letter-spacing:-0.5px;color:#FFFFFF;margin-top:6px;">New enquiry</div></td>' +
    '<td style="vertical-align:middle;text-align:right;"><div style="font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#8A8680;">Reference</div>' +
    '<div style="font-size:18px;font-weight:700;color:#FFFFFF;margin-top:4px;">' + v.ref + '</div><div style="font-size:12px;color:#D4CFC7;margin-top:6px;">' + v.received + '</div></td>' +
    '</tr></table></td></tr>' +
    '<tr><td style="background:#8B7355;height:4px;line-height:4px;font-size:0;">&nbsp;</td></tr>' +
    '<tr><td style="background:#F5F2ED;padding:34px 48px 32px;">' +
    '<table cellpadding="0" cellspacing="0"><tr><td style="background:' + v.leadBg + ';color:#FFFFFF;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:7px 12px;">' + v.leadLabel + '</td>' +
    '<td style="padding-left:10px;font-size:12px;color:#5E5A55;vertical-align:middle;">' + v.role + '</td></tr></table>' +
    '<div style="font-size:30px;font-weight:700;letter-spacing:-0.6px;line-height:1.15;margin-top:16px;">' + v.name + '</div>' +
    '<div style="font-size:16px;color:#5E5A55;margin-top:4px;">' + v.company + '</div>' +
    '<div style="font-size:17px;font-weight:600;color:#1A1A1A;margin-top:18px;line-height:1.4;">' + v.headline + '</div>' +
    '<table cellpadding="0" cellspacing="0" style="margin-top:24px;"><tr><td style="background:#1A1A1A;padding:13px 22px;"><a href="' + v.replyLink + '" style="color:#FFFFFF;font-size:13px;font-weight:700;letter-spacing:0.3px;text-decoration:none;">Reply by email</a></td>' + call + '</tr></table>' +
    '</td></tr>' +
    '<tr><td style="padding:34px 48px 10px;"><table width="100%" cellpadding="0" cellspacing="0"><tr>' +
    '<td style="width:46%;padding-right:28px;">' + head_('Contact') + '<table width="100%" cellpadding="0" cellspacing="0" style="font-size:13px;">' +
    row_('Name', v.name, true) + row_('Role', v.role) + row_('Company', v.company) +
    row_('Email', '<a href="mailto:' + v.email + '" style="color:#1A1A1A;border-bottom:1px solid #8B7355;">' + v.email + '</a>') +
    row_('Phone', v.phone) + '</table></td>' +
    '<td style="width:54%;">' + head_('Project') + '<table width="100%" cellpadding="0" cellspacing="0" style="font-size:13px;">' +
    row_('Project', v.projectName, true) + row_('Scope', v.type) + row_('Location', v.location) + row_('Sector', v.sector) +
    row_('Tender', v.tender) + row_('Plans', v.plans) + '</table></td>' +
    '</tr></table></td></tr>' +
    '<tr><td style="padding:26px 48px 34px;">' + head_('Their message') +
    '<div style="background:#FAF8F5;border-left:3px solid #8B7355;padding:20px 24px;margin-top:16px;font-size:14px;line-height:1.65;color:#2A2A2A;">' + v.message + '</div></td></tr>' +
    '<tr><td style="padding:0 48px;"><table width="100%" cellpadding="0" cellspacing="0" style="background:#E8E4DF;"><tr><td style="padding:14px 20px;font-size:12px;color:#2A2A2A;">' + v.autoreplyLine + '</td></tr></table></td></tr>' +
    '<tr><td style="padding:22px 48px 30px;"><table width="100%" cellpadding="0" cellspacing="0" style="font-size:10.5px;color:#8A8680;"><tr>' +
    '<td>Coastside Solid Plastering &middot; Byron Bay to the Gold Coast to South East Brisbane</td>' +
    '<td style="text-align:right;">Submitted via ' + v.source + (v.utm ? ' (' + esc_(v.utm) + ')' : '') + '</td></tr></table></td></tr>' +
    '</table></body></html>';
}

function notifyText_(v) {
  return 'New enquiry ' + v.ref + ' (' + v.received + ')\n\n' +
    v.nameRaw + (v.companyRaw ? ', ' + v.companyRaw : '') + '\n' + v.emailRaw + '\n\n' +
    v.headlineRaw + '\n\n' + (v.messageRaw || '') + '\n\nThe full summary is attached as a PDF. Reply to this email to reply to them.';
}

/* ---------- auto-reply to the enquirer ---------- */
function autoreplyHtml_(v) {
  var when = CONFIG.RESPONSE_TIME ? ' and we\'ll be in touch ' + esc_(CONFIG.RESPONSE_TIME) : ' and we\'ll be in touch shortly';
  return '<div style="font-family:Helvetica,Arial,sans-serif;font-size:15px;line-height:1.6;color:#1A1A1A;max-width:560px;">' +
    '<p>Hi ' + v.firstName + ',</p>' +
    '<p>Thanks for getting in touch with Coastside Solid Plastering. We\'ve received your enquiry (reference ' + v.ref + ')' + when + '.</p>' +
    '<p>To help us quote accurately, reply to this email with anything you already have:</p>' +
    '<ul style="padding-left:20px;margin:0 0 16px;"><li>Plans or drawings</li><li>Finish or coating specification</li><li>Site location and project stage</li><li>Program and timing</li></ul>' +
    '<p>You can see recent work on Instagram: <a href="https://www.instagram.com/coast_side_plastering/" style="color:#8B7355;">@coast_side_plastering</a></p>' +
    '<p>Steve<br>Coastside Solid Plastering<br><span style="color:#5E5A55;">Byron Bay to the Gold Coast to South East Brisbane</span></p>' +
    '<hr style="border:0;border-top:1px solid #E8E4DF;margin:28px 0 16px;">' +
    '<p style="font-size:12px;color:#8A8680;margin:0 0 6px;text-transform:uppercase;letter-spacing:1.5px;">Your enquiry</p>' +
    '<table cellpadding="0" cellspacing="0" style="font-size:13px;color:#2A2A2A;">' +
    '<tr><td style="padding:3px 16px 3px 0;color:#8A8680;">Scope</td><td>' + v.type + '</td></tr>' +
    '<tr><td style="padding:3px 16px 3px 0;color:#8A8680;">Location</td><td>' + v.location + '</td></tr>' +
    '<tr><td style="padding:3px 16px 3px 0;color:#8A8680;vertical-align:top;">Notes</td><td>' + v.message + '</td></tr></table></div>';
}
function autoreplyText_(v) {
  return 'Hi ' + v.firstNameRaw + ',\n\nThanks for getting in touch with Coastside Solid Plastering. We\'ve received your enquiry (reference ' + v.ref + ')' +
    (CONFIG.RESPONSE_TIME ? ' and we\'ll be in touch ' + CONFIG.RESPONSE_TIME : ' and we\'ll be in touch shortly') + '.\n\n' +
    'To help us quote accurately, reply to this email with anything you already have:\n- Plans or drawings\n- Finish or coating specification\n- Site location and project stage\n- Program and timing\n\n' +
    'Recent work on Instagram: @coast_side_plastering\n\nSteve\nCoastside Solid Plastering\nByron Bay to the Gold Coast to South East Brisbane';
}

/* ---------- run this once from the editor to test (sends to NOTIFY_TO only) ---------- */
function testSend() {
  var r = doPost({ postData: { contents: JSON.stringify({
    role: 'Builder', name: 'Sample Name', company: 'Sample Constructions Pty Ltd', email: CONFIG.NOTIFY_TO, phone: '0400 000 000',
    project_name: 'Mermaid Beach residence', project_address: 'Mermaid Beach', sector: 'Luxury residential', build_type: 'New build',
    services: 'external-rendering, architectural-coatings', is_tender: 'Yes', tender_close: '2026-10-15',
    plans_link: 'https://example.com/plans', message: 'TEST. Two-storey coastal home, approx. 380 m2 of external render over AAC and blockwork.',
    submitted_from: '/v7/quote/'
  }) } });
  Logger.log(r.getContent());
}
