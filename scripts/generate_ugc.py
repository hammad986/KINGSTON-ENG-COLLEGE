import os
import re
import urllib.request
import urllib.parse
import ssl
import socket
socket.setdefaulttimeout(15)

base_dir = r"d:\clg website new"
template_path = os.path.join(base_dir, "about.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

ugc_nav_old = r'<li class="has-dropdown">\s*<a href="ugc_mandatory_committee\.html">UGC Mandatory Committee.*?<li><a href="index\.html">Contact Us</a></li>\s*</ul>\s*</li>'
ugc_nav_old_2 = r'<li class="has-dropdown">\s*<a href="ugc_mandatory_committee\.html">UGC Mandatory Committee.*?<li><a href="facilities_infrastructure\.html">Picture Gallery</a></li>\s*<li><a href="index\.html">Contact Us</a></li>\s*</ul>\s*</li>'
ugc_nav_old_3 = r'<li class="has-dropdown">\s*<a href="ugc_mandatory_committee\.html">UGC Mandatory Committee.*?<li class="has-dropdown" style="position:relative;">\s*<a href="#">Information Corner.*?</ul>\s*</li>'

ugc_nav_new = '''<li class="has-dropdown">
                        <a href="ugc_mandatory_committee.html">UGC Mandatory Committee <i class="fas fa-caret-down"></i></a>
                        <ul class="dropdown js-exclude-dropdown">
                            <li><a href="ugc_mc_icc.html">Internal Complaint Committee</a></li>
                            <li><a href="ugc_mc_sgrc.html">Student Grievance Redressal</a></li>
                            <li><a href="ugc_mc_posh.html">POSH Cell</a></li>
                            <li><a href="ugc_mc_sedg.html">SEDG</a></li>
                            <li><a href="ugc_mc_arc.html">Anti Ragging Committee</a></li>
                            <li><a href="ugc_mc_eqc.html">Equal Opportunity Cell</a></li>
                        </ul>
                    </li>
                    <li class="has-dropdown">
                        <a href="ugc_undertaking.html">UGC Undertaking Letter By HOI <i class="fas fa-caret-down"></i></a>
                        <ul class="dropdown js-exclude-dropdown">
                            <li><a href="ugc_ul_1.html">Undertaking Letter I</a></li>
                            <li><a href="ugc_ul_2.html">Undertaking Letter II</a></li>
                        </ul>
                    </li>
                    <li class="has-dropdown">
                        <a href="public_self_disclosure.html">Public Self Disclosure <i class="fas fa-caret-down"></i></a>
                        <ul class="dropdown js-exclude-dropdown">
                            <li class="has-dropdown">
                                <a href="#">About HEI <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_aboutus.html">About Us</a></li>
                                    <li><a href="ugc_ps_act_statutes.html">Act and Statutes</a></li>
                                    <li><a href="ugc_ps_idp.html">Institutional Development Plan</a></li>
                                    <li><a href="ugc_ps_affiliating.html">Affiliating University</a></li>
                                    <li><a href="ugc_ps_accreditation.html">Accreditation / Ranking Status</a></li>
                                    <li><a href="ugc_ps_recognition.html">Recognition / Approvals</a></li>
                                    <li><a href="ugc_ps_annual_reports.html">Annual Reports</a></li>
                                    <li><a href="ugc_ps_annual_accounts.html">Annual Accounts & Audit Reports</a></li>
                                    <li><a href="ugc_ps_sponsoring_body.html">Sponsoring Body Details</a></li>
                                </ul>
                            </li>
                            <li class="has-dropdown">
                                <a href="#">Administrations <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_finance.html">Finance Officer</a></li>
                                    <li><a href="ugc_ps_coe.html">Controller of Examination</a></li>
                                    <li><a href="ugc_ps_cvo.html">Chief Vigilance Officer</a></li>
                                    <li><a href="ugc_ps_ombudsperson.html">Ombudsperson</a></li>
                                    <li><a href="ugc_ps_bos.html">Executive Council</a></li>
                                    <li><a href="ugc_ps_academic_leadership.html">Academic Leadership (HoDs)</a></li>
                                </ul>
                            </li>
                            <li class="has-dropdown">
                                <a href="#">Academic <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_academic_programs.html">Academic Programs</a></li>
                                    <li><a href="ugc_ps_academic_calendar.html">Academic Calendars</a></li>
                                    <li><a href="ugc_ps_examinations.html">Examinations</a></li>
                                    <li><a href="departments.html">Department</a></li>
                                    <li><a href="ugc_ps_staff.html">Department Wise Faculty Details</a></li>
                                    <li><a href="iqac_about.html">Internal Quality Assurance Cell</a></li>
                                    <li><a href="#">Library</a></li>
                                    <li><a href="ugc_ps_mou.html">Academic Collaborations</a></li>
                                </ul>
                            </li>
                            <li class="has-dropdown">
                                <a href="#">Admissions <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_prospectus.html">Prospectus</a></li>
                                    <li><a href="ugc_ps_feerefund.html">Fee Refund Policy</a></li>
                                    <li><a href="ugc_ps_admission_policy.html">Admission Process and Guidelines</a></li>
                                </ul>
                            </li>
                            <li class="has-dropdown">
                                <a href="#">Research's <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_rnd.html">Research and Development Cell</a></li>
                                    <li><a href="ugc_ps_incubation.html">Incubation Centre / Start-Ups / IIC</a></li>
                                    <li><a href="#">Central Facilities</a></li>
                                </ul>
                            </li>
                            <li class="has-dropdown">
                                <a href="#">Student Life <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_sports.html">Sports Facilities</a></li>
                                    <li><a href="ugc_ps_nss.html">NSS</a></li>
                                    <li><a href="ugc_ps_hostel.html">Hostel Details</a></li>
                                    <li><a href="placement_pat.html">Placement Cell & Activities</a></li>
                                    <li><a href="ugc_ps_sl_sgrc.html">SGRC and Ombudsperson</a></li>
                                    <li><a href="ugc_ps_health.html">Health Facilities</a></li>
                                    <li><a href="ugc_ps_sl_icc.html">Internal Complaints Committee</a></li>
                                    <li><a href="ugc_ps_sl_antiragging.html">Anti Ragging Cell</a></li>
                                    <li><a href="ugc_ps_sl_equalopportunity.html">Equal Opportunity Cell</a></li>
                                    <li><a href="ugc_ps_sl_sedg.html">SEDG</a></li>
                                    <li><a href="ugc_ps_differentlyabled.html">Facilities for Differently Abled</a></li>
                                </ul>
                            </li>
                            <li><a href="ugc_ps_alumni.html">Alumni Association</a></li>
                            <li class="has-dropdown">
                                <a href="#">Information Corner <i class="fas fa-angle-right" style="float:right; margin-top:4px;"></i></a>
                                <ul class="dropdown js-exclude-dropdown">
                                    <li><a href="ugc_ps_rti.html">RTI</a></li>
                                    <li><a href="ugc_ps_circulars.html">Circulars and Notices</a></li>
                                    <li><a href="ugc_ps_announcements.html">Announcements</a></li>
                                    <li><a href="ugc_ps_newsletters.html">Newsletters</a></li>
                                    <li><a href="ugc_ps_events.html">News, Recent Events & Achievements</a></li>
                                    <li><a href="#">Job Openings</a></li>
                                    <li><a href="ugc_ps_studyinindia.html">Admission for International Students</a></li>
                                    <li><a href="#">Details and Location Map</a></li>
                                </ul>
                            </li>
                        </ul>
                    </li>'''

# Try to replace the old navigation chunk
new_template = re.sub(ugc_nav_old, ugc_nav_new, template_content, flags=re.DOTALL)
if new_template == template_content:
    new_template = re.sub(ugc_nav_old_2, ugc_nav_new, template_content, flags=re.DOTALL)
if new_template == template_content:
    new_template = re.sub(ugc_nav_old_3, ugc_nav_new, template_content, flags=re.DOTALL)

# Forceful cleanup of any duplicates created by partial matches
new_template = re.sub(r'<li><a href="facilities_infrastructure\.html">Picture Gallery</a></li>\s*', '', new_template)
new_template = re.sub(r'<li><a href="index\.html">Contact Us</a></li>\s*', '', new_template)

# Forceful cleanup of legacy UGC links that were accidentally injected into the IQAC dropdown
legacy_ugc_iqac = r'<li[^>]*>\s*<a href="ugc_mandatory_committee\.html"[^>]*>.*?UGC Mandatory Committee</a>\s*</li>\s*<li>\s*<a href="ugc_undertaking\.html"[^>]*>.*?UGC Undertaking \(HOI\)</a>\s*</li>\s*<li>\s*<a href="public_self_disclosure\.html"[^>]*>.*?Public Self-Disclosure</a>\s*</li>'
new_template = re.sub(legacy_ugc_iqac, '', new_template, flags=re.DOTALL)

# Propagate new nav to all core pages
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
    "iqac_strategic_plan.html",
    "naac_iiqa.html", "naac_ssr.html", "naac_dvv.html", "naac_rti.html",
    "naac_extended_profile.html", "naac_curricular_aspects.html",
    "naac_teaching_learning.html", "naac_research_innovation.html",
    "naac_infrastructure.html", "naac_student_support.html",
    "naac_governance.html", "naac_institutional_values.html",
    "ugc_mandatory_committee.html", "ugc_undertaking.html", "public_self_disclosure.html",
    "ugc_mc_icc.html", "ugc_mc_sgrc.html", "ugc_mc_posh.html", "ugc_mc_sedg.html", "ugc_mc_arc.html", "ugc_mc_eqc.html",
    "ugc_ul_1.html", "ugc_ul_2.html", "ugc_ps_aboutus.html", "ugc_ps_act_statutes.html",
    "ugc_ps_idp.html", "ugc_ps_affiliating.html", "ugc_ps_accreditation.html", "ugc_ps_recognition.html",
    "ugc_ps_annual_reports.html", "ugc_ps_annual_accounts.html", "ugc_ps_sponsoring_body.html",
    "ugc_ps_finance.html", "ugc_ps_coe.html", "ugc_ps_cvo.html", "ugc_ps_ombudsperson.html",
    "ugc_ps_bos.html", "ugc_ps_academic_leadership.html", "ugc_ps_academic_programs.html",
    "ugc_ps_academic_calendar.html", "ugc_ps_examinations.html", "ugc_ps_staff.html",
    "ugc_ps_mou.html", "ugc_ps_prospectus.html", "ugc_ps_feerefund.html", "ugc_ps_admission_policy.html",
    "ugc_ps_rnd.html", "ugc_ps_incubation.html", "ugc_ps_sports.html", "ugc_ps_nss.html",
    "ugc_ps_hostel.html", "ugc_ps_sl_sgrc.html", "ugc_ps_health.html", "ugc_ps_sl_icc.html",
    "ugc_ps_sl_antiragging.html", "ugc_ps_sl_equalopportunity.html", "ugc_ps_sl_sedg.html",
    "ugc_ps_differentlyabled.html", "ugc_ps_alumni.html", "ugc_ps_circulars.html",
    "ugc_ps_announcements.html", "ugc_ps_newsletters.html", "ugc_ps_events.html",
    "ugc_ps_studyinindia.html", "ugc_ps_rti.html", "ugc_ps_aicte.html", "ugc_ps_mission_vision.html"
]

