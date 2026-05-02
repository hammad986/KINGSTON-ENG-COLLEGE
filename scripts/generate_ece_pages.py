import os
import re

print("Starting ECE multipage generation...")

# We will use dept_cse.html as our base template to grab the generic top-bar, header, footer.
base_file = "dept_cse.html"
with open(base_file, "r", encoding="utf-8") as f:
    base_html = f.read()

# Split around the sidebar and main content
# The wrapper is <div class="dept-details-wrapper">
start_wrap = base_html.split('<div class="dept-details-wrapper">')[0] + '<div class="dept-details-wrapper">\n\n'
end_wrap = '\n    </div>\n\n    <!-- Footer -->\n    <footer class="main-footer">' + base_html.split('<!-- Footer -->\n    <footer class="main-footer">')[1]


ece_sidebar = """        <aside class="dept-sidebar">
            <ul class="dept-sidebar-menu">
                <li><a href="ece_about.html"><i class="fa-solid fa-house"></i> About the Department</a></li>
                <li><a href="ece_vision_mission.html"><i class="fa-solid fa-bullseye"></i> Vision and Mission</a></li>
                <li><a href="ece_peos.html"><i class="fa-regular fa-file-lines"></i> PEOs, POs and PSOs</a></li>
                <li><a href="ece_faculty.html"><i class="fa-solid fa-user-tie"></i> Faculty</a></li>
                <li><a href="ece_board_of_studies.html"><i class="fa-solid fa-graduation-cap"></i> Board of Studies</a></li>
                <li><a href="ece_curriculum.html"><i class="fa-solid fa-book-open"></i> Curriculum</a></li>
                <li><a href="ece_academic_calendar.html"><i class="fa-regular fa-calendar-days"></i> Department Academic Calendar</a></li>
                <li><a href="ece_timetable.html"><i class="fa-solid fa-table-cells"></i> Time Table</a></li>
                <li><a href="ece_coe.html"><i class="fa-solid fa-trophy"></i> Centre of Excellence (4G/5G Lab)</a></li>
                <li><a href="ece_faculty_achievements.html"><i class="fa-solid fa-medal"></i> Faculty Achievements</a></li>
                <li><a href="ece_faculty_upskilling.html"><i class="fa-solid fa-arrow-trend-up"></i> Faculty Upskilling</a></li>
                <li><a href="ece_events.html"><i class="fa-regular fa-calendar-check"></i> Events Organized</a></li>
                <li><a href="ece_innovations.html"><i class="fa-solid fa-lightbulb"></i> Innovations & Hackathons</a></li>
                <li><a href="ece_sports.html"><i class="fa-solid fa-basketball"></i> Sports Achievements</a></li>
                <li><a href="ece_student_participations.html"><i class="fa-solid fa-users-viewfinder"></i> Student Participations</a></li>
                <li><a href="ece_toppers.html"><i class="fa-solid fa-medal"></i> Toppers List</a></li>
                <li><a href="ece_industry_visits.html"><i class="fa-solid fa-building"></i> Industry Visits</a></li>
                <li><a href="ece_placement.html"><i class="fa-solid fa-briefcase"></i> Placement</a></li>
                <li><a href="ece_distinguished_alumni.html"><i class="fa-solid fa-star"></i> Distinguished Alumni</a></li>
                <li><a href="ece_student_publications.html"><i class="fa-solid fa-newspaper"></i> Student Publications</a></li>
                <li><a href="ece_online_courses.html"><i class="fa-solid fa-laptop"></i> Online Courses</a></li>
                <li><a href="ece_newsletter.html"><i class="fa-regular fa-newspaper"></i> Newsletter and Magazines</a></li>
                <li><a href="ece_contact.html"><i class="fa-solid fa-envelope"></i> Contact Us</a></li>
            </ul>
        </aside>
"""

