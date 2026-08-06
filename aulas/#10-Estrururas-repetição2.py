
#ESTRUTURA DE VALIDAÇÃO S/N
'''c = 0
rsp = 'S'
s = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}o. valor ==> '))
    s += n
    escolha = str(input('Você quer continuar? [S/N] '))
    
    if escolha == 'S':
        continue

    elif escolha == 'N':
        break

print(f'A soma de todos os valores digitados é {s}')'''
        
#CONTAR DE 1 ATE 10
'''
from time import sleep
for c in range(1, 11):
    print(c)
    sleep(1)'''

#TABUADA DE QUALQUER NÚMERO
'''
numero = int(input('NÚMERO: '))
print('-'*10)
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')
print('-'*10)'''

#Quantos números são negativos
'''
possitivo = 0
negativo = 0

for c in range(1, 6):
    num = int(input(f'Digite {c}o. valor: '))
    if num < 0:
        negativo += 1
    else:
        possitivo += 1

print(f'{negativo} negativos e {possitivo} possitivos')'''

#FATORIAL
'''
from math import factorial
opc = 'S'
while True:
    print('-'*30)
    num = int(input('Número pra calcular o fatorial: '))
    print('-'*30)

    print(num,end=' ')

    for c in range(num-1, 0, -1):
        num *= c
        print(f'x {c}', end = ' ')
    print(f'= {num}')

    while opc != 'S' or  opc != 'N':
        opc = str(input('Deseja continuar? [S/N] ')).upper()
        if opc == 'S':
            break
        if opc == 'N':
            print('saindo...')
            break
        else:
            print(f'Apenas S/N')
    if opc == 'N':
        break'''

#PRIMO?
'''p = 0
num = int(input('Número: '))
for c in range(1,num+1):
    d = num/c
    if d % 1 == 0:
        p += 1
if p == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')'''