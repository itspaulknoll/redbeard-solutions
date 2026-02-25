#!/usr/bin/python3
import os
import re

FILES = ["blog-post-1.html", "blog-post-2.html", "blog-post-3.html", "blog-post-4.html", "blog-post-5.html", "blog-post-6.html"]

NAV_BLOCKS = {
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

def fix_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return

    with open(filename, 'r') as f:
        content = f.read()

    # 1. Fix the site header (nav/ul nesting)
    content = re.sub(r'<ul>(.*?)</ul>\s*</header>', r'<ul>\1</ul>\n        </nav>\n    </header>', content, flags=re.DOTALL)
    content = re.sub(r'<ul>(.*?)</ul>\s*</footer>\s*</header>', r'<ul>\1</ul>\n        </nav>\n    </header>', content, flags=re.DOTALL)

    # 2. Extract parts of the file to rebuild it
    # Find header and start of article
    match = re.search(r'(<!DOCTYPE html>.*?<article class="blog-post">)', content, flags=re.DOTALL)
    if not match:
        print(f"Could not find article start in {filename}")
        return
    prefix = match.group(1)

    # Find the post header (title/date)
    match = re.search(r'(<header>.*?</header>)', content[len(prefix):], flags=re.DOTALL)
    if not match:
        print(f"Could not find post header in {filename}")
        return
    post_header = match.group(1)

    # Find the post content start
    match = re.search(r'(<section class="post-content">)', content, flags=re.DOTALL)
    if not match:
        print(f"Could not find post content start in {filename}")
        return
    section_start = match.group(1)

    # Find the end of content (before nav links/mess starts)
    # We'll look for the last paragraph before any <footer> or <nav> mess
    # A safer way: find everything between section_start and the end of the article
    article_end_match = re.search(r'</article>', content, flags=re.DOTALL)
    if not article_end_match:
        print(f"Could not find article end in {filename}")
        return
    
    body_mess = content[content.find(section_start) + len(section_start) : article_end_match.start()]
    # Remove the mess from body_mess
    body_clean = re.sub(r'(<footer|<nav|<a class="further-reading).*$', '', body_mess, flags=re.DOTALL | re.MULTILINE).strip()
    # Also clean stray </a> tags or labels
    body_clean = re.sub(r'</a>\s*</a>', '', body_clean)
    body_clean = re.sub(r'<span class="nav-label">.*</span>', '', body_clean)
    body_clean = re.sub(r'</section>', '', body_clean)

    # 3. Rebuild the file
    new_nav = NAV_BLOCKS[filename]
    
    new_content = f"""{prefix}
            {post_header}
            <section class="post-content">
                {body_clean}
            </section>
{new_nav}
        </article>
    </main>

    <footer>
        <p>&copy; 2026 Redbeard Solutions. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

    # Cleanup any double sections or article tags
    new_content = re.sub(r'\n\s*\n', '\n', new_content)

    with open(filename, 'w') as f:
        f.write(new_content)
    print(f"Successfully rebuilt {filename}")

for f in FILES:
    fix_file(f)
