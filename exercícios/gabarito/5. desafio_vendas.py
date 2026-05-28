# desafio_vendas.py
# Contexto real: Pequeno e-commerce precisa de relatório diário de vendas

# Dados de entrada (vendas do dia: valor de cada transação)
vendas = [120.50, 45.00, 0, 89.90, -10.00, 200.00, 15.75, 0, 150.30]

# 1. Filtrar vendas válidas
vendas_validas = [v for v in vendas if v > 0]

# 2. Cálculos estatísticos
total = sum(vendas_validas)
quantidade = len(vendas_validas)
ticket_medio = total / quantidade if quantidade > 0 else 0
maior_venda = max(vendas_validas) if vendas_validas else 0
menor_venda = min(vendas_validas) if vendas_validas else 0

# 3. Vendas premium
vendas_premium = [v for v in vendas_validas if v >= 100]

# 4. Relatório formatado
print("📊 RELATÓRIO DE VENDAS DIÁRIO")
print(f"✅ Vendas válidas: {quantidade}")
print(f"💰 Total: R$ {total:.2f}")
print(f"🎫 Ticket médio: R$ {ticket_medio:.2f}")
print(f"📈 Maior venda: R$ {maior_venda:.2f}")
print(f"📉 Menor venda: R$ {menor_venda:.2f}")
print(f"⭐ Vendas premium (≥R$100): {len(vendas_premium)}")
if vendas_premium:
    print(f"   Valores: {[f'R$ {v:.2f}' for v in vendas_premium]}")