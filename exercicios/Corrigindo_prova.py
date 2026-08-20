from rich import print

gabarito = []
tempgabarito = []
totgabarito = []
Alunos = []
acerto = [0,0,0]
print('-'*25)
print('  GABRITO ORIGINAL')
print('-'*25)
for c in range(5):
    gabarito.append(str(input(f'Questão {c+1}: ')))

for a in range(3):
    print('-'*25)
    print(f'  ALUNO  {a+1}')
    print('-'*25)
    Alunos.append(str(input('Nome: ')))
   
    for q in range(5):
        tempgabarito.append(str(input(f'Questão {q+1}: ')))
    totgabarito.append(tempgabarito.copy())
    tempgabarito.clear()

for p, g in enumerate(totgabarito):
    for q in totgabarito[p]:
        if q == gabarito[p]:
            acerto[p] += 2

print('-'*25)
print('  GABRITO ORIGINAL')
print('-'*25)   
for p,a in enumerate(Alunos):
    print(f'{a:20} {acerto[p]:.1f}')
print('-'*25) 
print(f'Media da turma: {sum(acerto)/len(Alunos)}')  ;