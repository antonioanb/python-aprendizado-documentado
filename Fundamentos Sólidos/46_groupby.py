from itertools import groupby



alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

#os dados precisam estar ordenados para o groupby funcionar porque o groupby só olha o item atual e o anterior.
#sem a ordem criaria grupos repetidos.

#ordenando a lista de dicionarios por nota

def pegar_nota(aluno):
    return aluno["nota"]

alunos_ordenados = sorted(alunos, key=pegar_nota)
grupos = groupby(alunos_ordenados, key=pegar_nota)

for nota, grupos_de_alunos in grupos:
    print(nota)
    for aluno in grupos_de_alunos:
        print(aluno)

#o groupby aceita apenas dois parametros, o iteravel e a key que é uma função que define o criterio de agrupamento.

#A função que é passada no key é executada para cada item do iterável. O valor que essa função retorna é o que o groupby usa para decidir se deve criar um novo grupo ou continuar no atual.

#Se você tiver uma lista simples e já ordenada, não precisa do key:
letras = ["A", "A", "B", "B", "B", "C"]

for chave, grupo in groupby(letras):
    print(f" letra:{chave} _ repetição {len(list(grupo))} vezes")