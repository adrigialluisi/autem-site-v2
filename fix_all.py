with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix hero alignment on ultrawide (1441px+)
css = css.replace(
    ".hero-inner { padding: 0 40px; }",
    ".hero-inner { padding: 0 40px; max-width: 1400px; }"
)

# 2. Fix hero scroll indicator closer to the bottom
css = css.replace(
    "bottom: 16px;",
    "bottom: 4px;"
)

# 3. Fix hero-content max-width so it wraps better on desktop, keeping it left-aligned
css = css.replace(
    ".hero-content { max-width: 560px; display: flex; flex-direction: column; gap: 28px; }",
    ".hero-content { max-width: 680px; display: flex; flex-direction: column; gap: 28px; }"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied fixes correctly")
