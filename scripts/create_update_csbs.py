import os
import re
import glob

base_dir = r"c:\Users\mdham\Downloads\Kingston-Engineering-College-main\Kingston-Engineering-College-main"
template_file = os.path.join(base_dir, "csbs_about.html")

try:
    with open(template_file, "r", encoding="utf-8") as f:
        template_html = f.read()
except FileNotFoundError:
    print(f"Error: Template file not found at {template_file}")
    exit(1)

# Function to replace main content and title
def create_page(filename, title, active_link, main_content_html):
    # Update title
    html = re.sub(r'<title>.*?</title>', f'<title>{title} - CSBS | Kingston Engineering College</title>', template_html, flags=re.IGNORECASE)
    
    # Replace main content
    main_regex = r'(<main class="dept-main-content">)(.*?)(</main>)'
    # We want to keep the H1 title in main content, so we just replace everything after the H1 or generate the whole main content.
    new_main = f'''<main class="dept-main-content">

            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT OF<br>COMPUTER SCIENCE AND BUSINESS SYSTEMS</h1>

{main_content_html}

        </main>'''
    
    html = re.sub(main_regex, new_main, html, flags=re.DOTALL | re.IGNORECASE)
    
    # Save file
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {filename}")

# 1. Industry Visits Page
ind_visits_html = '''
            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY VISITS TO INDUSTRY</h3>
                <div class="events-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                    
                    <div class="event-card" data-aos="fade-up" data-aos-delay="100" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-left:4px solid var(--brand-blue); transition:transform 0.3s ease;">
                        <div style="font-size:0.8rem; color:#666; margin-bottom:5px;"><i class="fa-regular fa-calendar"></i> Jan 9-10, 2025</div>
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">Umagine TN 2025</h4>
                        <p style="font-size:0.9rem; margin-bottom:0;">Faculty members participated in this flagship technology event by Govt. of Tamil Nadu, engaging with thought leaders and exploring cross-institutional collaboration.</p>
                    </div>

                    <div class="event-card" data-aos="fade-up" data-aos-delay="200" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-left:4px solid var(--brand-yellow); transition:transform 0.3s ease;">
                        <div style="font-size:0.8rem; color:#666; margin-bottom:5px;"><i class="fa-regular fa-calendar"></i> Jan 23, 2025</div>
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">Systech Solutions Pvt. Ltd., Chennai</h4>
                        <p style="font-size:0.9rem; margin-bottom:0;">Visit to understand current industry practices, data-centric solutions, and to strengthen academia-industry bridge.</p>
                    </div>

                    <div class="event-card" data-aos="fade-up" data-aos-delay="300" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-left:4px solid var(--green); transition:transform 0.3s ease;">
                        <div style="font-size:0.8rem; color:#666; margin-bottom:5px;"><i class="fa-regular fa-calendar"></i> Jul 15, 2024</div>
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">Infosys & Infoview, Chennai</h4>
                        <p style="font-size:0.9rem; margin-bottom:0;">Familiarization with evolving technology trends and opportunities for institutional collaboration and knowledge exchange.</p>
                    </div>
                    
                    <div class="event-card" data-aos="fade-up" data-aos-delay="400" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-left:4px solid var(--light-gray); transition:transform 0.3s ease;">
                        <div style="font-size:0.8rem; color:#666; margin-bottom:5px;"><i class="fa-regular fa-calendar"></i> Jul 8, 2024</div>
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">CSIR & Bahwan CyberTek, Chennai</h4>
                        <p style="font-size:0.9rem; margin-bottom:0;">Exploration of ongoing research initiatives, collaborative projects in science, and strategic technological trends.</p>
                    </div>

                    <div class="event-card" data-aos="fade-up" data-aos-delay="500" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-left:4px solid var(--brand-blue); transition:transform 0.3s ease;">
                        <div style="font-size:0.8rem; color:#666; margin-bottom:5px;"><i class="fa-regular fa-calendar"></i> Jun 22, 2024</div>
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">TANSAM</h4>
                        <p style="font-size:0.9rem; margin-bottom:0;">Explored advanced manufacturing ecosystem designed to support MSMEs and students across Tamil Nadu for Aerospace, EV and Defense.</p>
                    </div>

                </div>
            </section>
'''
create_page("csbs_industry_visits.html", "Faculty Visits to Industry", "csbs_industry_visits.html", ind_visits_html)

