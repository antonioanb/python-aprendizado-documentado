import m36_import#ao importar assim todos os escopos do outro modulo vem junto, e ficam guardados dentro do objeto m36_import

from m36_import import saudacao# trazendo apenas uma função especifica para omescopo atual

import pacote1.modulo1#importando de um pacote



#print("Está vindo do outro modulo") print vindo do outro moduilo executa automaticamente ao importar

#usando função do outro modulo, é preciso acessar ela pelo nome do modulo
print(m36_import.soma(10,10))

#usando função de outro modulo diretamente já que ela foi especificamente importada não precisa usar o nome do modulo
print(saudacao("Antonio"))


#um modulo só é carregado uma vez, das outras vezes ele fica salvo, se quiser recarregar deve usar:
#import importlib
#importlib.reload(m36_import)

subtracao = pacote1.modulo1.subtrair(4, 1)
print(f"função importada de um pacote {subtracao}")