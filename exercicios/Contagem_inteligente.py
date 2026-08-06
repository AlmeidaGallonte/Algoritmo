
print('CONTAGEM INTELIGENTE')
print('-'*20)

a = int(input('Inicio: '))-1
b = int(input('Fim: '))

print('-'*20)
print('C O N T A D O R')
print('-'*20)

while a != b :
    if a > b:
        a -= 1
    elif b > a:
        a += 1
    print(a,end = '... ')