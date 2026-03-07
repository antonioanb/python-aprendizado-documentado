#Crie uma função zipper (como o zipper de roupas)
#O trabalho dessa função será unir duas
#listas na ordem.
#Use todos os valores da menor lista.
#Ex.:
#['Salvador', 'Ubatuba', 'Belo Horizonte']
#['BA', 'SP', 'MG', 'RJ']
#Resultado
#[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


#def ziper(l1, l2):
#    menor_lista = min(len(l1), len(l2))
    
#    return [ (l1[i], l2[i]) for i in range(menor_lista)]



lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(lista1, lista2)))