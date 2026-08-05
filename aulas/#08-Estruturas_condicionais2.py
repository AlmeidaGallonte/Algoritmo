#CONDICIONAL ANINHADA
'''dinheiro = int(input('Quanto você tem? '))

if dinheiro >= 10_000:
    print('Partiu Disney')

elif 5_000 <= dinheiro <= 10_000 :
    print('Visitar família')

else:
    print('#chateado')'''

'''nota_1 = float(input('NOTA 1: '))
nota_2 = float(input('NOTA 2: '))

media = (nota_2+nota_1) / 2
print(f'A média foi de {media:.2f}\nSITUAÇÃO ALUNO:',end=' ')
if media >= 7:
    print('APROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')'''

#IMC
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
    print('     Abaixo do peso.')
elif 18.5 <= IMC <= 24.9:
    print('     Peso normal (saudável).')
elif 25 <= IMC <= 29.9:
    print('     Sobrepeso.')
elif 30 <= IMC <= 34.9:
    print('     Obesidade grau I.')
elif 35 <= IMC <= 39.9:
    print('     Obesidade grau II.')
else:
    print('   Obesidade grau III (grave).')

print('-'*25)'''

#CRIANÇA ESPERANÇA
'''while True:
    print('-'*20)
    print(' CRIANÇA ESPERANÇA')
    print('-'*20)

    escolha = int(input('[1] doar R$10\n[2] doar R$25\n[3] doar R$50\n[4] outros valores\n[5] cancelar\n: '))

    print('-'*20)

    if escolha == 1:
        print('DOATES R$10')
    elif escolha == 2:
        print('DOATES R$25')
    elif escolha == 3:
        print('DOATES R$50')
    elif escolha == 4:
        valor_doar = float(input('Valor da doação: R$'))
        print(f'DOATES R${valor_doar:.2f}')
    elif escolha == 5:
        print('Operação cancelada...')
        break
    else:
        print('ERRO:Resposta invaída. tente novamente')'''

#QUANTIDADE DE DEPENDENTES DE UM FUNCIONÁRIO

'''nome = str(input('NOME: '))
salario = float(input('SALARIO: R$'))
dependentes = int(input('DEPENDENTES: '))

if dependentes == 0:
    novo_salario = salario + salario*5/100
elif dependentes == 1 or dependentes == 2 or dependentes == 3:
    novo_salario = salario + salario*10/100
elif dependentes == 4 or dependentes == 5 or dependentes == 6:
    novo_salario = salario + salario*15/100
else:
    novo_salario = salario + salario*18/100

print(f'Salario de {nome} era R${salario:.2f} e passou a ser de R${novo_salario:.2f}')'''
