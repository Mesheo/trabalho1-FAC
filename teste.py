

def somaBinaria(a,b): 

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

def oposto(bit):
    if bit == '0':
        return '1' 
    if bit == '1':
        return '0'

def conversor_binario_decimal(numero):
    numero_invertido = numero[::-1]
    resultado_decimal = 0

    for posicao in range(len(numero_invertido)):
        resultado_decimal += int(numero_invertido[posicao]) * (2**posicao)
        
    return (resultado_decimal)

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

def converter_C2_decimal(numero):
    sinal_numero = str(numero)[0:1:] #separa o primeiro numero da esquerda p direita
    resultado_decimal = ''

    if sinal_numero == '1':
        numero_C2 = negativo_C2(numero)

        resultado_decimal = f'-{conversor_binario_decimal(numero_C2)}'

        return resultado_decimal        

    if sinal_numero == '0':
        return conversor_binario_decimal(numero[1::])


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
      


  


def main():
    print(calculos_C2('0100', '0111', 'subtrair'))



main()