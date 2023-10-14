listaNumeros = []
i = 0

while True:
    listaNumeros.append(int(input('Digite um valor: ')))

    if listaNumeros.count(listaNumeros[i]) != 1:
        print('\033[31m▬▬▬▬▬ Valor ja digitado ▬▬▬▬▬\033[m')
        listaNumeros.pop()
        i -= 1

    else:
        print('\033[32m▬▬▬▬▬▬ Valor adicionado ▬▬▬▬▬▬\033[m')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break 

    print('\033[36m▬\033[m' * 30)

    i += 1 

print(f'Você digitou os valores {sorted(listaNumeros)}')
