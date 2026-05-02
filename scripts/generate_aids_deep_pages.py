import os

# Define the highly animated AI&DS department pages with deep analysis from PDF data.

pages = {
    'dept_aids.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">B.TECH. ARTIFICIAL INTELLIGENCE & DATA SCIENCE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>ABOUT THE DEPARTMENT</h3>
                <div class="glass-card-ai">
                    <p>The Department of Artificial Intelligence and Data Science was established to create a new generation of data-driven specialists. Our curriculum, derived from the <strong>Anna University R2021 Regulation</strong>, is designed to provide deep expertise in Machine Learning, Deep Learning, Big Data, and IoT.</p>
                    <p>Our focus is on solving "wicked societal problems" using theoretical knowledge and practical industrial tools.</p>
                </div>
                <div class="grid-3" style="margin-top:20px;">
                    <div class="stat-card" data-aos="zoom-in" data-aos-delay="100">
                        <h2 style="color:#a31f24; margin:0;">2021</h2>
                        <p style="font-size:0.8rem; margin:0;">Year Established</p>
                    </div>
                    <div class="stat-card" data-aos="zoom-in" data-aos-delay="200">
                        <h2 style="color:#a31f24; margin:0;">R2021</h2>
                        <p style="font-size:0.8rem; margin:0;">Regulation</p>
                    </div>
                    <div class="stat-card" data-aos="zoom-in" data-aos-delay="300">
                        <h2 style="color:#a31f24; margin:0;">100%</h2>
                        <p style="font-size:0.8rem; margin:0;">Curriculum Mapping</p>
                    </div>
                </div>
            </section>
    ''',

    'aids_curriculum.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CURRICULUM & VERTICALS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ACADEMIC JOURNEY (ANNA UNIVERSITY R2021)</h3>
                <p>The AI&DS curriculum is structured into 8 semesters of rigorous analytical and engineering studies.</p>
                <div class="sem-grid">
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="100"><h4>Semester I</h4><p>Matrices, Python Programming, Physics, Chemistry</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="150"><h4>Semester II</h4><p>Data Structures, Statistics & Numerical Methods, Graphics</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="200"><h4>Semester III</h4><p>Artificial Intelligence, Algorithms, Database Management</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="250"><h4>Semester IV</h4><p>Machine Learning, Data Science & Analytics, Networks</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="300"><h4>Semester V</h4><p>Deep Learning, Big Data Analytics, Cloud Computing</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="350"><h4>Semester VI</h4><p>Embedded Systems, IoT, Professional Electives</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="400"><h4>Semester VII</h4><p>Human Values & Ethics, Open Electives</p></div>
                    <div class="sem-card" data-aos="zoom-in" data-aos-delay="450"><h4>Semester VIII</h4><p>Final Year Project Work / Industry Internship</p></div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROFESSIONAL ELECTIVE VERTICALS (SPECIALIZATIONS)</h3>
                <p>Our curriculum offers 6 specialized clusters (Verticals) to tailor your technical career:</p>
                <div class="vertical-box">
                    <span class="vertical-tag" title="Specialized AI Knowledge"><i class="fa-solid fa-brain"></i> Knowledge Engineering</span>
                    <span class="vertical-tag" title="UI/UX & Graphics"><i class="fa-solid fa-palette"></i> Creative Media</span>
                    <span class="vertical-tag" title="Modern App Development"><i class="fa-solid fa-code"></i> Full Stack Development</span>
                    <span class="vertical-tag" title="Cloud Infra"><i class="fa-solid fa-cloud"></i> Cloud Computing</span>
                    <span class="vertical-tag" title="Data Security"><i class="fa-solid fa-shield-halved"></i> Cyber Security & Privacy</span>
                    <span class="vertical-tag" title="ML & Robotics"><i class="fa-solid fa-microchip"></i> Emerging Technologies</span>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>SYLLABUS DOWNLOAD</h3>
                <div class="glass-card-ai" style="text-align:center;">
                    <i class="fa-solid fa-file-pdf" style="font-size:3.5rem; color:#a31f24; margin-bottom:15px;"></i>
                    <p style="font-weight:700;">Full B.Tech AI&DS Syllabus (R2021)</p>
                    <a href="assets/aids/ai-ds.pdf" download class="pdf-btn">Download Syllabus PDF</a>
                    <div style="margin-top:20px; border-radius:15px; overflow:hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
                        <iframe src="assets/aids/ai-ds.pdf" width="100%" height="800px"></iframe>
                    </div>
                </div>
            </section>
    ''',

    'aids_placement.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">PLACEMENT & TRAINING</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>3nd YEAR STRATEGIC TRAINING ROADMAP</h3>
                <div class="roadmap">
                    <div class="roadmap-step" data-aos="fade-right">
                        <div class="step-number">Y1</div>
                        <div class="step-content">
                            <h4>COMMUNICATION & CONFIDENCE</h4>
                            <p>Verbal listening, speaking labs, and English language proficiency training to build workplace self-confidence from Day 1.</p>
                        </div>
                    </div>
                    <div class="roadmap-step" data-aos="fade-right" data-aos-delay="100">
                        <div class="step-number">Y2</div>
                        <div class="step-content">
                            <h4>APTITUDE & ANALYTICAL REASONING</h4>
                            <p>Intensive training in Mathematical Aptitude, Logical Reasoning, and Problem-Solving abilities required for pre-placement tests.</p>
                        </div>
                    </div>
                    <div class="roadmap-step" data-aos="fade-right" data-aos-delay="200">
                        <div class="step-number">Y3</div>
                        <div class="step-content">
                            <h4>TECHNICAL DOMAIN MASTERY</h4>
                            <p>Deep specialization in AI, Java, Python, and Industry coding ethics. Real-time project implementation and coding bootcamps.</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>TOP INDUSTRIAL RECRUITERS & HIRING</h3>
                <div class="grid-2">
                    <div class="glass-card-ai" style="display:flex; align-items:center; gap:20px;">
                        <i class="fa-solid fa-handshake" style="font-size:3rem; color:#a31f24;"></i>
                        <div>
                            <h4>GODB Tech Hiring</h4>
                            <p>Recent on-campus hiring drive for AI-specific roles and Data Analyst positions.</p>
                        </div>
                    </div>
                    <div class="glass-card-ai" style="display:flex; align-items:center; gap:20px;">
                        <i class="fa-solid fa-industry" style="font-size:3rem; color:#003366;"></i>
                        <div>
                            <h4>Core IT Partnerships</h4>
                            <p>Strong connections with software giants at TIDEL Park and firms in Mahindra World City.</p>
                        </div>
                    </div>
                </div>
                <div style="margin-top:20px;">
                     <a href="assets/aids/placement-report-22-23.pdf" download class="pdf-btn">View Full Placement Report 2022-23</a>
                </div>
            </section>
    ''',

    'aids_internships.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">INDUSTRY CONNECT & VISITS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>REAL-WORLD EXPOSURE (INDUSTRIAL VISITS)</h3>
                <p>AI&DS department ensures students witness technology in action through periodic visits:</p>
                <div class="grid-2">
                    <div class="visit-card" data-aos="flip-up">
                        <div class="visit-header"><span>TVS Sundram Fasteners</span> <i class="fa-solid fa-gears"></i></div>
                        <div class="visit-body"><p>Studied <strong>IoT implementation</strong> in real-time manufacturing at Mahindra World City units.</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="100">
                        <div class="visit-header"><span>Codoid Innovations</span> <i class="fa-solid fa-laptop-code"></i></div>
                        <div class="visit-body"><p>Software Quality Assurance & QA automation framework analysis (TIDEL Park, Chennai).</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="200">
                        <div class="visit-header"><span>IIT Research Park</span> <i class="fa-solid fa-microchip"></i></div>
                        <div class="visit-body"><p>Faculty & Student visit to the <strong>Incubation Cell</strong> to explore the deep-tech startup ecosystem.</p></div>
                    </div>
                    <div class="visit-card" data-aos="flip-up" data-aos-delay="300">
                        <div class="visit-header"><span>MSC Technology</span> <i class="fa-solid fa-shuttle-space"></i></div>
                        <div class="visit-body"><p>Deep dive into large-scale logistics software and global technology deployment strategies.</p></div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>FEATURED INDUSTRY INTERNSHIPS</h3>
                <div class="glass-card-ai" style="text-align:center; border-top: 5px solid #f89820;">
                    <i class="fa-brands fa-java" style="font-size:4rem; color:#f89820; margin-bottom:15px;"></i>
                    <h3 style="color:#a31f24; margin:0 0 10px 0;">VEI TECHNOLOGIES</h3>
                    <h4 style="color:#003366;">Java Application Development</h4>
                    <p>Selected Students: <strong>Suruthi I K</strong>, <strong>Swathi K</strong>, <strong>Thirisha N</strong> (III Year AI&DS)</p>
                </div>
            </section>
    ''',

    'aids_coe.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CENTRE OF EXCELLENCE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>VALUE ADDED TRAINING CENTER</h3>
                <p>Bridging the gap between the syllabus and the industry through global certifications.</p>
                <div class="grid-3" style="margin-top:20px;">
                    <div class="stat-card" data-aos="fade-up" style="background:#fdf5f5; border-top:4px solid #a31f24;">
                        <i class="fa-solid fa-robot" style="font-size:2.5rem; color:#a31f24; margin-bottom:10px;"></i>
                        <h4>Generative AI</h4>
                        <p style="font-size:0.8rem; color:#666;">Infosys Springboard Verified</p>
                    </div>
                    <div class="stat-card" data-aos="fade-up" data-aos-delay="100" style="background:#f0f7ff; border-top:4px solid #003366;">
                        <i class="fa-solid fa-database" style="font-size:2.5rem; color:#003366; margin-bottom:10px;"></i>
                        <h4>Oracle AI</h4>
                        <p style="font-size:0.8rem; color:#666;">Global OCI Certification</p>
                    </div>
                    <div class="stat-card" data-aos="fade-up" data-aos-delay="200" style="background:#fffaf0; border-top:4px solid gold;">
                        <i class="fa-solid fa-cubes" style="font-size:2.5rem; color:gold; margin-bottom:10px;"></i>
                        <h4>Blockchain</h4>
                        <p style="font-size:0.8rem; color:#666;">C-DAC Specialized Bootcamp</p>
                    </div>
                </div>
            </section>
    ''',

    'aids_vision_mission.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">VISION AND MISSION</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="glass-card-ai" style="border-left: 10px solid #a31f24; background:rgba(163,31,36,0.05);">
                    <h3 style="color:#a31f24; margin-top:0;">DEPARTMENT VISION</h3>
                    <p style="font-style:italic; font-size:1.1rem;">"To evolve AI based efficient domain specific processes for effective decision making and to arrive at actionable foresight, insight, and hindsight from data for solving business and engineering problems."</p>
                </div>
                <div class="glass-card-ai" style="border-left: 10px solid #003366; background:rgba(0,51,102,0.05); margin-top:25px;">
                    <h3 style="color:#003366; margin-top:0;">DEPARTMENT MISSION</h3>
                    <ul style="list-style:none; padding:0;">
                        <li style="margin-bottom:15px; display:flex; gap:10px;"><i class="fa-solid fa-circle-check" style="color:#a31f24; margin-top:5px;"></i> <span>Utilize proficiencies in basic sciences, mathematics, and AI/DS to build systems that require management and analysis of large volumes of data.</span></li>
                        <li style="margin-bottom:15px; display:flex; gap:10px;"><i class="fa-solid fa-circle-check" style="color:#a31f24; margin-top:5px;"></i> <span>Advance technical skills to pursue pioneering research in the field of AI and Data Science for the welfare of ecosystems.</span></li>
                        <li style="margin-bottom:15px; display:flex; gap:10px;"><i class="fa-solid fa-circle-check" style="color:#a31f24; margin-top:5px;"></i> <span>Collaborative and ethical attitude in multidisciplinary teams with innovative thoughts for economy building.</span></li>
                    </ul>
                </div>
            </section>
    ''',
}

