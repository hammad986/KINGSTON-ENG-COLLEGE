import os
import re

def generate_subpage(filename, title, content_html, extra_css=""):
    print(f"Generating {filename}...")
    with open("about.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Extract header and footer
    header_match = re.search(r'([\s\S]*?<\/header>)', template)
    header = header_match.group(1) if header_match else ""
    
    footer_match = re.search(r'(<footer[\s\S]*?<\/html>)', template)
    if not footer_match:
        footer_match = re.search(r'(<div class="footer-bottom"[\s\S]*?<\/html>)', template)
    footer = footer_match.group(1) if footer_match else "</body></html>"

    # Inject title
    header = re.sub(r'<title>.*?</title>', f'<title>{title} - Kingston Engineering College</title>', header)

    # Inject extra styles
    # Add standardized hero styles for all subpages
    base_css = """
    .fac-hero { position: relative; width: 100%; height: 460px; overflow: hidden; background: #000; }
    .fac-hero video { width: 100%; height: 100%; object-fit: cover; }
    .fac-hero-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.25) 60%, transparent 100%); display: flex; align-items: flex-end; padding: 44px 64px; }
    .fac-hero-overlay h1 { color: #fff; font-size: 2.8rem; font-weight: 800; text-transform: uppercase; letter-spacing: 3px; border-left: 6px solid #f5c518; padding-left: 22px; }
    """
    header = header.replace("</head>", f"<style>{base_css}\n{extra_css}</style>\n</head>")

    video_hero = f'<section class="fac-hero"><video autoplay muted loop playsinline><source src="video.mp4" type="video/mp4"></video><div class="fac-hero-overlay"><h1>{title}</h1></div></section>'

    # Assemble final HTML
    final_html = header + f"\n{video_hero}\n<main>\n{content_html}\n</main>\n" + footer
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)

# --- Contents for Subpages ---

