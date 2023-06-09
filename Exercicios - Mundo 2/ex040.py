n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('Sua média foi de {:.1f} você esta \033[31mREPROVADO\033[m!'.format(m))
elif m >= 5.0 and m < 7.0:
    print('Sua média foi de {:.1f} você esta de \033[33mRECUPERAÇÃO\033[m!'.format(m))
else:
    print('Sua média foi de {:.1f} você esta \033[34mAPROVADO\033[m!'.format(m))
