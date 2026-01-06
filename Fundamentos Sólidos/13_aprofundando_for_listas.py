# o for percorre uma lista pegando item por item na lista, depois faz uma "etiqueta" chamada variavel de controle apontar para o item temporariamente.

frutas = ["maçã", "banana", "abacaxi", "laranja"]

for fruta in frutas:
    print(fruta)

# aqui a variavel temporaria fruta do for é a variavel de controle, ela aponta para cada item a cada iteração.


# pegando o indice, as vezes é preciso obter o indece dos item percorridos, pra isso se usa enumerate(), ele retorna o indice e o valor de cada item.

# pra isso é preciso ter duas variaveis de controle, uma para receber o index e outra para o  valor
for index, fruta in enumerate(frutas):
    print(f"indice: {index} -> {fruta}")

