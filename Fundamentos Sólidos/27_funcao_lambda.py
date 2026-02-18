#exemplo simples de uma função que executa outra função
def executa(f,*args):
   return f(*args)
#----------------------------------------------------------

def soma(n1,n2):
   return n1 + n2


print(executa(soma, 2 ,4))


# outro exemplo: usando uma função lambda com a função 'executa'. 
# Uma função lambda normalmente é executada por outra função, mas isso não é uma regra.
print(executa(lambda n1, n2: n1 + n2, 5, 5))

#lambda n1, n2: n1 + n2 é a definição da função inteira em uma linnha
#ela não precisa de () nem da palavra return pois retorna automaticamente

