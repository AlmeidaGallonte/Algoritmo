print('-'*20)
print(' TABELA DE PARTIDAS')
print('-'*20)
times = []
for i in range(1,4):
    times.append(str(input(f'Nome do {i}o. time: ')))

print('-'*20)
print(' TABELA DE PARTIDAS')
print('-'*20)

for t in times:
    for v in times:
        if t == v:
            pass
        else:
            print(f'{t:10}[] x [] {v}')
print('-'*20)