# 2. Student Participations Page
stu_part_html = '''
            <section class="dept-section" data-aos="fade-up">
                <h3>STUDENT PARTICIPATIONS (Workshops & Symposiums)</h3>
                <p>Highlighting the active participation of our students in various national level symposiums, workshops, and paper presentations.</p>
                
                <div class="events-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                    <div class="event-card" data-aos="fade-up" data-aos-delay="100" style="background:#fff; border-radius:12px; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,0.05); border-top:4px solid var(--brand-blue); transition:transform 0.3s ease;">
                        <h4 style="color:var(--brand-red); margin-bottom:10px; font-size:1.1rem;">Eloquence'24 Symposium</h4>
                        <p style="font-size:0.9rem; color:#444; margin-bottom:15px;">Participated in paper presentation at the 7th National level Symposium at <strong>C. Abdul Hakeem College of Engineering and Technology</strong>.</p>
                        
                        <div style="background:#f8f9fa; padding:15px; border-radius:8px;">
                            <h5 style="color:var(--brand-blue); margin-bottom:10px; font-size:0.95rem;">Participating Students:</h5>
                            <ul style="font-size:0.85rem; margin-left:1rem; margin-bottom:0; color:#555;">
                                <li><strong>Sathyasadhana. S</strong> (III Year, Reg: 511322244025)</li>
                                <li><strong>Divya. K</strong> (III Year, Reg: 511322244005)</li>
                                <li><strong>Priyanka. S</strong> (III Year, Reg: 511322244019)</li>
                                <li><strong>Harini Sree. S</strong> (III Year, Reg: 511322244009)</li>
                                <li><strong>Bhavyasree. G.R</strong> (II Year, Reg: 511323244005)</li>
                                <li><strong>Swetha. S</strong> (II Year, Reg: 511323244029)</li>
                                <li><strong>Nivethitha. K.V</strong> (II Year, Reg: 511323244019)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
'''
create_page("csbs_student_participations.html", "Student Participations", "csbs_student_participations.html", stu_part_html)

