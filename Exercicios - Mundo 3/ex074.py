from random import randint

numeroAleatorio = tuple(randint(1, 9) for c in range(1, 6))

print('Os valores sorteados foram:', end=' ')
for c in range(0, len(numeroAleatorio)):
    print(numeroAleatorio[c], end=' ')
print('')

numeroOrganizado = sorted(numeroAleatorio)
print(f'O menor número sorteado foi {numeroOrganizado[0]}')
print(f'O maior número sorteado foi {numeroOrganizado[-1]}')
