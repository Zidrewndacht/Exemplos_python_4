# pratica_fila.py
# Contexto real: Sistema simples de fila de atendimento (primeiro a entrar, primeiro a sair)

fila_atendimento = []

# 1. Simule a chegada de 5 clientes (nomes) na fila
# Use append() para adicionar ao final
clientes = ["Ana", "Bruno", "Carla", "Daniel", "Elena"]
# Sua solução aqui:
# copie os clientes para a fila_atendimento em ordem de chegada:

for cliente in clientes:
    fila_atendimento.append(cliente)

# Atender primeiros 2
fila_atendimento.pop(0)  # Ana
fila_atendimento.pop(0)  # Bruno

# Prioritário
fila_atendimento.insert(0, "Fernanda")

# Exibir com numeração
for pos, nome in enumerate(fila_atendimento, start=1):
    print(f"{pos}. {nome}")

# Verificar presença
if "Ana" in fila_atendimento:
    print("Ana ainda está na fila")
else:
    print("Ana já foi atendida")