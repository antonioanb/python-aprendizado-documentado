# exemplo criando uma lista

lista1 = []

for numero in range(10):
    #criando pode inserir filtros ou calculos complexos
    lista1.append(numero)
print(lista1)

# fazendo o mesmo com list comprehension
# Sintaxe: [expressão for item in iterável]

list2 =[numero for numero in range(10)]
print(list2)

# O que está à esquerda do 'for' é o corpo do loop (o valor a ser inserido); 
# os [ ] já criam a lista e inserem os itens, dispensando o uso de .append(). porque o processo já está sendo feito dentro da lista.

