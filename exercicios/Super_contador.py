while True:
    print('='*20)
    print('|       MENU       |')
    print('='*20)
    escolha = int(input('| [1] de 1 a 10 |\n| [2] de 1 a 10 |\n| [3] Sair      |\n====================\n:'))
    if escolha == 1:
        for c in range(1,11):
            print(c,end='...')
        print()
    if escolha == 2:
        for c in range(10,0,-1):
            print(c,end='...')
        print()
    if escolha == 3:
        print('Saindo...')
        break