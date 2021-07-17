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