custom_css = """
<style>
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
    padding: 24px;
    border-radius: 12px;
    margin-bottom: 24px;
    transition: transform 0.3s ease, border-color 0.3s ease;
}
.glass-card:hover {
    transform: translateY(-5px);
    border-color: rgba(163, 31, 36, 0.3);
}
.event-card {
    display: flex;
    flex-direction: column;
    padding: 20px;
    background: linear-gradient(145deg, #ffffff, #f8f9fa);
    border-left: 4px solid #a31f24;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}
.event-card:hover {
    box-shadow: 0 8px 25px rgba(163, 31, 36, 0.15);
    transform: translateX(5px);
}
.event-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #003366;
    margin-bottom: 8px;
}
.event-meta {
    font-size: 0.9rem;
    color: #666;
    display: flex;
    gap: 15px;
    align-items: center;
}
.pub-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
    font-size: 0.95rem;
}
.pub-table th {
    background: #a31f24;
    color: white;
    padding: 12px 15px;
    text-align: left;
}
.pub-table td {
    padding: 12px 15px;
    border-bottom: 1px solid #ddd;
    color: #444;
}
.pub-table tr:hover td {
    background: #fdf5f5;
}
.hero-innovate {
    background: linear-gradient(135deg, #003366, #a31f24);
    color: white;
    padding: 40px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(163, 31, 36, 0.3);
}
.hero-innovate h2 {
    font-size: 2.5rem;
    margin-bottom: 15px;
    color: #f5c518;
}
.hero-innovate p {
    font-size: 1.2rem;
    opacity: 0.9;
}
.pdf-btn {
    display: inline-block;
    padding: 10px 20px;
    background: #003366;
    color: white !important;
    text-decoration: none;
    border-radius: 5px;
    transition: 0.3s;
    font-weight: 500;
}
.pdf-btn:hover {
    background: #a31f24;
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
@media (max-width: 768px) {
    .grid-2 {
        grid-template-columns: 1fr;
    }
}
</style>
"""

