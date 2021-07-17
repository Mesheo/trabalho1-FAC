
def leitura(nome_arquivo):
    dados = open(nome_arquivo, "r", encoding="utf-8")
    linhas = []
    for texto in dados:
        linha = texto.strip('\n') 
        linhas.append(linha)
    return linhas      
 
def converter_SM_decimal(numero1):
    magnitude_numero = str(numero1)[1::1]

    sinal_numero = str(numero1)[0:1:]

    numero_decimal = conversor_binario_decimal(magnitude_numero)
    sinal = ''
    
    resultado_decimal = ''

    if sinal_numero == '0':
        sinal = ''
    elif sinal_numero == '1':
        sinal = '-'

    resultado_decimal = f'{sinal}{numero_decimal}'
    return resultado_decimal

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

def somaBinaria(a,b): #CORRECTO

  a = list(map(int,a))
  b = list(map(int,b))
  resultado = []
  for i in range(len(a)-1, -1, -1):
         #print(resultado)
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

def calculos_SM(numero1, numero2):
    #separando as magnitudes 
    magnitude_numero1 = str(numero1)[1::1]
    magnitude_numero2 = str(numero2)[1::1]
    print(f'Magnitude 1: {magnitude_numero1}')
    print(f'Magnitude 2: {magnitude_numero2}')
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
        sinal_resultado = sinal_numero1
        magnitude_resultado = somaBinaria(magnitude_numero1, magnitude_numero2)
    else:
        print('CHEGUEI')
        if (conversor_decimal((magnitude_numero1)) > conversor_decimal((magnitude_numero2))):
            magnitude_resultado = subtracaoBinaria(magnitude_numero1, magnitude_numero2) 
            sinal_resultado = sinal_numero1
        else: 
            sinal_resultado = sinal_numero2
            magnitude_resultado = subtracaoBinaria(magnitude_numero2, magnitude_numero1) 

    #juncao do sinal resposta com a magnitude da resposta
    resultado = f'{sinal_resultado}{magnitude_resultado}'

    #Checando se aconteceu overflow
    if len(resultado) >= 33: 
        raise Exception("Sorry, you reached Overflow!")
    
    return resultado
    

def main():
    #ler arquivo de 2 em 2 ✅
    input = leitura('teste.txt')
    print(f'input1: {input[0]}')
    print(f'input2: {input[1]}')

    #representar os valores na base 10 usando a logica de SM ✅
    print('\n', end='')
    print(converter_SM_decimal(input[0]))
    print(converter_SM_decimal(input[1]))

    #Realizar as operações de soma e subtração dos valores como sinal e magnitude, 
    calculo = calculos_SM('10000000000000000000000000001011', '00000000000000000000000000001010') #111010
    print(calculo)

    # Realizar as operações de soma e subtração na base 10.

main()