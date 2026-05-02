import re

faculty_data = [
    ('Dr. S. R. Surem Samuel', 'Head of the Department', 'Ph.D', 'Artificial Intelligence', ''),
    ('Mrs. M. Rathika', 'Assistant Professor', 'M.E', 'VLSI Design', ''),
    ('Mr. Paul Richardson Gnanaraj J', 'Assistant Professor', 'M.E', 'VLSI Design', 'paulrichardson@kingston.ac.in'),
    ('Dr. Venkatesan A', 'Assistant Professor', 'M.E., Ph.D', 'VLSI Design, Wireless Communication', 'venkatesan@kingston.ac.in'),
    ('Mr. Raja S', 'Assistant Professor', 'M.Tech', 'Embedded System Technology', 'Rajaece.engineering@kingston.ac.in'),
    ('Mr. Thiyagarajan V', 'Assistant Professor', 'M.Tech', 'VLSI Design', 'thiyagarajan.engineering@kingston.ac.in'),
    ('Mr. Sathishkumar G', 'Assistant Professor', 'M.E', 'VLSI Design', 'Sathishkumar.engineering@kingston.ac.in'),
    ('Mrs. Thulasi Bruntha B', 'Assistant Professor', 'M.E', 'Power Electronics', 'thulashibrindha@kingston.ac.in'),
    ('Mr. Hariram S', 'Assistant Professor', 'M.E', 'VLSI Design', 'hariram.engineering@kingston.ac.in'),
    ('Mrs. Gracy Kavitha N', 'Assistant Professor', 'M.E', 'Applied Electronics', 'gracykavitha.engineering@kingston.ac.in'),
    ('Mrs. Vanitha N', 'Assistant Professor', 'M.Tech', 'Applied Electronics', 'vanitha@kingston.ac.in'),
    ('Mrs. Suganya S', 'Assistant Professor', 'M.E', 'Applied Electronics', 'suganyas.engineering@kingston.ac.in')
]

html_rows = ''
for i, f in enumerate(faculty_data):
    html_rows += f"""
                        <tr>
                            <td>{i+1}</td>
                            <td><strong>{f[0]}</strong></td>
                            <td>{f[1]}</td>
                            <td>{f[2]}</td>
                            <td>{f[3]}</td>
                            <td><a href="mailto:{f[4]}">{f[4]}</a></td>
                        </tr>"""

faculty_table_html = f"""            <section class="dept-section" data-aos="fade-up">
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
                        <tbody>{html_rows}
                        </tbody>
                    </table>
                </div>
            </section>
"""

with open('ece_faculty.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific section where the iframe is
new_content = content.replace('<section class="dept-section" data-aos="fade-up">\n                <h3>FACULTY REFERENCE</h3>', faculty_table_html + '\n            <section class="dept-section" data-aos="fade-up">\n                <h3>FACULTY REFERENCE</h3>')

with open('ece_faculty.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ece_faculty.html updated with table.")
