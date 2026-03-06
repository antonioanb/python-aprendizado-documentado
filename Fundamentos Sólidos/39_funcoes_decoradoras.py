# função decoradora
def criar_funcao(func):
    def interna(*args):
        for arg in args:
            checar_param(arg)
            resultado = func(*args)
        return resultado

    return interna


def inverte_str(str):
    return str[::-1]


def checar_param(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")
    

inverte_str_checar_param = criar_funcao(inverte_str)
invertida = inverte_str_checar_param("antonio")
print(invertida)