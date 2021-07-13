dados = open("teste.txt", "r", encoding="utf-8")
for texto in dados:
    linha = texto.strip('\n') 
    print(linha)