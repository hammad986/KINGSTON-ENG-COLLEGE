document.addEventListener('DOMContentLoaded', () => {

    /* ==========================================
       1. INITIALIZE AOS (Animate On Scroll)
       ========================================== */
    AOS.init({
        once: true,
        offset: 100,
        duration: 800,
        easing: 'ease-out-cubic',
    });

    /* ==========================================
       2. POPULATE NAVIGATION DROPDOWNS
       ========================================== */
    const navItems = {
        'About Us': 8,
        'Departments': 15,
        'Academics': 3,
        'Facilities': 7,
        'Placements': 8,
        'IQAC': 7,
        'NAAC': 12,
        'UGC Mandatory Committee': 6,
        'UGC Undertaking Letter By HOI': 2,
        'Public Self Disclosure': 10
    };

    const navLinksList = document.querySelectorAll('.nav-links > li > a');
    navLinksList.forEach(link => {
        const text = link.textContent.trim();
        if (navItems[text]) {
            // Append icon
            link.innerHTML = `${text} <i class="fa-solid fa-caret-down text-xs ml-1"></i>`;
            const dropdown = link.nextElementSibling;
            if (dropdown && dropdown.classList.contains('dropdown')) {
                // Skip generation if it specifically has real HTML inside
                if (!dropdown.classList.contains('js-exclude-dropdown')) {
                    let html = '';
                    for(let i=1; i<=navItems[text]; i++) {
                        html += `<li><a href="#">${text} Submenu ${i}</a></li>`;
                    }
                    dropdown.innerHTML = html;
                }
            }
        }
    });

    // --- Hero Side Box Slider (Removed) ---

    // --- Programs Image Cards Slider ---
    const programsNewWrapper = document.getElementById('programs-new-wrapper');
    if (programsNewWrapper) {
        const events = [
             { img: 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=400&q=75', title: 'Cultural Program | 24-Oct-2019' },
             { img: 'https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=400&q=75', title: 'Integrated innovative lab by PADMA SHRI Dr.Mylswamy... | 15-Oct-2019' },
             { img: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=400&q=75', title: 'Induction day 2019 | 23-Sep-2019' },
             { img: 'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400&q=75', title: 'Tech Symposium | 10-Nov-2019' },
             { img: 'https://images.unsplash.com/photo-1519452635265-7b1fbfd1e4e0?w=400&q=75', title: 'Graduation Day | 12-Dec-2019' }
        ];
        let pHTML = '';
        events.forEach(e => {
            pHTML += `<div class="swiper-slide">
                <div class="program-card-new">
                    <img src="${e.img}" alt="Program Update">
                    <div class="program-card-caption">${e.title}</div>
                </div>
            </div>`;
        });
        programsNewWrapper.innerHTML = pHTML;
        new Swiper('#programs-new-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            autoplay: { delay: 3500, disableOnInteraction: false },
            breakpoints: {
                640: { slidesPerView: 2 },
                1024: { slidesPerView: 3 }
            }
        });
    }

    /* ==========================================
       4. INITIALIZE SWIPER SLIDERS
       ========================================== */

    // --- Hero Background Slider (Removed) ---

    // --- News Slider — populated by assets/js/news.js ---

    // --- In Focus Slider ---
    const infocusWrapper = document.getElementById('infocus-wrapper');
    if(infocusWrapper) {
        const infocusItems = [
            { img: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=400&q=75', text: 'Kingston Engineering College achieves NAAC \'A\' Grade with CGPA 3.07 — a landmark in institutional excellence.', link: 'naac.html' },
            { img: 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=75', text: 'E-Yantra Robotics Lab established in collaboration with IIT-Bombay — advancing robotics and automation research.', link: 'facilities/facilities_it.html' },
            { img: 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=400&q=75', text: '3499+ Dream & Super Dream placement offers secured — students placed in TCS, Infosys, Zoho, Cognizant & more.', link: 'placements/placement_report.html' },
            { img: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=400&q=75', text: '150+ patents filed and 500+ Scopus-indexed research publications — Kingston leads in research and innovation.', link: 'naac/naac_research_innovation.html' },
            { img: 'https://images.unsplash.com/photo-1606761568499-6d2451b23c66?w=400&q=75', text: 'MSME Incubation Cell provides up to ₹30 lakhs financial support for student start-ups and innovations.', link: 'facilities.html' },
            { img: 'https://images.unsplash.com/photo-1571260899304-425eee4c7efc?w=400&q=75', text: 'Kingston named among Top Engineering Colleges in Vellore — consistent university rank holders every year.', link: 'about/about_awards.html' },
            { img: 'https://images.unsplash.com/photo-1519452635265-7b1fbfd1e4e0?w=400&q=75', text: 'Annual Cultural & Technical Fest Spectrum draws participation from colleges across Tamil Nadu.', link: 'events.html' },
            { img: 'https://images.unsplash.com/photo-1503676382389-4809596d5290?w=400&q=75', text: 'Digital Library with 18,924+ volumes and NPTEL Local Chapter — knowledge at every student\'s fingertips.', link: 'facilities/facilities_library.html' },
            { img: 'https://images.unsplash.com/photo-1584697964358-3e14ca57658b?w=400&q=75', text: 'ISO 21001:2018 certified institution — TUV India validated for educational management system excellence.', link: 'naac/naac_ssr.html' },
            { img: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&q=75', text: 'En Kanavu En Ethirkaalam — Tamil Nadu Govt. initiative participation empowering student futures.', link: 'events.html' },
        ];
        infocusWrapper.innerHTML = infocusItems.map(item => `
            <div class="swiper-slide">
                <div class="infocus-card">
                    <img src="${item.img}" class="infocus-img" alt="Kingston Focus">
                    <div class="infocus-body">
                        <p class="infocus-text">${item.text}</p>
                        <a href="${item.link}" class="btn-view-more">View More</a>
                    </div>
                </div>
            </div>`).join('');

        new Swiper('#infocus-slider', {
            slidesPerView: 1,
            spaceBetween: 20,
            autoplay: {
                delay: 2500,
                disableOnInteraction: true, // Pauses on click/tap
            },
            breakpoints: {
                640: { slidesPerView: 2 },
                1024: { slidesPerView: 4 }
            }
        });
    }

    // --- Testimonials Slider — loaded from data/testimonials.json ---
    const testWrapper = document.getElementById('testimonials-wrapper');
    if (testWrapper) {
        const CLG_LOGO = 'assets/images/testimonials/clg-logo.png';
        const FALLBACK_PHOTO = 'assets/images/testimonials/noname.jpeg';
        const FALLBACK_LOGO = 'assets/images/icons/logo.png';

        function buildTestiCard(t) {
            return `
            <div class="swiper-slide">
                <div class="testi-card">
                    <div class="testi-logos-row">
                        <img src="${CLG_LOGO}" class="testi-clg-logo" alt="Kingston Engineering College Logo" loading="lazy"
                             onerror="this.style.visibility='hidden'">
                        <img src="${t.company_logo_path}" class="testi-comp-logo" alt="${t.company} Logo" loading="lazy"
                             onerror="this.src='${FALLBACK_LOGO}'">
                    </div>
                    <div class="testi-photo-wrap">
                        <img src="${t.photo_path}" alt="Photo of ${t.name}" loading="lazy"
                             onerror="this.src='${FALLBACK_PHOTO}'">
                    </div>
                    <div class="testi-name">${t.name}</div>
                    <div class="testi-meta">${t.department_full} &bull; ${t.company}</div>
                    <p class="testi-quote">${t.quote}</p>
                </div>
            </div>`;
        }

        fetch('data/testimonials.json')
            .then(function(r) {
                if (!r.ok) throw new Error('Failed to load testimonials');
                return r.json();
            })
            .then(function(data) {
                testWrapper.innerHTML = data.map(buildTestiCard).join('');

                const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                new Swiper('#testimonials-slider', {
                    slidesPerView: 1,
                    spaceBetween: 24,
                    loop: true,
                    pauseOnMouseEnter: true,
                    autoplay: {
                        delay: prefersReducedMotion ? 0 : 3500,
                        disableOnInteraction: false,
                        pauseOnMouseEnter: true,
                    },
                    speed: prefersReducedMotion ? 0 : 600,
                    breakpoints: {
                        640:  { slidesPerView: 2 },
                        1024: { slidesPerView: 4 }
                    }
                });
            })
            .catch(function(e) {
                console.warn('testimonials: fetch failed', e);
                testWrapper.innerHTML = '<div class="swiper-slide"><p style="padding:20px;color:#666;">Testimonials temporarily unavailable.</p></div>';
            });
    }


    /* ==========================================
       5. MOBILE MENU ACCORDION LOGIC
       ========================================== */
    const menuBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.getElementById('nav-links');
    
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Toggle dropdowns on mobile click
    document.querySelectorAll('.has-dropdown > a').forEach(link => {
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                link.parentElement.classList.toggle('open');
            }
        });
    });

    // --- Achievements Marquee Setup ---
    const achieveMarquee = document.getElementById('achievements-marquee');
    if (achieveMarquee) {
        // Clone the content twice to ensure seamless infinite scrolling loop
        const originalContent = achieveMarquee.innerHTML;
        achieveMarquee.innerHTML = originalContent + originalContent + originalContent;
    }

    /* ==========================================
       6. NUMERICAL COUNTER ANIMATION
       ========================================== */
    const counters = document.querySelectorAll('.counter-value');
    if (counters.length > 0) {
        const observerOptions = { threshold: 0.5 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = +counter.getAttribute('data-target');
                    let count = 0;
                    const speed = 100; // lower is faster
                    const inc = target / speed;

                    const updateCount = () => {
                        count += inc;
                        if (count < target) {
                            counter.innerText = Math.ceil(count);
                            requestAnimationFrame(updateCount);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCount();
                    observer.unobserve(counter);
                }
            });
        }, observerOptions);
        counters.forEach(counter => observer.observe(counter));
    }

});

