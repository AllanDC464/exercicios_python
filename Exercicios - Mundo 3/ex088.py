from random import randint
from time import sleep
jogosSorteados = []
temp = []

print('▬' * 44)
print('JOGA NA MEGA SENA'.center(44))
print('▬' * 44)

numeroDeSorteios = int(input('Quantos jogos você quer que eu sorteie?'.center(42)))
print('-='*6, end='')
print(f'SORTEANDO {numeroDeSorteios} JOGOS'.center(20), end='')
print('=-'*6)
print('')

for c in range(0, numeroDeSorteios):
    for c in range(0, 6):
        temp.append(randint(1, 60))
    i = 0
    for c in temp:
        while temp.count(temp[i]) != 1:
            temp.pop()
            temp.append(randint(1, 60))
        i +=1
    jogosSorteados.append(temp[:])
    temp.clear()

b = 0
for c in jogosSorteados:
    print(f'Jogo {b+1}: {sorted(jogosSorteados[b])}')
    sleep(1)
    b += 1
