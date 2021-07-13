comparador = 10000000000000000000000000000000 #tava usando muito esse número

def eh_negativo(numero):
    if str(numero)[0] == '1':
        return True
    else: 
        return False

def lendo_Arquivo(nome_do_Arquivo):
    dados = open(nome_do_Arquivo, "r", encoding="utf-8")
    linhas = []
    for texto in dados:
        linha = texto.strip('\n') 
        linhas.append(linha)
    return linhas

#conversor SM -> DEC - Funcionando pra todos os testes que eu tentei
def convSM_Dec(b):
  if eh_negativo(b): #checa se o número é negativo 
    return ((int(b,2)*-1)+2147483648) #retira o bit de sinal e retorna o número certo
  else:
    return int(b,2)

#soma SM - incompleto 1/4
def somaSM(a,b):
  if eh_negativo(a) and eh_negativo(b) or (int(a) < comparador and int(b) < comparador): #checa se ambos os números possuem o mesmo sinal
     #alerta! você entrou na zona da matemática gambiarra
     if int(a) > comparador: #checa se vai ser de negativos
       a = list(map(int,a))
       b = list(map(int,b))
       #print(a,b)
       #converte de volta pra lista de inteiros pq eu preciso disso pra fazer os cálculos
       resultado = [i for i in range(31)]
       for i in range(30, 0, -1):
         #print(resultado)
         if (a[i+1] + b[i+1]) == 0:
           resultado[i] = '0'
         elif(a[i+1] + b[i+1]) ==1:
           resultado[i] = '1'
         elif(a[i+1] + b[i+1]) ==2:
           resultado[i] = '0'
           a[i] = a[i] + 1
         else:
           resultado[i] = '1'
           a[i] = a[i] + 1
       resultado = list(map(str, resultado))
       resultado = "".join(resultado)
       return(resultado)
     else:
       print('igreja')
  else:
    print('pqp q xereca de cerol')
   

#subtração SM - incompleto
def subSM():
  pass

#conversor C2 -> DEC - Funcionando pra todos os testes que eu tentei
def convC2_Dec(b):
  if int(b) >= comparador: #checa se o número é negativo 
    b = list(b) #converte a string pra lista
    b = ['0' if i=='1' else '1' for i in b] #troca cada 0 por 1
    b = "".join(b) #converte a lista pra string
    return (((int(b,2))+1)*-1) #converte pra número inteiro, soma 1 e negativa(a ordem dos passos é alterada se comparada ao algoritmo mas o resultado matematicamente é o mesmo)
  else:
    return int(b,2)
  
#soma C2 - incompleto
def somaC2():
  pass

#subtração C2 - incompleto
def subC2():
  pass



#Pegando os inputs do arquivo
input1 = lendo_Arquivo('teste.txt')[0]
input2 = lendo_Arquivo('teste.txt')[1]

print(convSM_Dec(input1))
print(convSM_Dec(input2))
print(convC2_Dec(input1))
print(convC2_Dec(input2))
print(somaSM(input1, input2))

#números úteis pra teste
#10000000000000000000000000001011
#10000000000000000000000000000001
