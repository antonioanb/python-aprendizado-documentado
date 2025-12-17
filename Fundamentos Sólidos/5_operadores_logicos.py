# operadores logicos são usados para criar condições mais inteligentes e complexas.

# em pyhton os tres principais são and, or e not

# ------------------------------------------------------
#and(E) é o mais exigente. ele só deixa o codigo entrar no bloco se todas as condições forem verdadeiras ao mesmo tempo

# exemplo, vamos imaginar que para entrar no cinema voce precise do ingresso e um documento, se faltar um voce não entra
ingresso = True
documento = True

if ingresso and documento:
    print("pode entrar no cinema 🍿")
else:
    print("algo está faltando, entrada proibida")
    
# ------------------------------------------------------
#or(ou), já o or deixa o codigo entrar se pelo menos uma das condições forem verdadeiras

#exemplo, para ganhar um desconto voce precisa ser estudante ou ter mais de 60 anos, se uma das duas condições forem verdadeiras o desconto é seu.

estudante = False
idoso = True

if estudante or idoso:
    print("voce tem direito ao desconto 💸")
else:
    print("sem direito ao desconto 😟")


# ------------------------------------------------------
# not(não/inversor) not é do contra se algo é True ele transforma em False e vice e versa

#exemplo, se não tiver chovendo eu vou para academia

chovendo = False

if not chovendo:
    print("indo treinar 💪🏼 ")
    
    
# exemplo usando tudo

#a pessoa só vai viajar se ela tiver dinheiro ou se for feriado ou final de semana

tem_dinheiro = True
feriado = False
final_de_semana = True

if tem_dinheiro and (feriado or final_de_semana):
    print(" vai viajar ")
    
#é possivel usar () para oorganizar as condições pois tudo que está entre parênteses é processado primeiro. 

# Tabela Verdade
# Operador      Regra Simples
#   and	      Só é True se tudo for verdade.
#   or	      É True se pelo menos um for verdade.
#   not	      Inverte: o que é verdade vira mentira e vice-versa.