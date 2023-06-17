vm = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
while vm != 5:
    vm = int(input('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa \nOPÇÂO: '))
    if vm == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um valor: '))
        vm = int(input('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa'))
    elif vm == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, num1 + num2))
    elif vm == 2:
        print('O produto entre {} e {} é {}'.format(num1, num2, num1 * num2))
    elif vm == 3:
        if num1 > num2:
            print('O número {} é maior que {}'.format(num1, num2))
        else:
            print('O número {} é maior que {}'.format(num2, num1))