for cp in core_pages:
    p = os.path.join(base_dir, cp)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as fCore:
            cData = fCore.read()
            # Do regex iteratively to catch the different previous versions of the file being processed
            newData = re.sub(ugc_nav_old, ugc_nav_new, cData, flags=re.DOTALL)
            if newData == cData:
                newData = re.sub(ugc_nav_old_2, ugc_nav_new, cData, flags=re.DOTALL)
            if newData == cData:
                newData = re.sub(ugc_nav_old_3, ugc_nav_new, cData, flags=re.DOTALL)
        with open(p, 'w', encoding='utf-8') as fCore:
            fCore.write(newData)

# Extract core header and footer for generated pages
header_match = re.search(r'(<!DOCTYPE html>.*?<section class="about-hero-section">.*?<div class="hero-video-wrapper">.*?<video.*?</video>)', template_content, re.DOTALL)
header_part1 = header_match.group(1) if header_match else ""
footer_match = re.search(r'(<footer class="main-footer">.*)', template_content, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

# Helper function
def get_pdf_page(title, subtitle, pdf_path):
    hero_html = f'''
        <div class="hero-overlay" style="background:rgba(0,0,0,0.85);"></div>
        <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:10;flex-direction:column;pointer-events:none;">
            <div style="padding:10px 25px; background:rgba(255,215,0,0.9); border-radius:30px; margin-bottom:15px; font-weight:800; color:#111; font-family:'Poppins',sans-serif; letter-spacing:1px; font-size:0.9rem; backdrop-filter:blur(5px); display:flex; align-items:center; gap:8px; box-shadow:0 5px 15px rgba(255,215,0,0.3);">
                <i class="fas fa-file-pdf"></i> UGC DOCUMENT COMPLIANCE
            </div>
            <h1 style="color:#fff;font-size:3.5rem;font-weight:900;letter-spacing:1px;text-shadow:0 10px 30px rgba(0,0,0,0.8);text-transform:uppercase;text-align:center;">{title}</h1>
            <p style="color:#ddd; font-family:'Inter',sans-serif; font-size:1.2rem; margin-top:5px; text-transform:uppercase; letter-spacing:3px;">{subtitle}</p>
            <div style="width:100px; height:5px; background:linear-gradient(90deg, #ffd700, transparent); margin-top:20px; border-radius:3px;"></div>
        </div>
    </div>
    </section>
    '''
    content_html = f'''
    <section class="page-section" style="padding: 100px 0; background:linear-gradient(to bottom, #ffffff, #f4f7f6);">
        <div class="container" style="max-width: 1400px;">
            <div class="section-title text-center" data-aos="fade-down" style="margin-bottom:50px;">
                <p style="text-transform:uppercase; letter-spacing:2px; font-weight:700; color:#8b1a2b; font-family:'Inter',sans-serif; margin-bottom:10px; font-size:0.9rem;">Official Document Viewer</p>
                <h2 style="font-family:'Poppins',sans-serif; font-size:2.8rem; font-weight:800; color:#111; margin-bottom:15px; text-transform:uppercase;">{title}</h2>
                <div style="width:120px; height:4px; background:linear-gradient(90deg, #8b1a2b, #e74c3c); margin:0 auto; border-radius:2px;"></div>
            </div>
            <div data-aos="zoom-in" data-aos-delay="200" style="background:#fff; padding:20px; border-radius:20px; box-shadow:0 25px 50px rgba(139,26,43,0.1); border:1px solid rgba(0,0,0,0.05); position:relative; overflow:hidden;">
                <!-- Frame sizing -->
                <iframe src="{pdf_path}" width="100%" height="900px" style="border:none; border-radius:15px; box-shadow:inset 0 0 20px rgba(0,0,0,0.05); background:#fdfdfd;"></iframe>
            </div>
            <div class="text-center mt-5" data-aos="fade-up" data-aos-delay="400">
                <a href="{pdf_path}" target="_blank" style="background:#8b1a2b; color:#fff; padding:15px 40px; border-radius:30px; font-family:'Inter',sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:1px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; transition:transform 0.3s, box-shadow 0.3s; box-shadow:0 10px 20px rgba(139,26,43,0.2);">
                    Download PDF <i class="fas fa-download"></i>
                </a>
            </div>
        </div>
    </section>
    '''
    return header_part1 + hero_html + content_html + footer_html

ugc_targets = {
    # UGC Mandatory
    "Internal Complaint Committee": ("ugc_mandatory_committee", "ugc_mc_icc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/icc.pdf"),
    "Student Grievance Redressal": ("ugc_mandatory_committee", "ugc_mc_sgrc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/sgrc.pdf"),
    "POSH Cell": ("ugc_mandatory_committee", "ugc_mc_posh.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/posh.pdf"),
    "SEDG": ("ugc_mandatory_committee", "ugc_mc_sedg.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/sedg.pdf"),
    "Anti Ragging Committee": ("ugc_mandatory_committee", "ugc_mc_arc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/arc.pdf"),
    "Equal Opportunity Cell": ("ugc_mandatory_committee", "ugc_mc_eqc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Mandatory_Committee/eqc.pdf"),
    # UGC Undertaking
    "Undertaking Letter I": ("ugc_undertaking", "ugc_ul_1.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Undertaking_Letter_by_HOI/UGC_HOI_I.pdf"),
    "Undertaking Letter II": ("ugc_undertaking", "ugc_ul_2.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/UGC_Undertaking_Letter_by_HOI/UGC_HOI_II.pdf"),
    # Public Self Disclosure - About HEI
    "About Us": ("public_self_disclosure", "ugc_ps_aboutus.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/aboutus.pdf"),
    "Act and Statutes": ("public_self_disclosure", "ugc_ps_act_statutes.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/act_statutes/act_statutes.pdf"),
    "Institutional Development Plan": ("public_self_disclosure", "ugc_ps_idp.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/institutional_development_plan.pdf"),
    "Affiliating University": ("public_self_disclosure", "ugc_ps_affiliating.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/affiliating_university.pdf"),
    "Accreditation and Ranking": ("public_self_disclosure", "ugc_ps_accreditation.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/accrediation_ranking/accrediation_ranking.pdf"),
    "Recognition and Approvals": ("public_self_disclosure", "ugc_ps_recognition.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/recognition_approvals/recognition_approvals.pdf"),
    "Annual Reports": ("public_self_disclosure", "ugc_ps_annual_reports.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/annual_reports/annual_reports.pdf"),
    "Annual Accounts & Audit": ("public_self_disclosure", "ugc_ps_annual_accounts.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/accounts_report/accounts_report.pdf"),
    "Sponsoring Body": ("public_self_disclosure", "ugc_ps_sponsoring_body.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/about_hei/sponsoring_body/sponsoring_body.pdf"),
    # Public Self Disclosure - Administrations
    "Finance Officer": ("public_self_disclosure", "ugc_ps_finance.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/finance_officer.pdf"),
    "Controller of Examination": ("public_self_disclosure", "ugc_ps_coe.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/coe.pdf"),
    "Chief Vigilance Officer": ("public_self_disclosure", "ugc_ps_cvo.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/cvo.pdf"),
    "Ombudsperson": ("public_self_disclosure", "ugc_ps_ombudsperson.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/ombudsperson.pdf"),
    "Executive Council": ("public_self_disclosure", "ugc_ps_bos.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/bos.pdf"),
    "Academic Leadership (HoDs)": ("public_self_disclosure", "ugc_ps_academic_leadership.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/administration/academic_leadership.pdf"),
    # Public Self Disclosure - Academic
    "Academic Programs": ("public_self_disclosure", "ugc_ps_academic_programs.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/academic/academic_programs.pdf"),
    "Academic Calendars": ("public_self_disclosure", "ugc_ps_academic_calendar.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/academic/academic_calendar.pdf"),
    "Examinations": ("public_self_disclosure", "ugc_ps_examinations.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/academic/examination/statutes.pdf"),
    "Department Wise Faculty Details": ("public_self_disclosure", "ugc_ps_staff.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/academic/staff/staff.pdf"),
    "Academic Collaborations": ("public_self_disclosure", "ugc_ps_mou.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/academic/mou/mou.pdf"),
    # Public Self Disclosure - Admissions
    "Prospectus": ("public_self_disclosure", "ugc_ps_prospectus.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/admission/prospectus.pdf"),
    "Fee Refund Policy": ("public_self_disclosure", "ugc_ps_feerefund.html", "https://kingston.ac.in/engineering-resources/autonomous/Fee_Refund_Policy.pdf"),
    "Admission Process and Guidelines": ("public_self_disclosure", "ugc_ps_admission_policy.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/admission/admission_policy.pdf"),
    # Public Self Disclosure - Research
    "Research and Development Cell": ("public_self_disclosure", "ugc_ps_rnd.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/research/research_development.pdf"),
    "Incubation Centre / Start-Ups": ("public_self_disclosure", "ugc_ps_incubation.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/research/incubation.pdf"),
    # Public Self Disclosure - Student Life
    "Sports Facilities": ("public_self_disclosure", "ugc_ps_sports.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/sports.pdf"),
    "NSS": ("public_self_disclosure", "ugc_ps_nss.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/nss/nss.pdf"),
    "Hostel Details": ("public_self_disclosure", "ugc_ps_hostel.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/hostel.pdf"),
    "SGRC and Ombudsperson": ("public_self_disclosure", "ugc_ps_sl_sgrc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/sgrc.pdf"),
    "Health Facilities": ("public_self_disclosure", "ugc_ps_health.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/health.pdf"),
    "Internal Complaints Committee": ("public_self_disclosure", "ugc_ps_sl_icc.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/icc.pdf"),
    "Anti Ragging Cell": ("public_self_disclosure", "ugc_ps_sl_antiragging.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/antiragging.pdf"),
    "Equal Opportunity Cell": ("public_self_disclosure", "ugc_ps_sl_equalopportunity.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/equalopportunity.pdf"),
    "SEDG ": ("public_self_disclosure", "ugc_ps_sl_sedg.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/sedg.pdf"),
    "Facilities for Differently Abled": ("public_self_disclosure", "ugc_ps_differentlyabled.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/student_life/facilityfordifferentlyabled.pdf"),
    # Public Self Disclosure - Alumni 
    "Alumni Association": ("public_self_disclosure", "ugc_ps_alumni.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/alumni/alumni.pdf"),
    # Public Self Disclosure - Information Corner
    "RTI": ("public_self_disclosure", "ugc_ps_rti.html", "https://kingston.ac.in/engineering-resources/naac/rti.pdf"),
    "Circulars and Notices": ("public_self_disclosure", "ugc_ps_circulars.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/information_corner/circular_0001.pdf"),
    "Announcements": ("public_self_disclosure", "ugc_ps_announcements.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/information_corner/announcements.pdf"),
    "Newsletters": ("public_self_disclosure", "ugc_ps_newsletters.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/information_corner/newsletters.pdf"),
    "News, Recent Events & Achievements": ("public_self_disclosure", "ugc_ps_events.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/information_corner/news_events.pdf"),
    "Admission for International Students": ("public_self_disclosure", "ugc_ps_studyinindia.html", "https://kingston.ac.in/engineering-resources/ugc_mandatory_disclosure/information_corner/studyinindia.pdf")
}

pages = {}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading and sorting {len(ugc_targets)} UGC PDFs into separate folders...")
for title, (folder_name, html_filename, url) in ugc_targets.items():
    pdf_dir = os.path.join(base_dir, "assets", "pdfs", folder_name)
    os.makedirs(pdf_dir, exist_ok=True)
    
    parsed = urllib.parse.urlparse(url)
    safe_name = parsed.path.strip('/').replace('/', '_')
    if not safe_name.endswith('.pdf'): safe_name += '.pdf'
    
    local_pdf_path = os.path.join(pdf_dir, safe_name)
    relative_pdf_path = f"assets/pdfs/{folder_name}/{safe_name}"

    if not os.path.exists(local_pdf_path):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as r, open(local_pdf_path, 'wb') as f:
                f.write(r.read())
            print(f"Downloaded: {safe_name}")
        except Exception as e:
            print(f"Skipping link {safe_name}: {e}")
            relative_pdf_path = url # Drop to Live URL silently 
        
    parent_category = folder_name.replace("_", " ").title()
    pages[html_filename] = get_pdf_page(title, parent_category, relative_pdf_path)

for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully generated {len(pages)} highly animated UGC pages.")
