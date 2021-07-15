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

def subtracao_SM(numero1, numero2):
    #separando as magnitudes 
    magnitude_numero1 = str(numero1)[1::1]
    magnitude_numero2 = str(numero2)[1::1]

    #declarando a magnitude da resposta
    magnitude_resultado = 0
    
    #separando os sinais
    sinal_numero1 = str(numero1)[0:1:1]
    sinal_numero2 = str(numero2)[0:1:1]
    
    #declarando o sinal da resposta
    sinal_resultado = 0

    #resultado onde iremos juntar o sinal resposta com a magnitude resposta 
    resultado = ''


    #comparador para fazer a soma, caso sejam de sinais iguais, ou prosseguir para a subtracao
    if sinal_numero1 == sinal_numero2:
        magnitude_resultado = somaBinaria(magnitude_numero1 + magnitude_numero2)
        resultado = int(str(sinal) + str(magnitude_resultado)) 
    else:
        if conversor_decimal(str(magnitude_numero1)) > conversor_decimal(str(magnitude_numero2)):
            magnitude_resultado = subtracaoBinario(magnitude_numero1 - magnitude_numero2) ❌
            sinal = sinal_numero1
        else: 
            sinal = sinal_numero2
            magnitude_resultado = subtracaoBinario(magnitude_numero2 - magnitude_numero1) ❌

    #juncao do sinal resposta com a magnitude da resposta
    resultado = int(str(sinal) + str(magnitude_resultado))

    #Checando se aconteceu overflow
    if len(resultado) >= 9: 
        raise Exception("Sorry, you reached Overflow!")
    