# 3. Toppers List Page
toppers_html = '''
            <section class="dept-section" data-aos="fade-up">
                <h3>DEPARTMENT TOPPERS LIST</h3>
                <p>Recognizing the academic excellence of our students in the Anna University Examinations (November/December 2024).</p>
                
                <div class="table-responsive mt-4" data-aos="fade-up" data-aos-delay="150" style="box-shadow: 0 5px 20px rgba(0,0,0,0.05); border-radius:8px; overflow:hidden;">
                    <table class="data-table" style="width:100%; border-collapse: collapse; text-align:left;">
                        <thead>
                            <tr style="background-color: var(--brand-blue); color: #fff;">
                                <th style="padding:15px;">S.No</th>
                                <th style="padding:15px;">Year</th>
                                <th style="padding:15px;">Rank</th>
                                <th style="padding:15px;">Registration No.</th>
                                <th style="padding:15px;">Student Name</th>
                                <th style="padding:15px;">Semester</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- II Year -->
                            <tr style="background:#fdfdfd; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">1</td>
                                <td style="padding:15px; font-weight:600; color:var(--brand-red);" rowspan="3">II CSBS</td>
                                <td style="padding:15px;"><span style="display:inline-block; width:25px; height:25px; background:gold; color:#000; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">1</span></td>
                                <td style="padding:15px;">511323244024</td>
                                <td style="padding:15px; font-weight:500;">M. Sabari</td>
                                <td style="padding:15px;">4</td>
                            </tr>
                            <tr style="background:#fdfdfd; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">2</td>
                                <td style="padding:15px;"><span style="display:inline-block; width:25px; height:25px; background:#e0e0e0; color:#000; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">2</span></td>
                                <td style="padding:15px;">511323244027</td>
                                <td style="padding:15px; font-weight:500;">C. Shobana</td>
                                <td style="padding:15px;">4</td>
                            </tr>
                            <tr style="background:#fdfdfd; border-bottom:2px solid #ddd;">
                                <td style="padding:15px;">3</td>
                                <td style="padding:15px;"><span style="display:inline-block; width:25px; height:25px; background:#cd7f32; color:#fff; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">3</span></td>
                                <td style="padding:15px;">511323244002</td>
                                <td style="padding:15px; font-weight:500;">P. Atchaya</td>
                                <td style="padding:15px;">4</td>
                            </tr>
                            
                            <!-- III Year -->
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">4</td>
                                <td style="padding:15px; font-weight:600; color:var(--brand-blue);" rowspan="10">III CSBS</td>
                                <td style="padding:15px;" rowspan="2"><span style="display:inline-block; width:25px; height:25px; background:gold; color:#000; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">1</span></td>
                                <td style="padding:15px;">511322244013</td>
                                <td style="padding:15px; font-weight:500;">S. Mathumitha</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">5</td>
                                <td style="padding:15px;">511322244019</td>
                                <td style="padding:15px; font-weight:500;">S. Priyanka</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            
                            <tr style="background:#fdfdfd; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">6</td>
                                <td style="padding:15px;" rowspan="2"><span style="display:inline-block; width:25px; height:25px; background:#e0e0e0; color:#000; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">2</span></td>
                                <td style="padding:15px;">511322244002</td>
                                <td style="padding:15px; font-weight:500;">M. Baviya</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fdfdfd; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">7</td>
                                <td style="padding:15px;">511322244009</td>
                                <td style="padding:15px; font-weight:500;">S. Harini Sree</td>
                                <td style="padding:15px;">6</td>
                            </tr>

                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">8</td>
                                <td style="padding:15px;" rowspan="6"><span style="display:inline-block; width:25px; height:25px; background:#cd7f32; color:#fff; text-align:center; border-radius:50%; font-weight:bold; line-height:25px;">3</span></td>
                                <td style="padding:15px;">511322244001</td>
                                <td style="padding:15px; font-weight:500;">G. Archana</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">9</td>
                                <td style="padding:15px;">511322244004</td>
                                <td style="padding:15px; font-weight:500;">J. Dharshan</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">10</td>
                                <td style="padding:15px;">511322244005</td>
                                <td style="padding:15px; font-weight:500;">K. Divya</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">11</td>
                                <td style="padding:15px;">511322244014</td>
                                <td style="padding:15px; font-weight:500;">B. Monica</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">12</td>
                                <td style="padding:15px;">511322244018</td>
                                <td style="padding:15px; font-weight:500;">M.P. Oppiliyappan</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                            <tr style="background:#fff; border-bottom:1px solid #eee;">
                                <td style="padding:15px;">13</td>
                                <td style="padding:15px;">511322244022</td>
                                <td style="padding:15px; font-weight:500;">V. Salini</td>
                                <td style="padding:15px;">6</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>
'''
create_page("csbs_toppers.html", "Department Toppers List", "csbs_toppers.html", toppers_html)

# Update sidebar in all csbs_*.html files
print("Updating sidebars...")
files = glob.glob(os.path.join(base_dir, "csbs_*.html"))
files.append(os.path.join(base_dir, "dept_csbs.html"))

# The new links to inject
new_links_html = '''<li><a href="csbs_industry_visits.html"><i class="fa-solid fa-building"></i> Industry Visits</a></li>
                <li><a href="csbs_student_participations.html"><i class="fa-solid fa-users-viewfinder"></i> Student Participations</a></li>
                <li><a href="csbs_toppers.html"><i class="fa-solid fa-medal"></i> Toppers List</a></li>'''

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Strip out these links if they exist to prevent duplicates
    content = re.sub(r'<li><a href="csbs_industry_visits\.html".*?</li>\n\s*', '', content)
    content = re.sub(r'<li><a href="csbs_student_participations\.html".*?</li>\n\s*', '', content)
    content = re.sub(r'<li><a href="csbs_toppers\.html".*?</li>\n\s*', '', content)

    # 2. Insert new links right after "Faculty Achievements"
    insert_point = r'(<li><a href="csbs_faculty_achievements\.html".*?</li>)'
    replacement = r'\1\n                ' + new_links_html
    content = re.sub(insert_point, replacement, content)

    # 3. Handle active class dynamically based on filename
    basename = os.path.basename(filepath)
    # Remove all active classes from the sidebar menu first
    content = re.sub(r'(<ul class="dept-sidebar-menu">.*?</ul>)', 
                     lambda m: m.group(1).replace('class="active"', ''), 
                     content, flags=re.DOTALL)
    
    # Add active class to the current file's link
    content = re.sub(rf'(<a href="{basename}")', r'\1 class="active"', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Sidebar update complete.")
