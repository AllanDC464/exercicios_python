contagemZeroAVinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

número = int(input('Digite um número entre 0 e 20: '))

while True:
    if número < 0 or número > 20:
       print('Número invalido!')
       número = int(input('Digite um número entre 0 e 20: '))
    else:
        print(f'O número \033[32;4m{número}\033[m por extenso é \033[32;4m{contagemZeroAVinte[número]}\033[m')
        break
