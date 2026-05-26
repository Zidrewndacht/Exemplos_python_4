# listas_iteracao.py

# 🔄 Iteração básica com for
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
for nota in notas:
    print(f"Nota: {nota}")

# 🔢 Com índice: use enumerate() (PEP 8 preferido sobre range(len()))
for indice, nota in enumerate(notas, start=1):
    print(f"Aluno {indice}: {nota}")

# 🤝 Iteração paralela: use zip()
alunos = ["Ana", "Bruno", "Carla"]
notas = [8.5, 7.0, 9.0]
for aluno, nota in zip(alunos, notas):
    print(f"{aluno}: {nota}")

# ✨ List Comprehensions: forma concisa de criar listas
# Sintaxe: [expressão for item in iterável if condição]

# Exemplo 1: Transformação (quadrado de números)
quadrados = [n**2 for n in range(1, 6)]  # [1, 4, 9, 16, 25]

# Exemplo 2: Filtragem (apenas notas >= 7)
notas = [7.5, 6.0, 8.0, 5.5, 9.0]
aprovados = [n for n in notas if n >= 7]  # [7.5, 8.0, 9.0]

# Exemplo 3: Transformação + Filtragem (notas aprovadas com bônus)
notas_com_bonus = [n + 0.5 for n in notas if n >= 7]  # [8.0, 8.5, 9.5]

# Exemplo 4: Conditional expression dentro da comprehension
status = ["Aprovado" if n >= 7 else "Reprovado" for n in notas]

# ⚠️ Quando NÃO usar comprehensions:
# - Lógica muito complexa (prefira loop tradicional para legibilidade)
# - Efeitos colaterais (ex: print dentro da comprehension)
# - Quando você não precisa da lista resultante (use loop simples)