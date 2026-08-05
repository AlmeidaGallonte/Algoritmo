time_casa = 'SÃO PAULO'
time_fora = 'SPORT'
print(f'     {time_casa} X {time_fora}')
print('-'*30)
gols_casa = int(input(f'Quantos gols do {time_casa}: '))
gols_fora = int(input(f'Quantos gols do {time_fora}: '))
dif = gols_casa - gols_fora
print('-'*30)
print('DIFERENÇA: ', abs(dif))
print('STATUS:', end=' ')
if abs(dif) >= 5:
    print('GOLEADA')
elif dif == 0:
    print('EMPATE')
else:
    print('NORMAL')