pages = {
    'ece_about.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT OF<br>ELECTRONICS AND COMMUNICATION ENGINEERING</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>DEPARTMENT INTRODUCTION</h3>
                <div class="glass-card">
                    <p>The Department has fully equipped state-of-the-art laboratories and highly qualified and dedicated faculty with international reputation. The department functions with efficient faculty and well equipped lab facilities. It has conducted many technical symposium and workshops. Extensive laboratory facilities for various labs including VLSI, Communication, Networking, DSP& Signal processing, Microprocessors etc. are available.</p>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up">
                <h3>OBJECTIVES</h3>
                <div class="glass-card">
                    <p>To establish our department as a premiere center of educational excellence by providing a student-centered learning environment that is committed to changing the destinies of ordinary and disenfranchised persons so they can become extraordinary citizen leaders in their communities and the world.</p>
                    <p>Our department seeks to educate the whole person, and the great deal of learning takes place outside of the traditional classroom. Student life at our department is defined the mixture and balance of academic rigor, co-curricular and extracurricular pursuits, and service to others.</p>
                </div>
            </section>''',

    'ece_vision_mission.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">VISION AND MISSION</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>VISION OF THE DEPARTMENT</h3>
                <div class="glass-card" style="border-left: 4px solid #f5c518;">
                    <p>To develop the department into a full-fledged centre for learning in recent trends of Electronics and Communication Engineering and thereby enabling our graduates to excel as efficient engineer, manager or entrepreneur.</p>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up">
                <h3>MISSION OF THE DEPARTMENT</h3>
                <div class="glass-card" style="border-left: 4px solid #a31f24;">
                    <ul>
                        <li><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> Providing quality education in the areas of Electronics and communication engineering to enhance the competitiveness of our graduates in the job market and contribute to the economic, scientific and social developments.</li>
                        <li style="margin-top:10px;"><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> Endowing students with the knowledge, technical skills and values that prepare them to excel as engineers and leaders in their profession and to be committed to lifelong learning.</li>
                        <li style="margin-top:10px;"><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> Promoting active learning, critical thinking and engineering judgment coupled with business, management and entrepreneurial skills.</li>
                    </ul>
                </div>
            </section>''',

    'ece_peos.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">PEOs, POs and PSOs</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM EDUCATIONAL OBJECTIVES (PEOs)</h3>
                <div class="glass-card">
                    <ul>
                        <li style="margin-bottom:10px;"><strong>PEO 1:</strong> To provide the students with a strong foundation in the required sciences in order to pursue studies in Electronics and Communication Engineering.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 2:</strong> To gain adequate knowledge to become a good professional in electronic and communication engineering associated industries, higher education, and research.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 3:</strong> To develop an attitude in lifelong learning, applying and adapting new ideas and technologies as their field evolves.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 4:</strong> To prepare students to critically analyze existing literature in an area of specialization and ethically develop innovative and research-oriented methodologies to solve the problems identified.</li>
                        <li><strong>PEO 5:</strong> To inculcate in the students a professional and ethical attitude and an ability to visualize the engineering issues in a broader social context.</li>
                    </ul>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM OUTCOMES (POs)</h3>
                <div class="glass-card">
                    <p style="margin-bottom:15px;">Engineering Graduates will be able to:</p>
                    <div style="display:flex; flex-direction:column; gap:10px;">
                        <p><strong>PO1: Engineering knowledge:</strong> Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex engineering problems.</p>
                        <p><strong>PO2: Problem analysis:</strong> Identify, formulate, review research literature, and analyse complex engineering problems reaching substantiated conclusions.</p>
                        <p><strong>PO3: Design/development of solutions:</strong> Design solutions for complex engineering problems and design system components or processes that meet the specified needs.</p>
                        <p><strong>PO4: Conduct investigations of complex problems:</strong> Use research-based knowledge and research methods including design of experiments, analysis and interpretation of data.</p>
                        <p><strong>PO5: Modern tool usage:</strong> Create, select, and apply appropriate techniques, resources, and modern engineering and IT tools.</p>
                        <p><strong>PO6: The engineer and society:</strong> Apply reasoning informed by the contextual knowledge to assess societal, health, safety, legal and cultural issues.</p>
                        <p><strong>PO7: Environment and sustainability:</strong> Understand the impact of the professional engineering solutions in societal and environmental contexts.</p>
                        <p><strong>PO8: Ethics:</strong> Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice.</p>
                        <p><strong>PO9: Individual and team work:</strong> Function effectively as an individual, and as a member or leader in diverse teams.</p>
                        <p><strong>PO10: Communication:</strong> Communicate effectively on complex engineering activities with the engineering community and with society at large.</p>
                        <p><strong>PO11: Project management and finance:</strong> Demonstrate knowledge and understanding of the engineering and management principles.</p>
                        <p><strong>PO12: Life-long learning:</strong> Recognize the need for, and have the preparation and ability to engage in independent and life-long learning.</p>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM SPECIFIC OUTCOMES (PSOs)</h3>
                <div class="glass-card">
                    <ul>
                        <li style="margin-bottom:10px;"><strong>PSO1:</strong> Design, develop and analyze electronic systems through application of relevant electronics, mathematics and engineering principles.</li>
                        <li style="margin-bottom:10px;"><strong>PSO2:</strong> Design, develop and analyze communication systems through application of fundamentals from communication principles, signal processing, and RF System Design & Electromagnetics.</li>
                        <li><strong>PSO3:</strong> Adapt to emerging electronics and communication technologies and develop innovative solutions for existing and newer problems.</li>
                    </ul>
                </div>
            </section>''',

    'ece_faculty.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT FACULTY</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY LIST</h3>
                <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.05); margin-bottom: 30px;">
                    <table class="pub-table">
                        <thead>
                            <tr>
                                <th>S.No</th>
                                <th>Name of the Faculty</th>
                                <th>Designation</th>
                                <th>Specialization</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td><strong>Mrs. M. RATHIKA</strong></td>
                                <td>Assistant Professor & Head</td>
                                <td>RF System Design & Electromagnetics</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td><strong>Dr. S.R. SUREM SAMUEL</strong></td>
                                <td>Associate Professor</td>
                                <td>Artificial Intelligence, Signal Processing</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td><strong>Mrs. N. VANITHA</strong></td>
                                <td>Assistant Professor</td>
                                <td>VLSI Design</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td><strong>Mr. A. VENKATESAN</strong></td>
                                <td>Assistant Professor</td>
                                <td>Communication Systems</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <h3>OFFICIAL STAFF DETAILS</h3>
                <p style="margin-bottom: 20px;">Please refer to the embedded PDF document below for the complete and official detailed profile of our esteemed ECE faculty members.</p>
                <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/UGC Mandatory Disclosure/3. Academics/4. Dept Faculty Details/ECE Staff Details.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>''',

    'ece_curriculum.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">CURRICULUM & SYLLABUS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>B.E & M.E ELECTRONICS AND COMMUNICATION ENGINEERING</h3>
                <p>Access the regulations and syllabus documents across different regulation years.</p>
                <div class="grid-2" style="margin-top:20px;">
                    <div class="event-card">
                        <div class="event-title">R2021 Curriculum</div>
                        <div class="event-meta" style="margin-bottom:15px; color:#003366;">B.E - ECE</div>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/R2021-B.E-ECE.pdf" target="_blank" class="pdf-btn" style="text-align:center;"><i class="fa-solid fa-download"></i> View R2021 B.E Syllabus</a>
                    </div>
                    <div class="event-card">
                        <div class="event-title">R2017 Curriculum</div>
                        <div class="event-meta" style="margin-bottom:15px; color:#003366;">B.E - ECE</div>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/R2017-B.E-ECE.pdf" target="_blank" class="pdf-btn" style="text-align:center;"><i class="fa-solid fa-download"></i> View R2017 B.E Syllabus</a>
                    </div>
                    <div class="event-card">
                        <div class="event-title">R2017 Curriculum</div>
                        <div class="event-meta" style="margin-bottom:15px; color:#003366;">M.E - ECE</div>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/R2017-M.E-ECE.pdf" target="_blank" class="pdf-btn" style="text-align:center;"><i class="fa-solid fa-download"></i> View R2017 M.E Syllabus</a>
                    </div>
                    <div class="event-card">
                        <div class="event-title">R2013 Curriculum</div>
                        <div class="event-meta" style="margin-bottom:15px; color:#003366;">B.E - ECE</div>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/R2013-B.E-ECE.pdf" target="_blank" class="pdf-btn" style="text-align:center;"><i class="fa-solid fa-download"></i> View R2013 B.E Syllabus</a>
                    </div>
                    <div class="event-card" style="grid-column: 1 / -1;">
                        <div class="event-title">R2013 Curriculum</div>
                        <div class="event-meta" style="margin-bottom:15px; color:#003366;">M.E - ECE</div>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/R2013-M.E-ECE.pdf" target="_blank" class="pdf-btn" style="text-align:center;"><i class="fa-solid fa-download"></i> View R2013 M.E Syllabus</a>
                    </div>
                </div>
            </section>''',

    'ece_timetable.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">CLASS TIME TABLE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>Semester Schedule (2024-25 EVEN)</h3>
                <div class="grid-2" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); margin-top: 20px;">
                    <div class="event-card">
                        <div class="event-title" style="color:#a31f24; border-bottom:1px solid #eee; padding-bottom:8px;">YEAR I (SEM II)</div>
                        <p style="margin: 15px 0;">ECE - First Year Time Table</p>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/ECE-2024-25-EVEN-TT.pdf" target="_blank" class="pdf-btn" style="text-align:center;">
                            <i class="fa-solid fa-clock"></i> View Time Table
                        </a>
                    </div>
                    <div class="event-card">
                        <div class="event-title" style="color:#a31f24; border-bottom:1px solid #eee; padding-bottom:8px;">YEAR II (SEM IV)</div>
                        <p style="margin: 15px 0;">ECE - Second Year Time Table</p>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/ECE-2024-25-EVEN-TT.pdf" target="_blank" class="pdf-btn" style="text-align:center;">
                            <i class="fa-solid fa-clock"></i> View Time Table
                        </a>
                    </div>
                    <div class="event-card">
                        <div class="event-title" style="color:#a31f24; border-bottom:1px solid #eee; padding-bottom:8px;">YEAR III (SEM VI)</div>
                        <p style="margin: 15px 0;">ECE - Third Year Time Table</p>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/ECE-2024-25-EVEN-TT.pdf" target="_blank" class="pdf-btn" style="text-align:center;">
                            <i class="fa-solid fa-clock"></i> View Time Table
                        </a>
                    </div>
                    <div class="event-card">
                        <div class="event-title" style="color:#a31f24; border-bottom:1px solid #eee; padding-bottom:8px;">YEAR IV (SEM VIII)</div>
                        <p style="margin: 15px 0;">ECE - Fourth Year Time Table</p>
                        <a href="https://engineering.kingston.ac.in/assets/pdf/departments/ece/ECE-2024-25-EVEN-TT.pdf" target="_blank" class="pdf-btn" style="text-align:center;">
                            <i class="fa-solid fa-clock"></i> View Time Table
                        </a>
                    </div>
                </div>

                <h3 style="margin-top: 50px;">Previous Semester Archives</h3>
                <div class="event-card" style="max-width: 400px;">
                    <div class="event-title">TT Archives</div>
                    <p style="margin: 10px 0;">Previous semester time tables for reference.</p>
                    <a href="#" class="pdf-btn"><i class="fa-solid fa-folder-open"></i> View TT Archive</a>
                </div>
            </section>''',

    'ece_innovations.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">INNOVATIONS & HACKATHONS</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="hero-innovate">
                    <h2><i class="fa-solid fa-rocket"></i> ₹15 LAKHS FINANCIAL GRANT</h2>
                    <h3>MSME IDEA HACKATHON 3.0 (WOMEN)</h3>
                    <p style="margin-top:20px; font-weight:300;">"Smart Bike Safety Innovation"</p>
                </div>
                <div class="glass-card" style="margin-top: 30px;">
                    <p style="font-size: 1.1rem; line-height:1.8; text-align:center;">
                        Idea submitted by <strong>Ms. S. Pavithra</strong> (IV ECE), Kingston Engineering College, mentored by <strong>Mrs. M. Rathika</strong>, Head of the Department, ECE. The project was officially selected in the <em>MSME IDEA HACKATHON 3.0 (Women)</em>, receiving a massive financial assistance grant of <strong>Rs. 15 Lakhs</strong>.
                    </p>
                </div>
            </section>''',

    'ece_sports.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">SPORTS ACHIEVEMENTS</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="grid-2">
                    <div class="event-card">
                        <div class="event-title"><i class="fa-solid fa-volleyball" style="color:#a31f24;"></i> Volleyball Tournament</div>
                        <div class="event-meta">Anna University Zone 6</div>
                        <div style="margin-top:15px; font-weight:bold; color:#003366;">First Place <i class="fa-solid fa-trophy" style="color:#f5c518;"></i></div>
                        <p style="margin-top:10px;">Won by Dharshini</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title"><i class="fa-solid fa-basketball" style="color:#a31f24;"></i> Basketball Tournament</div>
                        <div class="event-meta">Anna University Zone 6</div>
                        <div style="margin-top:15px; font-weight:bold; color:#003366;">Second Place <i class="fa-solid fa-medal" style="color:silver;"></i></div>
                        <p style="margin-top:10px;">Won by C.K. Akshaya Prathiksha</p>
                    </div>
                </div>
            </section>''',

    'ece_coe.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">CENTRE OF EXCELLENCE</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>4G / 5G LABORATORY</h3>
                <div class="glass-card">
                    <p style="font-size:1.1rem;">Established <strong>4G/5G Laboratory</strong> for Academic and Research purposes on 07th March 2024.</p>
                    <p style="margin-top:15px; color:#555;">This state-of-the-art facility empowers students to gain hands-on experience in next-generation telecommunication technologies, fostering greater research and industrial readiness.</p>
                </div>
            </section>''',

    'ece_events.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">EVENTS ORGANIZED</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="event-card">
                    <div class="event-title">4G / 5G Laboratory Inauguration</div>
                    <div class="event-meta"><i class="fa-regular fa-calendar"></i> 07th March 2024</div>
                    <p style="margin-top:15px;">Official establishment and inauguration of the advanced 4G/5G testing and research laboratory catering to ECE students and faculty.</p>
                </div>
                <div class="event-card">
                    <div class="event-title">KNEC Project Expo 2024</div>
                    <div class="event-meta"><i class="fa-regular fa-calendar"></i> 25th April 2024</div>
                    <p style="margin-top:15px;">Departmental project exposition showcasing final year and pre-final year electronic innovations.</p>
                </div>
            </section>''',

    'ece_faculty_achievements.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">FACULTY ACHIEVEMENTS & UPSKILLING</h1>
            <section class="dept-section" data-aos="fade-up">
                <table class="pub-table">
                    <thead>
                        <tr>
                            <th>Faculty Name</th>
                            <th>Event Title / FDP Attended</th>
                            <th>Organizer / Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Dr. S.R. Surem Samuel</strong></td>
                            <td>Online FDP on “Artificial Intelligence Impact on Transforming Fields”</td>
                            <td>Dhaanish Ahed College of Engineering (5th-10th Aug)</td>
                        </tr>
                        <tr>
                            <td><strong>Dr. S.R. Surem Samuel</strong></td>
                            <td>National Level FDP: "Exploring Computational Intelligence"</td>
                            <td>VIT-AP University (16th-20th July 2024)</td>
                        </tr>
                        <tr>
                            <td><strong>Mrs. M. Rathika</strong></td>
                            <td>FDP: "EV: Challenges and Opportunities"</td>
                            <td>Alagappa Chettiar (TN Govt Sponsored)</td>
                        </tr>
                        <tr>
                            <td><strong>Mrs. N. Vanitha</strong></td>
                            <td>FDP: "EV: Challenges and Opportunities"</td>
                            <td>Alagappa Chettiar (TN Govt Sponsored)</td>
                        </tr>
                        <tr>
                            <td><strong>Mr. A. Venkatesan</strong></td>
                            <td>FDP: "EV: Challenges and Opportunities"</td>
                            <td>Alagappa Chettiar (TN Govt Sponsored)</td>
                        </tr>
                    </tbody>
                </table>
            </section>''',

    'ece_student_participations.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">STUDENT PARTICIPATIONS & AWARDS</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="grid-2">
                    <div class="event-card">
                        <div class="event-title">National Level Symposium: Paper Presentation</div>
                        <div class="event-meta">Thanthai Periyar Govt. Institute</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - L. Bharat Kumar (Mind Unfolded)</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">National Level Symposium: Paper Presentation</div>
                        <div class="event-meta">C. Abdul Hakeem College of Engineering</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - L. Bharat Kumar (Life Technology)</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">World Organ Donation Day Awareness</div>
                        <div class="event-meta">Sri Narayani Hospital & Research Centre</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - S. Priya</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">AMCET Symposium: Power Point Presentation</div>
                        <div class="event-meta">Annai Mira College of Engineering</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - Naveen Moses D</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">AMCET Symposium: Code Debugging</div>
                        <div class="event-meta">Annai Mira College of Engineering</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - Naveen Moses D</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">AMCET Symposium: Circuit Debugging</div>
                        <div class="event-meta">Annai Mira College of Engineering</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - Uthrakumar T N</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">AMCET Symposium: Dumb Charades</div>
                        <div class="event-meta">Annai Mira College of Engineering</div>
                        <p style="margin-top:10px;"><strong>1st Place</strong> - Karthick V, Sanjay Kumar S</p>
                    </div>
                    <div class="event-card">
                        <div class="event-title">MATLAB For Science & Tech Workshop</div>
                        <div class="event-meta">VIT, Vellore (5 days)</div>
                        <p style="margin-top:10px;">Participated: M. Jagan, K. Deepika</p>
                    </div>
                </div>
            </section>''',

    'ece_online_courses.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">ONLINE COURSES & CERTIFICATIONS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>NPTEL CERTIFICATIONS</h3>
                <table class="pub-table">
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Course Name</th>
                            <th>Award Grade</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Karthick V</strong></td>
                            <td>Introduction To Internet Of Things</td>
                            <td><span style="color:#003366; font-weight:bold;">Elite + Silver</span></td>
                        </tr>
                        <tr>
                            <td><strong>Sanjay Kumar S</strong></td>
                            <td>Introduction To Internet Of Things</td>
                            <td><span style="color:#003366; font-weight:bold;">Elite + Silver</span></td>
                        </tr>
                        <tr>
                            <td><strong>Naveen Moses D</strong></td>
                            <td>Introduction To Internet Of Things</td>
                            <td><span style="color:#003366; font-weight:bold;">Elite + Silver</span></td>
                        </tr>
                        <tr>
                            <td><strong>C.K. Akshaya Prathiksha</strong></td>
                            <td>Introduction To Internet Of Things</td>
                            <td><span style="color:#003366; font-weight:bold;">Elite + Silver</span></td>
                        </tr>
                        <tr>
                            <td><strong>Naveen Moses D</strong></td>
                            <td>Programming In Java</td>
                            <td><span style="color:#003366; font-weight:bold;">Elite</span></td>
                        </tr>
                    </tbody>
                </table>
            </section>''',

    'ece_newsletter.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">NEWSLETTER AND MAGAZINES</h1>
            <section class="dept-section" data-aos="fade-up">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                    <h3>TECH PULSE 2023-2024</h3>
                    <a href="college-detail/Autonomous/News Letter/ECE.pdf" download class="pdf-btn"><i class="fa-solid fa-download"></i> Download PDF</a>
                </div>
                <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/News Letter/ECE.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>'''
}

# Add missing blank pages
empty_pages = {
    'ece_board_of_studies.html': 'BOARD OF STUDIES',
    'ece_academic_calendar.html': 'ACADEMIC CALENDAR',
    'ece_faculty_upskilling.html': 'FACULTY UPSKILLING',
    'ece_toppers.html': 'TOPPERS LIST',
    'ece_industry_visits.html': 'INDUSTRY VISITS',
    'ece_placement.html': 'PLACEMENT',
    'ece_distinguished_alumni.html': 'DISTINGUISHED ALUMNI',
    'ece_student_publications.html': 'STUDENT PUBLICATIONS',
    'ece_contact.html': 'CONTACT US'
}

for e_p, title in empty_pages.items():
    pages[e_p] = f'''
            <h1 class="dept-title-red" data-aos="fade-up">{{title}}</h1>
            <section class="dept-section" data-aos="fade-up">
                <!-- Content to be added later -->
            </section>
'''

# We also want dept_ece.html to be identical to ece_about.html
pages['dept_ece.html'] = pages['ece_about.html']

for filename, main_content in pages.items():
    # Inject CSS
    final_main = custom_css + '\n' + f'<main class="dept-main-content">\n{main_content}\n</main>'
    
    # Process sidebar active link
    # find the li with href=filename and add class="active"
    current_sidebar = ece_sidebar.replace(f'href="{filename}"', f'href="{filename}" class="active"')
    
    # Assemble the full HTML
    full_html = start_wrap + current_sidebar + '\n' + final_main + end_wrap
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)

print(f"Generated {len(pages)} ECE pages successfully!")
