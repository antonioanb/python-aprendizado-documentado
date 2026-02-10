import copy

pessoa = {
    "nome":"Antonio",
    "sobrenome": "Barros",
    "idade": 30,
    #"profissao":"programador",
}

#metodos
print(pessoa.keys())#retorna um dict_keys com os nomes
print(pessoa.values())#retorna um dict_values com os valores
print(pessoa.items())#retorna um dict_items com os itens

print(pessoa.setdefault("profissao", 0))#caso não tiver essa chave no dict ele retorna 0 "ou qualquer coisa especificada", caso tenha ele não faz nada

#iterando o dicionario
for chave, valor in pessoa.items():
    print(f"chave -> {chave} - valor -> {valor}")
    
#explicação rapida sobre copia

pessoa2 = pessoa #faz pessoa2 apontar para o mesmo local da memoria que pessoa

pessoa2 = pessoa.copy()#(Shallow Copy)copia apenas os itens imutaveis, os mutaveis como listas são compartinhados pois aponta para o mesmo lugar na memoria

pessoa2 = pessoa.deepcopy()#usando o deepcopy do modulo copy faz uma copia completa, é a unica forma de fazer pessoa2 ser independente de pessoa.