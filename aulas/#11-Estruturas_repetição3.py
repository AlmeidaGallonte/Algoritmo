#FOR
#contar 1 a 10
'''for variavel in range(10,0,-1):
    print(variavel)'''

#pra repetiçoes limitadas

#números pares
'''valor = int(input('Digite um valor: '))
if valor%2 == 1:
    valor -= 1
for par in range(valor,0,-2):
    print(par)'''

#Quantos valore de 0 a 10
'''quais_valores = []
entr_0e10 = 0
soma_impar = 0
for c in range(0,6):
    numero = int(input('Digite um valor: '))
    if 0 <= numero <= 10:
        entr_0e10 += 1
        quais_valores.append(numero)
        if numero%2 == 1:
            soma_impar += numero
print(f'No total foram {entr_0e10} números entre 0 e 10 que foram {quais_valores} e a soma dos números impares digitados é {soma_impar}')'''

#Combinacões
'''for c1 in range(1,4):
    for c2 in range(1,4):
        print(c1, c2)'''


