# desafio_vendas.py
# Contexto real: Pequeno e-commerce precisa de relatório diário de vendas

# Dados de entrada (vendas do dia: valor de cada transação)
vendas = [120.50, 45.00, 0, 89.90, -10.00, 200.00, 15.75, 0, 150.30]

# 🎯 Requisitos:
# 1. Remova vendas inválidas (valores <= 0)
# 2. Calcule:
#    • Total de vendas válidas
#    • Ticket médio (total / quantidade)
#    • Maior e menor venda
# 3. Crie uma lista de "vendas premium" (>= R$ 100)
# 4. Gere um relatório formatado (use f-strings)

# 💡 Dicas:
# - Use list comprehensions para filtrar e transformar
# - Métodos úteis: max(), min(), sum(), len()
# - Formatação: f"{valor:.2f}" para 2 casas decimais

# Sua solução completa aqui: