from random import randint
player = int(input('[1] Pedra \n[2] Papel \n[3] Tesoura \nEscolha uma opção: '))
pc = randint(1, 3)
if player == 1 and pc == 2:
    print('Você perdeu')
elif player == 1 and pc ==3:
    print('Você ganhou')
elif player == 2 and pc == 1:
    print('Você ganhou')
elif player == 2 and pc == 3:
    print('Você perdeu')
elif player == 3 and pc == 1:
    print('Você perdeu')
elif player == 3 and pc == 2:
    print('Você ganhou')
elif player == pc:
    print('Empatou')
else:
    print('Opção invalida! \nTente outra opção!')
    