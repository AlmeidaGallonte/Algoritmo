from datetime import date

ano_atual = date.today().year
print('-'*25)
print('DEPARTAMENTO DE TRANSITO')
print('-'*25)
ano_nasc = int(input('Ano de Nascimento (yyyy): '))
idade = ano_atual - ano_nasc
print('-'*8,'STATUS','-'*8)
print(f'IDADE: {idade} anos')
if idade < 18:
    print(f'INAPTO A TIRAR CARTEIRA')
else:
    print(f'APTO A TIRAR CARTEIRA')
print('-'*25)