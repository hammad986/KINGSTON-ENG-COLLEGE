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
| `academics.html` | Academics information |
| `departments.html` | Departments listing |
| `placements.html` | Placement information |
| `naac.html` | NAAC accreditation |
| `facilities.html` | Campus facilities |
| `contact.html` | Contact & directions |

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
| Fix dept nav links | ✅ Done | dept_AI&DS.html → dept_aids.html (999 fixes), dept_mechanical → dept_mech, dept_civil/eee → departments |
| Fix broken href="#" links | ✅ Done | about.html:460 → academics.html; index.html:918 → news.html |
| Fix forms (action/method) | ✅ Done | contact, admission_enquiry, apply_now all have action/method + JS handlers in script.js |
| Link NAAC/UGC PDFs | ✅ Done | naac.html rebuilt with direct PDF download links; ugc_ps_idp.html already had IDP PDF |
| Standardize header/footer | ✅ Done | sitemap.html & privacy_policy.html now have full font/library/CSS links |
| Ensure search on all pages | ✅ Done | search.js auto-injects into any page with .main-nav .container (all pages) |
| Campus tour redesign (VIT-style) | ✅ Done | Added VIT-style 6-panel photo walk grid above map section |
| Gallery dummy photos (16 Picsum) | ✅ Done | Event gallery expanded from 4 → 16 photos with year filter JS; campus tour gallery 6 → 9 photos |
| Testimonials UI | ✅ Done | Already premium-quality CSS; filter/search working via testimonials.js |
| Dept sub-pages carousels | ✅ Done | Dept sub-pages have hero swiper carousel (confirmed in cse_about.html, aids_about.html) |
| Verify sitemap/privacy_policy | ✅ Done | Both pages now have full font/library/CSS standardization |

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
├── naac/            # NAAC sub-pages (ssr, iiqa, dvv, extended profile, 7 criteria)
├── iqac/            # IQAC sub-pages
├── ugc/             # UGC mandatory disclosure sub-pages
├── placements/      # Placement sub-pages
├── departments/     # Dept sub-pages (cse, aids, aiml, ece, it, mech, mba, arch, sh)
├── facilities/      # Facilities sub-pages (infrastructure, library, event gallery, IT)
├── about/           # About sub-pages (chairman, principal, organogram, governing, etc.)
└── naac.html        # NAAC landing page — fully rebuilt with 7-criteria cards + PDF downloads
```
