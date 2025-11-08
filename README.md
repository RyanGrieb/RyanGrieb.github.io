# Ryan Grieb - IT Professional Portfolio

A professional GitHub Pages portfolio showcasing IT, helpdesk, and DevOps expertise. This portfolio emphasizes automation capabilities, technical documentation, and hands-on infrastructure experience.

## 🎯 Purpose

This portfolio is designed to:
- Highlight IT support and technical troubleshooting skills
- Showcase automation tools and DevOps capabilities
- Demonstrate technical documentation abilities
- Position for IT, helpdesk, and DevOps roles

## 🚀 Quick Start - Deploying to GitHub Pages

### Method 1: Direct Upload (Easiest)

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it: `yourusername.github.io` (replace `yourusername` with your actual GitHub username)
   - Make it Public
   - Don't initialize with README (we're uploading files)
   - Click "Create repository"

2. **Upload these files:**
   - Click "uploading an existing file" on the Quick setup page
   - Drag and drop ALL files from this folder
   - Commit the files

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Under "Source", select "main" branch
   - Click Save
   - Your site will be live at: `https://yourusername.github.io`

### Method 2: Using Git (Recommended)

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial portfolio commit"

# Add your GitHub repository as remote
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then enable GitHub Pages in repository settings as described above.

## 📝 Customization Guide

### 1. Update Personal Information

**In `index.html`:**
- Line 49-51: Update hero title and subtitle
- Line 184-194: Update contact information
- Line 190: Replace `yourusername` with your actual GitHub username

**In `documentation.html`:**
- Line 16-20: Update navigation links if needed

### 2. Add Your GitHub Username

Replace all instances of `yourusername` with your actual GitHub username:
- `index.html` (line 190)
- Any other files referencing your GitHub profile

### 3. Hide or Archive OpenCiv Project

To make OpenCiv less visible on your profile:

**Option A - Archive it:**
1. Go to your OpenCiv repository
2. Settings → Scroll to bottom
3. Click "Archive this repository"

**Option B - Make it private:**
1. Go to your OpenCiv repository  
2. Settings → Scroll to "Danger Zone"
3. Click "Change visibility" → "Make private"

**Option C - Add .github-private topic:**
1. Go to your OpenCiv repository
2. Click the gear icon next to "About"
3. Add topic: `personal-project` or `archived`
4. This helps categorize it as a side project

### 4. Adding Your Documentation

You have your own `.md` documentation files. Here's how to add them:

**Option A - Convert Markdown to HTML (Recommended):**

1. For each `.md` file, create a new HTML file in the `/docs` folder
2. Use `/docs/network-troubleshooting.html` as a template
3. Copy the structure and paste your content into the body
4. Update the navigation and title

**Option B - Use a Markdown Renderer:**

Add this to any page to render markdown:
```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
    // Load and render your .md file
    fetch('your-file.md')
        .then(response => response.text())
        .then(text => {
            document.getElementById('content').innerHTML = marked.parse(text);
        });
</script>
```

**Option C - Link to GitHub Files:**

If you want to keep your docs as `.md` on GitHub:
```html
<a href="https://github.com/yourusername/yourusername.github.io/blob/main/docs/your-doc.md">
    View Documentation →
</a>
```

### 5. Update Documentation Cards

In `documentation.html`, update the documentation cards (lines 35-125) to match your actual documentation:

```html
<div class="doc-card">
    <div class="doc-icon">🔧</div>
    <h3>Your Documentation Title</h3>
    <p class="doc-category">Category</p>
    <p class="doc-description">Brief description</p>
    <div class="doc-tags">
        <span class="tag-small">Tag1</span>
        <span class="tag-small">Tag2</span>
    </div>
    <a href="docs/your-doc.html" class="doc-link">View Documentation →</a>
</div>
```

## 📂 File Structure

```
portfolio/
├── index.html              # Main landing page
├── documentation.html      # Documentation showcase page
├── styles.css             # All styling
├── script.js              # Interactive features
├── docs/                  # Documentation pages folder
│   └── network-troubleshooting.html  # Template/example doc
└── README.md              # This file
```

## 🎨 Customizing Colors

To change the color scheme, edit the CSS variables in `styles.css` (lines 8-18):

```css
:root {
    --primary-color: #2563eb;     /* Main blue color */
    --primary-dark: #1e40af;      /* Darker blue */
    --accent-color: #0ea5e9;      /* Light blue accent */
    /* ... other colors ... */
}
```

## ✨ Features

- **Responsive Design:** Works on desktop, tablet, and mobile
- **Smooth Animations:** Fade-in effects as you scroll
- **Professional Layout:** Clean, modern design for IT professionals
- **Documentation Showcase:** Dedicated page for your technical writing
- **SEO Optimized:** Meta tags for better search visibility
- **Fast Loading:** Minimal dependencies, pure HTML/CSS/JS

## 🔧 Highlighting Automation Skills

The portfolio emphasizes your automation work without showing proprietary code:

**On Homepage:**
- "Key Achievement" box highlighting your Python automation tool
- Dedicated "Automation & Projects" section
- DevOps skills prominently displayed

**What NOT to do:**
- Don't upload actual code from Texas Techs (proprietary)
- Don't include customer data or internal systems details
- Don't share company-specific scripts

**What TO do:**
- Describe the impact and results of your automation
- Create sanitized example scripts that demonstrate your skills
- Show the technologies used without revealing business logic

## 📊 Adding Projects/Automation Examples

To add a new project card in the "Automation & Projects" section:

```html
<div class="project-card">
    <h3>Project Name</h3>
    <p class="project-tech">Technologies Used</p>
    <p>Brief description of the project and its impact</p>
    <ul>
        <li>Key achievement or metric</li>
        <li>Another achievement</li>
    </ul>
</div>
```

## 🎯 Optimization Tips for Job Search

1. **Update GitHub Profile README:**
   Create a `README.md` in a repo named after your username (e.g., `ryangrieb/ryangrieb`)
   
2. **Pin Relevant Repositories:**
   Pin 3-6 repositories that showcase IT/automation skills, hide gaming projects

3. **Add Keywords:**
   Include relevant keywords in your repo descriptions:
   - "IT automation"
   - "Python scripts"
   - "Network troubleshooting"
   - "DevOps tools"
   - "Technical documentation"

4. **Keep Activity Current:**
   - Commit documentation regularly
   - Update your portfolio with new skills
   - Contribute to IT-related open source projects

5. **LinkedIn Integration:**
   Add your portfolio link to your LinkedIn:
   - Profile headline
   - Featured section
   - Experience descriptions

## 🐛 Troubleshooting

**Site not loading?**
- Wait 5-10 minutes after first deployment
- Check Settings → Pages shows the green success message
- Verify branch is set to "main" (not "master")

**Changes not appearing?**
- GitHub Pages can take 1-2 minutes to update
- Hard refresh your browser (Ctrl+Shift+R / Cmd+Shift+R)
- Check you committed and pushed all changes

**Styling broken?**
- Verify all files are in the root directory (not in a subfolder)
- Check that `styles.css` path in HTML matches file location

## 📞 Support

If you need help deploying or customizing:
- GitHub Pages Documentation: https://docs.github.com/en/pages
- HTML/CSS Resources: https://developer.mozilla.org/

## 📄 License

Feel free to use this template for your own portfolio. No attribution required.

---

**Ready to deploy?** Follow the Quick Start guide above and you'll have your portfolio live in under 10 minutes!
