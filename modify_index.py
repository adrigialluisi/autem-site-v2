import re

with open('/Users/adrianagialluisi/Desktop/Autem/autem-site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. HERO MENOR + NÚMEROS NO PRIMEIRO VIEWPORT
content = content.replace(
    ".hero {\n  background: var(--grad-hero);\n  min-height: 92vh;\n  display: flex; align-items: center;\n  padding: 80px 0 60px;\n  position: relative; overflow: hidden;\n}",
    ".hero {\n  background: var(--grad-hero);\n  min-height: 70vh;\n  display: flex; align-items: center;\n  padding: 100px 0 20px;\n  position: relative; overflow: hidden;\n}"
)

content = content.replace(
    ".hero-scroll-indicator {\n  position: absolute; bottom: 32px;",
    ".hero-scroll-indicator {\n  position: absolute; bottom: 16px;"
)

content = content.replace(
    ".numeros {\n  padding: 72px 0;\n  background: #3A4FD6;\n}",
    ".numeros {\n  padding: 20px 0 64px 0;\n  background: var(--grad-hero);\n  position: relative;\n  z-index: 1;\n}"
)

# 2. BARRA DE PRÊMIOS SEPARADA (CSS)
old_numeros_premio_css = """.numeros-premio {
  display: flex; align-items: center; justify-content: center; gap: 32px;
  margin-top: 48px; padding-top: 40px;
  border-top: 1px solid rgba(255,255,255,0.07);
  flex-wrap: wrap;
}
.premio-badge {
  display: flex; align-items: center; gap: 12px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px; padding: 14px 22px;
}
.premio-badge-icon {
  width: 36px; height: 36px; border-radius: 8px;
  background: rgba(69,235,203,0.12);
  display: flex; align-items: center; justify-content: center;
  color: var(--c-green);
}
.premio-badge-text { font-size: 13px; color: rgba(255,255,255,0.7); font-weight: 600; }
.premio-badge-sub { font-size: 11px; color: rgba(255,255,255,0.35); margin-top: 2px; }"""

new_numeros_premio_css = """.premios-bar {
  padding: 32px 0;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
}
.numeros-premio {
  display: flex; align-items: center; justify-content: center; gap: 32px;
  flex-wrap: wrap;
}
.premio-badge {
  display: flex; align-items: center; gap: 12px;
  background: var(--bg-white);
  border: 1px solid var(--border);
  border-radius: 12px; padding: 14px 22px;
}
.premio-badge-icon {
  width: 36px; height: 36px; border-radius: 8px;
  background: rgba(69,235,203,0.15);
  display: flex; align-items: center; justify-content: center;
  color: var(--c-green);
}
.premio-badge-text { font-size: 13px; color: var(--text-primary); font-weight: 600; }
.premio-badge-sub { font-size: 11px; color: var(--text-muted); margin-top: 2px; }"""
content = content.replace(old_numeros_premio_css, new_numeros_premio_css)

# BARRA DE PRÊMIOS (HTML)
old_html_numeros_premio = """      </div>
      <div class="numeros-premio">
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Top Escritório BTG</div>
            <div class="premio-badge-sub">Prêmio 2024</div>
          </div>
        </div>
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Certificação CVM</div>
            <div class="premio-badge-sub">Resolução 178</div>
          </div>
        </div>
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Parceiro BTG Pactual</div>
            <div class="premio-badge-sub">Maior banco de inv. da AL</div>
          </div>
        </div>
      </div>
    </div>
  </section>"""

new_html_numeros_premio = """      </div>
    </div>
  </section>

  <!-- BARRA DE PRÊMIOS -->
  <section class="premios-bar">
    <div class="container">
      <div class="numeros-premio">
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Top Escritório BTG</div>
            <div class="premio-badge-sub">Prêmio 2024</div>
          </div>
        </div>
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Certificação CVM</div>
            <div class="premio-badge-sub">Resolução 178</div>
          </div>
        </div>
        <div class="premio-badge">
          <div class="premio-badge-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <div class="premio-badge-text">Parceiro BTG Pactual</div>
            <div class="premio-badge-sub">Maior banco de inv. da AL</div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
content = content.replace(old_html_numeros_premio, new_html_numeros_premio)

# 4. SAIBA MAIS NOS CARDS E MAIS CTAs
# Adicionar CSS para card-link
content = content.replace(
    ".pilar-desc { font-size: var(--text-sm); color: var(--text-muted); line-height: 1.68; }",
    ".pilar-desc { font-size: var(--text-sm); color: var(--text-muted); line-height: 1.68; }\n.card-link {\n  display: inline-flex; align-items: center; gap: 6px;\n  font-size: 13px; font-weight: 700; color: var(--c-purple-mid);\n  margin-top: 16px; transition: color .2s;\n}\n.card-link:hover { color: var(--c-purple-dark); }"
)

# Adicionar links nos pilar-cards
pilar_replacements = [
    (
        '<p class="pilar-desc">Acesso completo ao maior banco de investimentos da América Latina, com toda a solidez e tecnologia do BTG Pactual.</p>',
        '<p class="pilar-desc">Acesso completo ao maior banco de investimentos da América Latina, com toda a solidez e tecnologia do BTG Pactual.</p>\n          <a href="https://www.btgpactual.com" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="pilar-desc">Uma equipe dedicada a entender seus objetivos e indicar as melhores oportunidades do mercado para o seu perfil.</p>',
        '<p class="pilar-desc">Uma equipe dedicada a entender seus objetivos e indicar as melhores oportunidades do mercado para o seu perfil.</p>\n          <a href="quem-somos.html" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="pilar-desc">Gerencie toda a sua carteira pelo app BTG a qualquer hora — com visibilidade total sobre seus investimentos.</p>',
        '<p class="pilar-desc">Gerencie toda a sua carteira pelo app BTG a qualquer hora — com visibilidade total sobre seus investimentos.</p>\n          <a href="https://www.btgpactual.com/aplicativo" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="pilar-desc">Fundos fechados, operações estruturadas, ofertas coordenadas pelo BTG e ativos exclusivos do ecossistema.</p>',
        '<p class="pilar-desc">Fundos fechados, operações estruturadas, ofertas coordenadas pelo BTG e ativos exclusivos do ecossistema.</p>\n          <a href="https://www.btgpactual.com/investimentos" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    )
]

for old, new in pilar_replacements:
    content = content.replace(old, new)

# CTA pós Pilares
content = content.replace(
    "      </div>\n    </div>\n  </section>\n\n\n  <!-- PORTFÓLIO",
    "      </div>\n      <div class=\"text-center\" style=\"margin-top: 56px;\">\n        <button class=\"btn-primary\">Abra sua conta</button>\n      </div>\n    </div>\n  </section>\n\n\n  <!-- PORTFÓLIO"
)

# Adicionar links nos banking-prod-cards
banking_replacements = [
    (
        '<p class="banking-prod-desc">TED e PIX sem custo. Saldo aplicado automaticamente no overnight — seu dinheiro parado rende.</p>',
        '<p class="banking-prod-desc">TED e PIX sem custo. Saldo aplicado automaticamente no overnight — seu dinheiro parado rende.</p>\n            <a href="https://banking.btgpactual.com" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Programa de milhas com principalidade BTG. Anuidade zero e controle pelo app integrado à carteira.</p>',
        '<p class="banking-prod-desc">Programa de milhas com principalidade BTG. Anuidade zero e controle pelo app integrado à carteira.</p>\n            <a href="https://banking.btgpactual.com/cartoes" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Empréstimo com garantia de investimentos. Taxas menores, sem precisar resgatar sua carteira.</p>',
        '<p class="banking-prod-desc">Empréstimo com garantia de investimentos. Taxas menores, sem precisar resgatar sua carteira.</p>\n            <a href="https://banking.btgpactual.com/credito" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Crédito com garantia de imóvel. Acesso a grandes valores com parcelas compatíveis e taxas competitivas.</p>',
        '<p class="banking-prod-desc">Crédito com garantia de imóvel. Acesso a grandes valores com parcelas compatíveis e taxas competitivas.</p>\n            <a href="https://banking.btgpactual.com/credito" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Débito automático, boletos e pagamentos integrados. Tudo em um único app, sem trocar de banco.</p>',
        '<p class="banking-prod-desc">Débito automático, boletos e pagamentos integrados. Tudo em um único app, sem trocar de banco.</p>\n            <a href="https://banking.btgpactual.com" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Remessas internacionais e cartão multimoeda. Taxas competitivas com câmbio BTG direto no app.</p>',
        '<p class="banking-prod-desc">Remessas internacionais e cartão multimoeda. Taxas competitivas com câmbio BTG direto no app.</p>\n            <a href="https://banking.btgpactual.com/cambio" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Conta corrente empresarial com TED, PIX e boletos sem custo. Saldo aplicado automaticamente no overnight.</p>',
        '<p class="banking-prod-desc">Conta corrente empresarial com TED, PIX e boletos sem custo. Saldo aplicado automaticamente no overnight.</p>\n            <a href="https://empresas.btgpactual.com" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Cartão corporativo com controle de gastos por centro de custo e integração com o sistema financeiro da empresa.</p>',
        '<p class="banking-prod-desc">Cartão corporativo com controle de gastos por centro de custo e integração com o sistema financeiro da empresa.</p>\n            <a href="https://empresas.btgpactual.com/cartoes" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Linhas de crédito para necessidades operacionais. Aprovação ágil e taxas competitivas para empresas em crescimento.</p>',
        '<p class="banking-prod-desc">Linhas de crédito para necessidades operacionais. Aprovação ágil e taxas competitivas para empresas em crescimento.</p>\n            <a href="https://empresas.btgpactual.com/credito" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Antecipe duplicatas, notas fiscais e recebíveis de cartão. Melhore o fluxo de caixa sem comprometer o limite bancário.</p>',
        '<p class="banking-prod-desc">Antecipe duplicatas, notas fiscais e recebíveis de cartão. Melhore o fluxo de caixa sem comprometer o limite bancário.</p>\n            <a href="https://empresas.btgpactual.com/credito" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Estrutura de garantia para contratos, M&As e projetos. Controle total dos fluxos com segurança jurídica.</p>',
        '<p class="banking-prod-desc">Estrutura de garantia para contratos, M&As e projetos. Controle total dos fluxos com segurança jurídica.</p>\n            <a href="https://empresas.btgpactual.com" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    ),
    (
        '<p class="banking-prod-desc">Remessas, importações e exportações com câmbio BTG. Hedge cambial e consultoria especializada para empresas.</p>',
        '<p class="banking-prod-desc">Remessas, importações e exportações com câmbio BTG. Hedge cambial e consultoria especializada para empresas.</p>\n            <a href="https://empresas.btgpactual.com/cambio" target="_blank" class="card-link">Saiba mais &rarr;</a>'
    )
]

for old, new in banking_replacements:
    content = content.replace(old, new)

# CTA pós Banking
content = content.replace(
    "      </div>\n    </div>\n  </section>\n\n  <!-- COMO FUNCIONA -->",
    "      </div>\n      <div class=\"text-center\" style=\"margin-top: 56px;\">\n        <button class=\"btn-primary\">Abra sua conta</button>\n      </div>\n    </div>\n  </section>\n\n  <!-- COMO FUNCIONA -->"
)

# CTA pós Mídia
content = content.replace(
    "Ver todas as matérias →\n          </a>\n        </div>\n      </div>\n    </div>\n  </section>\n\n  <!-- CUSTÓDIA -->",
    "Ver todas as matérias →\n          </a>\n          <div style=\"margin-top: 32px;\">\n            <button class=\"btn-primary\">Abra sua conta</button>\n          </div>\n        </div>\n      </div>\n    </div>\n  </section>\n\n  <!-- CUSTÓDIA -->"
)

with open('/Users/adrianagialluisi/Desktop/Autem/autem-site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modificacoes aplicadas com sucesso.")
