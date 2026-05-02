import os
import re

base_dir = r"d:\clg website new"
template_path = os.path.join(base_dir, "about.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Update navigation globally for NAAC
nav_old = r'<li class="has-dropdown">\s*<a href="#">NAAC</a>\s*<ul class="dropdown[^>]*">.*?</ul>\s*</li>'
nav_new = '''<li class="has-dropdown">
                        <a href="#">NAAC</a>
                        <ul class="dropdown js-exclude-dropdown">
                            <li><a href="naac_iiqa.html">IIQA</a></li>
                            <li><a href="naac_ssr.html">SSR</a></li>
                            <li><a href="naac_dvv.html">DVV Clarification</a></li>
                            <li><a href="naac_rti.html">RTI</a></li>
                            <li><a href="naac_extended_profile.html">Extended Profile</a></li>
                            <li><a href="naac_curricular_aspects.html">Curricular Aspects</a></li>
                            <li><a href="naac_teaching_learning.html">Teaching Learning and Evaluation</a></li>
                            <li><a href="naac_research_innovation.html">Research Innovation and Extension</a></li>
                            <li><a href="naac_infrastructure.html">Infrastructure and Learning Resource</a></li>
                            <li><a href="naac_student_support.html">Student Support Progression</a></li>
                            <li><a href="naac_governance.html">Governance, Leadership and Management</a></li>
                            <li><a href="naac_institutional_values.html">Institution Values and Best Practices</a></li>
                        </ul>
                    </li>'''

template_content = re.sub(nav_old, nav_new, template_content, flags=re.DOTALL)

core_pages = [
    "about.html", "index.html", "departments.html", "academics.html", 
    "facilities.html", "facilities_infrastructure.html",
    "about_chairman.html", "about_principal.html", "about_mou.html",
    "about_awards.html", "about_organogram.html", "about_governing.html",
    "about_accreditation.html",
    "placement_pat.html", "placement_vision_mission.html", "placement_recruiters.html",
    "placement_report.html", "placement_industry_connect.html", "placement_campus_hiring.html",
    "placement_value_added.html", "placement_capacity_dev.html",
    "iqac_about.html", "iqac_mom.html", "iqac_quality_initiatives.html",
    "iqac_annual_reports.html", "iqac_academic_audit.html", "iqac_feedback.html",
    "iqac_strategic_plan.html"
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
        <div class="hero-overlay" style="background:rgba(0,0,0,0.65);"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:10;flex-direction:column;pointer-events:none;">
            <div style="padding:10px 25px; background:rgba(139,26,43,0.8); border-radius:30px; margin-bottom:15px; font-weight:700; color:#fff; font-family:'Poppins',sans-serif; letter-spacing:1px; font-size:1rem; backdrop-filter:blur(5px); display:flex; align-items:center; gap:8px;">
                <i class="fas fa-shield-alt"></i> NAAC ACCREDITATION
            </div>
            <h1 style="color:#fff;font-size:3.5rem;font-weight:900;letter-spacing:1px;text-shadow:0 10px 30px rgba(0,0,0,0.8);text-transform:uppercase;text-align:center;">{title}</h1>
            <div style="width:120px; height:5px; background:linear-gradient(90deg, #fff, transparent); margin-top:20px; border-radius:3px;"></div>
        </div>
    </div>
    </section>
    '''
    return header_part1 + hero_html + content + footer_html

def get_pdf_page(url):
    return f'''
    <section class="page-section" style="padding: 60px 0; background:#f4f7f6;">
        <div class="container" data-aos="fade-up">
            <div style="width:100%; height:900px; border-radius:15px; overflow:hidden; box-shadow:0 15px 50px rgba(0,0,0,0.1); border:1px solid #ddd; position:relative; z-index:5;">
                <iframe src="{url}" width="100%" height="100%" style="border:none;"></iframe>
            </div>
        </div>
    </section>
    '''

def get_metrics_grid(metrics):
    cards_html = ""
    for idx, (text, url) in enumerate(metrics.items()):
        delay = (idx % 4) * 100
        cards_html += f'''
        <a href="{url}" target="_blank" class="metric-card" data-aos="fade-up" data-aos-delay="{delay}">
            <div class="metric-number">
                <i class="fas fa-file-invoice" style="margin-right:8px; font-size:1.2rem; opacity:0.8;"></i>
                Evidence Document
            </div>
            <div class="metric-text">{text}</div>
            <div class="metric-action">
                View Evidence <i class="fas fa-arrow-right"></i>
            </div>
        </a>
        '''
    
    return f'''
    <style>
    .metrics-container {{ padding:80px 0; background:#fafafa; position:relative; overflow:hidden; }}
    .metrics-container::before {{ content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%; background:radial-gradient(circle, rgba(139,26,43,0.02) 0%, transparent 60%); z-index:0; pointer-events:none; }}
    .metric-grid {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(350px, 1fr)); gap:35px; position:relative; z-index:1; }}
    .metric-card {{ background:#fff; border-radius:16px; padding:35px 30px; display:flex; flex-direction:column; box-shadow:0 10px 30px rgba(0,0,0,0.04); border-left:6px solid #8b1a2b; border-bottom:1px solid #eee; border-top:1px solid #eee; border-right:1px solid #eee; transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); text-decoration:none; position:relative; overflow:hidden; }}
    .metric-card::after {{ content:''; position:absolute; right:-20px; top:-20px; width:100px; height:100px; background:radial-gradient(circle, rgba(139,26,43,0.05) 0%, transparent 70%); border-radius:50%; transition:all 0.4s; }}
    .metric-card:hover {{ transform:translateY(-12px); box-shadow:0 20px 40px rgba(139,26,43,0.1); border-left-width:10px; }}
    .metric-card:hover::after {{ transform:scale(2); opacity:0; }}
    .metric-number {{ font-family:'Poppins',sans-serif; color:#8b1a2b; font-weight:800; font-size:0.9rem; margin-bottom:15px; display:flex; align-items:center; text-transform:uppercase; letter-spacing:1px; }}
    .metric-text {{ font-family:'Inter',sans-serif; color:#333; font-size:1.05rem; line-height:1.7; flex-grow:1; margin-bottom:25px; }}
    .metric-action {{ background:#f8f9fa; color:#8b1a2b; padding:12px 20px; border-radius:8px; font-weight:700; font-family:'Inter',sans-serif; font-size:0.9rem; display:flex; justify-content:space-between; align-items:center; transition:all 0.3s; }}
    .metric-card:hover .metric-action {{ background:#8b1a2b; color:#fff; padding-left:25px; }}
    .metric-card:hover .metric-action i {{ transform:translateX(5px); }}
    </style>
    <section class="metrics-container">
        <div class="container">
            <div class="metric-grid">
                {cards_html}
            </div>
        </div>
    </section>
    '''

pages = {}

# PDF Pages
pages['naac_iiqa.html'] = get_page("IIQA", get_pdf_page("assets/pdfs/naac/assets_pdf_naac_IIQA.pdf"))
pages['naac_ssr.html'] = get_page("SSR", get_pdf_page("assets/pdfs/naac/assets_pdf_naac_ssr-new.pdf"))
pages['naac_dvv.html'] = get_page("DVV Clarification", get_pdf_page("assets/pdfs/naac/engineering-resources_dvv_DVV-001_dvv-clarifications-link.pdf"))
pages['naac_rti.html'] = get_page("RTI", get_pdf_page("assets/pdfs/naac/engineering-resources_naac_rti.pdf"))

# Criteria Pages
# 1. Extended Profile
ext_prof_metrics = {
    "Number of students year wise during the last five years": "assets/pdfs/naac/engineering-resources_naac_extended-profile_1.1_front-sheet.pdf",
    "Number of full-time teachers’ year wise during the last five years (2.1)": "assets/pdfs/naac/engineering-resources_naac_extended-profile_2.1_front-sheet.pdf",
    "Number of full-time teachers’ year wise during the last five years (2.2)": "assets/pdfs/naac/engineering-resources_naac_extended-profile_2.2_front-sheet.pdf",
    "Expenditure excluding salary component year wise during the last five years": "assets/pdfs/naac/engineering-resources_naac_extended-profile_3.1_front-sheet.pdf"
}
pages['naac_extended_profile.html'] = get_page("Extended Profile", get_metrics_grid(ext_prof_metrics))

# 2. Curricular Aspects
curr_asp_metrics = {
    "The Institution ensures effective curriculum planning and delivery through a well-planned and documented process including Academic calendar and conduct of continuous internal Assessment": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.1_front-sheet.pdf",
    "Number of Certificate/Value added courses offered and online courses of MOOCs, SWAYAM, NPTEL etc. where the students of the institution have enrolled and successfully completed during the last five years": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.2.1_front-sheet.pdf",
    "Percentage of students enrolled in Certificate/ Value added courses and also completed online courses of MOOCs, SWAYAM, NPTEL etc. as against the total number of students during the last five years": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.2.2_front-sheet.pdf",
    "Institution integrates crosscutting issues relevant to Professional Ethics, Gender, Human Values, Environment and Sustainability in transacting the Curriculum": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.3.1_front-sheet.pdf",
    "Percentage of students undertaking project work/field work/ internships (Data for the latest completed academic year)": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.3.2_front-sheet.pdf",
    "Institution obtains feedback on the academic performance and ambience of the institution from various stakeholders, such as Students, Teachers, Employers, Alumni etc. and action taken report on the feedback is made available on institutional website": "assets/pdfs/naac/engineering-resources_naac_curricular-aspects_1.4.1_front-sheet.pdf"
}
pages['naac_curricular_aspects.html'] = get_page("Curricular Aspects", get_metrics_grid(curr_asp_metrics))

# 3. Teaching Learning and Evaluation
teach_learn_metrics = {
    "Enrolment percentage": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.1.1_front-sheet.pdf",
    "Percentage of seats filled against reserved categories (SC, ST, OBC etc.) as per applicable reservation policy for the first-year admission during the last five years": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.1.2_front-sheet.pdf",
    "Student – Full time Teacher Ratio": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.2.1_front-sheet.pdf",
    "Student centric methods, such as experiential learning, participative learning and problem solving methodologies are used for enhancing learning experiences and teachers use ICT- enabled tools including online resources for effective teaching and learning process": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.3.1_front-sheet.pdf",
    "Percentage of full-time teachers against sanctioned posts during the last five years": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.4.1_front-sheet.pdf",
    "Percentage of full time teachers with NET/SET/SLET/ Ph. D./D.Sc. / D.Litt./L.L.D. during the last five years (consider only highest degree for count)": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.4.2_front-sheet.pdf",
    "Mechanism of internal/ external assessment is transparent and the grievance redressal system is time- bound and efficient": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.5.1_front-sheet.pdf",
    "Programme Outcomes (POs) and Course Outcomes (COs) for all Programmes offered by the institution are stated and displayed on website": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.6.1_front-sheet.pdf",
    "Attainment of POs and COs are evaluated.": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.6.2_front-sheet.pdf",
    "Pass percentage of Students during last five years (excluding backlog students)": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.6.3_front-sheet.pdf",
    "Online student satisfaction survey regarding to teaching learning process.": "assets/pdfs/naac/engineering-resources_naac_teaching-learning_2.7.1_student-survey.pdf"
}
pages['naac_teaching_learning.html'] = get_page("Teaching Learning and Evaluation", get_metrics_grid(teach_learn_metrics))

# 4. Research Innovation and Extension
rsch_metrics = {
    "Grants received from Government and non-governmental agencies for research projects / endowments in the institution during the last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.1.1_front-sheet.pdf",
    "Institution has created an ecosystem for innovations, Indian Knowledge System (IKS), including awareness about IPR, establishment of IPR cell, Incubation centre and other initiatives for the creation and transfer of knowledge/technology and the outcomes of the same are evident": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.2.1_front-sheet.pdf",
    "Number of workshops/seminars/conferences including programs conducted on Research Methodology, Intellectual Property Rights (IPR) and entrepreneurship during the last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.2.2_front-sheet.pdf",
    "Number of research papers published per teacher in the Journals as notified on UGC CARE list during the last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.3.1_front-sheet.pdf",
    "Number of books and chapters in edited volumes/books published and papers published in national/ international conference proceedings per teacher during last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.3.2_front-sheet.pdf",
    "Outcomes of Extension activities in the neighborhood community in terms of impact and sensitizing the students to social issues for their holistic development during the last five years.": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.4.1_front-sheet.pdf",
    "Awards and recognitions received for extension activities from government / government recognised bodies": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.4.2_front-sheet.pdf",
    "Number of extension and outreach programs conducted by the institution through organized forums including NSS/NCC with involvement of community during the last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.4.3_front-sheet.pdf",
    "Number of functional MoUs/linkages with institutions/ industries in India and abroad for internship, on-the-job training, project work, student / faculty exchange and collaborative research during the last five years": "assets/pdfs/naac/engineering-resources_naac_research-innovation_3.5.1_front-sheet.pdf"
}
pages['naac_research_innovation.html'] = get_page("Research Innovation and Extension", get_metrics_grid(rsch_metrics))

# 5. Infrastructure and Learning Resource
infra_metrics = {
    "The Institution has adequate infra-and-learning and other facilities for teaching – learning, viz., classrooms, laboratories, computing equipment etc ICT – enabled facilities such as smart class, LMS etc. Facilities for Cultural and sports activities, yoga centre, games (indoor and outdoor), Gymnasium, auditorium etc": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.1.1_front-sheet.pdf",
    "Percentage of expenditure for infrastructure development and augmentation excluding salary during the last five years": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.1.2_front-sheet.pdf",
    "Library is automated with digital facilities using Integrated Library Management System (ILMS), adequate subscriptions to e-resources and journals are made. The library is optimally used by the faculty and students": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.2.1_front-sheet.pdf",
    "Institution frequently updates its IT facilities and provides sufficient bandwidth for internet connection": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.3.1_front-sheet.pdf",
    "Student – Computer ratio (Data for the latest completed academic year)": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.3.2_front-sheet.pdf",
    "Percentage expenditure incurred on maintenance of physical facilities and academic support facilities excluding salary component, during the last five years": "assets/pdfs/naac/engineering-resources_naac_infra-and-learning_4.4.1_front-sheet.pdf"
}
pages['naac_infrastructure.html'] = get_page("Infrastructure and Learning Resource", get_metrics_grid(infra_metrics))

# 6. Student Support Progression
stu_sup_metrics = {
    "Percentage of students benefited by scholarships and freeships provided by the institution, government and non-government bodies, industries, individuals, philanthropists during the last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.1.1_front-sheet.pdf",
    "Following capacity development and skills enhancement activities are organised for improving students’ capability": "assets/pdfs/naac/engineering-resources_naac_student-support_5.1.2_front-sheet.pdf",
    "Percentage of students benefitted by guidance for competitive examinations and career counseling offered by the Institution during the last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.1.3_front-sheet.pdf",
    "The institution adopts the following for redressal of student grievances including sexual harassment and ragging cases": "assets/pdfs/naac/engineering-resources_naac_student-support_5.1.4_front-sheet.pdf",
    "Percentage of placement of outgoing students and students progressing to higher education during the last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.2.1_front-sheet.pdf",
    "Percentage of students qualifying in state/national/ international level examinations during the last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.2.2_front-sheet.pdf",
    "Number of awards/medals for outstanding performance in sports/ cultural activities at University / state/ national / international level during the last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.3.1_front-sheet.pdf",
    "Average number of sports and cultural programs in which students of the Institution participated during last five years": "assets/pdfs/naac/engineering-resources_naac_student-support_5.3.2_front-sheet.pdf",
    "There is a registered Alumni Association that contributes significantly to the development of the institution through financial and/or other support services": "assets/pdfs/naac/engineering-resources_naac_student-support_5.4.1_front-sheet.pdf"
}
pages['naac_student_support.html'] = get_page("Student Support Progression", get_metrics_grid(stu_sup_metrics))

# 7. Governance, Leadership and Management
gov_metrics = {
    "The institutional governance and leadership are in accordance with the vision and mission of the Institution and it is visible in various institutional practices such as NEP implementation, sustained institutional growth, decentralization, participation in the institutional governance and in their short term and long term Institutional Perspective Plan.": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.1.1_front-sheet.pdf",
    "The institutional perspective plan is effectively deployed and functioning of the institutional bodies is effective and efficient as visible from policies, administrative setup, appointment, service rules, and procedures, etc.": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.2.1_front-sheet.pdf",
    "Institution implements e-governance in its operations": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.2.2_front-sheet.pdf",
    "The institution has performance appraisal system, effective welfare measures for teaching and non-teaching staff and avenues for career development/progression": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.3.1_front-sheet.pdf",
    "Percentage of teachers provided with financial support to attend conferences/workshops and towards membership fee of professional bodies during the last five years": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.3.2_front-sheet.pdf",
    "Percentage of teaching and non-teaching staff participating in Faculty development Programmes (FDP), Management Development Programmes (MDPs) professional development /administrative training programs during the last five years": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.3.3_front-sheet.pdf",
    "Institution has strategies for mobilization and optimal utilization of resources and funds from various sources (government/ non-government organizations) and it conducts financial audits regularly (internal and external)": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.4.1_front-sheet.pdf",
    "Internal Quality Assurance Cell (IQAC) has contributed significantly for institutionalizing the quality assurance strategies and processes. It reviews teaching learning process, structures & methodologies of operations and learning outcomes at periodic intervals and records the incremental improvement in various activities": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.5.1_front-sheet.pdf",
    "Quality assurance initiatives of the institution include: 1. Regular meeting of Internal Quality Assurance Cell (IQAC); quality improvement initiatives identified and implemented 2. Academic and Administrative Audit (AAA) and follow-up action taken 3. Collaborative quality initiatives with other institution(s) 4. Participation in NIRF and other recognized rankings Any other quality audit/accreditation recognized by state, national or international agencies such as NAAC, NBA etc": "assets/pdfs/naac/engineering-resources_naac_governance-leadership-management_6.5.2_front-sheet.pdf"
}
pages['naac_governance.html'] = get_page("Governance, Leadership and Management", get_metrics_grid(gov_metrics))

# 8. Institution Values and Best Practices
inst_val_metrics = {
    "Institution has initiated the Gender Audit and measures for the promotion of gender equity during the last five years.": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.1.1_front-sheet.pdf",
    "The Institution has facilities and initiatives for 1. Alternate sources of energy and energy conservation measures 2. Management of the various types of degradable and non-degradable waste 3. Water conservation 4. Green campus initiatives 5. Disabled-friendly, barrier free environment": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.1.2_front-sheet.pdf",
    "Quality audits on environment and energy regularly undertaken by the Institution. The institutional environment and energy initiatives are confirmed through the following 1. Green audit / Environment audit 2. Energy audit 3. Clean and green campus initiatives 4. Beyond the campus environmental promotion and sustainability activities": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.1.3_front-sheet.pdf",
    "Describe the Institutional efforts/initiatives in providing an inclusive environment i.e., tolerance and harmony towards cultural, regional, linguistic, communal socioeconomic diversity and Sensitization of students and employees to the constitutional obligations: values, rights, duties and responsibilities of citizens": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.1.4_front-sheet.pdf",
    "Describe two best practices successfully implemented by the Institution as per NAAC format provided in the Manual": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.2_front-sheet.pdf",
    "Portray the performance of the Institution in one area distinctive to its priority and thrust within 1000 words": "assets/pdfs/naac/engineering-resources_naac_institutional-values_7.3_front-sheet.pdf"
}
pages['naac_institutional_values.html'] = get_page("Institution Values and Best Practices", get_metrics_grid(inst_val_metrics))

# Write all pages
for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(pages)} highly animated NAAC pages and updated navigation globally.")
