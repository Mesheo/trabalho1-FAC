
def leitura():
    dados = open("teste.txt", "r", encoding="utf-8")
    for texto in dados:
        linha = texto.strip('\n') 
    # print(linha)

def sub(a, b):
  a = list(map(int,a))
  b = list(map(int,b))
  resultado = []
  for i in range(len(a)-1, -1, -1):
    print(i)
    print(resultado)
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

print(sub('0000000000000000000000000001011', '0000000000000000000000000001010'))


#TESTE 1 ✅
#11100010
#11000000
#00100010 resposta do codigo
#00100010 resposta da calculadora



def soma(a,b): #CORRECTO

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


#TESTE 1 ✅
#1101
#1111
#11100 resposta do codigo
#11100 resposta da calculadora

#TESTE 2 ✅ 
#11110001
#11001111
#111000000 resposta do codigo
#111000000 resposta da calculadora

#TESTES 3 ✅
#11110000111100001111000010101011 
#11001100110011000000000000000000
#110111101101111001111000010101011 resposta do codigo
#110111101101111001111000010101011 resposta da calculadora

