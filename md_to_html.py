#!/usr/bin/env python3
"""
Markdown to HTML Documentation Converter
Converts your .md files into styled HTML documentation pages for your portfolio

Usage:
    python md_to_html.py your-document.md

This will create: docs/your-document.html
"""

import sys
import os
import re
from datetime import datetime

def convert_md_to_html(md_file):
    """Convert a markdown file to an HTML documentation page"""
    
    # Read the markdown file
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {md_file}")
        return
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Documentation"
    
    # Generate output filename
    base_name = os.path.splitext(os.path.basename(md_file))[0]
    output_file = f"docs/{base_name}.html"
    
    # Basic markdown to HTML conversion
    html_content = md_content
    
    # Convert headers
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    
    # Convert bold and italic
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_content)
    html_content = re.sub(r'`(.+?)`', r'<code>\1</code>', html_content)
    
    # Convert lists
    html_content = re.sub(r'^\- (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    
    # Wrap consecutive list items in ul/ol tags
    html_content = re.sub(r'(<li>.*?</li>\n)+', r'<ul>\g<0></ul>\n', html_content, flags=re.DOTALL)
    
    # Convert paragraphs (lines that aren't already HTML)
    lines = html_content.split('\n')
    processed_lines = []
    for line in lines:
        if line.strip() and not line.strip().startswith('<'):
            processed_lines.append(f'<p>{line}</p>')
        else:
            processed_lines.append(line)
    html_content = '\n'.join(processed_lines)
    
    # Create the full HTML document
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Ryan Grieb</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .doc-content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }}
        
        .doc-content h1 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--text-dark);
        }}
        
        .doc-meta {{
            display: flex;
            gap: 2rem;
            margin-bottom: 2rem;
            padding-bottom: 2rem;
            border-bottom: 2px solid var(--border-color);
            font-size: 0.95rem;
            color: var(--text-light);
        }}
        
        .doc-content h2 {{
            font-size: 1.75rem;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            color: var(--text-dark);
            text-align: left;
        }}
        
        .doc-content h3 {{
            font-size: 1.35rem;
            margin-top: 2rem;
            margin-bottom: 0.75rem;
            color: var(--text-dark);
            text-align: left;
        }}
        
        .doc-content p {{
            color: var(--text-light);
            line-height: 1.8;
            margin-bottom: 1.25rem;
        }}
        
        .doc-content ul, .doc-content ol {{
            margin-bottom: 1.5rem;
            padding-left: 2rem;
        }}
        
        .doc-content li {{
            color: var(--text-light);
            margin-bottom: 0.75rem;
            line-height: 1.7;
        }}
        
        .doc-content code {{
            background-color: var(--bg-light);
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: var(--text-dark);
        }}
        
        .doc-content pre {{
            background-color: var(--text-dark);
            color: #f8fafc;
            padding: 1.5rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }}
        
        .doc-content pre code {{
            background-color: transparent;
            color: #f8fafc;
            padding: 0;
        }}
        
        .back-link {{
            display: inline-block;
            margin-bottom: 2rem;
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }}
        
        .back-link:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">Ryan Grieb</div>
            <ul class="nav-menu">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../index.html#about">About</a></li>
                <li><a href="../index.html#experience">Experience</a></li>
                <li><a href="../index.html#skills">Skills</a></li>
                <li><a href="../documentation.html" class="active">Documentation</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <div class="doc-content">
        <a href="../documentation.html" class="back-link">← Back to Documentation</a>
        
        <div class="doc-meta">
            <div><strong>Last Updated:</strong> {datetime.now().strftime('%B %Y')}</div>
        </div>

        {html_content}

        <a href="../documentation.html" class="back-link">← Back to Documentation</a>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2024 Ryan Grieb. All rights reserved.</p>
        </div>
    </footer>

    <script src="../script.js"></script>
</body>
</html>
"""
    
    # Create docs directory if it doesn't exist
    os.makedirs('docs', exist_ok=True)
    
    # Write the HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"✅ Successfully converted {md_file} to {output_file}")
    print(f"\nNext steps:")
    print(f"1. Review the generated file in a browser")
    print(f"2. Add a card for this doc in documentation.html")
    print(f"3. Commit and push to GitHub")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py your-document.md")
        sys.exit(1)
    
    md_file = sys.argv[1]
    convert_md_to_html(md_file)
