# Os operadores de comparação são os símbolos que usamos para fazer as "perguntas" ao Python dentro do if. O resultado de qualquer comparação é sempre um valor booleano (True ou False). 

# Operador	Nome	                 O que ele pergunta?	                              Exemplo
#   ==	    Igual a	           O valor da esquerda é igual ao da direita?	            5 == 5 (True)
#   !=	    Diferente de       Os valores são diferentes?	                            5 != 3 (True)
#   >	    Maior que	       O da esquerda é maior que o da direita?	                > 5 (True)
#   <	    Menor que	       O da esquerda é menor que o da direita?	                3 < 8 (True)
#   >=	    Maior ou igual	   É maior ou pelo menos igual?	                            10 >= 10 (True)
#   <=	    Menor ou igual	   É menor ou no máximo igual?	                            5 <= 10 (True)

#---------------------
# exemplo de  "Igual a",  codigo verifica se o admim digitado pelo usuario é igual ao do sistema, se for o usuario entra

admin_digitado = input("Digite o admin: ")
admin_sistema = "master"

if admin_digitado == admin_sistema:
    print("ENTROU ✅")
else:
    print("Nome não são iguais ❌")
    
#------------------------
#exemplo de Maior que, pergunta se a temperatura é maior que 37, se sim está com febre

temperatura =  float(input("qual a sua temperatura ?: "))

if temperatura > 37:
    print("está com febre 🤒 ")
else:
    print("está normal 😀 ")
    
#------------------------
#exemplo de maior ou igual, vaga só suporta 9 pessoas ele barra se o numero de pessoas for 9 ou maior
pessoas = int(input("digite o numero de pessoas"))
vagas = 9

if pessoas >= vagas:
    print("vagas cheias")
else:
    print("ainda tem vagas")  
    