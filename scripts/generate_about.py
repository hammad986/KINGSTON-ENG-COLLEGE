import os
import glob
import re

base_dir = r"d:\clg website new"
template_path = os.path.join(base_dir, "about.html")

with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Update navigation globally
replacements = [
    ('<li><a href="#">Chairman</a></li>', '<li><a href="about_chairman.html">Chairman</a></li>'),
    ('<li><a href="#">Principal</a></li>', '<li><a href="about_principal.html">Principal</a></li>'),
    ('<li><a href="#">MOU</a></li>', '<li><a href="about_mou.html">MOU</a></li>'),
    ('<li><a href="#">Awards and Achievements</a></li>', '<li><a href="about_awards.html">Awards and Achievements</a></li>'),
    ('<li><a href="#">Organogram</a></li>', '<li><a href="about_organogram.html">Organogram</a></li>'),
    ('<li><a href="#">Governing Council</a></li>', '<li><a href="about_governing.html">Governing Council</a></li>'),
    ('<li><a href="#">Accreditation</a></li>', '<li><a href="about_accreditation.html">Accreditation</a></li>')
]

for old, new in replacements:
    template_content = template_content.replace(old, new)

core_pages = ["about.html", "index.html", "departments.html", "academics.html", "facilities.html", "facilities_infrastructure.html"]
for cp in core_pages:
    p = os.path.join(base_dir, cp)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as fCore:
            cData = fCore.read()
            for old, new in replacements:
                cData = cData.replace(old, new)
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
            <h1 style="color:#fff;font-size:3.2rem;font-weight:800;letter-spacing:1px;text-shadow:0 2px 10px rgba(0,0,0,0.6);text-transform:uppercase;">{title}</h1>
        </div>
    </div>
    </section>
    '''
    return header_part1 + hero_html + content + footer_html

pages = {}

# 1. Chairman
pages['about_chairman.html'] = get_page("Chairman's Message", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container">
        <div class="msg-layout" style="display: grid; grid-template-columns: 1fr 350px; gap: 56px; align-items: flex-start;" data-aos="fade-up">
            <div class="msg-body">
                <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Chairman's Message</h1>
                <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:28px;"></div>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">Dear parents and students,</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">My heartiest congratulations for your great success in the school final examinations.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">Education is a very important contributing element to both social mobility and economic development of a country. Technological progress in the last few decades in communication, transportation and information has helped to eliminate national barriers and create a global market place. At Kingston Engineering College our mission is to provide you a quality education and aliveness and edify from the eclipse of illiteracy by providing more eventualities for unfulfilled dreams.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">Furthermore, we aim to provide an academically exhilarating environment allowing our students to enjoy a first-class educational and social experience which encourages students to develop confidence, self-motivation, research and problem-solving skills and more importantly independent and innovative thinking.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">When combining these aspirations, we believe that graduates from Kingston Engineering College will be well equipped to meet the challenges of the global market, equipped with more technical and professional knowledge. Providing right education at the right time with right infrastructure and right academicians was the core objective of DURAI MURUGAN EDUCATIONAL TRUST and Kingston Engineering College, since its inception has striven to live up to its motto of setting standards in Educational Excellence. I personally welcome you ALL and I wish you ALL THE BEST for your career success in KINGSTON ENGINEERING COLLEGE.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">With warm regards,</p>
                <div class="signature" style="margin-top:20px;">
                    <div class="sig-name" style="font-weight:700; font-size:1rem; color:#111; font-family:'Inter',sans-serif;">Thiru.D.M. KATHIR ANAND M.B.A (USA)</div>
                    <div class="sig-role" style="color:#888; font-size:0.9rem; font-family:'Inter',sans-serif; margin-top:4px;">Chairman, Kingston Engineering College</div>
                </div>
            </div>
            <div class="msg-photo">
                <img src="assets/images/campus/chairman.png" alt="Chairman" style="width:100%; border-radius:6px; box-shadow:0 8px 30px rgba(0,0,0,0.12);" onerror="this.src='https://via.placeholder.com/350x420?text=Chairman'">
                <div class="msg-photo-caption" style="margin-top:14px; border-top:2px solid #eee; padding-top:10px;">
                    <div class="pc-name" style="font-weight:700; font-size:0.95rem; color:#111; font-family:'Inter',sans-serif;">Thiru.D.M. KATHIR ANAND M.B.A (USA)</div>
                    <div class="pc-title" style="color:#555; font-size:0.87rem; font-family:'Inter',sans-serif; margin-top:4px;">Chairman</div>
                </div>
            </div>
        </div>
    </div>
</section>
""")

# 2. Principal
pages['about_principal.html'] = get_page("Principal's Message", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container">
        <div class="msg-layout" style="display: grid; grid-template-columns: 1fr 350px; gap: 56px; align-items: flex-start;" data-aos="fade-up">
            <div class="msg-body">
                <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Principal's Message</h1>
                <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:28px;"></div>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">Dear All, Greetings!</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">It is my privilege to be associated with the family of Kingston Group of Educational Institutions. I warmly welcome you to the website of KINGSTON, an institution to provide an excellent value added education for our students, one that recognizes and embraces the importance of inter disciplinary collaborators to define and solve fundamentally important problems and to respond to national & international needs.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">KINGSTON is amongst many other established educational institutions in Tamilnadu. The campus is recognized for its unique philosophy, 'learning with delight' where students are encouraged to learn in a stress free environment. The campus has highly equipped infrastructure, which facilitates a positive & truthful learning environment for students.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">We will have a positive impact on the world economy through excellence in education, research, engagements and economic development programs and by preparing students for leadership roles in a diverse and global society. KINGSTON is one of the institutions which ensure that No child left behind in any aspects.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">We used to find a way to help every student to reach their highest potential with the compassion of dignity that every human deserves.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">I am proud of being the Principal of such a wonderful institution dedicated to the causes of better India.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">I assure you all that KINGSTON, a team of dedicated & highly qualified "great teachers" , is fully committed to produce engineers of very high caliber through our extended curriculum directed towards creating Industry Ready, "plug and play" & confident professionals.</p>
                <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:14px; font-family:'Inter',sans-serif;">With warm regards,</p>
                <div class="signature" style="margin-top:20px;">
                    <div class="sig-name" style="font-weight:700; font-size:1rem; color:#111; font-family:'Inter',sans-serif;">Dr.U.V.Arivazhagu M.E.,Ph.D</div>
                    <div class="sig-role" style="color:#888; font-size:0.9rem; font-family:'Inter',sans-serif; margin-top:4px;">Principal, Kingston Engineering College</div>
                </div>
            </div>
            <div class="msg-photo">
                <img src="assets/images/campus/principal.png" alt="Principal" style="width:100%; border-radius:6px; box-shadow:0 8px 30px rgba(0,0,0,0.12);" onerror="this.src='https://via.placeholder.com/350x420?text=Principal'">
                <div class="msg-photo-caption" style="margin-top:14px; border-top:2px solid #eee; padding-top:10px;">
                    <div class="pc-name" style="font-weight:700; font-size:0.95rem; color:#111; font-family:'Inter',sans-serif;">Dr.U.V.Arivazhagu M.E.,Ph.D</div>
                    <div class="pc-title" style="color:#555; font-size:0.87rem; font-family:'Inter',sans-serif; margin-top:4px;">Principal</div>
                </div>
            </div>
        </div>
    </div>
</section>
""")

# 3. MOU
pages['about_mou.html'] = get_page("Memorandum of Understanding", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Memorandum of Understanding (MoU)</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:28px;"></div>
        
        <p style="font-size:0.97rem; line-height:1.85; color:#333; margin-bottom:40px; max-width:1000px; font-family:'Inter',sans-serif;">
            The MoUs have been signed between Kingston Engineering College with leading industries and Training organizations with the sole aim of offering training in emerging technologies for developing employability skills, value added courses, career guidance programs, project works and internships thereby making the students industry ready and providing placements to the students.
        </p>

        <h3 style="font-size:1.4rem; font-weight:700; color:#111; margin-bottom:20px; font-family:'Poppins',sans-serif;">MOUs AND COLLABORATIONS</h3>
        
        <ul style="column-count: 2; column-gap: 40px; list-style: disc; padding-left: 20px; color: #555; font-size:0.92rem; font-family:'Inter',sans-serif; margin-bottom:60px;">
            <li style="margin-bottom:8px;">GODOID SYSTEMS, TIDEL PARK, CHENNAI</li>
            <li style="margin-bottom:8px;">RELEVANTZ TECHNOLOGY SERVICES, CHENNAI</li>
            <li style="margin-bottom:8px;">AIR MEDIA BROADCAST SOLUTIONS PVT. LTD, COIMBATORE</li>
            <li style="margin-bottom:8px;">TOP FRESHERS TECHNOLOGIES PVT. LTD, CHENNAI</li>
            <li style="margin-bottom:8px;">PRIMETEC AUTOMOTIVE PARTS PVT LTD, CHENNAI</li>
            <li style="margin-bottom:8px;">MILKYWAY CELL TECH, CHENNAI</li>
            <li style="margin-bottom:8px;">CAPARO ENGINEERING INDIA LIMITED, CHENNAI</li>
            <li style="margin-bottom:8px;">CRUD OPERATION PRIVATE LIMITED, CHENNAI</li>
            <li style="margin-bottom:8px;">METRO COMPOSITES, CHENNAI</li>
            <li style="margin-bottom:8px;">AVEON INFOTECH PRIVATE LIMITED, COIMBATORE</li>
            <li style="margin-bottom:8px;">TECHFULLY PVT. LTD, BANGALORE</li>
            <li style="margin-bottom:8px;">EVR ELECTRICALS PRIVATE LTD, CHENNAI</li>
            <li style="margin-bottom:8px;">INFOGRO TECHNOLOGY, CHENNAI</li>
            <li style="margin-bottom:8px;">SHREE ABIRAMI ENGINEERING PRIVATE LIMITED, CHENNAI</li>
            <li style="margin-bottom:8px;">SELVI SOFTWARE TECHNOLOGIES PVT LTD, VELLORE</li>
            <li style="margin-bottom:8px;">KAASHV INFOTECH, CHENNAI</li>
            <li style="margin-bottom:8px;">SHIAASH INFO SOLUTION PRIVATE LIMITED, CHENNAI</li>
            <li style="margin-bottom:8px;">ICESTERLI INDIA PVT LTD, RANIPET</li>
            <li style="margin-bottom:8px;">IMS LEARNING RESOURCE PRIVATE LTD, VELLORE</li>
            <li style="margin-bottom:8px;">DIGIDOC SOLUTIONS, VELLORE</li>
            <li style="margin-bottom:8px;">FOCUS LOGIC IT SERVICES, RANIPET</li>
            <li style="margin-bottom:8px;">FACT ENTRY DATA SOLUTIONS, VELLORE</li>
            <li style="margin-bottom:8px;">VIS EDUCATION AND TRAINING COMPANY, VELLORE</li>
            <li style="margin-bottom:8px;">NIT TTI, CHENNAI</li>
            <li style="margin-bottom:8px;">TECHBYHEART, KOCHI</li>
            <li style="margin-bottom:8px;">V3TS TECHNOLOGIES, CHENNAI</li>
        </ul>

        <style>
        .mou-marquee-wrap { width: 100%; overflow: hidden; white-space: nowrap; position: relative; padding: 40px 0; margin-top: 40px; border-top: 1px solid #ddd; }
        .mou-marquee-inner { display: inline-block; animation: scrollLeftMarqueeMOU 40s linear infinite; }
        .mou-marquee-inner:hover { animation-play-state: paused; }
        .mou-strip { display: inline-block; margin-right: 50px; height: 100px; vertical-align: middle; }
        @keyframes scrollLeftMarqueeMOU { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
        </style>
        <div class="mou-marquee-wrap">
            <div class="mou-marquee-inner">
                <img src="assets/images/mou/mou_strip_1.png" class="mou-strip" alt="MOU Partners">
                <img src="assets/images/mou/mou_strip_2.png" class="mou-strip" alt="MOU Partners">
                <img src="assets/images/mou/mou_strip_1.png" class="mou-strip" alt="MOU Partners">
                <img src="assets/images/mou/mou_strip_2.png" class="mou-strip" alt="MOU Partners">
            </div>
        </div>
    </div>
</section>
""")

# 4. Awards & Achievements
awards_list = glob.glob(os.path.join(base_dir, 'assets/images/awards&achievements/*.*'))
awards_images_html = ""
for img in awards_list:
    rel_path = img.replace(base_dir + "\\", "").replace("\\", "/")
    awards_images_html += f'<div class="award-img-box"><img src="{rel_path}" alt="Award"></div>'

pages['about_awards.html'] = get_page("Awards and Achievements", f"""
<style>
.awards-marquee-wrap {{ width: 100%; overflow: hidden; white-space: nowrap; position: relative; padding: 20px 0; margin-top: 30px; }}
.awards-marquee-inner {{ display: inline-block; animation: scrollLeftMarquee 150s linear infinite; }}
.awards-marquee-inner:hover {{ animation-play-state: paused; }}
.award-img-box {{ display: inline-block; margin-right: 30px; width: 350px; height: 480px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #eaeaea; overflow: hidden; background: #fff; vertical-align: top; transition:transform 0.3s; cursor:pointer; padding:10px; }}
.award-img-box:hover {{ transform:scale(1.02); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}
.award-img-box img {{ width: 100%; height: 100%; object-fit: contain; }}
@keyframes scrollLeftMarquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
</style>
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Awards and Achievements</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:28px;"></div>
    </div>
    
    <div class="awards-marquee-wrap">
        <div class="awards-marquee-inner">
            {awards_images_html}
            {awards_images_html}
        </div>
    </div>
</section>
""")

# 5. Organogram
pages['about_organogram.html'] = get_page("Organogram", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up" style="text-align:center;">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px; text-align:left;">Organogram</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <img src="assets/images/organogram/Organogram.jpeg" onerror="this.src='assets/images/organogram/organogram.jpg'; this.onerror=function(){this.src='https://via.placeholder.com/1200x800?text=Organogram+Image+Missing'};" alt="Organogram" style="width:100%; max-width:1100px; margin: 0 auto; display: block; border-radius:10px; box-shadow:0 10px 40px rgba(0,0,0,0.1); border:1px solid #eee;">
    </div>
</section>
""")

# 6. Governing Council
pages['about_governing.html'] = get_page("Governing Council", """
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Governing Council</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:40px;"></div>
        
        <div style="width:100%; height:900px; border-radius:12px; overflow:hidden; box-shadow:0 10px 40px rgba(0,0,0,0.15); border:1px solid #ddd;">
            <iframe src="assets/pdf/governing-council/governing-council.pdf" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
</section>
""")

# 7. Accreditation
acc_dirs = {
    'NAAC': 'NAAC',
    'NBA': 'NBA',
    'UGC': 'UGC',
    'AISHE': 'aishe',
    'Anna University': 'anna university',
    'ISO Audit': 'iso audit'
}

acc_html = ""
for title, folder in acc_dirs.items():
    images = glob.glob(os.path.join(base_dir, f'assets/images/accreditation/{folder}/*.*'))
    if images:
        acc_html += f'<h3 style="font-size:1.5rem; color:#111; margin:40px 0 20px; border-left:5px solid #8b1a2b; padding-left:15px; font-family:Poppins,sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">{title}</h3>'
        acc_html += '<div style="display:flex; flex-wrap:wrap; gap:30px; margin-bottom:50px;">'
        for img in images:
            rel_path = img.replace(base_dir + "\\", "").replace("\\", "/")
            escaped_path = rel_path.replace("'", "%27")
            acc_html += f'<img src="{escaped_path}" style="max-height:450px; border:1px solid #eee; padding:8px; box-shadow:0 4px 15px rgba(0,0,0,0.08); border-radius:8px; background:#fff; object-fit:contain; transition:transform 0.3s;" onmouseover="this.style.transform=&#39;scale(1.02)&#39;;" onmouseout="this.style.transform=&#39;scale(1)&#39;;">'
        acc_html += '</div>'

pages['about_accreditation.html'] = get_page("Accreditation", f"""
<section class="page-section" style="padding: 70px 0;">
    <div class="container" data-aos="fade-up">
        <h1 class="msg-heading" style="font-family:'Poppins',sans-serif; font-size:2.6rem; font-weight:800; color:#8b1a2b; margin-bottom:10px;">Accreditations & Certificates</h1>
        <div class="msg-divider" style="width:200px; height:3px; background:#8b1a2b; margin-bottom:20px;"></div>
        {acc_html}
    </div>
</section>
""")

# Write all pages
for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("All 7 About Us pages generated successfully.")
