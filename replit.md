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

## Cloudflare Deployment Files

- `_redirects` — short URL aliases, deleted stub 301s, 200 fallback for SPA
- `_headers` — security headers + cache control (both in project root)
