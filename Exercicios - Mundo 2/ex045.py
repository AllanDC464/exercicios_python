from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
Jogador = int(input('[1] Pedra \n[2] Papel \n[3] Tesoura \nQual sua jogada? '))
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[Jogador]))
if pc == 0:
    if Jogador == 0:
        print('EMPATE')
    elif Jogador == 1: 
        print('Jogador VENCEU')
    elif Jogador == 2:
        print('Computador VENCEU')
    else:
        print('Jogada INVALIDA')
elif pc == 1:
    if Jogador == 0:
        print('Computador VENCE')
    elif Jogador == 1:
        print('EMPATE')
    elif Jogador == 2:
        print('Jogador VENCE')
    else:
        print('Jogada INVALIDA')
elif pc == 2:
    if Jogador == 0:
        print('Jogador VENCE')
    elif Jogador == 1:
        print('Computador VENCE')
    elif Jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVALIDA')
