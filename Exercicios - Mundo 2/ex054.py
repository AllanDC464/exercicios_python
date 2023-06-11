from datetime import date
anoAtu = date.today().year
smai = 0
smei = 0
for c in range(1, 8):
    anoNas = int(input('Digite o ano de nascimento: '))
    idade = anoAtu - anoNas
    if idade >= 21:
        smai += 1
    elif idade > 0:
        smei += 1
    else:
        print('Idade Invalida!')
print('{} são maiores de idade! \n{} são menores de idade!'.format(smai, smei))
