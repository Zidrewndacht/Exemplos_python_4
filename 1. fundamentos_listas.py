# listas_fundamentos.py

# ✅ Criação de listas - múltiplas formas
frutas = ["maçã", "banana", "laranja"]           # Literal
numeros = list(range(1, 6))                        # Conversão de range
vazia = []                                         # Lista vazia
misturada = [1, "texto", 3.14, True]              # Tipos mistos (permitido, mas use com critério)

# 🔍 Indexação: acesso por posição (0-based)
print(frutas[0])    # "maçã" - primeiro elemento
print(frutas[-1])   # "laranja" - último elemento (índice negativo)

# ✂️ Slicing: fatiamento [início:fim:passo]
print(frutas[0:2])     # ["maçã", "banana"] - do índice 0 até 1 (fim exclusivo)
print(frutas[::2])     # ["maçã", "laranja"] - pula de 2 em 2
print(frutas[::-1])    # ["laranja", "banana", "maçã"] - inverte a lista

# 🔄 Listas são MUTÁVEIS (podem ser alteradas após criação)
frutas[1] = "morango"  # Substitui "banana" por "morango"
print(frutas)          # ["maçã", "morango", "laranja"]

# ⚠️ Cuidado com aliasing (duas variáveis apontando para a mesma lista)
lista_a = [1, 2, 3]
lista_b = lista_a      # NÃO cria cópia! Ambas referenciam o mesmo objeto
lista_b.append(4)
print(lista_a)         # [1, 2, 3, 4] - lista_a também foi alterada!

# ✅ Para copiar de verdade:
lista_c = lista_a.copy()  # ou lista_a[:]
lista_c.append(5)
print(lista_a)            # [1, 2, 3, 4] - inalterada