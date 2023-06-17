from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 10)
print('\033[1;34m... Pensando em um número ...\033[m')
print('\033[33m-=-\033[m' * 10)
rand = randint(0, 11)
sleep(2)
num = int(input('\033[1;31mPensei em um número entre 0 e 5, adivinhe se puder: \033[m'))
cont = 1
while num != rand:
    print('Você errou, tente novamente!')
    num = int(input('\033[1;31mPensei em um número entre 0 e 5, adivinhe se puder: \033[m'))
    cont += 1
print('\033[32mVocê acertou!\033[m \nForam necessárias \033[1;4m{} tentativas.\033[m'.format(cont))




"""if num == rand:
    sleep(1)
    print('\033[1;32mVocê acertou!\033[m')
else:
    sleep(1)
    print('\033[1;31mVocê errou\033[m, o número em que pensei foi \033[1;32m{}\033[m e não \033[1;31m{}\033[m'.format(rand, num))"""
