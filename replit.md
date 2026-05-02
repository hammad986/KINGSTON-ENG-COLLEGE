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

## File Structure

```
/
├── assets/
│   ├── css/         # Stylesheets (style.css, animations.css, ai-assistant.css, etc.)
│   ├── js/          # JavaScript files
│   ├── images/      # Images and icons
│   └── videos/      # (empty — video1.mp4 missing)
├── data/            # JSON data files (knowledge-base, search-index, news, events, etc.)
├── docs/            # Document files
├── naac/            # NAAC related pages
├── iqac/            # IQAC related pages
├── ugc/             # UGC related pages
├── placements/      # Placement sub-pages
├── departments/     # Department sub-pages
├── facilities/      # Facility sub-pages
└── scripts/         # Utility/sync Python scripts
```
