#!/bin/bash
# blog_fix.sh

FILES=("blog-post-1.html" "blog-post-2.html" "blog-post-3.html" "blog-post-4.html" "blog-post-5.html" "blog-post-6.html")

for f in "${FILES[@]}"; do
    echo "Processing $f..."
    
    # 1. Strip the mess: Remove everything between post-content and </article>
    # Then we will re-insert the correct navigation block.
    
    # Actually, let's just use a Python script for precise multiline replacement.
    python3 - <<EOF
import sys
import re

path = "$f"
with open(path, 'r') as file:
    content = file.read()

# Pattern to find the navigation block regardless of the mess
# We look for the start of the navigation links and remove that whole block
nav_pattern = re.compile(r'(<nav class="further-reading"|<footer class="post-footer">).*?(</nav>|</footer>)', re.DOTALL)
content = nav_pattern.sub('', content)

# Clean up any stray closing tags that sed might have left
content = content.replace('            </footer>', '')
content = content.replace('        </section>', '</section>')

# Define the navigation blocks for each page
nav_blocks = {
    "blog-post-1.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-2.html" class="further-reading-link" rel="next">
                        <span class="nav-label">Next</span>
                        <span class="nav-title">A Week of AI-Powered Prototyping: Four Projects, One Goal</span>
                    </a>
                </nav>
            </footer>""",
    "blog-post-2.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-1.html" class="further-reading-link" rel="prev">
                        <span class="nav-label">Previous</span>
                        <span class="nav-title">How an AI Assistant Helped Build This Website</span>
                    </a>
                    <a href="blog-post-3.html" class="further-reading-link" rel="next">
                        <span class="nav-label">Next</span>
                        <span class="nav-title">The Quest for Free LLMs: An Experiment Log</span>
                    </a>
                </nav>
            </footer>""",
    "blog-post-3.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-2.html" class="further-reading-link" rel="prev">
                        <span class="nav-label">Previous</span>
                        <span class="nav-title">A Week of AI-Powered Prototyping: Four Projects, One Goal</span>
                    </a>
                    <a href="blog-post-4.html" class="further-reading-link" rel="next">
                        <span class="nav-label">Next</span>
                        <span class="nav-title">Connecting Worlds: Browser Control on a Mac Node</span>
                    </a>
                </nav>
            </footer>""",
    "blog-post-4.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-3.html" class="further-reading-link" rel="prev">
                        <span class="nav-label">Previous</span>
                        <span class="nav-title">The Quest for Free LLMs: An Experiment Log</span>
                    </a>
                    <a href="blog-post-5.html" class="further-reading-link" rel="next">
                        <span class="nav-label">Next</span>
                        <span class="nav-title">Going Public: Launching Redbeard Solutions on GitHub Pages</span>
                    </a>
                </nav>
            </footer>""",
    "blog-post-5.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-4.html" class="further-reading-link" rel="prev">
                        <span class="nav-label">Previous</span>
                        <span class="nav-title">Connecting Worlds: Browser Control on a Mac Node from a Linux VM</span>
                    </a>
                    <a href="blog-post-6.html" class="further-reading-link" rel="next">
                        <span class="nav-label">Next</span>
                        <span class="nav-title">Refining the User Experience: Consistent Navigation and Semantic HTML</span>
                    </a>
                </nav>
            </footer>""",
    "blog-post-6.html": """
            <footer class="post-footer">
                <nav class="further-reading" aria-label="Blog post navigation">
                    <a href="blog-post-5.html" class="further-reading-link" rel="prev">
                        <span class="nav-label">Previous</span>
                        <span class="nav-title">Going Public: Launching Redbeard Solutions on GitHub Pages</span>
                    </a>
                </nav>
            </footer>"""
}

# Re-insert the block before the closing article tag
new_block = nav_blocks.get(path, "")
content = content.replace('</article>', new_block + '\n        </article>')

with open(path, 'w') as file:
    file.write(content)
EOF
done
