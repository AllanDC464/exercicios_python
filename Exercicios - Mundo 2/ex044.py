pp = float(input('Preço do produto? R$'))
fp = int(input('[ 1 ] À vista no dinheiro/cheque \n[ 2 ] À vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão \nSelecione a forma de pagamento: '))
print('Preço das compras: {:.2f}'.format(pp))
if fp == 1:
    print('Valor do desconto: {:.2f} \nPreço final: {:.2f}'.format(pp*10/100, pp-pp*10/100))
elif fp == 2:
    print('Valor do desconto: {:.2f} \nPreço final: {:.2f}'.format(pp*5/100, pp-pp*5/100))
elif fp == 3:
    print('Sua compra ficou e 2x de R${:.2f}'.format(pp/2))
elif fp == 4:
    parcelas =int(input('Quantas parcelas? '))
    print('Sua compra será parcelas em {}x de R${:.2f} com juros'.format(parcelas, (pp+pp*20/100)/parcelas))
    print('Valor do juros: {:.2f} \nPreço final: {:.2f}'.format(pp*20/100, pp+pp*20/100))
else:
    print('Opção invalida!')
