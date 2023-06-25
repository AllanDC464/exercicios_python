cont = num = s = 0
while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'A soma dos {cont} valores é {s}.')
