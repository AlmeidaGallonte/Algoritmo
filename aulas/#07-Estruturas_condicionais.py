#Estruturas condicionais
'''
exemplo real:
'se eu tiver dinheiro então vou fazer uma viagem pra disney' 

'''
#exemplo do scratch
"""" while True:
    escolha = str(input('Posso andar? [S/N] '))
    if escolha not in 'SN':
        print('Resposta invalída! [S/N]')
    else:
        if escolha == 'S':
            print('Andar')
            break
        if escolha == 'N':
            print('Não andar')
            break """

# exemplo visualg

'''escolha = int(input('quanto dinheiro? '))
if escolha >= 10000:
    print('Então vou viajar...Partiu Disney')
else:
    print('Então vou ficar em casa. #chateado')'''

'''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'Estamos em {ano_atual} e você tem {idade} anos.', end= ' ')
if idade >= 21:
    print('já esta na maior idade!')'''

#ímpar ou par
'''numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')'''

#calculo de IMC
'''
print('-'*25)
print('    CALCULO DE IMC')
print('-'*25)
altura = float(input('Altura (m): '))
peso = float(input('Peso (kg): '))
IMC = peso / (altura ** 2)
print('-'*25)
print(f'PESO: {peso}KG\nALTURA: {altura}M\nIMC: {IMC:.2f}')
print('-'*25)
print('  RESULTADO PRA ADULTOS')
print('-'*25)
if IMC < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= IMC <= 24.9:
    print('Peso normal (saudável).')
elif 25 <= IMC <= 29.9:
    print('Sobrepeso.')
elif 30 <= IMC <= 34.9:
    print('Obesidade grau I.')
elif 35 <= IMC <= 39.9:
    print('Obesidade grau II.')
else:
    print('Obesidade grau III (grave).')

print('-'*25)'''

