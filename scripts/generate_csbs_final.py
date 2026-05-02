import os

# Final CSBS Department Generator (Phase 2)
# Refined UI with deep data integration, PDF assets, and official Anna University links.
# Theme: Corporate Tech (Glassmorphic, Deep Violet & Neon Cyan)

def generate_csbs():
    print("Starting Final CSBS Phase 2 Generation (Deep Integration)...")

    # Load templates
    try:
        with open('csbs_header.txt', 'r', encoding='utf-8') as f: header = f.read()
        with open('csbs_footer.txt', 'r', encoding='utf-8') as f: footer = f.read()
    except FileNotFoundError:
        print("Error: CSBS templates not found. Ensure split_csbs.py has been run.")
        return

    extra_styles = """
<style>
:root {
    --csbs-violet: #4b0082;
    --csbs-neon: #00ffff;
    --csbs-dark: #0f0c29;
    --csbs-glass: rgba(255, 255, 255, 0.07);
}

.dept-main-content section {
    background: #fff;
    border-radius: 25px;
    padding: 40px;
    margin-bottom: 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.06);
    border: 1px solid rgba(75, 0, 130, 0.05);
    transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.dept-main-content section:hover {
    transform: translateY(-5px);
    box-shadow: 0 25px 60px rgba(75, 0, 130, 0.12);
    border-color: var(--csbs-violet);
}

.dept-title-red {
    background: linear-gradient(135deg, var(--csbs-violet), #302b63, #000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    font-size: 3.2rem;
    text-transform: uppercase;
    letter-spacing: -1px;
}

/* Glassmorphic Cards */
.glass-card-csbs {
    background: var(--csbs-glass);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
    border-left: 8px solid var(--csbs-neon);
}

/* Faculty & Achievement Grids */
.achievement-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
}

.achieve-box {
    background: #fff;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #efefff;
    transition: 0.4s;
    position: relative;
    overflow: hidden;
}

.achieve-box:hover {
    background: var(--csbs-violet);
    color: #fff;
}

.achieve-box h4 { font-weight: 800; margin-bottom: 10px; color: inherit; }

/* Interactive PDF Buttons */
.premium-pdf-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: linear-gradient(135deg, var(--csbs-violet), #000);
    color: #fff;
    padding: 16px 35px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 800;
    font-size: 1.1rem;
    box-shadow: 0 10px 25px rgba(75, 0, 130, 0.3);
    transition: 0.4s;
    border: 2px solid transparent;
}

.premium-pdf-btn:hover {
    transform: scale(1.05);
    background: var(--csbs-neon);
    color: #000;
    box-shadow: 0 15px 35px rgba(0, 255, 255, 0.4);
}

.anna-univ-btn {
    background: #fff;
    color: var(--csbs-violet);
    border: 2px solid var(--csbs-violet);
}

.anna-univ-btn:hover {
    background: var(--csbs-violet);
    color: #fff;
}

/* Animations */
@keyframes slideDown { from { opacity:0; transform:translateY(-20px); } to { opacity:1; transform:translateY(0); } }
@keyframes slideUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }

.animate-slide-down { animation: slideDown 0.8s ease-out; }
.animate-slide-up { animation: slideUp 0.8s ease-out; }
</style>
"""

    header = header.replace('</head>', extra_styles + '</head>')

    pages = {
        'csbs_about.html': '''
            <h1 class="dept-title-red animate-slide-down">ABOUT THE DEPARTMENT</h1>
            <section class="dept-section animate-slide-up" data-aos="fade-up">
                <h3>Department Overview</h3>
                <p>The B.Tech. Computer Science and Business Systems program is designed to create industry-ready software engineers who have a strong foundation in Computer Science and an equivalent competency in Business Systems. This curriculum, jointly designed by IT industry giants and academic experts, ensures that our graduates are highly productive from day one.</p>
                <div class="glass-card-csbs">
                    <h4>Industry-Oriented Learning</h4>
                    <p>Unlike traditional engineering programs, CSBS integrates subjects like Financial Management, Business Strategy, and Marketing into the core technical curriculum of Machine Learning, Cloud Computing, and Software Engineering.</p>
                </div>
            </section>
        ''',

        'csbs_vision_mission.html': '''
            <h1 class="dept-title-red animate-slide-down">VISION AND MISSION</h1>
            <section class="dept-section animate-slide-up" data-aos="fade-up">
                <div class="achievement-grid">
                    <div class="achieve-box" style="border-top: 6px solid var(--csbs-violet);">
                        <i class="fa-solid fa-eye" style="font-size: 3rem; color: var(--csbs-violet); margin-bottom: 20px;"></i>
                        <h2>VISION</h2>
                        <p>To strive for excellence in Computer Science and Business Systems with high business values and multi-disciplinary knowledge to produce globally competent and socially responsible technocrats through technical education and innovation.</p>
                    </div>
                    <div class="achieve-box" style="border-top: 6px solid var(--csbs-neon);">
                        <i class="fa-solid fa-rocket" style="font-size: 3rem; color: var(--csbs-neon); margin-bottom: 20px;"></i>
                        <h2>MISSION</h2>
                        <ul style="padding-left: 20px;">
                            <li style="margin-bottom: 10px;">To deliver high-impact engineering education by implementing interactive teaching-learning methodologies.</li>
                            <li style="margin-bottom: 10px;">To nurture specialized domains including Cloud Computing, AI, and Business Analytics through industry collaboration.</li>
                            <li style="margin-bottom: 10px;">To bridge the gap between academia and industry requirements.</li>
                        </ul>
                    </div>
                </div>
            </section>
        ''',

        'csbs_peos.html': '''
            <h1 class="dept-title-red animate-slide-down">PEOs, POs AND PSOs</h1>
            <section class="dept-section animate-slide-up" data-aos="fade-up">
                <h3>Programme Educational Objectives (PEOs)</h3>
                <div class="glass-card-csbs" style="border-left-color: var(--csbs-violet);">
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 15px;"><strong>PEO 1:</strong> Apply fundamental knowledge of science, mathematics, and engineering in solving real-life challenges.</li>
                        <li style="margin-bottom: 15px;"><strong>PEO 2:</strong> Master core competencies in technical and business systems for successful industry careers.</li>
                        <li style="margin-bottom: 15px;"><strong>PEO 3:</strong> Demonstrate leadership qualities and ethical values in multi-disciplinary environments.</li>
                    </ul>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>Programme Specific Outcomes (PSOs)</h3>
                <div class="achievement-grid">
                    <div class="achieve-box">
                        <h4>PSO 1: ANALYTICS</h4>
                        <p>Apply mathematical and business principles to solve complex problems in software projects and data analytics.</p>
                    </div>
                    <div class="achieve-box">
                        <h4>PSO 2: BUSINESS TECH</h4>
                        <p>Integrate computer science foundations with business intelligence tools for effective enterprise solution delivery.</p>
                    </div>
                </div>
            </section>
        ''',

        'csbs_faculty.html': '''
            <h1 class="dept-title-red animate-slide-down">FACULTY DIRECTORY</h1>
            <section class="dept-section animate-slide-up" data-aos="fade-up">
                <h3>Dedicated Leadership & Expertise</h3>
                <p>The department is led by experienced faculty members specializing in Computer Science, Business Analytics, and Cloud Computing.</p>
                <div class="achievement-grid">
                    <div class="achieve-box">
                         <h4>Ms. M. ANITHA, M.E., (Ph.D)</h4>
                         <span class="badge" style="background: var(--csbs-violet); color: white;">HoD / Assistant Professor</span>
                         <p style="margin-top: 10px; font-size: 0.9rem;">Specialization: Cloud Computing, Data Science.</p>
                    </div>
                    <div class="achieve-box">
                         <h4>FACULTY TEAM</h4>
                         <p>Expert team including Assistant Professors with specializations in AI, ML, and Software Engineering.</p>
                    </div>
                </div>
                
                <div style="margin-top: 50px; text-align: center; background: #fafafa; padding: 40px; border-radius: 20px; border: 1px dashed #ccc;">
                    <h4 style="margin-bottom: 20px; font-weight: 800;">OFFICIAL STAFF DIRECTORY</h4>
                    <a href="assets/csbs/CSBS staff details.pdf" target="_blank" class="premium-pdf-btn">
                        <i class="fa-solid fa-file-pdf"></i> View Staff Details PDF
                    </a>
                    <p style="margin-top: 15px; font-size: 0.85rem; color: #666;">Detailed profile and publication history of current CSBS faculty.</p>
                </div>
            </section>
        ''',

        'csbs_curriculum.html': '''
            <h1 class="dept-title-red animate-slide-down">CURRICULUM & SYLLABUS</h1>
            <section class="dept-section animate-slide-up" data-aos="fade-up">
                <h3>Official Anna University Pathways</h3>
                <p>Our curriculum is strictly aligned with Anna University regulations while incorporating high-demand industry electives.</p>
                
                <div class="achievement-grid">
                    <div class="achieve-box" style="border-top: 5px solid var(--csbs-violet);">
                        <h4>Regulation 2021</h4>
                        <p>Foundation for modern B.Tech. CSBS. Integrated business modules and advanced computing.</p>
                        <a href="https://cac.annauniv.edu/aidetails/afug_2021_fu/Revised/IandC/B.Tech.CSBS.pdf" target="_blank" class="premium-pdf-btn anna-univ-btn" style="width: 100%; justify-content: center; margin-top: 20px;">
                            <i class="fa-solid fa-link"></i> AU R2021 Syllabus
                        </a>
                    </div>
                    <div class="achieve-box" style="border-top: 5px solid var(--csbs-neon);">
                        <h4>Regulation 2025</h4>
                        <p>The revised B.E. CSBS framework for incoming batches, focusing on next-gen AI-Business syngery.</p>
                        <a href="https://cac.annauniv.edu/aidetails/afug_2025_fu/CSIE/B.E.%20CSBS%20.pdf" target="_blank" class="premium-pdf-btn" style="width: 100%; justify-content: center; margin-top: 20px;">
                            <i class="fa-solid fa-link"></i> AU R2025 Syllabus
                        </a>
                    </div>
                </div>

                <div class="glass-card-csbs" style="margin-top: 40px; border-left-color: #f5c518;">
                    <h4 style="color: #000;"><i class="fa-solid fa-lightbulb" style="color: #f5c518;"></i> Value Addition</h4>
                    <p>In addition to Anna University core, our department offers value-added courses in <strong>Cloud Computing (Azure)</strong> and <strong>Full Stack Engineering</strong>.</p>
                </div>
            </section>
        ''',

        'csbs_academic_calendar.html': '''
             <h1 class="dept-title-red animate-slide-down">ACADEMIC CALENDAR</h1>
             <section class="dept-section animate-slide-up" data-aos="fade-up" style="text-align: center;">
                <h3>Departmental Schedule 2024-25</h3>
                <p style="margin-bottom: 30px;">Access the official timeline for academic sessions, internal assessments, and department events.</p>
                
                <div class="glass-card-csbs" style="display: inline-block; width: 100%; max-width: 600px; border-left: none; border-bottom: 8px solid var(--csbs-violet);">
                    <i class="fa-regular fa-calendar-check" style="font-size: 4rem; color: var(--csbs-violet); margin-bottom: 20px;"></i>
                    <h2 style="font-weight: 900;">2024-25 CALENDAR</h2>
                    <p style="margin: 20px 0;">Official PDF containing all semester milestones.</p>
                    <a href="assets/csbs/academic_calendar.pdf" target="_blank" class="premium-pdf-btn">
                        <i class="fa-solid fa-download"></i> Download & View Calendar
                    </a>
                </div>
             </section>
        ''',
        
        'csbs_timetable.html': '''
             <h1 class="dept-title-red animate-slide-down">CLASS TIME TABLE</h1>
             <section class="dept-section animate-slide-up" data-aos="fade-up">
                <h3>Semester Schedule</h3>
                <div class="achievement-grid">
                    <div class="achieve-box">
                        <h4>EVEN SEMESTER 2024-25</h4>
                        <a href="assets/csbs/CSBS-2025-26-EVEN SEMESTER TIME TABLE.pdf" target="_blank" class="premium-pdf-btn anna-univ-btn">
                            <i class="fa-solid fa-clock"></i> View Time Table
                        </a>
                    </div>
                    <div class="achieve-box">
                        <h4>PREVIOUS SEMESTER (VII)</h4>
                        <a href="assets/csbs/IV-CSBS-VII-SEM-TT.pdf" target="_blank" class="premium-pdf-btn">
                            <i class="fa-solid fa-file-invoice"></i> View TT Archive
                        </a>
                    </div>
                </div>
             </section>
        '''
    }

    # Generate pages
    for filename, content in pages.items():
        print(f"Generating CSBS Phase 2 Page: {filename}...")
        # Active link hack
        page_header = header.replace(f'href="{filename}"', f'href="{filename}" class="active"')
        
        final_html = page_header + content + footer
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

    print("SUCCESS: CSBS Phase 2 Modernization Complete!")

if __name__ == "__main__":
    generate_csbs()
