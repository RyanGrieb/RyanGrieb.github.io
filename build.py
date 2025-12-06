#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Paths
ROOT = Path(__file__).parent
SRC = ROOT / "src"
BUILD = ROOT / "build"
STATIC = SRC / "static"


def clean_build():
    """Remove and recreate build directory"""
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir()
    (BUILD / "css").mkdir(parents=True, exist_ok=True)


def build_html():
    """Render Jinja2 templates"""
    env = Environment(loader=FileSystemLoader(SRC / "templates"))

    # Main page templates
    templates = ["index.html", "all-projects.html", "documentation.html"]

    for template_name in templates:
        try:
            template = env.get_template(template_name)
            html = template.render()
            output_path = BUILD / template_name
            output_path.write_text(html)
            print(f"✓ Built {output_path}")
        except Exception as e:
            print(f"✗ Failed to build {template_name}: {e}")

    # Documentation page templates
    doc_templates = ["active-directory.html", "network-troubleshooting.html"]
    (BUILD / "docs").mkdir(parents=True, exist_ok=True)

    for doc_template in doc_templates:
        try:
            template = env.get_template(f"docs/{doc_template}")
            html = template.render()
            output_path = BUILD / "docs" / doc_template
            output_path.write_text(html)
            print(f"✓ Built {output_path}")
        except Exception as e:
            print(f"✗ Failed to build docs/{doc_template}: {e}")


def copy_static():
    """Copy static assets"""
    if STATIC.exists():
        shutil.copytree(STATIC, BUILD / "static", dirs_exist_ok=True)
        print(f"✓ Copied static assets")

    # Copy JS files
    if (SRC / "js").exists():
        shutil.copytree(SRC / "js", BUILD / "js", dirs_exist_ok=True)
        print(f"✓ Copied js/")

    # Copy favicon
    if (ROOT / "favicon.ico").exists():
        shutil.copy2(ROOT / "favicon.ico", BUILD / "favicon.ico")
        print(f"✓ Copied favicon.ico")


def generate_css():
    """Build Tailwind CSS"""
    print("Building CSS with Tailwind...")
    result = os.system(
        "npx tailwindcss -i src/css/tailwind.css -o build/css/styles.css --minify"
    )
    if result == 0:
        print("✓ Generated CSS")
    else:
        print("✗ CSS generation failed")


if __name__ == "__main__":
    print("🔨 Building portfolio...")
    clean_build()
    build_html()
    copy_static()
    generate_css()
    print("✅ Build complete! Check the build/ directory")
