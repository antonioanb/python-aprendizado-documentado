# if(se) é uma estrutura condicional, ele faz o python executar um codigo caso a condição seja verdadeira.

idade = 18


if idade >= 18:
    print("maior de idade 🧔🏻")

#no codigo acima o print("maior de idade 🧔🏻") só vai executar se a idade for maior ou igual a 18, se não for ele pula o bloco do if.

# para deixar mais completo temos o else(se não), o else só existe depois do if, pois se a condição do if for falso ele executa o else.

else:
    print("menor de idade 🧒🏻")
    



# elif (senão se): É o intermediário.
# Serve para testar uma nova condição caso a anterior tenha sido falsa.
# exemplo mais completo.

nota = int(input("Qual sua nota? "))

if nota >= 9:
    print("Excelente! 🏆")
elif nota >= 7:
    # O Python só chega aqui se a nota for menor que 9.
    print("Você passou! ✅")
elif nota >= 5:
    # O Python só chega aqui se a nota for menor que 7.
    print("Exame final... 📝")
else:
    # Se não for nenhuma das opções acima.
    print("Reprovado. ❌")

# o else é sempre o ultimo
