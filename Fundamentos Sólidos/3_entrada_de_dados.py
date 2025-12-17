# para falar de entrada de dados precisa conhecer a função input()

# input é uma função que  entrada de dados que pausa a execução do programa e fica esperando o usuario digitar algo

idade = input("Qual é a sua idade ? ")

# tudo que vem do input() o python classifica como texto, então nesse caso se a pessoa responder 25 o python vẽ como "25" um texto, e uma operação como "25" + 1 vai dar erro.

# para resolver isso é preciso fazer conversão de tipos(Casting) que é trocar a "etiqueta" que o python coloca no valor para o tipo desejado.
idade_convertida = int(idade)

idade_somada = idade_convertida + 1

# print exibe um valor no terminal quando o codigo é executado
print(idade_somada)

