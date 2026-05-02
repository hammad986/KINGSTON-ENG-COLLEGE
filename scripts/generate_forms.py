import os
import re

def generate_form_page(filename, title, form_html, extra_css=""):
    print(f"Generating {filename}...")
    with open("about.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Extract header and footer
    header_match = re.search(r'([\s\S]*?<\/header>)', template)
    header = header_match.group(1) if header_match else ""
    
    footer_match = re.search(r'(<footer[\s\S]*?<\/html>)', template)
    if not footer_match:
        footer_match = re.search(r'(<div class="footer-bottom"[\s\S]*?<\/html>)', template)
    footer = footer_match.group(1) if footer_match else "</body></html>"

    # Inject title
    header = re.sub(r'<title>.*?</title>', f'<title>{title} - Kingston Engineering College</title>', header)

    # Base styles for forms
    base_css = """
    .form-hero { position: relative; width: 100%; height: 350px; overflow: hidden; background: #000; display: flex; align-items: center; justify-content: center; text-align: center; }
    .form-hero video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; }
    .form-hero-content { position: relative; z-index: 10; color: #fff; }
    .form-hero-content h1 { font-size: 3.5rem; font-weight: 900; text-transform: uppercase; margin-bottom: 15px; }
    .form-hero-content p { font-size: 1.2rem; opacity: 0.9; font-weight: 500; }

    .form-container-wrap { padding: 80px 0; background: #f4f7fa; }
    .glass-form-card { background: #fff; border-radius: 20px; box-shadow: 0 25px 50px rgba(0,0,0,0.1); padding: 50px; overflow: hidden; border: 1px solid #eee; }
    
    .form-group { margin-bottom: 25px; position: relative; }
    .form-group label { display: block; margin-bottom: 8px; font-weight: 700; color: #003366; font-size: 0.95rem; }
    .form-control { width: 100%; padding: 12px 18px; border-radius: 10px; border: 2px solid #e1e8ef; transition: 0.3s; font-size: 1rem; }
    .form-control:focus { border-color: #f5c518; outline: none; box-shadow: 0 0 10px rgba(245, 197, 24, 0.1); }
    
    .btn-submit { background: #003366; color: #fff; padding: 15px 40px; border-radius: 30px; border: none; font-weight: 800; font-size: 1.1rem; cursor: pointer; transition: 0.4s; width: 100%; text-transform: uppercase; letter-spacing: 1px; }
    .btn-submit:hover { background: #f5c518; color: #000; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }

    /* Multi-step logic styles */
    .step-indicator { display: flex; justify-content: space-between; margin-bottom: 40px; }
    .step { width: 40px; height: 40px; border-radius: 50%; background: #e1e8ef; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #777; transition: 0.3s; }
    .step.active { background: #003366; color: #fff; transform: scale(1.1); }
    .step.completed { background: #27ae60; color: #fff; }
    .step-line { flex: 1; height: 3px; background: #e1e8ef; align-self: center; margin: 0 10px; }
    .step-line.active { background: #003366; }
    """

    header = header.replace("</head>", f"<style>{base_css}\n{extra_css}</style>\n</head>")

    # Add Hero Video to Page
    hero_video = f"""
    <section class="form-hero">
        <video autoplay muted loop playsinline>
            <source src="video.mp4" type="video/mp4">
        </video>
        <div class="form-hero-content" data-aos="fade-down">
            <h1>{title}</h1>
            <div style="width: 60px; height: 4px; background: #f5c518; margin: 0 auto 20px;"></div>
            <p>Start your journey with Kingston Engineering College today.</p>
        </div>
    </section>
    """

    # Assemble final HTML
    final_html = header + f"\n{hero_video}\n<main class='form-container-wrap'>\n{form_html}\n</main>\n" + footer
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)

# --- Contents for Forms ---

# 1. Admission Enquiry
enquiry_html = """
<div class="container">
    <div class="row" style="display: flex; gap: 40px; align-items: flex-start;">
        <div style="flex: 2;">
            <div class="glass-form-card" data-aos="fade-right">
                <h2 style="color: #003366; margin-bottom: 30px; font-weight: 800;">Get in Touch</h2>
                <form id="enquiryForm" action="#" method="POST">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>Full Name *</label>
                            <input type="text" class="form-control" placeholder="Enter your full name" required>
                        </div>
                        <div class="form-group">
                            <label>Email Address *</label>
                            <input type="email" class="form-control" placeholder="Enter your email" required>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>Phone Number *</label>
                            <input type="tel" class="form-control" placeholder="Your contact number" required>
                        </div>
                        <div class="form-group">
                            <label>Course Interested In *</label>
                            <select class="form-control" required>
                                <option value="">Select a Course</option>
                                <option>B.E. Computer Science and Engineering</option>
                                <option>B.E. AI & ML</option>
                                <option>B.Tech Information Technology</option>
                                <option>B.E. Electronics & Communication</option>
                                <option>B.Arch</option>
                                <option>MBA</option>
                            </select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Your Message / Query</label>
                        <textarea class="form-control" rows="4" placeholder="Tell us what you'd like to know"></textarea>
                    </div>
                    <button type="submit" class="btn-submit">Send Enquiry</button>
                </form>
            </div>
        </div>
        <div style="flex: 1;" data-aos="fade-left">
            <div style="background: #003366; color: #fff; padding: 40px; border-radius: 20px;">
                <h3 style="color: #f5c518; margin-bottom: 25px;">Why Kingston?</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 20px;"><i class="fa-solid fa-trophy" style="margin-right: 15px; color: #f5c518;"></i> 95% Placement Record</li>
                    <li style="margin-bottom: 20px;"><i class="fa-solid fa-flask" style="margin-right: 15px; color: #f5c518;"></i> AICTE Idea Lab</li>
                    <li style="margin-bottom: 20px;"><i class="fa-solid fa-graduation-cap" style="margin-right: 15px; color: #f5c518;"></i> Autonomous Institution</li>
                    <li style="margin-bottom: 20px;"><i class="fa-solid fa-users" style="margin-right: 15px; color: #f5c518;"></i> Expert Faculty</li>
                </ul>
                <div style="margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px;">
                    <p style="font-size: 0.9rem; opacity: 0.8;">Need immediate help? Call us:</p>
                    <h4 style="color: #f5c518; font-size: 1.3rem;">+91 75400 37999</h4>
                </div>
            </div>
        </div>
    </div>
</div>
"""

