/**
 * Kingston Engineering College – AI Assistant v3
 * Features: weighted scoring, context memory, search fallback,
 * typing indicator, Hindi/Hinglish support, follow-up suggestions,
 * improved fallback cards, chat persistence (localStorage)
 */

class AIAssistant {
    constructor() {
        this.knowledgeBase = null;
        this.searchIndex = null;
        this.intentMemory = [];
        this.MAX_MEMORY = 3;
        this.STORAGE_KEY_FP = 'kec_chat_fullpage';
        this.STORAGE_KEY_WG = 'kec_chat_widget';
        this.MAX_STORED = 60; // max message objects in localStorage

        /* ── Per-intent follow-up suggestions ────────────────── */
        this.followUps = {
            greeting:        [{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '💰 Fees', q: 'What is the fee structure?' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            admission:       [{ text: '💰 Fee Structure', q: 'What is the fee structure?' }, { text: '🏆 Scholarships', q: 'Tell me about scholarships' }, { text: '📞 Contact Admission', q: 'How to contact Kingston?' }],
            fees:            [{ text: '🏆 Scholarships', q: 'Tell me about scholarships' }, { text: '📋 Admission Process', q: 'Tell me about admissions' }, { text: '💳 Pay Online', q: '' }],
            placement:       [{ text: '💼 Internships', q: 'Tell me about internships' }, { text: '🏭 Industry Connect', q: 'Tell me about industry connect' }, { text: '🎓 Higher Education', q: 'Tell me about higher education' }],
            contact:         [{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '🗺️ Campus Tour', q: 'Tell me about campus tour' }],
            departments:     [{ text: '💻 CSE Details', q: 'Tell me about CSE department' }, { text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            hostel:          [{ text: '🚌 Transport', q: 'Tell me about transport and bus routes' }, { text: '🏫 Facilities', q: 'What facilities are available?' }, { text: '💰 Hostel Fees', q: 'What is the fee structure?' }],
            scholarship:     [{ text: '📋 Admission Process', q: 'Tell me about admissions' }, { text: '💰 Fee Structure', q: 'What is the fee structure?' }],
            naac:            [{ text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }, { text: '⭐ IQAC', q: 'Tell me about IQAC' }],
            facilities:      [{ text: '📚 Library', q: 'Tell me about library' }, { text: '⚽ Sports', q: 'Tell me about sports' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            library:         [{ text: '🏫 Other Facilities', q: 'What facilities are available?' }, { text: '🔬 Research', q: 'Tell me about research at Kingston' }],
            sports:          [{ text: '🎭 Clubs', q: 'Tell me about clubs and activities' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            transport:       [{ text: '📞 Contact Us', q: 'How to contact Kingston?' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            clubs:           [{ text: '🔬 Research', q: 'Tell me about research at Kingston' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            research:        [{ text: '🏛️ Departments', q: 'What departments are available?' }, { text: '🎓 Higher Education', q: 'Tell me about higher education' }],
            cse:             [{ text: '📊 CSE Placements', q: 'Tell me about CSE placements' }, { text: '👥 CSE Faculty', q: 'Tell me about CSE faculty' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            alumni:          [{ text: '📊 Placements', q: 'Tell me about placements' }, { text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }],
            higher_education:[{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            internship:      [{ text: '📊 Placements', q: 'Tell me about placements' }, { text: '💼 Industry Connect', q: 'Tell me about industry connect' }],
            iqac:            [{ text: '🏅 NAAC', q: 'Tell me about NAAC accreditation' }, { text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }],
            about:           [{ text: '🏛️ Departments', q: 'What departments are available?' }, { text: '🗺️ Campus Tour', q: 'Tell me about campus tour' }, { text: '📋 Admissions', q: 'Tell me about admissions' }],
            thanks:          [{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            goodbye:         [],
        };

        this.init();
    }

    /* ── Bootstrap ───────────────────────────────────────────── */
    async init() {
        try {
            await Promise.all([
                this.loadKnowledgeBase(),
                this.loadSearchIndex()
            ]);
            this.attachEventListeners();
            this.bindGlobalButtons(); // Bind chatbot buttons on all pages
            this.restoreOrWelcome();
            this.autoFocusInput();
        } catch (e) {
            console.error('[KingstonAI] Init error:', e);
        }
    }

    /* ── Global Button Binding (for all pages) ──────────────────── */
    bindGlobalButtons() {
        try {
            // Bind AI toggle buttons (primary selector is ai-widget-toggle class)
            const toggleBtns = document.querySelectorAll('.ai-widget-toggle');
            console.log('[KingstonAI] Found', toggleBtns.length, 'toggle buttons');
            toggleBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    console.log('[KingstonAI] Button clicked!');
                    const widget = document.getElementById('ai-widget-container');
                    if (widget) {
                        widget.classList.toggle('active');
                        console.log('[KingstonAI] Widget toggled. Active:', widget.classList.contains('active'));
                    } else {
                        console.error('[KingstonAI] Widget container not found!');
                    }
                });
            });
        } catch (e) {
            console.warn('[KingstonAI] Button binding error:', e);
        }
    }

    async loadKnowledgeBase() {
        try {
            const res = await fetch('data/knowledge-base.json');
            this.knowledgeBase = await res.json();
        } catch (e) {
            console.warn('[KingstonAI] Failed to load knowledge base.', e);
        }
    }

    async loadSearchIndex() {
        try {
            const res = await fetch('data/search-index.json');
            this.searchIndex = await res.json();
        } catch (e) {
            console.warn('[KingstonAI] Failed to load search index.', e);
        }
    }

    /* ── Event listeners ─────────────────────────────────────── */
    attachEventListeners() {
        const sendBtns = [
            document.getElementById('fullpage-send'),
            document.getElementById('ai-send-btn')
        ];
        const inputs = [
            document.getElementById('fullpage-input'),
            document.getElementById('ai-input')
        ];

        sendBtns.forEach(btn => {
            if (!btn) return;
            btn.addEventListener('click', () => {
                const type = btn.id.includes('fullpage') ? 'fullpage' : 'widget';
                this.handleSendMessage(type);
            });
        });

        inputs.forEach(input => {
            if (!input) return;
            input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    const type = input.id.includes('fullpage') ? 'fullpage' : 'widget';
                    this.handleSendMessage(type);
                }
            });
        });

        // Quick action buttons (static)
        document.querySelectorAll('.ai-quick-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const query = btn.getAttribute('data-query');
                if (query) {
                    this.setInput(query);
                    this.handleSendMessage('fullpage');
                }
            });
        });

        // Close button handler (toggle binding is handled by bindGlobalButtons)
        const widget = document.getElementById('ai-widget-container');
        const close = document.getElementById('ai-widget-close');

        if (close && widget) {
            close.addEventListener('click', () => widget.classList.remove('active'));
        }

        // Auto-focus input when widget opens
        if (widget) {
            widget.addEventListener('click', (e) => {
                if (widget.classList.contains('active') && e.target.id === 'ai-input') {
                    e.target.focus();
                }
            });
        }

        // Clear chat button (fullpage only)
        const clearBtn = document.getElementById('ai-clear-chat');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => this.clearChat('fullpage'));
        }
    }

    autoFocusInput() {
        setTimeout(() => {
            const input = document.getElementById('fullpage-input') || document.getElementById('ai-input');
            if (input) input.focus();
        }, 500);
    }

    setInput(text) {
        const input = document.getElementById('fullpage-input') || document.getElementById('ai-input');
        if (input) { input.value = text; input.focus(); }
    }

    /* ── Chat Persistence ────────────────────────────────────── */
    storageKey(type) {
        return type === 'fullpage' ? this.STORAGE_KEY_FP : this.STORAGE_KEY_WG;
    }

    saveMessage(html, sender, type) {
        try {
            const key = this.storageKey(type);
            const history = JSON.parse(localStorage.getItem(key) || '[]');
            history.push({ html, sender, ts: Date.now() });
            // Keep only the last MAX_STORED messages
            if (history.length > this.MAX_STORED) history.splice(0, history.length - this.MAX_STORED);
            localStorage.setItem(key, JSON.stringify(history));
        } catch (e) { /* storage full or private mode */ }
    }

    restoreHistory(type) {
        try {
            const key = this.storageKey(type);
            const history = JSON.parse(localStorage.getItem(key) || '[]');
            if (!history.length) return false;

            history.forEach(({ html, sender }) => {
                this.displayMessage(html, sender, false, type, false); // no save again
            });
            return true;
        } catch (e) { return false; }
    }

    clearChat(type) {
        try { localStorage.removeItem(this.storageKey(type)); } catch (e) {}
        const containerId = type === 'fullpage' ? 'fullpage-messages' : 'ai-messages';
        const container = document.getElementById(containerId);
        if (container) container.innerHTML = '';
        // Re-show welcome
        const intent = this.getIntentById('greeting');
        if (intent) this.renderResponse(intent, false, type);
        else this.displayMessage("👋 Welcome back! How can I help you?", 'bot', false, type);
    }

    restoreOrWelcome() {
        const fpRestored = this.restoreHistory('fullpage');
        const wgRestored = this.restoreHistory('widget');

        if (!fpRestored) {
            const intent = this.getIntentById('greeting');
            if (intent) this.renderResponse(intent, false, 'fullpage');
            else this.displayMessage("👋 Welcome to Kingston! How can I help you today?", 'bot', false, 'fullpage');
        }
        if (!wgRestored) {
            const intent = this.getIntentById('greeting');
            if (intent) this.renderResponse(intent, false, 'widget');
            else this.displayMessage("👋 Welcome to Kingston! How can I help you today?", 'bot', false, 'widget');
        }
    }

    /* ── Message flow ────────────────────────────────────────── */
    handleSendMessage(type = 'fullpage') {
        const inputId = type === 'fullpage' ? 'fullpage-input' : 'ai-input';
        const input = document.getElementById(inputId);
        if (!input) return;

        const userMessage = input.value.trim();
        if (!userMessage) return;

        input.value = '';
        this.displayMessage(userMessage, 'user', true, type);
        this.showTypingIndicator(type);

        setTimeout(() => {
            this.hideTypingIndicator(type);
            this.processUserMessage(userMessage, type);
        }, 350 + Math.random() * 200);
    }

    processUserMessage(message, type) {
        const normalized = this.normalize(message);

        const contextResponse = this.handleContextualFollowUp(normalized);
        if (contextResponse) {
            this.recordMemory(contextResponse.id);
            this.renderResponse(contextResponse, true, type);
            return;
        }

        const intent = this.detectIntent(normalized);
        if (intent) {
            this.recordMemory(intent.id);
            this.renderResponse(intent, true, type);
        } else {
            this.renderSearchFallback(normalized, type);
        }
    }

    /* ── Normalise input ─────────────────────────────────────── */
    normalize(text) {
        return text
            .toLowerCase()
            // Hinglish / mixed-language common patterns → English equivalents
            .replace(/\bkya hai\b/g, 'what is')
            .replace(/\bkaise\b/g, 'how')
            .replace(/\bkahan\b/g, 'where')
            .replace(/\bkitna\b/g, 'how much')
            .replace(/\bpadhna\b|\bpadvna\b/g, 'study')
            .replace(/\bpadhai\b/g, 'education')
            .replace(/\bbatao\b|\bbataiye\b/g, 'tell me')
            .replace(/\bchahiye\b|\bchahie\b/g, 'need')
            .replace(/\bkaro\b|\bkarna\b/g, 'do')
            .replace(/\bhaan\b|\bha\b/g, 'yes')
            .replace(/\bnahi\b|\bnahin\b/g, 'no')
            .replace(/\btheek hai\b|\bthik hai\b/g, 'ok')
            .replace(/\baplly\b/g, 'apply')   // common typo
            .replace(/\bplacment\b/g, 'placement') // typo
            .replace(/\bfaculity\b/g, 'faculty')   // typo
            .replace(/[?!,।]/g, '')
            .replace(/\s+/g, ' ')
            .trim();
    }

    /* ── Weighted Intent Detection ───────────────────────────── */
    detectIntent(message) {
        if (!this.knowledgeBase?.intents) return null;

        const scores = this.knowledgeBase.intents.map(intent => ({
            intent,
            score: this.scoreIntent(intent, message)
        }));

        // Sort by score (descending)
        scores.sort((a, b) => b.score - a.score);

        // Only return if score > 0
        if (scores[0].score === 0) {
            return this.getIntentById('not_found') || null;
        }
        
        return scores[0].intent;
    }

    scoreIntent(intent, message) {
        try {
            let total = 0;
            if (!intent || typeof intent !== 'object') return 0;
            
            const keywords = Array.isArray(intent.keywords) ? intent.keywords : [];
            if (keywords.length === 0) return 0;

            for (const kw of keywords) {
                if (typeof kw !== 'string') continue;
                
                const k = kw.toLowerCase();
                const msgWords = message.split(/\s+/).filter(Boolean);
                const kwWords = k.split(/\s+/).filter(Boolean);

                if (!k || !message) continue;

                // Exact full match
                if (message === k) {
                    total += 100;
                    continue;
                }

                // Full keyword appears as substring
                if (message.includes(k)) {
                    total += 60 + (k.length * 2);
                    continue;
                }

                // All words in keyword appear in message
                if (kwWords.length > 0 && kwWords.every(w => message.includes(w))) {
                    total += 50;
                    continue;
                }

                // Individual keyword word matches
                for (const kwWord of kwWords) {
                    if (kwWord && msgWords.includes(kwWord)) {
                        total += 30;
                    }
                }

                // Partial match (80% of keyword)
                if (k.length >= 4) {
                    const partial = k.slice(0, Math.ceil(k.length * 0.8));
                    if (message.includes(partial)) {
                        total += 15;
                    }
                }
            }

            return Math.max(0, total);
        } catch (e) {
            console.warn('[KingstonAI] scoreIntent error:', e);
            return 0;
        }
    }

    /* ── Context memory ──────────────────────────────────────── */
    recordMemory(intentId) {
        this.intentMemory.push(intentId);
        if (this.intentMemory.length > this.MAX_MEMORY) this.intentMemory.shift();
    }

    handleContextualFollowUp(message) {
        const acks = ['yes', 'ok', 'okay', 'sure', 'go ahead', 'please', 'haan', 'theek hai', 'ha', 'tell me more'];
        if (!acks.includes(message)) return null;

        const last = this.intentMemory[this.intentMemory.length - 1];
        if (!last) return null;

        const followUp = {
            'admission': 'fees', 'fees': 'scholarship', 'placement': 'internship',
            'departments': 'cse', 'cse': 'placement', 'hostel': 'transport',
            'about': 'facilities'
        };
        const nextId = followUp[last];
        return nextId ? this.getIntentById(nextId) : null;
    }

    /* ── Search Fallback ─────────────────────────────────────── */
    renderSearchFallback(query, type) {
        const fallback = this.knowledgeBase?.fallback;
        const results = this.searchPages(query, 4);

        const fallbackMessages = [
            "Hmm, I couldn't find an exact match — but here are some relevant pages:",
            "Good question! I'm still learning, but these pages might have what you need:",
            "Let me help you find the right information:",
            "I may not have a direct answer, but here's what might help:"
        ];
        const msg = fallbackMessages[Math.floor(Math.random() * fallbackMessages.length)];
        let html = `<p style="margin:0 0 10px 0;">${msg}</p>`;

        if (results.length > 0) {
            html += `<div class="ai-result-cards">`;
            results.forEach(r => {
                const cat = r.category || 'General';
                html += `
                <a href="${r.url}" class="ai-result-card">
                    <div class="ai-result-card-inner">
                        <div class="ai-result-card-title">${r.title}</div>
                        <div class="ai-result-card-desc">${r.description}</div>
                    </div>
                    <div class="ai-result-card-cat">${cat}</div>
                </a>`;
            });
            html += `</div>`;
        }

        if (fallback?.suggestions) {
            html += `<div class="ai-actions" style="margin-top:12px;">`;
            fallback.suggestions.forEach(sug => {
                html += `<button class="ai-btn outline" onclick="window.KingstonAI.setInput('${sug.query}'); window.KingstonAI.handleSendMessage('${type}');">${sug.text}</button>`;
            });
            html += `</div>`;
        }

        this.displayMessage(html, 'bot', true, type);
    }

    searchPages(query, limit = 4) {
        if (!this.searchIndex) return [];
        const q = query.toLowerCase();
        const words = q.split(/\s+/).filter(Boolean);

        const scored = this.searchIndex.map(entry => {
            let score = 0;
            const title = (entry.title || '').toLowerCase();
            const desc = (entry.description || '').toLowerCase();
            const kws = (entry.keywords || []).join(' ').toLowerCase();

            if (title.includes(q)) score += 60;
            if (kws.includes(q)) score += 40;
            if (desc.includes(q)) score += 20;
            words.forEach(w => {
                if (title.includes(w)) score += 10;
                if (kws.includes(w)) score += 7;
                if (desc.includes(w)) score += 3;
            });
            return { entry, score };
        }).filter(r => r.score > 0)
          .sort((a, b) => b.score - a.score)
          .slice(0, limit)
          .map(r => r.entry);

        return scored;
    }

    /* ── Render helpers ──────────────────────────────────────── */
    renderResponse(intent, animated, type = 'fullpage') {
        let html = `<strong>${intent.title}</strong>`;
        html += `<ul class="ai-points">`;
        (intent.content_points || []).forEach(point => {
            html += `<li>${point}</li>`;
        });
        html += `</ul>`;

        if (intent.actions?.length) {
            html += `<div class="ai-actions">`;
            intent.actions.forEach(action => {
                if (action.url) {
                    html += `<a href="${action.url}" class="ai-btn primary">${action.text}</a>`;
                } else if (action.query) {
                    html += `<button class="ai-btn secondary" onclick="window.KingstonAI.setInput('${action.query}'); window.KingstonAI.handleSendMessage('${type}');">${action.text}</button>`;
                }
            });
            html += `</div>`;
        }

        this.displayMessage(html, 'bot', animated, type);

        // Append smart follow-up suggestion chips after the bubble
        const chips = this.followUps[intent.id];
        if (chips && chips.length > 0) {
            this.renderSuggestionChips(chips, type, animated);
        }
    }

    getIntentById(id) {
        return this.knowledgeBase?.intents?.find(i => i.id === id) || null;
    }

    /* ── Follow-up suggestion chips ──────────────────────────── */
    renderSuggestionChips(chips, type, animated) {
        const containerId = type === 'fullpage' ? 'fullpage-messages' : 'ai-messages';
        const container = document.getElementById(containerId);
        if (!container) return;

        const row = document.createElement('div');
        row.className = `ai-suggestions-row${animated ? ' animate' : ''}`;

        chips.forEach(chip => {
            const btn = document.createElement('button');
            btn.className = 'ai-suggestion-chip';
            btn.textContent = chip.text;

            if (chip.url) {
                btn.addEventListener('click', () => { window.location.href = chip.url; });
            } else if (chip.q) {
                btn.addEventListener('click', () => {
                    // Remove this chip row once clicked for clean UX
                    row.remove();
                    this.setInput(chip.q);
                    this.handleSendMessage(type);
                });
            }
            row.appendChild(btn);
        });

        container.appendChild(row);
        this.scrollToLatest(container);

        // Save chips row html to localStorage too
        this.saveMessage(row.innerHTML, '__chips__', type);
    }

    /* ── Typing indicator ────────────────────────────────────── */
    showTypingIndicator(type) {
        const containerId = type === 'fullpage' ? 'fullpage-messages' : 'ai-messages';
        const container = document.getElementById(containerId);
        if (!container) return;

        const el = document.createElement('div');
        el.className = 'ai-message-group bot ai-typing-group';
        el.id = `typing-${type}`;
        el.innerHTML = `
            <div class="ai-bot-avatar"><i class="fa-solid fa-robot"></i></div>
            <div class="ai-message-bubble ai-typing-bubble">
                <span class="ai-typing-dot"></span>
                <span class="ai-typing-dot"></span>
                <span class="ai-typing-dot"></span>
            </div>`;
        container.appendChild(el);
        this.scrollToLatest(container);
    }

    hideTypingIndicator(type) {
        const el = document.getElementById(`typing-${type}`);
        if (el) el.remove();
    }

    /* ── Display message ─────────────────────────────────────── */
    displayMessage(content, sender, animated = true, type = 'fullpage', persist = true) {
        const containerId = type === 'fullpage' ? 'fullpage-messages' : 'ai-messages';
        const container = document.getElementById(containerId);
        if (!container) return;

        // Handle restored chip rows specially
        if (sender === '__chips__') {
            const row = document.createElement('div');
            row.className = 'ai-suggestions-row';
            row.innerHTML = content;
            // Re-attach click handlers on restored chips
            row.querySelectorAll('.ai-suggestion-chip').forEach(btn => {
                const text = btn.textContent;
                // Find matching chip query from followUps
                let foundQ = null;
                for (const chips of Object.values(this.followUps)) {
                    const match = chips.find(c => c.text === text);
                    if (match) { foundQ = match.q; break; }
                }
                if (foundQ) {
                    btn.addEventListener('click', () => {
                        row.remove();
                        this.setInput(foundQ);
                        this.handleSendMessage(type);
                    });
                }
            });
            container.appendChild(row);
            this.scrollToLatest(container);
            return;
        }

        const group = document.createElement('div');
        group.className = `ai-message-group ${sender}${animated ? ' animate' : ''}`;

        const bubble = document.createElement('div');
        bubble.className = 'ai-message-bubble';
        bubble.innerHTML = content;

        if (sender === 'bot') {
            const avatar = document.createElement('div');
            avatar.className = 'ai-bot-avatar';
            avatar.innerHTML = '<i class="fa-solid fa-robot"></i>';
            group.appendChild(avatar);
        }

        group.appendChild(bubble);
        container.appendChild(group);
        this.scrollToLatest(container);

        if (persist) this.saveMessage(content, sender, type);
    }

    scrollToLatest(container) {
        if (!container) return;
        setTimeout(() => { container.scrollTop = container.scrollHeight; }, 60);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    window.KingstonAI = new AIAssistant();
});
