distancia = int(input('Qual a distancia da viagem em km: '))
if distancia > 200:
    print('\033[1;32mO valor da sua passagem é de \033[4mR${:.2f}\033[m\033[m'.format(distancia * 0.45))
else:
    print('\033[1;32mO valor da sua passagem é de \033[4mR${:.2f}\033[m\033[m'.format(distancia * 0.50))
