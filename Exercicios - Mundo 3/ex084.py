pessoas = []
dados = []
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi de {maiorPeso}Kg.', end=' Peso de ')
for p in pessoas:
    if maiorPeso == p[1]:
        print(f'[{p[0]}]', end=' ')
print('')

print(f'O menor peso cadastrado foi de {menorPeso}Kg.', end=' Peso de ')
for p in pessoas:
    if menorPeso == p[1]:
        print(f'[{p[0]}]', end=' ')
print('')
