import os
import re

print("Starting IT multipage generation with highly animated graphics...")

# Use dept_cse.html as the base boilerplate.
base_file = "dept_cse.html"
with open(base_file, "r", encoding="utf-8") as f:
    base_html = f.read()

# Isolate header and footer wrappers
start_wrap = base_html.split('<div class="dept-details-wrapper">')[0] + '<div class="dept-details-wrapper">\n\n'
end_wrap = '\n    </div>\n\n    <!-- Footer -->\n    <footer class="main-footer">' + base_html.split('<!-- Footer -->\n    <footer class="main-footer">')[1]


it_sidebar = """        <aside class="dept-sidebar">
            <ul class="dept-sidebar-menu">
                <li><a href="it_about.html"><i class="fa-solid fa-house"></i> About the Department & Labs</a></li>
                <li><a href="it_vision_mission.html"><i class="fa-solid fa-bullseye"></i> Vision and Mission</a></li>
                <li><a href="it_peos.html"><i class="fa-regular fa-file-lines"></i> PEOs & Outcomes</a></li>
                <li><a href="it_faculty.html"><i class="fa-solid fa-user-tie"></i> Faculty</a></li>
                <li><a href="it_board_of_studies.html"><i class="fa-solid fa-graduation-cap"></i> Board of Studies</a></li>
                <li><a href="it_curriculum.html"><i class="fa-solid fa-book-open"></i> Curriculum</a></li>
                <li><a href="it_academic_calendar.html"><i class="fa-regular fa-calendar-days"></i> Academic Calendar</a></li>
                <li><a href="it_timetable.html"><i class="fa-solid fa-table-cells"></i> Time Table</a></li>
                <li><a href="it_coe.html"><i class="fa-solid fa-trophy"></i> Centre of Excellence</a></li>
                <li><a href="it_faculty_achievements.html"><i class="fa-solid fa-medal"></i> Faculty Achievements</a></li>
                <li><a href="it_events.html"><i class="fa-regular fa-calendar-check"></i> Events & FDPs</a></li>
                <li><a href="it_industry_visits.html"><i class="fa-solid fa-building"></i> Industry Visits</a></li>
                <li><a href="it_student_achievements.html"><i class="fa-solid fa-trophy"></i> Student Tech Achievements</a></li>
                <li><a href="it_toppers.html"><i class="fa-solid fa-award"></i> Toppers List</a></li>
                <li><a href="it_placement.html"><i class="fa-solid fa-briefcase"></i> Placement</a></li>
                <li><a href="it_newsletter.html"><i class="fa-regular fa-newspaper"></i> Newsletters & Magazines</a></li>
                <li><a href="it_contact.html"><i class="fa-solid fa-envelope"></i> Contact Us</a></li>
            </ul>
        </aside>
"""

