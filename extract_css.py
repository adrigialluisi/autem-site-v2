import os
import re

html_files = ['index.html', 'blog.html', 'quem-somos.html', 'time.html']

# 1. Extract CSS from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
if match:
    css_content = match.group(1).strip()
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Replace <style> blocks in all files with <link rel="stylesheet" href="style.css">
for file in html_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We replace the <style>...</style> block
        new_content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css">', content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
