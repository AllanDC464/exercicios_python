from random import randint

numeroAleatorio = tuple(randint(1, 10) for c in range(1, 6))
print('Os valores sorteados foram:', end=' ')
for c in range(0, len(numeroAleatorio)):
    print(numeroAleatorio[c], end=' ')
print(f'\nO menor número sorteado foi {min(numeroAleatorio)}')
print(f'O maior número sorteado foi {max(numeroAleatorio)}')
print('▬' * 40)


numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteador foi {min(numeros)}')
print(f'O maior valor sorteador foi {max(numeros)}')
