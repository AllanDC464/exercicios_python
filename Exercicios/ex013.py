sal = float(input('Digite seu salario atual R$'))
nsal = (15 * sal)/100
print('Voce obteve um aumento de salario de R${:.2f}, e agora recebe R${:.2f}!'.format(nsal, sal+nsal))
