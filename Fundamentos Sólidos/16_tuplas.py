# o tipo tuple(tupla) é uma lista imutavel.
# é mais rapido do que uma lista em alguns casos pois não carrega muitos dos metodos que uma lista carrega

#criação
nomes = ("eduardo", "carlos", "joão")
print(f" tupla original: {nomes}")

#convertendo uma lista em tupla
lista_nomes = ["Ana", "vitoria", "beatriz"]
tupla_nomes = tuple(lista_nomes)
print(f" lista convertida em tupla {tupla_nomes}")

# o acesso é igual e lista
print(nomes[2])

# desempacotamento
nome1, nome2, nome3 = nomes
print(nome1)
print(nome2)
print(nome3)

# uma tupla com um unico elemento presisa de uma virgula no final
nome4 = ("unico",)

nome5 = ("unico") #não é uma tupla

print(type(nome4))
print(type(nome5))#não é tupla, é uma string