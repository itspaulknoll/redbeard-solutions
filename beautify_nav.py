#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

# Wrapper for each nav link to allow side-by-side styling
NAV_CONTENT = {
    "blog-post-1.html": '<div class="nav-group"></div><div class="nav-group" style="text-align: right;"><h2>Next Article</h2><p><a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p></div>',
    "blog-post-2.html": '<div class="nav-group"><h2>Previous Article</h2><p><a href="blog-post-1.html">How an AI Assistant Helped Build This Website</a></p></div><div class="nav-group" style="text-align: right;"><h2>Next Article</h2><p><a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p></div>',
    "blog-post-3.html": '<div class="nav-group"><h2>Previous Article</h2><p><a href="blog-post-2.html">A Week of AI-Powered Prototyping: Four Projects, One Goal</a></p></div><div class="nav-group" style="text-align: right;"><h2>Next Article</h2><p><a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node</a></p></div>',
    "blog-post-4.html": '<div class="nav-group"><h2>Previous Article</h2><p><a href="blog-post-3.html">The Quest for Free LLMs: An Experiment Log</a></p></div><div class="nav-group" style="text-align: right;"><h2>Next Article</h2><p><a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p></div>',
    "blog-post-5.html": '<div class="nav-group"><h2>Previous Article</h2><p><a href="blog-post-4.html">Connecting Worlds: Browser Control on a Mac Node from a Linux VM</a></p></div><div class="nav-group" style="text-align: right;"><h2>Next Article</h2><p><a href="blog-post-6.html">Refining the User Experience: Consistent Navigation and Semantic HTML</a></p></div>',
    "blog-post-6.html": '<div class="nav-group"><h2>Previous Article</h2><p><a href="blog-post-5.html">Going Public: Launching Redbeard Solutions on GitHub Pages</a></p></div><div class="nav-group"></div>'
}

def beautify_nav(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find the nav safe block and replace its content
    pattern = re.compile(r'<section class="post-navigation-reader-safe">.*?</section>', re.DOTALL)
    new_block = f'<section class="post-navigation-reader-safe">{NAV_CONTENT[filename]}</section>'
    
    content = pattern.sub(new_block, content)
    
    with open(filename, 'w') as f:
        f.write(content)

for f in FILES:
    beautify_nav(f)
print("Finished beautifying individual blog post navigation.")
