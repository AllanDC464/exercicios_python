listaNumeros = [[],[]]

for c in range (1, 8):
    numeros = int(input(f'Digite o {c}º valor: '))
    if numeros % 2 == 0:
        listaNumeros[1].append(numeros)
    else:
        listaNumeros[0].append(numeros)

print(f'Os valores ímpares digitados foram: {sorted(listaNumeros[0])}')
print(f'Os valores pares digitados foram: {sorted(listaNumeros[1])}')
