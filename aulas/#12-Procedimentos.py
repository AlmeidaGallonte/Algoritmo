#Detector de pesado
'''maior = 0
pesado = ''
def Topo():
    print('-'*30)
    print('     DETECTOR DE PESADO')
    print(f'Maior peso até agr: {maior}Kg')
    print('-'*30)

Topo()
for c in range(5):
    n = str(input('Digite seu nome: '))
    p = float(input(f'Digite o peso de {n}: '))
    if p > maior:
        maior = p
        pesado = n
        
    Topo()

Topo()
print(f'A pessoa mais pesada foi {pesado} com {maior}Kg')'''

#Passagem de parâmetro por Valor (Soma)
'''def soma(a:int=0, b:int=0):
    print(f'{a} +', end=' ')
    print(f'{b}', end=' ')
    print (f'= {a + b}')

soma(5, 3)'''

#Par ou Ímpar
'''def par_impar(n = 0):
    if n % 2 == 0:
        print(f'O valor {n} é Par')
    else:
        print(f'O valor {n} é Ímpar')

par_impar()'''

#Escopo
#local onde uma determinada variavel vai funcionar
'''def par_impar(n = 0):
    if n % 2 == 0:
        print(f'O valor {n} é Par')
    else:
        print(f'O valor {n} é Ímpar')

par_impar()
print(n)'''

#Passagem de parâmetro por referencia
'''def soma(a:int, b:int):
    a += 1
    b += 2
    print (f'Soma = {a + b}')

x = 4
y = 8
soma(x, y)
print(x, y)'''

#sequência fibonacci
'''def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)


# Exemplo para imprimir o 5º termo
print(fibonacci(9))'''
