import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace transform: translateY(48px) with relative positioning
css = css.replace(
    ".midia-card:nth-child(even) { transform: translateY(48px); }",
    ".midia-card:nth-child(even) { position: relative; top: 48px; }"
)

# And for the mobile reset
css = css.replace(
    ".midia-card:nth-child(even) { transform: translateY(0); }",
    ".midia-card:nth-child(even) { position: static; top: auto; }"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed hover bug by using relative positioning instead of transform")
