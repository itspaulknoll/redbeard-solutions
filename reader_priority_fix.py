#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

NAV_LINKS = {
    "blog-post-1.html": '<h2>Next Article</h2><p><a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p>',
    "blog-post-2.html": '<h2>Previous Article</h2><p><a href="blog-post-1.html">How an AI Assistant Helped Build This Website</a></p><h2>Next Article</h2><p><a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p>',
    "blog-post-3.html": '<h2>Previous Article</h2><p><a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p><h2>Next Article</h2><p><a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node</a></p>',
    "blog-post-4.html": '<h2>Previous Article</h2><p><a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p><h2>Next Article</h2><p><a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p>',
    "blog-post-5.html": '<h2>Previous Article</h2><p><a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node from a Linux VM</a></p><h2>Next Article</h2><p><a href="blog-post-6.html">Refining the User Experience: Consistent Navigation and Semantic HTML</a></p>',
    "blog-post-6.html": '<h2>Previous Article</h2><p><a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p>'
}

def fix_reader_priority(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Clear out the previous simple_nav_fix block
    content = re.sub(r'\s*<div class="post-navigation-simple">.*?</div>', '', content, flags=re.DOTALL)
    
    # 2. Clear out the hidden post-footer completely for individual posts 
    # as it might be confusing the algorithm
    content = re.sub(r'\s*<footer class="post-footer">.*?</footer>', '', content, flags=re.DOTALL)

    # 3. Add heavy-duty semantic headers for navigation
    links = NAV_LINKS[filename]
    # We use actual <h2> tags and <p> tags - Reader Mode ALMOST ALWAYS includes headers.
    nav_block = f'\n            <section class="post-navigation-reader-safe">\n                <hr>\n                {links}\n            </section>'
    
    # Place it inside the section so it's part of the main article body
    content = content.replace('</section>', f'{nav_block}\n            </section>')
    
    with open(filename, 'w') as f:
        f.write(content)

for f in FILES:
    fix_reader_priority(f)
print("Finished adding high-priority reader headers to individual posts.")
