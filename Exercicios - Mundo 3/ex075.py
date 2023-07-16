valor = tuple(int(input('Digite um valor: ')) for c in range(1, 5))

print(f'Você digitou os valores {valor}')

print(f'O número 9 apareceu {valor.count(9)} vezes')

if 3 in valor:
    print(f'O 3 foi digitado pela primeira vez na {valor.index(3)+1}ª posição')
else:
    print('O 3 não aparece entre os valores digitados')

print('Os valores pares digitados foram', end=' ')
for c in range(0, 4):
    if valor[c] % 2 == 0:
        print(valor[c], end=' ')
