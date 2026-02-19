numeros = [1, 2, 3, 4, 5]

numeros_duplicados = [numero * 2 for numero in numeros]

print(numeros)
print(numeros_duplicados)

#mapeamento é pegar uma lista e gerar outra lista apartir dela do mesmo tamanho com cada item modificado

produtos = [
    {"nome": "tv", "preco": 200.0},
    {"nome" : "radio", "preco": 300.0},
    {"nome" : "celular", "preco": 1200.0}
]

novos_produtos = [{**produto, "preco" : produto["preco"] * 1.5} for produto in produtos]

print(novos_produtos)