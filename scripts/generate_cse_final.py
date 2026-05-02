import os

# Final Computer Science Engineering Department Generator with Deep Data Integration

def generate_cse():
    print("Starting Final CSE Supreme Generation (Deep Integration)...")

    # Load templates
    try:
        with open('cse_header.txt', 'r', encoding='utf-8') as f: header = f.read()
        with open('cse_footer.txt', 'r', encoding='utf-8') as f: footer = f.read()
    except FileNotFoundError:
        print("Error: CSE templates not found. Run extract_cse_template.py first.")
        return

    # Define specialized CSE styles
    extra_styles = """
<style>
/* CSE-Specific High-Impact UI */

/* Cyber Network Dashboard Stats */
.cyber-dashboard { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 20px; margin: 30px 0; }
.cyber-card { 
    background: #0b132b; border-radius: 20px; padding: 30px; text-align: center; 
    border-bottom: 6px solid #00ffff; box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
    transition: 0.4s; position: relative; overflow: hidden; color: #fff;
}
.cyber-card:hover { transform: translateY(-10px); border-bottom-color: #f5c518; box-shadow: 0 20px 45px rgba(0,255,255,0.3); }
.cyber-icon { font-size: 3rem; color: #00ffff; margin-bottom: 15px; text-shadow: 0 0 10px rgba(0,255,255,0.5); }
.cyber-val { font-size: 2.2rem; font-weight: 900; color: #fff; margin: 5px 0; display: block; }
.cyber-label { font-size: 0.9rem; font-weight: 700; color: #aaa; text-transform: uppercase; letter-spacing: 1px; }

/* Cyber Patent spotlight */
.cyber-patent { 
    background: linear-gradient(135deg, #0b132b, #1c2541); 
    color: white; padding: 40px; border-radius: 25px; position: relative; 
    overflow: hidden; border: 1px solid rgba(0, 255, 255, 0.2); 
    margin-top: 30px; border-left: 10px solid #00ffff;
}
.cyber-patent::before {
    content: ''; position: absolute; top:0; left:0; width:100%; height:100%;
    background: url('https://engineering.kingston.ac.in/assets/img/pattern.png'); opacity: 0.05;
}
.cyber-tag { 
    background: rgba(0, 255, 255, 0.1); color: #00ffff; padding: 8px 20px; border-radius: 30px; 
    font-weight: 800; font-size: 0.75rem; display: inline-block; margin-bottom: 15px; border: 1px solid #00ffff; 
}
.patent-name { font-size: 1.8rem; font-weight: 900; margin: 10px 0; line-height: 1.2; letter-spacing: -0.5px; }

/* Curriculum Cyber Grid */
.cyber-matrix { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; margin-top: 30px; }
.c-card { 
    background: rgba(255,255,255,0.9); padding: 25px; 
    border-radius: 20px; border: 1px solid #e0e0e0; transition: 0.3s;
    border-top: 4px solid #003366;
}
.c-card:hover { background: #0b132b; color: white; transform: scale(1.03); border-top-color: #00ffff; }
.c-card h4 { font-weight: 800; margin-bottom: 15px; font-size: 1.2rem; color: inherit; }
.c-card ul { padding-left: 20px; font-size: 0.9rem; line-height: 1.6; opacity: 0.9; }

/* FOSS Label */
.foss-banner { 
    background: #28a745; color: white; padding: 10px 25px; border-radius: 10px; 
    display: inline-flex; align-items: center; gap: 10px; font-weight: 800; margin-top: 20px; 
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""

    # Inject styles
    header = header.replace('</head>', extra_styles + '</head>')

    pages = {
        'cse_infrastructure.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">NETWORK & INFRASTRUCTURE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>HIGH-SPEED COMPUTING ECOSYSTEM</h3>
                <p>The CSE department is powered by an enterprise-grade computing architecture providing uninterrupted, high-speed access for advanced development and research.</p>
                <div class="cyber-dashboard">
                    <div class="cyber-card" data-aos="zoom-in" data-aos-delay="50">
                        <i class="fa-solid fa-network-wired cyber-icon"></i>
                        <span class="cyber-val">1.155 Gbps</span>
                        <span class="cyber-label">Dedicated Leased Line</span>
                    </div>
                    <div class="cyber-card" data-aos="zoom-in" data-aos-delay="100">
                        <i class="fa-solid fa-server cyber-icon"></i>
                        <span class="cyber-val">2000+</span>
                        <span class="cyber-label">Computing Terminals</span>
                    </div>
                    <div class="cyber-card" data-aos="zoom-in" data-aos-delay="150">
                        <i class="fa-solid fa-wifi cyber-icon"></i>
                        <span class="cyber-val">24x7</span>
                        <span class="cyber-label">Campus Wi-Fi Backbone</span>
                    </div>
                    <div class="cyber-card" data-aos="zoom-in" data-aos-delay="200">
                        <i class="fa-brands fa-python cyber-icon"></i>
                        <span class="cyber-val">FOSS</span>
                        <span class="cyber-label">Open Source Ecosystem</span>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>SPECIALIZED COMPUTING LABORATORIES</h3>
                <div class="grid-2">
                    <div class="visit-card" data-aos="fade-right">
                        <div class="visit-header"><span>Problem Solving & Data Structures</span> <i class="fa-solid fa-code"></i></div>
                        <div class="visit-body">Equipped for deep algorithmic training using Python and C/C++ environments, focusing on core computing fundamentals.</div>
                    </div>
                    <div class="visit-card" data-aos="fade-left">
                        <div class="visit-header"><span>DBMS & Operating Systems</span> <i class="fa-solid fa-database"></i></div>
                        <div class="visit-body">Specialized environments for advanced database administration, OS kernel research, and distributed systems.</div>
                    </div>
                </div>
            </section>
        ''',

        'cse_research.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">RESEARCH & INTELLECTUAL PROPERTY</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>CYBER INCUBATION & RESEARCH</h3>
                <p>The CSE department leads the institution in software innovation, focusing heavily on Cybersecurity, Agent Computing, and Machine Learning systems.</p>
                <div class="rank-card" data-aos="flip-up" style="border-left-color:#00ffff; background: #0b132b; color: white;">
                    <i class="fa-solid fa-shield-halved rank-medal" style="color:#00ffff;"></i>
                    <div class="rank-info">
                        <span class="badge" style="background:rgba(0, 255, 255, 0.2); color:#00ffff; border: 1px solid #00ffff;">FOCUS AREA</span>
                        <h4 style="color:#fff;">CYBERSECURITY & NETWORK SYSTEMS</h4>
                        <p style="color:#aaa;">Pioneering research in threat detection, data privacy, and secure architectures.</p>
                    </div>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>IPR WALL (CYBERSECURITY SPOTLIGHT)</h3>
                <div class="cyber-patent" data-aos="zoom-out-up">
                    <span class="cyber-tag"><i class="fa-solid fa-lock"></i> OFFICIAL PATENT FILED</span>
                    <h2 class="patent-name">"STRANGELY DETECT AND CONTROL CYBERCRIME DEVICE"</h2>
                    <h4 style="color:#f5c518; margin-top:15px; font-weight:800;">DR. RAJARAJESWARI P.</h4>
                    <p style="opacity:0.8; margin-top:10px; line-height:1.6; color:#ddd;">Patent Number: 201941018711. A pioneering device designed to identify, isolate, and mitigate advanced cyber threats in real-time, aligning with modern network security demands.</p>
                </div>
            </section>
        ''',

        'cse_curriculum.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CURRICULUM & SYLLABUS DIRECTORY</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>B.E. & M.E. CSE SYLLABUS VAULT</h3>
                <p>Explore the evolution of our rigorous curriculum frameworks across various Anna University regulations (R2013, R2017, R2021). The syllabus is continuously adapted to meet rapidly changing industry standards and cybersecurity threats.</p>
                
                <div class="glass-card-deep" style="margin-top:30px; padding: 40px; border-radius: 25px; border-top: 5px solid #00ffff; box-shadow: 0 15px 40px rgba(0, 255, 255, 0.1);">
                    <div style="display:flex; justify-content:center; gap:15px; margin-bottom:40px; flex-wrap:wrap;">
                        <button class="btn-side bg-brand-yellow text-black" style="padding: 12px 30px; font-size: 1.1rem; border-radius: 50px; font-weight: 800; cursor: pointer; border: 2px solid #f5c518; transition: 0.3s;" onclick="document.querySelectorAll('.reg-block').forEach(n=>n.style.display='none'); document.getElementById('r2021').style.display='block'; window.scrollTo({top: this.offsetTop, behavior: 'smooth'});">Regulation 2021</button>
                        <button class="btn-side bg-light-gray text-black" style="padding: 12px 30px; font-size: 1.1rem; border-radius: 50px; font-weight: 800; cursor: pointer; border: 2px solid transparent; transition: 0.3s;" onclick="document.querySelectorAll('.reg-block').forEach(n=>n.style.display='none'); document.getElementById('r2017').style.display='block'; window.scrollTo({top: this.offsetTop, behavior: 'smooth'});">Regulation 2017</button>
                        <button class="btn-side bg-light-gray text-black" style="padding: 12px 30px; font-size: 1.1rem; border-radius: 50px; font-weight: 800; cursor: pointer; border: 2px solid transparent; transition: 0.3s;" onclick="document.querySelectorAll('.reg-block').forEach(n=>n.style.display='none'); document.getElementById('r2013').style.display='block'; window.scrollTo({top: this.offsetTop, behavior: 'smooth'});">Regulation 2013</button>
                    </div>

                    <!-- Regulation 2021 -->
                    <div id="r2021" class="reg-block" style="display:block; animation: slideUp 0.6s ease-out;">
                        <h3 style="color:#00ffff; text-align:center; font-weight:900; margin-bottom:10px; font-size: 2rem;">R2021 CYBER-AI FRAMEWORK</h3>
                        <p style="text-align:center; color:#ddd; font-size: 1.1rem; margin-bottom: 30px;">The current foundational framework heavily utilizing Cloud Computing, Agent Systems, and advanced Machine Learning.</p>
                        <div class="cyber-matrix">
                            <div class="c-card" data-aos="zoom-in" data-aos-delay="0">
                                <h4><i class="fa-solid fa-terminal" style="color:#00ffff; margin-right: 8px;"></i> Foundational Core (Sem I-III)</h4>
                                <ul>
                                    <li>Problem Solving & Python</li>
                                    <li>Data Structures & Algorithms</li>
                                    <li>Object Oriented Programming</li>
                                </ul>
                            </div>
                            <div class="c-card" data-aos="zoom-in" data-aos-delay="50">
                                <h4><i class="fa-solid fa-server" style="color:#00ffff; margin-right: 8px;"></i> Systems & Architecture (Sem IV-V)</h4>
                                <ul>
                                    <li>Operating Systems</li>
                                    <li>Database Management</li>
                                    <li>Computer Networks</li>
                                </ul>
                            </div>
                            <div class="c-card" data-aos="zoom-in" data-aos-delay="100">
                                <h4><i class="fa-solid fa-microchip" style="color:#00ffff; margin-right: 8px;"></i> Advanced Tech (Sem VI-VII)</h4>
                                <ul>
                                    <li>Artificial Intelligence</li>
                                    <li>Cloud Computing</li>
                                    <li>Cryptography & Security</li>
                                </ul>
                            </div>
                            <div class="c-card" data-aos="zoom-in" data-aos-delay="150">
                                <h4><i class="fa-solid fa-briefcase" style="color:#00ffff; margin-right: 8px;"></i> Application (Sem VIII)</h4>
                                <ul>
                                    <li>Professional Electives</li>
                                    <li>Industry Internships</li>
                                    <li>Major Capstone Project</li>
                                </ul>
                            </div>
                        </div>
                        <div style="margin-top:40px; text-align:center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                            <a href="assets/cse/R2021-B.E-CSE.pdf" download class="pdf-btn-premium" style="background:#0b132b; border: 2px solid #00ffff; box-shadow: 0 0 20px rgba(0,255,255,0.3); padding: 15px 35px; border-radius: 50px; color: #fff; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s;"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> B.E. R2021 Syllabus</a>
                            <a href="assets/cse/R2021-M.E-CSE.pdf" download class="pdf-btn-premium" style="background:#f5c518; color: #000; border: 2px solid #f5c518; padding: 15px 35px; border-radius: 50px; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s; box-shadow: 0 0 20px rgba(245,197,24,0.3);"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> M.E. R2021 Syllabus</a>
                        </div>
                    </div>

                    <!-- Regulation 2017 -->
                    <div id="r2017" class="reg-block" style="display:none; animation: slideUp 0.6s ease-out;">
                        <h3 style="color:#f5c518; text-align:center; font-weight:900; margin-bottom:10px; font-size: 2rem;">R2017 ENGINEERING FRAMEWORK</h3>
                        <p style="text-align:center; color:#ddd; font-size: 1.1rem; margin-bottom: 30px;">A comprehensive curriculum that established robust software engineering and networking fundamentals.</p>
                        <div class="cyber-matrix" style="margin-bottom: 30px;">
                            <div class="c-card" style="border-top-color: #f5c518;">
                                <h4 style="color:#003366;"><i class="fa-solid fa-code" style="color:#f5c518; margin-right: 8px;"></i> Programming Core</h4>
                                <ul><li>C, C++, Java Programming</li><li>Data Structures</li></ul>
                            </div>
                            <div class="c-card" style="border-top-color: #f5c518;">
                                <h4 style="color:#003366;"><i class="fa-solid fa-network-wired" style="color:#f5c518; margin-right: 8px;"></i> Systems Core</h4>
                                <ul><li>Computer Architecture</li><li>Networks & OS</li></ul>
                            </div>
                        </div>
                        <div style="text-align:center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                            <a href="assets/cse/R2017-B.E-CSE.pdf" download class="pdf-btn-premium" style="background:#0b132b; border: 2px solid #f5c518; padding: 15px 35px; border-radius: 50px; color: #fff; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s;"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> B.E. R2017 Syllabus</a>
                            <a href="assets/cse/R2017-M.E-CSE.pdf" download class="pdf-btn-premium" style="background:#fff; color: #000; border: 2px solid #333; padding: 15px 35px; border-radius: 50px; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s;"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> M.E. R2017 Syllabus</a>
                        </div>
                    </div>

                    <!-- Regulation 2013 -->
                    <div id="r2013" class="reg-block" style="display:none; animation: slideUp 0.6s ease-out;">
                        <h3 style="color:#ff4d4d; text-align:center; font-weight:900; margin-bottom:10px; font-size: 2rem;">R2013 LEGACY FRAMEWORK</h3>
                        <p style="text-align:center; color:#ddd; font-size: 1.1rem; margin-bottom: 30px;">The foundational syllabus outlining early exploration into networking, databases, and microprocessors.</p>
                        
                        <div style="text-align:center; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                            <a href="assets/cse/R2013-B.E-CSE.pdf" download class="pdf-btn-premium" style="background:#0b132b; border: 2px solid #ff4d4d; padding: 15px 35px; border-radius: 50px; color: #fff; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s;"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> B.E. R2013 Syllabus</a>
                            <a href="assets/cse/R2013-M.E-CSE.pdf" download class="pdf-btn-premium" style="background:#fff; color: #000; border: 2px solid #333; padding: 15px 35px; border-radius: 50px; font-weight: 800; font-size: 1.1rem; text-decoration: none; transition: 0.3s;"><i class="fa-solid fa-download" style="margin-right: 10px;"></i> M.E. R2013 Syllabus</a>
                        </div>
                    </div>
                </div>
            </section>
        ''',

        'cse_placement.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">INDUSTRY CONNECT & PLACEMENTS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>TECHNOLOGY PARTNERS (MoUs)</h3>
                <p>The CSE department bridges the gap between academia and industry through strategic partnerships with leading tech firms.</p>
                <div class="grid-3">
                    <div class="visit-card" style="text-align:center; border-top: 4px solid #00ffff;">
                        <h4 style="color:#003366; font-weight:900;">AIRTEL CHENNAI</h4>
                        <p>Telecom & Networking</p>
                    </div>
                    <div class="visit-card" style="text-align:center; border-top: 4px solid #00ffff;">
                        <h4 style="color:#003366; font-weight:900;">KAASHIV INFOTECH</h4>
                        <p>Software Development</p>
                    </div>
                    <div class="visit-card" style="text-align:center; border-top: 4px solid #00ffff;">
                        <h4 style="color:#003366; font-weight:900;">SELVI SOFTWARE</h4>
                        <p>IT Solutions & Training</p>
                    </div>
                </div>
                
                <div class="glass-card-deep" style="margin-top:30px;">
                    <h4>IT PLACEMENT DYNAMICS</h4>
                    <div class="grid-2" style="margin-top:20px;">
                        <ul style="line-height:2;">
                            <li><i class="fa-solid fa-building" style="color:#003366;"></i> Relevantz Technology Services</li>
                            <li><i class="fa-solid fa-building" style="color:#003366;"></i> Infogro Technology</li>
                            <li><i class="fa-solid fa-building" style="color:#003366;"></i> Aveon Infotech</li>
                        </ul>
                        <div style="background:#0b132b; padding:20px; border-radius:15px; text-align:center; color: white;">
                            <h2 style="color:#00ffff; font-weight:900; margin:0;">100%</h2>
                            <p style="font-size:0.9rem; font-weight:700; color: #ddd;">Commitment to Tech Hiring</p>
                            <a href="assets/pdf/placement-report/campus-hiring.pdf" class="btn-side bg-brand-yellow text-black" style="display: inline-block; margin-top: 10px; padding: 5px 15px; text-decoration: none;">View Hiring Report</a>
                        </div>
                    </div>
                </div>
            </section>
        '''
    }

    # Generate pages
    for filename, content in pages.items():
        print(f"Generating CSE Deep Page: {filename}...")
        final_html = header + content + footer
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

    print("SUCCESS: Computer Science Engineering Deep Integration Complete!")

if __name__ == "__main__":
    generate_cse()
