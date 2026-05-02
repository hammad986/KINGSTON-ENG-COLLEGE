import re

faculty_data = [
    ("Dr. Priya T", "Assistant Professor", "M.Tech., Ph.D."),
    ("Mrs. Yashema N", "Assistant Professor", "M.E."),
    ("Mrs. Manju A", "Assistant Professor", "M.E."),
    ("Mrs. Samundeeswari M", "Assistant Professor", "M.E."),
    ("Ms. Chinnima C", "Assistant Professor", "M.E."),
    ("Mrs. Manimala V", "Assistant Professor", "M.E."),
    ("Mrs. Archana S", "Assistant Professor", "M.E."),
    ("Mrs. Gayathri K H", "Assistant Professor", "M.E."),
    ("Mrs. Vanitha V", "Assistant Professor", "M.E."),
    ("Mrs. Sharmily D", "Assistant Professor", "M.E."),
    ("Mrs. Anandhi A V", "Assistant Professor", "M.E."),
    ("Mrs. Pavithra M", "Assistant Professor", "M.E."),
    ("Mrs. Mohana Sudha M", "Assistant Professor", "M.E."),
    ("Mr. Kavinilavan B", "Assistant Professor", "M.E."),
    ("Mr. Pradeep M", "Assistant Professor", "M.E."),
    ("Mrs. Haripriya S", "Assistant Professor", "M.E."),
    ("Mr. Kumar G J", "Assistant Professor", "M.E."),
    ("Mrs. Malini R", "Assistant Professor", "M.E.")
]

rows = ""
for i, (name, desig, qual) in enumerate(faculty_data, 1):
    rows += "                        <tr>\n"
    rows += f"                            <td>{i}</td>\n"
    rows += f"                            <td>{name}</td>\n"
    rows += f"                            <td>{desig}</td>\n"
    rows += f"                            <td>{qual}</td>\n"
    rows += "                        </tr>\n"

# Add the final reference note row
rows += '''                        <tr>
                            <td colspan="4" style="text-align:center;color:#666;font-style:italic;padding:15px;">Please refer to the detailed PDF below for specializations and contact information.</td>
                        </tr>'''

file_path = "cse_faculty.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"(<tbody>).*?(</tbody>)"
new_content = re.sub(pattern, rf"\1\n{rows}\n                    \2", content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Added {len(faculty_data)} faculty members to cse_faculty.html")
