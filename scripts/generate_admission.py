import os
import requests
import re

# List of admission PDFs and their links
admission_pdfs = [
    ("Eligibility Criteria", "https://engineering.kingston.ac.in/assets/pdf/Eligibility.pdf"),
    ("Online Admission Procedure", "https://engineering.kingston.ac.in/assets/pdf/OnlineProcedure.pdf"),
    ("Scholarship Policy", "https://engineering.kingston.ac.in/assets/pdf/scholarship_policy.pdf")
]

PDF_DIR = r"assets\pdfs\admission"
if not os.path.exists(PDF_DIR):
    os.makedirs(PDF_DIR)

def download_pdfs():
    print("Downloading Admission PDFs...")
    local_pdfs = {}
    for title, url in admission_pdfs:
        filename = os.path.basename(url)
        filename = requests.utils.unquote(filename)
        local_path = os.path.join(PDF_DIR, filename)
        
        if not os.path.exists(local_path):
            try:
                print(f"Downloading {title}...")
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    with open(local_path, "wb") as f:
                        f.write(response.content)
                    local_pdfs[title] = local_path.replace("\\", "/")
                else:
                    print(f"Failed to download {title}: Status {response.status_code}")
                    local_pdfs[title] = url
            except Exception as e:
                print(f"Error downloading {title}: {e}")
                local_pdfs[title] = url
        else:
            local_pdfs[title] = local_path.replace("\\", "/")
    return local_pdfs

