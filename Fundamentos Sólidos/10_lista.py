# diferente de uma variavel simples que aponta para um unico valor, uma lista é uma estrutura que permite apontar para uma sequencia de valores.

frutas = ["Maçã", "Banana", "Uva"]

# cada posição ou index (0 ,1, 2, ...) aponta para o endereço de cada valor literal.

# assim é possivel acessar cada valor pela posição que começa da posição [0]:
print(frutas[0])
print(frutas[1])
print(frutas[2])

# o python mantém a ordem em que o item foi colocado.
# listas são mutaveis, por isso é possivel mudar para onde cada indice aponta.

frutas[1] = "Morango"
# a etiqueta do indice 1 parou de apontar para "Banana" e agora aponta para "Morango".

print(frutas)#mostrando lista inteira


# também é possivel colocar listas dentro de listas
matriz = [[1,2], [3, 4], [5, 6]]
# a variavel matriz aponta para uma lista onde cada item também é uma lista, isso é conecido como matriz.

print(matriz[0][1])#acessando item 2

print(matriz[2][1])#acesando o item 6


