import glob
import re
import os

files = glob.glob('about/*.html')
pattern = re.compile(r'\s*<!-- Hero Swiper Carousel -->.*?</div>\s*</div>\s*(?=</section>)', re.DOTALL)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<!-- Hero Swiper Carousel -->' in content:
        # Simplest string replacement based on exact markers.
        # Find start
        start = content.find('<!-- Hero Swiper Carousel -->')
        # Find </section> after start
        end = content.find('</section>', start)
        if start != -1 and end != -1:
            # Reconstruct content
            # We want to remove from start to just before the </section>
            # Actually, to leave space, let's keep one newline.
            new_content = content[:start] + "\n    " + content[end:]
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print('Updated', f)

print('Total updated:', count)
