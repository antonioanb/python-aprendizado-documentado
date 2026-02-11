#exercicio - sistema de pertguntas

perguntas = [
    {
     "pergunta":"Quanto é 2 +2 ?",
     "op":["23", "4", "3", "6"],
     "resposta": 4
     },
    {
     "pergunta":"Quanto é 5  * 10 ?",
     "op":["100", "40", "200", "50"],
     "resposta": 50
     },
   
]

#variaveis declaradas
acertos = 0
erros = 0

#percorrendo dicionario
for pergunta in perguntas:
    print(f"Pergunta: {pergunta["pergunta"]}")
   
    #pegando as opções do dicionario
    for i, op in enumerate(pergunta["op"]):
        print(f"{i}) {op} ")
    escolha = input("resposta > ").strip()     
    print("-"*30) 
    
    if escolha == "":
        print("a resposta não pode ser vazia 😠 ")
        print("-"*30)
        erros += 1   
        continue
    escolha = int(escolha)
    #logica de acertos
    if escolha == pergunta["resposta"]:
        print("acertou ✅")
        print("-"*30)
        acertos += 1
    else:
        print("errou ❌")
        print("-"*30)
        erros += 1
        
#resultado
print(f"acertos: {acertos} ✅")
print(f"erros: {erros} ❌")