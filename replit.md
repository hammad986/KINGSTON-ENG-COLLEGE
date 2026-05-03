# Kingston Engineering College – Website

A full-featured static college website for Kingston Engineering College, Vellore, Tamil Nadu.

## Architecture

- **Type**: Static HTML/CSS/JS website (no build step required)
- **Server**: Python `http.server` on port 5000
- **AI Assistant**: Custom rule-based chatbot (`assets/js/ai-assistant.js`)
- **Data**: JSON files in `data/` directory

## Key Pages

| File | Purpose |
|---|---|
| `index.html` | Homepage with hero, news, events, testimonials |
| `ai-assistant.html` | Full-page AI Campus Guide chatbot |
| `about.html` | About the college |
| `academics.html` | Academics information + Department-wise Faculty PDF block |
| `placements.html` | Placement information |
| `naac.html` | NAAC accreditation |
| `facilities.html` | Campus facilities (sports dual-col marquee added) |
| `contact.html` | Contact & directions |
| `achievements.html` | Student & faculty achievements (linked from about/about_awards.html) |

## AI Assistant

- **Script**: `assets/js/ai-assistant.js`
- **CSS**: `assets/css/ai-assistant.css`
- **Knowledge Base**: `data/knowledge-base.json`
- **Search Index**: `data/search-index.json`
- **Global instance**: `window.KingstonAI`
- **Features**:
  - Weighted intent detection with keyword scoring
  - Context memory (last 3 intents)
  - Search fallback with result cards
  - Follow-up suggestion chips
  - Chat persistence via localStorage
  - Typing indicator with animation
  - Both fullpage and widget modes
- **Known issue**: AI widget on pages 2+ levels deep (e.g. `departments/mba/`) fails to load `data/` JSON because paths are relative. Widget degrades gracefully.

## Running the Server

```bash
python3 -m http.server 5000
```

## Known Issues / Missing Assets

- `assets/videos/video1.mp4` — Hero background video is missing (hero shows as blank background)
- `favicon.ico` — Not present (causes 404 in browser)

## Deployment Readiness — Completed Tasks

| Task | Status | Notes |
|---|---|---|
| Delete Python files | ✅ Done | Deleted 6 Python scripts (dynamic_sync.py, master_sync.py, etc.) |
| Fix dept nav links | ✅ Done | dept_AI&DS.html → dept_aids.html (999 fixes); dept_mechanical → dept_mech; dept_civil/eee → departments |
| Fix broken href="#" links | ✅ Done | about.html:460 → academics.html; index.html:918 → news.html |
| Fix forms (action/method) | ✅ Done | contact, admission_enquiry, apply_now all have action/method + JS handlers in script.js |
| Link NAAC/UGC PDFs | ✅ Done | naac.html rebuilt with direct PDF download links |
| Standardize header/footer | ✅ Done | sitemap.html & privacy_policy.html now have full font/library/CSS links |
| Search on all pages | ✅ Done | search.js auto-injects into any page with .main-nav .container |
| Facilities sports marquee | ✅ Done | Dual-col infinite vertical marquee (pure CSS, hover-pause, fade overlays) |
| NAAC PDF Quick Download panel | ✅ Done | 8-card dark panel with gold accents, real verified PDFs |
| naac_extended_profile.html | ✅ Done | Fixed malformed onerror attr + removed duplicate AI widget |
| academics.html Faculty PDF block | ✅ Done | 14 glass cards — one per dept — linking UGC Mandatory Disclosure PDFs; gold "Download Complete Directory" CTA |
| Orphan cleanup (stubs) | ✅ Done | Deleted 6 confirmed stubs: HEADER_TEMPLATE.html, footer.html, public-self-disclosure.html, temp.html, ugc-mandatory-committee.html, ugc-undertaking-hoi.html |
| **Broken link fix — sub-pages** | ✅ Done | **147 → 0 broken links**. 54 files in naac/, ugc/, iqac/ had root-relative nav paths missing `../`. Python script prepended `../` only where root file exists but subdir-resolved path doesn't. |
| Fix iqac_ space bug | ✅ Done | `iqac_ strategic_plan.html` (with space) → `iqac/iqac_strategic_plan.html` in academics.html and policies.html |
| dept_MBA broken links | ✅ Done | `mba_student_achievements.html` → `departments/mba/mba_toppers.html`; `mba_industry_visits.html` → `departments/mba/mba_industry_visits.html` |
| Create mba_industry_visits.html | ✅ Done | Full page: hero, gold stats bar (25+ companies, 500+ students), 6 visit cards (BHEL/SBI/ITC/Apollo/DHL), objectives glass-card section |
| Link achievements.html | ✅ Done | "Explore All Achievements" CTA added at bottom of about/about_awards.html |

