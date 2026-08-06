print('-'*20)
print('     POLI VALENTE')
print('-'*20)

maior = 0
nome_maior = ''

for a in range(1, int(input('Quantos alunos a turma tem? '))+1):

    print('-'*20)
    print(f'ALUNO {a}')
    nome = str(input('NOME: '))
    nota = float(input(f'NOTA de {nome}: '))
    if nota > maior:
        maior = nota
        nome_maior = nome

print('-'*20)
print(f'O melhor aproveitamento foi de {nome_maior} com a nota {maior}')


    
