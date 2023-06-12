from datetime import date
anoAtu = date.today().year
smai = 0
smei = 0
for c in range(1, 8):
    anoNas = int(input('Digite o ano de nascimento: '))
    idade = anoAtu - anoNas
    if idade >= 21:
        smai += 1
    else:
        smei += 1
print('\033[32m{} são maiores de idade!\033[m \n\033[31m{} são menores de idade!\033[m'.format(smai, smei))