# Sidebar nav is embedded directly to ensure it doesn't fail
aids_sidebar_nav = """        <aside class="dept-sidebar">
            <ul class="dept-sidebar-menu">
                <li><a href="aids_about.html"><i class="fa-solid fa-house"></i> About the Department</a></li>
                <li><a href="aids_vision_mission.html"><i class="fa-solid fa-bullseye"></i> Vision and Mission</a></li>
                <li><a href="aids_peos_pos.html"><i class="fa-regular fa-file-lines"></i> PEOs, POs & PSOs</a></li>
                <li><a href="aids_faculty.html"><i class="fa-solid fa-user-tie"></i> Faculty</a></li>
                <li><a href="aids_board_of_studies.html"><i class="fa-solid fa-graduation-cap"></i> Board of Studies</a></li>
                <li><a href="aids_curriculum.html"><i class="fa-solid fa-book-open"></i> Curriculum & Verticals</a></li>
                <li><a href="aids_academic_calendar.html"><i class="fa-regular fa-calendar-days"></i> Academic Calendar</a></li>
                <li><a href="aids_timetable.html"><i class="fa-solid fa-table-cells"></i> Time Table</a></li>
                <li><a href="aids_coe.html"><i class="fa-solid fa-trophy"></i> Centre of Excellence</a></li>
                <li><a href="aids_faculty_achievements.html"><i class="fa-solid fa-medal"></i> Faculty Certifications</a></li>
                <li><a href="aids_events.html"><i class="fa-regular fa-calendar-check"></i> Events & FDPs</a></li>
                <li><a href="aids_student_workshops.html"><i class="fa-solid fa-laptop-code"></i> Student Workshops</a></li>
                <li><a href="aids_internships.html"><i class="fa-solid fa-briefcase"></i> Internships & Industry</a></li>
                <li><a href="aids_sports.html"><i class="fa-solid fa-person-running"></i> Sports Achievements</a></li>
                <li><a href="aids_toppers.html"><i class="fa-solid fa-award"></i> Toppers List</a></li>
                <li><a href="aids_placement.html"><i class="fa-solid fa-building"></i> Placement & Training</a></li>
                <li><a href="aids_newsletter.html"><i class="fa-regular fa-newspaper"></i> Newsletters & Magazines</a></li>
                <li><a href="aids_contact.html"><i class="fa-solid fa-envelope"></i> Contact Us</a></li>
            </ul>
        </aside>"""

