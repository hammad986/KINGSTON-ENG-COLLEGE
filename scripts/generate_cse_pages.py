import os
import re

base_file = 'dept_cse.html'

with open(base_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Separate prefix, main, suffix
parts = html.split('<main class="dept-main-content">')
pre_main = parts[0]
post_main_raw = parts[1]

post_parts = post_main_raw.split('</main>')
old_main = post_parts[0]
suffix = '</main>' + post_parts[1]

# Clean sidebar in pre_main (Remove active class and remove deleted items)
pre_main = pre_main.replace('class="active"', '')
pre_main = re.sub(r'<li[^>]*><a href="cse_ipr.html"[^>]*>.*?</a></li>', '', pre_main, flags=re.IGNORECASE)
pre_main = re.sub(r'<li[^>]*><a href="cse_consultancy.html"[^>]*>.*?</a></li>', '', pre_main, flags=re.IGNORECASE)

# Common custom styles for new elements
custom_css = """
<style>
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
        margin: 40px auto;
        max-width: 600px;
        transition: transform 0.3s ease;
    }
    .glass-card:hover { transform: translateY(-5px); box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.2); }
    .glass-card i { font-size: 3rem; color: #a31f24; margin-bottom: 20px; }
    .glass-card h2 { color: #2c3e50; font-weight: 700; margin-bottom: 15px; }
    .glass-card p { color: #555; line-height: 1.6; }
    .animated-pulse { animation: pulseGlow 2s infinite; }
    @keyframes pulseGlow {
        0% { box-shadow: 0 8px 32px 0 rgba(163, 31, 36, 0.1); }
        50% { box-shadow: 0 8px 32px 0 rgba(163, 31, 36, 0.3); }
        100% { box-shadow: 0 8px 32px 0 rgba(163, 31, 36, 0.1); }
    }
    
    .event-card {
        display: flex; gap: 20px;
        background: white; border-radius: 12px;
        padding: 20px; margin-bottom: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #a31f24;
        transition: all 0.3s;
    }
    .event-card:hover { transform: translateX(10px); box-shadow: 0 8px 25px rgba(0,0,0,0.1); }
    .event-icon { background: rgba(163, 31, 36, 0.1); color: #a31f24; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; }
    .event-details h4 { color: #a31f24; margin-bottom: 10px; font-weight: 700; }
    .event-meta { font-size: 0.9rem; color: #666; margin-bottom: 10px; display: flex; gap: 15px; flex-wrap: wrap; }
    .event-meta span { display: inline-flex; align-items: center; gap: 5px; }
    .event-desc { color: #444; line-height: 1.6; }
    
    .pub-table { width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); border-radius: 8px; overflow: hidden; }
    .pub-table th, .pub-table td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
    .pub-table th { background: #a31f24; color: white; font-weight: 600; }
    .pub-table tr:hover { background: #f9f9f9; }
    .pub-table tr:last-child td { border-bottom: none; }
</style>
"""

coming_soon_html = f"""
{custom_css}
<div class="coming-soon-wrapper" data-aos="fade-up">
    <div class="glass-card animated-pulse">
        <i class="fa-solid fa-hourglass-half"></i>
        <h2>Under Development</h2>
        <p>This section is currently being updated with the latest information. Please check back soon for detailed insights and updates!</p>
    </div>
</div>
"""

pages = {
    # 1. LIVE DATA PAGES
    'cse_about.html': old_main,
    'dept_cse.html': old_main, # Same as about
    'cse_vision_mission.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">VISION & MISSION</h1>
    <section class="dept-section" data-aos="fade-up">
        <h3>VISION OF THE DEPARTMENT</h3>
        <p>To build competent industry ready professionals to largely contribute the society, by imparting the knowledge in the domain of Computer Science and Engineering with managerial skills, human and social values.</p>
    </section>
    <section class="dept-section" data-aos="fade-up" data-aos-delay="100">
        <h3>MISSION OF THE DEPARTMENT</h3>
        <p>To build competent industry ready professionals to largely contribute the society, by imparting the knowledge in the domain of Computer Science and Engineering with managerial skills, human and social values.</p>
    </section>
    """,
    'cse_peos.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">PEOs, POs & PSOs</h1>
    <section class="dept-section" data-aos="fade-up">
        <h3>PROGRAM EDUCATIONAL OBJECTIVES (PEOs)</h3>
        <p><strong>Graduates can:</strong></p>
        <ul style="line-height: 1.8; margin-left: 20px; padding-bottom: 20px;">
            <li>Develop proficiency as a computer science engineer with an ability to solve a wide range of computational problems and have sustainable development in industry or any other work environment.</li>
            <li>Analyze and adapt quickly to new environments and technologies, gather new information, and work on emerging technologies to solve multidisciplinary engineering problems.</li>
            <li>Possess the ability to think analytically and logically to understand technical problems with computational systems for a lifelong learning which leads to pursuing research.</li>
            <li>Adopt ethical practices to collaborate with team members and team leaders to build technology with cutting-edge technical solutions for computing systems.</li>
            <li>Strongly focus on design thinking and critical analysis to create innovative products and become entrepreneurs.</li>
        </ul>
        
        <h3>PROGRAM OUTCOMES (POs)</h3>
        <ul style="line-height: 1.8; margin-left: 20px; padding-bottom: 20px;">
            <li><strong>Engineering knowledge:</strong> Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex engineering problems.</li>
            <li><strong>Problem analysis:</strong> Identify, formulate, review research literature, and analyze complex engineering problems reaching substantiated conclusions.</li>
            <li><strong>Design/development of solutions:</strong> Design solutions for complex engineering problems and design system components or processes that meet the specified needs.</li>
            <li><strong>Conduct investigations of complex problems:</strong> Use research-based knowledge and research methods.</li>
            <li><strong>Modern tool usage:</strong> Create, select, and apply appropriate techniques, resources, and modern IT tools.</li>
        </ul>
        
        <h3>PROGRAM SPECIFIC OUTCOMES (PSOs)</h3>
        <ul style="line-height: 1.8; margin-left: 20px; padding-bottom: 20px;">
            <li>Exhibit design and programming skills to build and automate business solutions using cutting edge technologies.</li>
            <li>Strong theoretical foundation leading to excellence and excitement towards research, to provide elegant solutions to complex problems.</li>
            <li>Ability to work effectively with various engineering fields as a team to design, build and develop system applications.</li>
        </ul>
    </section>
    """,
    
    # 2. PDF EMBED PAGES
    'cse_board_of_studies.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">BOARD OF STUDIES</h1>
    <section class="dept-section" data-aos="fade-up">
        <p>The Board of Studies provides academic leadership and guidance for curriculum development and quality assurance.</p>
        <div style="margin-top: 30px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <iframe src="assets/cse/BOS-CSE.pdf" width="100%" height="800px" style="border: none;"></iframe>
        </div>
    </section>
    """,
    'cse_academic_calendar.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT ACADEMIC CALENDAR</h1>
    <section class="dept-section" data-aos="fade-up">
        <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <iframe src="assets/cse/academic_calendar.pdf" width="100%" height="800px" style="border: none;"></iframe>
        </div>
    </section>
    """,
    'cse_faculty.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT FACULTY</h1>
    <section class="dept-section" data-aos="fade-up">
        <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <iframe src="college-detail/Autonomous/UGC Mandatory Disclosure/3. Academics/4. Dept Faculty Details/CSE staff details.pdf" width="100%" height="800px" style="border: none;"></iframe>
        </div>
    </section>
    """,
    'cse_curriculum.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">CURRICULUM & SYLLABUS</h1>
    <section class="dept-section" data-aos="fade-up">
        <p>Explore our comprehensive and industry-aligned curriculum records.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px;">
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2013-B.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2013-B.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2013-M.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2013-M.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2017-B.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2017-B.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2017-M.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2017-M.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2021-B.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2021-B.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
            <div class="event-card">
                <div class="event-icon"><i class="fa-solid fa-file-pdf"></i></div>
                <div class="event-details">
                    <h4>R2021-M.E-CSE</h4>
                    <a href="assets/pdf/departments/cse/R2021-M.E-CSE.pdf" target="_blank" class="btn btn-danger btn-sm mt-2">View Syllabus</a>
                </div>
            </div>
        </div>
    </section>
    """,
    
    # 3. NEWSLETTER EXTRACTED DATA (Animated Glassmorphism Pages)
    'cse_events_organized.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">EVENTS ORGANIZED</h1>
    <section class="dept-section" data-aos="fade-up">
        
        <div class="event-card">
            <div class="event-icon"><i class="fa-brands fa-aws"></i></div>
            <div class="event-details">
                <h4>Workshop on AWS Cloud Data Architectures</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> August 2023</span>
                    <span><i class="fa-solid fa-users"></i> Students & Faculty</span>
                </div>
                <p class="event-desc">A comprehensive one-day workshop focusing on AWS Cloud data architectures, providing attendees with hands-on exposure to deploying and managing scalable data solutions on the cloud.</p>
            </div>
        </div>

        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-vr-cardboard"></i></div>
            <div class="event-details">
                <h4>Value Added Course: Semi-Immersive Reality</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> March 2024</span>
                    <span><i class="fa-solid fa-certificate"></i> Certification Provided</span>
                </div>
                <p class="event-desc">An engaging value-added course designed to introduce students to the emerging field of semi-immersive reality, blending physical and virtual realities for enhanced interactive experiences.</p>
            </div>
        </div>
        
    </section>
    """,
    'cse_guest_lectures.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">GUEST LECTURES & WORKSHOPS</h1>
    <section class="dept-section" data-aos="fade-up">
        
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-microphone-lines"></i></div>
            <div class="event-details">
                <h4>AWS Cloud Architectures Interactive Session</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> August 2023</span>
                    <span><i class="fa-solid fa-chalkboard-user"></i> Guest Speaker</span>
                </div>
                <p class="event-desc">Industry experts were invited to deliver a guest lecture breaking down the complexities of modern AWS cloud infrastructures, followed by an interactive Q&A session with CSE students.</p>
            </div>
        </div>

    </section>
    """,
    'cse_association_activities.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">ASSOCIATION ACTIVITIES & VISITS</h1>
    <section class="dept-section" data-aos="fade-up">
        
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-industry"></i></div>
            <div class="event-details">
                <h4>Industrial Visit to NARL, Tirupati</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> October 2023</span>
                    <span><i class="fa-solid fa-user-graduate"></i> II Year CSE Students</span>
                </div>
                <p class="event-desc">An educational industrial visit to the National Atmospheric Research Laboratory (NARL) ensuring students experience practical organizational workflows and technological executions.</p>
            </div>
        </div>

        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-building-user"></i></div>
            <div class="event-details">
                <h4>Industrial Visit to Incresco Technology, Bengaluru</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> March 2024</span>
                    <span><i class="fa-solid fa-user-graduate"></i> III Year CSE Students</span>
                </div>
                <p class="event-desc">Students gained exposure to the corporate software development lifecycle, agile methodologies, and IT infrastructure during this intensive industry connect session.</p>
            </div>
        </div>
        
    </section>
    """,
    'cse_student_publications.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">STUDENT ACHIEVEMENTS</h1>
    <section class="dept-section" data-aos="fade-up">
        
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-trophy"></i></div>
            <div class="event-details">
                <h4>First Place in Project Expo (KALAM'22)</h4>
                <div class="event-meta">
                    <span><i class="fa-solid fa-user"></i> Mr. Pulluru Bhavith</span>
                </div>
                <p class="event-desc">Secured the prestigious First Place in the highly competitive Project-Expo at KALAM'22, showcasing outstanding technical innovation and presentation skills.</p>
            </div>
        </div>

        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-medal"></i></div>
            <div class="event-details">
                <h4>Excellence in Sports</h4>
                <div class="event-meta">
                    <span><i class="fa-solid fa-users"></i> Mr. Pugazhvendhan, Ms. Tejaswini, Ms. Pavithra</span>
                </div>
                <p class="event-desc">Demonstrated phenomenal discipline and team spirit by bringing laurels to the CSE department in inter-college sports tournaments.</p>
            </div>
        </div>
        
    </section>
    """,
    'cse_research_publications.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">RESEARCH PUBLICATIONS</h1>
    <section class="dept-section" data-aos="fade-up">
        <p>Our faculty members consistently contribute to knowledge creation through rigorous research and publications in reputed journals.</p>
        
        <table class="pub-table" data-aos="fade-up" data-aos-delay="100">
            <thead>
                <tr>
                    <th>Faculty Name</th>
                    <th>Journal Name</th>
                    <th>Year/Issue</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>B. Sujai Mathew</strong></td>
                    <td>International Research Journal of Advanced Engineering and Technology (IRJAET)</td>
                    <td>2023 - 2024</td>
                </tr>
                <tr>
                    <td><strong>M. Sugavanam</strong></td>
                    <td>International Journal of Innovative Research in Multidisciplinary Education and Technology (IJIRMET)</td>
                    <td>2023 - 2024</td>
                </tr>
                <tr>
                    <td><strong>V. Vishal</strong></td>
                    <td>International Research Journal of Advanced Engineering and Technology (IRJAET)</td>
                    <td>2023 - 2024</td>
                </tr>
            </tbody>
        </table>
    </section>
    """,
    'cse_faculty_upskilling.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">FACULTY UPSKILLING</h1>
    <section class="dept-section" data-aos="fade-up">
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-chalkboard-user"></i></div>
            <div class="event-details">
                <h4>Faculty Development Programs (FDP)</h4>
                <div class="event-meta">
                    <span><i class="fa-regular fa-calendar"></i> Academic Year 2023-2024</span>
                </div>
                <p class="event-desc">The Department encourages continuous learning. Multiple faculty members attended specialized FDPs to upskill themselves in emerging technologies like Artificial Intelligence, Data Science, and Cloud Architecture, ensuring our curriculum delivery remains cutting-edge.</p>
            </div>
        </div>
    </section>
    """,
    'cse_faculty_achievements.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">FACULTY ACHIEVEMENTS</h1>
    <section class="dept-section" data-aos="fade-up">
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-award"></i></div>
            <div class="event-details">
                <h4>Research & Publication Excellence</h4>
                <p class="event-desc">Faculty members <b>B. Sujai Mathew</b>, <b>M. Sugavanam</b>, and <b>V. Vishal</b> successfully published high-impact research papers in international journals including IRJAET and IJIRMET during the 2023-2024 academic cycle.</p>
            </div>
        </div>
    </section>
    """,
    'cse_research_projects.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">RESEARCH PROJECTS</h1>
    <section class="dept-section" data-aos="fade-up">
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-microscope"></i></div>
            <div class="event-details">
                <h4>Ongoing Domain Explorations</h4>
                <p class="event-desc">The CSE Department engages in profound research spanning Artificial Intelligence, Cloud Computing, and Information Security. Internal sponsored projects serve as platforms for converting disruptive ideas into viable prototypes.</p>
            </div>
        </div>
    </section>
    """,
    'cse_phd_ms_research.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">Ph.D. / M.S. (RESEARCH)</h1>
    <section class="dept-section" data-aos="fade-up">
        <div class="event-card">
            <div class="event-icon"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="event-details">
                <h4>Research Capabilities</h4>
                <p class="event-desc">We foster an active environment for scholarly work. Our specialized faculty guide scholars diving deep into core computer science algorithms and applied tech fields, leading to significant journal publications.</p>
            </div>
        </div>
    </section>
    """,
    'cse_online_courses.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">ONLINE COURSES</h1>
    <section class="dept-section" data-aos="fade-up">
        <p>Continuous self-learning is promoted via platforms like NPTEL. Our students consistently secure certifications in demanding topics.</p>
        
        <table class="pub-table" data-aos="fade-up" data-aos-delay="100">
            <thead>
                <tr>
                    <th>Student Name</th>
                    <th>Platform</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Yuvan Prakash</strong></td>
                    <td>NPTEL</td>
                    <td>Successfully Completed</td>
                </tr>
                <tr>
                    <td><strong>Praveen Kumar</strong></td>
                    <td>NPTEL</td>
                    <td>Successfully Completed</td>
                </tr>
                <tr>
                    <td colspan="3" style="text-align: center; color: #666; font-style: italic;">...and numerous other enthusiastic students.</td>
                </tr>
            </tbody>
        </table>
    </section>
    """,
    'cse_newsletter_magazines.html': f"""
    {custom_css}
    <h1 class="dept-title-red" data-aos="fade-up">NEWSLETTER: TECH PULSE</h1>
    <section class="dept-section" data-aos="fade-up">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <p style="margin: 0;">Explore the complete stories, events, and highlights from the 2023-2024 academic year in our interactive newsletter viewer.</p>
            <a href="college-detail/Autonomous/News Letter/CSE.pdf" download class="btn btn-danger"><i class="fa-solid fa-download"></i> Download PDF</a>
        </div>
        <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <iframe src="college-detail/Autonomous/News Letter/CSE.pdf" width="100%" height="800px" style="border: none;"></iframe>
        </div>
    </section>
    """
}

# 4. MISSING ITEMS (Coming Soon)
coming_soon_files = [
    'cse_non_teaching_faculty.html',
    'cse_time_table.html',
    'cse_centre_of_excellence.html',
    'cse_best_practices.html',
    'cse_placement.html',
    'cse_higher_education.html',
    'cse_entrepreneurship.html',
    'cse_distinguished_alumni.html',
    'cse_professional_societies.html',
    'cse_club_activities.html',
    'cse_contact.html'
]

for cs_file in coming_soon_files:
    pages[cs_file] = coming_soon_html

# Write the files
def get_active_sidebar(pre_main, filename):
    # Regex to find the link for this filename and add class="active"
    # E.g. href="cse_about.html" -> href="cse_about.html" class="active"
    pattern = r'(<a href="' + re.escape(filename) + r'")'
    return re.sub(pattern, r'\1 class="active"', pre_main)

count = 0
for filename, content in pages.items():
    sidebar_active_pre_main = get_active_sidebar(pre_main, filename)
    full_html = sidebar_active_pre_main + '<main class="dept-main-content">' + content + suffix
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    count += 1
    print(f"Generated {filename}")

print(f"\\nSuccessfully generated {count} files.")
