#importações necessarias
from itertools import combinations, permutations, product



#listas para teste
pessoas = ["Antonio", "Sintia", "Carlos", "rita"]

camisetas  = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculina", "feminina"],
    ["algodão", "sintetico"],
    ]

# COMBINAÇÂO = para criar grupos ex: duplas de trabalho
#a ordem não importa - ele foca em todas as conbinações teoricas - osado em estatistica e probabilidade
print(combinations(pessoas, 2))#retotna um objeto iterator <itertools.combinations object at 0x7373151d42c0>

#ao comsumir em uma lista dá para ver as combinações em dois grupos, as combinações são unicas
print(*list(combinations(pessoas, 2)), sep="\n")

print("-" * 20)

# PERMUTAÇÂO = variações de ordem [Antonio, Rita] é diferente de [Rita, Antonio] então ele mostra todas as possibilidades
print(*list(permutations(pessoas, 2)), sep="\n")

print("-" * 20)

#PRODUTO = para cruzamento de caracteristicas ex: gerador de estoque, combina cada item da lista A com todos da lista B, C, D
print(*list(product(*camisetas)), sep="\n")