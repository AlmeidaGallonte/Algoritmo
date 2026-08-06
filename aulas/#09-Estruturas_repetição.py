#estrutura de contagem
'''for mao in range(10,-1,-1):
    print(f'{mao}')'''

'''from time import sleep
mao = 10
while mao >= 0:
    sleep(0.9)
    print(mao)
    mao -= 1
print('Terminei de contar')'''

'''from time import sleep
for contador in range(0,int(input('0 até : '))+1,int(input('Qual o valor do salto: '))):
    sleep(0.9)
    print(contador)'''

#CRONOMETRO
'''from time import sleep

h = int(input('Cronometrar quanto tempo(h): ')) 
m = int(input('Cronometrar quanto tempo(m): ')) 
s = int(input('Cronometrar quanto tempo(s): '))

temp = (h * 3600) + (m * 60) + s

print(f'CRONOMETRAR: {h}:{m}:{s}')

while temp != -2:
    print(f'{h}:{m}:{s}')
    temp -= 1
    s -= 1
    sleep(0.000001)
    if s <= 0:
        if m > 0:
            m -= 1
            s = 60
    if m <= 0:
        if h > 0:
            h -= 1
            m = 60'''

#SOMADOR NUMERICO
'''
soma = 0

for l in range(1,11):
    numero = int(input(f'[{l}] NÚMERO: '))
    soma += numero
print(f'A soma de todos os números digitados foi {soma}')'''

#MAIOR
'''
soma = 0
maior = 0
for l in range(1,11):
    numero = int(input(f'[{l}] NÚMERO: '))
    soma += numero
    if maior < numero:
        maior = numero
print(f'A soma de todos os números digitados foi {soma} e o maior número foi {maior}')'''

#CONVERSÃO DE MOEDAS
'''for c in range(int(input('Quantas vezes deseja converter? '))):
    reais = float(input('Valor em reais: R$'))
    dolar = reais / 5.15
    print(f'R${reais:.2f} = US${dolar:.2f}')'''
