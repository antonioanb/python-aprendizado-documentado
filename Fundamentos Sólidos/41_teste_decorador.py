import time

def meu_decorador(funcao):
    #a fnção envelope abraça a original passada por parametro
    def envelope():
        print("___Inicio da execução___")
        inicio = time.time()

        funcao()#executa a função  orinal

        fim = time.time()
        print(f"Tempo total: {fim - inicio:.4} segundos")
        print("___Fim da execução___")
    return envelope


@meu_decorador#diz para o python passar carregar_dados como argumento para meu_decorador
def carregar_dados():
    time.sleep(1)
    print("Dados carregados com sucesso")

carregar_dados()#quando carregar_dados é chamada na verdade é envelope que está sendo chamada.