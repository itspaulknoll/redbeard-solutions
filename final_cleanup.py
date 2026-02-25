#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

def final_cleanup(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Remove the stray </a> tag if it exists
    content = content.replace('</a>\n            \n            <section class="post-navigation-reader-safe">', '\n            <section class="post-navigation-reader-safe">')
    
    # 2. Fix the nested sections (ensure post-content closes before post-navigation starts)
    if '<section class="post-content">' in content and '<section class="post-navigation-reader-safe">' in content:
        # Find start of navigation
        nav_start = content.find('<section class="post-navigation-reader-safe">')
        # Find the end of post-content that should be right before it
        # We'll just rebuild that junction
        parts = content.split('<section class="post-navigation-reader-safe">')
        if len(parts) == 2:
            left = parts[0].strip()
            # Ensure left ends with </section>
            if not left.endswith('</section>'):
                # Try to find a stray </section> earlier and move it here
                left = re.sub(r'</section>\s*$', '', left)
                left += '\n            </section>'
            content = left + '\n            <section class="post-navigation-reader-safe">' + parts[1]

    # 3. Final article closing check
    content = re.sub(r'</section>\s*</section>\s*</article>', '</section>\n        </article>', content)

    with open(filename, 'w') as f:
        f.write(content)

for f in FILES:
    final_cleanup(f)
print("Finished final cleanup of blog HTML nesting.")
