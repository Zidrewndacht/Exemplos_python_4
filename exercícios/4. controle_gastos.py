# controlador_gastos_pratica.py
# Complete as partes marcadas

print("💰 CONTROLADOR DE GASTOS SEMANAL")

# 1. Coleta do limite
while True:
    limite_input = input("Limite semanal (R$): ").strip()
    # SUA SOLUÇÃO: valide e converta para float
    if __________:
        limite_semanal = float(limite_input)
        break
    print("⚠️  Valor inválido.")

# 2. Coleta de gastos
descricoes = []
valores = []

while True:
    desc = input("Descrição (ou 'fim'): ").strip().title()
    if desc.lower() == 'fim':
        break
    
    # SUA SOLUÇÃO: colete e valide o valor do gasto
    valor = float(valor_input)
    
    # SUA SOLUÇÃO: adicione às listas
    descricoes.append(__________)
    valores.append(__________)

# 3. Cálculos
total_gasto = sum(valores)
saldo_restante = __________

# SUA SOLUÇÃO: identifique gastos >= 50 usando list comprehension
gastos_significativos = [
    (__________, __________) 
    for i in range(len(valores)) 
    if __________
]

# SUA SOLUÇÃO: encontre o maior gasto (abordagem linear sem max())
if len(valores) > 0:
    indice_maior = 0
    for i in range(1, len(valores)):
        if __________:
            indice_maior = i
    categoria_mais_cara = descricoes[indice_maior]
    valor_mais_caro = valores[indice_maior]

# 4. Saída com alertas
print(f"\n📊 Total gasto: R$ {total_gasto:.2f}")
print(f"Saldo: R$ {saldo_restante:.2f}")

# SUA SOLUÇÃO: alertas condicionais
if __________:
    print(f"🚨 ALERTA: Limite ultrapassado!")
elif __________:
    print(f"⚠️  Atenção: Orçamento quase esgotado.")
else:
    print(f"✅ Tudo sob controle.")

if gastos_significativos:
    print(f"\n🔍 Gastos ≥ R$ 50:")
    for desc, val in gastos_significativos:
        print(f"   • {desc}: R$ {val:.2f}")

# BÔNUS 1: Agrupe gastos por categoria simples (ex: "Alimentação", "Transporte")
# Dica: use uma lista de categorias pré-definidas e verifique com in

# BÔNUS 2: Calcule a média de gastos por item registrado
# Dica: total_gasto / len(valores)

# BÔNUS 3: Sugira um valor máximo por gasto restante para não estourar o limite
# Fórmula: saldo_restante / (dias_restantes_da_semana * gastos_medios_por_dia)