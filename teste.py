dados = open("teste.txt", "r", encoding="utf-8")
for texto in dados:
    linha = texto.strip('\n') 
    # print(linha)

numero = 10101111
magnitude = str(numero)[1::1]
print(magnitude)