from rich import print

#Prática (Soma)
'''def soma(a:int=0, b:int=0):
    s = a + b
    return s 

v1 = int(input('Digite o primeiro valor: '))
v2 =  int(input('Digite o segundo valor: '))
res = soma(v1, v2)

print(f'{v1} + {v2} = {res}')'''

#Prática (par/impar)
'''def parOUimpar(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

n = int(input('Digite um número: '))
resp = parOUimpar(n)
print(f'O número {n} é {resp}')'''

#Fatorial em função
'''def Fatorial(n):
    for c in range(n-1,0,-1):
        n *= c 
    return n 

v = int(input('Digite um número: '))
print(f'O valor de {v}! = {Fatorial(v)}')'''

#Fibonacci F.
'''def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

resultado = fib(10)
print(resultado)'''

#Função prontas
from rich import print
'''
site = 'CursoEmVídeo'
#le o tamanho da str
print(len(site))

#retorna a posição da parte da str escolhida
print(site[6])

#Modifica a string
#MAIUSCULA
print(site.upper())

#minuscila
print(site.lower())

#mostra a posição da string
print(site.find('Vídeo'))
print(site.index('Vídeo'))

#ASCII
#str pra int cd
print(ord('C'))
#int pra str cd
print(chr(65))'''

nome = str(input('Digite seu nome: '))
print(f'Total de letras do seu nome: {len(nome)}')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A ultima letra do seu nome é {nome[len(nome)-1]}')
print(f'Seu nome tem a letra A na posição {nome.upper().index('A')}')
print(f'O código da letra "A" é {ord('A')}')
print(f'A letra de código 65 é {chr(65)}')
print('E seu nome escrito ao contario é', end=' ')
for c in range(len(nome)-1, -1,-1):
    print(f'[red]{nome[c].upper()}[/]',end='')