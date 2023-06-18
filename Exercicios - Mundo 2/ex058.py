from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 10)
print('\033[1;34m... Pensando em um número ...\033[m')
print('\033[33m-=-\033[m' * 10)
pc = randint(0, 10)
sleep(2)
print('\033[1;31mPensei em um número entre 0 e 10, adivinhe se puder! \033[m')
cont = 0
player = ''
while player != pc:
    cont += 1
    player = int(input('\033[1;32mQual seu palpite?\033[m '))
    if player < pc:
        print('Mais... Tente mais uma vez.')
    elif player > pc:
        print('Menos... Tente mais uma vez.')
print('\033[32mVocê acertou!\033[m \nForam necessárias \033[1;4m{} tentativas.\033[m'.format(cont))
