from time import sleep
vm = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
while vm != 5:
    vm = int(input('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa \n→ OPÇÂO: '))
    if vm == 1:
        print('=-=' * 10)
        print('\033[32mA soma entre {} e {} é {}\033[m'.format(num1, num2, num1 + num2))
        print('=-=' * 10)
    elif vm == 2:
        print('=-=' * 10)
        print('\033[32mO produto entre {} e {} é {}\033[m'.format(num1, num2, num1 * num2))
        print('=-=' * 10)
    elif vm == 3:
        if num1 > num2:
            print('=-=' * 10)
            print('\033[32mO número {} é maior que {}\033[m'.format(num1, num2))
            print('=-=' * 10)
        else:
            print('=-=' * 10)
            print('\033[32mO número {} é maior que {}\033[m'.format(num2, num1))
            print('=-=' * 10)
    elif vm == 4:
            print('Informe novamente os valores.')
            num1 = int(input('Digite um valor: '))
            num2 = int(input('Digite um valor: '))
    elif vm == 5:
        print('\033[4;32mFINALIZANDO...\033[m')
        sleep(2)
    elif vm > 5:
        print('=-=' * 10)
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
        print('=-=' * 10)
print('\033[4;32mFIM DO PROGRAMA! VOLTE SEMPRE!\033[m')
