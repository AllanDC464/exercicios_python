sal = float(input('\033[37mQual é o salário do funcionario? R$'))
if sal <= 1250.00:
    print('\033[4;31mSalario atual: {:.2f}\033[m \n\033[4;33mValor do aumento: {:.2f}\033[m \n\033[4;32mSalario final: {:.2f}\033[m'.format(sal, sal*15/100, sal+sal*15/100))
else:
    print('\033[4;31mSalario atual: {:.2f}\033[m \n\033[4;33mValor do aumento: {:.2f}\033[m \n\033[4;32mSalario final: {:.2f}\033[m'.format(sal, sal*10/100, sal+sal*10/100))
