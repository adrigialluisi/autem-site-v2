import os
import re

html_files = ['index.html', 'blog.html', 'quem-somos.html', 'time.html']

# 1. Update stroke-width in all HTML files
for file in html_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace stroke-width="anything" with stroke-width="0.5"
        # Also handle cases where stroke-width is inside a style attribute (unlikely here but safe)
        content = re.sub(r'stroke-width="[^"]+"', 'stroke-width="0.5"', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated stroke-width in {file}")


# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix blue bar on mobile by removing padding from the unified 768px .hero block
# Original unified: .hero { padding: 100px 0 40px; min-height: auto; }
css = css.replace('.hero { padding: 100px 0 40px; min-height: auto; }', '.hero { padding: 0; min-height: 0; }')

# Fix font sizes on mobile
# In the older mobile block: .hero h1 { font-size: 36px !important; letter-spacing: -1.5px !important; }
css = css.replace('.hero h1 { font-size: 36px !important; letter-spacing: -1.5px !important; }', '.hero h1 { font-size: clamp(36px, 9vw, 44px); letter-spacing: -1.5px; line-height: 1.1; }')
# In unified 768px: .hero h1 { font-size: clamp(32px, 8vw, 48px); }
css = css.replace('.hero h1 { font-size: clamp(32px, 8vw, 48px); }', '.hero h1 { font-size: clamp(36px, 9vw, 44px); }')

# Section titles were small:
# .section-title { font-size: clamp(28px, 7vw, 36px); } -> clamp(32px, 9vw, 42px)
css = css.replace('.section-title { font-size: clamp(28px, 7vw, 36px); }', '.section-title { font-size: clamp(32px, 9vw, 42px); }\n  .section-sub { font-size: 17px; }')
css = css.replace('.hero-sub { margin: 0 auto; }', '.hero-sub { margin: 0 auto; font-size: 18px; }')

# Fix numbers section 2x2 grid on mobile (480px block)
old_480_numeros = """.numeros-grid { grid-template-columns: 1fr; }
  .numero-item { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.08); }
  .numero-item:last-child { border-bottom: none; }"""
new_480_numeros = """.numeros-grid { grid-template-columns: repeat(2, 1fr); }
  .numero-item { padding: 24px 16px; border-bottom: 1px solid rgba(255,255,255,0.08); border-right: 1px solid rgba(255,255,255,0.08); }
  .numero-item:nth-child(even) { border-right: none; }
  .numero-item:nth-child(n+3) { border-bottom: none; }"""
css = css.replace(old_480_numeros, new_480_numeros)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
