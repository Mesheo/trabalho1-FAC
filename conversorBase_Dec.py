numero = str(input('Digite um numero para ser convertido para base10: '))
base = int(input('Digite a base numerica: '))

def conversor_decimal(base, numero):
    numero_invertido = numero[::-1]
    resultado_decimal = 0

    for posicao in range(len(numero_invertido)):
        resultado_decimal += int(numero_invertido[posicao]) * (base**posicao)

    print(f'Esse numero na base 10 é {resultado_decimal}')
    return None

conversor_decimal(base, numero)

#caso teste: 101001001 na base 2 saida esperada 329