import glob

files = glob.glob('about/*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if there is an unclosed hero-college-brand or missing hero-brand-text
    # Since different files may have slight whitespace variations from manual editing,
    # let's look for the logo part, then just dynamically restore it.
    start_tag = '<div class="hero-college-brand">'
    end_tag = '</section>'
    
    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find(end_tag, start_idx)
        
        # Determine replacing string
        replacement = """<div class="hero-college-brand">
                <img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/A_Greek_Temple_Icon.svg"
                    class="hero-logo-medium" onerror="this.style.display='none'">
            </div>
            <div class="hero-admission-title-wrap">
                <h1 class="hero-admission-year" data-aos="fade-up" data-aos-delay="300" style="color:white; font-size: 2.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">ABOUT US</h1>
            </div>
        </div>
    """
        
        # We only want to replace if the hero isn't already well-formed
        # we check if it has "ABOUT US"
        if "hero-brand-text" not in content[start_idx:end_idx]:
            new_content = content[:start_idx] + replacement + content[end_idx:]
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print(f'Fixed {f}')
            
print(f'Total fixed: {count}')
