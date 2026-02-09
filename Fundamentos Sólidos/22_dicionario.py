#dicionarios são tipos de dados que tem itens, cada item tem uma chave e um valor associado a essa chave

# dicionario = {"chave":"valor"}

pessoa = {'nome':'antonio',
          'sobrenome':'barros',
          'idade': '35',
          'enderecos': [
              {'rua': 'vitoria', 'numero':110,},
              {'rua':"silva",'numero': 230},
          ]}
#pessoa = dict(nome="antonio", sobrenome="barros") outra forma de criar um dicionario, usando argumentos nomeados
#print(pessoa, type(pessoa), sep=" / ")

#pegando elementos especificos do dicionario
print(pessoa['nome'])
print(pessoa['idade'])


#crtiando uma chave dinamica
ch = "profissao"

pessoa[ch] = "Programador"

print(pessoa)

#deletando uma chave
del pessoa[ch]

                