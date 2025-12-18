# while é uma estrutura de repetição(loop), ele é como um if que não desiste de executar um bloco de codigo enquanto a condição for verdadeira.

contador = 1#variavel para controlar a repetição

while contador <=5:
    #enquanto contador for menor ou igual a 5 ele repete o bloco e volta para verificar a condição.
    print(contador)
    #é preciso mudar o valor da condição usando a variavel de controle somando 1 a cada repetição, se não o contador sempre vai ser 1 e o while vai ficar repetindo para sempre.
    contador = contador +1

#Sempre certifique-se de que algo dentro do bloco vai eventualmente tornar a condição falsa, se não vai entrar em loop infinito repetindo até o computador travar ou o codigo for encerrado manualmente.

#while é otimo para validar entradas, Exemplo: obrigar o usuario a digitar a senha correta para continuar

senha_correta = "1234"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("difgite a senha para entrar: ")
   
    if tentativa != senha_correta:
        print("senha errada!, tente novamente")

print("Acesso concedido !")    
    