m = 0
nmv = ''
idmv = ''
mnv = 0
for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = int(input('[ 1 ] HOMEM \n[ 2 ] MULHER \nSua opção: '))
    m += idade
    med = m / 4
    if c == 1:
        nmv = nome
        idmv = idade
    else:
        if sexo == 1 and idade > idmv:
            nmv = nome
        if sexo == 2 and idade < 20:
            mnv += 1
print('A média de idade do grupo é de {:.0f} anos.'.format(med))
print('O nome do homem mais velho é {}.'.format(nmv))
print('A {} mulheres com menos de 20 anos.'.format(mnv))