custom_css = """
<style>
/* Supreme Glassmorphic Card */
.glass-card-premium {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 30px;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}
.glass-card-premium::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 50%; height: 100%;
    background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) 50%, rgba(255,255,255,0) 100%);
    transform: skewX(-25deg);
    transition: all 0.7s ease;
}
.glass-card-premium:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 50px rgba(0, 51, 102, 0.2);
    border-color: rgba(163, 31, 36, 0.4);
}
.glass-card-premium:hover::before {
    left: 200%;
}

/* Cyber/Lab Specs Card */
.lab-card {
    background: linear-gradient(145deg, #1A1A2E, #16213E);
    color: #E94560;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    border-left: 5px solid #0F3460;
    box-shadow: 0 8px 32px rgba(22, 33, 62, 0.5);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.lab-card:hover {
    transform: scale(1.03);
    box-shadow: 0 12px 40px rgba(233, 69, 96, 0.3);
    border-left: 5px solid #E94560;
}
.lab-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #FFFFFF;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.lab-spec {
    font-family: 'Courier New', monospace;
    font-size: 1rem;
    color: #00FFCC;
    background: rgba(0,0,0,0.4);
    padding: 10px;
    border-radius: 5px;
}

/* Event Timelines */
.event-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
}
.event-box {
    background: #fff;
    border-radius: 12px;
    padding: 20px;
    border-top: 4px solid #a31f24;
    box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    transition: transform 0.3s ease;
}
.event-box:hover {
    transform: translateY(-5px);
}
.event-date {
    display: inline-block;
    padding: 5px 12px;
    background: #fdf5f5;
    color: #a31f24;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.85rem;
    margin-bottom: 15px;
}

/* Animated Student Achievement Grid */
.achievement-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
}
.achieve-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(240,240,250,0.9));
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    border: 1px solid rgba(0, 51, 102, 0.1);
    position: relative;
    overflow: hidden;
    transition: all 0.3s;
}
.achieve-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    background: linear-gradient(135deg, rgba(255,255,255,1), rgba(255,255,255,1));
}
.achieve-card::after {
    content: '\\f091';
    font-family: "Font Awesome 6 Free";
    font-weight: 900;
    position: absolute;
    bottom: -20px;
    right: -20px;
    font-size: 6rem;
    color: rgba(163, 31, 36, 0.05);
    transform: rotate(-15deg);
    transition: all 0.5s;
}
.achieve-card:hover::after {
    color: rgba(245, 197, 24, 0.2);
    transform: rotate(0deg) scale(1.1);
}
.student-name {
    color: #003366;
    font-weight: 800;
    font-size: 1.2rem;
    margin-bottom: 10px;
    border-bottom: 2px solid #a31f24;
    display: inline-block;
    padding-bottom: 5px;
}
.prize-item {
    margin-top: 10px;
    display: flex;
    align-items: flex-start;
    gap: 10px;
}
.prize-badge {
    background: #f5c518;
    color: #000;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: bold;
    white-space: nowrap;
}

/* Faculty Table */
.pub-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin-top: 15px;
    font-size: 0.95rem;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.pub-table th {
    background: #003366;
    color: white;
    padding: 15px;
    text-align: left;
}
.pub-table td {
    padding: 15px;
    border-bottom: 1px solid #eee;
    background: #fff;
    color: #444;
}
.pub-table tr:hover td {
    background: #fdf5f5;
}

.pdf-btn {
    display: inline-block;
    padding: 10px 20px;
    background: #a31f24;
    color: white !important;
    text-decoration: none;
    border-radius: 5px;
    transition: 0.3s;
    font-weight: 600;
}
.pdf-btn:hover {
    background: #003366;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
</style>
"""

