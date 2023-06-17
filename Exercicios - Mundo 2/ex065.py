num = 0
cont = 0
resp = ''
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar [S/N]: '))
    num += n
    cont += 1
    if cont == 1:
        numMA = n
        numME = n
    else:
        if n > numMA:
            numMA = n
        if n < numME:
            numME = n
print('A média entre os valores digitados é de {}'.format(num/cont))
print('O maior valor digitado foi {}'.format(numMA))
print('O menor valor digitado foi {}'.format(numME))