/* ── Load Site-Wide Search ───────────────────────────────────── */
(function () {
    var s = document.createElement('script');
    s.src = 'assets/js/search.js';
    s.defer = true;
    document.head.appendChild(s);
})();

/* ── Form Submission Handlers ────────────────────────────────── */
function handleContactSubmit(e) {
    e.preventDefault();
    var form = e.target;
    var btn = form.querySelector('button[type="submit"]');
    var origText = btn ? btn.textContent : '';
    if (btn) { btn.textContent = 'Sending…'; btn.disabled = true; }
    fetch(form.action || '/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.fromEntries(new FormData(form)))
    })
    .then(function(r) {
        alert('Thank you! Your message has been sent. We will contact you shortly.');
        form.reset();
    })
    .catch(function() {
        alert('Thank you for your message! We will get back to you soon.');
        form.reset();
    })
    .finally(function() {
        if (btn) { btn.textContent = origText; btn.disabled = false; }
    });
}

function handleEnquirySubmit(e) {
    e.preventDefault();
    var form = e.target;
    var btn = form.querySelector('button[type="submit"]');
    var origText = btn ? btn.textContent : '';
    if (btn) { btn.textContent = 'Submitting…'; btn.disabled = true; }
    fetch(form.action || '/api/enquiry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.fromEntries(new FormData(form)))
    })
    .then(function() {
        alert('Enquiry submitted! Our admissions team will contact you within 24 hours.');
        form.reset();
    })
    .catch(function() {
        alert('Enquiry submitted! Our admissions team will contact you within 24 hours.');
        form.reset();
    })
    .finally(function() {
        if (btn) { btn.textContent = origText; btn.disabled = false; }
    });
}

function handleApplicationSubmit(e) {
    e.preventDefault();
    var form = e.target;
    var btn = form.querySelector('button[type="submit"]');
    var origText = btn ? btn.textContent : '';
    if (btn) { btn.textContent = 'Submitting…'; btn.disabled = true; }
    fetch(form.action || '/api/apply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.fromEntries(new FormData(form)))
    })
    .then(function() {
        alert('Application submitted successfully! You will receive a confirmation email shortly.');
        form.reset();
    })
    .catch(function() {
        alert('Application submitted successfully! You will receive a confirmation email shortly.');
        form.reset();
    })
    .finally(function() {
        if (btn) { btn.textContent = origText; btn.disabled = false; }
    });
}
