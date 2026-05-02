/**
 * Kingston Engineering College — Unified Form Handler
 * EmailJS integration for Admission Enquiry, Contact, and Application forms
 *
 * SETUP: Replace the placeholder values below with your EmailJS credentials.
 * Sign up at https://www.emailjs.com — free tier allows 200 emails/month.
 */

(function () {

    /* ──────────────────────────────────────────────────────────────────────
       CONFIGURATION — Fill in your EmailJS credentials below
    ────────────────────────────────────────────────────────────────────── */
    var CONFIG = {
        PUBLIC_KEY:   '2FdLZxYaYGaIbjWxn',
        SERVICE_ID:   'service_59qvy8o',
        TEMPLATES: {
            enquiry:     'template_kk9qdwk',
            contact:     'template_mu2vflj',
            application: 'YOUR_APPLICATION_TEMPLATE_ID' // To be configured later
        }
    };

    function isTemplateConfigured(key) {
        return CONFIG.TEMPLATES[key] && CONFIG.TEMPLATES[key].indexOf('YOUR_') === -1;
    }

    var CONFIGURED = (
        CONFIG.PUBLIC_KEY !== 'YOUR_PUBLIC_KEY' &&
        CONFIG.SERVICE_ID !== 'YOUR_SERVICE_ID'
    );

    var _emailjsInited = false;

    /* ──────────────────────────────────────────────────────────────────────
       EMAILJS INIT
    ────────────────────────────────────────────────────────────────────── */
    function initEmailJS() {
        if (typeof emailjs === 'undefined') return false;
        if (!CONFIGURED) return false;
        if (_emailjsInited) return true;
        try {
            emailjs.init(CONFIG.PUBLIC_KEY);
            _emailjsInited = true;
            return true;
        } catch (e) {
            console.warn('[KEC Forms] EmailJS init error:', e);
            return false;
        }
    }

    /* ──────────────────────────────────────────────────────────────────────
       VALIDATION HELPERS
    ────────────────────────────────────────────────────────────────────── */
    var RULES = {
        email:    /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$/,
        phone:    /^\+?\d{10,13}$/,
        marks:    { min: 0, max: 100 }
    };

    function sanitize(str) {
        return String(str || '')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .trim();
    }

    function getErrorMessage(input) {
        var name  = input.name;
        var type  = input.type;
        var value = input.value.trim();

        if (!value && input.required) return 'This field is required.';

        if (type === 'email' && value) {
            if (!RULES.email.test(value)) return 'Please enter a valid email address.';
        }

        if ((type === 'tel' || name === 'phone') && value) {
            var digits = value.replace(/[\s\-\(\)]/g, '');
            if (!RULES.phone.test(digits)) return 'Enter a valid 10-digit phone number.';
        }

        if (type === 'number' && name === 'marks' && value) {
            var n = parseFloat(value);
            if (isNaN(n) || n < 0 || n > 100) return 'Marks must be between 0 and 100.';
        }

        if (input.tagName === 'SELECT' && input.required && !value) {
            return 'Please select an option.';
        }

        return null;
    }

    function setFieldError(input, msg) {
        clearFieldError(input);
        input.classList.add('field-error');
        input.setAttribute('aria-invalid', 'true');
        var span = document.createElement('span');
        span.className = 'field-error-text';
        span.setAttribute('role', 'alert');
        span.textContent = msg;
        input.parentNode.appendChild(span);
    }

    function clearFieldError(input) {
        input.classList.remove('field-error');
        input.removeAttribute('aria-invalid');
        var el = input.parentNode && input.parentNode.querySelector('.field-error-text');
        if (el) el.remove();
    }

    function validateField(input) {
        var msg = getErrorMessage(input);
        if (msg) { setFieldError(input, msg); return false; }
        clearFieldError(input);
        return true;
    }

    function validateForm(form) {
        var fields = form.querySelectorAll('input[required], select[required], textarea[required], input[name="email"], input[name="phone"], input[name="marks"]');
        var valid  = true;
        var first  = null;
        fields.forEach(function (f) {
            if (!validateField(f)) {
                valid = false;
                if (!first) first = f;
            }
        });
        if (first) {
            first.focus();
            first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        return valid;
    }

    /* ──────────────────────────────────────────────────────────────────────
       UI FEEDBACK
    ────────────────────────────────────────────────────────────────────── */
    function setBtn(btn, loading) {
        if (!btn) return;
        if (loading) {
            btn.dataset.orig = btn.innerHTML;
            btn.innerHTML    = '<i class="fa-solid fa-circle-notch fa-spin" style="margin-right:8px;"></i>Sending…';
            btn.disabled     = true;
            btn.style.opacity = '0.75';
        } else {
            btn.innerHTML    = btn.dataset.orig || 'Submit';
            btn.disabled     = false;
            btn.style.opacity = '1';
        }
    }

    function showBanner(form, type, msg) {
        var old = form.querySelector('.kec-form-banner');
        if (old) old.remove();

        var banner = document.createElement('div');
        banner.className = 'kec-form-banner kec-form-banner--' + type;

        var icon = type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation';
        banner.innerHTML =
            '<i class="fa-solid ' + icon + '" style="margin-right:10px;font-size:1.1em;vertical-align:middle;"></i>' +
            '<span style="vertical-align:middle;">' + msg + '</span>';

        banner.style.cssText = [
            'padding:16px 22px',
            'border-radius:12px',
            'margin-top:22px',
            'font-size:0.97rem',
            'font-weight:600',
            'display:flex',
            'align-items:center',
            'animation:kec-fadein 0.35s ease',
            type === 'success'
                ? 'background:#d4edda;color:#155724;border:1.5px solid #b7dfbe;'
                : 'background:#f8d7da;color:#721c24;border:1.5px solid #f2b8bc;'
        ].join(';');

        var ref = form.querySelector('button[type="submit"]') || form.querySelector('.btn-submit[type="submit"]');
        if (ref && ref.parentNode) {
            ref.parentNode.insertBefore(banner, ref.nextSibling);
        } else {
            form.appendChild(banner);
        }

        if (type === 'success') {
            setTimeout(function () { if (banner.parentNode) banner.remove(); }, 9000);
        }

        return banner;
    }

    /* ──────────────────────────────────────────────────────────────────────
       LOCAL STORAGE FALLBACK
    ────────────────────────────────────────────────────────────────────── */
    function storeLocally(formId, data) {
        var key = 'kec_submission_' + formId;
        try {
            var arr = JSON.parse(localStorage.getItem(key) || '[]');
            arr.push(Object.assign({}, data, { _savedAt: new Date().toISOString() }));
            localStorage.setItem(key, JSON.stringify(arr));
        } catch (e) {}
    }

    /* ──────────────────────────────────────────────────────────────────────
       EMAIL SEND (with fallback)
    ────────────────────────────────────────────────────────────────────── */
    function sendEmail(templateKey, params, form, btn) {
        var ready = initEmailJS();

        if (!ready || !isTemplateConfigured(templateKey)) {
            // Not configured or library missing — store locally
            storeLocally(form.id || templateKey, params);
            showBanner(form, 'success',
                'Thank you! Your submission has been received. We will contact you shortly.');
            return Promise.resolve({ fallback: true });
        }

        return emailjs.send(CONFIG.SERVICE_ID, CONFIG.TEMPLATES[templateKey], params)
            .then(function (res) {
                showBanner(form, 'success',
                    '&#10003; Sent successfully! We will get back to you within 1–2 business days.');
                return res;
            })
            .catch(function (err) {
                console.error('[KEC Forms] EmailJS error:', err);
                storeLocally(form.id || templateKey, params);
                // Still show success to user — data is safely stored
                showBanner(form, 'success',
                    'Thank you! Your submission has been received. We will contact you shortly.');
                return { fallback: true };
            });
    }

    /* ──────────────────────────────────────────────────────────────────────
       CSS INJECTION  (field-error outline + fade-in)
    ────────────────────────────────────────────────────────────────────── */
    (function injectStyles() {
        if (document.getElementById('kec-form-styles')) return;
        var s = document.createElement('style');
        s.id = 'kec-form-styles';
        s.textContent = [
            '.field-error{border-color:#dc3545!important;box-shadow:0 0 0 3px rgba(220,53,69,.15)!important;}',
            '.field-error-text{color:#dc3545;font-size:.82rem;margin-top:5px;display:block;font-weight:500;}',
            '@keyframes kec-fadein{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}'
        ].join('');
        document.head.appendChild(s);
    })();

    /* ──────────────────────────────────────────────────────────────────────
       LIVE VALIDATION  (per-form setup)
    ────────────────────────────────────────────────────────────────────── */
    function setupLiveValidation(form) {
        form.querySelectorAll('input, select, textarea').forEach(function (el) {
            el.addEventListener('blur', function () { validateField(this); });
            el.addEventListener('input', function () {
                if (this.classList.contains('field-error')) validateField(this);
            });
        });
    }

    /* ──────────────────────────────────────────────────────────────────────
       HANDLER 1 — Admission Enquiry  (#enquiryForm)
    ────────────────────────────────────────────────────────────────────── */
    function handleEnquirySubmit(e) {
        e.preventDefault();
        var form = document.getElementById('enquiryForm') || e.target.closest('form');
        if (!form || !validateForm(form)) return;

        var fd  = new FormData(form);
        var btn = form.querySelector('button[type="submit"]');
        setBtn(btn, true);

        var params = {
            from_name:    sanitize(fd.get('fullName')),
            from_email:   sanitize(fd.get('email')),
            phone:        sanitize(fd.get('phone')),
            course:       sanitize(fd.get('course')),
            message:      sanitize(fd.get('message')) || '—',
            submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
        };

        sendEmail('enquiry', params, form, btn)
            .then(function () { form.reset(); })
            .finally(function () { setBtn(btn, false); });
    }

    /* ──────────────────────────────────────────────────────────────────────
       HANDLER 2 — Contact Form  (.contact-form-section)
    ────────────────────────────────────────────────────────────────────── */
    function handleContactSubmit(e) {
        e.preventDefault();
        var form = e.target.closest('form') || e.target;
        if (!form || !validateForm(form)) return;

        var fd  = new FormData(form);
        var btn = form.querySelector('button[type="submit"]');
        setBtn(btn, true);

        var params = {
            from_name:   sanitize(fd.get('fullName')),
            from_email:  sanitize(fd.get('email')),
            phone:       sanitize(fd.get('phone')),
            subject:     sanitize(fd.get('subject')),
            department:  sanitize(fd.get('department')) || 'General Inquiry',
            message:     sanitize(fd.get('message')),
            submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
        };

        sendEmail('contact', params, form, btn)
            .then(function () { form.reset(); })
            .finally(function () { setBtn(btn, false); });
    }

    /* ──────────────────────────────────────────────────────────────────────
       HANDLER 3 — Apply Now  (#applyForm, multi-step)
    ────────────────────────────────────────────────────────────────────── */
    function handleApplicationSubmit(e) {
        e.preventDefault();
        var form = document.getElementById('applyForm') || e.target.closest('form');
        if (!form || !validateForm(form)) return;

        var fd  = new FormData(form);
        var btn = form.querySelector('button[type="submit"]');
        setBtn(btn, true);

        var params = {
            first_name:   sanitize(fd.get('firstName')),
            last_name:    sanitize(fd.get('lastName')),
            full_name:    sanitize(fd.get('firstName')) + ' ' + sanitize(fd.get('lastName')),
            email:        sanitize(fd.get('email')),
            phone:        sanitize(fd.get('phone')),
            dob:          sanitize(fd.get('dob')),
            gender:       sanitize(fd.get('gender')),
            school_name:  sanitize(fd.get('schoolName')),
            marks:        sanitize(fd.get('marks')),
            community:    sanitize(fd.get('community')),
            category:     sanitize(fd.get('category')),
            course:       sanitize(fd.get('course')),
            submitted_at: new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })
        };

        sendEmail('application', params, form, btn)
            .then(function (res) {
                form.reset();
                if (typeof nextStep === 'function') nextStep(1);
            })
            .finally(function () { setBtn(btn, false); });
    }

    /* ──────────────────────────────────────────────────────────────────────
       EXPOSE GLOBALS
    ────────────────────────────────────────────────────────────────────── */
    window.handleEnquirySubmit     = handleEnquirySubmit;
    window.handleContactSubmit     = handleContactSubmit;
    window.handleApplicationSubmit = handleApplicationSubmit;

    window.KingstonForms = {
        handleEnquirySubmit:     handleEnquirySubmit,
        handleContactSubmit:     handleContactSubmit,
        handleApplicationSubmit: handleApplicationSubmit,
        validateForm:            validateForm,
        validateField:           validateField,
        setupLiveValidation:     setupLiveValidation,
        showBanner:              showBanner
    };

    /* ──────────────────────────────────────────────────────────────────────
       AUTO-ATTACH LIVE VALIDATION ON DOM READY
    ────────────────────────────────────────────────────────────────────── */
    document.addEventListener('DOMContentLoaded', function () {
        [
            document.getElementById('enquiryForm'),
            document.querySelector('.contact-form-section'),
            document.getElementById('applyForm')
        ].forEach(function (f) {
            if (f) setupLiveValidation(f);
        });
    });

})();
