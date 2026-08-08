import os
import glob
import re

files = glob.glob('C:/Users/kaife/Documents/ELARA/frontend/app/**/*.tsx', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'http://localhost:8000/api/v1' in content:
        # We want to replace fetch("http://localhost:8000/api/v1...") with fetch("/api/v1...")
        # But NOT window.location.href = "http://localhost:8000/api/v1/auth/google/login"
        
        # Replace only in fetch calls
        new_content = re.sub(r'fetch\([\'"`]http://localhost:8000/api/v1', r'fetch("/api/v1', content)
        new_content = re.sub(r'fetch\(`http://localhost:8000/api/v1', r'fetch(`/api/v1', new_content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file}")

print("Done fixing URLs")
