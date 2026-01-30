#lista de compras com as opções de inserir apagar listas sair
import os

lista = []

while True:
    print("escolha uma opção: ")
    opcao = input("[i]Inserir, [a]Apagar, [l]Listar [s]Sair -> ").lower()
    
    if opcao == "i":
        os.system("clear")
        valor = input("adicione um item: ")
        lista.append(valor)
        
    elif opcao == "a":
     try:
       indice_apagar = int(input("digite um numero do index: "))
       del lista[indice_apagar]
     except ValueError:
       print("digite um numero valido")
     except IndexError:
         print("indice não existe na lista")
     except:
        print("Erro desconhencido.")
        
    elif opcao == "l":
        os.system("clear")
        for i,v in enumerate(lista):
            print(f"item {i} -> {v}")
    else:
        print("digite uma opção valida")
        
    if opcao == "s":
        print("Obrigado por usar, saindo .....")
        break