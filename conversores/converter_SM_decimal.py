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