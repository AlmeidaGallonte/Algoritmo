from rich import print

matriz = [[],[],[],[]]

for c in range(4):
    for l in range(4):
        n = int(input(f'Digite valor pra posição [{c+1}:{l+1}]: '))
        matriz[c].insert(l, n)
print()

while True:
    print()
    c = int(input('MENUS MATRIZ\n==============\n[1] Mostrar a matriz\n[2]Diagonal Principal\n[3]Triangulo Superior\n[4]Triangulo Inferio\n[5]sair\n===== OPÇÃO: '))
    print()
    if c == 1:
        for c in range(4):
            for l in range(4):
                print(f'{matriz[c][l]:5}',end= ' ')
            print()

    elif c == 2:
        for c in range(4):
            for l in range(4):
                if c == l:
                    print(f'{matriz[c][l]:5}',end= ' ')
                else:
                    print(f'     ',end= ' ')
            print()
            
    elif c == 3:
        for c in range(4):
            for l in range(4):
                if c < l:
                    print(f'{matriz[c][l]:5}',end= ' ')
                else:
                    print(f'     ',end= ' ')
            print()  
    elif c == 4:
        for c in range(4):
            for l in range(4):
                if c > l:
                    print(f'{matriz[c][l]:5}',end= ' ')
                else:
                    print(f'     ',end= ' ')
            print()
    elif c == 5:
        print('Finalizando sistema matriz...')
        break