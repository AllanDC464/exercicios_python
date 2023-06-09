vc = float(input('Valor da casa: R$'))
sal = float(input('Sálario do comprador: R$'))
tpp = int(input('Em quantos anos deseja pagar: '))
v = sal * 30 / 100
vp = vc / (tpp * 12)
if vp <= v:
    print('\033[32mEmprestimo aprovado!\033[m')
else:
    print('\033[31mEmprestimo negado!\033[m')