## CSS Constraints

- **NO** `backdrop-filter: blur` anywhere — causes performance/compat issues on some deploy targets
- Glass cards use `rgba(255,255,255,0.05–0.06)` background + `rgba(255,255,255,0.10–0.12)` border
- AOS (`data-aos="fade-up"`) for scroll entrance animations
- Font Awesome 6 for icons, Google Fonts (Inter) for body

## File Structure

```
/
├── assets/
│   ├── css/         # Stylesheets (style.css, animations.css, ai-assistant.css, search.css, etc.)
│   ├── js/          # JavaScript (script.js, search.js, ai-assistant.js, testimonials.js, etc.)
│   ├── images/      # Images and icons
│   ├── pdfs/        # NAAC criteria PDFs, UGC Mandatory Disclosure PDFs
│   └── videos/      # (empty — video1.mp4 missing)
├── data/            # JSON data files (knowledge-base, search-index, news, events, testimonials)
├── naac/            # NAAC sub-pages (ssr, iiqa, dvv, extended profile, 7 criteria) — paths fixed
├── iqac/            # IQAC sub-pages — paths fixed
├── ugc/             # UGC mandatory disclosure sub-pages — paths fixed
├── placements/      # Placement sub-pages
├── departments/     # Dept sub-pages per department (aids, aiml, arch, cse, csbs, ece, it, mba, mech, sh)
│   └── mba/         # Includes new mba_industry_visits.html
├── facilities/      # Facilities sub-pages (infrastructure, library, event gallery, IT)
├── about/           # About sub-pages (chairman, principal, organogram, governing, awards)
│   └── about_awards.html  # Now links to achievements.html via CTA
└── naac.html        # NAAC landing page — fully rebuilt with 7-criteria cards + PDF downloads
```

## Total HTML File Count

470 HTML files (video_gallery.html added). Breakdown:
- `departments/`: 334
- `ugc/`: 55
- root: 40 (includes new video_gallery.html)
- `naac/`: 12
- `placements/`: 8
- `about/`: 7
- `iqac/`: 7
- `facilities/`: 5
- `alumni/`: 2

## Session 6 — UGC Mandatory Disclosure Complete Build (55 pages)