# 2. Apply Now (Multi-step)
apply_html = """
<div class="container">
    <div style="max-width: 900px; margin: 0 auto;">
        <div class="glass-form-card" data-aos="zoom-in">
            <div class="step-indicator">
                <div class="step active" id="step1">1</div>
                <div class="step-line active"></div>
                <div class="step" id="step2">2</div>
                <div class="step-line" id="line2"></div>
                <div class="step" id="step3">3</div>
            </div>

            <form id="applyForm">
                <!-- Step 1: Personal Details -->
                <div id="step-panel-1">
                    <h2 style="color: #003366; margin-bottom: 30px; font-weight: 800;">Personal Information</h2>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>First Name</label>
                            <input type="text" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label>Last Name</label>
                            <input type="text" class="form-control" required>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>Date of Birth</label>
                            <input type="date" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label>Gender</label>
                            <select class="form-control" required>
                                <option>Male</option>
                                <option>Female</option>
                                <option>Other</option>
                            </select>
                        </div>
                    </div>
                    <button type="button" class="btn-submit" onclick="nextStep(2)">Next Step &rarr;</button>
                </div>

                <!-- Step 2: Academics -->
                <div id="step-panel-2" style="display: none;">
                    <h2 style="color: #003366; margin-bottom: 30px; font-weight: 800;">Academic Background</h2>
                    <div class="form-group">
                        <label>School / College Name (Last Attended)</label>
                        <input type="text" class="form-control" required>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div class="form-group">
                            <label>12th Mark (Percentage)</label>
                            <input type="number" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label>Community</label>
                            <select class="form-control">
                                <option>OC</option>
                                <option>BC</option>
                                <option>MBC</option>
                                <option>SC/ST</option>
                            </select>
                        </div>
                    </div>
                    <div style="display: flex; gap: 15px;">
                        <button type="button" class="btn-submit" style="background: #777;" onclick="nextStep(1)">&larr; Back</button>
                        <button type="button" class="btn-submit" onclick="nextStep(3)">Next Step &rarr;</button>
                    </div>
                </div>

                <!-- Step 3: Course Selection -->
                <div id="step-panel-3" style="display: none;">
                    <h2 style="color: #003366; margin-bottom: 30px; font-weight: 800;">Program Selection</h2>
                    <div class="form-group">
                        <label>Select Category</label>
                        <select class="form-control" required>
                            <option>Undergraduate (U.G)</option>
                            <option>Postgraduate (P.G)</option>
                            <option>Architecture</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Course Priority 1</label>
                        <select class="form-control" required>
                            <option>B.E. Computer Science and Engineering</option>
                            <option>B.E. Artificial Intelligence & Data Science</option>
                            <option>B.Tech Information Technology</option>
                        </select>
                    </div>
                    <div style="display: flex; gap: 15px;">
                        <button type="button" class="btn-submit" style="background: #777;" onclick="nextStep(2)">&larr; Back</button>
                        <button type="submit" class="btn-submit" style="background: #27ae60;">Submit Application</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>

<script>
    function nextStep(step) {
        // Hide all panels
        document.getElementById('step-panel-1').style.display = 'none';
        document.getElementById('step-panel-2').style.display = 'none';
        document.getElementById('step-panel-3').style.display = 'none';
        
        // Show target panel
        document.getElementById('step-panel-' + step).style.display = 'block';
        
        // Update indicators
        const steps = [1, 2, 3];
        steps.forEach(s => {
            const el = document.getElementById('step' + s);
            if(s < step) el.className = 'step completed';
            else if(s == step) el.className = 'step active';
            else el.className = 'step';
        });

        // Update lines
        if(step > 1) document.querySelector('.step-line').className = 'step-line active';
        else document.querySelector('.step-line').className = 'step-line';
        
        if(step > 2) document.getElementById('line2').className = 'step-line active';
        else if(document.getElementById('line2')) document.getElementById('line2').className = 'step-line';
    }
</script>
"""

if __name__ == "__main__":
    generate_form_page("admission_enquiry.html", "Admission Enquiry", enquiry_html)
    generate_form_page("apply_now.html", "Apply Now", apply_html)
