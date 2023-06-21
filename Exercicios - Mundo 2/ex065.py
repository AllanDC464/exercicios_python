num = cont = 0
resp = ''
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar [S/N]: '))
    num += n
    cont += 1
    if cont == 1:
        numMA = numME = n
    else:
        if n > numMA:
            numMA = n
        if n < numME:
            numME = n
print('Você digitou \033[4;32m{}\033[m números e a média foi \033[4;32m{}\033[m'.format(cont, num/cont))
print('O maior valor foi \033[4;32m{}\033[m e o menor foi \033[4;32m{}\033[m'.format(numMA, numME))
