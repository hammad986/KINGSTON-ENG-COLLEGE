import os
import re

# 1. Update cse_faculty.html
faculty_path = 'cse_faculty.html'
with open(faculty_path, 'r', encoding='utf-8') as f:
    faculty_html = f.read()

# We need to replace the content inside <main class="dept-main-content"> ... </main>
# We can just read from dept_cse.html (which is same for sidebar), but faculty_html already has it.

parts = faculty_html.split('<main class="dept-main-content">')
pre_main = parts[0]
post_main_raw = parts[1]
post_main_parts = post_main_raw.split('</main>')
post_main = '</main>' + post_main_parts[1]

new_faculty_content = """
            <style>
                .faculty-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                .faculty-table th, .faculty-table td {
                    border: 1px solid #ddd;
                    padding: 12px 16px;
                    text-align: left;
                    font-size: 0.95rem;
                }
                .faculty-table th {
                    background: #a31f24;
                    color: #fff;
                    font-weight: 600;
                }
                .faculty-table tr:nth-child(even) { background: #f8f9fa; }
                .faculty-table tr:hover { background: #fdf5f5; }
            </style>
            
            <h1 class="dept-title-red" data-aos="fade-up">DEPARTMENT FACULTY</h1>

            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY</h3>
                <p>The Department is enriched with a dedicated, well qualified and experienced faculty team of 5 Professors, 12 Associate Professors and 20 Assistant Professors specialized in various domains including Image Processing, Cloud Computing, Agent Computing, Computer Vision, Machine Learning, Deep Learning, Network Security, and Cyber Security.</p>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>FACULTY LIST</h3>
                <table class="faculty-table">
                    <thead>
                        <tr>
                            <th>S.No</th>
                            <th>Name</th>
                            <th>Designation</th>
                            <th>Qualification</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Placeholder rows to match CSBS style -->
                        <tr>
                            <td>1</td>
                            <td>Dr. B. Sujai Mathew</td>
                            <td>Professor</td>
                            <td>M.E., Ph.D.</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Dr. M. Sugavanam</td>
                            <td>Associate Professor</td>
                            <td>M.Tech., Ph.D.</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>Dr. V. Vishal</td>
                            <td>Assistant Professor</td>
                            <td>M.E., Ph.D.</td>
                        </tr>
                        <tr>
                            <td colspan="4" style="text-align:center;color:#666;font-style:italic;">Please refer to the detailed PDF below for the full list of our faculty members.</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <section class="dept-section" data-aos="fade-up">
                <h3>DETAILED FACULTY REFERENCE</h3>
                <div style="margin-top: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe src="college-detail/Autonomous/UGC Mandatory Disclosure/3. Academics/4. Dept Faculty Details/CSE staff details.pdf" width="100%" height="800px" style="border: none;"></iframe>
                </div>
            </section>
"""

with open(faculty_path, 'w', encoding='utf-8') as f:
    f.write(pre_main + '<main class="dept-main-content">' + new_faculty_content + post_main)
print("Updated cse_faculty.html")

# 2. Revert "Under Development" pages to empty template
coming_soon_files = {
    'cse_non_teaching_faculty.html': 'NON TEACHING FACULTY',
    'cse_time_table.html': 'TIME TABLE',
    'cse_centre_of_excellence.html': 'CENTRE OF EXCELLENCE',
    'cse_best_practices.html': 'BEST PRACTICES',
    'cse_placement.html': 'PLACEMENT',
    'cse_higher_education.html': 'HIGHER EDUCATION',
    'cse_entrepreneurship.html': 'ENTREPRENEURSHIP',
    'cse_distinguished_alumni.html': 'DISTINGUISHED ALUMNI',
    'cse_professional_societies.html': 'PROFESSIONAL SOCIETIES',
    'cse_club_activities.html': 'CLUB ACTIVITIES',
    'cse_contact.html': 'CONTACT US'
}

for cs_file, title in coming_soon_files.items():
    if os.path.exists(cs_file):
        with open(cs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parts_cs = content.split('<main class="dept-main-content">')
        if len(parts_cs) == 2:
            pre = parts_cs[0]
            post_raw = parts_cs[1]
            post = '</main>' + post_raw.split('</main>')[1]
            
            empty_content = f'''
            <h1 class="dept-title-red" data-aos="fade-up">{title}</h1>
            <section class="dept-section" data-aos="fade-up">
                <!-- Content to be added later -->
            </section>
            '''
            
            with open(cs_file, 'w', encoding='utf-8') as f:
                f.write(pre + '<main class="dept-main-content">' + empty_content + post)
            print(f"Reverted {cs_file}")

print("All updates successful.")
