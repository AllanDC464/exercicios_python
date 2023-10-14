valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'Você digitou os valores {valores}')

i = p = 0
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for c in valores:
    if valores[i] == max(valores):
        print(f'{p+1}', end='... ')
    i += 1
    p += 1

i = p = 0
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c in valores:
    if valores[i] == min(valores):
        print(f'{p+1}', end='... ')
    i += 1
    p += 1
