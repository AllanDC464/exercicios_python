n = 0
num = 0
cont = -1
while n != 999:
    cont += 1
    num += n
    n = int(input('Digite um número: '))
print('Foram digitados {} números \nA soma entre os números digitados é {}'.format(cont, num))
