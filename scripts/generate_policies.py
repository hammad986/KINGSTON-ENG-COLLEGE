import os
import requests
import re

# List of policies and their PDF links
policies = [
    ("ALUMNI POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/1.%20ALUMNI%20POLICY.pdf"),
    ("ACADEMIC AUDIT POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/ACADEMIC%20AUDIT%20POLICY.pdf"),
    ("ADMISSION POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/ADMISSION%20POLICY.pdf"),
    ("CODE OF ETHICS AND CONDUCT", "https://engineering.kingston.ac.in/about/policies/code-of-ethics-and-construct"), # Detail page as fallback
    ("E-GOVERNANCE POLICY", "https://engineering.kingston.ac.in/about/policies/e-goverance-policy"), # Detail page as fallback
    ("ENVIRONMENTAL AND GREEN CAMPUS POLICIES", "https://engineering.kingston.ac.in/assets/pdf/policy/ENVIRONMENTAL%20AND%20GREEN%20CAMPUS%20POLICIES.pdf"),
    ("E-WASTE MANAGEMENT POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/E-WASTE%20MANAGEMENT%20POLICY.pdf"),
    ("FINANCE POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/FINANCE%20POLICY.pdf"),
    ("HUMAN RESOURCES POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/HUMAN%20RESOURCES%20POLICY.pdf"),
    ("INFORMATION TECHNOLOGY POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/INFORMATION%20TECHNOLOGY%20POLICY.pdf"),
    ("INFRASTRUCTURE MAINTENANCE POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/INFRASTRUCTURE%20MAINTENANCE%20POLICY.pdf"),
    ("INTERNAL QUALITY ASSURANCE POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/INTERNAL%20QUALITY%20ASSURANCE%20POLICY.pdf"),
    ("LIBRARY POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/LIBRARY%20POLICY.pdf"),
    ("MOU POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/MOU_POLICY.pdf"),
    ("PLACEMENT POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/PLACEMENT_POLICY.pdf"),
    ("PURCHASE POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/PURCHASE_POLICY.pdf"),
    ("R&D POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/R&D_Policy.pdf"),
    ("SCHOLARSHIP POLICY", "https://engineering.kingston.ac.in/assets/pdf/scholarship_policy.pdf"),
    ("SPORTS POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/SPORTS_POLICY.pdf"),
    ("STUDENT EMPOWERMENT POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/STUDENT_EMPOWERMENT_POLICY.pdf"),
    ("VALUE ADDED POLICY", "https://engineering.kingston.ac.in/assets/pdf/policy/VALUE_ADDED_POLICY.pdf")
]

PDF_DIR = r"assets\pdfs\policies"
if not os.path.exists(PDF_DIR):
    os.makedirs(PDF_DIR)

def download_pdfs():
    print("Downloading PDFs...")
    local_policies = []
    for title, url in policies:
        if url.endswith(".pdf"):
            filename = os.path.basename(url)
            # Remove %20 and other URL encoding
            filename = requests.utils.unquote(filename)
            local_path = os.path.join(PDF_DIR, filename)
            
            if not os.path.exists(local_path):
                try:
                    print(f"Downloading {title}...")
                    response = requests.get(url, timeout=30)
                    if response.status_code == 200:
                        with open(local_path, "wb") as f:
                            f.write(response.content)
                        local_policies.append((title, local_path.replace("\\", "/")))
                    else:
                        print(f"Failed to download {title}: Status {response.status_code}")
                        local_policies.append((title, url)) # Fallback to live URL
                except Exception as e:
                    print(f"Error downloading {title}: {e}")
                    local_policies.append((title, url)) # Fallback to live URL
            else:
                local_policies.append((title, local_path.replace("\\", "/")))
        else:
            # For non-pdf links (broken or detail pages)
            local_policies.append((title, url))
    return local_policies

def generate_html(policy_data):
    print("Generating policies.html...")
    with open("about.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Extract header (up to </header>)
    header_match = re.search(r'([\s\S]*?<\/header>)', content)
    header = header_match.group(1) if header_match else ""
    
    # Extract footer (from <footer> or similar)
    # Finding the footer start - usually <footer or the part after main content
    footer_match = re.search(r'(<footer[\s\S]*?<\/html>)', content)
    if not footer_match:
        # Fallback: find the last </div> before </body> and treat as footer start if no <footer>
        footer_match = re.search(r'(<div class="footer-bottom"[\s\S]*?<\/html>)', content)
    
    footer = footer_match.group(1) if footer_match else "</body></html>"

    # Define the core styles for the Policies page
    extra_styles = """
    <style>
        .policies-section {
            padding: 80px 0;
            background: #f8f9fa;
        }
        .policies-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        .policy-card {
            background: #fff;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid #eee;
            position: relative;
            overflow: hidden;
        }
        .policy-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.1);
            border-color: #f5c518;
        }
        .policy-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #003366, #f5c518);
            transform: scaleX(0);
            transition: transform 0.3s ease;
            transform-origin: left;
        }
        .policy-card:hover::before {
            transform: scaleX(1);
        }
        .policy-icon {
            font-size: 3rem;
            color: #003366;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        .policy-card:hover .policy-icon {
            transform: scale(1.1) rotate(5deg);
        }
        .policy-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: #333;
            margin-bottom: 20px;
            text-transform: uppercase;
            line-height: 1.4;
        }
        .btn-view-policy {
            display: inline-block;
            padding: 10px 20px;
            background: #003366;
            color: #fff;
            border-radius: 25px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            margin-top: auto;
        }
        .btn-view-policy:hover {
            background: #f5c518;
            color: #003366;
            box-shadow: 0 5px 15px rgba(245, 197, 24, 0.3);
        }
        .section-header {
            text-align: center;
            margin-bottom: 50px;
        }
        .section-header h1 {
            font-size: 2.5rem;
            color: #003366;
            font-weight: 800;
            position: relative;
            display: inline-block;
            margin-bottom: 15px;
        }
        .section-header h1::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: #f5c518;
            border-radius: 2px;
        }
        .section-header p {
            color: #666;
            font-size: 1.1rem;
        }
    </style>
    """

    # Insert extra styles before </head>
    header = header.replace("</head>", extra_styles + "\n</head>")

    body_content = f"""
    <main>
        <section class="policies-section">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <h1>Institutional Policies</h1>
                    <p>Guiding principles for excellence in education and governance</p>
                </div>
                
                <div class="policies-grid">
    """

    for i, (title, path) in enumerate(policy_data):
        delay = (i % 3) * 100
        body_content += f"""
                    <div class="policy-card" data-aos="fade-up" data-aos-delay="{delay}">
                        <div class="policy-icon">
                            <i class="fa-solid fa-file-shield"></i>
                        </div>
                        <h3 class="policy-title">{title}</h3>
                        <a href="{path}" target="_blank" class="btn-view-policy">
                            <i class="fa-solid fa-file-pdf mr-2"></i> View Policy
                        </a>
                    </div>
        """

    body_content += """
                </div>
            </div>
        </section>
    </main>
    """

    # Assemble final HTML
    final_html = header + body_content + footer
    
    with open("policies.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    print("policies.html created successfully.")

if __name__ == "__main__":
    policy_data = download_pdfs()
    generate_html(policy_data)
