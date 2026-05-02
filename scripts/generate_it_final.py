import os

# Final IT Department Generator with Deep Data Integration

def generate_it():
    print("Starting Final IT Supreme Generation (Deep Integration)...")

    # Load templates
    try:
        with open('it_header.txt', 'r', encoding='utf-8') as f: header = f.read()
        with open('it_footer.txt', 'r', encoding='utf-8') as f: footer = f.read()
    except FileNotFoundError:
        print("Error: IT templates not found. Run extract_it_template.py first.")
        return

    # Define specialized IT styles
    extra_styles = """
<style>
/* IT-Specific High-Impact UI */

/* Network Dashboard Stats */
.net-dashboard { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 20px; margin: 30px 0; }
.net-card { 
    background: #fff; border-radius: 20px; padding: 30px; text-align: center; 
    border-bottom: 6px solid #003366; box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
    transition: 0.4s; position: relative; overflow: hidden;
}
.net-card:hover { transform: translateY(-10px); border-bottom-color: #f5c518; box-shadow: 0 20px 45px rgba(0,51,102,0.15); }
.net-icon { font-size: 3rem; color: #003366; margin-bottom: 15px; opacity: 0.9; }
.net-val { font-size: 2.2rem; font-weight: 900; color: #a31f24; margin: 5px 0; display: block; }
.net-label { font-size: 0.9rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 1px; }

/* Patent Spotlight Card */
.patent-spotlight { 
    background: linear-gradient(135deg, #001a33, #003366); 
    color: white; padding: 40px; border-radius: 25px; position: relative; 
    overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); 
    margin-top: 30px;
}
.patent-spotlight::before {
    content: ''; position: absolute; top:0; left:0; width:100%; height:100%;
    background: url('https://engineering.kingston.ac.in/assets/img/pattern.png'); opacity: 0.05;
}
.patent-badge { 
    background: #f5c518; color: #000; padding: 8px 20px; border-radius: 30px; 
    font-weight: 800; font-size: 0.8rem; display: inline-block; margin-bottom: 15px; 
}
.patent-title { font-size: 1.8rem; font-weight: 900; margin: 10px 0; line-height: 1.2; text-shadow: 0 4px 10px rgba(0,0,0,0.3); }

/* Hall of Fame - Rank Holder */
.rank-card { 
    background: #fff; border-radius: 20px; padding: 35px; border-left: 8px solid gold; 
    display: flex; align-items: center; gap: 30px; box-shadow: 0 15px 40px rgba(0,0,0,0.06); 
    margin-top: 30px; transition: 0.3s;
}
.rank-card:hover { transform: scale(1.02); }
.rank-medal { font-size: 4rem; color: gold; filter: drop-shadow(0 5px 15px rgba(255, 215, 0, 0.4)); }
.rank-info h4 { margin: 0; color: #003366; font-size: 1.5rem; font-weight: 900; }
.rank-info p { margin: 5px 0 0 0; color: #a31f24; font-weight: 700; font-size: 1.1rem; }

/* Curriculum Matrix */
.matrix-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 18px; margin-top: 25px; }
.matrix-card { 
    background: #fdf5f5; padding: 22px; border-radius: 15px; border: 1px solid #eee; 
    transition: 0.3s; cursor: pointer;
}
.matrix-card:hover { background: #a31f24; color: white; transform: translateY(-5px); }
.matrix-card h5 { margin: 0; font-weight: 800; font-size: 1.1rem; }
.matrix-card ul { margin: 10px 0 0 0; padding-left: 20px; font-size: 0.85rem; opacity: 0.8; }

/* FOSS Label */
.foss-banner { 
    background: #28a745; color: white; padding: 10px 25px; border-radius: 10px; 
    display: inline-flex; align-items: center; gap: 10px; font-weight: 800; margin-top: 20px; 
}
</style>
"""

    # Inject styles
    header = header.replace('</head>', extra_styles + '</head>')

    pages = {
        'it_infrastructure.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">IT INFRASTRUCTURE & DATA CENTER</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>HIGH-SPEED NETWORK DASHBOARD</h3>
                <p>The IT department powers the campus with a state-of-the-art enterprise-grade networking ecosystem.</p>
                <div class="net-dashboard">
                    <div class="net-card" data-aos="zoom-in" data-aos-delay="50">
                        <i class="fa-solid fa-gauge-high net-icon"></i>
                        <span class="net-val">1155 Mbps</span>
                        <span class="net-label">Total Bandwidth (Tata + VIL)</span>
                    </div>
                    <div class="net-card" data-aos="zoom-in" data-aos-delay="100">
                        <i class="fa-solid fa-laptop-code net-icon"></i>
                        <span class="net-val">2000+</span>
                        <span class="net-label">Computational Terminals</span>
                    </div>
                    <div class="net-card" data-aos="zoom-in" data-aos-delay="150">
                        <i class="fa-solid fa-database net-icon"></i>
                        <span class="net-val">900 Sq. Ft.</span>
                        <span class="net-label">Centralized Data Center</span>
                    </div>
                    <div class="net-card" data-aos="zoom-in" data-aos-delay="200">
                        <i class="fa-solid fa-server net-icon"></i>
                        <span class="net-val">4.0 TB</span>
                        <span class="net-label">NAS & Server Storage</span>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>SPECIALIZED LABORATORIES</h3>
                <div class="grid-2">
                    <div class="visit-card" data-aos="fade-right">
                        <div class="visit-header"><span>FOSS Lab</span> <i class="fa-brands fa-linux"></i></div>
                        <div class="visit-body">Dedicated to <strong>Free and Open Source Software</strong>, featuring fully integrated Linux environments and open-stack technologies.</div>
                    </div>
                    <div class="visit-card" data-aos="fade-left">
                        <div class="visit-header"><span>Enterprise Networking</span> <i class="fa-solid fa-network-wired"></i></div>
                        <div class="visit-body">Equipped with Cisco Managed Switches and 24x7 Wi-Fi controllers for hands-on network administration training.</div>
                    </div>
                </div>
            </section>
        ''',

        'it_achievements.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">DEPARTMENTAL ACHIEVEMENTS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ACADEMIC HALL OF FAME</h3>
                <div class="rank-card" data-aos="flip-up">
                    <i class="fa-solid fa-trophy rank-medal"></i>
                    <div class="rank-info">
                        <span class="badge" style="background:#f5c518; color:#000;">UNIVERSITY RANK HOLDER</span>
                        <h4>BHUVANESHWARI J.</h4>
                        <p>University Rank: 4 <span style="font-weight:400; color:#666;">(Batch 2009 - 2013)</span></p>
                    </div>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>RESEARCH & INNOVATION (PATENT SPOTLIGHT)</h3>
                <div class="patent-spotlight">
                    <span class="patent-badge"><i class="fa-solid fa-certificate"></i> PATENT GRANTED / FILED</span>
                    <h2 class="patent-title">"STRANGELY DETECT AND CONTROL CYBERCRIME DEVICE"</h2>
                    <h4 style="color:#f5c518; margin-top:15px; font-weight:800;">DR. RAJARAJESWARI P.</h4>
                    <p style="opacity:0.8; margin-top:10px; line-height:1.6;">An innovative security hardware-software hybrid developed to identify and mitigate cyber threats in real-time, aligning with global Cyber Security standards.</p>
                </div>
            </section>
        ''',

        'it_curriculum.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CURRICULUM & ELECTIVE VERTICALS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ANNA UNIVERSITY R2021 REGULATION</h3>
                <p>An industry-aligned 8-semester matrix focusing on core computing and specialized electives.</p>
                <div class="matrix-grid">
                    <div class="matrix-card" data-aos="zoom-in"><h5>Semester I & II</h5><ul><li>Python Programming</li><li>Engg Mathematics</li><li>Engg Physics</li></ul></div>
                    <div class="matrix-card" data-aos="zoom-in" data-aos-delay="50"><h5>Semester III & IV</h5><ul><li>Data Structures</li><li>OS & DBMS</li><li>AI & Machine Learning</li></ul></div>
                    <div class="matrix-card" data-aos="zoom-in" data-aos-delay="100"><h5>Semester V & VI</h5><ul><li>Computer Networks</li><li>Full Stack Web Dev</li><li>Mobile App Dev</li></ul></div>
                    <div class="matrix-card" data-aos="zoom-in" data-aos-delay="150"><h5>Semester VII & VIII</h5><ul><li>Cyber Security</li><li>Human Values</li><li>Final Year Project</li></ul></div>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>PROFESSIONAL ELECTIVE VERTICALS (7 PATHS)</h3>
                <div class="vertical-box">
                    <span class="vertical-tag"><i class="fa-solid fa-database"></i> Data Science</span>
                    <span class="vertical-tag"><i class="fa-solid fa-code"></i> Full Stack Development</span>
                    <span class="vertical-tag"><i class="fa-solid fa-cloud"></i> Cloud Computing</span>
                    <span class="vertical-tag"><i class="fa-solid fa-shield-halved"></i> Cyber Security</span>
                    <span class="vertical-tag"><i class="fa-solid fa-palette"></i> Creative Media</span>
                    <span class="vertical-tag"><i class="fa-solid fa-microchip"></i> Emerging Technologies</span>
                    <span class="vertical-tag"><i class="fa-solid fa-robot"></i> Artificial Intelligence</span>
                </div>
                <div style="margin-top:30px; text-align:center;">
                    <a href="assets/it/R2021-B.TECH-IT.pdf" download class="pdf-btn-premium">Download R2021 Syllabus PDF</a>
                </div>
            </section>
        ''',

        'it_placement.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">PLACEMENT & RECRUITERS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>IT RECRUITMENT OVERVIEW (2022-23)</h3>
                <div class="grid-3" style="margin-bottom:30px;">
                    <div class="stat-card" style="border-top:6px solid #a31f24;">
                        <h2 style="font-size:2.5rem; margin:0;">12 LPA</h2>
                        <p style="font-weight:700;">Highest Package</p>
                    </div>
                    <div class="stat-card" style="border-top:6px solid #003366;">
                        <h2 style="font-size:2.5rem; margin:0;">4.5 LPA</h2>
                        <p style="font-weight:700;">Average Package</p>
                    </div>
                    <div class="stat-card" style="border-top:6px solid gold;">
                        <h2 style="font-size:2.5rem; margin:0;">95%</h2>
                        <p style="font-weight:700;">Placement Record</p>
                    </div>
                </div>
                
                <div class="glass-card-deep">
                    <h4>TOP IT HIRING PARTNERS</h4>
                    <div class="grid-2" style="margin-top:20px;">
                        <ul style="line-height:2;">
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> Zoho Corporation</li>
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> Tata Consultancy Services (TCS)</li>
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> Tech Mahindra</li>
                        </ul>
                        <ul style="line-height:2;">
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> Codoid Innovations</li>
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> MSC Technology</li>
                            <li><i class="fa-solid fa-check-circle" style="color:green;"></i> Plastic Omnium</li>
                        </ul>
                    </div>
                </div>
                <div style="margin-top:30px; text-align:center;">
                    <a href="assets/it/campus-hiring.pdf" download class="pdf-btn-premium">Download Hiring Overview PDF</a>
                </div>
            </section>
        '''
    }

    # Generate pages
    for filename, content in pages.items():
        print(f"Generating IT Deep Page: {filename}...")
        final_html = header + content + footer
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

    print("SUCCESS: IT Department Deep Integration Complete!")

if __name__ == "__main__":
    generate_it()
