
#o que vem na direita do for é mapeamento o que vem na esquerda do for é filtro, filtrando os numeors menor ou igual a 5.
lista_numeros = [ numero for numero in range(10) if numero <= 5]

print(lista_numeros)

produtos = [
    {"nome" : "tv", "preco": 500.0},
    {"nome" : "radio", "preco": 300.0},
    {"nome" : "celular", "preco" : 2000.0}
]

novos_produtos = [ {**produto, "preco" : produto["preco"] * 1.5} for produto in produtos  if produto["preco"] < 500.0]

print(novos_produtos)