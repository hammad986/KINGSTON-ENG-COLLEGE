import os
import re

# Define the highly animated AI&DS department pages with deep analysis from PDF data.

def generate_aids():
    print("Starting Final AI&DS Supreme Generation...")

    # Load base template from dept_aids.html
    try:
        with open('dept_aids.html', 'r', encoding='utf-8') as f:
            base_html = f.read()
    except FileNotFoundError:
        print("Error: dept_aids.html not found. Using generic template.")
        base_html = "<html><body><main class='dept-main-content'>{content}</main></body></html>"

    # Extract header and footer
    if '<main class="dept-main-content">' in base_html:
        header = base_html.split('<main class="dept-main-content">')[0] + '<main class="dept-main-content">'
        footer = '</main>' + base_html.split('</main>')[1]
    else:
        header = "<html><body><main class='dept-main-content'>"
        footer = "</main></body></html>"

    # Define common styles for the deep analysis updates
    extra_styles = """
<style>
/* Curriculum Semester Grid */
.sem-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 25px; }
.sem-card { 
    background: white; 
    padding: 20px; 
    border-radius: 12px; 
    border-bottom: 5px solid #a31f24; 
    box-shadow: 0 8px 25px rgba(0,0,0,0.06); 
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
    cursor: pointer; 
}
.sem-card:hover { transform: translateY(-8px); background: #a31f24; color: white; border-bottom-color: gold; }
.sem-card h4 { margin: 0; font-size: 1.15rem; font-weight: 800; }
.sem-card p { margin: 8px 0 0; font-size: 0.85rem; opacity: 0.8; line-height: 1.4; }

/* Specialization Verticals */
.vertical-box { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 25px; background: linear-gradient(135deg, #003366, #001a33); padding: 30px; border-radius: 18px; border: 1px solid rgba(0, 204, 255, 0.1); }
.vertical-tag { 
    background: rgba(255, 255, 255, 0.08); 
    color: white; 
    padding: 10px 22px; 
    border-radius: 30px; 
    border: 1px solid rgba(255, 255, 255, 0.15); 
    font-weight: 600; 
    font-size: 0.9rem; 
    transition: all 0.3s ease; 
}
.vertical-tag:hover { background: #f5c518; color: #a31f24; transform: scale(1.1); box-shadow: 0 0 20px rgba(245, 197, 24, 0.4); border-color: transparent; }

/* Placement Roadmap */
.roadmap { position: relative; padding: 20px 0; border-left: 3px dashed #a31f24; margin-left: 35px; }
.roadmap-step { display: flex; gap: 25px; margin-bottom: 45px; position: relative; margin-left: -33px; align-items: center; }
.step-number { 
    width: 66px; height: 66px; 
    background: #a31f24; 
    color: white; 
    border-radius: 50%; 
    display: flex; 
    align-items: center; 
    justify-content: center; 
    font-weight: 900; 
    font-size: 1.6rem; 
    box-shadow: 0 0 25px rgba(163, 31, 36, 0.4); 
    border: 4px solid #fff;
    z-index: 10;
}
.step-content { 
    background: #fff; 
    padding: 25px; 
    border-radius: 18px; 
    flex-grow: 1; 
    border: 1px solid #eee; 
    box-shadow: 0 10px 40px rgba(0,0,0,0.06); 
    transition: 0.3s;
}
.step-content:hover { transform: translateX(10px); background: #fdf5f5; }
.step-content h4 { color: #a31f24; margin: 0 0 8px 0; letter-spacing: 0.5px; }

/* Industrial Visit Cards */
.visit-card { background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.07); transition: all 0.4s ease; border: 1px solid #eee; }
.visit-card:hover { transform: scale(1.02); box-shadow: 0 20px 50px rgba(0,0,0,0.12); border-color: #003366; }
.visit-header { background: #003366; color: #f5c518; padding: 18px 25px; display: flex; justify-content: space-between; align-items: center; font-weight: 800; font-size: 1.2rem; }
.visit-body { padding: 25px; font-size: 1rem; color: #444; line-height: 1.6; }

/* AI-Themed Glass Card */
.glass-card-deep { 
    background: rgba(255, 255, 255, 0.1); 
    backdrop-filter: blur(15px); 
    border: 1px solid rgba(255, 255, 255, 0.2); 
    padding: 35px; 
    border-radius: 22px; 
    box-shadow: 0 15px 45px rgba(0,0,0,0.08); 
    transition: 0.3s;
}

.pdf-btn-premium { 
    display: inline-block; 
    padding: 15px 35px; 
    background: #a31f24; 
    color: white !important; 
    font-weight: 800; 
    border-radius: 12px; 
    transition: all 0.3s; 
    text-transform: uppercase; 
    letter-spacing: 1.2px; 
    border: none; 
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(163,31,36,0.25);
}
.pdf-btn-premium:hover { background: #003366; transform: translateY(-3px); box-shadow: 0 15px 35px rgba(0,51,102,0.3); }

/* Animation Overrides */
[data-aos] { pointer-events: none; }
[data-aos].aos-animate { pointer-events: auto; }
</style>
"""

    # Inject styles into header
    if '</style>' in header:
        header = header.replace('</style>', extra_styles + '</style>')
    else:
        header = header.replace('</head>', '<style>' + extra_styles + '</style></head>')

    pages = {
        'aids_curriculum.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CURRICULUM & VERTICALS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ACADEMIC JOURNEY (ANNA UNIVERSITY R2021)</h3>
                <p>The AI&DS curriculum is meticulously structured across 8 semesters to build core-to-advanced engineering competencies.</p>
                <div class="sem-grid">
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="50"><h4>Semester I</h4><p>Matrices & Calculus, Python Programming, Physics, Chemistry</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="100"><h4>Semester II</h4><p>Data Structures, Statistics & Numerical Methods, Engineering Graphics</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="150"><h4>Semester III</h4><p>Artificial Intelligence, Design & Analysis of Algorithms, DBMS</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="200"><h4>Semester IV</h4><p>Machine Learning, Data Science & Analytics, Computer Networks</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="250"><h4>Semester V</h4><p>Deep Learning, Big Data Analytics, Distributed Computing</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="300"><h4>Semester VI</h4><p>Embedded Systems & IoT, Professional Electives - Verticals</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="350"><h4>Semester VII</h4><p>Human Values & Ethics, Management Electives, Open Electives</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="400"><h4>Semester VIII</h4><p>Final Year Project Work / Major Industry Internship</p></div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROFESSIONAL ELECTIVE VERTICALS (DEEP SPECIALIZATION)</h3>
                <p>Students can customize their niche by choosing from our 6 strategic career verticals:</p>
                <div class="vertical-box">
                    <span class="vertical-tag" title="AI Architect, Data Architect"><i class="fa-solid fa-brain"></i> Knowledge Engineering</span>
                    <span class="vertical-tag" title="Unity, Maya, UI/UX"><i class="fa-solid fa-palette"></i> Creative Media & Animation</span>
                    <span class="vertical-tag" title="MERN Stack, App Dev"><i class="fa-solid fa-code"></i> Full Stack Development</span>
                    <span class="vertical-tag" title="AWS, Azure, OCI"><i class="fa-solid fa-cloud"></i> Cloud Computing</span>
                    <span class="vertical-tag" title="Security, Pentesting"><i class="fa-solid fa-shield-halved"></i> Cyber Security & Privacy</span>
                    <span class="vertical-tag" title="NLP, Robotics, AR/VR"><i class="fa-solid fa-microchip"></i> Emerging Technologies</span>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>OFFICIAL SYLLABUS DOCUMENT</h3>
                <div class="glass-card-deep" style="text-align:center;">
                    <i class="fa-solid fa-file-pdf" style="font-size:4rem; color:#a31f24; margin-bottom:20px;"></i>
                    <p style="font-size:1.2rem; font-weight:700; color:#003366;">B.Tech AI&DS Full Syllabus (R2021)</p>
                    <a href="assets/aids/ai-ds.pdf" download class="pdf-btn-premium">Download Syllabus PDF</a>
                    <div style="margin-top:30px; border-radius:20px; overflow:hidden; box-shadow: 0 15px 50px rgba(0,0,0,0.25);">
                        <iframe src="assets/aids/ai-ds.pdf" width="100%" height="900px" style="border:none;"></iframe>
                    </div>
                </div>
            </section>
        ''',

        'aids_placement.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">PLACEMENT & TRAINING</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>3-YEAR STRATEGIC TRAINING ROADMAP</h3>
                <p>Derived from our "Placement and Training (PAT) Cell" vision for 2023-2025.</p>
                <div class="roadmap">
                    <div class="roadmap-step" data-aos="fade-right">
                        <div class="step-number">01</div>
                        <div class="step-content">
                            <h4>COMMUNICATION & CONFIDENCE (Year 1)</h4>
                            <p>Verbal listening, speaking labs, and English language proficiency to ensure every student can communicate effectively in a corporate environment.</p>
                        </div>
                    </div>
                    <div class="roadmap-step" data-aos="fade-right" data-aos-delay="100">
                        <div class="step-number">02</div>
                        <div class="step-content">
                            <h4>APTITUDE & PROBLEM SOLVING (Year 2)</h4>
                            <p>Concentrated training on Quantative Aptitude, Logical Reasoning, and First-principles thinking for pre-placement examinations.</p>
                        </div>
                    </div>
                    <div class="roadmap-step" data-aos="fade-right" data-aos-delay="200">
                        <div class="step-number">03</div>
                        <div class="step-content">
                            <h4>TECHNICAL MASTERY & CODING ETHICS (Year 3)</h4>
                            <p>Domain specialization (Java, Python, AI/ML), Real-time Industry tasks, and mini-projects guided by technical experts.</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>TOP INDUSTRIAL RECRUITERS</h3>
                <div class="grid-2">
                    <div class="glass-card-deep" style="display:flex; align-items:center; gap:25px;">
                        <i class="fa-solid fa-handshake" style="font-size:3.5rem; color:#a31f24;"></i>
                        <div>
                            <h4>GODB Tech On-Campus</h4>
                            <p>Recent high-impact hiring drive specifically for AI & Data Science roles.</p>
                        </div>
                    </div>
                    <div class="glass-card-deep" style="display:flex; align-items:center; gap:25px;">
                        <i class="fa-solid fa-city" style="font-size:3.5rem; color:#003366;"></i>
                        <div>
                            <h4>TIDEL Park & Mahindra World City</h4>
                            <p>Partnerships with software giants for software development and automated manufacturing roles.</p>
                        </div>
                    </div>
                </div>
                <div style="margin-top:25px; text-align:center;">
                     <a href="assets/aids/placement-report-22-23.pdf" download class="pdf-btn-premium">View Detailed Placement Report 2022-23</a>
                </div>
            </section>
        ''',

        'aids_internships.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">INDUSTRY CONNECT & VISITS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>DIRECT INDUSTRY EXPOSURE (INDUSTRIAL VISITS)</h3>
                <p>AI&DS students witness technology in action at premium manufacturing and software hubs:</p>
                <div class="grid-2">
                    <div class="visit-card" data-aos="flip-up">
                        <div class="visit-header"><span>TVS Sundram Fasteners</span> <i class="fa-solid fa-gears"></i></div>
                        <div class="visit-body"><p>Studied <strong>IoT applications</strong> in real-time manufacturing at Mahindra World City units.</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="100">
                        <div class="visit-header"><span>Codoid Innovations</span> <i class="fa-solid fa-code"></i></div>
                        <div class="visit-body"><p>Software Quality Assurance & QA automation framework analysis (TIDEL Park, Chennai).</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="200">
                        <div class="visit-header"><span>IIT Research Park</span> <i class="fa-solid fa-microchip"></i></div>
                        <div class="visit-body"><p>Exclusive visit to the <strong>Incubation Cell</strong> to explore the deep-tech startup ecosystem and Disruptive Tech.</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="300">
                        <div class="visit-header"><span>MSC Technology</span> <i class="fa-solid fa-ship"></i></div>
                        <div class="visit-body"><p>Exploring large-scale Enterprise Resource Planning (ERP) and global technology deployment.</p></div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PREMIUM INTERNSHIPS</h3>
                <div class="glass-card-deep" style="text-align:center; border-top: 6px solid #f89820;">
                    <i class="fa-brands fa-java" style="font-size:4.5rem; color:#f89820; margin-bottom:15px;"></i>
                    <h3 style="color:#a31f24; margin:0 0 10px 0; font-size:1.8rem; font-weight:900;">VEI TECHNOLOGIES</h3>
                    <h4 style="color:#003366; text-transform:uppercase; letter-spacing:1px;">Java Application Development Internship</h4>
                    <p style="font-size:1.1rem; color:#555;">Selected III Year Students: <strong>Suruthi I K, Swathi K, Thirisha N</strong></p>
                </div>
            </section>
        ''',

        'aids_coe.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CENTRE OF EXCELLENCE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>VALUE ADDED TRAINING CENTER</h3>
                <p>Bridging the Academia-Industry gap through specific high-demand technology certifications.</p>
                <div class="grid-3" style="margin-top:30px;">
                    <div class="stat-card" data-aos="fade-up" style="background:#fff5f5; border-top:5px solid #a31f24; padding:35px;">
                        <i class="fa-solid fa-robot" style="font-size:3rem; color:#a31f24; margin-bottom:15px;"></i>
                        <h4 style="margin:0;">Generative AI</h4>
                        <p style="font-size:0.85rem; color:#666; margin-top:5px;">Infosys Springboard Verified</p>
                    </div>
                    <div class="stat-card" data-aos="fade-up" data-aos-delay="100" style="background:#f0f8ff; border-top:5px solid #003366; padding:35px;">
                        <i class="fa-solid fa-database" style="font-size:3rem; color:#003366; margin-bottom:15px;"></i>
                        <h4 style="margin:0;">Oracle AI</h4>
                        <p style="font-size:0.85rem; color:#666; margin-top:5px;">Global Infrastructure Certification</p>
                    </div>
                    <div class="stat-card" data-aos="fade-up" data-aos-delay="200" style="background:#fffef0; border-top:5px solid gold; padding:35px;">
                        <i class="fa-solid fa-cubes-stacked" style="font-size:3rem; color:gold; margin-bottom:15px;"></i>
                        <h4 style="margin:0;">Blockchain</h4>
                        <p style="font-size:0.85rem; color:#666; margin-top:5px;">C-DAC Specialized Security Bootcamp</p>
                    </div>
                </div>
            </section>
        '''
    }

    # Generate the finalized pages
    for filename, content in pages.items():
        print(f"Generating Deep UI: {filename}...")
        final_html = header + content + footer
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

    print("SUCCESS: AI&DS High-Impact 'Deep' UI Updates Complete!")

if __name__ == "__main__":
    generate_aids()
