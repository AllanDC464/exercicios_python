m = 0
nmv = ''
idmv = 0
mnv = 0
for c in range(1, 5):
    print('▬▬▬▬▬▬▬ {}° PESSOA ▬▬▬▬▬▬▬'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: '))
    m += idade
    med = m / 4
    if c == 1 and sexo in 'Mm':
        nmv = nome
        idmv = idade
    if sexo in 'Mm' and idade > idmv:
            nmv = nome
            idmv = idade
    if sexo in 'Ff' and idade < 20:
            mnv += 1
print('A média de idade do grupo é de {} anos.'.format(med))
print('A idade do homem mais velho é {} e ele se chama {}.'.format(idmv, nmv))
print('A {} mulheres com menos de 20 anos.'.format(mnv))
