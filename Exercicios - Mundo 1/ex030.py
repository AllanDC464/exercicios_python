num = int(input('\033[35mDigite um número:\033[m '))
if num % 2 == 0:
    print('{} é um número \033[1;34mPAR\033[m'.format(num))
else:
    print('{} é um número \033[1;34mIMPAR\033[m'.format(num))