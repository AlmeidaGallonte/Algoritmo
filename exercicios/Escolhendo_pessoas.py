resp1 = 0
resp2 = 0

while True:
    print('='*20)
    print('|       MENU       |')
    print('='*20)

    sexo = str(input('Qual o Sexo? [M/F] '))
    idade = int(input('Qual sua Idade? '))
    cor_cabelo = int(input('Qual a cor do Cabelo?\n====================\n[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo\n:'))
    cont = str(input('Quer continuar? [S/N] '))

    if sexo in 'Mm' and idade > 18 and cor_cabelo == 2:
        resp1 += 1 

    if sexo in 'Ff' and 25 <= idade <= 30 and cor_cabelo == 3:
        resp2 += 1

    if cont in 'Nn':
        print('='*20)
        print(f'Total de homens com mais de 18 e cabelos castanhos {resp1}')
        print(f'Total de mulheres entre 25 e 30 e cabelos loiros {resp2}')
        break