pages = {
    'it_about.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">DEPARTMENT OF<br>INFORMATION TECHNOLOGY</h1>
            <section class="dept-section" data-aos="fade-up" data-aos-delay="100">
                <h3>DEPARTMENT INTRODUCTION</h3>
                <div class="glass-card-premium">
                    <p>The Department of Information Technology was established in the year 2008 with an intake of 60 students. Our vision and mission focus towards academic excellence along with emerging technologies. We adhere to the Anna University curriculum as an affiliated institution. The department provides an environment towards collaborative research by guiding students in developing solutions to meet industry or society needs. The department has been achieving consistently good placement and academic records.</p>
                    <p>The main objective is to motivate the students to excel in basic engineering skills and mould them as good technocrats through futuristic plans. We also provide continuous exposure on current trends and tools through practical hours and workshops in which the collaboration from industry people is in place.</p>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up" data-aos-delay="200">
                <h3>ADVANCED LABORATORY CONFIGURATIONS</h3>
                <div class="grid-2">
                    <div class="lab-card" data-aos="zoom-in" data-aos-delay="300">
                        <div class="lab-title"><i class="fa-solid fa-database"></i> Data Structures Lab</div>
                        <div class="lab-spec">Processor: AMD Ryzen 3 / 3.60 GHz<br>Memory: 8 GB RAM<br>Storage: 480 GB SSD</div>
                    </div>
                    <div class="lab-card" data-aos="zoom-in" data-aos-delay="400">
                        <div class="lab-title"><i class="fa-solid fa-sitemap"></i> Object Oriented Analysis & Design Lab</div>
                        <div class="lab-spec">Processor: AMD Ryzen 3 / 3.60 GHz<br>Memory: 8 GB RAM<br>Storage: 480 GB SSD</div>
                    </div>
                    <div class="lab-card" data-aos="zoom-in" data-aos-delay="500">
                        <div class="lab-title"><i class="fa-solid fa-globe"></i> Web Technology Lab</div>
                        <div class="lab-spec">Processor: Intel i3 10th Gen / 3.70 GHz<br>Memory: 8 GB RAM<br>Storage: 480 GB SSD</div>
                    </div>
                </div>
            </section>''',

    'it_vision_mission.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">VISION AND MISSION</h1>
            <section class="dept-section" data-aos="fade-right">
                <h3>VISION OF THE INSTITUTION</h3>
                <div class="glass-card-premium" style="border-left: 5px solid #f5c518;">
                    <p>To provide quality education to the students and impart IT excellence by building strong academic environment and to enable the essential skills in the innovators and entrepreneurs making them as proficient professionals for industrial consultancy.</p>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-left">
                <h3>MISSION OF THE INSTITUTION</h3>
                <div class="glass-card-premium" style="border-left: 5px solid #a31f24;">
                    <ul style="line-height:1.8;">
                        <li><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> <strong>Developing innovative, competent computer engineers</strong> through planning, in-depth analysis, and hands-on problem solving in the quest for the students to work with emerging technologies.</li>
                        <li><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> <strong>Inculcating a learning environment</strong> and upgrade the knowledge of students through value-based education and promotes the academic excellence.</li>
                        <li><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> <strong>Providing leadership and ethical values</strong> for effective deliberate and tactical planning to cater the needs of the Society and to Prepare students for professional career and higher studies and promoting innovative research and education programs in the IT field.</li>
                    </ul>
                </div>
            </section>''',

    'it_peos.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">PROGRAM EDUCATIONAL OBJECTIVES (PEOs)</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="glass-card-premium">
                    <ul style="line-height:2;">
                        <li><strong style="color:#a31f24;">PEO 1 (Fundamental Knowledge):</strong> To ensure graduates will be proficient in utilizing the fundamental knowledge of basic sciences, mathematics and Information Technology for the applications relevant to various streams of Engineering and Technology.</li>
                        <li><strong style="color:#a31f24;">PEO 2 (Core Competencies):</strong> To enrich graduates with the core competencies necessary for applying knowledge of computers and telecommunications equipment to store, retrieve, transmit, manipulate and analyze data in the context of business enterprise.</li>
                        <li><strong style="color:#a31f24;">PEO 3 (Life-Long Learning):</strong> To enable graduates to think logically, pursue life-long learning and will have the capacity to understand technical issues related to computing systems and to design optimal solutions.</li>
                        <li><strong style="color:#a31f24;">PEO 4 (Professional Career):</strong> To enable graduates to develop hardware and software systems by understanding the importance of social, business and environmental needs in the human context.</li>
                        <li><strong style="color:#a31f24;">PEO 5 (Multifaceted Aspects):</strong> To enable graduates to gain employment in organizations and establish themselves as professionals by applying their technical skills to solve real world problems and meet the diversified needs of industry, academia and research.</li>
                    </ul>
                </div>
            </section>''',

    'it_faculty.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">DEPARTMENT FACULTY</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY LIST</h3>
                <div class="table-responsive" style="margin-top:20px;">
                    <table class="pub-table">
                        <thead>
                            <tr>
                                <th>Name of the Staff</th>
                                <th>Designation</th>
                                <th>Qualification</th>
                                <th>Specialization</th>
                                <th>E-Mail ID</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Mrs. Menaka M</strong></td><td>HoD / Assistant Professor</td><td>M.E</td><td>Artificial Intelligence, Data Science</td><td>menaka@kingston.ac.in</td></tr>
                            <tr><td><strong>Mrs. Sarah S</strong></td><td>Assistant Professor</td><td>M.E</td><td>Deep Learning, Network Security</td><td>sarah@kingston.ac.in</td></tr>
                            <tr><td><strong>Mrs. Deepa U</strong></td><td>Assistant Professor</td><td>M.Tech</td><td>Mobile Computing, Image Processing</td><td>deepa.engineering@kingston.ac.in</td></tr>
                            <tr><td><strong>Dr. Vasumathy M</strong></td><td>Associate Professor</td><td>M.S(SE)., P.hD</td><td>Data Science & Machine Learning</td><td>vasumathy.engineering@kingston.ac.in</td></tr>
                            <tr><td><strong>Mr. Gajendiran K S</strong></td><td>Assistant Professor</td><td>M.Tech</td><td>Data Science & Machine Learning</td><td>gajendiran@kingston.ac.in</td></tr>
                            <tr><td><strong>Ms. Nathiya S</strong></td><td>Assistant Professor</td><td>M.E</td><td>Artificial Intelligence, Data Analytics</td><td>nathiya.engineering@kingston.ac.in</td></tr>
                            <tr><td><strong>Ms. Vishnupriya R</strong></td><td>Assistant Professor</td><td>M.E</td><td>Computer Networks, AI</td><td>vishnupriya.engineering@kingston.ac.in</td></tr>
                            <tr><td><strong>Mrs. Priyadharshini B S</strong></td><td>Assistant Professor</td><td>M.E</td><td>Network Security, Image Processing</td><td>priyaadarshini.engineering@kingston.ac.in</td></tr>
                            <tr><td><strong>Mrs. Bharathi M</strong></td><td>Assistant Professor</td><td>M.E</td><td>Deep Learning, Network Security</td><td>bharathi2528@gmail.com</td></tr>
                        </tbody>
                    </table>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up" data-aos-delay="300">
                <h3>FACULTY REFERENCE DOCUMENT</h3>
                <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/UGC Mandatory Disclosure/3. Academics/4. Dept Faculty Details/IT Staff Details.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>''',

    'it_faculty_achievements.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">FACULTY ACHIEVEMENTS</h1>
            
            <section class="dept-section" data-aos="fade-right">
                <h3>PATENTS PUBLISHED</h3>
                <div class="glass-card-premium" style="border-left: 5px solid #f5c518;">
                    <h4>Mrs. Menaka M</h4>
                    <ul>
                        <li><i class="fa-solid fa-certificate" style="color:#f5c518;"></i> <strong>Design and Implementation of the Inventory Management System</strong> (Application: 202341034506) - Published 16-06-2023</li>
                        <li style="margin-top:8px;"><i class="fa-solid fa-certificate" style="color:#f5c518;"></i> <strong>QR Code Controlled Clever Cookies/Beverages Vending Machine</strong> and Auto Payable Option Using UPI Payments Application (Application: 202341027064) - Published 05-05-2023</li>
                    </ul>
                    <hr style="margin:20px 0; border:0; border-top:1px solid rgba(0,0,0,0.1);">
                    <h4>Mrs. Sarah S</h4>
                    <ul>
                        <li><i class="fa-solid fa-certificate" style="color:#f5c518;"></i> <strong>Cancer Cell Detection Device</strong> (Design No: 387009-001) - Published 18-08-2023</li>
                    </ul>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-left">
                <h3>IEEE PUBLICATIONS & CONFERENCE PAPERS</h3>
                <div class="grid-2">
                    <div class="event-box">
                        <div class="event-title" style="color:#003366;">A Combination of Cloud Radio Accessing Networks and Mobile Cloud Computing</div>
                        <div style="font-size:0.9rem; color:#666; margin:8px 0;"><strong>Mrs. Menaka M</strong> | IEEE Conference (July 2023)</div>
                        <code style="background:#f1f1f1; padding:2px 5px; border-radius:3px; font-size:0.8rem;">DOI: 10.1109/ICESC57686.2023.10193219</code>
                    </div>
                    <div class="event-box">
                        <div class="event-title" style="color:#003366;">Forecasting Naturally Occurring Forest Fires using AI and Machine Learning</div>
                        <div style="font-size:0.9rem; color:#666; margin:8px 0;"><strong>Mrs. Menaka M</strong> | IEEE Conference (August 2023)</div>
                        <code style="background:#f1f1f1; padding:2px 5px; border-radius:3px; font-size:0.8rem;">DOI: 10.1109/ICIRCA57980.2023.10220860</code>
                    </div>
                    <div class="event-box">
                        <div class="event-title" style="color:#003366;">Blockchain Technology Based Privacy Protection Scheme</div>
                        <div style="font-size:0.9rem; color:#666; margin:8px 0;"><strong>Mrs. Menaka M</strong> | IEEE Conference (August 2023)</div>
                        <code style="background:#f1f1f1; padding:2px 5px; border-radius:3px; font-size:0.8rem;">DOI: 10.1109/ICIRCA57980.2023.10220586</code>
                    </div>
                    <div class="event-box">
                        <div class="event-title" style="color:#003366;">Predictive Policing: Harnessing Machine Learning for Crime Forecasting</div>
                        <div style="font-size:0.9rem; color:#666; margin:8px 0;"><strong>Mrs. Sarah S</strong> | IC2ACM-2023 (December 2023)</div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>OTHER FACULTY PARTICIPATIONS</h3>
                <div class="glass-card-premium">
                    <p><i class="fa-solid fa-star" style="color:#a31f24;"></i> <strong>Mrs. Sarah S</strong> acted as a Jury member for the Student Innovation and Development Programme for Vellore and Ranipet District Level Bootcamp for School Students Projects organized by EDII, Govt of Tamil Nadu (Feb 2024).</p>
                    <p><i class="fa-solid fa-star" style="color:#a31f24;"></i> <strong>Mrs. Sarah S</strong> was a Niral Thiruvizha Project Mentor, receiving a fund of ₹10,000 for the project titled "Gamified App for Learning by PwDs" (March 2024).</p>
                    <p><i class="fa-solid fa-star" style="color:#a31f24;"></i> <strong>Mrs. Menaka M</strong> acted as Resource Person, Robo Talento Competition at FIITJEE Global Public School.</p>
                </div>
            </section>''',

    'it_events.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">GUEST LECTURES, FDPs & EVENTS</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="event-grid">
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="100">
                        <span class="event-date">March 21 - 25, 2024</span>
                        <div class="event-title">Exploring Frontiers of AI Computing & Technologies (EFACT’24)</div>
                        <p style="font-size:0.9rem; color:#555;">Faculty Development Program featuring guests from MSC Tech, NIT-Puducherry, ATE-Machine Vision Systems, and ATOS.</p>
                    </div>
                    
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="200">
                        <span class="event-date">April 18, 2024</span>
                        <div class="event-title">TechXperience with REST APIs for Application Development</div>
                        <p style="font-size:0.9rem; color:#555;">Virtual workshop conducted by Alumni Mr. Dhanush Ram, Senior Software Engineer at CRUX Digital, Bangalore.</p>
                    </div>
                    
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="300">
                        <span class="event-date">February 8, 2024</span>
                        <div class="event-title">Cybercrime Awareness: Cyber Resilience Navigation</div>
                        <p style="font-size:0.9rem; color:#555;">Held for students with a drawing competition on cybercrime awareness involving HODs of Mechanical and ECE.</p>
                    </div>
                    
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="400">
                        <span class="event-date">January 30 - Feb 3, 2024</span>
                        <div class="event-title">Art of Generative AI Algorithms and Applications</div>
                        <p style="font-size:0.9rem; color:#555;">5-day intensive Value-Added Course on GenAI.</p>
                    </div>
                    
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="500">
                        <span class="event-date">November 20-21, 2023</span>
                        <div class="event-title">Cambridge English - Naan Mudhalvan Initiative</div>
                        <p style="font-size:0.9rem; color:#555;">FDP featuring Ms. Scharada Dubey, author and communication consultant from Bengaluru.</p>
                    </div>
                    
                    <div class="event-box" data-aos="zoom-in" data-aos-delay="600">
                        <span class="event-date">May 29, 2024</span>
                        <div class="event-title">Naan Mudhalvan State-wide Placement Drive</div>
                        <p style="font-size:0.9rem; color:#555;">State Level Job fair where 106 job offers were made by 19 different participating companies.</p>
                    </div>
                </div>
            </section>''',

    'it_industry_visits.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">INDUSTRIAL VISITS</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="glass-card-premium">
                    <div style="display:flex; align-items:center; gap:20px; margin-bottom:20px; border-bottom:1px solid rgba(0,0,0,0.1); padding-bottom:15px;">
                        <i class="fa-solid fa-ship" style="font-size:2.5rem; color:#003366;"></i>
                        <div>
                            <h3 style="margin:0; color:#a31f24;">MSC Technology, Chennai</h3>
                            <p style="margin:5px 0 0; color:#555;"><strong>Date:</strong> September 14, 2023</p>
                            <p style="margin:0; color:#777; font-size:0.9rem;">Participants: III Year IT and IV Year IT students.</p>
                        </div>
                    </div>
                    
                    <div style="display:flex; align-items:center; gap:20px;">
                        <i class="fa-solid fa-microchip" style="font-size:2.5rem; color:#003366;"></i>
                        <div>
                            <h3 style="margin:0; color:#a31f24;">Visvesvaraya Industrial and Technological Park, Bengaluru</h3>
                            <p style="margin:5px 0 0; color:#555;"><strong>Date:</strong> March 4, 2024</p>
                            <p style="margin:0; color:#777; font-size:0.9rem;">Participants: III Year IT students.</p>
                        </div>
                    </div>
                </div>
            </section>''',

    'it_student_achievements.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">STUDENT TECHNICAL ACHIEVEMENTS</h1>
            <h4 style="text-align:center; color:#555; margin-bottom:40px;" data-aos="fade-up">Awards won across numerous Technical Symposiums & Hackathons</h4>
            
            <section class="dept-section">
                <div class="achievement-grid">
                
                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="0">
                        <div class="student-name">Rohan Samuel J (III Year)</div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Code-athon (Dhanish Ahmed College)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Connexion (Dhanish Ahmed College)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Coding & Debugging (NEXUS 2K24, Kongu Engineering)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Triumph Journey (NEXUS 2K24, Kongu Engineering)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Code Crafters Summit (Electrofocus'24, MIT Anna Univ)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Fault Fix Fiesta (Electrofocus'24, MIT Anna Univ)</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Code Class with Python</span></div>
                    </div>

                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="100">
                        <div class="student-name">Nithyasree G (III Year)</div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Script Debugging (Tech Spark'23)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Code Dilemma (TPGIT, ALGOTRON)</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Web Crafting (Tech Spark'23)</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Web Design (INFOGRAM'23, CAHCET)</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:#cd7f32;">3rd Prize</span> <span>Visual Vision 2K24</span></div>
                    </div>

                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="200">
                        <div class="student-name">Shree Varshenee K (III Year)</div>
                        <div class="prize-item"><span class="prize-badge">World Record</span> <span>Classical Dance - Arunachaleswarar Temple</span></div>
                        <div class="prize-item"><span class="prize-badge">Award</span> <span>Nattiya Mangai Award'23</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Treasure Hunt (Zenithrive, AMCET)</span></div>
                        <div class="prize-item"><span class="prize-badge">Distinction</span> <span>Bharathanatyam Grade-II & I Exam</span></div>
                    </div>

                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="300">
                        <div class="student-name">Rajeshwari S (II Year)</div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Tongue Twister (Global Cognizance'23)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>Paper Demonstration (Tech Spark'23)</span></div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Badminton (Annual Sports Meet'23)</span></div>
                    </div>
                    
                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="400">
                        <div class="student-name">Gayathri S (III Year)</div>
                        <div class="prize-item"><span class="prize-badge" style="background:silver;">2nd Prize</span> <span>Script Debugging (Tech Spark'23)</span></div>
                        <div class="prize-item"><span class="prize-badge">1st Class</span> <span>Tamil Typewriting</span></div>
                    </div>
                    
                    <div class="achieve-card" data-aos="zoom-in" data-aos-delay="500">
                        <div class="student-name">Pon Lavanya S (III Year)</div>
                        <div class="prize-item"><span class="prize-badge">1st Prize</span> <span>SDG Quiz (MGR IGEN ENSAV CLUB)</span></div>
                    </div>

                </div>
            </section>''',

    'it_toppers.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">TOPPERS & RANK HOLDERS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>ANNA UNIVERSITY EXAMINATIONS TOPPERS (2023-2024)</h3>
                <div class="grid-2" style="margin-top:20px;">
                    <!-- Second Year -->
                    <div class="glass-card-premium" style="text-align:center;">
                        <h4 style="color:#003366; border-bottom:2px solid; padding-bottom:10px;">II Year (Semester 3)</h4>
                        <div style="margin:15px 0;">
                            <h2 style="color:#a31f24; margin:0;">BARATH M</h2>
                            <p><strong>Rank 1</strong></p>
                        </div>
                        <div style="margin:15px 0;">
                            <h3 style="color:#a31f24; margin:0;">RITHICK R</h3>
                            <p>Rank 2</p>
                        </div>
                        <div style="margin:15px 0;">
                            <h3 style="color:#a31f24; margin:0;">LOKESH A</h3>
                            <p>Rank 3</p>
                        </div>
                    </div>
                    
                    <!-- Third Year -->
                    <div class="glass-card-premium" style="text-align:center;">
                        <h4 style="color:#003366; border-bottom:2px solid; padding-bottom:10px;">III Year (Semester 5)</h4>
                        <div style="margin:15px 0;">
                            <h2 style="color:#a31f24; margin:0;">MALAIYARASI M</h2>
                            <p><strong>Rank 1</strong></p>
                        </div>
                        <div style="margin:15px 0;">
                            <h3 style="color:#a31f24; margin:0;">SOWMIYA G</h3>
                            <p>Rank 2</p>
                        </div>
                        <div style="margin:15px 0;">
                            <h3 style="color:#a31f24; margin:0;">SARAVANAN C</h3>
                            <p>Rank 3</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>BEST OUTGOING STUDENTS (NOV/DEC 2023)</h3>
                <div class="grid-2">
                    <div class="lab-card" style="align-items:center; text-align:center;">
                        <i class="fa-solid fa-user-graduate" style="font-size:3rem; margin-bottom:10px; color:#f5c518;"></i>
                        <h2 style="color:white; margin:0;">YESWANTH M</h2>
                        <p style="color:#00FFCC; margin:0;">Male Category</p>
                        <p style="color:#aaa; font-size:0.8rem;">IV IT - Reg No: 511320205033</p>
                    </div>
                    <div class="lab-card" style="align-items:center; text-align:center;">
                        <i class="fa-solid fa-user-graduate" style="font-size:3rem; margin-bottom:10px; color:#f5c518;"></i>
                        <h2 style="color:white; margin:0;">NISHA V</h2>
                        <p style="color:#00FFCC; margin:0;">Female Category</p>
                        <p style="color:#aaa; font-size:0.8rem;">IV IT - Reg No: 511320205019</p>
                    </div>
                </div>
            </section>''',

    'it_newsletter.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">NEWSLETTER AND MAGAZINES</h1>
            <section class="dept-section" data-aos="fade-up">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                    <h3>IT NEWSLETTER (JULY 2023 - JUNE 2024)</h3>
                    <a href="college-detail/Autonomous/News Letter/IT.pdf" download class="pdf-btn"><i class="fa-solid fa-download"></i> Download PDF</a>
                </div>
                <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.15);">
                    <iframe src="college-detail/Autonomous/News Letter/IT.pdf" width="100%" height="850px" style="border: none;"></iframe>
                </div>
            </section>''',

    'it_academic_calendar.html': f'''
            <h1 class="dept-title-red" data-aos="fade-down">ACADEMIC CALENDAR</h1>
            <section class="dept-section" data-aos="fade-up">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                    <h3>IT ACADEMIC CALENDAR</h3>
                    <a href="assets/it/academic_calendar.pdf" download class="pdf-btn"><i class="fa-solid fa-download"></i> Download PDF</a>
                </div>
                <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.15);">
                    <iframe src="assets/it/academic_calendar.pdf" width="100%" height="850px" style="border: none;"></iframe>
                </div>
            </section>'''
}

