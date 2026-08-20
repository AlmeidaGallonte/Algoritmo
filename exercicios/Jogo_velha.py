from rich import print

tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]

while True:

    for c in range(3):
        for l in range(3):
            print(f'[{tabuleiro[c][l]}]',end=' ')
        print()

    jgd = int(input('Vai jogar (X) em qual posição: '))
    for c in range(3):
         for l in range(3):
             if jgd == tabuleiro[c][l]:
                 tabuleiro[c][l] = 'X'

    for c in range(3):
            for l in range(3):
                print(f'[{tabuleiro[c][l]}]',end=' ')
            print()

    jgd = int(input('Vai jogar (O) em qual posição: '))
    for c in range(3):
        for l in range(3):
            if jgd == tabuleiro[c][l]:
                tabuleiro[c][l] = 'O'

