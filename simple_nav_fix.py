#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

NAV_LINKS = {
    "blog-post-1.html": '<a href="blog-post-2.html" class="view-post-link">Next Article</a>',
    "blog-post-2.html": '<a href="blog-post-1.html" class="view-post-link">Previous Article</a> | <a href="blog-post-3.html" class="view-post-link">Next Article</a>',
    "blog-post-3.html": '<a href="blog-post-2.html" class="view-post-link">Previous Article</a> | <a href="blog-post-4.html" class="view-post-link">Next Article</a>',
    "blog-post-4.html": '<a href="blog-post-3.html" class="view-post-link">Previous Article</a> | <a href="blog-post-5.html" class="view-post-link">Next Article</a>',
    "blog-post-5.html": '<a href="blog-post-4.html" class="view-post-link">Previous Article</a> | <a href="blog-post-6.html" class="view-post-link">Next Article</a>',
    "blog-post-6.html": '<a href="blog-post-5.html" class="view-post-link">Previous Article</a>'
}

def fix_individual_post(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Remove the failed hidden reader block
    content = re.sub(r'\s*<div class="reader-navigation-links">.*?</div>', '', content, flags=re.DOTALL)
    
    # 2. Add the "View Article" style links at the very end of the content section
    # Use the same class name that works on the index page
    links = NAV_LINKS[filename]
    link_block = f'\n                <div class="post-navigation-simple">\n                    <hr>\n                    {links}\n                </div>'
    
    content = content.replace('</section>', f'{link_block}\n            </section>')
    
    with open(filename, 'w') as f:
        f.write(content)

for f in FILES:
    fix_individual_post(f)
print("Finished adding simple navigation links to individual posts.")
