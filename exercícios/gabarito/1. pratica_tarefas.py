
# pratica_tarefas.py
# Objetivo: Criar um mini gerenciador de tarefas usando apenas conceitos vistos até aqui

# 1. Crie uma lista vazia para armazenar tarefas
tarefas = []

# 2. Adicione 3 tarefas iniciais (strings)
tarefas = ["Estudar Python", "Fazer exercícios", "Revisar HTML"]

# 3. Imprima a tarefa prioritária (primeira da lista)
print(f"Prioridade: {tarefas[0]}")

# 4. Marque a primeira tarefa como concluída (substitua por "✅ " + nome da tarefa)
tarefas[0] = "✅ " + tarefas[0]

# 5. Use slicing para mostrar apenas as tarefas pendentes (exclua a primeira)
pendentes = tarefas[1:]
print(f"Pendentes: {pendentes}")

# 6. Inverta a ordem da lista para priorizar as mais recentes
tarefas.reverse()  # ou tarefas = tarefas[::-1]