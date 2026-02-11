d1 = {
    "nome": "Eduardo",
    "sobrenome":"Barros"
}

# get, ao em vez de usar [] para pegar um valor é possivel usar get

print(d1.get("idade", "não existe"))#dessa forma ele retorna um valor definido no segundo parametro para caso o valor não existir

#print(d1["idade"]) isso daria KeyError

#pop deleta uma chave e retorna o valor dela para uma variavel
nome = d1.pop("nome")
print(f"nome {nome} foi deletado do dicionario")

#também existe popitem() que faz deleta e retorna a ultima chave do dicionario

#update, atualiza valores de chaves no dicionario e criar novas chaves
d1.update( sobrenome = "andrade", profissao = "programador")
print(d1)

#update com tupla
tupla = ("nome", "Antonio"), ("ID", 213)
d1.update(tupla)
print(d1)