import os

# Final Mechanical Engineering Department Generator with Deep Data Integration

def generate_mech():
    print("Starting Final Mechanical Supreme Generation (Deep Integration)...")

    # Load templates
    try:
        with open('mech_header.txt', 'r', encoding='utf-8') as f: header = f.read()
        with open('mech_footer.txt', 'r', encoding='utf-8') as f: footer = f.read()
    except FileNotFoundError:
        print("Error: MECH templates not found. Run extract_mech_template.py first.")
        return

    # Define specialized Mechanical Engineering styles
    extra_styles = """
<style>
/* Mechanical-Specific High-Impact UI */

/* Workshop Dashboard Stats */
.gear-dashboard { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 20px; margin: 30px 0; }
.gear-card { 
    background: #fff; border-radius: 20px; padding: 30px; text-align: center; 
    border-bottom: 6px solid #a31f24; box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
    transition: 0.4s; position: relative; overflow: hidden;
}
.gear-card:hover { transform: translateY(-10px) rotate(1deg); border-bottom-color: #003366; box-shadow: 0 20px 45px rgba(163,31,36,0.15); }
.gear-icon { font-size: 3rem; color: #a31f24; margin-bottom: 15px; opacity: 0.9; }
.gear-val { font-size: 2.2rem; font-weight: 900; color: #003366; margin: 5px 0; display: block; }
.gear-label { font-size: 0.9rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 1px; }

/* Mechanical Patent spotlight */
.mech-patent { 
    background: linear-gradient(135deg, #1a1a1a, #4a0404); 
    color: white; padding: 40px; border-radius: 25px; position: relative; 
    overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.1); 
    margin-top: 30px; border-right: 10px solid #f5c518;
}
.mech-patent::before {
    content: ''; position: absolute; top:0; left:0; width:100%; height:100%;
    background: url('https://engineering.kingston.ac.in/assets/img/pattern.png'); opacity: 0.05;
}
.patent-tag { 
    background: #f5c518; color: #000; padding: 8px 20px; border-radius: 30px; 
    font-weight: 800; font-size: 0.75rem; display: inline-block; margin-bottom: 15px; 
}
.patent-name { font-size: 1.8rem; font-weight: 900; margin: 10px 0; line-height: 1.2; letter-spacing: -0.5px; }

/* Specialization Verticals Grid */
.verticals-matrix { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; margin-top: 30px; }
.v-card { 
    background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); padding: 25px; 
    border-radius: 20px; border: 1px solid rgba(0,51,102,0.1); transition: 0.3s;
}
.v-card:hover { background: #003366; color: white; transform: scale(1.03); }
.v-card h4 { font-weight: 800; margin-bottom: 10px; font-size: 1.2rem; }
.v-card p { font-size: 0.85rem; opacity: 0.8; line-height: 1.5; }

/* Heavy Workshop showcase */
.workshop-showcase { 
    background: #fdfdfd; border: 1px solid #eee; border-radius: 20px; padding: 30px; 
    display: flex; gap: 30px; align-items: center; margin-top: 25px;
}
.workshop-showcase img { width: 300px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
</style>
"""

    # Inject styles
    header = header.replace('</head>', extra_styles + '</head>')

    pages = {
        'mech_infrastructure.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">CENTRALIZED WORKSHOP & LABS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>ADVANCED MANUFACTURING ECOSYSTEM</h3>
                <p>The Mechanical Engineering department houses the college's flagship Centralized Workshop, supporting multi-disciplinary engineering projects.</p>
                <div class="gear-dashboard">
                    <div class="gear-card" data-aos="zoom-in" data-aos-delay="50">
                        <i class="fa-solid fa-gears gear-icon"></i>
                        <span class="gear-val">12+</span>
                        <span class="gear-label">Specialized Laboratories</span>
                    </div>
                    <div class="gear-card" data-aos="zoom-in" data-aos-delay="100">
                        <i class="fa-solid fa-microchip gear-icon"></i>
                        <span class="gear-val">CNC Turning</span>
                        <span class="gear-label">Production Center</span>
                    </div>
                    <div class="gear-card" data-aos="zoom-in" data-aos-delay="150">
                        <i class="fa-solid fa-industry gear-icon"></i>
                        <span class="gear-val">Centralized</span>
                        <span class="gear-label">Workshop Facility</span>
                    </div>
                    <div class="gear-card" data-aos="zoom-in" data-aos-delay="200">
                        <i class="fa-solid fa-pen-nib gear-icon"></i>
                        <span class="gear-val">CAD/CAM</span>
                        <span class="gear-label">Analysis Center</span>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>LABORATORY SHOWCASE</h3>
                <div class="grid-2">
                    <div class="visit-card" data-aos="fade-right">
                        <div class="visit-header"><span>Metrology & Quality Control</span> <i class="fa-solid fa-compass-drafting"></i></div>
                        <div class="visit-body">Equipped with precise measuring instruments including Vernier Height Gauges, Sine Bars, and Profile Projectors for industrial QC training.</div>
                    </div>
                    <div class="visit-card" data-aos="fade-left">
                        <div class="visit-header"><span>Simulated Analysis Lab</span> <i class="fa-solid fa-laptop-code"></i></div>
                        <div class="visit-body">Featuring advanced SOLIDWORKS, ANSYS, and CAD packages for finite element analysis and structural modeling.</div>
                    </div>
                </div>
            </section>
        ''',

        'mech_research.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">RESEARCH & INNOVATION (IPR)</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ANNA UNIVERSITY RESEARCH CENTRE</h3>
                <p>Approved center since 2017, focusing on Thermodynamics, Material Science, and Renewable Energy.</p>
                <div class="rank-card" data-aos="flip-up" style="border-left-color:#a31f24;">
                    <i class="fa-solid fa-microscope rank-medal" style="color:#a31f24;"></i>
                    <div class="rank-info">
                        <span class="badge" style="background:#003366; color:#fff;">CORE RESEARCH STATUS</span>
                        <h4>17+ PhD DOCTORATES</h4>
                        <p>Web of Science & Scopus Indexed Publication Hub</p>
                    </div>
                </div>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>PATENT WALL (MECHANICAL)</h3>
                <div class="mech-patent" data-aos="zoom-out-up">
                    <span class="patent-tag"><i class="fa-solid fa-bolt"></i> ENERGY SYSTEMS PATENT</span>
                    <h2 class="patent-name">"THERMODYNAMIC CYCLE BASED POWER GENERATION SYSTEM"</h2>
                    <h4 style="color:#f5c518; margin-top:15px; font-weight:800;">DR. N. SHANKAR GANESH</h4>
                    <p style="opacity:0.8; margin-top:10px; line-height:1.6;">An innovative approach to high-efficiency power generation using advanced thermodynamic cycles, published internationally.</p>
                </div>
                
                <div class="mech-patent" data-aos="zoom-out-up" style="margin-top:20px; background:linear-gradient(135deg, #2c3e50, #000);">
                    <span class="patent-tag"><i class="fa-solid fa-utensils"></i> CULINARY TECH PATENT</span>
                    <h2 class="patent-name">"SYSTEM AND METHOD FOR COOKING FOOD ITEMS"</h2>
                    <h4 style="color:#3498db; margin-top:15px; font-weight:800;">DR. V. MOHANAVEL ET AL.</h4>
                    <p style="opacity:0.8; margin-top:10px; line-height:1.6;">Automated monitoring and control systems for industrial food processing and large-scale culinary operations.</p>
                </div>
            </section>
        ''',

        'mech_curriculum.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">R2021 CURRICULUM & SPECIALIZATIONS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>10 CAREER-TRACK VERTICALS</h3>
                <p>Mechanical Engineering under R2021 offers diverse paths to specialization, aligning with National Education Policy (NEP) goals.</p>
                <div class="verticals-matrix">
                    <div class="v-card" data-aos="fade-up" data-aos-delay="0">
                        <h4>Modern Mobility</h4>
                        <p>Focus on Electric Vehicles (EV), Hybrid systems, and Autonomous driving technologies.</p>
                    </div>
                    <div class="v-card" data-aos="fade-up" data-aos-delay="50">
                        <h4>Robotics & Automation</h4>
                        <p>Mechatronics, Industrial Robotics, and IoT integration in manufacturing.</p>
                    </div>
                    <div class="v-card" data-aos="fade-up" data-aos-delay="100">
                        <h4>Clean Energy</h4>
                        <p>Renewable energy heat systems, Power Generation, and Green hydrogen tech.</p>
                    </div>
                    <div class="v-card" data-aos="fade-up" data-aos-delay="150">
                        <h4>Product Development</h4>
                        <p>Computer Integrated Manufacturing and Product Lifecycle Management (PLM).</p>
                    </div>
                </div>
                <div style="margin-top:30px; text-align:center;">
                    <a href="assets/mech/R2021-B.E-MECH.pdf" download class="pdf-btn-premium" style="background:#a31f24; border-radius:10px;">Download B.E. R2021 Syllabus</a>
                    <a href="assets/mech/R2021-M.E-MECH.pdf" download class="pdf-btn-premium" style="background:#003366; border-radius:10px; margin-left:15px;">Download M.E. R2021 Syllabus</a>
                </div>
            </section>
        ''',

        'mech_placement.html': '''
            <h1 class="dept-title-red" data-aos="fade-down">INDUSTRY CONNECT & PLACEMENTS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>MECHANICAL INDUSTRY PARTNERS (MoUs)</h3>
                <div class="grid-3">
                    <div class="visit-card" style="text-align:center;">
                        <h4 style="color:#003366; font-weight:900;">VOLTECH</h4>
                        <p>Electrical & Power Engineering</p>
                    </div>
                    <div class="visit-card" style="text-align:center;">
                        <h4 style="color:#003366; font-weight:900;">BGR ENERGY</h4>
                        <p>Infrastructure & Power</p>
                    </div>
                    <div class="visit-card" style="text-align:center;">
                        <h4 style="color:#003366; font-weight:900;">KKM SOFT</h4>
                        <p>Authorized Autodesk Center</p>
                    </div>
                </div>
                
                <div class="glass-card-deep" style="margin-top:30px;">
                    <h4>MECH PLACEMENT TRACK RECORD</h4>
                    <div class="grid-2" style="margin-top:20px;">
                        <ul style="line-height:2;">
                            <li><i class="fa-solid fa-industry" style="color:#a31f24;"></i> Caparo Engineering</li>
                            <li><i class="fa-solid fa-industry" style="color:#a31f24;"></i> Emerald Resilient Tyre</li>
                            <li><i class="fa-solid fa-industry" style="color:#a31f24;"></i> TVS Upasana</li>
                        </ul>
                        <div style="background:rgba(163,31,36,0.05); padding:20px; border-radius:15px; text-align:center;">
                            <h2 style="color:#a31f24; font-weight:900; margin:0;">12 LPA</h2>
                            <p style="font-size:0.9rem; font-weight:700;">Highest Mechanical Placement</p>
                        </div>
                    </div>
                </div>
            </section>
        '''
    }

    # Generate pages
    for filename, content in pages.items():
        print(f"Generating MECH Deep Page: {filename}...")
        final_html = header + content + footer
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

    print("SUCCESS: Mechanical Engineering Deep Integration Complete!")

if __name__ == "__main__":
    generate_mech()
