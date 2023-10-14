lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

organizado = sorted(lista)
print(f'Foram digitados {len(lista)} números')
print(f'Os valores em ordem decrescente são {list(reversed(organizado))}')

if lista.count(5) != 0:
    print(f'\033[32mO valor 5 foi encontrado na lista {lista.count(5)} vezes!\033[m')
else:
    print('\033[31mO valor 5 não foi encontrado na lista!\033[m')
