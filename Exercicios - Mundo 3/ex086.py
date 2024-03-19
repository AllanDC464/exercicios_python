listaMatriz = [[], [], []]

for a in range(0, 3):
    for b in range(0, 3):
        listaMatriz[a].append(int(input(f'Digite um valor para [{a}, {b}]: ')))

for c in listaMatriz:
    for i in range(0,3):
        print(f'[ {c[i]:^5} ]', end='')
    print('')
