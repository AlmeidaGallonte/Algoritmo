n1 = int(input('n1: '))
n2 = int(input('n2: '))
m = (n1 + n2) / 2
print(f'A média de {n1} e {n2} = {m}')

a = 5
b = 2

adição = '+'
print(a+b)
subtração = '-'
print(a-b)
multiplicação = '*'
print(a*b)
divisão = '/'
print(a/b)
divisão_inteira = '//'
print(a//b)
exponenciação = '**'
print(a**b)
módulo = '%'
print(a%b)

#ordem de precedência
'''
parênteses ()
exponenciação **
multiplicação ou divisão * ou /
adção ou subtração + ou -

'''

#funçoes aritméticas
import math
print(abs(-10),
9**5,
int(3.9),
math.sqrt(25),
math.pi,
math.sin(0.523),
math.cos(0.523),
math.tan(0.523),
math.radians(30),
)
'''
abs =  valor absoluto
** = exponenciação
int = valor inteiro
sqrt = raiz quadrada
pi =  retorna pi
sin = seno (rad)
cos = cosseno (rad)
tan = tangente (rad)
radians = graus pra rad 
'''


angulo = int(input('informe um angulo: '))
s:float = math.sin(math.radians(angulo))
print(f'O seno de {angulo} é igual a {s}')


