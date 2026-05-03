/**
 * Kingston Engineering College – AI Assistant v4
 * Features: Facts lookup layer (HOD/contact/fee queries answered precisely),
 * weighted intent scoring, context memory, department-specific intents,
 * search fallback, typing indicator, Hindi/Hinglish support,
 * follow-up suggestion chips, chat persistence (localStorage)
 */

class AIAssistant {
    constructor() {
        this.knowledgeBase = null;
        this.searchIndex = null;
        this.intentMemory = [];
        this.MAX_MEMORY = 3;
        this.STORAGE_KEY_FP = 'kec_chat_fullpage';
        this.STORAGE_KEY_WG = 'kec_chat_widget';
        this.MAX_STORED = 60;

        /* ── Dept keyword → dept code map ─────────────────────── */
        this.deptMap = {
            'cse': 'cse', 'computer science': 'cse', 'cs': 'cse', 'c s e': 'cse',
            'ece': 'ece', 'electronics': 'ece', 'communication': 'ece', 'e c e': 'ece',
            'mech': 'mech', 'mechanical': 'mech', 'automobile': 'mech',
            'it': 'it', 'information technology': 'it', 'i t': 'it',
            'aids': 'aids', 'ai data science': 'aids', 'data science': 'aids', 'ai&ds': 'aids', 'ai ds': 'aids',
            'aiml': 'aiml', 'ai ml': 'aiml', 'machine learning': 'aiml', 'ai&ml': 'aiml', 'artificial intelligence': 'aiml',
            'csbs': 'csbs', 'business systems': 'csbs', 'cs business': 'csbs',
            'arch': 'arch', 'architecture': 'arch', 'b arch': 'arch', 'barch': 'arch',
            'mba': 'mba', 'management': 'mba', 'business administration': 'mba',
            'sh': 'sh', 'science humanities': 'sh', 'humanities': 'sh', 's&h': 'sh'
        };

        /* ── Per-intent follow-up suggestion chips ─────────────── */
        this.followUps = {
            greeting:        [{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '💰 Fee Structure', q: 'What is the fee structure?' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            admission:       [{ text: '💰 Fee Structure', q: 'What is the fee structure?' }, { text: '🏆 Scholarships', q: 'Tell me about scholarships' }, { text: '📞 Contact Admission', q: 'How to contact Kingston?' }],
            fees:            [{ text: '🏆 Scholarships', q: 'Tell me about scholarships' }, { text: '📋 Admission Process', q: 'Tell me about admissions' }, { text: '🏠 Hostel Fee', q: 'Tell me about hostel facilities' }],
            placement:       [{ text: '💼 Internships', q: 'Tell me about internships' }, { text: '📞 Placement Cell', q: 'Placement cell contact' }, { text: '🎓 Higher Education', q: 'Tell me about higher education' }],
            contact:         [{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '🏫 Departments', q: 'What departments are available?' }],
            departments:     [{ text: '💻 CSE Contact', q: 'CSE department contact' }, { text: '📡 ECE Contact', q: 'ECE department contact' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            hostel:          [{ text: '🚌 Transport', q: 'Tell me about transport and bus routes' }, { text: '🏫 Facilities', q: 'What facilities are available?' }, { text: '💰 Hostel Fees', q: 'What is the fee structure?' }],
            scholarship:     [{ text: '📋 Admission Process', q: 'Tell me about admissions' }, { text: '💰 Fee Structure', q: 'What is the fee structure?' }],
            naac:            [{ text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }, { text: '⭐ IQAC', q: 'Tell me about IQAC' }],
            iqac:            [{ text: '🏅 NAAC', q: 'Tell me about NAAC accreditation' }, { text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }],
            facilities:      [{ text: '📚 Library', q: 'Tell me about library' }, { text: '⚽ Sports', q: 'Tell me about sports' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            library:         [{ text: '🏫 Other Facilities', q: 'What facilities are available?' }, { text: '🔬 Research', q: 'Tell me about research at Kingston' }],
            sports:          [{ text: '🎭 Clubs', q: 'Tell me about clubs and activities' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            transport:       [{ text: '📞 Contact Us', q: 'How to contact Kingston?' }, { text: '🏠 Hostel', q: 'Tell me about hostel facilities' }],
            clubs:           [{ text: '🔬 Research', q: 'Tell me about research at Kingston' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            research:        [{ text: '🏛️ Departments', q: 'What departments are available?' }, { text: '🎓 Higher Education', q: 'Tell me about higher education' }],
            cse:             [{ text: '📊 CSE Placements', q: 'Tell me about CSE placements' }, { text: '👥 CSE Faculty', q: 'Tell me about CSE faculty' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            ece:             [{ text: '📊 ECE Placements', q: 'ECE placements' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            mech:            [{ text: '📊 Mech Placements', q: 'Mechanical placements' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            it:              [{ text: '📊 IT Placements', q: 'IT placements' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            aids:            [{ text: '🤖 AI&ML Dept', q: 'Tell me about AIML department' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            aiml:            [{ text: '🤖 AI&DS Dept', q: 'Tell me about AIDS department' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            csbs:            [{ text: '📊 CSBS Placements', q: 'CSBS placements' }, { text: '📋 Admission', q: 'Tell me about admissions' }],
            arch:            [{ text: '📋 Arch Admission', q: 'Tell me about admissions' }, { text: '💰 Arch Fees', q: 'What is the fee structure?' }],
            mba:             [{ text: '💰 MBA Fees', q: 'What is the fee structure?' }, { text: '📊 MBA Placements', q: 'MBA placements' }],
            alumni:          [{ text: '📊 Placements', q: 'Tell me about placements' }, { text: '🏛️ About Kingston', q: 'Tell me about Kingston Engineering College' }],
            higher_education:[{ text: '📋 Admissions', q: 'Tell me about admissions' }, { text: '📊 Placements', q: 'Tell me about placements' }],
            internship:      [{ text: '📊 Placements', q: 'Tell me about placements' }, { text: '💼 Industry Connect', q: 'Tell me about industry connect' }],
            coe:             [{ text: '🎓 Student Login', q: '' }, { text: '📋 Academics', q: 'Tell me about academics' }],
            about:           [{ text: '🏛️ Departments', q: 'What departments are available?' }, { text: '📋 Admissions', q: 'Tell me about admissions' }],
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
            this.bindGlobalButtons();
            this.restoreOrWelcome();
            this.autoFocusInput();
        } catch (e) {
            console.error('[KingstonAI] Init error:', e);
        }
    }

    /* ── Global Button Binding ───────────────────────────────── */
    bindGlobalButtons() {
        try {
            const toggleBtns = document.querySelectorAll('.ai-widget-toggle');
            toggleBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const widget = document.getElementById('ai-widget-container');
                    if (widget) widget.classList.toggle('active');
                });
            });
        } catch (e) {
            console.warn('[KingstonAI] Button binding error:', e);
        }
    }

    async loadKnowledgeBase() {
        try {
            const base = this.getBasePath();
            const res = await fetch(`${base}data/knowledge-base.json`);
            this.knowledgeBase = await res.json();
        } catch (e) {
            console.warn('[KingstonAI] Failed to load knowledge base.', e);
        }
    }

    async loadSearchIndex() {
        try {
            const base = this.getBasePath();
            const res = await fetch(`${base}data/search-index.json`);
            this.searchIndex = await res.json();
        } catch (e) {
            console.warn('[KingstonAI] Failed to load search index.', e);
        }
    }

    /* Resolve correct base path for fetch (works at all directory depths)
       depth-0 / root (index.html)         → ''
       depth-1 (naac/naac_ssr.html)        → '../'
       depth-2 (departments/cse/cse.html)  → '../../'
    */
    getBasePath() {
        const segments = window.location.pathname.split('/').filter(Boolean);
        const depth = Math.max(0, segments.length - 1); // subtract 1 for the filename
        return '../'.repeat(depth);
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

        document.querySelectorAll('.ai-quick-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const query = btn.getAttribute('data-query');
                if (query) {
                    this.setInput(query);
                    this.handleSendMessage('fullpage');
                }
            });
        });

        const widget = document.getElementById('ai-widget-container');
        const close = document.getElementById('ai-widget-close');
        if (close && widget) {
            close.addEventListener('click', () => widget.classList.remove('active'));
        }

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
            if (history.length > this.MAX_STORED) history.splice(0, history.length - this.MAX_STORED);
            localStorage.setItem(key, JSON.stringify(history));
        } catch (e) {}
    }

    restoreHistory(type) {
        try {
            const key = this.storageKey(type);
            const history = JSON.parse(localStorage.getItem(key) || '[]');
            if (!history.length) return false;
            history.forEach(({ html, sender }) => {
                this.displayMessage(html, sender, false, type, false);
            });
            return true;
        } catch (e) { return false; }
    }

    clearChat(type) {
        try { localStorage.removeItem(this.storageKey(type)); } catch (e) {}
        const containerId = type === 'fullpage' ? 'fullpage-messages' : 'ai-messages';
        const container = document.getElementById(containerId);
        if (container) container.innerHTML = '';
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

        /* Priority 1: Precise fact lookup (HOD name/contact/email etc.) */
        const factHtml = this.lookupFact(normalized, type);
        if (factHtml) {
            this.displayMessage(factHtml, 'bot', true, type);
            return;
        }

        /* Priority 2: Context-aware follow-up */
        const contextResponse = this.handleContextualFollowUp(normalized);
        if (contextResponse) {
            this.recordMemory(contextResponse.id);
            this.renderResponse(contextResponse, true, type);
            return;
        }

        /* Priority 3: Intent detection */
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
            .replace(/\baplly\b/g, 'apply')
            .replace(/\bplacment\b/g, 'placement')
            .replace(/\bfaculity\b/g, 'faculty')
            .replace(/[?!,।]/g, '')
            .replace(/\s+/g, ' ')
            .trim();
    }

    /* ── FACTS LOOKUP LAYER (v4 — the precise answer engine) ─── */
    lookupFact(query, type) {
        if (!this.knowledgeBase) return null;
        const kb = this.knowledgeBase;
        const depts = kb.departments || {};
        const facts = kb.facts || {};
        const hods = facts.hods || {};
        const quickFacts = facts.quick_facts || [];

        /* ── 1. Quick facts (NAAC grade, highest package, etc.) */
        for (const fact of quickFacts) {
            if (query.includes(fact.q)) {
                return this._factCard('📌 Quick Answer', fact.a);
            }
        }

        /* ── 2. HOD queries ──────────────────────────────────── */
        const hodPatterns = [/hod/, /head of dept/, /head of department/, /department head/, /hod name/, /who is hod/, /hod who/];
        const asksHod = hodPatterns.some(p => p.test(query));
        const asksContact = /phone|contact|number|call/.test(query);
        const asksEmail = /email|mail/.test(query);

        const detectedDept = this._detectDept(query);

        if (detectedDept) {
            const deptData = depts[detectedDept];
            const hodData = hods[detectedDept];

            if (asksHod && hodData) {
                return this._factCard(
                    `👤 ${deptData?.name || detectedDept.toUpperCase()} — Head of Department`,
                    `<strong>${hodData.name}</strong><br>
                    ${hodData.designation}<br>
                    📞 <a href="tel:${hodData.phone.replace(/\s|-/g,'')}">${hodData.phone}</a><br>
                    📧 <a href="mailto:${hodData.email}">${hodData.email}</a>`
                );
            }

            if (asksEmail && deptData?.email) {
                return this._factCard(
                    `📧 ${deptData.name} — Email`,
                    `<a href="mailto:${deptData.email}">${deptData.email}</a>`
                );
            }

            if (asksContact && deptData?.phone) {
                return this._factCard(
                    `📞 ${deptData.name} — Contact`,
                    `Phone: <a href="tel:${deptData.phone.replace(/\s|-/g,'')}">${deptData.phone}</a><br>
                    Email: <a href="mailto:${deptData.email}">${deptData.email}</a>`
                );
            }

            /* Placement stats per dept */
            if (/placement|package|placed|lpa|salary/.test(query) && deptData?.placement_rate) {
                return this._factCard(
                    `📊 ${deptData.name} — Placement Stats`,
                    `Placement Rate: <strong>${deptData.placement_rate}</strong><br>
                    Avg Package: <strong>${deptData.avg_package}</strong><br>
                    Top Recruiters: ${(deptData.top_recruiters || []).join(' • ')}`
                );
            }

            /* Intake / seats */
            if (/intake|seats|capacity|how many students/.test(query) && deptData?.intake) {
                return this._factCard(
                    `🎓 ${deptData.name} — Intake`,
                    `Annual intake: <strong>${deptData.intake} seats</strong><br>
                    Degree: ${deptData.degree} | Duration: ${deptData.duration || '4 years'}`
                );
            }
        }

        /* ── 3. All department contacts query ──────────────── */
        if (/all department|all dept|department contact|dept contact|department number|department phone/.test(query)) {
            const deptKeys = ['cse','ece','mech','it','aids','aiml','csbs','arch','mba'];
            let rows = deptKeys.map(k => {
                const d = depts[k];
                if (!d) return '';
                return `<tr><td style="padding:4px 8px;font-weight:600;">${d.short}</td>
                <td style="padding:4px 8px;">${d.name.split(' ').slice(0,3).join(' ')}</td>
                <td style="padding:4px 8px;"><a href="tel:${(d.phone||'').replace(/\s|-/g,'')}">${d.phone||'—'}</a></td>
                <td style="padding:4px 8px;"><a href="mailto:${d.email||''}">${d.email||'—'}</a></td></tr>`;
            }).join('');
            return `<strong>📞 All Department Contacts</strong>
            <div style="overflow-x:auto;margin-top:10px;">
            <table style="width:100%;border-collapse:collapse;font-size:0.82rem;">
            <thead><tr style="background:rgba(0,51,102,0.12);">
            <th style="padding:6px 8px;text-align:left;">Code</th>
            <th style="padding:6px 8px;text-align:left;">Department</th>
            <th style="padding:6px 8px;text-align:left;">Phone</th>
            <th style="padding:6px 8px;text-align:left;">Email</th>
            </tr></thead><tbody>${rows}</tbody></table></div>`;
        }

        /* ── 4. All HOD query ──────────────────────────────── */
        if (/all hod|all heads|list of hod|all head of department/.test(query)) {
            const deptKeys = ['cse','ece','mech','it','aids','aiml','csbs','arch','mba','sh'];
            let rows = deptKeys.map(k => {
                const h = hods[k]; const d = depts[k];
                if (!h) return '';
                return `<tr><td style="padding:4px 8px;font-weight:600;">${d?.short || k.toUpperCase()}</td>
                <td style="padding:4px 8px;">${h.name}</td>
                <td style="padding:4px 8px;"><a href="mailto:${h.email}">${h.email}</a></td></tr>`;
            }).join('');
            return `<strong>👥 All Department HoDs</strong>
            <div style="overflow-x:auto;margin-top:10px;">
            <table style="width:100%;border-collapse:collapse;font-size:0.82rem;">
            <thead><tr style="background:rgba(0,51,102,0.12);">
            <th style="padding:6px 8px;text-align:left;">Dept</th>
            <th style="padding:6px 8px;text-align:left;">HoD Name</th>
            <th style="padding:6px 8px;text-align:left;">Email</th>
            </tr></thead><tbody>${rows}</tbody></table></div>`;
        }

        /* ── 5. Placement cell contact ─────────────────────── */
        if (/placement cell contact|placement office|placement phone|placement email/.test(query)) {
            const p = kb.placements || {};
            return this._factCard('💼 Placement & Training Cell',
                `📞 <a href="tel:${(p.placement_cell_phone||'').replace(/\s|-/g,'')}">${p.placement_cell_phone}</a><br>
                📧 <a href="mailto:${p.placement_cell_email}">${p.placement_cell_email}</a>`
            );
        }

        /* ── 6. Specific fee queries ───────────────────────── */
        const feeData = kb.fees || {};
        if (/be fee|btech fee|engineering fee|ug fee/.test(query)) {
            const f = feeData.be_btech || {};
            return this._factCard('💰 B.E. / B.Tech Annual Fee',
                `Tuition: <strong>${f.tuition_per_year}</strong><br>University Fee: ${f.university_fee}<br>Total: <strong>${f.total_approx}</strong>`
            );
        }
        if (/barch fee|architecture fee/.test(query)) {
            const f = feeData.barch || {};
            return this._factCard('💰 B.Arch Annual Fee',
                `Tuition: <strong>${f.tuition_per_year}</strong><br>Total: <strong>${f.total_approx}</strong>`
            );
        }
        if (/mba fee/.test(query)) {
            const f = feeData.mba || {};
            return this._factCard('💰 MBA Annual Fee', `Total: <strong>${f.tuition_per_year}</strong> per annum`);
        }
        if (/mtech fee/.test(query)) {
            const f = feeData.mtech || {};
            return this._factCard('💰 M.Tech Annual Fee', `Total: <strong>${f.tuition_per_year}</strong> per annum`);
        }

        /* ── 7. College basics ─────────────────────────────── */
        const col = kb.college || {};
        if (/main phone|office phone|college phone|kingston phone/.test(query)) {
            return this._factCard('📞 Kingston Main Office', `<a href="tel:${(col.phone||'').replace(/\s|-/g,'')}">${col.phone}</a>`);
        }
        if (/admission phone|admission number|helpline/.test(query)) {
            return this._factCard('📞 Admission Helpline', `<a href="tel:${(col.admission_phone||'').replace(/\s|-/g,'')}">${col.admission_phone}</a> (Mon–Sat, 9 AM – 6 PM)`);
        }
        if (/address|location|where is kingston|where is the college/.test(query)) {
            return this._factCard('📍 Address', col.address);
        }

        return null; /* No fact matched — fall through to intent detection */
    }

    _factCard(title, body) {
        return `<strong>${title}</strong><p style="margin:8px 0 0;line-height:1.8;">${body}</p>`;
    }

    _detectDept(query) {
        let bestMatch = null;
        let bestLen = 0;
        for (const [keyword, code] of Object.entries(this.deptMap)) {
            if (query.includes(keyword) && keyword.length > bestLen) {
                bestMatch = code;
                bestLen = keyword.length;
            }
        }
        return bestMatch;
    }

    /* ── Weighted Intent Detection ───────────────────────────── */
    detectIntent(message) {
        if (!this.knowledgeBase?.intents) return null;

        const scores = this.knowledgeBase.intents.map(intent => ({
            intent,
            score: this.scoreIntent(intent, message)
        }));

        scores.sort((a, b) => b.score - a.score);

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

                if (message === k) { total += 100; continue; }
                if (message.includes(k)) { total += 60 + (k.length * 2); continue; }
                if (kwWords.length > 0 && kwWords.every(w => message.includes(w))) { total += 50; continue; }

                for (const kwWord of kwWords) {
                    if (kwWord && msgWords.includes(kwWord)) total += 30;
                }

                if (k.length >= 4) {
                    const partial = k.slice(0, Math.ceil(k.length * 0.8));
                    if (message.includes(partial)) total += 15;
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
        const acks = ['yes', 'ok', 'okay', 'sure', 'go ahead', 'please', 'haan', 'theek hai', 'ha', 'tell me more', 'more info', 'details'];
        if (!acks.includes(message)) return null;

        const last = this.intentMemory[this.intentMemory.length - 1];
        if (!last) return null;

        const followUp = {
            'admission': 'fees', 'fees': 'scholarship', 'placement': 'internship',
            'departments': 'cse', 'cse': 'placement', 'ece': 'placement',
            'mech': 'placement', 'it': 'placement', 'hostel': 'transport',
            'about': 'facilities', 'naac': 'iqac'
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
            "Good question! Let me point you to the most relevant resources:",
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
                    row.remove();
                    this.setInput(chip.q);
                    this.handleSendMessage(type);
                });
            }
            row.appendChild(btn);
        });

        container.appendChild(row);
        this.scrollToLatest(container);
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

        if (sender === '__chips__') {
            const row = document.createElement('div');
            row.className = 'ai-suggestions-row';
            row.innerHTML = content;
            row.querySelectorAll('.ai-suggestion-chip').forEach(btn => {
                const text = btn.textContent;
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
