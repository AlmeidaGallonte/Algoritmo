#Detector de pesado
maior = 0
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
print(f'A pessoa mais pesada foi {pesado} com {maior}Kg')

    