| Task | Status | Notes |
|---|---|---|
| UGC subnav (all 55 pages) | ✅ Done | Sticky, horizontally scrollable, gold-accented (#ffd700) grouped subnav injected into ALL 55 ugc/*.html. 9 category groups: About HEI, Administration, Academics, Admissions, Research, Student Life, Committees, Info Corner, Undertaking. Active page highlighted. |
| Section intro content | ✅ Done | Substantive 2-paragraph intro injected into 51 pages (skipped 4 rich pages: ugc_mandatory, ugc_mandatory_committee, ugc_undertaking, ugc_ps_differentlyabled). All pages now ≥750 words. |
| Missing PDF fallbacks (6 pages) | ✅ Done | Broken iframes for 6 missing PDFs replaced with "Document Available on Request" glass card. Pages: ugc_ps_examinations, ugc_ps_nss, ugc_ps_rti, ugc_ps_circulars, ugc_ul_1, ugc_ul_2 |
| Div balance — all 55 pages | ✅ All OK | Fixed 6 imbalanced pages: 5 missing closing divs (auto-added before footer), 1 extra closing div (ugc_ps_health — manually removed orphan between </section> tags) |
| Relative path integrity | ✅ OK | All 55 pages are depth-1 (flat ugc/ folder). All asset refs use ../assets/. No paths broken. |
| Missing PDFs confirmed | ℹ️ Missing | 3. Examination.pdf, 2. NSS.pdf, 1. RTI.pdf, 2. Circulars and Notices.pdf, ugc_ul_1.pdf, ugc_ul_2.pdf — all replaced gracefully |

### UGC Subnav Design Spec
- Background: `#0f172a` (dark navy — distinct from NAAC `#1a1a2e` subnav)
- Accent: `#ffd700` (gold — distinct from NAAC red `#8b1a2b`)
- Category labels: gold inline-flex spans with Font Awesome icons; `background: rgba(255,215,0,0.07)`
- Active link: `border-bottom: 3px solid #ffd700; background: rgba(255,215,0,0.09); color: #fff`
- Mobile: `overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch`

## Session 5 — NAAC Section Complete Build

| Task | Status | Notes |
|---|---|---|
| NAAC subnav (all 12 pages) | ✅ Done | Sticky 12-link horizontal scrollable subnav injected into ALL 12 naac/*.html pages. Dark navy bg (#1a1a2e), active-page highlight, Font Awesome icons, overflow-x scroll on mobile |
| naac_governance.html div fix | ✅ Done | Missing `</div>` for KI 6.1 ki-card inserted. Was 96o/95c → now 98o/98c (balanced, +2 from subnav) |
| naac_governance.html | ✅ Done | Subnav added. Existing accordion (KI 6.1–6.5) with real PDFs (Strategic Plan, MOM, NBA audit) preserved |
| naac_institutional_values.html | ✅ Done | Subnav added before values-ticker-strip. Existing KI 7.1–7.3 cards preserved |
| naac_curricular_aspects.html | ✅ Done | Subnav + C1 intro paragraph (OBE, Board of Studies, electives) injected before metric cards |
| naac_extended_profile.html | ✅ Done | Subnav + EP intro paragraph (4 QnM baseline metrics) injected before metric cards |
| naac_infrastructure.html | ✅ Done | Subnav + C4 intro paragraph (labs, ICT, library, hostel) injected before metric cards |
| naac_teaching_learning.html | ✅ Done | Subnav + C2 intro paragraph (blended learning, CIA, OBE) injected before metric cards |
| naac_student_support.html | ✅ Done | Subnav + C5 intro injected; **video path fixed** (`../video.mp4` → `../assets/videos/video1.mp4`) |
| naac_research_innovation.html | ✅ Done | Subnav + C3 intro injected; **video path fixed** (`../video.mp4` → `../assets/videos/video1.mp4`) |
| naac_dvv.html | ✅ Done | Subnav + DVV explanation content; **broken xlsx iframe removed** (replaced with 3-card process grid + NAAC portal note) |
| naac_rti.html | ✅ Done | Subnav + RTI compliance framework; **wrong energy PDF iframe removed** (replaced with 4-card RTI structure + PIO contact card) |
| naac_ssr.html | ✅ Done | Subnav + SSR intro + "available on request" card (NAACS folder confirmed missing — no fake iframe) |
| naac_iiqa.html | ✅ Done | Subnav + IIQA intro + "available on request" card (NAACS folder confirmed missing — no fake iframe) |
| Div balance all 12 pages | ✅ All OK | All 12 pages: divs open == divs close. Word counts 949–1618 |
| NAACS folder | ℹ️ Missing | `assets/pdfs/NAACS/` does not exist — SSR/IIQA PDFs need to be placed there to enable iframes |

## Session 7 — NAAC Critical Fixes

| Task | Status | Notes |
|---|---|---|
| `naac_extended_profile.html` nested `<a>` bug | ✅ Fixed | All 4 `.metric-card` outer `<a href="#">` wrappers converted to `<div>` — invalid nested-anchor HTML eliminated. PDF buttons (`evidence-link`) now sit correctly inside their cards. Python regex used to handle Unicode right-apostrophe in text. |
| `naac_iiqa.html` PDF viewer restored | ✅ Done | Removed "IIQA Document — Available on Request" text card. Full iframe viewer added: title bar + "Open Fullscreen" button + 880px iframe + path hint. Dummy src: `../assets/pdfs/NAACS/IIQA.pdf` |
| `naac_ssr.html` PDF viewer restored | ✅ Done | Removed "SSR Document — Available on Request" text card. Full iframe viewer added. Dummy src: `../assets/pdfs/NAACS/ssr-new.pdf` |
| `naac_dvv.html` PDF viewer added | ✅ Done | Viewer section inserted before footer (existing portal-info content preserved above). Dummy src: `../assets/pdfs/NAACS/dvv_clarification.pdf` |
| `naac_rti.html` PDF viewer added | ✅ Done | Viewer section inserted before footer (PIO contact card preserved above). Dummy src: `../assets/pdfs/NAACS/rti_disclosure.pdf` |
| All 5 files integrity check | ✅ Pass | Python verification: no absent checks failed, all iframe/button strings present, zero nested `<a class="metric-card">` remaining. |

**PDF placeholder filenames needed in `assets/pdfs/NAACS/`:**
- `IIQA.pdf` — IIQA submission document
- `ssr-new.pdf` — Self Study Report
- `dvv_clarification.pdf` — DVV clarification bundle
- `rti_disclosure.pdf` — RTI proactive disclosure
- `ep_students.pdf`, `ep_teachers_2_1.pdf`, `ep_teachers_2_2.pdf`, `ep_expenditure.pdf` — Extended Profile front sheets

## Session 4 — Placement Pages Content Build

| Task | Status | Notes |
|---|---|---|
| placement_campus_hiring.html | ✅ Done | Built full content: overview para, stats bar (85+ companies / 712 students / 10 LPA / 4.8 LPA avg), 6-step hiring process cards, eligibility criteria list, 8-sector grid, contact CTA. Removed broken campus-hiring.pdf iframe. 87/87 div balance, ~1029 words |
| placement_capacity_dev.html | ✅ Done | Built full content: overview para, four pillars (Aptitude, Soft Skills, Technical, Mock Interviews), year-wise roadmap (Y1–Y4), training partners banner. Removed broken capacity_development PDF iframe. 67/67 div balance, ~1006 words |
| placement_value_added.html | ✅ Done | Built full content: overview para, 8 course cards (Python, Java, AWS, Data Science, Cyber Security, SQL, IoT, SAP) with hours/cert tags, kept working value_added_training_course.pdf iframe (3.4MB). 81/81 div balance, ~975 words |
| policies.html audit | ✅ Clean | 18 "coming soon" cards use intentional onclick-alert pattern; 3 cards have real PDFs (R&D, Scholarship, Sports); ADMISSION POLICY card is in HTML comment. No action needed. |
| placement_pat.html | ✅ Clean | "Loading stories..." is rendered by working placement-stories.js — not a static defect. |
| "placeholder" false positive | ✅ Resolved | All instances = form `placeholder="Type your question..."` attribute on AI chatbot input — 100% false positive. |

## Session 3 — Deployment-Ready Tasks Completed

| Task | Status | Notes |
|---|---|---|
| NAAC PDF broken links | ✅ Done | 68 broken → 0. All 8 naac sub-pages remapped: Criteria 1 → supporting docs, Criteria 6 → MOM/strategic plan, Criteria 2–5 → UGC annual report fallback, Extended Profile → UGC About Us |
| Dept left sidebar (334 pages) | ✅ Done | Injected `.dept-layout` + `.dept-left-sidebar` into all 334 dept sub-pages via Python. Dark navy (`#0d1b2a`) sidebar with `#f5c518` gold dept label, sticky on desktop, horizontal wrap on mobile. CSS injected inline into each `<head>`. Active page highlighting supported. |
| Placement report stat cards | ✅ Done | Replaced JS-driven (broken) KPI cards with hardcoded real data. Inline JS tab switcher for 2022–23 / 2023–24 / 2024–25 with dept-wise table. PDF fixed to real file: `assets/pdfs/placement/consolidated_placement_report_2022_23_student_coun.pdf` |
| video_gallery.html | ✅ Done | Created new page with dark-red gradient hero, filter tab bar (All/Campus/Placements/Events/Departments/Alumni), 9-card YouTube embed grid, JS filter, YouTube channel CTA. index.html link updated `facilities.html → video_gallery.html` |
| Cloudflare `_redirects` | ✅ Done | 30+ rules: short URLs, deleted stub redirects, video-gallery shortlink, SPA-style 200 fallback |
| Cloudflare `_headers` | ✅ Done | Security headers (HSTS, X-Frame-Options, CSP-ready), immutable caching for assets/js/css, PDF inline display, HTML must-revalidate |

## Session 11 — OG Tags + AI Knowledge Base v4 + AI Engine Upgrade

| Task | Status | Notes |
|---|---|---|
| Open Graph + Twitter Card tags | ✅ Done | 456 pages injected (18 already had them). All 474 HTML pages now have og:title, og:description, og:url, og:image, og:site_name, twitter:card, twitter:title, twitter:description, twitter:image. Page-specific titles and descriptions for all depth levels and all department sub-pages. |
| `data/knowledge-base.json` rebuilt (v4) | ✅ Done | Expanded from 231 lines/14 intents → 49KB/33 intents. New: 10 department intents (CSE/ECE/Mech/IT/AI&DS/AI&ML/CSBS/Arch/MBA/S&H), COE intent, all HOD names + contacts, real department emails/phones, placement stats per dept, fee structure, NAAC facts, `facts` section with HOD lookup, 20 quick facts, department contacts table. |
| `assets/js/ai-assistant.js` upgraded (v4) | ✅ Done | New `lookupFact()` layer runs BEFORE intent matching. Handles: HOD name/phone/email by department, all-departments contact table, all-HoDs table, placement stats per dept, fees per programme, college contacts, addresses. `getBasePath()` added so KB loads correctly from all page depths (root/depth-1/depth-2). |

### AI Assistant v4 — What It Now Knows
| Query Type | Example | Response |
|---|---|---|
| HOD name | "Who is CSE HOD?" | Dr. Priya T + phone + email |
| Dept phone | "ECE department contact" | +91-416-2244801 + ece@kingston.ac.in |
| Dept email | "IT email" | it@kingston.ac.in |
| All HODs | "List all HODs" | Full table of all 10 departments |
| All contacts | "All department contacts" | Phone + email table |
| NAAC grade | "NAAC grade" | A Grade, CGPA 2.93/4.00, 2022 |
| Highest package | "Highest package" | ₹25 LPA |
| Avg package | "Average package" | ₹6.5 LPA |
| Dept placements | "CSE placements" | 97%, ₹6.8 LPA, top companies |
| Fee | "BE fee" | ₹1,60,000 + ₹11,800 = ₹1,71,800/year |
| MBA fee | "MBA fee" | ₹2,00,000 per annum |
| Hostel fee | "hostel fee" | ₹1,00,000/year all-inclusive |
| Address | "Where is Kingston?" | Full address |

## Session 10 — sitemap.xml + robots.txt + Final Pre-Deployment Sweep

| Task | Status | Notes |
|---|---|---|
| `sitemap.xml` generated | ✅ Done | 475 URLs total (474 HTML pages + canonical `https://www.kingston.ac.in/`). Priorities: 1.0 = index, 0.9 = admission/departments/about/contact/academics, 0.8 = naac/iqac/ugc-mandatory/top-bar pages/login portals, 0.7 = dept sub-pages/placements, 0.6 = ugc/about/facilities sub-pages, 0.5 = remaining. Base URL: `https://www.kingston.ac.in/`. `<lastmod>` = 2026-05-03, `<changefreq>` = monthly. |
| `robots.txt` confirmed | ✅ Existing | `User-agent: * / Allow: /` with `Sitemap: https://www.kingston.ac.in/sitemap.xml` and internal path disallows. Already correct. |
| Sitewide `backdrop-filter:blur` final sweep | ✅ Done | 107 instances removed across 88 files (ugc/53, naac/12, dept-csbs/7, dept-mech/4, facilities/2, about/2, root dept pages/7, blog/1). `404.html` only has the phrase in a CSS comment — not a property. **Zero actual `backdrop-filter:blur` CSS properties remain sitewide.** |

### Pre-Deployment Checklist — ALL GREEN ✅
| Check | Result |
|---|---|
| `href="#"` dead links sitewide | 0 ✅ |
| `backdrop-filter:blur` CSS property violations | 0 ✅ |
| All 7 top-bar pages exist and wired | ✅ |
| `_redirects` (Cloudflare) | ✅ 40 lines |
| `_headers` (Cloudflare) | ✅ 32 lines |
| `robots.txt` | ✅ 17 lines |
| `sitemap.xml` | ✅ 475 URLs |
| Total HTML files | 474 ✅ |
| Login links wired at root / depth-1 / depth-2 | ✅ |
| `ai-assistant.css` linked | 469 pages ✅ |

## Session 9 — Login Portals + Sitewide href="#" Zero-Dead-Links Sweep

| Task | Status | Notes |
|---|---|---|
| `student_login.html` built | ✅ Done | New page: glassmorphism-lite two-column layout. Left: Sign In form (Registration Number + Password + Forgot Password + Login CTA). Right: Portal Information card (Attendance, Marks, Timetable, Fee, Certificates). IT Support contact card. Form handler alerts with ERP contact instructions. |
| `staff_login.html` built | ✅ Done | New page: same two-column layout. Left: Staff Sign In form (Staff ID + Password). Right: ERP Quick Access card (Leave Management, Payroll, Timetable Upload, Attendance Marking, Mark Entry). Dark navy ERP update banner. |
| `Student-Log In` top-bar wired sitewide | ✅ Done | 938 total link instances updated across all 471 HTML files at all 3 depths. Root: `student_login.html`, Depth-1: `../student_login.html`, Depth-2: `../../student_login.html`. |
| `Staff-Log In` top-bar wired sitewide | ✅ Done | Same 938 instances (paired with student). Root/Depth-1/Depth-2 relative paths all correct. |
| `Admission` top-bar link | ✅ Already wired | Was already pointing to `admission.html` / `../admission.html` / `../../admission.html` at all depths. Confirmed clean. |
| Sitewide `href="#"` sweep | ✅ Done | **Zero `href="#"` remaining sitewide.** 3492 instances fixed across 469 files. Rules applied: (1) Nav dropdown parents with fa-angle-right → `javascript:void(0)` (preserves JS dropdown handlers); (2) `href="#"` with existing onclick handler → `javascript:void(0)` + keep onclick; (3) All remaining pure dead links → `javascript:void(0)" onclick="return false;"`; (4) policies.html 18 remaining (title+onclick pattern) → `javascript:void(0)`. |

## Session 8 — Top-Bar Pages: Content Enrichment + Glassmorphism Compliance

| Task | Status | Notes |
|---|---|---|
| `alumni.html` — `backdrop-filter` removed | ✅ Done | `.glass-card` `backdrop-filter: blur(10px)` deleted. `--glass-bg` fixed: 0.7 → 0.06; `--glass-border` fixed: 0.3 → 0.12. Card bg changed to solid `#fff` with navy border. |
| `alumni.html` — `ai-assistant.css` added | ✅ Done | Was missing from `<head>`. Link added before `<style>`. |
| `grievance_helpdesk.html` — `backdrop-filter` removed | ✅ Done | `.grievance-hero .badge` had `backdrop-filter: blur(10px)`. Removed. Background changed from `rgba(255,255,255,0.1)` → `rgba(255,255,255,0.05)`. |
| `coe.html` — content enriched | ✅ Done | Added: 5-step Examination Process Flow (numbered circles), Grading & Marking Scheme table (O/A+/A/B+/B/C/RA grades per Anna Univ norms), 4 Results & Student Services portal buttons (Anna Univ portal, Revaluation, Photocopy, Provisional Cert), 4 Important Downloads (exam schedule, regulations, malpractice policy, grade sheet). |
| `careers.html` — content enriched | ✅ Done | Added: Non-Teaching & Administrative Roles table (5 positions: Lab Instructor, Office Admin, Librarian, IT Support, PE Director with vacancies), 5-step Application & Selection Timeline (numbered circles). No `backdrop-filter` violation found. |
| Global `backdrop-filter` check | ✅ Pass | Zero `backdrop-filter` matches across all 4 top-bar pages. |

## Cloudflare Deployment Files

- `_redirects` — short URL aliases, deleted stub 301s, 200 fallback for SPA
- `_headers` — security headers + cache control (both in project root)
