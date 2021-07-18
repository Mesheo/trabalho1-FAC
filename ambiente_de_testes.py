
def leitura(nome_arquivo):
    dados = open(nome_arquivo, "r", encoding="utf-8")
    texto = []
    print(f'DADOS: {dados}\n')
    for informacao in dados:
        linha = informacao.strip('\n') 

        if linha != '':
            texto.append(linha)


    entradas = []
    for i in range(0, len(texto),2):
        entrada = []
        entrada.append(texto[i])
        entrada.append(texto[i+1])
        entradas.append(entrada)
    return entradas   


  


def main():
    entradas = leitura("teste.txt")
    for entrada in entradas:
        print(entrada)
main()