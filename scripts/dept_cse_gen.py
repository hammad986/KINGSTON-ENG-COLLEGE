import os

# Read departments.html base structure to extract the exact header and footer
with open('d:/clg website new/departments.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract before header ends
header_end_idx = html.find('</header>') + len('</header>')
footer_start_idx = html.find('<!-- Footer -->')

before_header = html[:header_end_idx]
after_footer = html[footer_start_idx:]

cse_content = """

    <!-- Department Content Wrapper -->
    <div class="dept-details-wrapper">
        
        <!-- Sidebar Navigation -->
        <aside class="dept-sidebar">
            <ul class="dept-sidebar-menu">
                <li><a href="#" class="active"><i class="fa-solid fa-house"></i> About the Department</a></li>
                <li><a href="#"><i class="fa-solid fa-bullseye"></i> Vision and Mission</a></li>
                <li><a href="#"><i class="fa-regular fa-file-lines"></i> PEOs, POs and PSOs</a></li>
                <li><a href="#"><i class="fa-solid fa-user-tie"></i> Faculty</a></li>
                <li><a href="#"><i class="fa-solid fa-users"></i> Non Teaching Faculty</a></li>
                <li><a href="#"><i class="fa-solid fa-graduation-cap"></i> Board of Studies</a></li>
                <li><a href="#"><i class="fa-solid fa-book-open"></i> Curriculum</a></li>
                <li><a href="#"><i class="fa-regular fa-calendar-days"></i> Department Academic Calendar</a></li>
                <li><a href="#"><i class="fa-solid fa-table-cells"></i> Time Table</a></li>
                <li><a href="#"><i class="fa-solid fa-trophy"></i> Centre of Excellence</a></li>
                <li><a href="#"><i class="fa-solid fa-microscope"></i> Ph.D./M.S. (Research)</a></li>
                <li><a href="#"><i class="fa-regular fa-bookmark"></i> Research Publications</a></li>
                <li><a href="#"><i class="fa-regular fa-thumbs-up"></i> Best Practices</a></li>
                <li><a href="#"><i class="fa-solid fa-file-contract"></i> IPR</a></li>
                <li><a href="#"><i class="fa-solid fa-flask"></i> Research Projects</a></li>
                <li><a href="#"><i class="fa-solid fa-briefcase"></i> Consultancy</a></li>
                <li><a href="#"><i class="fa-solid fa-medal"></i> Faculty Achievements</a></li>
                <li><a href="#"><i class="fa-solid fa-arrow-trend-up"></i> Faculty Upskilling</a></li>
                <li><a href="#"><i class="fa-regular fa-calendar-check"></i> Events Organized</a></li>
                <li><a href="#"><i class="fa-solid fa-briefcase"></i> Placement</a></li>
            </ul>
        </aside>

        <!-- Main Content Area -->
        <main class="dept-main-content">
            
            <!-- Hero Slider Placeholder -->
            <div class="dept-main-slider data-aos="fade-up"">
                <img src="https://images.unsplash.com/photo-1577896851231-70ef18881754?w=1000&q=80" alt="Students in classroom">
                <div class="dept-slider-caption">Voice of Alumni How to get a Job in Product Based Companies - Mr.Ragav PS (Amazon Play)</div>
            </div>

            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT OF<br>COMPUTER SCIENCE AND ENGINEERING</h1>

            <section class="dept-section" data-aos="fade-up">
                <h3>ABOUT THE DEPARTMENT</h3>
                <p>The Department of Computer Science and Engineering was started with the sanctioned intake of 60 in the year 2008 and at present the annual intake is 240. The U.G. Program of the Department is accredited by National Board of Accreditation (NBA) in the years 2018, 2022. The Department aims at providing domain specific training and skills to the students for pursuing a career in the field of Computer Science. The Department has state-of-the art laboratory facilities to fulfil the curriculum, Industry collaborated Centres of Excellence (COEs) and also to carry out various projects, research and consultancy activities.Additionally, we aim to equip our learners with the necessary skills to tackle global challenges, nurture an entrepreneurial and innovative mindset.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY</h3>
                <p>The Department is enriched with a dedicated, well qualified and experienced faculty team of 5 Professors, 12 Associate Professors and 20 Assistant Professors specialized in various domains including Image Processing, Cloud Computing, Agent Computing, Computer Vision, Machine Learning, Deep Learning, Network Security, and Cyber Security. The faculty members are active members of professional bodies such as ISTE, CSI, IEEE, IAENG. Faculty Members were trained and certified in the Futuristic Technologies by Industries like Virtusa, Oracle, TCS, Cognizant, Infosys, Wipro, BNY Mellon, in the niche areas such as Artificial Intelligence, Data Science, Full Stack Engineering, Cloud Computing and Cyber Security, Machine Learning.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>RESEARCH</h3>
                <p>The Department promotes research among the faculty and 17 of them are doctorates and 17 are pursuing Ph.D. The Department has received Recognized Research Centre status by Anna University for Ph.D. programme. 5 research scholars completed their Ph.D. from this research centre and currently, 12 part-time and 5 full-time research scholars are associated with this research centre. Our department faculty members are active researchers publishing their research papers in Web of Science, SCI and Scopus Indexed Journals and various International and National Conferences. International and National Conferences were conducted by the department. The H-index of the departments is 19. All our faculty members are actively participating in various FDPs conducted by premier institutions and online courses offered by NPTEL, NITTTR, etc. and thereby enhance their teaching and research skills.Proposals for research grants are submitted regularly to AICTE, DST, SERB, MEITY and TNSCST.The Department has organized STTPs, FDPs, National Seminars and International Conferences funded by various organizations.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>CURRICULUM ENRICHMENT</h3>
                <p>In order make the students to excel in the emerging areas of computer science, the department is associated with three knowledge partners who contribute to the Centre of Excellence, enabling it to remain aligned with evolving technology trends.</p>
                <ul>
                    <li>Cloud Computing – AtoS</li>
                    <li>Full Stack Computing – NTT Data</li>
                    <li>Cyber Security - LTIMindtree</li>
                </ul>
                <p>Our esteemed Knowledge Partner, contributes to the design of 40% of the B.E. Computer Science and Engineering syllabus to meet the requirements of rapidly changing industry landscape.</p>
                <p><strong>Cloud Computing:</strong> In order to develop, manage and protect the cloud-based systems, a technology to which, nowadays, companies are moving, there exists a vast opportunity for the role of Cloud Engineers, Cloud Architects, Cloud Security Specialists, etc.</p>
                <p><strong>Cyber Security:</strong> Cyber threats are one of the major issues needs to be addressed in the Cyber World. IT world is in need of Security Architect, Cybersecurity Engineer, Information Security Analyst, Penetration Tester, and Cybersecurity Consultant.</p>
                <p><strong>Full Stack Computing:</strong> Computer Science and Information Technology field always looking for a professional who possesses a wide range of skills and expertise in both front-end and back-end web development. Their role is to handle all aspects of building and deploying web applications, from the user interface to the server-side logic and database interactions.</p>
                <p>These Centres of Excellence (CoEs) offer specialized training and industry-mentored, real-time projects in emerging technologies, equipping students with the skills and experience needed to become industry-ready professionals.</p>
                <p>Curriculum delivery is implemented using project-based learning, Self-Learning is inculcated among students by using RMK Nextgen, an AI powered Learning platform to impart Personalized Learning Experience. Digital Course Materials was designed and developed by our team of Faculty for the effective utilization of students in the Teaching Learning process</p>
            </section>
            
            <section class="dept-section" data-aos="fade-up">
                <h3>PLACEMENT</h3>
                <p>The Training and Placement Cell organizes various training programs with renowned expert trainers from industries and multinational companies to improve the oral, written and aptitude skills of the students which pave way to get hired by leading core and IT industries.<br>By imparting 360° placement training, students received offers from top MNCs such as Amazon, Zoho, TCS, Cognizant, Wipro, Infosys, L&T InfoTech, Virtusa, Hitachi, Accenture, etc. with consistent 85% of placement and highest salary package of 25 lakhs per annum.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>PROFESSIONAL SOCIETIES AND STUDENTS CLUB ACTIVITIES</h3>
                <p>The faculty members and the students are associated with 3 professional bodies, CSI, ISTE, IEI, with around 1230 membership. In order to expose the students’ various technical and non-technical talents, the department has established 12 students’ clubs. Students organize and participate in various intra-department and inter-department competitions conducted by these clubs. The national level technical symposium, “<strong>XENIOZ</strong>” is organized every year as a part of the CSE students Association to provide a platform for other college students to display their talents. As a part of student’s association activities, Guest Lectures, Workshops, and Seminars are arranged with experts from the industry as resource persons.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>SIGNIFICANT ACHIEVEMENTS</h3>
                <ul>
                    <li>31 Anna University rank holders from inception.</li>
                    <li>CTS Best Project Award in the year 2017</li>
                    <li>CSI Best Chapter Award in the year 2018</li>
                    <li>First prize in Virtusa Neural Hack, Hyderabad in the year 2022.</li>
                    <li>ISTE best student award in the year 2023</li>
                    <li>First Prize with a cash award of ₹1,00,000 in the Ministry of HRD (MHRD), Government of India sponsored Smart India Hackathon (SIH) 2024</li>
                    <li>A grant of ₹15 lakhs from the Ministry of MSME, Government of India, towards student project in the year 2025</li>
                    <li>Highest salary package offered Rs. 25 Lakhs by Amazon</li>
                </ul>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>SALIENT FEATURES</h3>
                <ul>
                    <li>Industry Designed Autonomous Curriculum</li>
                    <li>Research Oriented Curriculum in Futuristic Technologie</li>
                    <li>Product Development Lab from Semester I to VI through AICTE Idea Lab</li>
                    <li>Curriculum delivery through Innovative Pedagogical Techniques with Smart Classrooms, Viewsonic boards and LCD Projectors</li>
                    <li>Math Club, Coding Club, Language Club, Science and Innovation Club, Tech Club, Photography Club, Humor Club, Eco Club, Yoga Club, TEDx Club, Cultural Club, Astronomy Club, Sports Club</li>
                    <li>Live Interactive Assessment through RMKNextGen</li>
                    <li>Activity-Based Learning, Blended Learning, Project-Based Learning</li>
                    <li>Designing and Development of Digital Course Materials by our team of faculty</li>
                    <li>Counselling and Performance monitoring through Pragati Online Counselling App</li>
                    <li>Recognizing High Performers (RHP) and SkillRack Elite forum for Top coders</li>
                    <li>Industry Internship in Curriculum - 1 week in winter and 3 weeks in summer</li>
                    <li>Industrial visits</li>
                </ul>
            </section>

        </main>
    </div>

"""

# Also change the page title and active navigation class
new_html = before_header.replace('<title>Departments - Kingston Engineering College</title>', '<title>CSE Department - Kingston Engineering College</title>') + cse_content + after_footer

with open('d:/clg website new/dept_AI&DS.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Update the CSE department links in departments.html grid and the header dropdown
with open('d:/clg website new/departments.html', 'r', encoding='utf-8') as f:
    dept_html = f.read()

# Update Grid link
dept_html = dept_html.replace(
    '<a href="#" class="dept-card" data-aos="fade-up" data-aos-delay="100">\\n                    <i class="fa-solid fa-desktop"></i>\\n                    <span>Computer Science and Engineering</span>\\n                </a>',
    '<a href="dept_AI&DS.html" class="dept-card" data-aos="fade-up" data-aos-delay="100">\\n                    <i class="fa-solid fa-desktop"></i>\\n                    <span>Computer Science and Engineering</span>\\n                </a>'
)

# Replace the dropdown item links across ALL FILES so that CSE redirects exactly to the new page.
target_li = '<li><a href="departments.html">Computer Science and Engineering</a></li>'
replace_li = '<li><a href="dept_AI&DS.html">Computer Science and Engineering</a></li>'

dept_html = dept_html.replace(target_li, replace_li)

with open('d:/clg website new/departments.html', 'w', encoding='utf-8') as f:
    f.write(dept_html)

for file in ['index.html', 'about.html', 'dept_AI&DS.html']:
    with open(f'd:/clg website new/{file}', 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(target_li, replace_li)
    with open(f'd:/clg website new/{file}', 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated dept_AI&DS.html and updated dynamic links to it.")
