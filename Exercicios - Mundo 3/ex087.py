listaMatriz = [[], [], []]

for a in range(0, 3):
    for b in range(0, 3):
        listaMatriz[a].append(int(input(f'Digite um valor para [{a}, {b}]: ')))
print('-=-' * 12)

somaPares = somaTerceiraColuna = 0
for c in listaMatriz:
    for i in range(0, 3):
        print(f'[{c[i]:^5}]', end='')
        if c[i] % 2 == 0:
            somaPares += c[i]
        if i == 2:
            somaTerceiraColuna += c[i]
    print('')
print('-=-' * 12)

print(f'A soma dos valores pares é de {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {max(listaMatriz[1])}.')
