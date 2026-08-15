cadeiras = ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10']
for c in cadeiras:
    print(f'[ {c} ]', end='',)

print('\n')
while True:

    print('--'*35)
    escolha = str(input('CADEIRA: '))
    
    for p, c in enumerate(cadeiras):
        if escolha == cadeiras[p]:
            cadeiras[p] = '--'
        print(f'[ {cadeiras[p]} ]',end=' ')

    print('\n')
    print('--'*35)

    continua = str(input('\nContinua? [S/N]: '))

    if continua in 'Nn':
        print('fim das reservas.')
        break
     