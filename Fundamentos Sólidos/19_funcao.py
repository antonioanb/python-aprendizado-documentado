#função é um bloco de codigo que pode ser chamado para ser executado ao longo do codigo
#funções podem receber argumentos em seus parametros.

def ola():
    print("olá")
    
    
ola()#executando

#função que recebe um nome como argumento em seu parametro
def saudacao(nome):
    print(f"olá {nome}, tudo bem")
    
saudacao("Antonio")#executando

# uma função pode retornar um valor
def soma(a,b):
    resultado =  a + b
    return resultado#retorna o valor para quem chamou.

total = soma(2,5)#guardando o valor retornado em uma variavel
print(total)  
print(f"total da soma: {soma(10,20)}")#usando diretamente

#função com multiplos retornos
def operacoes(a,b):
    soma = a + b
    multiplicacao = a * b
    subtracao = a - b
    divisao = a / b
    return soma, multiplicacao, subtracao, divisao# retorna uma tupla

s, mult, sub, div = operacoes(20,50)#executando e desempacotando os retornos
print(f"-> a soma é: {s} -> a multiplicação é: {mult} -> a subtração é: {sub} -> a divisão é: {div} ")

#Parâmetros com VALORES PADRÃO
def saudacao(nome, mensagem="tudo bem"):
    print(f"Olá {nome}, {mensagem}?")

saudacao("Ana")  # Usa o valor padrão: "Olá Ana, tudo bem?"
saudacao("Pedro", "como vai")  # "Olá Pedro, como vai?"

# Funções devem fazer UMA coisa bem feita. Se uma função está fazendo muitas coisas diferentes, deve ser divida em funções menores.