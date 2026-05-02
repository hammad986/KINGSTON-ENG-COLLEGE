import os

def split():
    with open('dept_csbs.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split for CSBS Subpages
    main_start_tag = '<main class="dept-main-content">'
    split_pt = content.find(main_start_tag)
    if split_pt == -1:
        print("Could not find main start tag")
        return
    
    header = content[:split_pt + len(main_start_tag)]
    
    main_end_tag = '</main>'
    footer_pt = content.find(main_end_tag)
    if footer_pt == -1:
        print("Could not find main end tag")
        return
        
    footer = content[footer_pt:]
    
    with open('csbs_header.txt', 'w', encoding='utf-8') as f:
        f.write(header)
    with open('csbs_footer.txt', 'w', encoding='utf-8') as f:
        f.write(footer)
    print("Files created: csbs_header.txt, csbs_footer.txt")

if __name__ == "__main__":
    split()
