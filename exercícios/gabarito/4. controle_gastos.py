# controlador_gastos_semanal.py
# Programa útil: controle financeiro pessoal com alertas inteligentes

print("💰 CONTROLADOR DE GASTOS SEMANAL")
print("Registre seus gastos e receba alertas sobre seu orçamento.\n")

# 1. Definição do limite semanal
while True:
    limite_input = input("Defina seu limite semanal de gastos (R$): ").strip()
    if limite_input.replace('.', '', 1).isdigit():
        limite_semanal = float(lime_input)
        if limite_semanal > 0:
            break
    print("⚠️  Digite um valor positivo válido.")

# 2. Coleta de gastos: listas paralelas para descrição e valor
descricoes = []
valores = []

print("\n📝 Registre seus gastos (digite 'fim' na descrição para encerrar):")
while True:
    desc = input("Descrição do gasto: ").strip().title()
    
    if desc.lower() == 'fim':
        if len(valores) == 0:
            print("⚠️  Registre pelo menos um gasto para ver o relatório.")
            continue
        break
    
    if desc == "":
        print("⚠️  Descrição não pode ser vazia.")
        continue
    
    # Coleta e validação do valor
    valor_input = input(f"Valor para '{desc}' (R$): ").strip()
    if not valor_input.replace('.', '', 1).isdigit():
        print("⚠️  Digite um valor numérico válido.")
        continue
    
    valor = float(valor_input)
    if valor <= 0:
        print("⚠️  Valor deve ser positivo.")
        continue
    
    # Armazena nas listas
    descricoes.append(desc)
    valores.append(valor)
    print(f"✅ '{desc}': R$ {valor:.2f} registrado.\n")

# 3. Cálculos e análises
total_gasto = sum(valores)
saldo_restante = limite_semanal - total_gasto

# Identifica gastos acima de R$ 50 (alerta de "gasto significativo")
gastos_significativos = [
    (descricoes[i], valores[i]) 
    for i in range(len(valores)) 
    if valores[i] >= 50
]

# Categoria mais cara (sem usar funções - abordagem linear)
if len(valores) > 0:
    indice_maior = 0
    for i in range(1, len(valores)):
        if valores[i] > valores[indice_maior]:
            indice_maior = i
    categoria_mais_cara = descricoes[indice_maior]
    valor_mais_caro = valores[indice_maior]
else:
    categoria_mais_cara = "Nenhuma"
    valor_mais_caro = 0

# 4. Saída formatada com alertas úteis
print("\n" + "💰"*25)
print(f"📊 RELATÓRIO SEMANAL")
print(f"Limite definido: R$ {limite_semanal:.2f}")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Saldo restante: R$ {saldo_restante:.2f}")

# Alertas condicionais
if saldo_restante < 0:
    print(f"🚨 ALERTA: Você ultrapassou o limite em R$ {abs(saldo_restante):.2f}!")
elif saldo_restante < limite_semanal * 0.2:
    print(f"⚠️  ATENÇÃO: Restam menos de 20% do seu orçamento (R$ {saldo_restante:.2f}).")
else:
    print(f"✅ Orçamento sob controle.")

if gastos_significativos:
    print(f"\n🔍 Gastos significativos (≥ R$ 50,00):")
    for desc, val in gastos_significativos:
        print(f"   • {desc}: R$ {val:.2f}")

if len(valores) > 0:
    print(f"\n📈 Maior gasto: {categoria_mais_cara} (R$ {valor_mais_caro:.2f})")

print("💰"*25)