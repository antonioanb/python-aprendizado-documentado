# for(para cada) também é uma estutura de repetição, ele é muito usado para percorrer itaveis como strings ou listas.
# um item iteravel pode ser percorrido item a item pedaço por pedaço pelo for.

# uma string é um iteravel
iteravel = "Olá Mundo"

# for percorrendo um iteravel: 
# para cada repetição o iteravel entrega um item e coloca na variavel item
for item in iteravel:
    # assim cada volta item é uma letra do iteravel
    print(item)
    
    
# criando um contador com for e range()
# range é uma função que gera um iteravel de numeros especificados, no caso ele está gerando numeros de 1 a 10 pois o range não entrega o ultimo 

for numero in range(1, 11):
    print(numero)
 
# percorrendo listas
# uma lista é um conjunto de elementos indexados, como uma lista de compras

lista_de_compras = ["banana", "maçã", "leite", "uva", "arroz"]

# o for é perfeito para percorrer esse tipo de estrutura

# percorrendo uma lista de compras para encontra a "uva", depois de encontrar sai do for

for item in lista_de_compras:
    if item == "uva":
        print(f"{item} encontrado, parando...")
        break# sai do looo na hora
      

# usando continue: diferente de break que sai do loop o continue pula e volta atual e continua o loop
# exemplo voce quer exibir todos os numeros de uma lista mas quer pular o numero 3

numeros = [1,2,3,4,5]

for numero in numeros:
    if numero == 3:
        continue
    #  pode deixar o 3 nunca será exibido
    print(f"{numero}")