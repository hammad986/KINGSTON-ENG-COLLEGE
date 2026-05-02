import os

# Read about.html structure
with open('d:/clg website new/about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the department links in the header Navigation
nav_target = """                    <li class=\"has-dropdown\">
                        <a href=\"#\">Departments</a>
                        <ul class=\"dropdown dropdown-columns\">
                            <!-- JS will populate 15 items -->
                        </ul>
                    </li>"""

nav_replacement = """                    <li class=\"has-dropdown\">
                        <a href=\"departments.html\">Departments</a>
                        <ul class=\"dropdown dropdown-columns js-exclude-dropdown\">
                            <li><a href=\"departments.html\">Computer Science and Engineering</a></li>
                            <li><a href=\"departments.html\">Bachelor of Architecture</a></li>
                            <li><a href=\"departments.html\">Computer Science Engineering with Artificial Intelligence & Machine Learning</a></li>
                            <li><a href=\"departments.html\">Electronics and Communication Engineering</a></li>
                            <li><a href=\"departments.html\">Mechanical Engineering</a></li>
                            <li><a href=\"departments.html\">Information Technology</a></li>
                            <li><a href=\"departments.html\">Artificial Intelligence and Data Science</a></li>
                            <li><a href=\"departments.html\">Computer Science and Business Systems</a></li>
                            <li><a href=\"departments.html\">Science and Humanities</a></li>
                            <li><a href=\"departments.html\">Masters in business administration</a></li>
                        </ul>
                    </li>"""

html = html.replace(nav_target, nav_replacement)

# Extract before header ends
header_end_idx = html.find('</header>') + len('</header>')
footer_start_idx = html.find('<!-- Footer -->')

before_header = html[:header_end_idx]
after_footer = html[footer_start_idx:]

dept_content = """

    <!-- Department Header Banner -->
    <section class=\"dept-hero-section\">
        <img src=\"https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1920&q=80\" alt=\"College Building\" class=\"dept-hero-img\">
        <div class=\"dept-hero-overlay\"></div>
    </section>

    <!-- Departments Grid -->
    <section class=\"dept-content-section\">
        <div class=\"container relative z-10\">
            <h2 class=\"dept-page-title\" data-aos=\"fade-up\">dept</h2>
            
            <div class=\"dept-grid\">
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"0\">
                    <i class=\"fa-solid fa-building\"></i>
                    <span>Civil Engineering</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"50\">
                    <i class=\"fa-solid fa-flask\"></i>
                    <span>Chemistry</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"100\">
                    <i class=\"fa-solid fa-desktop\"></i>
                    <span>Computer Science and Engineering</span>
                </a>
                
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"150\">
                    <i class=\"fa-solid fa-laptop\"></i>
                    <span>Computer Science and Business Systems</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"200\">
                    <i class=\"fa-solid fa-laptop-code\"></i>
                    <span>Computer Applications</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"250\">
                    <i class=\"fa-solid fa-database\"></i>
                    <span>Applied Mathematics and Computational Science</span>
                </a>
                
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"300\">
                    <i class=\"fa-solid fa-wifi\"></i>
                    <span>Electronics and Communication Engineering</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"350\">
                    <i class=\"fa-solid fa-microchip\"></i>
                    <span>Electrical and Electronics Engineering</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"400\">
                    <i class=\"fa-solid fa-spell-check\"></i>
                    <span>English</span>
                </a>
                
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"450\">
                    <i class=\"fa-solid fa-mobile-screen\"></i>
                    <span>Information Technology</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"500\">
                    <i class=\"fa-solid fa-list-ol\"></i>
                    <span>Mathematics</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"550\">
                    <i class=\"fa-solid fa-car-side\"></i>
                    <span>Mechanical Engineering</span>
                </a>
                
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"600\">
                    <i class=\"fa-solid fa-robot\"></i>
                    <span>Mechatronics</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"650\">
                    <i class=\"fa-solid fa-atom\"></i>
                    <span>Physics</span>
                </a>
                <a href=\"#\" class=\"dept-card\" data-aos=\"fade-up\" data-aos-delay=\"700\">
                    <i class=\"fa-solid fa-archway\"></i>
                    <span>T'SEDA (Architecture, Design, Planning)</span>
                </a>
            </div>

            <div class=\"dept-actions\" data-aos=\"fade-up\" data-aos-delay=\"200\">
                <a href=\"#\" class=\"btn-dept-action\">QUICK LINKS</a>
                <a href=\"#\" class=\"btn-dept-action outline-action\">EXPLORE</a>
            </div>
        </div>
    </section>

    """

# Also change the page title
new_html = before_header.replace('<title>About Us - Kingston Engineering College</title>', '<title>Departments - Kingston Engineering College</title>') + dept_content + after_footer

# Change active class in nav
new_html = new_html.replace('<a href="about.html" class="active">About Us</a>', '<a href="about.html">About Us</a>')
new_html = new_html.replace('<a href="departments.html">Departments</a>', '<a href="departments.html" class="active">Departments</a>')

with open('d:/clg website new/departments.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Also update index.html nav
with open('d:/clg website new/index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()
idx_html = idx_html.replace(nav_target, nav_replacement)
with open('d:/clg website new/index.html', 'w', encoding='utf-8') as f:
    f.write(idx_html)

# Also update about.html nav
with open('d:/clg website new/about.html', 'r', encoding='utf-8') as f:
    abt_html = f.read()
abt_html = abt_html.replace(nav_target, nav_replacement)
with open('d:/clg website new/about.html', 'w', encoding='utf-8') as f:
    f.write(abt_html)

print("Generated departments.html and updated global navigation.")