# The remaining placeholder blank pages
empty_pages = {
    'it_board_of_studies.html': 'BOARD OF STUDIES',
    'it_curriculum.html': 'CURRICULUM & SYLLABUS',
    'it_timetable.html': 'TIME TABLE',
    'it_coe.html': 'CENTRE OF EXCELLENCE',
    'it_placement.html': 'PLACEMENT',
    'it_contact.html': 'CONTACT US'
}

for e_p, title in empty_pages.items():
    pages[e_p] = f'''
            <h1 class="dept-title-red" data-aos="fade-up">{title}</h1>
            <section class="dept-section" data-aos="fade-up">
                <!-- Content to be added later -->
            </section>
'''

# We also want dept_it.html to be identical to it_about.html
pages['dept_it.html'] = pages['it_about.html']

for filename, main_content in pages.items():
    # Inject CSS
    final_main = custom_css + '\n' + f'<main class="dept-main-content">\n{main_content}\n</main>'
    
    # Process sidebar active link
    current_sidebar = it_sidebar.replace(f'href="{filename}"', f'href="{filename}" class="active"')
    
    # Assemble the full HTML
    full_html = start_wrap + current_sidebar + '\n' + final_main + end_wrap
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)

print(f"Generated {len(pages)} IT pages with highly animated UI successfully!")
