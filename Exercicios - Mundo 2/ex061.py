print('=' * 25)
print('10 TERMOS DE UMA PA'.center(25))
print('=' * 25)
primter = int(input('1° termo da PA: '))
razao = int(input('Razão da PA: '))

c = 0
while c < 10:
    c += 1
    print(primter, end=' → ')
    primter += razao
print('ACABOU!')