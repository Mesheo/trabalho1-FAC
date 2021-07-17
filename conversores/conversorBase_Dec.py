numero = str(input('Digite um numero para ser convertido para base10: '))
base = int(input('Digite a base numerica: '))

def conversor_decimal(base, numero):
    numero_invertido = numero[::-1]
    resultado_decimal = 0

    for posicao in range(len(numero_invertido)):
        resultado_decimal += int(numero_invertido[posicao]) * (base**posicao)
        
    return (resultado_decimal)


print(conversor_decimal(base, numero))

# if __name__ == '__main__' :
#     conversor_decimal()

#caso teste: 101001001 na base 2 saida esperada 329