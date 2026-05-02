import os
import re

base_dir = r"d:\clg website new"
template_path = os.path.join(base_dir, "about.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Update navigation globally for IQAC
nav_old = r'<ul class="dropdown js-exclude-dropdown">\s*<li><a href="iqac_about\.html">IQAC</a></li>.*?<li><a href="iqac_strategic_plan\.html">Strategic Plan 2024</a></li>\s*</ul>'
nav_new = '''<ul class="dropdown js-exclude-dropdown">
                            <li><a href="iqac_about.html">IQAC</a></li>
                            <li><a href="iqac_mom.html">Minutes of Meeting</a></li>
                            <li><a href="iqac_quality_initiatives.html">IQAC Quality Initiatives</a></li>
                            <li><a href="iqac_annual_reports.html">Annual Reports</a></li>
                            <li><a href="iqac_academic_audit.html">Academic Audit</a></li>
                            <li><a href="iqac_feedback.html">Feedback</a></li>
                            <li><a href="iqac_strategic_plan.html">Strategic Plan 2024</a></li>
                        </ul>'''

template_content = re.sub(nav_old, nav_new, template_content)

core_pages = [
    "about.html", "index.html", "departments.html", "academics.html", 
    "facilities.html", "facilities_infrastructure.html",
    "about_chairman.html", "about_principal.html", "about_mou.html",
    "about_awards.html", "about_organogram.html", "about_governing.html",
    "about_accreditation.html",
    "placement_pat.html", "placement_vision_mission.html", "placement_recruiters.html",
    "placement_report.html", "placement_industry_connect.html", "placement_campus_hiring.html",
    "placement_value_added.html", "placement_capacity_dev.html"
]

for cp in core_pages:
    p = os.path.join(base_dir, cp)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as fCore:
            cData = fCore.read()
            cData = re.sub(nav_old, nav_new, cData, flags=re.DOTALL)
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
            <h1 style="color:#fff;font-size:3.5rem;font-weight:900;letter-spacing:2px;text-shadow:0 4px 15px rgba(0,0,0,0.8);text-transform:uppercase;text-align:center;">{title}</h1>
            <div style="width:100px; height:4px; background:#fff; margin-top:15px; border-radius:2px;"></div>
        </div>
    </div>
    </section>
    '''
    return header_part1 + hero_html + content + footer_html

pages = {}

# 1. IQAC (About)
pages['iqac_about.html'] = get_page("IQAC", """
<style>
.iqac-card { background:#fff; padding:40px; border-radius:20px; box-shadow:0 10px 40px rgba(0,0,0,0.06); transition:all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); border-top:6px solid #8b1a2b; position:relative; overflow:hidden; z-index:1;}
.iqac-card:hover { transform:translateY(-15px); box-shadow:0 20px 50px rgba(139,26,43,0.15); }
.iqac-icon { font-size:3.5rem; color:#8b1a2b; margin-bottom:25px; display:inline-block; }
.card-bg-icon { position:absolute; right:-20px; bottom:-30px; font-size:12rem; color:#f4f4f4; z-index:-1; transition:all 0.6s ease; opacity:0.6;}
.iqac-card:hover .card-bg-icon { transform:scale(1.2) rotate(-15deg); color:#eee; }
.iqac-title { font-size:1.6rem; font-weight:800; color:#111; font-family:'Poppins',sans-serif; margin-bottom:20px; text-transform:uppercase; letter-spacing:1px; }
.iqac-text { font-size:1.05rem; line-height:1.9; color:#555; font-family:'Inter',sans-serif; margin-bottom:0; }
.list-group { list-style:none; padding:0; margin:0; }
.list-group li { position:relative; padding-left:35px; margin-bottom:15px; font-size:1.05rem; line-height:1.8; color:#444; font-family:'Inter',sans-serif; }
.list-group li::before { content:'\\f058'; font-family:'Font Awesome 5 Free'; font-weight:900; position:absolute; left:0; top:0; color:#8b1a2b; font-size:1.3rem; }
</style>
<section class="page-section" style="padding: 100px 0; background:linear-gradient(to bottom, #ffffff, #f9f9f9);">
    <div class="container">
        <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:70px;">
            <h1 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">Internal Quality Assurance Cell <span style="color:#8b1a2b;">(IQAC)</span></h1>
            <div style="width:120px; height:4px; background:#8b1a2b; margin:0 auto; border-radius:2px;"></div>
        </div>
        
        <div style="background:#fff; padding:50px; border-radius:20px; box-shadow:0 15px 50px rgba(0,0,0,0.06); margin-bottom:60px;" data-aos="zoom-in" data-aos-duration="1000">
            <h3 style="font-size:1.8rem; font-weight:700; color:#111; margin-bottom:20px; font-family:'Poppins',sans-serif; border-left:5px solid #8b1a2b; padding-left:15px;">About IQAC</h3>
            <p style="font-size:1.1rem; line-height:1.9; color:#444; font-family:'Inter',sans-serif; margin-bottom:0;">
                In pursuance of the IQAC action plan for the performance evaluation, assessment & accreditation, and quality up-gradation of institutions' higher education, NAAC proposes every accredited institution should establish an Internal Quality Assurance Cell (IQAC) as a post-accreditation quality sustenance measure. Since quality enhancement is a continuous process, the IQAC will become a part of the institution’s system & work towards the realisation of the goals of quality enhancement & sustenance. The prime task of the IQAC is to develop a system for conscious, consistent and catalytic improvement in the overall performance of the institution. For this, during the post-accreditation period, it channelizes all efforts and measures of the institution towards promoting its holistic academic excellence.
            </p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(400px, 1fr)); gap:40px; margin-bottom:60px;">
            <div class="iqac-card" data-aos="fade-up" data-aos-delay="100">
                <i class="fas fa-gem card-bg-icon"></i>
                <div class="iqac-icon"><i class="fas fa-star"></i></div>
                <h3 class="iqac-title">Quality Policy</h3>
                <p class="iqac-text">To establish and implement a robust quality system at Kingston Engineering College, encircling teaching, learning, research, and self-reliance, focusing on core and support functions to ensure accountability to stakeholders through continuous improvement and sustenance towards promoting holistic academic excellence.</p>
            </div>
            
            <div class="iqac-card" data-aos="fade-up" data-aos-delay="200">
                <i class="fas fa-bullseye card-bg-icon"></i>
                <div class="iqac-icon"><i class="fas fa-crosshairs"></i></div>
                <h3 class="iqac-title">Objectives</h3>
                <ul class="list-group">
                    <li>To facilitate the creation of a learner-centric environment conducive to quality education imparted in an institution.</li>
                    <li>To provide a sound basis for decision making imbibing all the dimensions of service quality to improve institutional functioning and towards quality enhancement through the best practices.</li>
                </ul>
            </div>
        </div>
        
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(450px, 1fr)); gap:40px;">
            <div class="iqac-card" style="border-top-color:#1e3c72;" data-aos="fade-right">
                <i class="fas fa-cogs card-bg-icon"></i>
                <div class="iqac-icon" style="color:#1e3c72;"><i class="fas fa-chess-knight"></i></div>
                <h3 class="iqac-title" style="color:#1e3c72;">Strategies</h3>
                <ul class="list-group">
                    <li style="color:#555;">Ensuring timely, efficient and progressive performance of academic, administrative and financial tasks.</li>
                    <li style="color:#555;">Equitable access to and affordability of academic programmes for various sections of society.</li>
                    <li style="color:#555;">Optimization and integration of modern methods of teaching and learning.</li>
                    <li style="color:#555;">Ensuring the adequacy, maintenance and functioning of the support structure and services.</li>
                    <li style="color:#555;">Sharing of Research and networking with other institutions in India and abroad.</li>
                </ul>
            </div>
            
            <div class="iqac-card" style="border-top-color:#e67e22;" data-aos="fade-left">
                <i class="fas fa-project-diagram card-bg-icon"></i>
                <div class="iqac-icon" style="color:#e67e22;"><i class="fas fa-sitemap"></i></div>
                <h3 class="iqac-title" style="color:#e67e22;">Functions</h3>
                <ul class="list-group">
                    <li style="color:#555;">Development and application of quality benchmarks/parameters.</li>
                    <li style="color:#555;">Analysis for feedback response from stakeholders on quality-related processes.</li>
                    <li style="color:#555;">Organization of inter and intra-institutional workshops, seminars on quality.</li>
                    <li style="color:#555;">Documentation of the various programmes/activities.</li>
                    <li style="color:#555;">Acting as a nodal agency of the Institution for coordinating activities.</li>
                    <li style="color:#555;">Preparation of the Annual Quality Assurance Report (AQAR) as per guidelines.</li>
                </ul>
            </div>
        </div>
    </div>
</section>
""")

# 2. Minutes of Meeting
pages['iqac_mom.html'] = get_page("Minutes of Meeting", """
<style>
.doc-card { display:flex; flex-direction:column; align-items:center; background:#fff; padding:40px 20px; border-radius:20px; box-shadow:0 15px 35px rgba(0,0,0,0.06); transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); text-decoration:none; color:#333; position:relative; overflow:hidden;}
.doc-card::before { content:''; position:absolute; top:0; left:0; width:100%; height:5px; background:linear-gradient(90deg, #8b1a2b, #d9534f); transform:scaleX(0); transform-origin:left; transition:transform 0.4s; }
.doc-card:hover { transform:translateY(-12px); box-shadow:0 25px 50px rgba(139,26,43,0.15); }
.doc-card:hover::before { transform:scaleX(1); }
.doc-icon { font-size:4.5rem; color:#8b1a2b; margin-bottom:25px; filter:drop-shadow(0 8px 10px rgba(139,26,43,0.2)); transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.doc-card:hover .doc-icon { transform:scale(1.15) rotate(5deg); }
.doc-title { font-size:1.3rem; font-weight:800; font-family:'Poppins',sans-serif; text-align:center; margin-bottom:20px; color:#222;}
.doc-btn { padding:12px 30px; border-radius:30px; background:#f4f4f4; color:#8b1a2b; font-size:0.95rem; font-weight:700; letter-spacing:1px; border:2px solid transparent; text-transform:uppercase; font-family:'Inter',sans-serif; transition:all 0.4s; display:flex; align-items:center; gap:8px;}
.doc-card:hover .doc-btn { background:#8b1a2b; color:#fff; padding-left:40px; padding-right:40px; box-shadow:0 8px 20px rgba(139,26,43,0.3);}
</style>
<section class="page-section" style="padding: 100px 0; background:#f5f7fa;">
    <div class="container">
        <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:70px;">
            <h1 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">Minutes Of <span style="color:#8b1a2b;">Meeting</span></h1>
            <div style="width:120px; height:4px; background:#8b1a2b; margin:0 auto; border-radius:2px;"></div>
        </div>
        
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:40px;">
            <a href="assets/pdfs/iqac/assets_pdf_mom_1.%20MOM%20-%202021-22.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="100">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2021-22 (Part 1)</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_mom_2.%20MOM%20-%202021-22.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="200">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2021-22 (Part 2)</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_mom_3.%20MOM%20-%202022-23.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="300">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2022-23 (Part 1)</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_mom_4.%20MOM%20-%202022-23.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="400">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2022-23 (Part 2)</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_mom_5.%20MOM%20-%202022-23.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="500">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2022-23 (Part 3)</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_mom_6.%20MOM%20-%202023-24.pdf" target="_blank" class="doc-card" data-aos="zoom-in" data-aos-delay="600">
                <i class="fas fa-file-pdf doc-icon"></i>
                <div class="doc-title">MOM - 2023-24</div>
                <div class="doc-btn">View Detail <i class="fas fa-arrow-right"></i></div>
            </a>
        </div>
    </div>
</section>
""")

# 3. Quality Initiatives
pages['iqac_quality_initiatives.html'] = get_page("IQAC Quality Initiatives", """
<style>
.accordion-wrapper { max-width:900px; margin:0 auto; }
.acc-item { background:#fff; margin-bottom:20px; border-radius:15px; box-shadow:0 8px 25px rgba(0,0,0,0.05); overflow:hidden; transition:all 0.3s; border-left:4px solid #8b1a2b;}
.acc-item:hover { box-shadow:0 12px 35px rgba(0,0,0,0.08); transform:translateX(5px); }
.acc-header { padding:25px 30px; display:flex; justify-content:space-between; align-items:center; cursor:pointer; font-family:'Poppins',sans-serif; font-size:1.3rem; font-weight:700; color:#111; user-select:none; }
.acc-header i { font-size:1.5rem; color:#8b1a2b; transition:transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.acc-content { padding:0 30px; max-height:0; overflow:hidden; transition:max-height 0.4s ease, padding 0.4s ease; background:#fafafa; font-family:'Inter',sans-serif; color:#555; line-height:1.8; font-size:1rem; }
.acc-item.active .acc-header i { transform:rotate(180deg); color:#e74c3c; }
.acc-item.active .acc-content { padding:25px 30px; max-height:1000px; border-top:1px solid #eee; }
.empty-data { text-align:center; padding:30px; color:#888; font-style:italic;}
</style>
<section class="page-section" style="padding: 100px 0; background:#fdfdfd;">
    <div class="container">
        <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:70px;">
            <h1 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">Programs Organized <span style="display:block; font-size:1.4rem; color:#8b1a2b; margin-top:10px; font-weight:600;">With Internal Quality Assurance Cell</span></h1>
            <div style="width:120px; height:4px; background:#8b1a2b; margin:0 auto; border-radius:2px;"></div>
        </div>
        
        <div class="accordion-wrapper">
            <div class="acc-item" data-aos="fade-up" data-aos-delay="100">
                <div class="acc-header" onclick="this.parentElement.classList.toggle('active')">
                    Academic Year: 2023 - 2024 <i class="fas fa-chevron-down"></i>
                </div>
                <div class="acc-content">
                    <ul style="list-style:none; padding-left:0; margin:0;">
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">04.12.2023:</strong> "Adolescent Nutrition - Second Window of Opportunity", Dr. R. Anitha, Assistant Professor, Department of Food & Nutrition, Muthurangam Government Arts College, Vellore.</li>
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">21.03.2024 To 25.03.2024:</strong> Five Days FDP on "Exploring Frontiers of AI Computing & Technologies (EFACT'24)", Mrs. Jothi Naik (Msc Technologies), Mr. N. Jerrys (AtoS), Mr. K. Sathish Kumar (BGENT).</li>
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">14.09.2023 & 15.09.2023:</strong> "Two days Technology Outreach Programme". Resources: Dr. Bhaskaran Raman (IIT Bombay), Dr. Jayakumar L (NIT Agartala), Mr. Harishanker Selvaraj (GUVI), Mr. V. Kumbakarnan.</li>
                    </ul>
                </div>
            </div>
            
            <div class="acc-item" data-aos="fade-up" data-aos-delay="200">
                <div class="acc-header" onclick="this.parentElement.classList.toggle('active')">
                    Academic Year: 2022 - 2023 <i class="fas fa-chevron-down"></i>
                </div>
                <div class="acc-content">
                    <ul style="list-style:none; padding-left:0; margin:0;">
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">06.08.2022:</strong> Virtual Mentorship on "Roadmap from Academic to Corporate Skills", Ms. Yuvashree A.K (Accenture).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">23.09.2022 & 24.09.2022:</strong> "Two days Hands on Training on Embedded Systems", Mr. K. Agilan (FLDEC Systems).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">09.09.2022:</strong> Workshop on "Health and Happiness - Art of Living", Dr. Chandrasekaran Kuppan & Ms. Venkateswari Solaimalai.</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">30.09.2022:</strong> Workshop on "Machine Learning with Rapidminer", Dr. M. Venkatesan (NIT Puducherry).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">13.10.2022:</strong> Virtual session on "Investor Awareness program", Mr. A. Ashwin Umayorubahan (NSE India).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">15.10.2022:</strong> Webinar on "Placement, Career Planning & Advancement", Ms. Lingapoorani (TCS).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">09.11.2022:</strong> "Energy conservation towards unsustainable development goals", Dr. L. Ramesh & Dr. S. Madan Kumar.</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">19.11.2022:</strong> Workshop on "Navigating the Entrepreneurial Ecosystem", Dr. U.V. Arivazhagu (Principal, KEC).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">03.12.2022:</strong> Guest Lecture on "Emotional And Verbal Abuse", Mrs. Ramaaharan (PoSH Trainer).</li>
                         <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">27.02.2023:</strong> Guest Lecture on "Evolution of Mobility of Electric Vehicle", Mr. G. Sam Moses (Hyundai).</li>
                    </ul>
                </div>
            </div>
            
            <div class="acc-item" data-aos="fade-up" data-aos-delay="300">
                <div class="acc-header" onclick="this.parentElement.classList.toggle('active')">
                    Academic Year: 2021 - 2022 <i class="fas fa-chevron-down"></i>
                </div>
                <div class="acc-content">
                    <ul style="list-style:none; padding-left:0; margin:0;">
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">28.01.2022:</strong> Webinar on "Multiple views of Career Development", Ms. Hemasri R (Cognizant).</li>
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">29.01.2022:</strong> Workshop on "NAAC Assessment and Accreditation process", Dr. N. Alagumurthi (PEC).</li>
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">26.02.2022:</strong> "Responding to the Needs of Adolescents", Dr. Beulah Emmanuel (APCA).</li>
                        <li style="margin-bottom:15px; padding:15px; background:#fcf4f5; border-left:4px solid #8b1a2b; border-radius:4px;"><strong style="color:#8b1a2b;">16.04.2022:</strong> Webinar on "Intellectual Property Rights", Shri. Lakshmi Narayanan (Examiner of Patents & Designs).</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</section>
""")

# 4. Annual Reports
pages['iqac_annual_reports.html'] = get_page("Annual Reports", """
<style>
.ar-card { display:flex; align-items:center; background:#fff; padding:30px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.05); margin-bottom:25px; transition:all 0.4s; border:1px solid #f0f0f0; text-decoration:none;}
.ar-card:hover { transform:scale(1.03) translateX(10px); box-shadow:0 15px 40px rgba(139,26,43,0.1); border-color:#8b1a2b; }
.ar-icon { width:80px; height:80px; border-radius:50%; background:#fef0f2; display:flex; justify-content:center; align-items:center; font-size:2.5rem; color:#8b1a2b; margin-right:30px; transition:all 0.4s; flex-shrink:0;}
.ar-card:hover .ar-icon { background:#8b1a2b; color:#fff; transform:rotate(-15deg); }
.ar-info { flex-grow:1; }
.ar-title { font-size:1.5rem; font-weight:700; font-family:'Poppins',sans-serif; color:#111; margin-bottom:8px; }
.ar-sub { font-size:1rem; color:#777; font-family:'Inter',sans-serif; }
.ar-action { background:#111; color:#fff; padding:10px 25px; border-radius:30px; font-weight:600; font-family:'Inter',sans-serif; font-size:0.9rem; transition:all 0.3s; }
.ar-card:hover .ar-action { background:#8b1a2b; padding-right:35px; }
</style>
<section class="page-section" style="padding: 100px 0; background:#fbfcff;">
    <div class="container" style="max-width:900px;">
        <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:70px;">
            <h1 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">Annual <span style="color:#8b1a2b;">Reports</span></h1>
            <div style="width:120px; height:4px; background:#8b1a2b; margin:0 auto; border-radius:2px;"></div>
        </div>
        
        <a href="assets/pdfs/iqac/assets_pdf_ar_AR-2022-2023.pdf" target="_blank" class="ar-card" data-aos="fade-up" data-aos-delay="100">
            <div class="ar-icon"><i class="fas fa-chart-line"></i></div>
            <div class="ar-info">
                <div class="ar-title">AR 2022 - 2023</div>
                <div class="ar-sub">Annual Report for the Academic Year</div>
            </div>
            <div class="ar-action">View Report <i class="fas fa-external-link-alt" style="margin-left:5px;"></i></div>
        </a>
        <a href="assets/pdfs/iqac/assets_pdf_ar_AR-2021-2022.pdf" target="_blank" class="ar-card" data-aos="fade-up" data-aos-delay="200">
            <div class="ar-icon"><i class="fas fa-chart-line"></i></div>
            <div class="ar-info">
                <div class="ar-title">AR 2021 - 2022</div>
                <div class="ar-sub">Annual Report for the Academic Year</div>
            </div>
            <div class="ar-action">View Report <i class="fas fa-external-link-alt" style="margin-left:5px;"></i></div>
        </a>
        <a href="assets/pdfs/iqac/assets_pdf_ar_AR-2020-2021.pdf" target="_blank" class="ar-card" data-aos="fade-up" data-aos-delay="300">
            <div class="ar-icon"><i class="fas fa-chart-line"></i></div>
            <div class="ar-info">
                <div class="ar-title">AR 2020 - 2021</div>
                <div class="ar-sub">Annual Report for the Academic Year</div>
            </div>
            <div class="ar-action">View Report <i class="fas fa-external-link-alt" style="margin-left:5px;"></i></div>
        </a>
        <a href="assets/pdfs/iqac/assets_pdf_ar_AR-2019-2020.pdf" target="_blank" class="ar-card" data-aos="fade-up" data-aos-delay="400">
            <div class="ar-icon"><i class="fas fa-chart-line"></i></div>
            <div class="ar-info">
                <div class="ar-title">AR 2019 - 2020</div>
                <div class="ar-sub">Annual Report for the Academic Year</div>
            </div>
            <div class="ar-action">View Report <i class="fas fa-external-link-alt" style="margin-left:5px;"></i></div>
        </a>
        <a href="assets/pdfs/iqac/assets_pdf_ar_AR-2018-2019.pdf" target="_blank" class="ar-card" data-aos="fade-up" data-aos-delay="500">
            <div class="ar-icon"><i class="fas fa-chart-line"></i></div>
            <div class="ar-info">
                <div class="ar-title">AR 2018 - 2019</div>
                <div class="ar-sub">Annual Report for the Academic Year</div>
            </div>
            <div class="ar-action">View Report <i class="fas fa-external-link-alt" style="margin-left:5px;"></i></div>
        </a>
    </div>
</section>
""")

# 5. Academic Audit
pages['iqac_academic_audit.html'] = get_page("Academic Audit", """
<style>
.audit-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:30px; }
.audit-card { background:linear-gradient(135deg, #8b1a2b 0%, #4a0d16 100%); padding:40px 30px; border-radius:20px; text-align:center; color:#fff; text-decoration:none; box-shadow:0 15px 35px rgba(139,26,43,0.3); transition:all 0.5s; position:relative; overflow:hidden;}
.audit-card::after { content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%; background:radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 60%); opacity:0; transition:opacity 0.5s; transform:scale(0.5); }
.audit-card:hover { transform:translateY(-15px) scale(1.05); box-shadow:0 25px 50px rgba(139,26,43,0.5); }
.audit-card:hover::after { opacity:1; transform:scale(1); }
.audit-icon { font-size:3.5rem; margin-bottom:20px; color:rgba(255,255,255,0.9); }
.audit-title { font-size:1.6rem; font-weight:800; font-family:'Poppins',sans-serif; margin-bottom:15px; letter-spacing:1px; position:relative; z-index:1;}
.audit-btn { background:#fff; color:#8b1a2b; display:inline-block; padding:8px 25px; border-radius:30px; font-weight:700; font-size:0.9rem; font-family:'Inter',sans-serif; position:relative; z-index:1; transition:all 0.3s;}
.audit-card:hover .audit-btn { background:#111; color:#fff; }
</style>
<section class="page-section" style="padding: 100px 0; background:#fff;">
    <div class="container">
        <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:70px;">
            <h1 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">Academic <span style="color:#8b1a2b;">Audit</span></h1>
            <div style="width:120px; height:4px; background:#8b1a2b; margin:0 auto; border-radius:2px;"></div>
        </div>
        
        <div class="audit-grid">
            <a href="assets/pdfs/iqac/assets_pdf_academic-audit_2022-2023.pdf" target="_blank" class="audit-card" data-aos="zoom-in" data-aos-delay="100">
                <i class="fas fa-search-dollar audit-icon"></i>
                <div class="audit-title">2022 - 2023</div>
                <div class="audit-btn">View Detail</div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_academic-audit_2021-2022.pdf" target="_blank" class="audit-card" data-aos="zoom-in" data-aos-delay="200">
                <i class="fas fa-search-dollar audit-icon"></i>
                <div class="audit-title">2021 - 2022</div>
                <div class="audit-btn">View Detail</div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_academic-audit_2020-2021.pdf" target="_blank" class="audit-card" data-aos="zoom-in" data-aos-delay="300">
                <i class="fas fa-search-dollar audit-icon"></i>
                <div class="audit-title">2020 - 2021</div>
                <div class="audit-btn">View Detail</div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_academic-audit_2019-2020.pdf" target="_blank" class="audit-card" data-aos="zoom-in" data-aos-delay="400">
                <i class="fas fa-search-dollar audit-icon"></i>
                <div class="audit-title">2019 - 2020</div>
                <div class="audit-btn">View Detail</div>
            </a>
            <a href="assets/pdfs/iqac/assets_pdf_academic-audit_2018-2019.pdf" target="_blank" class="audit-card" data-aos="zoom-in" data-aos-delay="500">
                <i class="fas fa-search-dollar audit-icon"></i>
                <div class="audit-title">2018 - 2019</div>
                <div class="audit-btn">View Detail</div>
            </a>
        </div>
    </div>
</section>
""")

# 6. Feedback
pages['iqac_feedback.html'] = get_page("Feedback", """
<style>
.feedback-pill { display:flex; align-items:center; background:#fff; padding:15px 25px; border-radius:50px; text-decoration:none; color:#333; font-weight:700; font-family:'Inter',sans-serif; font-size:1rem; box-shadow:0 8px 20px rgba(0,0,0,0.06); transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); border:2px solid transparent; }
.feedback-pill i { font-size:1.3rem; margin-right:15px; color:#fff; background:linear-gradient(135deg, #8b1a2b, #e74c3c); padding:12px; border-radius:50%; transition:all 0.4s; box-shadow:0 4px 10px rgba(231,76,60,0.3);}
.feedback-pill:hover { background:linear-gradient(135deg, #8b1a2b, #4a0d16); color:#fff; transform:translateY(-8px); box-shadow:0 15px 30px rgba(139,26,43,0.3); border-color:rgba(255,255,255,0.2);}
.feedback-pill:hover i { background:#fff; color:#8b1a2b; box-shadow:none; transform:rotate(15deg) scale(1.1);}

.report-list-item { display:flex; justify-content:space-between; align-items:center; background:#fff; padding:25px 35px; border-radius:15px; margin-bottom:20px; border-left:5px solid #8b1a2b; box-shadow:0 8px 25px rgba(0,0,0,0.04); transition:all 0.4s; overflow:hidden; position:relative;}
.report-list-item::after { content:''; position:absolute; right:0; top:0; height:100%; width:0%; background:#fcf4f5; z-index:0; transition:width 0.4s ease; }
.report-list-item:hover { transform:translateX(15px); box-shadow:0 12px 30px rgba(139,26,43,0.1); border-left-width:10px;}
.report-list-item:hover::after { width:100%; }
.report-name { font-size:1.2rem; font-weight:700; font-family:'Poppins',sans-serif; color:#222; position:relative; z-index:1;}
.report-link { display:inline-flex; align-items:center; background:#111; color:#fff; padding:10px 20px; border-radius:30px; font-weight:600; text-decoration:none; font-family:'Inter',sans-serif; font-size:0.9rem; transition:all 0.3s; position:relative; z-index:1;}
.report-link i { margin-left:8px; transition:transform 0.3s; }
.report-list-item:hover .report-link { background:#8b1a2b; padding-right:25px; }
.report-list-item:hover .report-link i { transform:translateX(5px); }
</style>
<section class="page-section" style="padding: 100px 0; background:#f5f7fa;">
    <div class="container">
        
        <div class="row" style="margin-bottom:80px;">
            <div class="col-12" data-aos="fade-down">
                <h2 style="font-family:'Poppins',sans-serif; font-size:2.2rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase; border-bottom:4px solid #8b1a2b; display:inline-block; padding-bottom:10px;">Submit Feedback</h2>
            </div>
            
            <div class="col-12" style="margin-top:40px;">
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:30px;">
                    <a href="https://forms.gle/FcmyuydGaXiBWY66A" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="100">
                        <i class="fas fa-user-graduate"></i> Alumni Feedback Form
                    </a>
                    <a href="https://forms.gle/UCRiYj5Vz1u8ShHd8" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="150">
                        <i class="fas fa-user-friends"></i> Parents Feedback on Curriculum
                    </a>
                    <a href="https://forms.gle/vucmjBFSxzdcoUo97" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="200">
                        <i class="fas fa-briefcase"></i> Employer Feedback Form
                    </a>
                    <a href="https://forms.gle/L46n4DZRD1wE3A5w8" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="250">
                        <i class="fas fa-book-open"></i> Students Feedback on Curriculum
                    </a>
                    <a href="https://forms.gle/qMrnrvL1by2iqudp7" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="300">
                        <i class="fas fa-building"></i> Students Feedback on Facilities
                    </a>
                    <a href="https://forms.gle/aumrEvLxtuv9hqkr9" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="350">
                        <i class="fas fa-chalkboard-teacher"></i> Faculty Feedback Form
                    </a>
                    <a href="https://forms.gle/oGxcJ9aWL6HjmiTX6" target="_blank" class="feedback-pill" data-aos="zoom-in" data-aos-delay="400">
                        <i class="fas fa-bed"></i> Hostellers feedback on Facilities
                    </a>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-6" style="margin-bottom:50px;">
                <h2 style="font-family:'Poppins',sans-serif; font-size:1.8rem; font-weight:800; color:#111; margin-bottom:30px; text-transform:uppercase; border-bottom:4px solid #8b1a2b; display:inline-block; padding-bottom:10px;" data-aos="fade-right">Feedback Analysis Report</h2>
                
                <div data-aos="fade-up" data-aos-delay="100">
                    <div class="report-list-item">
                        <span class="report-name">Analysis 2022 - 2023</span>
                        <a href="assets/pdfs/iqac/engineering-resources_iqac_feedback-analysis-report_FB-22-23.pdf" target="_blank" class="report-link">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item">
                        <span class="report-name">Analysis 2021 - 2022</span>
                        <a href="assets/pdfs/iqac/engineering-resources_iqac_feedback-analysis-report_FB-21-22.pdf" target="_blank" class="report-link">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item">
                        <span class="report-name">Analysis 2020 - 2021</span>
                        <a href="assets/pdfs/iqac/engineering-resources_iqac_feedback-analysis-report_FB-20-21.pdf" target="_blank" class="report-link">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item">
                        <span class="report-name">Analysis 2019 - 2020</span>
                        <a href="assets/pdfs/iqac/engineering-resources_iqac_feedback-analysis-report_FB-19-20.pdf" target="_blank" class="report-link">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item">
                        <span class="report-name">Analysis 2018 - 2019</span>
                        <a href="assets/pdfs/iqac/engineering-resources_iqac_feedback-analysis-report_FB-18-19.pdf" target="_blank" class="report-link">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-6">
                <h2 style="font-family:'Poppins',sans-serif; font-size:1.8rem; font-weight:800; color:#111; margin-bottom:30px; text-transform:uppercase; border-bottom:4px solid #222; display:inline-block; padding-bottom:10px;" data-aos="fade-left">Action Taken Report</h2>
                
                <div data-aos="fade-up" data-aos-delay="200">
                    <div class="report-list-item" style="border-left-color:#222;">
                        <span class="report-name">Report 2022 - 2023</span>
                        <a href="assets/pdfs/iqac/assets_pdf_iqac_action-taken-report_AC-22-23.pdf" target="_blank" class="report-link" style="background:#8b1a2b;">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item" style="border-left-color:#222;">
                        <span class="report-name">Report 2021 - 2022</span>
                        <a href="assets/pdfs/iqac/assets_pdf_iqac_action-taken-report_AC-21-22.pdf" target="_blank" class="report-link" style="background:#8b1a2b;">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item" style="border-left-color:#222;">
                        <span class="report-name">Report 2020 - 2021</span>
                        <a href="assets/pdfs/iqac/assets_pdf_iqac_action-taken-report_AC-20-21.pdf" target="_blank" class="report-link" style="background:#8b1a2b;">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item" style="border-left-color:#222;">
                        <span class="report-name">Report 2019 - 2020</span>
                        <a href="assets/pdfs/iqac/assets_pdf_iqac_action-taken-report_AC-19-20.pdf" target="_blank" class="report-link" style="background:#8b1a2b;">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                    <div class="report-list-item" style="border-left-color:#222;">
                        <span class="report-name">Report 2018 - 2019</span>
                        <a href="assets/pdfs/iqac/assets_pdf_iqac_action-taken-report_AC-18-19.pdf" target="_blank" class="report-link" style="background:#8b1a2b;">View Detail <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
""")

# 7. Strategic Plan 2024
pages['iqac_strategic_plan.html'] = get_page("Strategic Plan 2024", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Strategic Plan 2024</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="width:100%; height:900px; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.15); border:1px solid #ddd;">
            <iframe src="assets/pdfs/iqac/assets_pdf_strategic-plan-2024.pdf" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
</section>
""")

# Write all pages
for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(pages)} highly animated IQAC pages and updated navigation globally.")
