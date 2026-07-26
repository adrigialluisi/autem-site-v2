import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove align-items: start;
css = css.replace(
    ".midia-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }",
    ".midia-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }"
)

# 2. Replace margin-top with transform for the non-linear layout
css = css.replace(
    ".midia-card:nth-child(even) { margin-top: 48px; }",
    ".midia-card:nth-child(even) { transform: translateY(48px); }"
)

# Also fix the mobile reset if it existed (in mobile, we had margin-top: 0;)
css = css.replace(
    ".midia-card:nth-child(even) { margin-top: 0; }",
    ".midia-card:nth-child(even) { transform: translateY(0); }"
)

# 3. Add flex to midia-card to ensure they all have identical internal layouts (pushing link to bottom)
old_card = """.midia-card {
  background: var(--bg-surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 36px 32px; transition: all .2s;
}"""
new_card = """.midia-card {
  background: var(--bg-surface); border: 1px solid var(--border);
  border-radius: 14px; padding: 36px 32px; transition: all .2s;
  display: flex; flex-direction: column; height: 100%; box-sizing: border-box;
}"""
css = css.replace(old_card, new_card)

# 4. Push link to the bottom
old_link = """.midia-card-link {
  display: inline-flex; align-items: center; gap: 5px;
  font-size: 12px; font-weight: 700; color: var(--c-purple-mid);
  margin-top: 16px;
}"""
new_link = """.midia-card-link {
  display: inline-flex; align-items: center; gap: 5px;
  font-size: 12px; font-weight: 700; color: var(--c-purple-mid);
  margin-top: auto; padding-top: 16px;
}"""
css = css.replace(old_link, new_link)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied transform instead of margin for grid stagger")
