L1 = float(input('Lado_1: '))
L2 = float(input('Lado_2: '))
L3 = float(input('Lado_3: ')
           )
EQ = L1 == L2 == L3
ES = L1 != L2 != L3

if (L1 < L2 + L3) and (L2 < L1 + L3) and (L3 < L2 + L1):
    print('Os valores forman um triangulo', end=' ')
    if EQ:
        print('EQUILATERO!')
    elif ES:
        print('ESCALENO!')
    else:
        print('ISOCILES!')
else:
    print('Os valores não formam um triangulo!')