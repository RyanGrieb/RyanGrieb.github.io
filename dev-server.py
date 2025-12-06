#!/usr/bin/env python3
"""
Simple development server with hot reload - no external dependencies
"""
import os
import time
import json
import subprocess
import threading
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

class DevHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="build", **kwargs)
    
    def do_GET(self):
        if self.path.endswith('.html') or self.path == '/' or self.path == '/index.html':
            # Inject hot reload script
            try:
                if self.path == '/':
                    file_path = Path("build/index.html")
                else:
                    file_path = Path("build" + self.path)
                
                if file_path.exists():
                    content = file_path.read_text()
                    # Inject hot reload script before closing body tag
                    hot_reload_script = """
<script>
(function() {
    let lastCheck = Date.now();
    function checkForChanges() {
        fetch('/reload-check?t=' + Date.now(), {cache: 'no-cache'})
            .then(response => response.json())
            .then(data => {
                if (data.changed) {
                    console.log('🔄 Files changed, reloading...');
                    window.location.reload();
                }
            })
            .catch(() => {});
    }
    setInterval(checkForChanges, 1000);
    console.log('🔥 Hot reload enabled');
})();
</script>"""
                    
                    if '</body>' in content:
                        content = content.replace('</body>', hot_reload_script + '\n</body>')
                    else:
                        content += hot_reload_script
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Cache-Control', 'no-cache')
                    self.end_headers()
                    self.wfile.write(content.encode())
                    return
            except Exception as e:
                print(f"Error serving HTML: {e}")
        
        elif self.path.startswith('/reload-check'):
            # Check if files changed
            changed = check_for_changes()
            response = json.dumps({'changed': changed})
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            self.wfile.write(response.encode())
            return
        
        # Default behavior for other files
        super().do_GET()

# Global variables for file watching
last_build_time = 0
file_times = {}

def get_file_times():
    """Get modification times for all source files"""
    times = {}
    src_path = Path("src")
    if src_path.exists():
        for file_path in src_path.rglob("*"):
            if file_path.is_file():
                times[str(file_path)] = file_path.stat().st_mtime
    return times

def check_for_changes():
    """Check if any source files have changed"""
    global file_times, last_build_time
    
    current_times = get_file_times()
    
    # First run - initialize
    if not file_times:
        file_times = current_times
        return False
    
    # Check for changes
    for file_path, mtime in current_times.items():
        if file_path not in file_times or file_times[file_path] != mtime:
            print(f"\n🔄 File changed: {Path(file_path).name}")
            
            # Rebuild
            rebuild_site()
            
            # Update file times
            file_times = current_times
            return True
    
    return False

def rebuild_site():
    """Rebuild the site"""
    try:
        print("🔨 Rebuilding site...")
        result = subprocess.run(["python", "build.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ Site rebuilt successfully")
        else:
            print(f"❌ Build failed: {result.stderr}")
    except subprocess.TimeoutExpired:
        print("❌ Build timed out")

def main():
    print("🚀 Starting development server with hot reload...")
    
    # Initial build
    print("🔨 Initial build...")
    subprocess.run(["python", "build.py"])
    
    # Initialize file times
    global file_times
    file_times = get_file_times()
    
    # Start HTTP server
    server = HTTPServer(('localhost', 8000), DevHTTPRequestHandler)
    
    print("✅ Development server running!")
    print("📡 Server: http://localhost:8000")
    print("👀 Watching: src/ for changes")
    print("🔄 Hot reload: enabled")
    print("Press Ctrl+C to stop\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        server.shutdown()

if __name__ == "__main__":
    main()