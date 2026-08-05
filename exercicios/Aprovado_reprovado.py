def linha(l=25):
    return print('-'*l)
def titulo(txt:str = ''):
    print(' ',txt)

linha()
titulo('ESCOLA JAVALI CANSADO')
linha()
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2 
linha()
print(f'MÉDIA: {media:.1f}')
if media < 7:
    print('ALUNO REPROVADO')
else:
    print('ALUNO APROVADO')
    
linha()