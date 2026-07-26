with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix hero alignment on ultrawide (1441px+)
# Add .hero-inner { max-width: 1400px; } inside the 1441px breakpoint
css = css.replace(
    ".hero-inner { padding: 0 40px; }",
    ".hero-inner { padding: 0 40px; max-width: 1400px; }"
)

# 2. Fix hero scroll indicator closer to the bottom
css = css.replace(
    "bottom: 16px;",
    "bottom: 4px;"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated hero alignment and scroll indicator")