# Custom CSS for the deep analysis updates
extra_styles = """
<style>
.sem-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 20px; }
.sem-card { background: white; padding: 20px; border-radius: 12px; border-bottom: 5px solid #a31f24; box-shadow: 0 5px 15px rgba(0,0,0,0.08); transition: 0.3s; cursor: pointer; }
.sem-card:hover { transform: translateY(-7px); background: #a31f24; color: white; border-bottom-color: gold; }
.sem-card h4 { margin: 0; font-size: 1.1rem; }
.sem-card p { margin: 5px 0 0; font-size: 0.8rem; opacity: 0.8; }

.vertical-box { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; background: #003366; padding: 25px; border-radius: 15px; }
.vertical-tag { background: rgba(255,255,255,0.1); color: white; padding: 10px 22px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.2); font-weight: 500; font-size: 0.9rem; transition: 0.3s; cursor:help; }
.vertical-tag:hover { background: gold; color: #a31f24; transform: scale(1.1); box-shadow: 0 0 15px gold; }

.roadmap { position: relative; padding: 30px 0; border-left: 3px dashed #a31f24; margin-left: 30px; }
.roadmap-step { display: flex; gap: 20px; margin-bottom: 40px; position: relative; margin-left: -32px; }
.step-number { width: 64px; height: 64px; background: #a31f24; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.5rem; box-shadow: 0 0 20px rgba(163,31,36,0.3); z-index: 5; }
.step-content { background: #fdf5f5; padding: 25px; border-radius: 15px; flex-grow: 1; border: 1px solid #eee; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }

.visit-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 8px 20px rgba(0,0,0,0.08); transition: 0.4s; }
.visit-card:hover { transform: scale(1.03); box-shadow: 0 15px 40px rgba(0,0,0,0.12); }
.visit-header { background: #003366; color: white; padding: 15px 25px; display: flex; justify-content: space-between; font-weight: 600; font-size: 1.1rem; }
.visit-body { padding: 20px; font-size: 0.95rem; color: #444; line-height: 1.6; }

.pdf-btn { display: inline-block; margin-top: 15px; padding: 14px 28px; background: #a31f24; color: white !important; font-weight: 700; border-radius: 10px; transition: 0.3s; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem; border: none; cursor: pointer; }
.pdf-btn:hover { background: #003366; transform: scale(1.05); box-shadow: 0 5px 20px rgba(0,51,102,0.3); }

/* Standard UI from previous pages for continuity */
.glass-card-ai { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); padding: 30px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
.stat-card { background: white; padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 20px rgba(0,0,0,0.05); transition: 0.3s; }
.stat-card:hover { transform: translateY(-5px); }
</style>
"""

# Base layout (Get the standard header/footer from dept_aids.html)
base_file = "dept_aids.html"
with open(base_file, "r", encoding="utf-8") as f:
    base_html = f.read()

# Separate the common header/sidebar and footer
# We assume the main content is inside <div class="dept-main-content">
parts = base_html.split('<div class="dept-main-content">')
header_part = parts[0] + '<div class="dept-main-content">\n'
footer_part = '</div>\n' + base_html.split('</div><!-- End of dept-main-content -->')[1]

# Inject the styles into header_part
if "</style>" in header_part:
    header_part = header_part.replace("</style>", extra_styles + "\n</style>")
else:
    header_part = header_part.replace("</head>", extra_styles + "\n</head>")

# Apply the sidebar update (if needed, but usually it's already there)
# If sidebar needs replacement:
# header_part = re.sub(r'<aside class="dept-sidebar">.*?</aside>', aids_sidebar_nav, header_part, flags=re.DOTALL)

# Generate Deep pages
for filename, content in pages.items():
    print(f"Generating Deep UI: {filename}...")
    final_html = header_part + content + footer_part
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)

print("SUCCESS: AI&DS High-Impact 'Deep Analysis' UI Generation Complete!")