def generate_html(pdf_data):
    print("Generating admission.html...")
    with open("about.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Extract header and footer
    header_match = re.search(r'([\s\S]*?<\/header>)', content)
    header = header_match.group(1) if header_match else ""
    
    footer_match = re.search(r'(<footer[\s\S]*?<\/html>)', content)
    if not footer_match:
        footer_match = re.search(r'(<div class="footer-bottom"[\s\S]*?<\/html>)', content)
    footer = footer_match.group(1) if footer_match else "</body></html>"

    extra_styles = """
    <style>
        .admission-container {
            padding: 80px 0;
            background: #fdfdfd;
        }
        .admission-header {
            text-align: center;
            margin-bottom: 60px;
        }
        .admission-header h1 {
            font-size: 3rem;
            color: #003366;
            font-weight: 900;
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        .admission-header p {
            font-size: 1.2rem;
            color: #555;
            max-width: 800px;
            margin: 0 auto;
        }

        /* Tabs Styling */
        .tabs-nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 50px;
            flex-wrap: wrap;
        }
        .tab-btn {
            padding: 15px 30px;
            border: 2px solid #003366;
            background: transparent;
            color: #003366;
            font-size: 1rem;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }
        .tab-btn:hover {
            transform: translateY(-5px);
            background: rgba(0, 51, 102, 0.05);
        }
        .tab-btn.active {
            background: #003366;
            color: #fff;
            box-shadow: 0 10px 25px rgba(0, 51, 102, 0.2);
        }

        .tab-content {
            display: none;
            animation: fadeInUp 0.6s ease forwards;
        }
        .tab-content.active {
            display: block;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Section Cards */
        .content-card {
            background: #fff;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.05);
            border: 1px solid #f0f0f0;
            margin-bottom: 30px;
        }
        .content-card h2 {
            font-size: 2rem;
            color: #003366;
            margin-bottom: 30px;
            border-left: 5px solid #f5c518;
            padding-left: 20px;
        }

        /* Programmes List */
        .programmes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        .prog-item {
            padding: 20px;
            background: #f8faff;
            border-radius: 12px;
            border-left: 4px solid #f5c518;
            transition: all 0.3s;
        }
        .prog-item:hover {
            transform: translateX(10px);
            background: #f0f4ff;
        }
        .prog-item h4 {
            margin: 0;
            color: #333;
            font-weight: 700;
        }

        /* Info Boxes */
        .info-box {
            background: #003366;
            color: #fff;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin-top: 30px;
        }
        .info-box h3 { margin-top: 0; color: #f5c518; }
        .counsel-code {
            font-size: 3rem;
            font-weight: 900;
            display: block;
            margin: 15px 0;
            letter-spacing: 5px;
        }

        /* PDF Preview Area */
        .pdf-frame-wrapper {
            margin-top: 30px;
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #ddd;
            height: 600px;
        }
        iframe { width: 100%; height: 100%; border: none; }

        .btn-pdf {
            display: inline-block;
            padding: 12px 25px;
            background: #f5c518;
            color: #003366;
            border-radius: 8px;
            font-weight: 700;
            text-decoration: none;
            margin-top: 15px;
            transition: 0.3s;
        }
        .btn-pdf:hover {
            background: #e5b515;
            box-shadow: 0 5px 15px rgba(245, 197, 24, 0.4);
        }
    </style>
    """

    header = header.replace("</head>", extra_styles + "\n</head>")

    body_content = f"""
    <main>
        <section class="admission-container">
            <div class="container">
                <div class="admission-header" data-aos="fade-down">
                    <h1>Admissions 2026-27</h1>
                    <p>Join a community of innovators and leaders. Kingston Engineering College offers industry-aligned programs and a vibrant learning ecosystem.</p>
                </div>

                <div class="tabs-nav" data-aos="fade-up">
                    <button class="tab-btn active" onclick="openTab(event, 'details')">Admission Details</button>
                    <button class="tab-btn" onclick="openTab(event, 'programmes')">Programmes Offered</button>
                    <button class="tab-btn" onclick="openTab(event, 'eligibility')">Eligibility Criteria</button>
                    <button class="tab-btn" onclick="openTab(event, 'guideline')">Admission Guideline</button>
                    <button class="tab-btn" onclick="openTab(event, 'scholarship')">Scholarship Policy</button>
                </div>

                <!-- Tab: Details -->
                <div id="details" class="tab-content active">
                    <div class="content-card">
                        <h2>Admission Counselling</h2>
                        <p>Admission eligibility for B.E, B.Tech, M.E and M.B.A Program as per the Tamil Nadu government and Anna University norms.</p>
                        <div class="info-box">
                            <h3>Anna University Counselling Code</h3>
                            <span class="counsel-code">1520</span>
                            <p>Use this code during TNEA counselling to choose Kingston Engineering College.</p>
                        </div>
                    </div>
                </div>

                <!-- Tab: Programmes -->
                <div id="programmes" class="tab-content">
                    <div class="content-card">
                        <h2>Undergraduate (UG) - 4 Years</h2>
                        <div class="programmes-grid">
                            <div class="prog-item"><h4>B.E. Computer Science and Engineering</h4></div>
                            <div class="prog-item"><h4>B.E. Electrical and Electronics Engineering</h4></div>
                            <div class="prog-item"><h4>B.E. Electronics and Communication Engineering</h4></div>
                            <div class="prog-item"><h4>B.Tech. Information Technology</h4></div>
                            <div class="prog-item"><h4>B.E. Mechanical Engineering</h4></div>
                            <div class="prog-item"><h4>B.E. Civil Engineering</h4></div>
                            <div class="prog-item"><h4>B.Tech. Artificial Intelligence and Data Science</h4></div>
                            <div class="prog-item"><h4>B.Tech. Computer Science and Business Systems</h4></div>
                            <div class="prog-item"><h4>B.E. Cyber Security</h4></div>
                        </div>
                        <h2 style="margin-top:50px;">Postgraduate (PG) - 2 Years</h2>
                        <div class="programmes-grid">
                            <div class="prog-item"><h4>M.E. Computer Science and Engineering</h4></div>
                            <div class="prog-item"><h4>M.E. VLSI Design</h4></div>
                            <div class="prog-item"><h4>M.E. Engineering Design</h4></div>
                            <div class="prog-item"><h4>M.E. Applied Electronics</h4></div>
                            <div class="prog-item"><h4>Master of Business Administration (MBA)</h4></div>
                        </div>
                    </div>
                </div>

                <!-- Tab: Eligibility -->
                <div id="eligibility" class="tab-content">
                    <div class="content-card">
                        <h2>Eligibility Criteria</h2>
                        <p>Academic requirements for admission based on qualifying marks and appearances.</p>
                        <a href="{pdf_data['Eligibility Criteria']}" target="_blank" class="btn-pdf">
                            <i class="fa-solid fa-download"></i> Download Eligibility PDF
                        </a>
                        <div class="pdf-frame-wrapper">
                            <iframe src="{pdf_data['Eligibility Criteria']}#toolbar=0"></iframe>
                        </div>
                    </div>
                </div>

                <!-- Tab: Guideline -->
                <div id="guideline" class="tab-content">
                    <div class="content-card">
                        <h2>Online Admission Procedure</h2>
                        <p>Follow these steps to complete your registration and application online.</p>
                        <a href="{pdf_data['Online Admission Procedure']}" target="_blank" class="btn-pdf">
                            <i class="fa-solid fa-download"></i> Download Procedure PDF
                        </a>
                        <div class="pdf-frame-wrapper">
                            <iframe src="{pdf_data['Online Admission Procedure']}#toolbar=0"></iframe>
                        </div>
                    </div>
                </div>

                <!-- Tab: Scholarship -->
                <div id="scholarship" class="tab-content">
                    <div class="content-card">
                        <h2>Scholarship Policy</h2>
                        <p>Learn about merit-based scholarships and financial aid opportunities.</p>
                        <a href="{pdf_data['Scholarship Policy']}" target="_blank" class="btn-pdf">
                            <i class="fa-solid fa-download"></i> Download Scholarship PDF
                        </a>
                        <div class="pdf-frame-wrapper">
                            <iframe src="{pdf_data['Scholarship Policy']}#toolbar=0"></iframe>
                        </div>
                    </div>
                </div>

            </div>
        </section>
    </main>

    <script>
    function openTab(evt, tabName) {{
        var i, tabContent, tabBtns;
        tabContent = document.getElementsByClassName("tab-content");
        for (i = 0; i < tabContent.length; i++) {{
            tabContent[i].classList.remove("active");
        }}
        tabBtns = document.getElementsByClassName("tab-btn");
        for (i = 0; i < tabBtns.length; i++) {{
            tabBtns[i].classList.remove("active");
        }}
        document.getElementById(tabName).classList.add("active");
        evt.currentTarget.classList.add("active");
        
        // Refresh AOS to handle newly visible content
        if (typeof AOS !== 'undefined') {{
            AOS.refresh();
        }}
    }}
    </script>
    """

    final_html = header + body_content + footer
    
    with open("admission.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    print("admission.html created successfully.")

if __name__ == "__main__":
    pdf_info = download_pdfs()
    generate_html(pdf_info)
