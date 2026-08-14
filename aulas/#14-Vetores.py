from rich import print,inspect
#Variavel simples
'''n1, n2, n3, n4 = 3, 5, 1, 0'''

#Variaveis composta homogêneas
'''n = [0,0,0,0]
n[0] = 3
n[1] = 5
n[2] = 1
n[3] = 0
print(n)'''

#Variaveis c. h. unidimencionais
'''v = [1,2,3,4]
print(v)
for i in range(4):
    v[i] = int(input(f'Valor pra n[{i}]: '))

for l in v:
    print(l,end=' ')'''

#pORimp
'''posicaoPar = []
tot_list = []
tot_imp = []
tot_par = []
for i in range(7):
    n = int(input(f'Digite o valor [{i}]: '))
    tot_list.append(n)
    if n%2 == 0:
        tot_par.append(n)
        posicaoPar.append(i)
    else:
        tot_imp.append(n)
print(f'Números totais foram {len(tot_list)} que são {tot_list}')
for p in tot_par:
    print(p,end=' ')
print()
for p in posicaoPar:
    print(f'POSIÇÃO: [red]{p}[/]',end=' ')
print()
print(f'Números Pares foram {len(tot_par)} que são {tot_par}')
print(f'"POSIÇOES" dos pares {posicaoPar}')
print(f'Números Ímpares foram {len(tot_imp)} que são {tot_imp}')'''

#Listagem de turma
'''nome = [0,0,0,0]
nt1 = [0,0,0,0]
nt2 = [0,0,0,0]
media = [0,0,0,0]
for i in range(4):
    nome[i] = str(input(f'ALUNO {i}\nNome: '))
    nt1[i] = float(input('Primeira Nota: '))
    nt2[i] = float(input('Segunda Nota: '))
    media[i] = (nt1[i] + nt2[i]) / 2
mediaT = sum(media) / 4
print('LISTAGEM DE ALUNOS')
print('-'*20)
print(f'A media da turma foi {mediaT}')
print('-'*20)
for i in range(4):
    if media[i] > mediaT:
        print(f'{nome[i]:15} [green]{media[i]}[/]')
    else:
         print(f'{nome[i]:15} {media[i]}')'''

#C?
'''seC = []
totc = 0
for c in range(10):
    nome = str(input('Digite seu nome: '))
    if nome[0].upper() == 'C':
        totc += 1
        seC.append(nome)
print('-'*20)
print('LISTAGEM DE "C"')
print(totc)
print('-'*20)

for c in range(len(seC)):
    print(seC[c])
print('-'*20)'''

#Ordenação do vetor
'''notas = [0,0,0,0]

for i in range(4):
    notas[i] = int(input('Digite um valor: '))

print(notas)
notas.sort(reverse=True)
print(notas)'''