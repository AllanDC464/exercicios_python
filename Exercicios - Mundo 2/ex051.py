print('=' * 25)
print('10 TERMOS DE UMA PA'.center(25))
print('=' * 25)
primter = int(input('1º termo da sua PA: '))
razao = int(input('Razão da sua PA: '))
for c in range(0, 10):
    print(primter, end=' → ')
    primter += razao
print('ACABOU!')
