#Prática (Soma)
'''def soma(a:int=0, b:int=0):
    s = a + b
    return s 

v1 = int(input('Digite o primeiro valor: '))
v2 =  int(input('Digite o segundo valor: '))
res = soma(v1, v2)

print(f'{v1} + {v2} = {res}')'''

#Prática (par/impar)
def parOUimpar(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

n = int(input('Digite um número: '))
resp = parOUimpar(n)
print(f'O número {n} é {resp}')

