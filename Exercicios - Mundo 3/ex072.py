contagemZeroAVinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
'Dezenove', 'Vinte')

while True:
    while True:
        número = int(input('Digite um número entre 0 e 20: '))
        if 0 <= número <= 20:
            break
        print('Número invalido!')
    print(f'O número \033[32;4m{número}\033[m por extenso é \033[32;4m{contagemZeroAVinte[número]}\033[m')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
