with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix carousel top margin that was stuck to text
# I will replace margin: 0 -20px; with margin: 40px -20px 0; inside the carousel track
css = css.replace("margin: 0 -20px;", "margin: 40px -20px 0;")

# Append strict mobile typography overrides
strict_mobile_css = """

/* ══════════════════════════════════════════
   STRICT MOBILE OVERRIDES (TYPOGRAPHY & BUTTONS)
══════════════════════════════════════════ */
@media (max-width: 768px) {
  /* Fix Carousel stuck to text */
  .carousel-track {
    margin-top: 32px !important;
  }

  /* Increase Card Titles */
  .pilar-title, .banking-prod-title, .sub-product-title, .blog-title, .time-card-name, .step-title, .step-visual-title, .blog-mini-title {
    font-size: 20px !important;
    line-height: 1.3 !important;
  }

  /* Increase Card Descriptions */
  .pilar-desc, .banking-prod-desc, .sub-product-desc, .blog-excerpt, .time-card-bio, .step-desc, .step-visual-desc {
    font-size: 16px !important;
    line-height: 1.6 !important;
  }

  /* Increase Buttons */
  .btn-primary, .btn-hero, .btn-accent, .btn-outline, .btn-form-submit, .nav-btn-outline, .blog-cat-btn {
    font-size: 16px !important;
    min-height: 54px !important;
    padding: 16px 24px !important;
    font-weight: 800 !important;
  }
  
  /* Section Subtitles */
  .section-sub {
    font-size: 18px !important;
  }
  
  /* Link inside cards */
  .card-link {
    font-size: 16px !important;
    margin-top: 24px !important;
  }
}
"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + strict_mobile_css)

print("Appended strict mobile overrides")
