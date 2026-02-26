import sys

#generator vs iteraveis:

# LISTA (Eager Evaluation): Aloca todos os elementos na memória imediatamente.
# Vantagem: Acesso aleatório via indices e reutilização dos dados.
lista = [n for n in range(1000)]

# GENERATOR (Lazy Evaluation): Gera um item por vez sob demanda (on-the-fly)..
# Vantagem: Consumo de memória constante, independente do volume de dados.
generator = (n for n in range(1000))

# Comparação de ocupação de memória (em bytes), inportando sys
print(f"Tamanho da Lista: {sys.getsizeof(lista)} bytes")
print(f"Tamanho do Generator: {sys.getsizeof(generator)} bytes")

print("---" * 10)


# O generator não armazena os dados, ele é um objeto iterável que "lembra" o último estado
print(f"Objeto Generator: {generator}")

# Ocultando a complexidade: next() consome o próximo valor e move o ponteiro adiante
print(next(generator)) # 0
print(next(generator)) # 1
print(next(generator)) # 2

#no iterator a lista está toda na memoria, já o generator fica esperando o valor ser requisitado para ele 

#percorendo com for, lembrando que o for já chama iter() para obter o iterator e depois chama next()  em loop para cada indentação, e encerra quando a exceção StopIteration aparece
for n in generator:
    print(n)