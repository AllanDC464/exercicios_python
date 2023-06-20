from time import sleep

print('\033[32m-=-\033[m' * 7)
print('GERADOR DE PA'.center(21))
print('\033[32m-=-\033[m' * 7)

print('')
termo = int(input('1° termo da PA: '))
razao = int(input('Razão da PA: '))
print('')

c = 0
while c < 10:
    c += 1
    print(termo, end=' → ')
    termo += razao
print('PAUSA')
print('')

maister = 0
mais = 1
cont = 10
while mais != 0:
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('')
    maister += mais
    while c < 10 + maister:
        print(termo, end=' → ')
        termo += razao
        c += 1
        cont += 1
    if mais != 0:
        print('PAUSA')
        print('')

print('Foram mostrados {} termos.'.format(cont))
print('ENCERRANDO PROGRAMA...')
sleep(2)
print('PROGRAMA ENCERRADO')
