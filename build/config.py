# -*- coding: utf-8 -*-
"""
Configuração do cliente — PCA · Plano de Captação de Clientes na Advocacia (sigla PCA).

Este é o ÚNICO arquivo que precisa ser editado para colocar o funil de um
cliente novo no ar (o build se recusa a rodar enquanto algum marcador de
texto do template continuar aqui).
Ordem completa: "CHECKLIST DE NOVO CLIENTE" no topo do CLAUDE.md.

Depois de editar, teste localmente:

    python build/build.py --meta-file meta.csv --sales-file sales.csv --out dist/index.html

`build/config.example.py` é a cópia intacta deste modelo — mantenha-o
sem preencher, para restaurar o config.py se precisar começar do zero.
"""
from __future__ import annotations

# ==========================================================================
# 1) PLANILHA(S) DO CLIENTE (Google Sheets)
# ==========================================================================
# SPREADSHEET_ID: o trecho entre /d/ e /edit na URL da planilha
#   (https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=...)
# GID_META / GID_SALES: o número depois de "gid=" na URL de cada aba.
# A planilha precisa estar com o link público em modo "Qualquer pessoa com
# o link pode visualizar" (o build lê via export CSV, SOMENTE LEITURA).
SPREADSHEET_ID = "1YI7XEWZP528Ru_MTLr6UtHnhc1Hfi6XAi-h3dA4WO7M"  # planilha única (Vendas PCA · Log · Página2)
# Opcional: se a lista de Compradores estiver em OUTRA planilha, coloque o ID
# dela aqui. Vazio = Compradores na mesma planilha do Meta Ads (padrão).
SPREADSHEET_ID_SALES = ""
GID_META = "883396410"    # aba "Página2" (export do Meta Ads)
GID_SALES = "1497298595"  # aba "Vendas PCA" (webhook da plataforma) — NÃO usar "Log"

# ==========================================================================
# 2) REGRAS DE NEGÓCIO
# ==========================================================================
# Fator de imposto aplicado sobre o gasto do Meta Ads quando o toggle
# "Imposto Meta" estiver ligado. Use 1.0 se o cliente não tiver imposto.
TAX_FACTOR = 1.13806   # +13,806% (mesmo padrão das demais dashs)

# Produto principal do funil (base de Vendas/CAC/ConvCHK/Ticket). Casamento
# por PREFIXO sobre o nome NORMALIZADO (sem acento, minúsculas) da coluna
# Produto da planilha de Compradores — escreva sem acento e em minúsculas.
# Aceita um prefixo ou uma tupla de prefixos. Em 23/10/2026 a aba Vendas PCA
# ainda não tinha nenhuma venda — conferir o nome real do produto na 1ª venda.
MAIN_PRODUCT_PREFIX = ("pca", "plano de captacao")
# A aba Vendas PCA é exclusiva deste funil: enquanto nenhum produto casar com
# o prefixo acima, todo produto aprovado conta como venda principal.
MAIN_PRODUCT_FALLBACK_ALL = True

# Qual coluna UTM da planilha de Compradores carrega o Ad Name do Meta:
# "utm_content", "utm_term" ou "utm_medium". Depende do parametrizador de URL
# dos anúncios do cliente — CONFIRA nos dados antes de assumir: a coluna que
# não carrega o anúncio costuma trazer o posicionamento (Instagram_Feed/Stories),
# e casar pela coluna errada zera as atribuições.
# Padrão das demais dashs (utm_content = Ad Name, ex.: AD01). Sem vendas ainda
# em 23/10/2026 para confirmar — validar na 1ª venda (CLAUDE.md, problema #10).
AD_UTM_COLUMN = "utm_content"

# A planilha de Compradores tem uma coluna de status de pagamento confiável?
# SIM -> False (o build filtra por is_paid()). NÃO (toda linha já é uma compra
# concretizada) -> True (conta todas as linhas como venda paga).
# PCA: a aba Vendas PCA vem de webhook (colunas Evento/Status, 1 linha por
# evento) — só conta status aprovado/pago, último evento de cada Order ID.
COUNT_ALL_AS_PAID = False

# Vendas com utm_source do Meta contam como tráfego do Meta mesmo sem casar
# com um anúncio da planilha (UTM quebrada {{...}}, campanha fora da extração).
META_UTM_SOURCES = ("meta-ads", "meta_ads", "meta ads", "facebook", "instagram", "fb", "ig")
# Sigla das campanhas deste funil (ex.: "PCA | E4-VEN | P2-FRIO | ...").
SIGLA = "PCA"

# ==========================================================================
# 3) RÓTULOS EXIBIDOS NA INTERFACE
# ==========================================================================
CLIENT_NAME = "PCA"
CLIENT_SUB = "Plano de Captação de Clientes na Advocacia"
TAX_LABEL = "Imposto Meta ×1,13806"
MAIN_PRODUCT = "PCA — Plano de Captação de Clientes na Advocacia"

# ==========================================================================
# 4) METAS (aba Relatórios) — código de cor de CAC/ROAS
# ==========================================================================
#   • ROAS: quanto MAIOR, melhor  -> desempenho = roas / ROAS_TARGET
#   • CAC : quanto MENOR, melhor  -> desempenho = CAC_TARGET / cac
# Faixas (sobre o desempenho): <REPORT_BAND_LOW vermelho · até 0,99 amarelo ·
#   até REPORT_BAND_HIGH verde · acima disso azul-ciano.
# CAC alvo em R$ — não definido ainda; 0.0 = sem código de cor no CAC
CAC_TARGET = 0.0
# ROAS alvo (Faturamento / Gasto) — não definido ainda; 0.0 = sem código de cor no ROAS
ROAS_TARGET = 0.0
REPORT_BAND_LOW = 0.70
REPORT_BAND_HIGH = 1.30

# ==========================================================================
# 5) IA INSIGHTS (Cloudflare Worker) — ver SETUP-IA.md
# ==========================================================================
# URL pública do Worker (não é secreta). Vazio = aba IA Insights indisponível.
# Preencher depois de publicar o Worker (checklist do CLAUDE.md).
# Worker ainda não publicado (SETUP-IA.md) — aba IA Insights desativada até lá.
IA_WORKER_URL = ""
