from random import randint
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
cont = 0
while True:
    pc = randint(1, 10)
    print('=-=' * 10)
    num = int(input('Diga um valor: '))
    parImpar = str(input('Par ou ímpar? [P/I] '))
    soma = num + pc
    print('▬' * 30)
    if soma % 2 == 0 and parImpar in 'Pp':
        print(f'Você jogou {num} e o computador {pc}. Total de {soma} DEU PAR')
        cont += 1
    elif soma % 2 != 0 and parImpar in 'Ii':
        print(f'Você jogou {num} e o computador {pc}. Total de {soma} DEU ÍMPAR')
        cont += 1
    else:
        if soma % 2 == 0:
            print(f'Você jogou {num} e o computador {pc}. Total de {soma} DEU PAR')
        elif soma % 2 != 0:
            print(f'Você Jogou {num} e o computador {pc}. Total de {soma} DEU ÍMPAR')
        print('Você PERDEU!')
        print('=-=' * 10)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    print('▬' * 30)
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
