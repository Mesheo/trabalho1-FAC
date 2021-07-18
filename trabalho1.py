
def leitura(nome_arquivo):
    dados = open(nome_arquivo, "r", encoding="utf-8")
    linhas = []
    for texto in dados:
        linha = texto.strip('\n') 
        linhas.append(linha)
    return linhas      

def oposto(bit):
    if bit == '0':
        return '1' 
    if bit == '1':
        return '0'

def converter_SM_decimal(numero):

    magnitude_numero = str(numero)[1::1]

    sinal_numero = str(numero)[0:1:]

    numero_decimal = conversor_binario_decimal(magnitude_numero)
    sinal = ''
    
    resultado_decimal = ''

    if sinal_numero == '0':
        sinal = ''
    elif sinal_numero == '1':
        sinal = '-'

    resultado_decimal = f'{sinal}{numero_decimal}'
    return resultado_decimal

def converter_C2_decimal(numero):
    sinal_numero = str(numero)[0:1:] #separa o primeiro numero da esquerda p direita
    resultado_decimal = ''

    if sinal_numero == '1': 
        bits_invertidos = []
        for posicao in range(len(numero)):
            bits_invertidos.append(oposto(numero[posicao]))
        
        acrescimo1 = '' #criando o numero binario equivalente pra ser somado
        for i in range(len(numero)-1):
            acrescimo1 += '0'
        acrescimo1 += '1'

        numero = ''.join(bits_invertidos)
        numero_C2 = somaBinaria(numero, acrescimo1)

        resultado_decimal = f'-{conversor_binario_decimal(numero_C2)}'

        return resultado_decimal        

    if sinal_numero == '0':
        return conversor_binario_decimal(numero[1::])

def conversor_binario_decimal(numero):
    numero_invertido = numero[::-1]
    resultado_decimal = 0

    for posicao in range(len(numero_invertido)):
        resultado_decimal += int(numero_invertido[posicao]) * (2**posicao)
        
    return (resultado_decimal)

def conversor_decimal(numero):
    numero_invertido = numero[::-1]
    resultado_decimal = 0

    for posicao in range(len(numero_invertido)):
        resultado_decimal += int(numero_invertido[posicao]) * (2**posicao)
        
    return (resultado_decimal)

def conversor_decBase(base, numero):

    resultado = []

    dividendo = numero
    quociente = dividendo//base
    resto = dividendo%base

    while quociente != 1:
        resto = dividendo%base
        quociente = dividendo//base
        dividendo = quociente
        resultado.append(resto)

    resultado.append(quociente)

    return resultado[::-1]

def subtracaoBinaria(a, b):
    a = list(map(int,a))
    b = list(map(int,b))
    resultado = []
    for i in range(len(a)-1, -1, -1):
        if(a[i] - b[i]) == -1:
            resultado.insert(0, '1')
            a[i-1] = a[i-1] - 1
        elif(a[i] - b[i]) == 1:
            resultado.insert(0, '1')
        elif(a[i] - b[i]) == -2:
            if(i==0):
                resultado.insert(0,'0')
                resultado.insert(0,'1')
            else:
                a[i-1] = a[i-1] -1
                resultado.insert(0, '0')
        else: #caso 0
            resultado.insert(0, '0') 

    resultado = list(map(str, resultado))
    resultado = "".join(resultado)
    return(resultado)

def somaBinaria(a,b): 

    a = list(map(int,a))
    b = list(map(int,b))
    resultado = []
    for i in range(len(a)-1, -1, -1):
        if (a[i] + b[i]) == 0:
            resultado.insert(0,'0')
        elif(a[i] + b[i]) ==1:
            resultado.insert(0,'1')
        elif(a[i] + b[i]) ==2:
            if (i == 0):
                resultado.insert(0, '0')
                resultado.insert(0,'1')
            else:
                resultado.insert(0,'0')
                a[i-1] = a[i-1] + 1
        else: #caso 3
            if(i==0):
                resultado.insert(0,'1')
                resultado.insert(0,'1')
            else:
                resultado.insert(0,'1')
                a[i-1] = a[i-1] + 1

    resultado = list(map(str, resultado))
    resultado = "".join(resultado)
    return(resultado)

