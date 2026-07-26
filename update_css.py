import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_breakpoints = """
/* ══════════════════════════════════════════
   UNIFIED BREAKPOINTS & RESPONSIVENESS
══════════════════════════════════════════ */

/* 1920px+ (Ultrawide) */
@media (min-width: 1441px) {
  .container { max-width: 1400px; }
  .hero-inner { padding: 0 40px; }
}

/* 1024px (Tablet Landscape) */
@media (max-width: 1024px) {
  .pilares-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .qs-pillars-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .banking-products-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .portfolio-layout { grid-template-columns: 240px 1fr; }
  .steps { grid-template-columns: 1fr; gap: 40px; }
  .step:not(:last-child)::after { display: none; }
  .custodia-inner, .qs-grid { grid-template-columns: 1fr; gap: 40px; }
  .blog-grid, .time-grid, .blog-all-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .numeros-grid { grid-template-columns: repeat(2, 1fr); }
  .footer-top { grid-template-columns: 1fr 1fr; gap: 32px; }
}

/* 768px (Tablet Portrait / Mobile Landscape) */
@media (max-width: 768px) {
  .container { padding: 0 20px; }
  .hero { padding: 100px 0 40px; min-height: auto; }
  .hero-content { align-items: center; text-align: center; margin: 0 auto; }
  .hero h1 { font-size: clamp(32px, 8vw, 48px); }
  .hero-cta-row { justify-content: center; width: 100%; flex-direction: column; gap: 16px; }
  
  .portfolio-layout { grid-template-columns: 1fr; }
  .product-tabs { flex-direction: row; overflow-x: auto; border-right: none; border-bottom: 1px solid rgba(255,255,255,0.07); padding-bottom: 8px; }
  .product-tab { flex: 0 0 auto; white-space: nowrap; border-bottom: none; border-right: 1px solid rgba(255,255,255,0.05); }
  .product-tab::before { left: 0; bottom: 0; top: auto; width: 100%; height: 3px; border-radius: 2px 2px 0 0; transform: scaleX(0); }
  .product-tab.active::before { transform: scaleX(1); }
  .sub-products-grid { grid-template-columns: 1fr; }
  .blog-featured { grid-template-columns: 1fr; }
  .qs-btg-inner { flex-direction: column; gap: 32px; }
  
  /* Botões Fluidos - Ocupando 100% do Grid */
  .btn-primary, .btn-hero, .nav-btn-outline, .btn-accent, .btn-outline, .btn-form-submit, button[class*="btn-"], a.btn-primary, a.btn-hero, a.btn-accent, a.btn-outline {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-sizing: border-box;
  }
}

/* 480px (Mobile Portrait) */
@media (max-width: 480px) {
  .pilares-grid, .qs-pillars-grid, .banking-products-grid { grid-template-columns: 1fr; }
  .blog-grid, .time-grid, .blog-all-grid { grid-template-columns: 1fr; }
  .numeros-grid { grid-template-columns: 1fr; }
  .numero-item { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.08); }
  .numero-item:last-child { border-bottom: none; }
  .footer-top { grid-template-columns: 1fr; gap: 40px; }
  .qs-btg-stats { flex-direction: column; gap: 24px; align-items: flex-start; }
  .section-title { font-size: clamp(28px, 7vw, 36px); }
}

/* ══ REDUCED MOTION ══ */
"""

# Replace from /* ══ TABLET BREAKPOINTS ══ */ to the end with our new breakpoints + reduced motion
css = re.sub(r'/\* ══ TABLET BREAKPOINTS ══ \*/.*', new_breakpoints, css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with unified breakpoints.")
