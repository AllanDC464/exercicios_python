from calendar import isleap
from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto: '))
print(isleap(ano))

if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} \033[1;4;32mÉ Bissexto\033[m'.format(ano))
else:
    print('O ano {} \033[1;4;31mNão é bissexto\033[m'.format(ano))
