import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update font sizes and button heights on mobile (in 768px block)
# Find the 768px unified block at the end (I added it recently)
# It starts with: /* 768px (Tablet Portrait / Mobile Landscape) */\n@media (max-width: 768px) {

mobile_vars = """  :root {
    --text-xs: 12px;
    --text-sm: 15px;
    --text-base: 17px;
    --text-md: 19px;
    --text-lg: 22px;
  }
"""

# Inject mobile_vars just after the 768px unified media query opens
css = css.replace(
    "/* 768px (Tablet Portrait / Mobile Landscape) */\n@media (max-width: 768px) {",
    "/* 768px (Tablet Portrait / Mobile Landscape) */\n@media (max-width: 768px) {\n" + mobile_vars
)

# 2. Make buttons taller and enforce font size on mobile
old_btn_css = """.btn-primary, .btn-hero, .nav-btn-outline, .btn-accent, .btn-outline, .btn-form-submit, button[class*="btn-"], a.btn-primary, a.btn-hero, a.btn-accent, a.btn-outline {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-sizing: border-box;
  }"""

new_btn_css = """.btn-primary, .btn-hero, .nav-btn-outline, .btn-accent, .btn-outline, .btn-form-submit, button[class*="btn-"], a.btn-primary, a.btn-hero, a.btn-accent, a.btn-outline {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-sizing: border-box;
    min-height: 52px;
    font-size: 16px;
    padding: 14px 24px;
    margin-top: 16px;
  }
  
  /* Sections Padding Mobile Standardization */
  .pilares, .portfolio, .banking-section, .como-funciona,
  .midia-section, .custodia, .blog-section { padding: 56px 0; }
  
  /* Card Padding Mobile */
  .pilar-card, .banking-prod-card, .blog-body, .time-card-body, .qs-pillar {
    padding: 24px 20px;
  }
  .card-link { margin-top: 24px; font-size: 15px; }
  
  .section-title { margin-bottom: 20px; }
  .section-sub { margin-bottom: 32px; }
"""

css = css.replace(old_btn_css, new_btn_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with better typography scale and spacing")
