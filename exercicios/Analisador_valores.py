Svalores = 0
D5valor = 0
nulos = 0
Spar = 0

for c in range(1, 6):
    valor = int(input(f'Digite o {c}o. Valor: '))
    Svalores += valor
    if valor != 0:
        nulos += 1
    if valor % 5 == 0:
        D5valor += 1
    if valor % 2 == 0:
        Spar += valor

media = Svalores / 5

print(f'A soma entre os valores é {Svalores}\nA média entre os valores é {media}\nValores divisiveis por cinco é {D5valor}\nValores nulos é {nulos}\nA soma dos valores pares é {Spar}')