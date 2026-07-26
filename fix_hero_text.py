with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the base .hero-content rule
# Original: .hero-content { max-width: 560px; display: flex; flex-direction: column; gap: 28px; }
css = css.replace(
    ".hero-content { max-width: 560px; display: flex; flex-direction: column; gap: 28px; }",
    ".hero-content { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 28px; }"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated hero-content max-width and margin")
