numero = int(input('Digite um numero decimal para ser representado em outra base: '))
base = int(input('Digite a base desejada: '))

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

print(len(conversor_decBase(base,numero)))
#caso teste 6 na base binaria é 110