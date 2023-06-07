pp = float(input('Digite o preço do produto R$ '))
vcd = (5 * pp) /100
print('O valor do seu desconto será de R${:.2f}.\nO valor final com desconto será de R${:.2f}'.format(vcd, pp-vcd))
