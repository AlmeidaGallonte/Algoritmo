from datetime import date

while True:
    ano_nascimento = int(input('Que anos você nasceu? '))
    if ano_nascimento > date.today().year or ano_nascimento < 1900:
        print('Data de nascimento invalida!')
    else:
        break

idade = date.today().year - ano_nascimento
print(f'Você tera que colocar {idade} velas no seu bolo! PÁRABENS!')