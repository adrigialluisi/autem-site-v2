with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix midia cards stretching
# Add align-items: start; to .midia-cards so they don't stretch to the row height
css = css.replace(
    ".midia-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }",
    ".midia-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }"
)

# Also make the cards display flex column to push the link to the bottom just in case they have slightly different text heights, 
# wait, if align-items: start is used, they won't have different heights from the grid, they will just take their own content height.
# Let's see if setting height: 100% works. If we use align-items: stretch (default), we can use display: flex; flex-direction: column; justify-content: space-between on the cards. But that puts the empty space in the middle.

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied align-items: start")
