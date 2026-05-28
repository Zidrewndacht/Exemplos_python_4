# pratica_sensores.py
# Contexto real: Filtrar e processar leituras de sensores (valores válidos entre 0-100)

# Dados brutos de um sensor (alguns com erro: -1 ou >100)
leituras_brutas = [23, 45, -1, 67, 105, 34, 89, -1, 56, 78]

# 1. Filtrar válidas
leituras_validas = [v for v in leituras_brutas if 0 <= v <= 100]

# 2. Média
media = sum(leituras_validas) / len(leituras_validas)
print(f"Média: {media:.2f}")

# 3. Classificação
classificacoes = [
    "Baixa" if v < 40 else "Média" if v <= 70 else "Alta"
    for v in leituras_validas
]

# 4. BÔNUS: tuplas para valores > 50
resultado = [
    (v, "Média" if v <= 70 else "Alta")
    for v in leituras_validas if v > 50
]
print(resultado)