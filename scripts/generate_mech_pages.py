import os
import re

print("Starting MECH multipage generation...")

# Use dept_ece.html or dept_cse.html as the base boilerplate.
base_file = "dept_cse.html"
with open(base_file, "r", encoding="utf-8") as f:
    base_html = f.read()

# Isolate header and footer wrappers
start_wrap = base_html.split('<div class="dept-details-wrapper">')[0] + '<div class="dept-details-wrapper">\n\n'
end_wrap = '\n    </div>\n\n    <!-- Footer -->\n    <footer class="main-footer">' + base_html.split('<!-- Footer -->\n    <footer class="main-footer">')[1]

mech_sidebar = """        <aside class="dept-sidebar">
            <ul class="dept-sidebar-menu">
                <li><a href="mech_about.html"><i class="fa-solid fa-house"></i> About the Department</a></li>
                <li><a href="mech_vision_mission.html"><i class="fa-solid fa-bullseye"></i> Vision and Mission</a></li>
                <li><a href="mech_peos.html"><i class="fa-regular fa-file-lines"></i> PEOs, POs and PSOs</a></li>
                <li><a href="mech_faculty.html"><i class="fa-solid fa-user-tie"></i> Faculty</a></li>
                <li><a href="mech_board_of_studies.html"><i class="fa-solid fa-graduation-cap"></i> Board of Studies</a></li>
                <li><a href="mech_curriculum.html"><i class="fa-solid fa-book-open"></i> Curriculum</a></li>
                <li><a href="mech_academic_calendar.html"><i class="fa-regular fa-calendar-days"></i> Department Academic Calendar</a></li>
                <li><a href="mech_timetable.html"><i class="fa-solid fa-table-cells"></i> Time Table</a></li>
                <li><a href="mech_coe.html"><i class="fa-solid fa-trophy"></i> Centre of Excellence</a></li>
                <li><a href="mech_faculty_achievements.html"><i class="fa-solid fa-medal"></i> Faculty Achievements</a></li>
                <li><a href="mech_faculty_upskilling.html"><i class="fa-solid fa-arrow-trend-up"></i> Faculty Upskilling</a></li>
                <li><a href="mech_events.html"><i class="fa-regular fa-calendar-check"></i> Events Organized</a></li>
                <li><a href="mech_internships.html"><i class="fa-solid fa-clipboard-check"></i> Internships</a></li>
                <li><a href="mech_industry_visits.html"><i class="fa-solid fa-building"></i> Industry Visits</a></li>
                <li><a href="mech_toppers.html"><i class="fa-solid fa-award"></i> Toppers List</a></li>
                <li><a href="mech_student_participations.html"><i class="fa-solid fa-users-viewfinder"></i> Student Participations</a></li>
                <li><a href="mech_placement.html"><i class="fa-solid fa-briefcase"></i> Placement</a></li>
                <li><a href="mech_distinguished_alumni.html"><i class="fa-solid fa-star"></i> Distinguished Alumni</a></li>
                <li><a href="mech_student_publications.html"><i class="fa-solid fa-newspaper"></i> Student Publications</a></li>
                <li><a href="mech_online_courses.html"><i class="fa-solid fa-laptop"></i> Online Courses</a></li>
                <li><a href="mech_newsletter.html"><i class="fa-regular fa-newspaper"></i> Newsletter and Magazines</a></li>
                <li><a href="mech_contact.html"><i class="fa-solid fa-envelope"></i> Contact Us</a></li>
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
    font-size: 0.9rem;
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
    'mech_about.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT OF<br>MECHANICAL ENGINEERING</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>DEPARTMENT INTRODUCTION</h3>
                <div class="glass-card">
                    <p>The department of Mechanical Engineering was established in the year 2009. The department offers B.E (Mechanical Engineering) from the academic year 2009 – 2010, M.E (Engineering Design) from the academic year 2013 – 2014 and M.E (Energy Engineering) from the academic year 2013– 2014.</p>
                    <p>The department became an approved research center of Anna University in the year 2017. The department has highly qualified and experienced faculty members with Ph.D. degree. The faculty members actively engage in research and constantly publish papers in International and National Journals. The department organizes technical workshops, Seminar/Conference for the faculty members to meet the recent emerging trends. The department has the state-of-the-art facilities for various laboratories, classrooms to support e-learning and department library.</p>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up">
                <h3>HIGHLIGHTS OF THE DEPARTMENT</h3>
                <div class="glass-card">
                    <ul style="line-height:1.7;">
                        <li><i class="fa-solid fa-angles-right" style="color:#a31f24;"></i> Highly qualified and experienced faculty members with Ph.D. degrees.</li>
                        <li><i class="fa-solid fa-angles-right" style="color:#a31f24;"></i> Approved research center of Anna University since 2017.</li>
                        <li><i class="fa-solid fa-angles-right" style="color:#a31f24;"></i> Faculty members actively engage in research and constantly publish papers in International and National Journals.</li>
                        <li><i class="fa-solid fa-angles-right" style="color:#a31f24;"></i> Well-equipped centralized workshop facility which caters to the needs of various departments.</li>
                        <li><i class="fa-solid fa-angles-right" style="color:#a31f24;"></i> Regular guest lectures and workshops conducted by Industry Experts and Eminent Professors.</li>
                    </ul>
                </div>
            </section>''',

    'mech_vision_mission.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">VISION AND MISSION</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>VISION OF THE DEPARTMENT</h3>
                <div class="glass-card" style="border-left: 4px solid #f5c518;">
                    <p>The department of Mechanical Engineering strives to develop skilled, competent, ethical and versatile mechanical engineers capable of designing, developing and analyzing the complex problems and implementation of emerging engineering technologies, to solve the real time problems.</p>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up">
                <h3>MISSION OF THE DEPARTMENT</h3>
                <div class="glass-card" style="border-left: 4px solid #a31f24;">
                    <ul>
                        <li><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> To impart quality education to the students to build their capacity and enhance their skills to make them globally competitive mechanical engineers.</li>
                        <li style="margin-top:10px;"><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> To maintain a vital, state-of-the-art research enterprise to provide our students and faculty with opportunities to create, interpret, apply and disseminate knowledge.</li>
                        <li style="margin-top:10px;"><i class="fa-solid fa-check" style="color:#a31f24; margin-right:8px;"></i> To prepare our graduates to pursue life-long learning, serve the profession and society and develop intellectual, ethical and career challenges.</li>
                    </ul>
                </div>
            </section>''',

    'mech_peos.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">PEOs, POs and PSOs</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM EDUCATIONAL OBJECTIVES (PEOs)</h3>
                <div class="glass-card">
                    <p style="margin-bottom:10px; font-weight:bold; color:#003366;">B.E. Mechanical Engineering</p>
                    <ul>
                        <li style="margin-bottom:10px;"><strong>PEO 1:</strong> Effectuating success in careers by exploring with the design, digital and computational analysis of engineering systems, experimentation and testing, smart manufacturing, technical services, and research.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 2:</strong> Amalgamating effectively with stakeholders to update and improve their core competencies and abilities to ethically compete in the ever-changing multicultural global enterprise.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 3:</strong> To encourage multi-disciplinary research and development to foster advanced technology, and to nurture innovation and entrepreneurship in order to compete successfully in the global economy.</li>
                        <li style="margin-bottom:10px;"><strong>PEO 4:</strong> To globally share and apply technical knowledge to create new opportunities that proactively advance our society through team efforts and to solve various challenging technical, environmental, and societal problems.</li>
                        <li><strong>PEO 5:</strong> To create world-class mechanical engineers capable of practicing engineering ethically with a solid vision to become great leaders in academia, industries, and society.</li>
                    </ul>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM OUTCOMES (POs)</h3>
                <div class="glass-card">
                    <p style="margin-bottom:15px;">Engineering Graduates will be able to:</p>
                    <div style="display:flex; flex-direction:column; gap:10px;">
                        <p><strong>PO1: Engineering knowledge:</strong> Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex engineering problems.</p>
                        <p><strong>PO2: Problem analysis:</strong> Identify, formulate, review research literature, and analyse complex engineering problems reaching substantiated conclusions using first principles of mathematics, natural sciences, and engineering sciences.</p>
                        <p><strong>PO3: Design/development of solutions:</strong> Design solutions for complex engineering problems and design system components or processes that meet the specified needs with appropriate consideration for the public health and safety, and the cultural, societal, and environmental considerations.</p>
                        <p><strong>PO4: Conduct investigations of complex problems:</strong> Use research-based knowledge and research methods including design of experiments, analysis and interpretation of data, and synthesis of the information to provide valid conclusions.</p>
                        <p><strong>PO5: Modern tool usage:</strong> Create, select, and apply appropriate techniques, resources, and modern engineering and IT tools including prediction and modeling to complex engineering activities with an understanding of the limitations.</p>
                        <p><strong>PO6: The engineer and society:</strong> Apply reasoning informed by the contextual knowledge to assess societal, health, safety, legal and cultural issues and the consequent responsibilities relevant to the professional engineering practice.</p>
                        <p><strong>PO7: Environment and sustainability:</strong> Understand the impact of the professional engineering solutions in societal and environmental contexts, and demonstrate the knowledge of, and need for sustainable development.</p>
                        <p><strong>PO8: Ethics:</strong> Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice.</p>
                        <p><strong>PO9: Individual and team work:</strong> Function effectively as an individual, and as a member or leader in diverse teams, and in multidisciplinary settings.</p>
                        <p><strong>PO10: Communication:</strong> Communicate effectively on complex engineering activities with the engineering community and with society at large.</p>
                    </div>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PROGRAM SPECIFIC OUTCOMES (PSOs)</h3>
                <div class="glass-card">
                    <ul>
                        <li style="margin-bottom:10px;"><strong>PSO 1:</strong> Apply the knowledge gained in Mechanical Engineering for design and development and manufacture of engineering systems.</li>
                        <li style="margin-bottom:10px;"><strong>PSO 2:</strong> Apply the knowledge acquired to investigate research-oriented problems in mechanical engineering with due consideration for environmental and social impacts.</li>
                        <li><strong>PSO 3:</strong> Use engineering analysis and data management tools for effective management of multidisciplinary projects.</li>
                    </ul>
                </div>
            </section>''',

    'mech_faculty.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT FACULTY</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY LIST</h3>
                <div class="table-responsive glass-card" style="padding: 0; overflow: hidden; margin-top:20px;">
                    <table class="pub-table" style="margin-top:0;">
                        <thead>
                            <tr>
                                <th>S.No</th>
                                <th>Name of the Staff</th>
                                <th>Designation</th>
                                <th>Qualification</th>
                                <th>Specialization</th>
                                <th>E-Mail ID</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td>1</td><td><strong>Dr. N. Shankar Ganesh</strong></td><td>Professor</td><td>M.E, Ph.D</td><td>Thermal</td><td>hodmech@kingston.ac.in</td></tr>
                            <tr><td>2</td><td><strong>Mr. S. Mahendiran</strong></td><td>Asso. Prof</td><td>M.E., (Ph.D)</td><td>CAD/CAM</td><td>mahendirans@kingston.ac.in</td></tr>
                            <tr><td>3</td><td><strong>Dr. C. G. Mohan</strong></td><td>Director (Placement)</td><td>M.E., Ph.D</td><td>Thermal</td><td>dharmagurusamycg@kingston.ac.in</td></tr>
                            <tr><td>4</td><td><strong>Dr. S. Sathiesh Kumar</strong></td><td>Asst. Prof</td><td>M.E, Ph.D</td><td>Design</td><td>sathieshkumarsm@kingston.ac.in</td></tr>
                            <tr><td>5</td><td><strong>Dr. L. S. Kishore</strong></td><td>Asst. Prof</td><td>M.E, Ph.D</td><td>Design</td><td>ls.kishore@kingston.ac.in</td></tr>
                            <tr><td>6</td><td><strong>Dr. A. Vinod Kumar</strong></td><td>Asst. Prof</td><td>M.E, Ph.D</td><td>Engineering Design</td><td>kumarv2732@kingston.ac.in</td></tr>
                            <tr><td>7</td><td><strong>Mr. S. T. Ezhilram</strong></td><td>Asst. Prof</td><td>M.E.</td><td>Thermal</td><td>ezhilram@kingston.ac.in</td></tr>
                            <tr><td>8</td><td><strong>Mr. Thillaidasan D</strong></td><td>Asst. Prof</td><td>M.E.</td><td>Applied Mechanics</td><td>thillaidasand@kingston.ac.in</td></tr>
                            <tr><td>9</td><td><strong>Mr. Manivannan D</strong></td><td>Asst. Prof</td><td>M.E.</td><td>Thermal</td><td>manivannand@kingston.ac.in</td></tr>
                            <tr><td>10</td><td><strong>Mr. G. Venkataramanan</strong></td><td>Asst. Prof</td><td>M.Tech</td><td>Production</td><td>venky@kingston.ac.in</td></tr>
                            <tr><td>11</td><td><strong>Mr. M. M. Ravikumar</strong></td><td>Asst. Prof</td><td>M.E., (Ph.D)</td><td>CAD</td><td>ravikumar.mechanical@kingston.ac.in</td></tr>
                            <tr><td>12</td><td><strong>Mr. Dineshkumar H</strong></td><td>Asst. Prof</td><td>M.E.</td><td>Manufacture</td><td>dineshkumarh.mech@kingston.ac.in</td></tr>
                            <tr><td>13</td><td><strong>Mr. Aswathy C Nair</strong></td><td>Asst. Prof</td><td>M.Tech</td><td>Production</td><td>Aswathynair.mech@kingston.ac.in</td></tr>
                            <tr><td>14</td><td><strong>Mr. V. Charunnath S</strong></td><td>Asst. Prof</td><td>M.Tech</td><td>Design</td><td>Charunnathsveve.mech@kingston.ac.in</td></tr>
                        </tbody>
                    </table>
                </div>
            </section>
            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY REFERENCE</h3>
                <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/UGC Mandatory Disclosure/3. Academics/4. Dept Faculty Details/Mech Staff Details.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>
''',

    'mech_faculty_achievements.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">FACULTY ACHIEVEMENTS & PUBLICATIONS</h1>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PUBLISHED PATENTS</h3>
                <div class="table-responsive glass-card" style="padding: 0; overflow: hidden; margin-top:20px;">
                    <table class="pub-table" style="margin-top:0;">
                        <thead>
                            <tr>
                                <th>Faculty Name</th>
                                <th>Title of the Patent</th>
                                <th>Application Number</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>N. Shankar Ganesh</strong>, D. Manivannan, Pradeep Kumar A R</td>
                                <td>Integrated Organic Rankine Cycle Power Generation and Ejector Refrigeration Systems using Waste Heat Recovery</td>
                                <td>202241004714 A</td>
                                <td><span style="color:green;">Published</span></td>
                            </tr>
                            <tr>
                                <td>Sivakandhan C, Pradeep Kumar A R, Senthur, N S, <strong>N. Shankar Ganesh</strong></td>
                                <td>Intelligent-balancing advanced vehicle structure</td>
                                <td>202041006033A</td>
                                <td><span style="color:green;">Published</span></td>
                            </tr>
                            <tr>
                                <td><strong>N. Shankar Ganesh</strong>, S. Mahendiran, D. Manivannan</td>
                                <td>Combined Thermodynamic Cycle Based Power Generation System and A Method Thereof</td>
                                <td>201941009276</td>
                                <td><span style="color:green;">Published</span></td>
                            </tr>
                            <tr>
                                <td><strong>N. Shankar Ganesh</strong>, T. Srinivas, M. M. Ravikumar</td>
                                <td>Thermodynamic Cycle Based Power Generation System</td>
                                <td>201741046830A</td>
                                <td><span style="color:#003366; font-weight:bold;">Granted</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>JOURNAL PUBLICATIONS & BOOK CHAPTERS (2023-2024)</h3>
                <div class="grid-2">
                    <div class="event-card">
                        <div class="event-title">Evaluation on novel Kalina power generation system</div>
                        <div class="event-meta">N. Shankar Ganesh</div>
                        <div style="margin-top:10px; font-weight:bold; color:#003366;">Case Studies in Thermal Engineering (Scopus)</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Exergy analysis of an innovative power generation</div>
                        <div class="event-meta">N. Shankar Ganesh</div>
                        <div style="margin-top:10px; font-weight:bold; color:#003366;">Int. Journal of Exergy (Scopus)</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Mechanical characterisation of AA6082 Aluminium metal matrix</div>
                        <div class="event-meta">S. Rudramoorthy and N. Shankar Ganesh</div>
                        <div style="margin-top:10px; font-weight:bold; color:#003366;">Int. Journal of Cast Metals Research (Scopus)</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Impact of Emulsified Bio-Fuel on the Environment (Book Chapter)</div>
                        <div class="event-meta">Dr. N. Shankar Ganesh - Springer</div>
                        <div style="margin-top:10px; font-weight:bold; color:#003366;">Bioenergy, pp 99-113</div>
                    </div>
                </div>
            </section>''',

    'mech_events.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">GUEST LECTURES & EVENTS ORGANIZED</h1>
            <section class="dept-section" data-aos="fade-up">
                <div class="grid-2">
                    <div class="event-card">
                        <div class="event-title">Python with Machine Learning for Mechanical Engineers</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Mr Manibharthi Karunakaran (Founder, Csuite Tech Labs)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 09.03.2023</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Industry 4.0 (Additive Manufacturing)</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Mr G Agiesh Ashok (MD, Inzaneone Technology)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 28.09.2022</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Exergy and Thermo Economic Investigation</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Dr. Sudipta De (Professor, Jadavpur University)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 09.08.2021 To 13.08.2021</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">BSVI engine technologies, emission control & testing</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Mr. Pritesh Suple (Sr. Manager, Tata Motors)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 17.04.2021</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Digital Transformation and Industrial Revolution</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Dr. G K Ananthasuresh (Professor, IISC)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 10.03.2020</div>
                    </div>
                    <div class="event-card">
                        <div class="event-title">Green Energy Technologies: Need of future</div>
                        <div class="event-meta"><i class="fa-regular fa-user"></i> Dr. M Udhaykumar (Professor, NIT)</div>
                        <div class="event-meta" style="margin-top:5px;"><i class="fa-regular fa-calendar"></i> 19.11.2019</div>
                    </div>
                </div>
            </section>''',

    'mech_industry_visits.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">INDUSTRIAL VISITS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>INDUSTRIAL TOURS ORGANIZED (2023-2024)</h3>
                <div class="table-responsive glass-card" style="padding: 0; overflow: hidden; margin-top:20px;">
                    <table class="pub-table" style="margin-top:0;">
                        <thead>
                            <tr>
                                <th>Date of Visit</th>
                                <th>Name of the Company / Location</th>
                                <th>Year Participated</th>
                                <th>No. of Students</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>06.10.23 & 07.10.23</td>
                                <td><strong>Kundah Power House, Ooty</strong></td>
                                <td>IV Year</td>
                                <td>17</td>
                            </tr>
                            <tr>
                                <td>24.11.2023</td>
                                <td><strong>Ashok Leyland Unit-1, Hosur</strong></td>
                                <td>II, III & IV Year</td>
                                <td>41</td>
                            </tr>
                            <tr>
                                <td>28.02.2024</td>
                                <td><strong>Neyveli Lignite Corporation (NLC), Neyveli</strong></td>
                                <td>II & III Year</td>
                                <td>30</td>
                            </tr>
                            <tr>
                                <td>18.03.2024</td>
                                <td><strong>FESTO CORPORATION, Bangalore</strong></td>
                                <td>II & III Year</td>
                                <td>30</td>
                            </tr>
                            <tr>
                                <td>12.04.2024</td>
                                <td><strong>Madras Atomic Power Station, Kalpakkam</strong></td>
                                <td>II & III Year</td>
                                <td>30</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>''',

    'mech_internships.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">STUDENT INTERNSHIPS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>INTERNSHIPS UNDERGONE BY STUDENTS</h3>
                <div class="table-responsive glass-card" style="padding: 0; overflow: hidden; margin-top:20px;">
                    <table class="pub-table" style="margin-top:0;">
                        <thead>
                            <tr>
                                <th>Name of the Student</th>
                                <th>Class / Section</th>
                                <th>Name & Address of the Company</th>
                                <th>Duration</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Neha Mahesh</strong></td>
                                <td>IV Year</td>
                                <td>Renault Nissan Business centre</td>
                                <td>10 Months (From 01.11.23)</td>
                            </tr>
                            <tr>
                                <td><strong>Nadheesan S</strong></td>
                                <td>III Year</td>
                                <td>Eesa Fabricator Pvt Ltd</td>
                                <td>15 Days (Jan 2024)</td>
                            </tr>
                            <tr>
                                <td><strong>Sanjay S</strong></td>
                                <td>III Year</td>
                                <td>Eesa Fabricator Pvt Ltd</td>
                                <td>15 Days (Jan 2024)</td>
                            </tr>
                            <tr>
                                <td><strong>Ragul Gandhi R</strong></td>
                                <td>III Year</td>
                                <td>Eesa Fabricator Pvt Ltd</td>
                                <td>15 Days (Jan 2024)</td>
                            </tr>
                            <tr>
                                <td><strong>Naveen T</strong></td>
                                <td>IV Year</td>
                                <td>India Japan Lighting company</td>
                                <td>56 Days (Jan-Feb 2024)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>''',

    'mech_online_courses.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">ONLINE COURSES & CERTIFICATIONS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>NPTEL CERTIFICATIONS (STUDENT ACHIEVEMENTS)</h3>
                <div class="table-responsive glass-card" style="padding: 0; overflow: hidden; margin-top:20px;">
                    <table class="pub-table" style="margin-top:0;">
                        <thead>
                            <tr>
                                <th>Student Name</th>
                                <th>Course Title</th>
                                <th>Score / Grade</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Akash A</strong></td><td>Fundamentals of Artificial Intelligence</td><td><span style="color:#a31f24; font-weight:bold;">54</span></td></tr>
                            <tr><td><strong>Bhuvaneshwar U</strong></td><td>Fundamentals of Artificial Intelligence</td><td><span style="color:#a31f24; font-weight:bold;">62</span></td></tr>
                            <tr><td><strong>Revanth G J</strong></td><td>Fundamentals of Artificial Intelligence</td><td><span style="color:#a31f24; font-weight:bold;">54</span></td></tr>
                            <tr><td><strong>Madhan Kumaran G</strong></td><td>Automation in Manufacturing</td><td><span style="color:#a31f24; font-weight:bold;">56</span></td></tr>
                            <tr><td><strong>Santhosh M</strong></td><td>Advanced Machining Processes</td><td><span style="color:#a31f24; font-weight:bold;">60</span></td></tr>
                            <tr><td><strong>Sudhakar A</strong></td><td>Inspection and Quality Control in Manufacturing</td><td><span style="color:#a31f24; font-weight:bold;">65</span></td></tr>
                            <tr><td><strong>Naveen Kumar P</strong></td><td>Product Design Using Value Engineering</td><td><span style="color:#a31f24; font-weight:bold;">71</span></td></tr>
                            <tr><td><strong>Parthiban R</strong></td><td>The Ethical Corporation</td><td><span style="color:#a31f24; font-weight:bold;">72</span></td></tr>
                        </tbody>
                    </table>
                </div>
            </section>''',

    'mech_toppers.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">TOPPERS & RANK HOLDERS</h1>
            <section class="dept-section" data-aos="fade-up">
                <h3>ANNA UNIVERSITY RANK HOLDERS</h3>
                <div class="grid-2" style="margin-top:20px;">
                    <div class="event-card" style="border-left: 4px solid #f5c518; text-align:center;">
                        <i class="fa-solid fa-crown" style="font-size:3rem; color:#f5c518; margin-bottom:15px;"></i>
                        <h2 style="color:#003366;">MADHANKUMARAN G</h2>
                        <h3 style="color:#a31f24;">9.14 CGPA</h3>
                        <p style="margin-top:10px;"><strong>Rank: 9</strong> (2022-2023)</p>
                    </div>
                    <div class="event-card" style="border-left: 4px solid silver; text-align:center;">
                        <i class="fa-solid fa-crown" style="font-size:3rem; color:silver; margin-bottom:15px;"></i>
                        <h2 style="color:#003366;">ARUN G</h2>
                        <h3 style="color:#a31f24;">9.03 CGPA</h3>
                        <p style="margin-top:10px;"><strong>Rank: 9</strong> (2019-2020)</p>
                    </div>
                </div>
            </section>''',

    'mech_newsletter.html': f'''
            <h1 class="dept-title-red" data-aos="fade-up">NEWSLETTER AND MAGAZINES</h1>
            <section class="dept-section" data-aos="fade-up">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                    <h3>MECH NEWSLETTER 2023-2024</h3>
                    <a href="college-detail/Autonomous/News Letter/MECH.pdf" download class="pdf-btn"><i class="fa-solid fa-download"></i> Download PDF</a>
                </div>
                <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/News Letter/MECH.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>'''
}

# The remaining placeholder blank pages
empty_pages = {
    'mech_board_of_studies.html': 'BOARD OF STUDIES',
    'mech_academic_calendar.html': 'ACADEMIC CALENDAR',
    'mech_curriculum.html': 'CURRICULUM & SYLLABUS',
    'mech_timetable.html': 'TIME TABLE',
    'mech_coe.html': 'CENTRE OF EXCELLENCE',
    'mech_faculty_upskilling.html': 'FACULTY UPSKILLING',
    'mech_student_participations.html': 'STUDENT PARTICIPATIONS',
    'mech_placement.html': 'PLACEMENT',
    'mech_distinguished_alumni.html': 'DISTINGUISHED ALUMNI',
    'mech_student_publications.html': 'STUDENT PUBLICATIONS',
    'mech_contact.html': 'CONTACT US'
}

for e_p, title in empty_pages.items():
    pages[e_p] = f'''
            <h1 class="dept-title-red" data-aos="fade-up">{title}</h1>
            <section class="dept-section" data-aos="fade-up">
                <!-- Content to be added later -->
            </section>
'''

# We also want dept_mech.html to be identical to mech_about.html
pages['dept_mech.html'] = pages['mech_about.html']

for filename, main_content in pages.items():
    # Inject CSS
    final_main = custom_css + '\n' + f'<main class="dept-main-content">\n{main_content}\n</main>'
    
    # Process sidebar active link
    current_sidebar = mech_sidebar.replace(f'href="{filename}"', f'href="{filename}" class="active"')
    
    # Assemble the full HTML
    full_html = start_wrap + current_sidebar + '\n' + final_main + end_wrap
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)

print(f"Generated {len(pages)} MECH pages successfully!")
