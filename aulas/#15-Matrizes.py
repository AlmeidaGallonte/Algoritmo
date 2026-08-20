#variaveis compostas pt2
#mais dimensões
'''m = [[], []]

for c in range(2):
    for l in range(3):
        m[c].insert(l,int(input(f'Número da Posição [{l+1}:{c+1}]: ')))

for l in range(3):
    for p,c in enumerate(m):     
        print(f'{m[p][l]:5}',end=' ')
    print()'''

#valores pares em uma matriz 3x3
'''from random import randint
from rich import print
m =[[],[],[]]
par = []

for p,c in enumerate(m):
    for l in range(3):
        n = randint(0, 20)
        m[p].append(n)
        if n % 2 == 0:
            par.append(n)

print()
for l in range(3):
    for c in range(3):
        if m[l][c] % 2 == 0:
            print(f'[yellow]{m[l][c]:6}[/]',end=' ')
        else:
            print(f'{m[l][c]:6}',end=' ')
    print()
print()
print(f'[yellow]{len(par)}[/] pares')'''

#Matriz identidade de 3a ordem
'''mID = [[],[],[],[],[]]

ORD = 5
for l in range(ORD):
    for c in range(ORD):
        if l == c:
            mID[c].insert(l,1)
        else:
            mID[c].insert(l,0)
print()
for l in range(ORD):
    for c in range(ORD):
        print(f'{mID[l][c]:6}',end=' ')
    print()
print()'''

#Matriz de ordem 4
from random import randint
import math

m = [[],[],[],[]]
Sdig = []
Pl2 = []
maiorC3 = 0

for c in range(4):
    for l in range(len(m)):
        n = randint(0,20)
        m[c].insert(l,n)
        if l == c:
            Sdig.append(n)
        if c == 1:
            Pl2.append(n)
        if l == 2:
            if n > maiorC3:
                maiorC3 = n 


print()
for l in range(4):
    for c in range(4):
        print(f'{m[l][c]:6}',end=' ')
    print()
print()

print(f'A soma dos valores da Diagonal principal é {sum(Sdig)}')
print(f'O produto dos números da linha 2 é {math.prod(Pl2)}')
print(f'O maior valor da coluna 3 é {maiorC3}')
