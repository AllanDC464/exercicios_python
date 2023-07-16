print('▬' * 41)
print('LISTAGEM DE PREÇOS'.center(41))
print('▬' * 41)

produto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

np = 0
vp = 1
rang = len(produto)
rang1 = rang / 2
for c in range(0, int(rang1)):
    print(f' {produto[np]:.<30}R${produto[vp]:>7.2f}')
    np += 2
    vp += 2

print('▬' * 41)
