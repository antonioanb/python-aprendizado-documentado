# desempacotamento de dicionario

pessoa = {
    "nome":"Antonio",
    "sobrenome":"Barros",
    
}

dados_pessoas = {
    "idade": "36",
    "profissão":"programador"
}

#desenpacotando as informação dos outros dicionarios em um dicionario
pessoa_completa = {**pessoa, **dados_pessoas, "genero":"masculino"}

print(pessoa_completa)


#kwargs = keyword arguments (argumentos nomeados)
#com kwargs a função pode receber chave e valor via argumentos nomeados
def mostra_argumentos(*args, **kwargs):
    #NÂO NOMEADOS VEM PARA ARGS
    for v in args:
        print(v)
    #PARAMETROS NOMEADOS VÃO PARA KWARGS
    #print(kwargs)#retorna um dicionario com chave e valor baseado nos argumentos nomeados
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostra_argumentos("python", "c++", nome="Eduardo, idade = 36",)
mostra_argumentos(**pessoa_completa)

#no exemplom eu desempacoto um dicionario em uma função
configuracoes = {
    "placa_mae": "ASUS TUF Gaming B550M",
    "processador": "AMD Ryzen 5 5600X",
    "memoria": "16 GB DDR4 3200MHz",
    "placa_de_video": "NVIDIA RTX 3060 12GB",
    "armazenamento": "SSD 1TB NVMe",
    "monitor": "LG 24'' 144Hz Full HD",
    "fonte": "Corsair 650W 80 Plus Bronze",
    "gabinete": "Cooler Master Q300L",
    "sistema": "Windows 11"
}

mostra_argumentos(**configuracoes)