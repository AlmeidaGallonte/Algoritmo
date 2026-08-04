valor_emprestimo = float(input('Valor do empréstimo: R$'))
parcelas = int(input('Quantas parcelas: '))
acrecimo = valor_emprestimo * 20 / 100
valor_total = valor_emprestimo + acrecimo
valor_parcelas = valor_total / parcelas
print(f'Empréstimo = R${valor_emprestimo:.2f}\nParcelas = {parcelas}\nacrécimo(20%) = {acrecimo:.2f}\nValor total = R${valor_total:.2f}\nValor a pagar mensais = R${valor_parcelas:.2f}')

