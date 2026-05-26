# listas_metodos.py

# 🔧 Métodos que MODIFICAM a lista original (retornam None!)
frutas = ["maçã", "banana"]

frutas.append("laranja")      # Adiciona ao final → ["maçã", "banana", "laranja"]
frutas.insert(1, "morango")   # Insere na posição 1 → ["maçã", "morango", "banana", "laranja"]
frutas.extend(["uva", "kiwi"]) # Adiciona múltiplos elementos

# 🗑️ Remoção de elementos
frutas.remove("banana")       # Remove primeira ocorrência do valor (erro se não existir)
ultima = frutas.pop()         # Remove e retorna o último elemento (ou índice específico)
# del frutas[0]               # Remove por índice (não retorna valor)

# 🔍 Busca e contagem
print(frutas.index("uva"))    # Retorna índice da primeira ocorrência (erro se não existir)
print(frutas.count("maçã"))   # Quantas vezes "maçã" aparece?

# 🔄 Reorganização
frutas.sort()                 # Ordena in-place (alfabético para strings)
frutas.reverse()              # Inverte a ordem in-place

# 📋 Cópia segura (shallow copy)
copia = frutas.copy()         # ou frutas[:]

# ⚠️ IMPORTANTE: Métodos como append(), sort(), reverse() retornam None!
resultado = frutas.sort()
print(resultado)  # None - NÃO faça: lista = lista.sort()