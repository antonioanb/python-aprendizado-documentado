# os metodos de lista são ferramentas que o python oferece para manipular as listas.

nomes = ["antonio", "carlos", "gabriel"]

# ADICIONANDO elementos: existem duas formas de colocar novos itens na lista.

# .append() -> adiciona um item ao final da lista.
# o ptyhon cria um novo espaço no final da sequencia e aponta para o valor.
nomes.append("beatriz")

# .insert -> adiciona em um lugar especifico.
# diz: "no indice 0, aponte para esse valor", o python "empurra" todos para o lado para abrir espaço.
nomes.insert(1, "davi") 

print(nomes)

# REMOVENDO elementos

# .pop() -> Remove pelo índice (ou o último se vazio).
# É como tirar um livro da prateleira. Ele te "devolve" o valor.
removido = nomes.pop(1)# remove quem está no indice 1 e guarda na variavel "removido"
print(removido)

# .remove() -> remove pelo valor literal.
# o python percorre a lista, encontra o primeiro "gabriel" e deleta o ponteiro dele.
nomes.remove("gabriel")
print(nomes)


# .clear() -> limpa a lista inteira.
# todos os itens ficam sem ponteiros e a lista fica vazia.
# quando não tem nada apontando para um valor o Garbage Collector entra em ação.
nomes.clear()
print(nomes)# lista vazia

# ORGANIZANDO e CONSULTANDO

numeros = [5, 2, 9, 1]

# .sort() -> ordena a lista de forma crescente por padão, os indices são reatribuidos para apontar na ordem correta.
numeros.sort()
print(numeros)

# .index() -> pergunta: "em qual indice está o valor x ?"
posicao = numeros.index(5)# procura o valor 5 e diz o indice que ele está
print(posicao)

# .len() -> não é um metodo é uma função, mas diz o tamanho da lista
tamanho = len(numeros)
print(tamanho)

# obs, sort() e append() alteram a lista diretamente na memoria, eles não criam uma nova lista, eles mexem na mesma que a variavel está apontando.

























































