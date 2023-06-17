primter = int(input('1° termo da PA: '))
razao = int(input('Razão da PA: '))

c = 0
while c < 10:
    c += 1
    print(primter, end=' → ')
    primter += razao
print('ACABOU!')
print('')



maister = 0
maiste = 1
while maiste != 0:
    maiste = int(input('Deseja ver mais termos? \nSe não digite 0 \nSe sim Quantos: '))
    maister += maiste
    while c < 10 + maister:
        print(primter, end=' → ')
        primter += razao
        c += 1
