#decoradores
def criar_funcao(func):
    def interna(*args):
        for arg in args:
            checar_param(arg)
            resultado = func(*args)
        return resultado

    return interna

#ao usar @criar_funcao, esse função é passada para dentro da função decoradora e passa a ser a função interna
@criar_funcao
def inverte_str(texto):
    print(f"nome da função {inverte_str.__name__}")
    return texto[::-1]


def checar_param(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")
    


invertida = inverte_str("antonio")
print(invertida)