pp = float(input('Preço do produto? R$'))
fp = int(input('[1] À vista no dinheiro/cheque \n[2] À vista no cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão \nSelecione a forma de pagamento: '))
if fp == 1:
    print('Preço do produto: {:.2f} \nValor do desconto: {:.2f} \nPreço final: {:.2f}'.format(pp, pp*10/100, pp-pp*10/100))
elif fp == 2:
    print('Preço do produto: {:.2f} \nValor do desconto: {:.2f} \nPreço final: {:.2f}'.format(pp, pp*5/100, pp-pp*5/100))
elif fp == 3:
    print('Nessa forma de pagamento não há nem descontos nem juros!')
elif fp == 4:
    print('Preço do produto: {} \nValor do juros: {} \nPreço final: {}'.format(pp, pp*20/100, pp+pp*20/100))
else:
    print('Opção invalida!')
