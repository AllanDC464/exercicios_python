s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Você informou \033[4;32m{}\033[m valores pares e a soma entre eles é \033[4;32m{}\033[m'.format(cont, s))
