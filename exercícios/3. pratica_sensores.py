# pratica_sensores.py
# Contexto real: Filtrar e processar leituras de sensores (valores válidos entre 0-100)

# Dados brutos de um sensor (alguns com erro: -1 ou >100)
leituras_brutas = [23, 45, -1, 67, 105, 34, 89, -1, 56, 78]

# 1. Filtre apenas leituras válidas (0 <= valor <= 100) usando list comprehension
# Sua solução aqui:


# 2. Calcule a média das leituras válidas (use sum() e len())
# Sua solução aqui:


# 3. Classifique cada leitura válida como "Baixa" (<40), "Média" (40-70) ou "Alta" (>70)
# Use conditional expression dentro de uma comprehension
# Sua solução aqui:


# 4. BÔNUS: Crie uma lista de tuplas (valor, classificação) apenas para leituras > 50
# Exemplo de saída: [(67, "Média"), (89, "Alta"), (56, "Média"), (78, "Alta")]
# Sua solução aqui: