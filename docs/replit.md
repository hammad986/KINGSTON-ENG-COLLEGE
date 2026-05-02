# Kingston Engineering College Website

## Overview
A comprehensive multi-page static website for Kingston Engineering College (an autonomous institution in Tamil Nadu, India). The site serves as a digital portal covering departments, admissions, facilities, placements, and regulatory compliance (NAAC, IQAC, UGC).

## Architecture
- **Type**: Pure static HTML website (no build step required)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **External Libraries**: Font Awesome, Swiper CSS, AOS — all loaded via CDN
- **Data**: JSON files in `/data/` used by the local AI Assistant
- **Tooling**: Python scripts for content generation and maintenance (not part of the served site)

## Project Structure
- `/` — 100+ HTML pages (index.html is the homepage)
- `/assets/css/` — Global styles and animations
- `/assets/js/` — JavaScript including the AI assistant logic
- `/assets/images/` — Categorized image assets
- `/assets/pdfs/` — Documents for admissions, policies, etc.
- `/components/` — Reusable HTML fragments
- `/data/` — JSON data files (knowledge-base.json for AI assistant)
- `/departments/` — Department-specific pages
- `/pages/` — Secondary organized pages

## Running the Project
The site is served with Python's built-in HTTP server:
```
python3 -m http.server 5000 --bind 0.0.0.0
```
Workflow: "Start application" on port 5000 (webview)

## Deployment
Configured as a **static** deployment with `publicDir: "."` (root directory).

## Features Added
### Site-Wide Search (`assets/js/search.js`, `data/search-index.json`, `assets/css/search.css`)
- Fuzzy search over 140+ pages with weighted ranking (title×3/keyword×2/desc×1)
- 300ms debounce, overlay UI, keyboard navigation, 7 results max
- Search button injected into navbar via `script.js` — no HTML changes needed

### AI Chatbot (`assets/js/ai-assistant.js`, `data/knowledge-base.json`, `assets/css/ai-assistant.css`)
- 22 intents covering all major college topics with English/Hindi/Hinglish support
- Weighted scoring, context memory, typing indicator, search fallback cards
- Follow-up suggestion chips after every response
- Chat persistence in localStorage with "Clear chat" button
- Full-page interface at `ai-assistant.html`; floating widget on other pages

### News System (`assets/js/news.js`, `data/news.json`)
- `data/news.json` — 12 rich news items with category, featured, tags, fallback images
- `assets/js/news.js` — fetches JSON and powers both homepage slider and blog page
- `blog.html` — full News & Announcements page with:
  - Category filter tabs (All, Research, Achievement, Event, Placement, etc.)
  - Live search/filter
  - News cards with featured badge, category badges, tags, hover animations
- Homepage slider updated to load real news data with category badges and dates
- Place real images in `assets/images/news/news1.jpg` through `news12.jpg`

## Upgrade Progress
### Phase 1 — Critical Fixes (COMPLETE)
- Email typo fixed across 50 files
- 7 new department pages created
- 7 missing image references fixed
- Forms overhauled with EmailJS integration (`assets/js/form-handler.js`)

### Phase 2 — Content Integration (IN PROGRESS)
- **Homepage (index.html)**: College name corrected, TNEA code updated to 1520, new "Why Choose Kingston" stats section, new "About Kingston" section, footer links fixed, explore campus links fixed, social media links added
- **COE page (coe.html)**: New page created with examination office details
- **Pay Online page (pay_online.html)**: Demo payment form with client-side validation
- **Social media links**: YouTube (UCXc_SY1bMEp6XrcoY9yoodw), Facebook (KingstonEngineeringCollege), Instagram (kaboraofficial), Twitter (KingstonEngClg)
- **About section pages**: Footer links, social media, copyright year, topbar links all updated across 8 pages
- **Knowledge base**: Address corrected to "Chittoor Main Road, Vellore, Tamil Nadu – 632 059"

### Key Content Facts
- **TNEA Code**: 1520
- **College Name**: Kingston Engineering College (Autonomous)
- **Trust**: M/S. Duraimurugan Educational Trust
- **Chairman**: Thiru.D.M. KATHIR ANAND M.B.A (USA)
- **Principal**: Dr.U.V.Arivazhagu M.E.,Ph.D
- **Address**: Chittoor Main Road, Vellore, Tamil Nadu – 632 059
- **Campus**: 11.62 acres, 5km from Katpadi Railway Station
- **Established**: 2001
