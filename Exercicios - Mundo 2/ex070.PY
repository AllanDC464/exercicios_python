from time import sleep
soma = maior = menor = cont = 0
print('▬' * 28)
print('LOJA BARATÃO'.center(28))
print('▬' * 28)
while True:
    nomeproduto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    soma += preco
    print('▬' * 28)
    if preco > 1000:
        maior += 1
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        produto = nomeproduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print('▬' * 28)
print('... ENCERRANDO ...'.center(28))
sleep(3)
print('▬' * 5 ,'FIM DO PROGRAMA!', '▬' * 5)
print(f'Total gasto: R${soma:.2f}')
print(f'{maior} produtos acima de R$1000,00')
print(f'Produto mais barato, {produto} custando R${menor:.2f}')
