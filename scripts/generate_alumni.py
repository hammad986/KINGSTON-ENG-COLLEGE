import os
import urllib.request
import ssl
import re

# Disable SSL verification for those pesky college servers
ssl._create_default_https_context = ssl._create_unverified_context

def download_pdf(url, dest_path):
    print(f"Downloading {url} to {dest_path}...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        dir_name = os.path.dirname(dest_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with urllib.request.urlopen(req, timeout=30) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
        print("Success.")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Setup directories
pdf_dir = "assets/pdfs/alumni"
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# PDF URLs
pdfs = {
    "Alumni_Cell_Member_List.pdf": "https://engineering.kingston.ac.in/assets/pdf/club-event/cell/Alumni.pdf",
    "Alumni_Association_Registration_Certificate.pdf": "https://engineering.kingston.ac.in/assets/pdf/alumini/Alumni%20Association%20Registration%20Certificate.pdf"
}

for filename, url in pdfs.items():
    download_pdf(url, os.path.join(pdf_dir, filename))

# Load template
try:
    with open("about.html", "r", encoding="utf-8") as f:
        template = f.read()
except:
    with open("index.html", "r", encoding="utf-8") as f:
        template = f.read()

def get_pdf_wrapper(title, pdf_path):
    # PDF Wrapper template matching the premium graduation style
    nav_end = template.find('</nav>')
    header_end = template.find('</header>', nav_end) + 9
    footer_start = template.find('<footer')
    
    main_section = f"""
    <section class="pdf-viewer-section" style="padding: 100px 0; background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); min-height: 80vh;">
        <div class="container">
            <div class="section-header text-center mb-10" data-aos="zoom-in">
                <h2 style="color: #fff; font-size: 3rem; margin-bottom: 20px; text-shadow: 0 0 20px rgba(255, 215, 0, 0.4);">{title}</h2>
                <div style="width: 100px; height: 5px; background: linear-gradient(to right, #ffd700, #ff8c00); margin: 0 auto 30px;"></div>
            </div>
            <div class="pdf-container" data-aos="flip-up" data-aos-delay="200" style="box-shadow: 0 25px 50px rgba(0,0,0,0.5); border-radius: 20px; overflow: hidden; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1);">
                <iframe src="{pdf_path}" width="100%" height="900px" style="border: none;"></iframe>
            </div>
            <div class="text-center mt-8" data-aos="fade-up">
                <a href="{pdf_path}" target="_blank" class="glow-on-hover" style="background: linear-gradient(45deg, #8b1a2b, #b31d35); color: #fff; padding: 15px 40px; text-decoration: none; border-radius: 50px; display: inline-block; font-weight: 700; transition: 0.3s; box-shadow: 0 10px 20px rgba(139, 26, 43, 0.4); font-family: 'Poppins', sans-serif;">Download Official PDF</a>
            </div>
        </div>
    </section>
    <style>
        .glow-on-hover:hover {{ transform: scale(1.05); box-shadow: 0 15px 30px rgba(139, 26, 43, 0.6); }}
    </style>
    """

    if header_end > 9 and footer_start > 0:
        new_page = template[:header_end] + main_section + template[footer_start:]
    else:
        new_page = template # Fallback
        
    return new_page

# Generate Wrappers
with open("alumni_cell_members.html", "w", encoding="utf-8") as f:
    f.write(get_pdf_wrapper("Alumni Cell Member List", "assets/pdfs/alumni/Alumni_Cell_Member_List.pdf"))

with open("alumni_registration.html", "w", encoding="utf-8") as f:
    f.write(get_pdf_wrapper("Alumni Association Registration Certificate", "assets/pdfs/alumni/Alumni_Association_Registration_Certificate.pdf"))

# Define full data from source documents
EXECUTIVE_BOARD = [
    {"role": "President", "name": "Mr. Raja Prakash V P", "dept": "Mechanical", "batch": "2012-2016"},
    {"role": "Vice President", "name": "Mr. Muthusaravanan S", "dept": "CSE", "batch": "2013-2017"},
    {"role": "Secretary", "name": "Mr. Aravind V", "dept": "ECE", "batch": "2018-2022"},
    {"role": "Treasurer", "name": "Ms. Parkavi S", "dept": "CSE", "batch": "2012-2016"},
    {"role": "Executive Member", "name": "Mr. Anand S", "dept": "IT", "batch": "2009-2013"},
    {"role": "Executive Member", "name": "Ms. Pavithra M", "dept": "IT", "batch": "2010-2014"},
    {"role": "Executive Member", "name": "Mr. Arunkumar P", "dept": "MBA", "batch": "2018-2020"},
    {"role": "Executive Member", "name": "Mr. Agilan K", "dept": "EEE", "batch": "2014-2018"},
    {"role": "Executive Member", "name": "Mr. Kishore PG", "dept": "ECE", "batch": "2017-2021"}
]

AWARD_CATEGORIES = [
    {"name": "Eminent Scientist", "icon": "fa-flask-vial"},
    {"name": "Prominent Industrialist", "icon": "fa-industry"},
    {"name": "Philanthropist / Social Service", "icon": "fa-hand-holding-heart"},
    {"name": "Young Alumnus Award", "icon": "fa-user-graduate"},
    {"name": "Administrator", "icon": "fa-user-tie"},
    {"name": "Sports / Arts / Music Excellence", "icon": "fa-trophy"}
]

ALUMNI_EVENTS_FULL = [
    {"title": "Lecture Series: National Technology Day", "speaker": "Mrs. Mukundha Shree (Lead Business Analyst, MSC Tech)", "description": "Kalpana Chawla's Memorial lectures and insightful analytics talk."},
    {"title": "Workshop: Game Dev using Unity", "speaker": "Mr. G Aswin Raj (Technical Lead, Rythmos India)", "description": "Two days hands-on immersive experience in Unity Engine."},
    {"title": "Webinar: Career Planning & Advancement", "speaker": "Ms. Lingapoorani (Consultant, TCS)", "description": "Strategic insights into industry expectations and career growth."},
    {"title": "Workshop: Industry 4.0 - Additive Mfg", "speaker": "Mr. G. Agiesh Ashok (MD, Inzaneone Tech)", "description": "Hands-on training on modern manufacturing paradigms."},
    {"title": "Workshop: Embedded Systems", "speaker": "Mr. K. Agilan (RTL Design Engineer, FLDEC Systems)", "description": "In-depth circuit design and firmware architectures."},
    {"title": "Webinar: Academic to Corporate Skills", "speaker": "Ms. A K Yuvashree (Senior Analyst, Accenture)", "description": "Bridging the gap between theory and industry implementation."},
    {"title": "Webinar: Multiple Views of Career Dev", "speaker": "Ms. Hemashri (Programmer Analyst, CTS)", "description": "Holistic view of multi-disciplinary career paths in tech."}
]

# High-End Content Generation
awards_html = "".join([f'<div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:10px; font-size:0.9rem; border:1px solid rgba(255,255,255,0.1);"><i class="fas {a["icon"]}" style="color:#ffd700; margin-right:8px;"></i> {a["name"]}</div>' for a in AWARD_CATEGORIES])

board_html = "".join([f'''
                <div class="member-card-3d" data-aos="fade-up" data-aos-delay="{i*100}">
                    <span class="member-role-badge">{m["role"]}</span>
                    <h4 class="member-name">{m["name"]}</h4>
                    <p class="member-meta">{m["dept"]} | Batch: {m["batch"]}</p>
                    <div style="margin-top:20px; border-top:1px solid rgba(255,255,255,0.15); padding-top:15px;">
                        <a href="alumni_cell_members.html" style="color:#ffd700; font-size:0.8rem; text-decoration:none; font-weight:700;">OFFICIAL PROFILE <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                ''' for i, m in enumerate(EXECUTIVE_BOARD)])

events_html = "".join([f'''
                <div class="timeline-item-mod" data-aos="fade-left" data-aos-delay="{i*100}">
                    <div class="event-card-mod">
                        <div class="event-title-mod">{e["title"]}</div>
                        <p style="color:#fff; font-weight:600; margin-bottom:10px;"><i class="fas fa-microphone-lines" style="color:#ffd700;"></i> {e["speaker"]}</p>
                        <p class="member-meta">{e["description"]}</p>
                    </div>
                </div>
                ''' for i, e in enumerate(ALUMNI_EVENTS_FULL)])

alumni_html_content = f"""
<style>
    /* ----- PREMIUM THEME & GLASSMORPHISM ----- */
    .alumni-main-wrap {{ 
        padding: 80px 0 120px; 
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('assets/images/alumni_hero_premium_bg.jpeg') center/cover fixed; 
        min-height: 100vh;
        color: #fff;
        font-family: 'Poppins', sans-serif;
    }}
    
    .glass-container {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 80px 50px;
        box-shadow: 0 40px 100px rgba(0,0,0,0.6);
        max-width: 1200px;
        margin: 0 auto;
    }}

    .section-title-glow {{
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(to right, #ffffff, #ffd700, #ffae00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 50px rgba(255, 215, 0, 0.4);
        margin-bottom: 10px;
        letter-spacing: -1px;
    }}

    /* ----- INTERACTIVE TABS ----- */
    .tabs-nav-modern {{ 
        display: flex; justify-content: center; gap: 20px; margin-bottom: 80px; flex-wrap: wrap; 
        padding: 15px; background: rgba(255,255,255,0.05); border-radius: 100px; width: fit-content; margin: 0 auto 80px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    
    .tab-btn-modern {{ 
        padding: 16px 32px; background: transparent; border: none; color: rgba(255,255,255,0.7); 
        font-weight: 700; cursor: pointer; border-radius: 100px; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        font-size: 1rem; text-transform: uppercase; letter-spacing: 1px;
    }}
    
    .tab-btn-modern.active {{ 
        background: linear-gradient(45deg, #8b1a2b, #b31d35); color: #fff; 
        box-shadow: 0 15px 30px rgba(139, 26, 43, 0.6); transform: translateY(-8px) scale(1.08);
    }}

    .tab-content-modern {{ display: none; animation: slideUpFade 0.8s cubic-bezier(0.165, 0.84, 0.44, 1) forwards; }}
    .tab-content-modern.active {{ display: block; }}
    
    @keyframes slideUpFade {{
        from {{ opacity: 0; transform: translateY(60px) scale(0.9); }}
        to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    /* ----- MEMBER CARDS ----- */
    .member-grid-premium {{ 
        display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 35px; 
    }}
    
    .member-card-3d {{
        background: rgba(255,255,255,0.05);
        padding: 45px 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .member-card-3d::before {{
        content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(255,215,0,0.15) 0%, transparent 60%);
        opacity: 0; transition: 0.6s;
    }}

    .member-card-3d:hover {{ 
        transform: translateY(-20px); 
        background: rgba(255,255,255,0.08);
        border-color: #ffd700;
        box-shadow: 0 30px 60px rgba(0,0,0,0.6);
    }}
    
    .member-card-3d:hover::before {{ opacity: 1; }}

    .member-role-badge {{
        display: inline-block; padding: 6px 18px; background: #8b1a2b; color: #fff;
        font-size: 0.8rem; font-weight: 800; border-radius: 50px; margin-bottom: 25px;
        text-transform: uppercase; letter-spacing: 2px;
        box-shadow: 0 5px 15px rgba(139, 26, 43, 0.4);
    }}

    .member-name {{ font-size: 1.5rem; font-weight: 800; margin-bottom: 12px; color: #ffd700; }}
    .member-meta {{ color: rgba(255,255,255,0.65); font-size: 0.95rem; font-weight: 500; }}

    /* ----- TIMELINE ----- */
    .timeline-wrap-mod {{ border-left: 3px solid rgba(255,215,0,0.4); padding-left: 50px; margin-left: 30px; }}
    
    .timeline-item-mod {{ position: relative; margin-bottom: 60px; }}
    
    .timeline-item-mod::before {{
        content: ''; position: absolute; left: -64px; top: 0; width: 24px; height: 24px;
        background: #8b1a2b; border: 5px solid #ffd700; border-radius: 50%;
        box-shadow: 0 0 25px #ffd700;
        z-index: 10;
    }}

    .event-card-mod {{
        background: rgba(255,255,255,0.05); padding: 40px; border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1); transition: 0.4s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }}
    
    .event-card-mod:hover {{ 
        background: rgba(255,255,255,0.1); transform: translateX(15px);
        border-color: #ffd700;
        box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    }}
    
    .event-title-mod {{ color: #ffd700; font-size: 1.6rem; font-weight: 800; margin-bottom: 15px; letter-spacing: -0.5px; }}
    
    /* ----- ACTION BUTTONS ----- */
    .btn-fusion {{
        display: inline-block; padding: 22px 50px; border-radius: 100px;
        font-weight: 900; text-transform: uppercase; letter-spacing: 2px;
        transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1); text-decoration: none; position: relative;
        margin: 20px; font-size: 1.1rem;
    }}
    
    .btn-gold {{
        background: linear-gradient(45deg, #ffd700, #ffab00);
        color: #000; box-shadow: 0 15px 40px rgba(255, 215, 0, 0.4);
    }}
    
    .btn-gold:hover {{ transform: scale(1.1) translateY(-5px); box-shadow: 0 25px 60px rgba(255, 215, 0, 0.6); }}

    .btn-glass {{
        background: rgba(255,255,255,0.1);
        color: #fff; backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.25);
    }}
    
    .btn-glass:hover {{ background: rgba(255,255,255,0.2); transform: scale(1.1) translateY(-5px); }}

</style>

<section class="alumni-main-wrap">
    <div class="container glass-container" data-aos="zoom-in">
        <div class="section-header text-center mb-16">
            <h1 class="section-title-glow" data-aos="zoom-out" data-aos-delay="200">Global Registry</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.4rem; font-weight: 600; letter-spacing: 3px; text-transform: uppercase;" data-aos="fade-up" data-aos-delay="400">Unity • Excellence • Impact</p>
            <div style="width: 150px; height: 6px; background: linear-gradient(to right, #8b1a2b, #ffd700); margin: 30px auto;" data-aos="stretch-x"></div>
        </div>

        <div class="tabs-nav-modern" data-aos="fade-up">
            <button class="tab-btn-modern active" onclick="openAlumniTab(event, 'core_about')">Philosophy</button>
            <button class="tab-btn-modern" onclick="openAlumniTab(event, 'executive_board')">Leadership</button>
            <button class="tab-btn-modern" onclick="openAlumniTab(event, 'official_reg')">Charter</button>
            <button class="tab-btn-modern" onclick="openAlumniTab(event, 'history_events')">Activities</button>
            <button class="tab-btn-modern" onclick="openAlumniTab(event, 'connect_now')">Network</button>
        </div>

        <!-- PHILOSOPHY TAB -->
        <div id="core_about" class="tab-content-modern active">
            <div class="row" style="display:flex; flex-wrap:wrap; gap:40px;">
                <div style="flex:1.2; min-width:350px;" data-aos="fade-right">
                    <div class="member-card-3d" style="text-align:left; border-left: 8px solid #ffd700;">
                        <h3 style="color:#ffd700; font-size: 2.2rem; margin-bottom:25px; font-weight:800;"><i class="fas fa-eye"></i> Visions & Missions</h3>
                        <p style="line-height:2; color:rgba(255,255,255,1); font-size: 1.2rem; font-weight:500;">
                            To bring all the Alumnis of Kingston Engineering College under one vibrant forum for the exchange of experience and knowledge and develop a strong network among themselves for bonding and fellowship and their career advancement.
                        </p>
                    </div>
                </div>
                <div style="flex:1; min-width:350px;" data-aos="fade-left">
                    <div class="member-card-3d" style="text-align:left; border-right: 8px solid #8b1a2b;">
                        <h3 style="color:#ffd700; font-size: 2.2rem; margin-bottom:25px; font-weight:800;"><i class="fas fa-crown"></i> Elite Awards</h3>
                        <div class="award-grid" style="display:grid; grid-template-columns: 1fr; gap:15px;">
                            {awards_html}
                        </div>
                    </div>
                </div>
            </div>
            <div class="member-card-3d" style="margin-top:50px; background: linear-gradient(45deg, rgba(139,26,43,0.4), rgba(0,0,0,0.6));" data-aos="fade-up">
                <h3 style="color:#fff; font-size: 2rem; font-weight:800;"><i class="fas fa-hand-fist"></i> Strategic Objectives</h3>
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:25px; padding:30px 0;">
                    <div class="member-meta" style="color:#fff;"><i class="fas fa-star" style="color:#ffd700; margin-right:10px;"></i> Career Guidance Architect</div>
                    <div class="member-meta" style="color:#fff;"><i class="fas fa-star" style="color:#ffd700; margin-right:10px;"></i> Industry-Academia Fusion</div>
                    <div class="member-meta" style="color:#fff;"><i class="fas fa-star" style="color:#ffd700; margin-right:10px;"></i> Student Support Ecosystem</div>
                    <div class="member-meta" style="color:#fff;"><i class="fas fa-star" style="color:#ffd700; margin-right:10px;"></i> Research & Innovation Hub</div>
                </div>
            </div>
        </div>

        <!-- LEADERSHIP TAB -->
        <div id="executive_board" class="tab-content-modern">
            <div class="member-grid-premium">
                {board_html}
            </div>
        </div>

        <!-- CHARTER TAB -->
        <div id="official_reg" class="tab-content-modern">
            <div class="member-card-3d" style="max-width:800px; margin:0 auto; padding:80px; background: rgba(0,0,0,0.4);" data-aos="zoom-out-up">
                <div style="font-size:6rem; color:#ffd700; margin-bottom:40px; filter: drop-shadow(0 0 20px rgba(255,215,0,0.5));">
                    <i class="fas fa-award"></i>
                </div>
                <h2 style="color:#fff; font-size:3rem; font-weight:900; letter-spacing: -1px;">Official Recognition</h2>
                <p style="font-size:1.8rem; color:rgba(255,255,255,0.9); margin:25px 0 50px;">
                    Reg No: <span style="background: linear-gradient(45deg, #ffd700, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;">SRG/Velur/45/2023</span>
                </p>
                <div style="display:flex; justify-content:center; gap:20px;">
                    <a href="alumni_registration.html" class="btn-fusion btn-gold">View Constitution</a>
                </div>
            </div>
        </div>

        <!-- ACTIVITIES TAB -->
        <div id="history_events" class="tab-content-modern">
            <div class="timeline-wrap-mod">
                {events_html}
            </div>
        </div>

        <!-- NETWORK TAB -->
        <div id="connect_now" class="tab-content-modern text-center">
            <div class="member-card-3d" style="padding:100px 50px; background: radial-gradient(circle at center, rgba(139,26,43,0.2) 0%, transparent 80%);" data-aos="zoom-in">
                <h2 style="font-size:4rem; font-weight:900; color:#ffd700; letter-spacing: -2px;">Global Alumni Matrix</h2>
                <p style="color:rgba(255,255,255,0.8); font-size:1.5rem; margin:30px 0 60px; max-width:700px; margin-left:auto; margin-right:auto;">Reconnect with the brilliance that defines Kingston. Join our prestigious network of innovators and leaders.</p>
                <div style="display:flex; justify-content:center; flex-wrap:wrap;">
                    <a href="https://forms.gle/TWF1jBYhyKJPDtAW9" target="_blank" class="btn-fusion btn-gold"><i class="fas fa-portal-enter"></i> Elite Registration</a>
                    <a href="https://forms.gle/2x5eeKPgngivoLUr9" target="_blank" class="btn-fusion btn-glass"><i class="fas fa-comment-dots"></i> Global Feedback</a>
                </div>
            </div>
        </div>

    </div>
</section>

<script>
    function openAlumniTab(evt, tabName) {{
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tab-content-modern");
        for (i = 0; i < tabcontent.length; i++) {{
            tabcontent[i].classList.remove("active");
            tabcontent[i].style.display = "none";
        }}
        tablinks = document.getElementsByClassName("tab-btn-modern");
        for (i = 0; i < tablinks.length; i++) {{
            tablinks[i].classList.remove("active");
        }}
        document.getElementById(tabName).style.display = "block";
        setTimeout(() => {{
            document.getElementById(tabName).classList.add("active");
        }}, 20);
        evt.currentTarget.classList.add("active");
        
        if(typeof AOS !== 'undefined') {{
            AOS.refresh();
        }}
    }}
</script>
"""

# Assemble page
nav_end = template.find('</nav>')
header_end = template.find('</header>', nav_end) + 9

footer_start = template.find('<footer')

if header_end > 9 and footer_start > 0:
    # We inject a special override for the main-header to ensure it doesn't cover the background
    style_overrides = """
    <style>
        .main-header { 
            background: rgba(0, 0, 0, 0.4) !important; 
            backdrop-filter: blur(15px) !important;
            border-bottom: 1px solid rgba(255,255,255,0.1) !important;
            box-shadow: none !important;
            position: sticky !important;
        }
        .top-bar { background: rgba(139, 26, 43, 0.6) !important; }
        .logo-bar, .notice-bar, .main-nav { background: transparent !important; border: none !important; }
        .nav-links > li > a { color: #fff !important; }
        .nav-links > li > a:hover { color: #ffd700 !important; }
        
        body { 
            background: #061528 !important; 
            margin: 0; padding: 0;
        }
    </style>
    """
    
    final_page = template[:header_end] + style_overrides + alumni_html_content + template[footer_start:]
    with open("alumni.html", "w", encoding="utf-8") as f:
        f.write(final_page)
    print("Highly animated premium Alumni page built successfully with fixed header.")
else:
    print(f"Error: Header end ({header_end}) or Footer start ({footer_start}) not found.")
