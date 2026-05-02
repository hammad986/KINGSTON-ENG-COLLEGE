import os
import re

base_dir = r"d:\clg website new"
template_path = os.path.join(base_dir, "about.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Update navigation globally for Placements
# We need to target the block containing "<!-- JS will populate 8 items -->" under "Placements"
nav_old = r'<ul class="dropdown">\s*<!-- JS will populate 8 items -->\s*</ul>'
nav_new = '''<ul class="dropdown js-exclude-dropdown">
                            <li><a href="placement_pat.html">Placement & Training Cell</a></li>
                            <li><a href="placement_vision_mission.html">Vision & Mission, Objectives</a></li>
                            <li><a href="placement_recruiters.html">Corporate Recruiters</a></li>
                            <li><a href="placement_report.html">Placement Report</a></li>
                            <li><a href="placement_industry_connect.html">Industry Connect</a></li>
                            <li><a href="placement_campus_hiring.html">Campus Hiring</a></li>
                            <li><a href="placement_value_added.html">Value added Courses Training</a></li>
                            <li><a href="placement_capacity_dev.html">Capacity Dev and Skill Dev</a></li>
                        </ul>'''

# Update template content in memory
template_content = re.sub(nav_old, nav_new, template_content)

core_pages = [
    "about.html", "index.html", "departments.html", "academics.html", 
    "facilities.html", "facilities_infrastructure.html",
    "about_chairman.html", "about_principal.html", "about_mou.html",
    "about_awards.html", "about_organogram.html", "about_governing.html",
    "about_accreditation.html"
]

for cp in core_pages:
    p = os.path.join(base_dir, cp)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as fCore:
            cData = fCore.read()
            cData = re.sub(nav_old, nav_new, cData)
        with open(p, 'w', encoding='utf-8') as fCore:
            fCore.write(cData)

# Extract header and footer
header_match = re.search(r'(<!DOCTYPE html>.*?<section class="about-hero-section">.*?<div class="hero-video-wrapper">.*?<video.*?</video>)', template_content, re.DOTALL)
header_part1 = header_match.group(1)

footer_match = re.search(r'(<footer class="main-footer">.*)', template_content, re.DOTALL)
footer_html = footer_match.group(1)

def get_page(title, content):
    hero_html = f'''
        <div class="hero-overlay" style="background:rgba(0,0,0,0.6);"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:10;flex-direction:column;pointer-events:none;">
            <h1 style="color:#fff;font-size:3.2rem;font-weight:800;letter-spacing:1px;text-shadow:0 2px 10px rgba(0,0,0,0.6);text-transform:uppercase;text-align:center;">{title}</h1>
        </div>
    </div>
    </section>
    '''
    return header_part1 + hero_html + content + footer_html

pages = {}

# 1. Placement & Training Cell
pages['placement_pat.html'] = get_page("Placement & Training Cell", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Department of Placement & Training</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="display:grid; grid-template-columns: 1fr; gap:40px;">
            <div style="background:#fff; padding:30px; border-radius:8px; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid #eaeaea;">
                <h3 style="font-size:1.4rem; color:#111; margin-bottom:15px; font-family:'Poppins',sans-serif;">Director Placement & Training</h3>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:14px; font-family:'Inter',sans-serif;">
                    More than 3 decades of experience in industry and institution, headed a sales team in software & training companies, Post graduated in Management studies, capable of identify the industry expectations from fresher engineers.
                </p>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:14px; font-family:'Inter',sans-serif;">
                    He has a good relationship network with various top level management peoples of various core engineering & software companies. In the last 13 years of experience as placement head in various institutes he placed nearly 5000+ fresh engineers & MBA’s in various corporate companies.
                </p>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:0; font-family:'Inter',sans-serif;">
                    He organized various industry visits for faculties, students in engineering, software companies and organized 100+ guest lecturers for the students from industry eminent technical, HR & Top level management peoples, for bridging the gap between the industry expectations from institutes. He received various awards for tremendous service, gave 100+ guest lectures and training for various college students, industry employees.
                </p>
            </div>
            
            <div style="background:#fff; padding:30px; border-radius:8px; box-shadow:0 4px 15px rgba(0,0,0,0.05); border:1px solid #eaeaea;">
                <h3 style="font-size:1.4rem; color:#111; margin-bottom:15px; font-family:'Poppins',sans-serif;">Assistant Placement Director</h3>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:14px; font-family:'Inter',sans-serif;">
                    Mechatronics Engineer and expertise in Human Resources Management with 17 years of excellence in Academics, Placements, Mentoring, people handling, and project management.
                </p>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:14px; font-family:'Inter',sans-serif;">
                    As a collaborative team player, he works on establishing the vital link between students and prospective employers to facilitate training and placement of students as they begin their career after graduation.
                </p>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:14px; font-family:'Inter',sans-serif;">
                    He motivate the students to develop technical knowledge & soft skills in terms of goal setting and also aspire for higher studies in the directions to take competitive exams.
                </p>
                <p style="font-size:0.97rem; line-height:1.85; color:#444; margin-bottom:0; font-family:'Inter',sans-serif;">
                    He prepare the students to meet the industries recruitment process and invites the reputed companies to the college for organizing campus placement session.
                </p>
            </div>
        </div>
    </div>
</section>
""")

# 2. Vision & Mission, Objectives
pages['placement_vision_mission.html'] = get_page("Vision & Mission, Objectives", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Vision Mission & Objectives</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="margin-bottom: 40px; background:#fdfdfd; padding:25px; border-left:4px solid #8b1a2b; box-shadow:0 3px 10px rgba(0,0,0,0.04);">
            <h3 style="font-size:1.5rem; color:#111; margin-bottom:12px; font-family:'Poppins',sans-serif;">Vision</h3>
            <p style="font-size:1rem; line-height:1.7; color:#444; font-family:'Inter',sans-serif;">To enhance the employability skills among the students to meet out the corporate expectations. All the students should get placed in the prospective IT, Core companies.</p>
        </div>
        
        <div style="margin-bottom: 40px; background:#fdfdfd; padding:25px; border-left:4px solid #8b1a2b; box-shadow:0 3px 10px rgba(0,0,0,0.04);">
            <h3 style="font-size:1.5rem; color:#111; margin-bottom:12px; font-family:'Poppins',sans-serif;">Mission</h3>
            <p style="font-size:1rem; line-height:1.7; color:#444; font-family:'Inter',sans-serif;">To create opportunities for the placements, opportunity for each & all students in the job market create a rapport with the industry people.</p>
        </div>
        
        <div style="margin-bottom: 40px;">
            <h3 style="font-size:1.5rem; color:#111; margin-bottom:15px; font-family:'Poppins',sans-serif;">AIM of PAT (Placement and Training) CELL</h3>
            <ul style="list-style-type:disc; padding-left:20px; font-size:1rem; line-height:1.8; color:#444; font-family:'Inter',sans-serif;">
                <li style="margin-bottom:8px;">Placement cell provide guidance to the students for selecting right career path.</li>
                <li style="margin-bottom:8px;">Assist the students to improve their skills set as per industry need, expectations.</li>
                <li style="margin-bottom:8px;">PAT Team more connected with the industry team (Technical & Recruitment).</li>
                <li style="margin-bottom:8px;">Organizing more pre placement seminars, motivational lectures, bringing industry peoples and organizes the technical lectures to transform "How the Curriculum contents applied in Industry".</li>
            </ul>
        </div>
        
        <div style="margin-bottom: 40px;">
            <h3 style="font-size:1.5rem; color:#111; margin-bottom:15px; font-family:'Poppins',sans-serif;">Training and Development</h3>
            <p style="font-size:1rem; line-height:1.8; color:#444; margin-bottom:15px; font-family:'Inter',sans-serif;">Kingston engineering College, takes various initiatives for the students with the best career opportunities. The college has appointed in house well qualified, experienced technical & soft skill trainers, transform the skills as industry expected way, and organize various campus recruitment drives which students get placed in various national, multinational companies with high salary packages.</p>
            <p style="font-size:1rem; line-height:1.8; color:#444; font-family:'Inter',sans-serif;">We started training from their first year, started with verbal communication skills and strengthening the student’s confidence to communicate through English, we have a dedicated lab for virtual verbal listening and speaking skills. In the second year of training we concentrate only on aptitude, problem solving skills, in the third year full of technical skill transformation training, based on the students interested domain, full freedom to the students to choose their interested domain and we are supporting them to achieve good heights with good confidence and without stress.</p>
        </div>
    </div>
</section>
""")

# 3. Corporate Recruiters
pages['placement_recruiters.html'] = get_page("Corporate Recruiters", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Corporate Recruiters</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <ul style="column-count: 2; column-gap: 40px; list-style: disc; padding-left: 20px; color: #444; font-size:1rem; line-height:1.8; font-family:'Inter',sans-serif;">
            <li style="margin-bottom:10px;">CODOID SYSTEMS, TIDEL PARK, CHENNAI</li>
            <li style="margin-bottom:10px;">RELEVANTZ TECHONOLOGY SERVICES, CHENNAI</li>
            <li style="margin-bottom:10px;">AIR MEDIA BROADCAST SOLUTIONS (P), LTD, COIMBATORE</li>
            <li style="margin-bottom:10px;">TOP FRESHERS TECHNOLOGIES.PVT.LTD, CHENNAI</li>
            <li style="margin-bottom:10px;">PRIMETEC AUTOMOTIVE PARTS PVT LTD, CHENNAI</li>
            <li style="margin-bottom:10px;">MILKYWAY CELL TECH, CHENNAI</li>
            <li style="margin-bottom:10px;">CAPARO ENGINEERING INDIA LIMITED, CHENNAI</li>
            <li style="margin-bottom:10px;">CRUD OPERATION PRIVATED LIMITED, CHENNAI</li>
            <li style="margin-bottom:10px;">METRO COMPOSITES, CHENNAI</li>
            <li style="margin-bottom:10px;">AVEON INFOTECH PRIVATE LIMITED, COIMBATORE</li>
            <li style="margin-bottom:10px;">TECHFULLY.PVT.LTD, BANGALORE</li>
            <li style="margin-bottom:10px;">EVR ELECTRICALS PRIVATE LTD, CHENNAI</li>
            <li style="margin-bottom:10px;">INFOGRO TECHNOLOGY, CHENNAI</li>
            <li style="margin-bottom:10px;">SHREE ABIRAMI ENGINEERING PRIVATE LIMITED, CHENNAI</li>
            <li style="margin-bottom:10px;">SELVI SOFTWARE TECHNOLOGIES PVT LTD, VELLORE</li>
            <li style="margin-bottom:10px;">KAASHIV INFOTECH, CHENNAI</li>
            <li style="margin-bottom:10px;">SHIA#SH INFO SOLUTION PRIVATE LIMITED, CHENNAI</li>
            <li style="margin-bottom:10px;">ICE STEEL1 INDIA PVT LTD, RANIPET</li>
            <li style="margin-bottom:10px;">IMS LEARNING RESOURCE PRIVATE LTD, VELLORE</li>
            <li style="margin-bottom:10px;">DIGIDOC SOLUTIONS, VELLORE</li>
            <li style="margin-bottom:10px;">FOCUS LOGIC IT SERVICES, RANIPET</li>
            <li style="margin-bottom:10px;">FACT ENTRY DATA SOLUTIONS, VELLORE</li>
            <li style="margin-bottom:10px;">VIS EDUCATION AND TRAINING COMPANY, VELLORE</li>
            <li style="margin-bottom:10px;">NITTR, Chennai</li>
            <li style="margin-bottom:10px;">TechByHeart, Kochi</li>
            <li style="margin-bottom:10px;">VEI’s technologies, Chennai</li>
        </ul>
    </div>
</section>
""")

# 4. Placement Report
pages['placement_report.html'] = get_page("Placement Report", """
<style>
.report-card { background:#fff; border:1px solid #ddd; padding:25px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; box-shadow:0 3px 10px rgba(0,0,0,0.03); transition:all 0.3s; }
.report-card:hover { transform:translateY(-3px); box-shadow:0 8px 15px rgba(0,0,0,0.08); border-color:#8b1a2b; }
.report-title { font-size:1.2rem; font-weight:700; color:#111; font-family:'Poppins',sans-serif; }
.report-btn { background:#8b1a2b; color:#fff; padding:10px 20px; border-radius:4px; text-decoration:none; font-weight:600; font-family:'Poppins',sans-serif; font-size:0.9rem; transition:background 0.3s; }
.report-btn:hover { background:#6a1120; color:#fff; }
</style>
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Placement Report</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:30px;"></div>
        
        <p style="font-size:1rem; line-height:1.8; color:#444; margin-bottom:40px; font-family:'Inter',sans-serif;">
            In the last five years, organized 300+ industry experts guest lecturers, from technical & HR’s heads, identifying the skill gap of the students and train them so that they meet the expectation of prospective employers. To guide the students in all possible ways, so they get confidence to face the interviews and get placed in their dream companies that will give them opportunities for growth and development.
        </p>

        <div style="max-width:800px;">
            <div class="report-card">
                <div class="report-title">2022-2023 Report</div>
                <a href="#" class="report-btn">View Detail</a>
            </div>
            <div class="report-card">
                <div class="report-title">2021-2022 Report</div>
                <a href="#" class="report-btn">View Detail</a>
            </div>
            <div class="report-card">
                <div class="report-title">2020-2021 Report</div>
                <a href="#" class="report-btn">View Detail</a>
            </div>
            <div class="report-card">
                <div class="report-title">2019-2020 Report</div>
                <a href="#" class="report-btn">View Detail</a>
            </div>
            <div class="report-card">
                <div class="report-title">2018-2019 Report</div>
                <a href="#" class="report-btn">View Detail</a>
            </div>
        </div>
    </div>
</section>
""")

# 5. Industry Connect
pages['placement_industry_connect.html'] = get_page("Industry Connect", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Industry Connect</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <p style="font-size:1.05rem; line-height:1.8; color:#444; margin-bottom:20px; font-family:'Inter',sans-serif;">
            We are closely connected with various industries and getting their real time problems in technology, business models and employee engagements, our faculties discussing these task’s with the students assist them for getting real time positive outcomes, we organize regular industry visits for our faculties then the experience will be transform to the students before taking them to the industries for visit.
        </p>
        <p style="font-size:1.05rem; line-height:1.8; color:#444; margin-bottom:20px; font-family:'Inter',sans-serif;">
            Our students are undergoing internship training programmes only from the industries in our tie up, signed a MoU with more than 50 industries in various domain.
        </p>
        <p style="font-size:1.05rem; line-height:1.8; color:#444; margin-bottom:40px; font-family:'Inter',sans-serif;">
            Our faculties are providing training session to the industries and NGO’s based on their requirements like (Updation in technology, in service training, personality development, time management etc.
        </p>

        <h3 style="font-size:1.6rem; font-weight:700; color:#111; margin-bottom:20px; font-family:'Poppins',sans-serif;">Industry Sponsored</h3>
        <p style="font-size:1.05rem; line-height:1.8; color:#444; margin-bottom:15px; font-family:'Inter',sans-serif;">
            Major automotive industries sponsored their products for conduct real time knowledge transforming training, research activities:
        </p>
        
        <ul style="list-style-type:disc; padding-left:25px; color: #444; font-size:1rem; line-height:1.8; font-family:'Inter',sans-serif; margin-bottom:30px;">
            <li style="margin-bottom:12px;"><strong>Hyundai</strong> – Sponsored CRETA CAR worth of 10Lacks,</li>
            <li style="margin-bottom:12px;"><strong>Renault Nissan</strong> - Sponsored Dutsun CAR with one spare engine, our students undergo the research and covert the petrol vehicle as E Vehicle.</li>
            <li style="margin-bottom:12px;"><strong>FORD</strong> –Sponsored ECO SPORTS CAR for training & Development.</li>
            <li style="margin-bottom:12px;"><strong>TATA Motors</strong> – sponsored a Yodha Utility vehicle, additional BS VI engine and complete wiring harness set for showcase in laboratory. They also conducted virtual training to the students about the architecture of particular vehicle.</li>
            <li style="margin-bottom:12px;"><strong>TEXMO Group (Aquasub Engineering)</strong> – Sponsored submersible pump motor for the students training & Development, they provide industry visit and career opportunity for the students.</li>
            <li style="margin-bottom:12px;"><strong>MSC Technology India Pvt Ltd</strong> - Worlds top level logistics and shipping companies technology division – Sponsored 25 latest computer system CPU, for setup collaboration skill development centre at Kingston, for develop latest technology training as per industry standard leads to CENTRE OF EXCELLENCE to our institution, They provide more guest lectures and industry visits in every semester for software engineering departments, through this initiative good number of our students got an opportunities in MSC Technology India Pvt Ltd.</li>
        </ul>
    </div>
</section>
""")

# 6. Campus Hiring (PDF)
pages['placement_campus_hiring.html'] = get_page("Campus Hiring", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Campus Hiring</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="width:100%; height:900px; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.15); border:1px solid #ddd;">
            <iframe src="assets/pdfs/placement/campus-hiring.pdf" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
</section>
""")

# 7. Value added Courses Training (PDF)
pages['placement_value_added.html'] = get_page("Value added Courses Training", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Value added Courses Training</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="width:100%; height:900px; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.15); border:1px solid #ddd;">
            <iframe src="assets/pdfs/placement/value-added-training-course.pdf" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
</section>
""")

# 8. Capacity Development and Skill Development (PDF)
pages['placement_capacity_dev.html'] = get_page("Capacity & Skill Development", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Capacity Development and Skill Development</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="width:100%; height:900px; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.15); border:1px solid #ddd;">
            <iframe src="assets/pdfs/placement/capacity-development.pdf" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
</section>
""")

# Write all pages
for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(pages)} Placement pages and updated navigation globally.")