def calculos_SM(numero1, numero2, operacao):
    #separando as magnitudes 
    magnitude_numero1 = str(numero1)[1::1]
    magnitude_numero2 = str(numero2)[1::1]

    sinal_numero1 = str(numero1)[0:1:1]
    sinal_numero2 = str(numero2)[0:1:1]
    
    if operacao == 'subtrair': #inverte o sinal
        sinal_numero1 = oposto(sinal_numero1)

    #declarando a magnitude da resposta
    magnitude_resultado = ''

    #declarando o sinal da resposta
    sinal_resultado = ''

    #resultado onde iremos juntar o sinal resposta com a magnitude resposta 
    resultado = ''

    #comparador para fazer a soma, caso sejam de sinais iguais, ou prosseguir para a subtracao
    if sinal_numero1 == sinal_numero2:
        sinal_resultado = sinal_numero1
        magnitude_resultado = somaBinaria(magnitude_numero1, magnitude_numero2)
    else:
        if (conversor_decimal((magnitude_numero1)) > conversor_decimal((magnitude_numero2))):
            magnitude_resultado = subtracaoBinaria(magnitude_numero1, magnitude_numero2) 
            sinal_resultado = sinal_numero1
        else: 
            sinal_resultado = sinal_numero2
            magnitude_resultado = subtracaoBinaria(magnitude_numero2, magnitude_numero1) 

    #juncao do sinal resposta com a magnitude da resposta
    resultado = f'{sinal_resultado}{magnitude_resultado}'

    #Checando se aconteceu overflow
    # if len(resultado) >= 33: 
    #     raise Exception("Sorry, you reached Overflow!")
    
    return resultado

def calculos_C2(numero1, numero2, operacao):
    if operacao == 'subtrair':
        numero2 = negativo_C2(numero2)

        soma_overflow = somaBinaria(numero1, numero2)
        soma_trim = []


        i = len(soma_overflow) -1
        while len(soma_trim) < len(numero1):
            soma_trim.append(soma_overflow[i])
            i -= 1

        resultado_binario = ''.join(soma_trim)[::-1]
        return resultado_binario
    
    if operacao == 'somar' :
        soma_overflow = somaBinaria(numero1, numero2)
        soma_trim = []


        i = len(soma_overflow) -1
        while len(soma_trim) < len(numero1):
            soma_trim.append(soma_overflow[i])
            i -= 1
        
        resultado_binario = ''.join(soma_trim)[::-1]
        return resultado_binario

def negativo_C2(numero):
    bits_invertidos = []
    for posicao in range(len(numero)):
        bits_invertidos.append(oposto(numero[posicao]))
    
    acrescimo1 = '' #criando o numero binario equivalente pra ser somado
    for i in range(len(numero)-1):
        acrescimo1 += '0'
    acrescimo1 += '1'

    numero = ''.join(bits_invertidos)
    numero_C2 = somaBinaria(numero, acrescimo1)

    return numero_C2

def main():
    #ler arquivo de 2 em 2 ✅
    import sys
    nome_do_arquivo = sys.argv[1]
    input = leitura(nome_do_arquivo)
    print('Exemplo de entrada: \n')
    print(f'{input[0]}')
    print(f'{input[1]}')

    #representar os valores na base 10 usando a logica de SM ✅
    print('\n', end='')
    print('Exemplo de saída: \n')
    print(converter_SM_decimal(input[0]))
    print(converter_SM_decimal(input[1]))
    print('\n', end='')

    #Realizar as operações de soma e subtração dos valores como sinal e magnitude ✅
    soma_SM = calculos_SM(input[0], input[1], 'somar') 
    subtracao_SM = calculos_SM(input[0], input[1],'subtrair') 
    print(soma_SM)
    print(subtracao_SM)
    print('\n', end='')

    #Realizar as operações de soma e subtração na base 10. ✅
    soma = int(converter_SM_decimal(input[0])) + int(converter_SM_decimal(input[1]))
    subtracao = int(converter_SM_decimal(input[0])) - int(converter_SM_decimal(input[1]))
    print(soma)
    print(subtracao)
    print('\n', end='')

    #Representacao em complemento a 2 ✅
    print(converter_C2_decimal(input[0]))
    print(converter_C2_decimal(input[1]))
    print('\n', end='')

    #Realizar as operações de soma e subtração dos valores como sinal e magnitude ✅
    soma_C2 = calculos_C2(input[0], input[1] , 'somar')
    subtracao_C2 = calculos_C2(input[0], input[1], 'subtrair')
    print(soma_C2)
    print(subtracao_C2)
    print('\n', end='')

    #Realizar as operações de soma e subtração na base 10. ✅
    soma1 = int(converter_C2_decimal(input[0])) + int(converter_C2_decimal(input[1]))
    subtracao1 = int(converter_C2_decimal(input[0])) - int(converter_C2_decimal(input[1]))
    print(soma1)
    print(subtracao1)
    print('\n', end='')

main()