lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continura? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

i = 0
for c in lista:
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
    i += 1

print('>=<' * 20)

print(f'\033[31mLista completa | {lista}\033[m')

if len(pares) != 0:
    print(f'\033[33mLista somente com valores PARES | {pares}\033[m')
else:
    print('\033[33mNão foram digitados valores PARES!\033[m')

if len(impares) != 0:
    print(f'\033[32mLista somente com valores IMPARES | {impares}\033[m')
else:
    print('\033[32mNão foram digitados valores IMPARES!\033[m')
