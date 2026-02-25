#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

READER_LINKS = {
    "blog-post-1.html": '<p><strong>Next:</strong> <a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p>',
    "blog-post-2.html": '<p><strong>Previous:</strong> <a href="blog-post-1.html">How an AI Assistant Helped Build This Website</a></p><p><strong>Next:</strong> <a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p>',
    "blog-post-3.html": '<p><strong>Previous:</strong> <a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p><p><strong>Next:</strong> <a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node</a></p>',
    "blog-post-4.html": '<p><strong>Previous:</strong> <a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p><p><strong>Next:</strong> <a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p>',
    "blog-post-5.html": '<p><strong>Previous:</strong> <a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node from a Linux VM</a></p><p><strong>Next:</strong> <a href="blog-post-6.html">Refining the User Experience: Consistent Navigation and Semantic HTML</a></p>',
    "blog-post-6.html": '<p><strong>Previous:</strong> <a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p>'
}

def fix_for_reader(filename):
    with open(filename, 'r') as f:
        content = f.read()

    links = READER_LINKS[filename]
    reader_block = f'\n                <div class="reader-navigation-links">\n                    <hr>\n                    {links}\n                </div>'
    
    # Insert inside the post-content section, right before it ends
    content = content.replace('</section>', f'{reader_block}\n            </section>')
    
    with open(filename, 'w') as f:
        f.write(content)

for f in FILES:
    fix_for_reader(f)
