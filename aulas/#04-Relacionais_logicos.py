#operadores relacionais
'''
 > = maior que
 < = menor que
 >= = maior ou igual a
 <= = menor ou igual a
 == = igual
 != = diferente de 
'''

a = int
b = int
c = int
a = 2
b = 3
c = 5
feliz = (not((a==b) or (c>a)))
if feliz:
    print(':)')
else:
    print(':(')

#operadores lógicos
'''
- operador and : verdadeiro quando as duas entradas são verdadeiras 
p    q    pANDq
v    v     v
v    f     f
f    v     f
f    f     f

- operador or: verdadeiro quando uma ou mais entrada for verdadeira
p    q    pORq
v    v     v
v    f     v
f    v     v
f    f     f

- operador not: inverte o valor de entrada
p    NÂO p 
v     f
f     v

EXEMPLOS:
(And)
p       q       pEq
:)      :(      :)
:)      :(      :(
:(      :)      :(
:(      :(      :(

(Or)
p       q       pOUq
:)      :(      :)
:)      :(      :)
:(      :)      :)
:(      :(      :(    

(Not)
p       Nãop
:)      :(
:(      :)

Oredem de precedência 

Aritméticos = (), **, * or /, + or -  
Relacionais = All
Lógicos = and, or, not

'''

