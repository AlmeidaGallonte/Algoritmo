def linha(l=25):
    return print('-'*l)
def titulo(txt:str = ''):
    print(' ',txt)

linha()
titulo('ESCOLA JAVALI CANSADO')
linha()
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media:float = (nota_1 + nota_2) / 2 
linha()
print(f'MÉDIA: {media:.1f}\nAPROVEITAMENTO:',end=' ')

if 9 <= media <= 10:
    print('A')
elif 8 <= media <= 8.9:
    print('B')
elif 7 <= media <= 7.9:
    print('C')
elif 6 <= media <= 6.9:
    print('D')
elif 5 <= media <= 5.9:
    print('E')
else:
    print('F')
    
linha()