# desempacotando os valores de uma lista para as respectivas variaveis

nome1, nome2, nome3 = ["antonio", "carlos", "miguel"]

print(nome1)
print(nome2)
print(nome3)

# pegando um valor e omitindo o resto

nome4, *_, _ = ["dolglas", "sergio", "caio"] 
print(nome4)

# pegando um valor e colocando o resto em outra lista

nome5, *resto = ["davi", "rita", "leandro"] 

print(nome5)
print(resto)

