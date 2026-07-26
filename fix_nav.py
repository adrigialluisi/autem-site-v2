with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix nav alignment on ultrawide (1441px+)
css = css.replace(
    "@media (min-width: 1441px) {\n  .container { max-width: 1400px; }\n  .hero-inner { padding: 0 40px; max-width: 1400px; }\n}",
    "@media (min-width: 1441px) {\n  .container { max-width: 1400px; }\n  .hero-inner { padding: 0 40px; max-width: 1400px; }\n  .nav-inner { padding: 0 40px; max-width: 1400px; }\n}"
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied nav ultrawide fix")