# 1. Event Gallery
event_gallery_content = """
<section style="padding: 80px 0; background: #f9f9f9;">
    <div class="container">
        <div class="gallery-filters" style="display: flex; justify-content: center; gap: 15px; margin-bottom: 50px;" data-aos="fade-up">
            <button class="filter-btn active">All</button>
            <button class="filter-btn">2024</button>
            <button class="filter-btn">2019</button>
            <button class="filter-btn">2018</button>
        </div>

        <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">
            <!-- Year 2024 -->
            <div class="gallery-item" data-aos="zoom-in" data-year="2024">
                <div class="gallery-card">
                    <img src="https://via.placeholder.com/400x300?text=On+Campus+Drive" alt="On Campus Drive">
                    <div class="gallery-overlay"><h4>On Campus Drive</h4><span>2024</span></div>
                </div>
            </div>
            <div class="gallery-item" data-aos="zoom-in" data-year="2024" data-aos-delay="100">
                <div class="gallery-card">
                    <img src="https://via.placeholder.com/400x300?text=Cultural+Day" alt="Cultural Day">
                    <div class="gallery-overlay"><h4>Cultural and Annual Day</h4><span>2024</span></div>
                </div>
            </div>
            <!-- Year 2019 -->
            <div class="gallery-item" data-aos="zoom-in" data-year="2019" data-aos-delay="200">
                <div class="gallery-card">
                    <img src="https://via.placeholder.com/400x300?text=Innovative+Lab" alt="Innovative Lab">
                    <div class="gallery-overlay"><h4>Innovative Lab by Dr.Mylswamy Annadurai</h4><span>2019</span></div>
                </div>
            </div>
            <div class="gallery-item" data-aos="zoom-in" data-year="2019" data-aos-delay="300">
                <div class="gallery-card">
                    <img src="https://via.placeholder.com/400x300?text=Induction+Day" alt="Induction Day">
                    <div class="gallery-overlay"><h4>Induction Day 2019</h4><span>2019</span></div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
event_css = """
.gallery-card { position: relative; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); cursor: pointer; transition: 0.4s; height: 100%; }
.gallery-card img { width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }
.gallery-card:hover img { transform: scale(1.1); }
.gallery-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,51,102,0.9), transparent); display: flex; flex-direction: column; justify-content: flex-end; padding: 20px; color: #fff; opacity: 0; transition: 0.4s; }
.gallery-card:hover .gallery-overlay { opacity: 1; }
.filter-btn { padding: 10px 25px; border-radius: 30px; border: 2px solid #003366; background: transparent; color: #003366; font-weight: 700; cursor: pointer; transition: 0.3s; }
.filter-btn.active, .filter-btn:hover { background: #003366; color: #fff; }
"""

# 2. Blog
blog_content = """
<section style="padding: 80px 0;">
    <div class="container">
        <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px;">
            <div class="blog-card" data-aos="fade-up">
                <div class="blog-img" style="height: 200px; background: #eee;"></div>
                <div class="blog-info" style="padding: 25px; background: #fff; border: 1px solid #eee; border-radius: 0 0 15px 15px;">
                    <span style="color: #f5c518; font-weight: 700;">Academic</span>
                    <h3 style="margin: 10px 0; color: #003366;">Admission Open for 2026-27</h3>
                    <p style="color: #666; font-size: 0.95rem;">Kingston Engineering College Invites applications for various UG and PG courses...</p>
                    <a href="admission.html" style="display: inline-block; margin-top: 15px; color: #003366; font-weight: 800; text-decoration: none;">Apply Now &rarr;</a>
                </div>
            </div>
            <!-- More blog cards can be added here -->
        </div>
    </div>
</section>
"""
blog_css = """
.blog-card { box-shadow: 0 15px 40px rgba(0,0,0,0.05); transition: 0.4s; border-radius: 15px; overflow: hidden; }
.blog-card:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(0,51,102,0.15); }
"""

# 3. IT Infrastructure
it_content = """
<section style="padding: 100px 0; background: #f0f4f8;">
    <div class="container">
        <div class="section-title text-center" style="margin-bottom: 60px;" data-aos="fade-down">
            <h1 style="font-size: 3rem; color: #003366; font-weight: 900;">IT Infrastructure</h1>
            <div style="width: 80px; height: 4px; background: #f5c518; margin: 20px auto;"></div>
        </div>

        <div class="it-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
            <div class="it-card" data-aos="fade-up">
                <div class="it-icon"><i class="fa-solid fa-globe"></i></div>
                <h3>Internet & Intranet</h3>
                <p>1155 Mbps 1:1 dedicated leased line connectivity. Access from more than 2000 computers across all departments.</p>
            </div>
            <div class="it-card" data-aos="fade-up" data-aos-delay="100">
                <div class="it-icon"><i class="fa-solid fa-laptop-code"></i></div>
                <h3>PCs / Laptops</h3>
                <p>More than 2000 Desktop PCs / Laptops connected through a robust fibre optic backbone.</p>
            </div>
            <div class="it-card" data-aos="fade-up" data-aos-delay="200">
                <div class="it-icon"><i class="fa-solid fa-wifi"></i></div>
                <h3>Wi-Fi Campus</h3>
                <p>Free 24x7 Wi-Fi facility covering entire campus including hostels, cafeteria, and seminar halls.</p>
            </div>
            <div class="it-card" data-aos="fade-up">
                <div class="it-icon"><i class="fa-solid fa-server"></i></div>
                <h3>Data Center</h3>
                <p>900 Sq.Ft Data Centre hosting Rack & Blade servers with uninterrupted power and 4 TB NAS storage.</p>
            </div>
            <div class="it-card" data-aos="fade-up" data-aos-delay="100">
                <div class="it-icon"><i class="fa-solid fa-shield-halved"></i></div>
                <h3>Firewall Security</h3>
                <p>Cyberoam 300ING firewall deployed for secure campus networking and load handling.</p>
            </div>
            <div class="it-card" data-aos="fade-up" data-aos-delay="200">
                <div class="it-icon"><i class="fa-solid fa-chalkboard-user"></i></div>
                <h3>ICT Facilities</h3>
                <p>Interactive panels, smartboards, and lecture capturing systems in classrooms and seminar halls.</p>
            </div>
        </div>
    </div>
</section>
"""
it_css = """
.it-card { background: #fff; padding: 40px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.05); text-align: center; transition: 0.4s; border-bottom: 5px solid transparent; }
.it-card:hover { transform: translateY(-10px); border-color: #f5c518; }
.it-icon { font-size: 3rem; color: #003366; margin-bottom: 25px; }
.it-card h3 { color: #003366; margin-bottom: 15px; font-weight: 800; }
"""

# 4. Library
library_content = """
<section style="padding: 80px 0;">
    <div class="container">
        <div class="content-card" data-aos="fade-right">
            <h2 style="color: #003366; font-size: 2.2rem; margin-bottom: 30px; border-left: 6px solid #f5c518; padding-left: 20px;">Overview</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #444;">Kingston Engineering College Library was established in the year 2008. The Learning Center gives professors, staff, researchers, and students access to a vast range of technological ideas and information. It functions on an Open Access System and is fully computerized with RFID Technology.</p>
        </div>

        <div class="rules-box" style="margin-top: 50px; background: #fffcf0; padding: 40px; border-radius: 20px; border: 1px solid #f5c518;" data-aos="fade-up">
            <h3 style="color: #003366; margin-bottom: 25px;"><i class="fa-solid fa-book-open-reader"></i> Library Rules</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 15px; display: flex; align-items: center;"><i class="fa-solid fa-check" style="color: #27ae60; margin-right: 15px;"></i> Working Hours: 08.30 A.M. to 06.30 P.M.</li>
                <li style="margin-bottom: 15px; display: flex; align-items: center;"><i class="fa-solid fa-check" style="color: #27ae60; margin-right: 15px;"></i> All books are affixed with RFID tags for automated tracking.</li>
                <li style="margin-bottom: 15px; display: flex; align-items: center;"><i class="fa-solid fa-check" style="color: #27ae60; margin-right: 15px;"></i> Online Public Access Catalogue (OPAC) available for book searches.</li>
            </ul>
        </div>
    </div>
</section>
"""
library_css = """
.stat-card { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: 0.3s; }
.stat-card:hover { background: rgba(255,255,255,0.2); transform: scale(1.05); }
.stat-card h3 { font-size: 2.5rem; color: #f5c518; margin-bottom: 10px; }
"""

# 5. Welfare Measures
welfare_content = """
<section style="padding: 100px 0; background: #fff;">
    <div class="container">
        <div class="section-title text-center" style="margin-bottom: 60px;" data-aos="fade-down">
            <h1 style="font-size: 3rem; color: #003366; font-weight: 900;">Welfare Measures</h1>
            <p style="color: #777; font-size: 1.1rem; margin-top: 10px;">Committed to the well-being and professional growth of our faculty and staff.</p>
        </div>

        <div class="welfare-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <div class="welfare-card" data-aos="fade-up">
                <i class="fa-solid fa-hand-holding-dollar"></i>
                <h4>Financial Support</h4>
                <p>EPF, ESIC, Festival Advance, Fee Concessions, and incentives for research publications.</p>
            </div>
            <div class="it-card" data-aos="fade-up" data-aos-delay="100">
                <i class="fa-solid fa-van-shuttle" style="font-size: 3rem; color: #003366; margin-bottom: 25px;"></i>
                <h4>Facilities & Amenities</h4>
                <p>Free transport, complimentary food on extra days, and individual computing systems.</p>
            </div>
            <div class="welfare-card" data-aos="fade-up" data-aos-delay="200">
                <i class="fa-solid fa-graduation-cap"></i>
                <h4>Career Progression</h4>
                <p>Support for FDPs, workshops, conferences, and a dedicated career motivation culture.</p>
            </div>
            <div class="welfare-card" data-aos="fade-up">
                <i class="fa-solid fa-heart-pulse"></i>
                <h4>Health & Family</h4>
                <p>Maternity/Paternity leave, holistic health care programs, and staff birthday celebrations.</p>
            </div>
        </div>
    </div>
</section>
"""
welfare_css = """
.welfare-card { background: #f8faff; padding: 40px; border-radius: 20px; transition: 0.4s; box-shadow: 0 10px 20px rgba(0,0,0,0.03); text-align: center; }
.welfare-card:hover { background: #003366; color: #fff; }
.welfare-card i { font-size: 3rem; color: #003366; margin-bottom: 25px; transition: 0.3s; }
.welfare-card:hover i { color: #f5c518; }
.welfare-card h4 { font-weight: 800; margin-bottom: 15px; }
"""

if __name__ == "__main__":
    generate_subpage("facilities_event_gallery.html", "Event Gallery", event_gallery_content, event_css)
    generate_subpage("blog.html", "News & Updates", blog_content, blog_css)
    generate_subpage("facilities_it.html", "IT Infrastructure", it_content, it_css)
    generate_subpage("facilities_library.html", "Library", library_content, library_css)
    generate_subpage("facilities_welfare.html", "Welfare Measures", welfare_content, welfare_css)
